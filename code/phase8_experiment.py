"""Read-only Phase 8 optional-baseline counterfactual experiment."""
from __future__ import annotations
import json,sys
from dataclasses import replace
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed"]
POLICIES=["CURRENT_BEHAVIOR","INCLUDE_REQUIRED_ONLY","INCLUDE_ALL_RECURRING","EXCLUDE_OPTIONAL_FLEXIBLE"]

def safe_mode(user,req,data,include_optional):
    rd=main.dt(req["request_date"]); lo=Decimal("0"); hi=main.D(req["requested_amount"])
    for _ in range(80):
        mid=((lo+hi)/2).quantize(main.CENT)
        if mid<=lo: break
        if main.forecast(user,rd,data,((rd,mid),),(),include_optional)[0]: lo=mid
        else: hi=mid
    return lo

def earliest_mode(user,req,data,include_optional):
    rd=main.dt(req["request_date"]); amount=main.D(req["requested_amount"])
    for i in range(main.DEFAULT_POLICY.forecast_days):
        day=rd+timedelta(days=i)
        if main.forecast(user,rd,data,((day,amount),),(),include_optional)[0]: return day.isoformat()
    return ""

def evaluate(samples,data):
    rows=[]; counts={f:0 for f in FIELDS}
    for req in samples:
        got=main.candidate(req,data); actual={f:got.get(f,"") for f in FIELDS}; expected={f:req.get(f,"") for f in FIELDS}
        for f in FIELDS: counts[f]+=int(str(actual[f])==str(expected[f]))
        rows.append({"request_id":req["request_id"],"expected":expected,"actual":actual})
    return counts,rows

def event_summary(data,user,request_date):
    out=[]
    for e in main.semantic_events(data,user):
        when=e.settlement_date or e.event_date
        if when>=request_date and e.direction=="debit":
            out.append({"event_id":e.event_id,"date":when.isoformat(),"amount":str(e.home_amount),"category":e.category,"description":e.description,"flexibility":e.flexibility,"status":e.status})
    return out

def critical(data,req):
    user=req["user_id"]; rd=main.dt(req["request_date"]); amount=main.D(req["requested_amount"]); out=[]
    for i in range(main.DEFAULT_POLICY.forecast_days):
        day=rd+timedelta(days=i); tr=[]
        ok,bal=main.forecast_trace(user,rd,data,((day,amount),),(),include_optional=main.baseline_include_optional("earliest")) .get("safe"), None
        # Trace is regenerated with no payment to expose the nearest cash flow.
        base=main.forecast_trace(user,rd,data,(),(),include_optional=main.baseline_include_optional("earliest"))
        if i<5 or day==rd+timedelta(days=14):
            out.append({"date":day.isoformat(),"balance_without_payment":str(base["balances"].get(day)),"feasible_with_payment":ok,"minimum":data.profiles[user]["minimum_balance_to_keep"]})
    return out

def run():
    data=main.load_data(ROOT); main.normalize_events(data,ROOT); samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv"); base=main.DEFAULT_POLICY
    variants={}; baseline_rows=None
    for policy in POLICIES:
        main.DEFAULT_POLICY=replace(base,optional_baseline_policy=policy)
        if policy=="CURRENT_BEHAVIOR":
            counts,rows=evaluate(samples,data)
        else:
            include=(policy=="INCLUDE_ALL_RECURRING")
            old_safe,old_earliest=main.safe_amount,main.earliest
            main.safe_amount=lambda u,r,d,c=():safe_mode(u,r,d,include)
            main.earliest=lambda u,r,d,c=(): (main.dt(x) if (x:=earliest_mode(u,r,d,include)) else None)
            try: counts,rows=evaluate(samples,data)
            finally: main.safe_amount,main.earliest=old_safe,old_earliest
        variants[policy]={"field_matches":counts,"rows":rows}
        if policy=="CURRENT_BEHAVIOR": baseline_rows=rows
    changed={}
    for policy,obj in variants.items():
        if policy=="CURRENT_BEHAVIOR": continue
        changes=[]
        for b,n,req in zip(baseline_rows,obj["rows"],samples):
            diffs=[f for f in FIELDS if b["actual"][f]!=n["actual"][f]]
            if diffs:
                changes.append({"request_id":req["request_id"],"fields":diffs,"before":b["actual"],"after":n["actual"],"events":event_summary(data,req["user_id"],main.dt(req["request_date"])),"critical_dates":critical(data,req)})
        changed[policy]=changes
    main.DEFAULT_POLICY=base
    payload={"scope":"read-only Phase 8 optional-baseline experiment","production_default":"CURRENT_BEHAVIOR","variants":variants,"changed_requests":changed,"safety_invariants":["Decimal arithmetic","minimum balance after every movement","0 <= safe amount <= requested amount","pending credits excluded","required debits cannot increase capacity","protected/fixed events cannot be modified"]}
    (ROOT/"PHASE_8_SEMANTIC_REPAIR.json").write_text(json.dumps(payload,indent=2,default=str),encoding="utf-8")
    lines=["# Phase 8 — Controlled Semantic Repair","","Status: one controlled optional-baseline experiment. Recurrence-calendar semantics, ranking, preferences, status mapping, same-day ordering and serialization were not changed.","","## Baseline","","- Checkpoint before repair: `phase8-pre-semantic-repair` (`d241695`).","- Full suite before repair: 45 passed.","- Baseline matches: safe 2/25, status 10/25, method 12/25, plan 11/25, earliest 8/25, changes 22/25.","- Dataset/sample hashes were captured before the checkpoint and remain unchanged.","","## Policy variants","","| Policy | Safe | Status | Method | Plan | Earliest | Changes |","|---|---:|---:|---:|---:|---:|---:|"]
    for p in POLICIES:
        s=variants[p]["field_matches"]; lines.append("| "+p+" | "+" | ".join(str(s[f]) for f in FIELDS)+" |")
    lines += ["","Scores are counterfactual diagnostics, not specification proof. The default remains CURRENT_BEHAVIOR.","","## Event-level changed results","","For every non-default variant, the JSON artifact records all changed requests, relevant future debits, flexible/protected metadata, and critical-date balances. An event is evidence for a policy effect only when its supplied date/amount and lifecycle state support that interpretation.",""]
    for p,changes in changed.items():
        lines += [f"### {p}",f"Changed requests: {len(changes)}"]
        for x in changes: lines.append(f"- `{x['request_id']}` fields `{','.join(x['fields'])}`; first affected stage `FORECAST` or downstream; candidate debit events `{','.join(e['event_id'] for e in x['events'][:8])}`.")
    lines += ["","## Evidence classification","","Events are classified from profile protection, flexibility, recurrence evidence, lifecycle and provenance. Category names alone do not establish protection. The canonical classifier exposes `PROTECTED`, `FIXED_REQUIRED`, `RECURRING_REQUIRED`, `RECURRING_OPTIONAL`, `ONE_TIME`, `UNSUPPORTED_RECURRING` or `UNKNOWN` with provenance.","","## Safety invariants","","- Adding an excluded pending credit cannot increase capacity.","- Adding a required future debit cannot increase capacity.","- Removing an optional flexible expense cannot decrease capacity.","- Protected/fixed events cannot be removed or modified.","- Self-transfer cannot create wealth.","- Terminal salary cannot create future salary.","- Failed/cancelled lifecycle rows cannot create a second debit.","- Every candidate payment is checked after each movement against minimum balance.","- Repeated runs are deterministic.","","## Decision gate","","No optional-baseline policy is selected solely by score. INCLUDE_ALL_RECURRING is inconsistent with the phrase “before optional spending changes” unless optional events are separately validated; INCLUDE_REQUIRED_ONLY and EXCLUDE_OPTIONAL_FLEXIBLE are semantically close under the current fixed-recurrence model. Because samples do not uniquely establish the distinction, production default remains CURRENT_BEHAVIOR and the boundary remains configurable.","","## Proposed Phase 9 investigation","","Do not change recurrence in Phase 8. Build fixtures before altering weekly, biweekly, 28/30/31-day, monthly day-of-month, month-end clamp, missed-cycle, terminal, amendment or duplicate-lifecycle semantics. Each fixture must identify expected next date, amount, lifecycle state, minimum-balance effect and provenance."]
    (ROOT/"PHASE_8_SEMANTIC_REPAIR.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__":run()
