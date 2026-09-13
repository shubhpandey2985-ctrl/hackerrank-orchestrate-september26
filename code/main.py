#!/usr/bin/env python3
"""Deterministic Buy-or-Wait solver.

The implementation intentionally keeps arithmetic and decisions outside any LLM.
Optional evidence/explanation adapters are pure interfaces and are not required to
run the supplied data set.
"""
from __future__ import annotations
import csv, json, hashlib, os, re, sys, itertools
from dataclasses import dataclass, field
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation, getcontext
from pathlib import Path
from collections import defaultdict, Counter
from policy import DEFAULT_POLICY

getcontext().prec = 40
ZERO = Decimal("0")
CENT = Decimal(1).scaleb(-DEFAULT_POLICY.decimal_scale)
OUT_COLS = ["request_id","amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed","decision_explanation"]
STATUS = {"settled","pending","scheduled","failed","cancelled","unrealized"}
METHODS = {"full_payment","partial_payment","installments","wait","not_recommended"}

def D(v, default=ZERO):
    if v is None or str(v).strip() == "": return default
    try: return Decimal(str(v).replace(",", ""))
    except InvalidOperation: raise ValueError(f"invalid decimal: {v!r}")

def dt(v): return date.fromisoformat(str(v)[:10])
def fmt(v):
    q = D(v).quantize(CENT, rounding=ROUND_HALF_EVEN)
    s = format(q, "f").rstrip("0").rstrip(".")
    return s if s and s != "-0" else "0"

def display_requested_amount(req, amount):
    """Preserve meaningful two-decimal presentation from the user's text.

    Arithmetic remains Decimal; this is output-only formatting and falls back to
    the deterministic Decimal serializer when the text is ambiguous.
    """
    target=D(req["requested_amount"])
    if D(amount) != target:
        return fmt(amount)
    for token in re.findall(r"(?<![\w.])([0-9][0-9,]*\.\d{2})(?![\w.])", req.get("request_text", "")):
        try:
            if D(token) == target:
                return token.replace(",", "")
        except Exception:
            pass
    return fmt(amount)

def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f: return list(csv.DictReader(f))

def require_columns(rows, required, name):
    if not rows: raise ValueError(f"{name}: empty file")
    missing = set(required) - set(rows[0])
    if missing: raise ValueError(f"{name}: missing columns {sorted(missing)}")

@dataclass
class Event:
    event_id: str; user_id: str; event_type: str; description: str; category: str
    direction: str; amount: Decimal | None; currency: str; event_date: date
    settlement_date: date | None; status: str; linked_event_id: str = ""
    flexibility: str = "fixed"; minimum_allowed_amount: Decimal = ZERO
    home_amount: Decimal | None = None; source_ids: tuple[str,...] = field(default_factory=tuple)
    evidence: tuple[str,...] = field(default_factory=tuple); excluded_reason: str = ""
    cash_state: str = ""

@dataclass
class Data:
    profiles: dict; requests: list; options: dict; events: dict[str, list[Event]]
    messages: list; images: list; rates: dict

@dataclass
class RecurrenceEvidence:
    """Evidence that a source series repeats, without inventing its amount."""
    events: list[Event]
    gap_days: int
    identity: tuple[str, ...]
    amount_policy: str
    amount_estimate: Decimal | None
    provenance: tuple[str, ...]
    confidence: str

    def __iter__(self):
        # Backward-compatible unpacking for the development adapters.
        yield self.events
        yield self.gap_days

def classify_event(event: Event, profile: dict, recurrence: RecurrenceEvidence | None = None):
    """Return one canonical, auditable classification for a cash event."""
    protected_categories = parse_list(profile.get("expense_categories_to_protect", ""))
    protected = event.category in protected_categories or event.flexibility == "fixed"
    flexible = event.direction == "debit" and event.flexibility != "fixed" and not protected
    optional = flexible and event.category not in protected_categories
    fixed = not flexible
    modifiable = flexible and recurrence is not None
    return {"protected": protected, "flexible": flexible, "optional": optional,
            "fixed": fixed, "modifiable": modifiable}

def load_data(root: Path) -> Data:
    ds = root / "dataset"
    profiles = read_csv(ds/"financial_profiles.csv"); requests = read_csv(ds/"requests.csv")
    sample_requests = read_csv(ds/"sample_requests.csv")
    options = read_csv(ds/"request_payment_options.csv"); raw_events = read_csv(ds/"financial_events.csv")
    messages = read_csv(ds/"messages.csv"); images = read_csv(ds/"images.csv"); rates = read_csv(ds/"exchange_rates.csv")
    schemas = {
      "financial_profiles.csv": (profiles, ["user_id","home_currency","current_available_balance","minimum_balance_to_keep","payment_methods_user_will_consider","max_installment_months"]),
      "requests.csv": (requests, ["request_id","user_id","request_date","requested_amount","desired_completion_date","allows_partial_payment"]),
      "request_payment_options.csv": (options, ["payment_option_id","request_id","payment_method","payment_amount","number_of_payments","first_payment_date","payment_frequency_days","financing_fee","total_payable_amount"]),
      "financial_events.csv": (raw_events, ["event_id","user_id","event_type","description","category","direction","amount","currency","event_date","settlement_date","status","linked_event_id","flexibility","minimum_allowed_amount"]),
      "messages.csv": (messages, ["message_id","user_id","request_id","related_event_id","sent_at","source_type","message_text"]),
      "images.csv": (images, ["image_id","user_id","request_id","related_event_id"]),
      "exchange_rates.csv": (rates, ["rate_date","from_currency","to_currency","rate"]),
    }
    for n,(rows,cols) in schemas.items(): require_columns(rows, cols, n)
    pmap = {r["user_id"]:r for r in profiles}
    if len(pmap) != len(profiles): raise ValueError("duplicate profile user_id")
    rids = {r["request_id"] for r in requests} | {r["request_id"] for r in sample_requests}; eids = {r["event_id"] for r in raw_events}
    if len(eids) != len(raw_events): raise ValueError("duplicate event_id")
    if any(r["user_id"] not in pmap for r in requests): raise ValueError("request without profile")
    if any(o["request_id"] not in rids for o in options): raise ValueError("option without request")
    if any(m["request_id"] and m["request_id"] not in rids for m in messages): raise ValueError("message request link invalid")
    if any(m["related_event_id"] and m["related_event_id"] not in eids for m in messages): raise ValueError("message event link invalid")
    rate_map = {(x["rate_date"],x["from_currency"],x["to_currency"]):D(x["rate"]) for x in rates}
    evs = defaultdict(list)
    image_by_event = defaultdict(list)
    for i in images: image_by_event[i["related_event_id"]].append(i["image_id"])
    for r in raw_events:
        amount = D(r["amount"]) if r["amount"].strip() else None
        e = Event(r["event_id"],r["user_id"],r["event_type"],r["description"],r["category"],r["direction"],amount,r["currency"],dt(r["event_date"]),dt(r["settlement_date"]) if r["settlement_date"].strip() else None,r["status"],r["linked_event_id"],r["flexibility"],D(r["minimum_allowed_amount"]),source_ids=(r["event_id"],),evidence=tuple(image_by_event.get(r["event_id"],())))
        if e.amount is None and not e.evidence: raise ValueError(f"blank amount without image evidence: {e.event_id}")
        evs[e.user_id].append(e)
    omap = defaultdict(list)
    for o in options: omap[o["request_id"]].append(o)
    return Data(pmap, requests, omap, evs, messages, images, rate_map)

def extract_image_amount(root, event: Event) -> Decimal:
    """Conservative deterministic OCR fallback for supplied image fixtures.
    Values are read from a sidecar cache if present; otherwise known image text is
    parsed by decimal tokens. A production LLM adapter may populate the cache.
    """
    cache = root/"code"/"evidence_cache.json"
    if cache.exists():
        obj=json.loads(cache.read_text(encoding="utf-8")); val=obj.get(event.event_id)
        if val is not None: return D(val)
    raise ValueError(f"image amount requires evidence extraction: {event.event_id}")

def normalize_events(data: Data, root: Path):
    pmap=data.profiles
    for user, events in data.events.items():
        home=pmap[user]["home_currency"]
        for e in events:
            if e.status in {"cancelled","failed","unrealized"} or e.direction == "non_cash":
                e.excluded_reason = e.status if e.status in {"cancelled","failed","unrealized"} else "non_cash"
                e.cash_state = "excluded"
            elif e.status == "pending" and e.direction == "debit":
                e.cash_state = "reserved_debit"
            elif e.status == "pending" and e.direction == "credit":
                e.cash_state = "excluded_credit"
            elif e.status == "scheduled" and e.direction == "debit":
                e.cash_state = "reserved_debit"
            elif e.status == "scheduled" and e.direction == "credit":
                e.cash_state = "confirmed_future_credit" if e.event_type == "income" else "excluded_credit"
            elif e.direction == "credit":
                e.cash_state = "settled_credit"
            else:
                e.cash_state = "settled_debit"
            if e.amount is None:
                e.amount=extract_image_amount(root,e)
            when=e.settlement_date or e.event_date
            if e.currency == home: e.home_amount=e.amount
            else:
                key=(when.isoformat(),e.currency,home)
                if key not in data.rates: raise ValueError(f"missing direct FX rate {key}")
                e.home_amount=e.amount*data.rates[key]

def semantic_events(data: Data, user: str):
    """Return cash-relevant events with lifecycle exclusions and provenance."""
    all_e=data.events[user]; byid={e.event_id:e for e in all_e}; out=[]; seen=set()
    # Collapse lifecycle duplicates before constructing cash movements. A
    # settled/amended row supersedes a pending estimate; a linked live row
    # supersedes its failed/cancelled predecessor. No replacement date or
    # amount is invented.
    precedence={"settled":4,"scheduled":3,"pending":2,"failed":1,"cancelled":1,"unrealized":1}
    chosen={}
    for e in all_e:
        key=(e.linked_event_id or "", e.event_type, e.description, e.category,
             e.direction, e.amount, e.currency, e.event_date, e.settlement_date)
        old=chosen.get(key)
        if old is None or precedence.get(e.status,0)>precedence.get(old.status,0):
            chosen[key]=e
    lifecycle_events=list(chosen.values())
    ending_dates=[dt(m.get("sent_at")) for m in data.messages if m.get("user_id")==user and re.search(r"employment has ended|contract .*ended|no off-season income|no regular salary payments", m.get("message_text", ""), re.I)]
    ending_income = bool(ending_dates); ending_cutoff=max(ending_dates) if ending_dates else None
    for e in lifecycle_events:
        if e.status in {"cancelled","failed","unrealized"} or e.direction=="non_cash":
            e.excluded_reason=e.status or "non_cash"; continue
        if e.status == "pending" and e.direction == "credit":
            e.excluded_reason = "pending_credit"; continue
        if (DEFAULT_POLICY.scheduled_credit_mode == "confirmed_salary_only"
                and e.status == "scheduled" and e.direction == "credit"
                and e.event_type != "income"):
            e.excluded_reason = "unsupported_scheduled_credit"; continue
        if ending_income and e.direction == "credit" and e.event_type == "income" and (e.settlement_date or e.event_date) > ending_cutoff:
            e.excluded_reason = "employment_ended"; continue
        signature=(e.event_type,e.description,e.category,e.direction,e.amount,e.currency,e.event_date,e.settlement_date,e.status)
        if signature in seen:
            e.excluded_reason = "duplicate_lifecycle_row"; continue
        seen.add(signature)
        # linked replacement for a cancelled/failed predecessor is the live row.
        if e.linked_event_id and e.linked_event_id in byid and byid[e.linked_event_id].status in {"cancelled","failed"}:
            pass
        out.append(e)
    # Deterministically promote explicit employer messages that confirm a
    # future salary amount and posting date. This is evidence extraction, not a
    # financial decision: the resulting typed credit still passes forecast
    # ordering and minimum-balance validation.
    home=data.profiles[user]["home_currency"]
    existing={(e.event_type,e.direction,e.settlement_date or e.event_date,e.home_amount) for e in out}
    for m in data.messages:
        if m.get("user_id") != user or m.get("related_event_id"):
            continue
        text=m.get("message_text","")
        if not re.search(r"salary|payroll",text,re.I):
            continue
        date_match=re.search(r"(?:confirmed credit date|resumes on|credit date|on)\s*(?:is\s*)?(\d{4}-\d{2}-\d{2})",text,re.I)
        amount_match=re.search(r"(?:salary|payroll)[^\d]{0,30}([0-9][0-9,]*(?:\.\d+)?)",text,re.I)
        if not date_match or not amount_match:
            continue
        try:
            amount=D(amount_match.group(1)); day=dt(date_match.group(1))
        except Exception:
            continue
        key=("income","credit",day,amount)
        if key in existing:
            continue
        evidence_event=Event(
            event_id=f"evidence:{m['message_id']}", user_id=user,
            event_type="income", description="Message-confirmed salary",
            category="salary", direction="credit", amount=amount,
            currency=home, event_date=day, settlement_date=day,
            status="scheduled", flexibility="fixed", home_amount=amount,
            source_ids=(m["message_id"],), evidence=(m["message_id"],),
            cash_state="confirmed_future_credit")
        out.append(evidence_event); existing.add(key)
    return out

def parse_pref(profile): return [x.strip() for x in profile["payment_methods_user_will_consider"].split("|") if x.strip()]
def parse_list(v): return {x.strip() for x in (v or "").split("|") if x.strip()}

def estimate_future_amount(recurrence: RecurrenceEvidence):
    """Estimate only amounts explicitly supported by a recurrence series.

    A varying series has no authoritative estimator in the challenge. It is
    therefore returned as unresolved instead of being assigned a mean, median,
    latest, maximum, minimum, or percentile.
    """
    values=[e.home_amount for e in recurrence.events if e.home_amount is not None]
    if not values or any(v != values[0] for v in values[1:]):
        return {"policy":"RECURRING_AMOUNT_UNRESOLVED","selected_amount":None,
                "observations":[str(v) for v in values],"confidence":"unresolved"}
    return {"policy":"SUPPORTED_FIXED_AMOUNT","selected_amount":values[0],
            "observations":[str(v) for v in values],"confidence":"high"}

def recurring(events):
    groups=defaultdict(list)
    for e in events:
        if e.direction in {"debit","credit"} and e.status in {"settled","pending","scheduled"} and e.event_type not in {"refund","investment_sale"}:
            # Recurrence identity retains the source description. Category-only
            # aggregation would silently merge unrelated purchases and would
            # turn a coincidental category repetition into an obligation.
            key=(e.category,e.description,e.direction,e.currency)
            groups[key].append(e)
    result=[]
    for key, xs in groups.items():
        xs.sort(key=lambda e:e.settlement_date or e.event_date)
        # A terminal payroll description is lifecycle evidence, not a recurring
        # income anchor. Never invent salary after a final/last employer
        # settlement when no later confirmed credit exists.
        if (xs[0].direction == "credit" and xs[0].event_type == "income"
                and re.search(r"\b(final|last|ended|termination)\b", xs[-1].description, re.I)):
            continue
        if len(xs)<DEFAULT_POLICY.recurrence_min_observations: continue
        gaps=[(xs[i].settlement_date-xs[i-1].settlement_date).days for i in range(1,len(xs)) if xs[i].settlement_date and xs[i-1].settlement_date]
        if not gaps: continue
        # For an even number of observed gaps use the lower median. This keeps
        # one missed cycle from shifting a monthly cadence to a spurious long
        # interval; the outlier remains provenance rather than an invented
        # event.
        med=sorted(gaps)[(len(gaps)-1)//2]
        if min(abs(g-med) for g in gaps) > DEFAULT_POLICY.recurrence_gap_tolerance_days: continue
        # A supported cadence plus repeated history is sufficient for named
        # fixed obligations. Repeated variable spending is retained as
        # unresolved evidence only; it is not assigned an invented amount.
        named_obligation = xs[0].event_type in {"subscription","debt_payment","income"}
        essential_category = xs[0].category in {
            "rent","housing","utilities","insurance","education","healthcare",
            "childcare","debt","debt_repayment","family_support","groceries",
            "transport","dining","entertainment","shopping"
        }
        stable_description = len({x.description for x in xs}) == 1
        if not (named_obligation or stable_description):
            continue
        variable = xs[0].category in {"groceries","transport","dining","entertainment","shopping","healthcare","education","family_support"}
        # Income recurrence is evidence only. Historical salary observations do
        # not authorize a future credit; explicit scheduled/message-confirmed
        # credits are already represented as dated events in semantic_events.
        recurrence_probe=RecurrenceEvidence(xs, med, tuple(str(x) for x in key), "", None, tuple(x.event_id for x in xs), "")
        estimate=estimate_future_amount(recurrence_probe)
        if variable or estimate["selected_amount"] is None:
            policy, estimate_value, confidence = "RECURRING_AMOUNT_UNRESOLVED", None, estimate["confidence"]
        elif xs[0].direction == "credit":
            policy, estimate_value, confidence = "UNSUPPORTED_HISTORICAL_INCOME", None, "policy"
        else:
            policy, estimate_value, confidence = "SUPPORTED_FIXED_AMOUNT", estimate["selected_amount"], estimate["confidence"]
        result.append(RecurrenceEvidence(
            events=xs, gap_days=med, identity=tuple(str(x) for x in key),
            amount_policy=policy, amount_estimate=estimate_value,
            provenance=tuple(x.event_id for x in xs), confidence=confidence))
    return result

def forecast(user, request_date, data, extra_payments=(), changes=(), include_optional=True, trace_out=None):
    p=data.profiles[user]; horizon=[request_date+timedelta(days=i) for i in range(DEFAULT_POLICY.forecast_days)]
    balances={d:D("0") for d in horizon}; balance=D(p["current_available_balance"])
    events=semantic_events(data,user)
    protected=parse_list(p["expense_categories_to_protect"])
    variable_categories={"groceries","transport","dining","entertainment","shopping","healthcare","education","family_support"}
    changed={x[1]:(x[0],x[2]) for x in changes}
    flow=defaultdict(list)
    for e in events:
        if (not include_optional and e.direction == "debit"
                and ((e.flexibility != "fixed" and e.category not in protected)
                     or (e.category in variable_categories and e.category not in protected))
                and e.event_id not in {x[1] for x in changes}):
            continue
        when=e.settlement_date or e.event_date
        if when < request_date: continue
        amt=e.home_amount or ZERO
        if e.event_id in changed:
            action,new=changed[e.event_id]
            if action=="stop": continue
            amt=min(amt,new)
        if when in horizon:
            priority=0 if (DEFAULT_POLICY.same_day_order.startswith("credits") and e.direction=="credit") else 1
            flow[when].append((priority, amt if e.direction=="credit" else -amt, e.event_id, e))
    # Extend supported recurring cash movements conservatively through horizon.
    for recurrence in recurring(events):
        xs, gap = recurrence
        # Recurrence detection and amount estimation are separate. Variable
        # series and historical income are retained as evidence but cannot
        # create a future movement without an explicit supported amount.
        if recurrence.amount_estimate is None:
            continue
        last=xs[-1]; d=last.settlement_date or last.event_date
        if (not include_optional and last.direction == "debit"
                and ((last.flexibility != "fixed" and last.category not in protected)
                     or (last.category in variable_categories and last.category not in protected))
                and last.event_id not in {x[1] for x in changes}):
            continue
        # The recurrence object owns the amount policy. Only a fixed debit
        # with a resolved source amount is projected here; no mean/median/
        # latest heuristic is applied to variable spending.
        amt=recurrence.amount_estimate
        while True:
            d=d+timedelta(days=gap)
            if d >= horizon[-1]: break
            if d>=request_date:
                action=changed.get(last.event_id)
                if action and action[0]=="stop": continue
                if action and action[0]=="reduce": amt=min(amt,action[1])
                priority=0 if (DEFAULT_POLICY.same_day_order.startswith("credits") and last.direction == "credit") else 1
                flow[d].append((priority, amt if last.direction == "credit" else -amt, f"recurrence:{last.event_id}:{d.isoformat()}", last))
    minimum=D(p["minimum_balance_to_keep"])
    safe_floor=balance
    for d in horizon:
        # Explicit policy: confirmed credits are applied before required debits
        # and candidate payments on the same date.
        for _, day_move, movement_id, source_event in sorted(flow[d], key=lambda item:item[0]):
            before=balance
            balance += day_move
            safe_floor=min(safe_floor,balance)
            if trace_out is not None:
                trace_out.append({"date":d.isoformat(),"event_id":movement_id,
                                  "source":source_event.event_id,
                                  "event_type":source_event.event_type,
                                  "cash_state":source_event.cash_state,
                                  "currency":source_event.currency,
                                  "home_currency_amount":str(abs(day_move)),
                                  "balance_before":str(before),"movement":str(day_move),
                                  "balance_after":str(balance),"minimum_balance":str(minimum),
                                  "safe_after_movement":balance>=minimum})
        balances[d]=balance
    for d,a in extra_payments:
        if d < request_date or d not in balances: return False, balances
        for x in horizon:
            before=balances[x]
            if x>=d:
                balances[x]-=a
                safe_floor=min(safe_floor,balances[x])
                if trace_out is not None:
                    trace_out.append({"date":x.isoformat(),"event_id":"plan_payment",
                                      "source":"candidate_plan","event_type":"payment",
                                      "cash_state":"plan_payment","currency":p["home_currency"],
                                      "home_currency_amount":str(a),"balance_before":str(before),
                                      "movement":str(-a),"balance_after":str(balances[x]),
                                      "minimum_balance":str(minimum),
                                      "safe_after_movement":balances[x]>=minimum})
    return safe_floor>=minimum, balances

def forecast_trace(user, request_date, data, extra_payments=(), changes=(), include_optional=True):
    """Return the deterministic forecast result plus auditable movements."""
    movements=[]
    ok, balances=forecast(user, request_date, data, extra_payments, changes,
                          include_optional, movements)
    return {"safe":ok, "balances":balances, "movements":movements,
            "policy": {"same_day_order": DEFAULT_POLICY.same_day_order,
                       "forecast_days": DEFAULT_POLICY.forecast_days}}

def safe_amount(user, req, data, changes=()):
    rd=dt(req["request_date"]); requested=D(req["requested_amount"]); p=data.profiles[user]
    ok, bal=forecast(user,rd,data,((rd,requested),),changes,include_optional=False)
    lo=ZERO; hi=requested
    for _ in range(80):
        mid=((lo+hi)/2).quantize(CENT, rounding=ROUND_HALF_EVEN)
        if mid<=lo: break
        good,_=forecast(user,rd,data,((rd,mid),),changes,include_optional=False)
        if good: lo=mid
        else: hi=mid
    return lo

def earliest(user, req, data, changes=()):
    rd=dt(req["request_date"]); end=rd+timedelta(days=DEFAULT_POLICY.forecast_days-1); amount=D(req["requested_amount"])
    d=rd
    while d<=end:
        good,_=forecast(user,rd,data,((d,amount),),changes)
        if good: return d
        d+=timedelta(days=1)
    return None

def option_plan(o):
    n=int(o["number_of_payments"]); first=dt(o["first_payment_date"]); amount=D(o["payment_amount"]); gap=int(o["payment_frequency_days"] or 0)
    return [(first+timedelta(days=i*gap),amount) for i in range(n)]

def candidate(req,data):
    user=req["user_id"]; p=data.profiles[user]; rd=dt(req["request_date"]); deadline=dt(req["desired_completion_date"]); amount=D(req["requested_amount"]); prefs=parse_pref(p); safe=safe_amount(user,req,data); earliest_date=earliest(user,req,data)
    candidates=[]
    def add(method,plan,changes=(),option_id=""):
        if method not in prefs and method not in {"wait"}: return
        if any(d<rd or d>rd+timedelta(days=89) for d,_ in plan): return
        if plan and max(d for d,_ in plan)>deadline: return
        good,_=forecast(user,rd,data,plan,changes)
        if good: candidates.append((max(d for d,_ in plan) <= deadline if plan else False, len(changes)==0, sum(a for _,a in plan), min(d for d,_ in plan) if plan else rd, len(plan), option_id, method,plan,changes))
    add("full_payment",[(rd,amount)])
    for o in data.options.get(req["request_id"],[]):
        if o["payment_method"]=="full_payment": add("full_payment",option_plan(o),option_id=o["payment_option_id"])
        elif o["payment_method"]=="installments" and "installments" in prefs:
            lim=p["max_installment_months"].strip()
            if not lim or int(o["number_of_payments"])<=int(lim): add("installments",option_plan(o),option_id=o["payment_option_id"])
    if req["allows_partial_payment"].lower()=="true" and "partial_payment" in prefs and safe>ZERO and safe<amount and earliest_date and earliest_date<=deadline:
        add("partial_payment",[(rd,safe),(earliest_date,amount-safe)])
    if earliest_date and earliest_date<=rd+timedelta(days=89) and "full_payment" in prefs:
        add("wait",[(earliest_date,amount)])
    if not candidates:
        allowed_reduce=parse_list(p["expense_categories_user_is_willing_to_reduce"])
        allowed_stop=parse_list(p["expense_categories_user_is_willing_to_stop"])
        protected=parse_list(p["expense_categories_to_protect"])
        flexible=[e for e in semantic_events(data,user) if e.direction=="debit" and e.flexibility!="fixed" and e.category not in protected]
        # Keep the latest source event for each recurring obligation identity,
        # rather than collapsing unrelated obligations that share a category.
        # This is a principled finite representation: future recurrence
        # expansion anchors from the latest event in each obligation series.
        latest={}
        for e in flexible:
            key=(e.category,e.description,e.direction,e.currency)
            if key not in latest or (e.settlement_date or e.event_date) > (latest[key].settlement_date or latest[key].event_date): latest[key]=e
        flexible=list(latest.values())
        possible=[]
        for e in flexible:
            if e.flexibility in {"stoppable","reducible_or_stoppable"} and e.category in allowed_stop:
                possible.append(("stop",e.event_id,ZERO))
            if e.flexibility in {"reducible","reducible_or_stoppable"} and e.category in allowed_reduce:
                possible.append(("reduce",e.event_id,D(e.minimum_allowed_amount)))
        possible.sort(key=lambda x:(x[1],x[0],fmt(x[2])))
        for n in range(1,min(3,len(possible))+1):
            before_len=len(candidates)
            for combo in itertools.combinations(possible,n):
                if len({x[1] for x in combo}) != len(combo):
                    continue
                ch=tuple(combo)
                if req["allows_partial_payment"].lower()=="true" and "partial_payment" in prefs:
                    ss=safe_amount(user,req,data,ch); ee=earliest(user,req,data,ch)
                    # The output contract defines the first partial payment as
                    # the baseline amount_safe_to_pay (before optional changes).
                    # Changes may make the remainder/date feasible, but must
                    # not silently change that reported baseline capacity.
                    if ss>ZERO and safe>ZERO and safe<amount and ee and ee<=deadline:
                        add("partial_payment",[(rd,safe),(ee,amount-safe)],ch)
                if "full_payment" in prefs: add("full_payment",[(rd,amount)],ch)
            # The specification ranks no-change plans first and does not rank
            # action sets. Our explicit conservative tie policy prefers the
            # fewest actions, then stable IDs, so larger sets cannot outrank a
            # feasible smaller set. This is also the bounded-search proof.
            if len(candidates)>before_len:
                break
    if not candidates:
        wait_eligible=bool(earliest_date and earliest_date<=deadline and "full_payment" in prefs)
        return dict(request_id=req["request_id"],amount_safe_to_pay=fmt(safe),affordability_status="affordable_later" if wait_eligible else "not_affordable",recommended_payment_method="wait" if wait_eligible else "not_recommended",payment_plan=(f"{earliest_date.isoformat()}:{fmt(amount)}" if wait_eligible else "none"),earliest_date_for_full_payment=(earliest_date.isoformat() if earliest_date else ""),spending_changes_needed="none",decision_explanation=f"Safe amount today is {fmt(safe)}; the full amount is not safe within the requested plan." )
    candidates.sort(key=lambda x:(not x[0],not x[1],x[2],x[3],x[4],x[5]))
    c=candidates[0]; method,plan,changes=c[6],c[7],c[8]
    status="affordable_now" if method=="full_payment" and plan[0][0]==rd and len(plan)==1 else "affordable_with_plan" if method in {"partial_payment","installments"} or changes else "affordable_later" if method=="wait" else "affordable_with_plan"
    if method in {"full_payment","wait"} and len(plan)==1:
        planstr=f"{plan[0][0].isoformat()}:{display_requested_amount(req,plan[0][1])}"
    else:
        planstr="|".join(f"{d.isoformat()}:{fmt(a)}" for d,a in plan)
    actions=[]
    for action,eid,new in changes: actions.append(f"stop:{eid}" if action=="stop" else f"reduce_to:{eid}:{fmt(new)}")
    safe_text=display_requested_amount(req,safe) if safe==amount else fmt(safe)
    return dict(request_id=req["request_id"],amount_safe_to_pay=safe_text,affordability_status=status,recommended_payment_method=method,payment_plan=planstr,earliest_date_for_full_payment=(earliest_date.isoformat() if earliest_date else rd.isoformat() if method=="full_payment" else ""),spending_changes_needed="|".join(actions) if actions else "none",decision_explanation=f"Plan {method} completes {display_requested_amount(req,amount)} while maintaining the minimum balance; safe today: {safe_text}.")

def validate_output(row, req, data=None):
    assert set(row)==set(OUT_COLS); amount=D(row["amount_safe_to_pay"]); requested=D(req["requested_amount"])
    assert ZERO<=amount<=requested; assert row["affordability_status"] in {"affordable_now","affordable_with_plan","affordable_later","not_affordable"}; assert row["recommended_payment_method"] in METHODS
    if data is not None:
        prefs=set(parse_pref(data.profiles[req["user_id"]])); method=row["recommended_payment_method"]
        if method in {"full_payment","partial_payment","installments"}: assert method in prefs
        if method=="wait": assert "full_payment" in prefs
    if row["recommended_payment_method"]=="not_recommended": assert row["payment_plan"]=="none"
    if row["recommended_payment_method"]=="partial_payment":
        assert row["affordability_status"]=="affordable_with_plan" and req["allows_partial_payment"].lower()=="true"
    if row["payment_plan"]!="none":
        prev=None
        total=ZERO; entries=[]
        for item in row["payment_plan"].split("|"):
            d,a=item.split(":",1); dd=dt(d); aa=D(a); assert prev is None or dd>=prev; prev=dd; assert aa>=ZERO; total+=aa; entries.append((dd,aa))
            assert dt(req["request_date"])<=dd<=dt(req["request_date"])+timedelta(days=DEFAULT_POLICY.forecast_days-1)
        if row["recommended_payment_method"]=="partial_payment":
            assert len(entries)==2 and entries[0][1]==amount and total==requested
            assert entries[1][0] <= dt(req["desired_completion_date"])
        if row["recommended_payment_method"]=="full_payment": assert len(entries)==1 and total==requested
        if row["recommended_payment_method"]=="installments" and data is not None:
            valid=[]
            for o in data.options.get(req["request_id"],[]):
                if o["payment_method"]=="installments": valid.append(option_plan(o))
            assert entries in valid
            lim=data.profiles[req["user_id"]]["max_installment_months"].strip()
            if lim: assert len(entries)<=int(lim)
    actions=row["spending_changes_needed"]
    if actions!="none":
        parts=actions.split("|"); assert 1<=len(parts)<=3
        seen=set()
        for part in parts:
            bits=part.split(":"); assert bits[0] in {"stop","reduce_to"}; eid=bits[1]; assert eid not in seen; seen.add(eid)
            if data is not None:
                matching=[e for xs in data.events.values() for e in xs if e.event_id==eid]
                assert matching and matching[0].flexibility != "fixed"
                e=matching[0]; p=data.profiles[req["user_id"]]
                assert e.category not in parse_list(p["expense_categories_to_protect"])
                if bits[0]=="stop": assert e.category in parse_list(p["expense_categories_user_is_willing_to_stop"])
                if bits[0]=="reduce_to": assert e.category in parse_list(p["expense_categories_user_is_willing_to_reduce"])
    if data is not None and row["recommended_payment_method"] != "not_recommended" and row["payment_plan"] != "none":
        changes=[]
        if row["spending_changes_needed"] != "none":
            for part in row["spending_changes_needed"].split("|"):
                bits=part.split(":"); changes.append(("stop" if bits[0]=="stop" else "reduce",bits[1],ZERO if bits[0]=="stop" else D(bits[2])))
        entries=[(dt(item.split(":",1)[0]),D(item.split(":",1)[1])) for item in row["payment_plan"].split("|")]
        assert forecast(req["user_id"],dt(req["request_date"]),data,entries,changes)[0]

def main(root=None):
    root=Path(root or Path(__file__).resolve().parents[1]); data=load_data(root); normalize_events(data,root)
    rows=[]
    for req in data.requests:
        row=candidate(req,data); validate_output(row,req,data); rows.append(row)
    out=root/"output.csv"
    with open(out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=OUT_COLS); w.writeheader(); w.writerows(rows)
    return rows

if __name__=="__main__": main()
