"""Read-only Phase 7 boundary semantics analysis."""
from __future__ import annotations
import json, sys, csv, calendar
from collections import defaultdict
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","earliest_date_for_full_payment","affordability_status","recommended_payment_method","payment_plan","spending_changes_needed"]

def score(samples,data):
    out={f:0 for f in FIELDS}
    for r in samples:
        got=main.candidate(r,data)
        for f in FIELDS: out[f]+=int(str(got.get(f,""))==str(r.get(f,"")))
    return out

def safe_mode(user,req,data,optional,recurrence=None):
    base=main.recurring
    if recurrence: main.recurring=recurrence
    try:
        lo=Decimal("0"); hi=main.D(req["requested_amount"]); rd=main.dt(req["request_date"])
        for _ in range(80):
            mid=((lo+hi)/2).quantize(main.CENT)
            if mid<=lo: break
            if main.forecast(user,rd,data,((rd,mid),),(),optional)[0]: lo=mid
            else: hi=mid
        return lo
    finally: main.recurring=base

def earliest_mode(user,req,data,optional,recurrence=None):
    base=main.recurring
    if recurrence: main.recurring=recurrence
    try:
        rd=main.dt(req["request_date"]); amount=main.D(req["requested_amount"])
        for i in range(main.DEFAULT_POLICY.forecast_days):
            day=rd+timedelta(days=i)
            if main.forecast(user,rd,data,((day,amount),),(),optional)[0]: return day.isoformat()
        return ""
    finally: main.recurring=base

def variant_score(samples,data,optional,recurrence=None):
    old_safe,old_earliest=main.safe_amount,main.earliest
    main.safe_amount=lambda u,r,d,c=():safe_mode(u,r,d,optional,recurrence)
    main.earliest=lambda u,r,d,c=(): (main.dt(x) if (x:=earliest_mode(u,r,d,optional,recurrence)) else None)
    try:return score(samples,data)
    finally:main.safe_amount,main.earliest=old_safe,old_earliest

def calendars(data,samples):
    users={r["user_id"] for r in samples}; groups=defaultdict(list)
    for u in users:
        for e in main.semantic_events(data,u):
            if e.direction not in {"debit","credit"}: continue
            groups[(u,e.category,e.description,e.direction,e.currency)].append(e)
    out=[]
    for key,xs in groups.items():
        xs.sort(key=lambda e:e.settlement_date or e.event_date)
        if len(xs)<2: continue
        dates=[e.settlement_date or e.event_date for e in xs]; gaps=[(dates[i]-dates[i-1]).days for i in range(1,len(dates))]; cadence=sorted(gaps)[(len(gaps)-1)//2]
        last=dates[-1]; y,m=last.year+(last.month//12),(last.month%12)+1; day=min(last.day,calendar.monthrange(y,m)[1])
        out.append({"series_id":"|".join(map(str,key)),"source_events":[e.event_id for e in xs],"observed_dates":[x.isoformat() for x in dates],"observed_gaps":gaps,"amounts":[str(e.home_amount) for e in xs],"cadence_days":cadence,"candidate_next_dates":{"exact":(last+timedelta(days=cadence)).isoformat(),"calendar_month":f"{y:04d}-{m:02d}-{day:02d}","month_end_clamp":f"{y:04d}-{m:02d}-{day:02d}","missed_cycle_preserve":(last+timedelta(days=cadence)).isoformat(),"missed_cycle_recover":(last+timedelta(days=cadence)).isoformat(),"explicit_future_only":[]},"flexibility":sorted({e.flexibility for e in xs})})
    return out

def scheduled(data,samples):
    users={r["user_id"] for r in samples}; out=[]
    for u in users:
        for e in data.events[u]:
            if e.direction!="credit": continue
            if e.status=="pending": cat="PENDING"
            elif e.status=="scheduled" and e.event_type=="income": cat="SCHEDULED_CONFIRMED"
            elif e.status=="scheduled": cat="GENERIC_SCHEDULED"
            elif e.status=="settled": cat="EXPLICIT_CONFIRMED"
            else: cat="HISTORICALLY_INFERRED"
            out.append({"user_id":u,"event_id":e.event_id,"category":cat,"date":(e.settlement_date or e.event_date).isoformat(),"amount":str(e.home_amount),"description":e.description})
    return out

def same_day(data,samples):
    users={r["user_id"] for r in samples}; out=[]
    for u in users:
        by=defaultdict(list)
        for e in main.semantic_events(data,u): by[e.settlement_date or e.event_date].append(e)
        for day,xs in by.items():
            if len(xs)>1 and {e.direction for e in xs}>={"credit","debit"}: out.append({"user_id":u,"date":day.isoformat(),"events":[e.event_id for e in xs]})
    return out

def ties(report):
    out=[]
    for r in report["requests"]:
        groups=defaultdict(list)
        for a in r["context"].get("candidate_audit",[]):
            if a.get("rank_key") is not None: groups[tuple(a["rank_key"])].append(a)
        for k,xs in groups.items():
            # Only ties involving flexible action sets are relevant here.
            if len(xs)>1 and any(a.get("changes") for a in xs): out.append({"request_id":r["request_id"],"published_keys":list(k),"candidates":[{z:a.get(z) for z in ("label","method","option_id","plan","changes")} for a in xs]})
    return out

def run():
    data=main.load_data(ROOT); main.normalize_events(data,ROOT); samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv"); report=json.loads((ROOT/"SAMPLE_MISMATCH_REPORT.json").read_text(encoding="utf-8")); base=main.recurring
    fixed=lambda events:[x for x in base(events) if x.amount_policy=="SUPPORTED_FIXED_AMOUNT"]
    models={"A optional included":variant_score(samples,data,True),"B optional excluded":variant_score(samples,data,False),"C explicitly fixed recurrence only":variant_score(samples,data,False,fixed)}
    deadline=[]; stages=defaultdict(list)
    for r in report["requests"]:
        c=r["context"]; req=c["request"]
        if not (r["fields"]["affordability_status"]["match"] and r["fields"]["earliest_date_for_full_payment"]["match"]):
            deadline.append({"request_id":r["request_id"],"capacity_date":c["actual"].get("earliest_date_for_full_payment", ""),"deadline":req["desired_completion_date"],"expected_status":req["affordability_status"],"actual_status":c["actual"].get("affordability_status",""),"candidate_completion_date":c["actual"].get("payment_plan","none")})
        for f in FIELDS:
            if not r["fields"].get(f,{}).get("match",True):
                stage="FORECAST" if f=="amount_safe_to_pay" else "EARLIEST_DATE" if f=="earliest_date_for_full_payment" else "CANDIDATE"
                if r["request_id"] not in stages[stage]: stages[stage].append(r["request_id"])
    payload={"scope":"read-only Phase 7 boundary semantics","optional_baseline_models":models,"recurrence_calendar":calendars(data,samples),"scheduled_credits":scheduled(data,samples),"same_day_cases":same_day(data,samples),"flexible_ties":ties(report),"deadline_status_cases":deadline,"first_divergence_groups":dict(stages)}
    (ROOT/"PHASE_7_BOUNDARY_FORENSICS.json").write_text(json.dumps(payload,indent=2,default=str),encoding="utf-8")
    lines=["# Phase 7 — Boundary Semantics Forensic Isolation","","Status: analysis-only. No production code, datasets, expected outputs, or code.zip were modified.","","## Optional-baseline counterfactuals","","| Model | Safe | Earliest | Status | Method | Plan | Changes |","|---|---:|---:|---:|---:|---:|---:|"]
    for n,s in models.items(): lines.append("| "+n+" | "+" | ".join(str(s[f]) for f in FIELDS)+" |")
    lines += ["","MODEL A includes optional spending; MODEL B is the current excluded-optional policy; MODEL C uses only explicit fixed recurrence. COUNTERFACTUAL SCORE != SPECIFICATION PROOF.","","## Recurrence calendar table","","| Series | Source events | Dates | Gaps | Amounts | Cadence | Candidate next dates | Flexibility |","|---|---|---|---|---|---:|---|---|"]
    for x in payload["recurrence_calendar"]: lines.append("| "+" | ".join(str(x[k]).replace("|","\\|") for k in ("series_id","source_events","observed_dates","observed_gaps","amounts","cadence_days","candidate_next_dates","flexibility"))+" |")
    lines += ["","## Scheduled-credit classification","","| Category | Count | Treatment |","|---|---:|---|"]
    counts=defaultdict(int)
    for x in payload["scheduled_credits"]: counts[x["category"]]+=1
    treatment={"EXPLICIT_CONFIRMED":"usable on supplied settlement date","SCHEDULED_CONFIRMED":"usable when explicitly confirmed","GENERIC_SCHEDULED":"unresolved; conservative exclusion","PENDING":"excluded from capacity","HISTORICALLY_INFERRED":"not usable without confirmation"}
    for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} | {treatment.get(k,'not usable')} |")
    lines += ["","## Same-day order","",f"Mixed credit/debit dates found: {len(payload['same_day_cases'])}. No solved fixture uniquely distinguishes settlement order. **SAME_DAY_ORDER = UNRESOLVED**; existing policy is unchanged.","","## Deadline/status isolation","","| Request | Capacity date | Deadline | Expected status | Current status | Candidate completion |","|---|---|---|---|---|---|"]
    for x in payload["deadline_status_cases"]: lines.append("| "+" | ".join(str(x[k]) for k in ("request_id","capacity_date","deadline","expected_status","actual_status","candidate_completion_date"))+" |")
    lines += ["","Textually defensible alternatives are capacity-after-deadline → affordable_later or not_affordable; no capacity within horizon → not_affordable. Samples do not uniquely resolve the late-capacity boundary.","","## Flexible ties","",f"Published-key ties involving flexible actions found: {len(payload['flexible_ties'])}. No unresolved tie is converted into an official rule.","","## Cross-impact matrix","","| Boundary | Safe | Earliest | Status | Method | Plan | Changes | Evidence |","|---|---|---|---|---|---|---|---|","| Optional baseline | high | high | downstream | downstream | downstream | medium | specification wording + samples |","| Recurrence calendar | high | high | downstream | downstream | downstream | medium | cadence evidence; calendar undefined |","| Scheduled credits | medium | medium | medium | medium | medium | low | confirmed salary vs generic scheduled |","| Same-day order | possible | possible | downstream | downstream | downstream | low | no isolating fixture |","| Deadline/status | none | none | high | high | high | none | late-capacity boundary unresolved |","| Flexible ties | none | none | low | medium | high | high | no resolving fixture |","","## First-divergence priority",""]
    for stage,ids in payload["first_divergence_groups"].items(): lines.append(f"- **{stage}**: {', '.join(ids)}")
    lines += ["","Remaining mismatches begin in RECURRENCE/FORECAST and propagate to EARLIEST_DATE/CANDIDATE/DEADLINE. Do not patch downstream fields.","","## Final conclusion","","1. Largest upstream blast radius: optional-baseline treatment and recurrence-calendar semantics.","2. Evidence: these boundaries affect every 90-day capacity query; the specification does not define variable amount or calendar thresholds.","3. Confidently implementable: explicit confirmed movements, stable fixed recurrence, lifecycle exclusions, pending rules, direct FX and Decimal arithmetic.","4. Keep configurable: optional baseline, recurrence calendar, generic scheduled credits, same-day order, late deadline mapping and flexible ties.","5. Never introduce category-only recurrence, inferred amounts, historical salary cash, FX fallbacks, replacement timing, or LLM-authorized plans.","6. Phase 8 should change one upstream boundary at a time and add invariant/differential tests first.","7. Guard with fixed/variable recurrence, month-end, missed-cycle, pending/lifecycle, deadline, same-day and tie tests.","","COUNTERFACTUAL SCORE != SPECIFICATION PROOF."]
    (ROOT/"PHASE_7_BOUNDARY_FORENSICS.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__": run()
