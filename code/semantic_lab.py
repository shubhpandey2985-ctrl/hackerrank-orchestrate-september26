"""Analysis-only synthetic forecast laboratory.

This module deliberately does not import or mutate production decision logic.
It models tiny fixtures with Decimal arithmetic so competing interpretations can
be compared without touching supplied challenge data.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_EVEN, getcontext
from typing import Iterable

getcontext().prec = 40
ZERO = Decimal("0")
CENT = Decimal("0.01")

@dataclass(frozen=True)
class LabEvent:
    event_id: str
    when: date
    amount: Decimal
    direction: str = "debit"
    status: str = "settled"
    category: str = "other"
    description: str = ""
    currency: str = "USD"
    settlement_date: date | None = None
    flexibility: str = "fixed"
    protected: bool = False
    recurrence_days: int | None = None
    recurrence_amount: Decimal | None = None
    terminal: bool = False
    linked_event_id: str = ""
    confirmed: bool = False

@dataclass(frozen=True)
class LabFixture:
    fixture_id: str
    question: str
    current_date: date
    opening_balance: Decimal
    minimum_balance: Decimal
    horizon_days: int = 30
    requested_amount: Decimal = Decimal("0")
    deadline: date | None = None
    home_currency: str = "USD"
    events: tuple[LabEvent, ...] = field(default_factory=tuple)
    fx: dict[tuple[date, str, str], Decimal] = field(default_factory=dict)

@dataclass
class LabResult:
    fixture_id: str
    model: str
    movements: list[dict]
    balances: dict[date, Decimal]
    minimum_observed: Decimal
    safe_amount: Decimal
    earliest_safe_date: date | None
    feasible: bool
    provenance: list[dict]

def _home_amount(e: LabEvent, f: LabFixture) -> Decimal:
    if e.currency == f.home_currency:
        return e.amount
    key = (e.settlement_date or e.when, e.currency, f.home_currency)
    if key not in f.fx:
        raise ValueError(f"missing direct FX rate {key}")
    return e.amount * f.fx[key]

def _include(e: LabEvent, model: str) -> tuple[bool, str]:
    if e.status in {"failed", "cancelled", "unrealized"} or e.direction == "non_cash":
        return False, "EXCLUDED_BECAUSE:lifecycle/non_cash"
    if e.status == "pending" and e.direction == "credit":
        return False, "EXCLUDED_BECAUSE:pending_credit"
    if e.status == "scheduled" and e.direction == "credit" and not e.confirmed:
        return False, "EXCLUDED_BECAUSE:generic_scheduled_credit"
    if model == "explicit_only" and e.recurrence_days is not None and e.when < f_current:
        return True, "INCLUDED_BECAUSE:explicit_historical_anchor_only"
    return True, "INCLUDED_BECAUSE:live_cash_state"

def _iter_movements(f: LabFixture, model: str, optional_included: bool = True):
    global f_current
    f_current = f.current_date
    out = []
    seen = set()
    for e in f.events:
        ok, reason = _include(e, model)
        if not ok:
            out.append((e.when, ZERO, e.event_id, reason, e))
            continue
        if e.category == "optional" and not optional_included:
            out.append((e.when, ZERO, e.event_id, "EXCLUDED_BECAUSE:optional_baseline", e))
            continue
        when = e.settlement_date or e.when
        if when >= f.current_date and when < f.current_date + timedelta(days=f.horizon_days):
            amt = _home_amount(e, f)
            signed = amt if e.direction == "credit" else -amt
            out.append((when, signed, e.event_id, reason, e))
            seen.add(e.event_id)
        if e.recurrence_days and e.when < f.current_date and not e.terminal and model in {"stable_fixed", "calendar", "variable"}:
            amount = e.recurrence_amount if e.recurrence_amount is not None else e.amount
            if model == "stable_fixed" and e.recurrence_amount is None:
                continue
            d = e.when
            while True:
                d += timedelta(days=e.recurrence_days)
                if d >= f.current_date + timedelta(days=f.horizon_days): break
                if d < f.current_date: continue
                a = amount
                if model == "variable" and e.recurrence_amount is None:
                    a = e.amount
                signed = a if e.direction == "credit" else -a
                rid = f"recurrence:{e.event_id}:{d.isoformat()}"
                out.append((d, signed, rid, "INCLUDED_BECAUSE:recurrence_model", e))
    return out

def run_fixture(f: LabFixture, model: str = "stable_fixed", optional_included: bool = True, same_day: str = "credit_first", payment: tuple[date, Decimal] | None = None, _metrics: bool = True) -> LabResult:
    moves = _iter_movements(f, model, optional_included)
    if payment:
        moves.append((payment[0], -payment[1], "plan_payment", "INCLUDED_BECAUSE:requested_plan", None))
    priority = {"credit_first": {"credit": 0, "debit": 1}, "debit_first": {"debit": 0, "credit": 1}}.get(same_day, {"credit": 0, "debit": 1})
    moves.sort(key=lambda x: (x[0], priority.get(x[4].direction if x[4] else "debit", 2), x[2]))
    bal = f.opening_balance; minimum = bal; balances = {}; records = []; provenance = []
    for d, signed, mid, reason, source in moves:
        before = bal; bal += signed; minimum = min(minimum, bal); balances[d] = bal
        records.append({"date": d.isoformat(), "movement_id": mid, "before": str(before), "movement": str(signed), "after": str(bal), "minimum": str(f.minimum_balance), "safe": bal >= f.minimum_balance, "reason": reason})
        provenance.append({"movement_id": mid, "source_event_id": source.event_id if source else "plan", "reason": reason})
    # carry final balance to every day so safe-date traces remain total.
    cursor = f.current_date
    running = f.opening_balance
    byday = {}
    for d in range(f.horizon_days):
        day = f.current_date + timedelta(days=d)
        dayrecs = [r for r in records if r["date"] == day.isoformat()]
        if dayrecs: running = Decimal(dayrecs[-1]["after"])
        byday[day] = running
    def feasible(amount: Decimal, day: date) -> bool:
        test = run_fixture(f, model, optional_included, same_day, (day, amount), _metrics=False)
        return test.minimum_observed >= f.minimum_balance
    if not _metrics:
        return LabResult(f.fixture_id, model, records, byday, minimum, ZERO, None, minimum >= f.minimum_balance, provenance)
    lo, hi = ZERO, max(ZERO, f.requested_amount)
    for _ in range(100):
        mid = ((lo + hi) / 2).quantize(CENT, rounding=ROUND_HALF_EVEN)
        if mid <= lo: break
        if feasible(mid, f.current_date): lo = mid
        else: hi = mid
    earliest = None
    if f.requested_amount > ZERO:
        for i in range(f.horizon_days):
            d = f.current_date + timedelta(days=i)
            if feasible(f.requested_amount, d): earliest = d; break
    return LabResult(f.fixture_id, model, records, byday, minimum, lo, earliest, minimum >= f.minimum_balance, provenance)

def fixture(event_id: str, question: str, **kwargs) -> LabFixture:
    return LabFixture(event_id, question, kwargs.pop("current_date", date(2025,1,1)), kwargs.pop("opening_balance", Decimal("1000")), kwargs.pop("minimum_balance", Decimal("100")), events=tuple(kwargs.pop("events", ())), **kwargs)

def catalog() -> list[LabFixture]:
    d=date(2025,1,1); prev=d-timedelta(days=7)
    out=[]
    # Variable spending fixtures VS-01..VS-10.
    out.append(fixture("VS-01","single variable occurrence",events=(LabEvent("v1",prev,Decimal("50"),category="groceries",description="market",flexibility="reducible"),),requested_amount=Decimal("500")))
    for ident,n,amounts in [("VS-02",2,[50,50]),("VS-03",3,[50,50,50]),("VS-04",3,[40,60,80])]:
        ev=tuple(LabEvent(f"{ident.lower()}_{i}",d-timedelta(days=7*(n-i)),Decimal(str(a)),category="groceries",description="market",flexibility="reducible") for i,a in enumerate(amounts))
        out.append(fixture(ident,"repeated variable amount series",events=ev,requested_amount=Decimal("500")))
    out.extend([
      fixture("VS-05","same category different merchants",events=(LabEvent("v5a",prev,Decimal("20"),category="food",description="merchant_a"),LabEvent("v5b",d-timedelta(days=14),Decimal("30"),category="food",description="merchant_b")),requested_amount=Decimal("500")),
      fixture("VS-06","same merchant different categories",events=(LabEvent("v6a",prev,Decimal("20"),category="food",description="merchant"),LabEvent("v6b",d-timedelta(days=14),Decimal("30"),category="transport",description="merchant")),requested_amount=Decimal("500")),
      fixture("VS-07","recurring flexible variable spending",events=(LabEvent("v7",prev,Decimal("50"),category="optional",description="hobby",flexibility="reducible",recurrence_days=7),),requested_amount=Decimal("500")),
      fixture("VS-08","recurring protected variable spending",events=(LabEvent("v8",prev,Decimal("50"),category="healthcare",description="care",protected=True,recurrence_days=7),),requested_amount=Decimal("500")),
      fixture("VS-09","terminal variable recurrence",events=(LabEvent("v9",prev,Decimal("50"),category="optional",description="hobby",recurrence_days=7,terminal=True),),requested_amount=Decimal("500")),
      fixture("VS-10","variable recurrence explicit future confirmation",events=(LabEvent("v10h",prev,Decimal("50"),category="optional",description="hobby",recurrence_days=7),LabEvent("v10f",d+timedelta(days=7),Decimal("70"),category="optional",description="hobby",confirmed=True)),requested_amount=Decimal("500")),
    ])
    # Recurrence, income, optional, pending, same-day, replacement, deadline, FX and decimal minimal fixtures.
    for ident,gap in [("RC-01",7),("RC-02",14),("RC-03",30),("RC-04",31),("RC-05",31),("RC-06",28),("RC-07",30),("RC-08",45),("RC-09",11),("RC-10",7),("RC-11",7),("RC-12",7),("RC-13",30),("RC-14",30)]:
        status="cancelled" if ident=="RC-11" else "settled"; terminal=ident in {"RC-10","RC-14"}
        ev=LabEvent(ident.lower(),d-timedelta(days=gap),Decimal("100"),direction="debit",status=status,description=ident,recurrence_days=gap,terminal=terminal)
        out.append(fixture(ident,"recurrence calendar boundary",events=(ev,),requested_amount=Decimal("500")))
    for ident,status,confirmed in [("INC-01","settled",False),("INC-02","settled",False),("INC-03","settled",False),("INC-04","settled",False),("INC-05","scheduled",True),("INC-06","scheduled",True),("INC-07","settled",False),("INC-08","scheduled",False),("INC-09","pending",False),("INC-10","cancelled",False)]:
        out.append(fixture(ident,"income future-money boundary",events=(LabEvent(ident.lower(),d-timedelta(days=30),Decimal("500"),direction="credit",status=status,description=ident,recurrence_days=30,confirmed=confirmed),),requested_amount=Decimal("500")))
    out.extend([
      fixture("OB-A","optional included",events=(LabEvent("oba",d+timedelta(days=2),Decimal("100"),category="optional",flexibility="reducible"),),requested_amount=Decimal("800")),
      fixture("OB-B","optional excluded",events=(LabEvent("obb",d+timedelta(days=2),Decimal("100"),category="optional",flexibility="reducible"),),requested_amount=Decimal("800")),
    ])
    for ident,status,settle in [("PEN-01","pending",d+timedelta(days=3)),("PEN-02","pending",d+timedelta(days=3)),("PEN-03","pending",None),("PEN-04","settled",d+timedelta(days=3)),("PEN-05","cancelled",d+timedelta(days=3))]:
        direction="credit" if ident=="PEN-01" else "debit"
        out.append(fixture(ident,"pending lifecycle",events=(LabEvent(ident.lower(),d,Decimal("100"),direction=direction,status=status,settlement_date=settle,linked_event_id="pen_old" if ident in {"PEN-04","PEN-05"} else ""),),requested_amount=Decimal("100")))
    for ident in ["SD-01","SD-02","SD-03","SD-04"]:
        events=(LabEvent(f"{ident.lower()}c",d+timedelta(days=2),Decimal("100"),direction="credit"),LabEvent(f"{ident.lower()}d",d+timedelta(days=2),Decimal("80"),direction="debit"))
        out.append(fixture(ident,"same-day movement ordering",events=events,requested_amount=Decimal("100")))
    for ident,status,linked in [("REP-01","failed",""),("REP-02","cancelled","rep_new"),("REP-03","failed","rep_amount"),("REP-04","failed","rep_date"),("REP-05","settled","rep_new")]:
        out.append(fixture(ident,"replacement lifecycle",events=(LabEvent(ident.lower(),d+timedelta(days=3),Decimal("100"),status=status,linked_event_id=linked),),requested_amount=Decimal("100")))
    for ident,offset in [("DL-01",0),("DL-02",5),("DL-03",6),("DL-04",20),("DL-05",None)]:
        evs=() if offset is None else (LabEvent(ident.lower(),d+timedelta(days=offset),Decimal("100"),direction="credit"),)
        out.append(fixture(ident,"deadline and capacity",events=evs,requested_amount=Decimal("100"),deadline=d+timedelta(days=5)))
    for ident,rate_date,rate in [("FX-01",d,Decimal("2")),("FX-02",d+timedelta(days=1),Decimal("2")),("FX-03",d,Decimal("0.5")),("FX-04",d,Decimal("2")),("FX-05",d,None)]:
        rates={} if rate is None else {(rate_date,"EUR","USD"):rate}
        out.append(fixture(ident,"direct dated FX",events=(LabEvent(ident.lower(),d,Decimal("10"),currency="EUR"),),fx=rates,requested_amount=Decimal("10")))
    for ident,amount in [("DEC-01","100.00"),("DEC-02","100.0"),("DEC-03","100"),("DEC-04","0.10"),("DEC-05","0.30"),("DEC-06","603.30")]:
        out.append(fixture(ident,"Decimal representation",events=(LabEvent(ident.lower(),d,Decimal(amount),direction="debit"),),requested_amount=Decimal(amount)))
    return out
