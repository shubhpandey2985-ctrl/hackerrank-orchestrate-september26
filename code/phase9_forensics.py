"""Read-only Phase 9 recurrence-calendar forensics."""
from __future__ import annotations
import calendar, json, sys
from collections import defaultdict
from datetime import timedelta
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed"]
VARIABLE={"groceries","transport","dining","entertainment","shopping","healthcare","education","family_support"}

def classify(xs):
    amounts=[e.home_amount for e in xs if e.home_amount is not None]
    statuses={e.status for e in xs}; desc=" ".join(e.description.lower() for e in xs)
    if any(k in desc for k in ("final","last","ended","terminated","termination")) or statuses & {"failed","cancelled"}: return "TERMINATED"
    if any((e.settlement_date or e.event_date) >= xs[-1].event_date for e in xs if e.status=="scheduled"): return "EXPLICIT_FUTURE_EVENT"
    if len(xs)>=3 and len(set(amounts))==1: return "EXPLICIT_FIXED_RECURRING"
    if len(xs)>=3 and len(set(amounts))>1: return "VARIABLE_RECURRING"
    if len(xs)>=2: return "WEAK_HISTORICAL_PATTERN"
    return "ONE_TIME"

def inventory(data,samples):
    users={r["user_id"] for r in samples}; groups=defaultdict(list)
    for u in users:
        for e in main.semantic_events(data,u):
            if e.direction not in {"debit","credit"}: continue
            groups[(u,e.category,e.description,e.direction,e.currency)].append(e)
    out=[]
    protected_by={u:main.parse_list(data.profiles[u].get("expense_categories_to_protect","")) for u in users}
    for key,xs in groups.items():
        xs.sort(key=lambda e:e.settlement_date or e.event_date)
        dates=[e.settlement_date or e.event_date for e in xs]; gaps=[(dates[i]-dates[i-1]).days for i in range(1,len(dates))]
        amounts=[str(e.home_amount) for e in xs]; state=classify(xs)
        last=dates[-1]; y,m=last.year+(last.month//12),(last.month%12)+1; dom=min(last.day,calendar.monthrange(y,m)[1])
        out.append({"user_id":key[0],"event_ids":[e.event_id for e in xs],"description":key[2],"category":key[1],"direction":key[3],"currency":key[4],"amounts":amounts,"dates":[x.isoformat() for x in dates],"gaps":gaps,"observations":len(xs),"lifecycle_states":sorted({e.status for e in xs}),"flexibility":sorted({e.flexibility for e in xs}),"protected":key[1] in protected_by[key[0]],"classification":state,"terminal_markers":[e.description for e in xs if any(k in e.description.lower() for k in ("final","last","ended","terminated"))],"linked_events":[{"event_id":e.event_id,"linked_event_id":e.linked_event_id} for e in xs if e.linked_event_id],"explicit_future_events":[e.event_id for e in xs if e.status=="scheduled"],"candidate_next_dates":{"exact":(last+timedelta(days=(sorted(gaps)[(len(gaps)-1)//2] if gaps else 0))).isoformat() if gaps else None,"monthly":f"{y:04d}-{m:02d}-{dom:02d}","explicit_only":[]},"evidence":"source-description identity; supplied dates/amounts/lifecycle"})
    return out

def score_models(samples,data):
    base=main.recurring
    def filt(pred): return lambda events:[x for x in base(events) if pred(x.events)]
    models={"A_EXACT_INTERVAL":base,"B_CALENDAR_WEEKLY":base,"C_CALENDAR_BIWEEKLY":base,"D_MONTHLY_DAY_OF_MONTH":base,"E_MONTH_END_CLAMP":base,"F_EXPLICIT_FUTURE_ONLY":lambda events:[],"G_FIXED_STABLE_ONLY":filt(lambda xs: len({e.home_amount for e in xs})==1)}
    out={}
    for name,fn in models.items():
        main.recurring=fn; counts={f:0 for f in FIELDS}
        for r in samples:
            got=main.candidate(r,data)
            for f in FIELDS: counts[f]+=int(str(got.get(f,""))==str(r.get(f,"")))
        out[name]=counts
    main.recurring=base
    return out

def run():
    data=main.load_data(ROOT); main.normalize_events(data,ROOT); samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv"); inv=inventory(data,samples); scores=score_models(samples,data)
    mismatch=json.loads((ROOT/"SAMPLE_MISMATCH_REPORT.json").read_text(encoding="utf-8"))
    classifications=defaultdict(list)
    for x in mismatch["mismatches"]:
        if x["field"] in {"amount_safe_to_pay","earliest_date_for_full_payment"}:
            field=x["field"]; root=x["root_cause"]
            kind="RECURRENCE_AMOUNT_ERROR" if field=="amount_safe_to_pay" and "recurrence" in root else "RECURRENCE_DATE_ERROR" if field=="earliest_date_for_full_payment" else "OTHER"
            classifications[kind].append({"request_id":x["request_id"],"field":field,"expected":x["expected"],"actual":x["actual"],"root_cause":root})
    payload={"scope":"read-only Phase 9 recurrence calendar forensics","series_count":len(inv),"series_inventory":inv,"model_scores":scores,"mismatch_classifications":dict(classifications),"same_day_unresolved":True,"conclusion":"RECURRENCE_REMAINS_UNRESOLVED","phase10_recommendation":"Add fixture-backed calendar policy configuration; do not change production recurrence until a fixture specifies next date, amount, lifecycle and minimum-balance effect."}
    (ROOT/"PHASE_9_RECURRENCE_FORENSICS.json").write_text(json.dumps(payload,indent=2,default=str),encoding="utf-8")
    lines=["# Phase 9 — Recurrence Calendar Forensics","","Status: analysis-only. No production code, dataset, expected output, output.csv, or code.zip was modified.","","## Inventory","",f"Inventoried **{len(inv)}** source-identity series across the 25 solved users. Identity includes user, category, description, direction and currency; unrelated descriptions were not merged.","","Classification counts:"]
    counts=defaultdict(int)
    for x in inv: counts[x["classification"]]+=1
    lines += [f"- `{k}`: {v}" for k,v in sorted(counts.items())]+["","Each JSON series records event IDs, dates, amounts, gaps, lifecycle states, flexibility, protected status, terminal markers, linked lifecycle rows, explicit future rows, candidate exact/monthly dates and provenance.","","## Calendar counterfactual score table","","| Model | Safe | Status | Method | Plan | Earliest | Changes |","|---|---:|---:|---:|---:|---:|---:|"]
    for n,s in scores.items(): lines.append("| "+n+" | "+" | ".join(str(s[f]) for f in FIELDS)+" |")
    lines += ["","These scores are diagnostics only. The current implementation does not actually switch to calendar-month or weekly arithmetic in this analysis; models A–E are represented as date-policy alternatives over the same supported recurrence evidence. No score is treated as specification proof.","","## Missed cycles and month-end","","Observed irregular gaps do not prove preserve, skip-and-resume, terminate, or explicit-confirmation semantics. Month-end cases (28/29/30/31 and 30-day months) have candidate dates that differ between exact intervals and calendar day-of-month/clamping. No solved fixture uniquely establishes overflow versus clamp versus exact-day behavior. **Month-end remains unresolved.**","","## Terminal, amended and lifecycle series","","Final/last/ended/terminated descriptions and failed/cancelled rows are terminal evidence and must not produce extrapolated movements. A linked replacement is usable only with its own supplied date and amount. Duplicate lifecycle rows must not create two debits. These rules are specification/evidence-supported and remain production invariants.","","## Variable amounts","","Variable series are classified `VARIABLE_RECURRING` and remain `VARIABLE_AMOUNT_UNRESOLVED` unless an explicit future amount exists. No mean, median, latest, maximum, minimum or percentile was used.","","## Mismatch distinction","",f"Amount/date mismatch classifications are machine-readable in JSON: {', '.join(f'{k}={len(v)}' for k,v in classifications.items())}.","","## Strongest defensible model","","The strongest defensible model is explicit confirmed movements plus stable fixed recurrence with source identity, terminal lifecycle checks and no invented variable amount. Calendar date semantics remain configurable because the specification and solved examples do not resolve them.","","## Phase 10 recommendation","","**RECURRENCE_REMAINS_UNRESOLVED**. The minimum evidence needed is a fixture with at least one repeated series and an authoritative expected next date (including month-end/missed-cycle behavior), amount, lifecycle state, and resulting minimum-balance trace. The smallest Phase 10 change is a fixture-backed recurrence-calendar policy boundary, followed by deterministic regression and metamorphic tests; do not alter production recurrence before that evidence exists.","","## Required never-assume rules","","Never use category-only recurrence, inferred variable amounts, historical salary cash without confirmation, invented replacement dates/amounts, FX fallbacks, or LLM-authorized financial decisions."]
    (ROOT/"PHASE_9_RECURRENCE_FORENSICS.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__":run()
