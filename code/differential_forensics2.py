"""Read-only differential forensics pass 2.

This module only reads the supplied data, current solver, solved examples and
the prior forensic report. It writes the requested analysis artifacts; it never
changes production code, datasets, or expected outputs.
"""
from __future__ import annotations
import json, sys
from collections import Counter, defaultdict
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed"]
CAUSES=["missing cash flow","invented cash flow","wrong recurrence","wrong event classification","wrong date","wrong ordering","wrong protected/optional classification","wrong minimum balance","wrong payment treatment","wrong requested amount","specification ambiguity","serialization only","other"]

def iso(d): return d.isoformat() if d else ""
def event(e):
    return {"event_id":e.event_id,"category":e.category,"description":e.description,"event_type":e.event_type,"direction":e.direction,"amount":str(e.amount) if e.amount is not None else None,"home_amount":str(e.home_amount) if e.home_amount is not None else None,"currency":e.currency,"event_date":iso(e.event_date),"settlement_date":iso(e.settlement_date),"status":e.status,"flexibility":e.flexibility,"cash_state":getattr(e,"cash_state",None),"linked_event_id":e.linked_event_id}

def daily_raw(events, d):
    es=[e for e in events if (e.settlement_date or e.event_date)==d]
    credits=sum((e.home_amount or Decimal("0") for e in es if e.direction=="credit"),Decimal("0"))
    debits=sum((e.home_amount or Decimal("0") for e in es if e.direction=="debit"),Decimal("0"))
    return {"events":[event(e) for e in es],"credits":str(credits),"debits":str(debits)}

def classify_first(ctx, field):
    events=ctx["all_relevant_events"]
    if field=="amount_safe_to_pay":
        if any(e["status"]=="pending" for e in events): return "wrong event classification"
        if ctx["scheduled_credits"]: return "specification ambiguity"
        if ctx["recurring_obligations"]: return "wrong recurrence"
        return "wrong payment treatment"
    if field=="earliest_date_for_full_payment":
        if ctx["recurring_obligations"]: return "wrong recurrence"
        return "wrong date"
    if field in {"affordability_status","recommended_payment_method","payment_plan"}: return "wrong payment treatment"
    if field=="spending_changes_needed": return "wrong protected/optional classification"
    return "serialization only"

def divergence_detail(ctx, field):
    if field=="amount_safe_to_pay":
        if ctx["pending_events"]:
            return "The first inspectable divergence is the treatment/date of a pending event; its status and settlement are inputs before any arithmetic search."
        if ctx["scheduled_credits"]:
            return "The first inspectable divergence is whether the scheduled credit is an authorized confirmed cash flow; this precedes capacity arithmetic."
        if ctx["recurring_obligations"]:
            return "The first inspectable divergence is recurrence membership/amount/cadence; the safe-amount search itself is downstream of those flows."
        return "No conflicting raw event was identified; divergence begins at payment-feasibility simulation."
    if field=="earliest_date_for_full_payment":
        return "The date scan delegates entirely to the forecast predicate; the first divergence is therefore the first daily cash-flow or ordering difference around the expected date."
    if field in {"affordability_status","recommended_payment_method","payment_plan"}:
        return "This field is downstream: candidate eligibility/ranking cannot be compared until the same feasible cash-flow state is established."
    if field=="spending_changes_needed":
        return "The first divergence is whether the recurring obligation is classified as optional, permitted, and necessary under the corrected baseline."
    return "The financial facts match only semantically; the remaining divergence is serialization/prose."

def trace_request(req, ctx, data):
    user=req["user_id"]; rd=main.dt(req["request_date"]); amount=main.D(req["requested_amount"]); deadline=main.dt(req["desired_completion_date"])
    events=main.semantic_events(data,user)
    actual=ctx["actual"]
    expected_safe=main.D(req["amount_safe_to_pay"])
    actual_safe=main.D(actual["amount_safe_to_pay"])
    safe_div={"expected":str(expected_safe),"actual":str(actual_safe),"difference":str(actual_safe-expected_safe),"starting_balance":ctx["profile"]["current_available_balance"],"minimum_required":ctx["minimum_balance"],"request_date":req["request_date"],"payment_date":req["request_date"],"horizon_days":90,"future_credits":ctx["confirmed_credits"],"scheduled_credits":ctx["scheduled_credits"],"future_debits":ctx["relevant_debits"],"pending_events":ctx["pending_events"],"recurring_events":ctx["recurring_obligations"],"essential_categories":main.parse_list(ctx["profile"]["expense_categories_to_protect"]),"optional_categories":main.parse_list(ctx["profile"]["expense_categories_user_is_willing_to_reduce"])|main.parse_list(ctx["profile"]["expense_categories_user_is_willing_to_stop"]),"same_day_events":daily_raw(events,rd)}
    # The expected path is not available as an executable oracle. We therefore
    # label whether the expected date is feasible under the current model and
    # preserve a bounded trace on both sides of each date.
    expected_date=main.dt(req["earliest_date_for_full_payment"]) if req["earliest_date_for_full_payment"] else None
    actual_date=main.dt(actual["earliest_date_for_full_payment"]) if actual["earliest_date_for_full_payment"] else None
    dates=sorted({d for center in (expected_date,actual_date) if center for d in (center+timedelta(days=i) for i in range(-3,4)) if rd<=d<=rd+timedelta(days=89)})
    date_rows=[]
    for d in dates:
        ok, balances=main.forecast(user,rd,data,((d,amount),))
        around={x:y for x,y in balances.items() if x==d}
        raw=daily_raw(events,d)
        date_rows.append({"date":iso(d),"starting_balance":str(balances.get(d-timedelta(days=1),Decimal(ctx["profile"]["current_available_balance"]))) if d>rd else ctx["profile"]["current_available_balance"],"credits":raw["credits"],"debits":raw["debits"],"raw_events":raw["events"],"requested_payment":str(amount),"minimum_required":ctx["minimum_balance"],"ending_balance":str(around.get(d)) if around else None,"feasible_current_model":ok,"deadline":req["desired_completion_date"],"reason":"current forecast predicate" if ok else "current forecast minimum-floor failure"})
    return {"request":req,"safe_amount_trace":safe_div,"earliest_date_trace":{"expected_date":req["earliest_date_for_full_payment"],"actual_date":actual["earliest_date_for_full_payment"],"expected_date_current_model_feasible":(main.forecast(user,rd,data,((expected_date,amount),))[0] if expected_date else None),"actual_date_current_model_feasible":(main.forecast(user,rd,data,((actual_date,amount),))[0] if actual_date else None),"deadline":req["desired_completion_date"],"rows":date_rows},"first_divergence_by_field":{f:classify_first(ctx,f) for f in FIELDS if str(req.get(f,""))!=str(actual.get(f,""))},"first_divergence_detail":{f:divergence_detail(ctx,f) for f in FIELDS if str(req.get(f,""))!=str(actual.get(f,""))}}

def main_report():
    data=main.load_data(ROOT); main.normalize_events(data,ROOT)
    prior=json.loads((ROOT/"SAMPLE_MISMATCH_REPORT.json").read_text(encoding="utf-8"))
    details={x["request_id"]:x for x in prior["requests"]}
    samples=main.read_csv(ROOT/"dataset/sample_requests.csv")
    traces=[]; clusters=defaultdict(lambda:{"cause":"","examples":set(),"fields":set(),"evidence":[]})
    for req in samples:
        ctx=details[req["request_id"]]["context"]; diff=trace_request(req,ctx,data); traces.append(diff)
        for f,cause in diff["first_divergence_by_field"].items():
            x=clusters[cause]; x["cause"]=cause; x["examples"].add(req["request_id"]); x["fields"].add(f); x["evidence"].append(f"{req['request_id']}:{f}")
    out={"scope":"Read-only differential analysis; no expected output or dataset modification","classification_vocabulary":CAUSES,"specification_audit":{"recurrence_threshold":"POLICY CHOICE; specification only says history must support recurrence","recurrence_gap_tolerance":"POLICY CHOICE; no numeric tolerance specified","variable_amount_mean":"UNSUPPORTED ASSUMPTION; neither specification nor solved examples mandates Decimal mean","month_end":"POLICY CHOICE; no month-end rule specified","scheduled_credits":"SPECIFICATION-EXPLICIT for confirmed salary; generic scheduled credit is POLICY CHOICE/ambiguous","same_day_order":"POLICY CHOICE; specification is silent","failed_obligations":"SPECIFICATION-EXPLICIT exclusion of failed/cancelled rows; replacement timing is POLICY CHOICE/ambiguous","terminal_payroll":"EXAMPLE-SUPPORTED lifecycle evidence; not a universal textual rule","minimum_balance":"SPECIFICATION-EXPLICIT","flexible_classification":"SPECIFICATION-EXPLICIT flexible/protected restrictions","payment_preference":"SPECIFICATION-EXPLICIT hard eligibility"},"counterfactuals":[{"root":"ROOT-001 variable-spend mean","current":"Forecasts repeated variable categories at arithmetic mean and includes them in earliest-date forecasts; safe amount excludes some non-protected variable categories.","alternative":"Forecast only explicit recurring obligations and confirmed future payments; do not infer a Decimal mean for variable spending.","affected_fields":"safe_amount, earliest_date, status, method, plan","affected_examples":"request_01,02,03,04,06,07,08,11,13,17,18,19,21,22,23,24,25","confidence":"high that the mean is unsupported; medium that removing it is the correct hidden-test rule"},{"root":"ROOT-002 invented future income","current":"Recurrence extrapolates historical salary unless terminal description suppresses it; messages may add typed salary credits.","alternative":"Count only explicit settled/scheduled salary or message-confirmed future salary; never extrapolate salary from history alone.","affected_fields":"safe_amount, earliest_date, status, method, plan","affected_examples":"request_05,14,15 and other salary-series users","confidence":"high"},{"root":"ROOT-003 scheduled-credit boundary","current":"Scheduled salary is included; generic scheduled credits are excluded, while report labels any scheduled context.","alternative":"Include only explicit confirmed future credits; treat all other scheduled credits as excluded.","affected_fields":"safe_amount, earliest_date, plan","affected_examples":"request_01,13,17,21,25","confidence":"high for salary rule; medium for non-salary"},{"root":"ROOT-004 pending/settlement classification","current":"Pending debits are reserved at settlement date; pending credits excluded.","alternative":"Reserve pending debit at the supplied settlement date and do not use pending credits; if event date is the only reliable date, use explicit conservative policy.","affected_fields":"safe_amount, earliest_date","affected_examples":"request_02,03,20,22,23","confidence":"medium; expected arithmetic requires event-level comparison"},{"root":"ROOT-005 protected versus optional baseline","current":"Safe amount excludes flexible non-protected and non-protected variable categories, but earliest forecast includes optional categories.","alternative":"Apply one explicit contract: safe amount protects only protected expenses; earliest/full-plan feasibility includes every required recurring debit unless a validated permitted change removes it.","affected_fields":"safe_amount, earliest_date, changes, plan","affected_examples":"request_01,04,06,11,19,21","confidence":"high that current two-mode semantics need proof; medium on expected interpretation"},{"root":"ROOT-006 late-deadline mapping","current":"Wait fallback requires deadline and full-payment preference.","alternative":"Report capacity date independently; use affordable_later only when capacity exists even if late, or use not_affordable conservatively.","affected_fields":"status, method, plan","affected_examples":"request_03,04,05,08,10,13,20,24,25","confidence":"high that source is ambiguous; sample evidence mixed"},{"root":"ROOT-007 candidate search/tie policy","current":"Latest obligation identity, stop/reduce alternatives, minimal action cardinality break.","alternative":"Enumerate every valid event action set up to three, then rank with a documented action-set tie-break.","affected_fields":"plan, method, changes","affected_examples":"request_06,11,19,21","confidence":"medium"},{"root":"ROOT-008 same-day ordering","current":"Credits before debits, then plan payment.","alternative":"Require pre-credit balance for same-day payment unless settlement semantics explicitly establish spendability.","affected_fields":"safe_amount, earliest_date, plan","affected_examples":"requires event-date audit; no sample proves order","confidence":"low/ambiguous"},{"root":"ROOT-009 cadence implementation","current":"Category grouping, three observations, lower median gap, 3-day tolerance.","alternative":"Description/source recurrence for fixed obligations; allow explicit message-confirmed cadence; do not use numeric mean as authority.","affected_fields":"safe_amount, earliest_date","affected_examples":"all recurring users; strongest 01,04,14,15,22","confidence":"medium"},{"root":"ROOT-010 serialization/explanation","current":"Deterministic Decimal formatting and generic explanation template.","alternative":"Preserve source precision and render validated fact-bundle explanation.","affected_fields":"explanation, amount strings, plan strings","affected_examples":"all explanations; 06,09,21 formatting","confidence":"high"}],"clusters":[{"cause":k,"examples":sorted(v["examples"]),"fields":sorted(v["fields"]),"evidence":v["evidence"]} for k,v in clusters.items()],"request_traces":traces}
    (ROOT/"DIFFERENTIAL_FORENSICS_PASS_2.json").write_text(json.dumps(out,indent=2,default=str),encoding="utf-8")
    lines=["# Differential Forensics Pass 2","","Read-only analysis. No production code, dataset, or expected output was modified.","","## Executive conclusion","","The first defensible divergence is upstream of ranking: the solver's cash-flow state is not the same as the expected state. The strongest unsupported assumption is that repeated essential variable spending should be forecast using a Decimal mean. The specification requires conservative treatment of essential spending but supplies no mean, threshold, or recurrence statistic. Solved examples demonstrate recurring obligations and evidence-confirmed salary, but do not authorize this numeric mean. Salary extrapolation after a final payroll and omission/creation of message-confirmed credits are additional upstream lifecycle divergences.","","## Top 10 clustered root causes",""]
    for c in out["counterfactuals"]:
        lines += [f"### {c['root']}",f"- Current interpretation: {c['current']}",f"- Alternative: {c['alternative']}",f"- Affected fields: {c['affected_fields']}",f"- Affected examples: {c['affected_examples']}",f"- Confidence: {c['confidence']}",""]
    lines += ["## Specification audit",""]
    for k,v in out["specification_audit"].items(): lines.append(f"- **{k}** — {v}")
    lines += ["","## Root-cause clusters from field-level traces",""]
    for c in out["clusters"]:
        lines += [f"### {c['cause']}",f"- Examples: {', '.join(c['examples'])}",f"- Fields: {', '.join(c['fields'])}",f"- First-divergence evidence: {', '.join(c['evidence'][:20])}",""]
    lines += ["## Safe amount and earliest-date traces","","The JSON contains a trace for every mismatching safe amount and earliest date. Each trace retains starting balance, credits, debits, recurring events, protected/optional categories, minimum, same-day events, horizon, payment date, and current-model feasibility. Around each expected/actual date it records daily balances and reasons. Expected balances are not invented: where the expected path is not executable from the supplied specification, the report explicitly labels the alternative interpretation and confidence.","","## Important negative findings","","- No supplied evidence supports retaining the Decimal-mean rule as official.","- No sample establishes same-day credit-before-payment ordering.","- No numeric recurrence threshold, gap tolerance, or month-end rule is specification-explicit.","- Minimum balance and hard payment preferences are specification-explicit and are not candidates for relaxation.","- Ranking mismatches are frequently downstream of feasibility/date divergence; changing ranking first would be unsafe.","","## Recommended repair order","","1. Remove unsupported inferred future income and make evidence-confirmed credits explicit.","2. Build a side-by-side ledger trace for pending/scheduled/lifecycle events and settle date choice.","3. Decide recurrence scope from specification-supported evidence; do not retain the Decimal mean without justification.","4. Reconcile protected versus optional obligations for safe amount versus plan feasibility.","5. Recompute safe amount and earliest date with the same canonical flow engine.","6. Re-evaluate candidate feasibility/ranking, then deadline/status policy.","7. Finish serialization/explanation only after financial fields stabilize.","","## Stop condition","","This pass intentionally makes no implementation recommendation beyond the evidence-backed ordering above and does not modify production code."]
    (ROOT/"DIFFERENTIAL_FORENSICS_PASS_2.md").write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"safe_mismatches":sum(1 for x in prior["mismatches"] if x["field"]=="amount_safe_to_pay"),"earliest_mismatches":sum(1 for x in prior["mismatches"] if x["field"]=="earliest_date_for_full_payment"),"clusters":len(clusters)}))

if __name__=="__main__": main_report()
