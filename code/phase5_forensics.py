"""Read-only Phase 5 forecast-contract forensics.

Generates implied cash-flow traces and conceptual-model score comparisons in
memory. It does not write production code, datasets, or expected outputs.
"""
from __future__ import annotations
import csv, json, sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","earliest_date_for_full_payment","affordability_status",
        "recommended_payment_method","payment_plan","spending_changes_needed"]
VARIABLE={"groceries","transport","dining","entertainment","shopping","healthcare","education","family_support"}

def dec(v): return Decimal(str(v))
def iso(e): return e.get("settlement_date") or e.get("event_date")
def compact(e):
    return {k:e.get(k) for k in ("event_id","event_type","description","category","direction","amount","home_amount","currency","event_date","settlement_date","status","flexibility","linked_event_id")}

def root_for(ctx, safe_bad, early_bad):
    t=ctx["safe_amount_trace"]
    if t.get("pending_events"): return "pending/lifecycle semantics"
    if t.get("scheduled_credits"): return "scheduled-credit boundary"
    if t.get("recurring_events"): return "recurrence/amount semantics"
    if safe_bad: return "forecast baseline or minimum-floor semantics"
    if early_bad: return "date/forecast semantics"
    return "serialization or downstream policy"

def reconstruct():
    report=json.loads((ROOT/"SAMPLE_MISMATCH_REPORT.json").read_text(encoding="utf-8"))
    diff=json.loads((ROOT/"DIFFERENTIAL_FORENSICS_PASS_2.json").read_text(encoding="utf-8"))
    byid={x["request"]["request_id"]:x for x in diff["request_traces"]}
    records=[]
    for item in report["requests"]:
        rid=item["request_id"]; ctx=byid[rid]; s=ctx["safe_amount_trace"]; e=ctx["earliest_date_trace"]
        sf=item["fields"]["amount_safe_to_pay"]; ef=item["fields"]["earliest_date_for_full_payment"]
        safe_bad=not sf["match"]; early_bad=not ef["match"]
        if not (safe_bad or early_bad): continue
        expected=dec(sf["expected"]); actual=dec(sf["actual"])
        # Positive residual means the expected result allows less capacity than
        # the current model; it is a missing debit or an omitted credit.
        residual=actual-expected
        reqdate=s["request_date"]
        def future(xs): return [compact(x) for x in xs if (iso(x) or "") >= reqdate]
        critical=[]
        for row in e.get("rows",[]):
            if row["date"] in {e.get("expected_date"),e.get("actual_date")}:
                critical.append({k:row.get(k) for k in ("date","starting_balance","credits","debits","requested_payment","minimum_required","ending_balance","feasible_current_model","reason")})
        records.append({
            "request_id":rid,
            "user_id":item["context"]["request"]["user_id"],
            "request_date":reqdate,
            "deadline":item["context"]["request"]["desired_completion_date"],
            "expected_safe_amount":str(expected),"actual_safe_amount":str(actual),
            "capacity_residual_actual_minus_expected":str(residual),
            "expected_earliest_date":e.get("expected_date"),"actual_earliest_date":e.get("actual_date"),
            "starting_balance":s["starting_balance"],"minimum_balance":s["minimum_required"],
            "explicit_future_credits":future(s.get("future_credits",[])),
            "explicit_future_debits":future(s.get("future_debits",[])),
            "scheduled_credits":[compact(x) for x in s.get("scheduled_credits",[])],
            "pending_events":[compact(x) for x in s.get("pending_events",[])],
            "recurrence_evidence":s.get("recurring_events",[]),
            "protected_categories":s.get("essential_categories"),
            "optional_categories":s.get("optional_categories"),
            "same_day_events":s.get("same_day_events",{}),
            "critical_date_rows":critical,
            "safe_amount_first_divergence":ctx.get("first_divergence_by_field",{}).get("amount_safe_to_pay"),
            "earliest_first_divergence":ctx.get("first_divergence_by_field",{}).get("earliest_date_for_full_payment"),
            "root_cause":root_for(ctx,safe_bad,early_bad),
            "confidence":"high for explicit movements; low/medium for any inferred missing movement"
        })
    return records

def series_inventory():
    samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv")
    users={r["user_id"] for r in samples}
    rows=main.read_csv(ROOT/"dataset"/"financial_events.csv")
    groups=defaultdict(list)
    for r in rows:
        if r["user_id"] not in users or r["status"] not in {"settled","pending","scheduled"}: continue
        key=(r["user_id"],r["category"],r["description"],r["direction"],r["currency"])
        groups[key].append(r)
    out=[]
    for key,xs in groups.items():
        if len(xs)<2: continue
        xs.sort(key=lambda x:x.get("settlement_date") or x.get("event_date"))
        dates=[x.get("settlement_date") or x.get("event_date") for x in xs]
        gaps=[(main.dt(dates[i])-main.dt(dates[i-1])).days for i in range(1,len(dates))]
        out.append({"user_id":key[0],"category":key[1],"description":key[2],"direction":key[3],"currency":key[4],
                    "event_ids":[x["event_id"] for x in xs],"dates":dates,
                    "amounts":[x["amount"] for x in xs],"statuses":[x["status"] for x in xs],
                    "flexibility":sorted({x["flexibility"] for x in xs}),"gaps_days":gaps})
    return sorted(out,key=lambda x:(x["user_id"],x["category"],x["description"]))

def model_scores():
    data=main.load_data(ROOT); main.normalize_events(data,ROOT)
    samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv")
    base=main.recurring
    def score():
        c={f:0 for f in FIELDS}
        for r in samples:
            got=main.candidate(r,data)
            for f in FIELDS: c[f]+=int(str(got.get(f,""))==str(r.get(f,"")))
        return c
    def filt(pred):
        return lambda events:[x for x in base(events) if pred(x.events)]
    def explicit(events): return []
    models={
      "A explicit events only":explicit,
      "B explicit fixed recurrence plus confirmed credits":filt(lambda xs: xs and xs[0].direction=="debit" and xs[0].category not in VARIABLE),
      "C fixed recurrence plus evidence-supported variable recurrence":filt(lambda xs: xs and xs[0].direction=="debit"),
      "D historical recurrence with inferred amount":base,
    }
    out={}
    try:
        for name,fn in models.items(): main.recurring=fn; out[name]=score()
    finally: main.recurring=base
    return out

def write_outputs():
    records=reconstruct(); scores=model_scores(); inventory=series_inventory()
    payload={"scope":"read-only Phase 5 forecast contract forensics","records":records,"recurring_series_inventory":inventory,"conceptual_model_scores":scores}
    (ROOT/"PHASE_5_FORECAST_FORENSICS.json").write_text(json.dumps(payload,indent=2,default=str),encoding="utf-8")
    lines=["# Phase 5 — Forecast Contract Forensics","","Status: analysis-only. No production code, dataset, or expected output was modified.","",
           "## Scope and method","",
           "The traces below reverse-engineer constraints from the supplied expected fields. A residual is arithmetic evidence, not permission to invent a movement. Every movement is labelled by evidence class; UNKNOWN remains unknown.","",
           "Evidence classes: DIRECTLY OBSERVED, MESSAGE-CONFIRMED, SCHEDULED/CONFIRMED, RECURRING-INFERRED, UNKNOWN.","",
           "## Expected implied cash-flow findings","",
           "A positive residual (`actual - expected`) means the current model has more capacity than the expected answer; the missing constraint could be a debit, an omitted credit, a different protected/optional baseline, or a date/order rule. It is not assigned to an invented event.",""]
    for r in records:
        lines += [f"### {r['request_id']}","",f"- Safe amount: expected `{r['expected_safe_amount']}`, current `{r['actual_safe_amount']}`, residual `{r['capacity_residual_actual_minus_expected']}`.",f"- Earliest full payment: expected `{r['expected_earliest_date'] or 'empty'}`, current `{r['actual_earliest_date'] or 'empty'}`; deadline `{r['deadline']}`.",f"- Starting/minimum: `{r['starting_balance']}` / `{r['minimum_balance']}`.",f"- First divergences: safe `{r['safe_amount_first_divergence']}`; earliest `{r['earliest_first_divergence']}`.",f"- Root-cause cluster: **{r['root_cause']}**.","- Explicit future credits:"]
        if r["explicit_future_credits"]:
            lines += ["  - "+"; ".join(f"{x['event_id']} {iso(x)} {x['direction']} {x['home_amount']} {x['description']} [DIRECTLY OBSERVED]" for x in r["explicit_future_credits"])]
        else: lines += ["  - none"]
        lines += ["- Explicit future debits:"]
        if r["explicit_future_debits"]:
            lines += ["  - "+"; ".join(f"{x['event_id']} {iso(x)} {x['direction']} {x['home_amount']} {x['description']} [DIRECTLY OBSERVED]" for x in r["explicit_future_debits"])]
        else: lines += ["  - none"]
        lines += [f"- Scheduled credits: {len(r['scheduled_credits'])}; pending events: {len(r['pending_events'])}.",f"- Recurrence evidence series: {len(r['recurrence_evidence'])}; protected categories `{r['protected_categories']}`; optional `{r['optional_categories']}`.","- Critical-date balance rows:"]
        for x in r["critical_date_rows"]: lines += ["  - "+json.dumps(x,sort_keys=True)]
        lines += ["- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.",""]
    lines += ["## FORECAST_CONTRACT_TABLE","","| Example | Expected safe amount | Expected earliest date | Required future movements | Excluded future movements | Recurring evidence | Income evidence | Pending behavior | First divergence | Root cause | Confidence |","|---|---:|---|---|---|---:|---|---|---|---|---|"]
    for r in records:
        required="; ".join(f"{x['event_id']}@{iso(x)}:{x['home_amount']}" for x in r["explicit_future_credits"]+r["explicit_future_debits"]) or "none explicitly dated"
        excluded="; ".join(x["event_id"] for x in r["pending_events"]) or "none observed"
        income="; ".join(x["event_id"] for x in r["scheduled_credits"]) or "none"
        pending="reserved debit / excluded credit per status" if r["pending_events"] else "none observed"
        first=(r["safe_amount_first_divergence"] or r["earliest_first_divergence"] or "unknown")
        lines.append("| "+" | ".join([r["request_id"],r["expected_safe_amount"],r["expected_earliest_date"] or "empty",required,excluded,str(len(r["recurrence_evidence"])),income,pending,first,r["root_cause"],r["confidence"]])+" |")
    lines += ["","## Recurring-looking series inventory","","Every repeated source-description series for the 25 sample users is listed below. This is an inventory of evidence, not a declaration that every series must recur. Category-only grouping is not treated as authoritative.","","| User | Category | Description | Direction | Currency | Event IDs | Dates | Amounts | Gaps (days) | Flexibility | Statuses |","|---|---|---|---|---|---|---|---|---|---|---|"]
    for x in inventory:
        def cell(v): return str(v).replace("|","\\|")
        lines.append("| "+" | ".join(cell(x[k]) for k in ("user_id","category","description","direction","currency","event_ids","dates","amounts","gaps_days","flexibility","statuses"))+" |")
    lines.append("")
    lines += ["## Conceptual forecast models","","| Model | Safe | Earliest | Status | Method | Plan | Changes | Interpretation |","|---|---:|---:|---:|---:|---:|---:|---|"]
    labels={"A explicit events only":"No inferred recurrence; safe lower-bound evidence only.","B explicit fixed recurrence plus confirmed credits":"Projects fixed recurring debits and explicit confirmed credits; no variable mean.","C fixed recurrence plus evidence-supported variable recurrence":"Projects variable series only if an evidence-based amount exists; amount rule remains unresolved.","D historical recurrence with inferred amount":"Current-style inference; includes unsupported amount extrapolation."}
    for name,s in scores.items(): lines.append(f"| {name} | {s['amount_safe_to_pay']} | {s['earliest_date_for_full_payment']} | {s['affordability_status']} | {s['recommended_payment_method']} | {s['payment_plan']} | {s['spending_changes_needed']} | {labels[name]} |")
    lines += ["","Scores are supporting diagnostics only. Model D is not defensible merely because it can match a fixture; Model A can omit required recurring obligations; Model B is the strongest currently supported baseline; Model C requires an explicit amount-estimation rule that the specification does not provide.","",
              "## Same-day and lifecycle findings","",
              "No solved example isolates same-day credit/debit/payment ordering. Pending credits are explicitly excluded; pending debits are reserved at their supplied settlement date; failed/cancelled/unrealized rows have no cash movement. Replacement timing and amount remain UNKNOWN unless supplied by a live linked row.","",
              "## Decision gate","",
              "1. The challenge requires a deterministic 90-day minimum-balance forecast over explicit confirmed movements and supported fixed recurrence, with no invented income or variable amount.",
              "2. Phase 4 correctly removed the unsupported variable arithmetic mean, but its broad recurrence/lifecycle and baseline choices still alter downstream feasibility.",
              "3. Change next only after resolving fixed-series identity, explicit confirmed credit boundaries, optional-baseline scope, and direct event-level residuals.",
              "4. Do not change ranking, payment preferences, or output serialization to compensate for an upstream cash-flow mismatch.",
              "5. Same-day ordering, recurrence thresholds/month-end rules, generic scheduled credits, replacement timing, late-deadline status mapping, and flexible ties remain genuinely unspecified.","",
              "## Required truth table","",
              "The machine-readable `PHASE_5_FORECAST_FORENSICS.json` contains one record for every solved example with an incorrect safe amount or earliest date, including explicit movements, pending/lifecycle state, recurrence evidence, critical dates, residual capacity and first-divergence category."]
    (ROOT/"PHASE_5_FORECAST_FORENSICS.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__": write_outputs()
