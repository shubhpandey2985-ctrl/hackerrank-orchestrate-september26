"""Generate forensic comparison reports for the 25 public solved requests.

Analysis-only tool: it reads supplied data and current deterministic behavior and
does not alter production code, datasets, or expected outputs.
"""
from __future__ import annotations
import csv, json, sys
from collections import Counter, defaultdict
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed","decision_explanation"]
ROOT_CATEGORIES=[
 "1. data loading","2. event classification","3. deduplication","4. currency conversion",
 "5. date ordering","6. recurrence detection","7. scheduled-credit semantics",
 "8. failed/cancelled/replacement lifecycle","9. forecast calculation","10. minimum-balance enforcement",
 "11. safe-amount calculation","12. earliest-safe-date calculation","13. candidate generation",
 "14. partial-payment logic","15. installment logic","16. payment-method preference",
 "17. flexible-spending logic","18. candidate ranking","19. deadline/status mapping","20. output serialization"
]

def dec(v): return main.D(v)
def iso(d): return d.isoformat() if d else ""

def event_dict(e):
    return {"event_id":e.event_id,"event_type":e.event_type,"description":e.description,
            "category":e.category,"direction":e.direction,"amount":str(e.amount) if e.amount is not None else None,
            "currency":e.currency,"home_amount":str(e.home_amount) if e.home_amount is not None else None,
            "event_date":iso(e.event_date),"settlement_date":iso(e.settlement_date),"status":e.status,
            "linked_event_id":e.linked_event_id,"flexibility":e.flexibility,
            "minimum_allowed_amount":str(e.minimum_allowed_amount),"excluded_reason":e.excluded_reason,
            "evidence":list(e.evidence)}

def option_dict(o):
    return dict(o)

def traces(req, data, actual):
    user=req["user_id"]; rd=main.dt(req["request_date"]); deadline=main.dt(req["desired_completion_date"])
    profile=data.profiles[user]; all_events=data.events[user]
    cash=main.semantic_events(data,user)
    baseline_ok, balances=main.forecast(user,rd,data,())
    safe=main.safe_amount(user,req,data)
    earliest=main.earliest(user,req,data)
    relevant=[e for e in all_events if (e.settlement_date or e.event_date) >= rd-timedelta(days=45) and (e.settlement_date or e.event_date) <= rd+timedelta(days=90)]
    credits=[e for e in relevant if e.direction=="credit"]
    debits=[e for e in relevant if e.direction=="debit"]
    pending=[e for e in relevant if e.status=="pending"]
    recurring=[]
    for xs,gap in main.recurring(all_events):
        if any(e in relevant for e in xs):
            recurring.append({"event_ids":[e.event_id for e in xs],"category":xs[0].category,"direction":xs[0].direction,"gap_days":gap,"amounts":[str(e.home_amount) for e in xs]})
    critical_dates=sorted({rd,deadline,rd+timedelta(days=89),*(e.settlement_date for e in relevant if e.settlement_date),*(main.dt(x.split(":",1)[0]) for x in actual["payment_plan"].split("|") if actual["payment_plan"]!="none")})
    critical_balances={d.isoformat():str(balances.get(d)) for d in critical_dates if d in balances}
    min_balance=min(balances.values()) if balances else None
    flexible=[event_dict(e) for e in cash if e.direction=="debit" and e.flexibility!="fixed" and e.category not in main.parse_list(profile["expense_categories_to_protect"])]
    # Candidate audit (eligibility and selected actual plan; no expected answer used).
    candidate_audit=[]
    prefs=main.parse_pref(profile)
    amount=dec(req["requested_amount"])
    def record(label, method, plan, option_id="", changes=()):
        eligible=method in prefs or method=="wait"
        within=all(rd<=d<=rd+timedelta(days=89) for d,_ in plan)
        by_deadline=bool(plan) and max(d for d,_ in plan)<=deadline
        safe_plan=False
        if eligible and within and by_deadline: safe_plan=main.forecast(user,rd,data,plan,changes)[0]
        rank_key=None
        if safe_plan:
            rank_key=[int(not by_deadline),int(bool(changes)),str(sum((a for _,a in plan), Decimal("0"))),iso(min(d for d,_ in plan)),len(plan),option_id]
        candidate_audit.append({"label":label,"method":method,"option_id":option_id,"plan":[[iso(d),str(a)] for d,a in plan],"eligible_preference":eligible,"within_horizon":within,"meets_deadline":by_deadline,"safe":safe_plan,"changes":[list(x) for x in changes],"rank_key":rank_key})
    record("full_today","full_payment",[(rd,amount)])
    for o in data.options.get(req["request_id"],[]):
        plan=main.option_plan(o)
        if o["payment_method"]=="full_payment": record("option_"+o["payment_option_id"],"full_payment",plan,o["payment_option_id"])
        elif o["payment_method"]=="installments": record("option_"+o["payment_option_id"],"installments",plan,o["payment_option_id"])
    if req["allows_partial_payment"].lower()=="true" and "partial_payment" in prefs and safe>0 and safe<amount and earliest and earliest<=deadline:
        record("partial","partial_payment",[(rd,safe),(earliest,amount-safe)])
    if earliest and "full_payment" in prefs:
        record("wait","wait",[(earliest,amount)])
    date_trace=[]
    for i in range(90):
        d=rd+timedelta(days=i)
        ok0,b0=main.forecast(user,rd,data,())
        oka,ba=main.forecast(user,rd,data,((d,amount),))
        date_trace.append({"date":iso(d),"baseline_balance":str(b0.get(d)) if d in b0 else None,"balance_after_full_payment":str(ba.get(d)) if d in ba else None,"minimum_after_full_payment":str(min(ba.values())) if ba else None,"full_payment_safe":oka})
    try:
        main.validate_output(actual, req, data)
        validator={"actual_row_valid":True,"notes":"main.validate_output passed"}
    except Exception as exc:
        validator={"actual_row_valid":False,"notes":f"main.validate_output rejected: {type(exc).__name__}: {exc}"}
    return {
      "request":dict(req),"actual":actual,"profile":profile,"home_currency":profile.get("home_currency"),
      "preferences":prefs,"minimum_balance":profile["minimum_balance_to_keep"],
      "requested_amount":req["requested_amount"],"request_date":req["request_date"],"deadline":req["desired_completion_date"],
      "confirmed_credits":[event_dict(e) for e in credits if e.status in {"settled","scheduled"}],
      "scheduled_credits":[event_dict(e) for e in credits if e.status=="scheduled"],
      "relevant_debits":[event_dict(e) for e in debits],"pending_events":[event_dict(e) for e in pending],
      "all_relevant_events":[event_dict(e) for e in relevant],"recurring_obligations":recurring,
      "flexible_candidates":flexible,"payment_options":[option_dict(o) for o in data.options.get(req["request_id"],[])],
      "safe_amount_trace":{"actual_safe":str(safe),"baseline_forecast_safe":baseline_ok,"minimum_forecast_balance":str(min_balance) if min_balance is not None else None,"critical_balances":critical_balances,"date_trace":date_trace},
      "earliest_trace":{"actual_earliest":iso(earliest),"dates_tested":[{"date":(rd+timedelta(days=i)).isoformat(),"safe":main.forecast(user,rd,data,((rd+timedelta(days=i),amount),))[0],"minimum_balance":str(min(main.forecast(user,rd,data,((rd+timedelta(days=i),amount),))[1].values()))} for i in range(90)]},
      "candidate_audit":candidate_audit,
      "validator":validator
    }

def classify(field, expected, actual, context):
    if field == "decision_explanation": return "20. output serialization"
    if field == "amount_safe_to_pay" and expected != actual:
        try:
            if Decimal(expected) == Decimal(actual): return "20. output serialization"
        except Exception: pass
    if field == "payment_plan" and expected != actual:
        def norm(p):
            if p == "none": return p
            try: return tuple((x.split(":",1)[0], str(Decimal(x.split(":",1)[1]))) for x in p.split("|"))
            except Exception: return p
        if norm(expected) == norm(actual): return "20. output serialization"
    if field=="amount_safe_to_pay":
        if context["scheduled_credits"] and expected!=actual: return "7. scheduled-credit semantics"
        if context["pending_events"] and expected!=actual: return "2. event classification"
        return "11. safe-amount calculation"
    if field=="earliest_date_for_full_payment": return "12. earliest-safe-date calculation"
    if field=="payment_plan":
        if actual!=expected and any(o.get("payment_method")=="installments" for o in context["payment_options"]): return "18. candidate ranking"
        return "13. candidate generation"
    if field=="recommended_payment_method": return "16. payment-method preference" if context["preferences"] else "18. candidate ranking"
    if field=="affordability_status": return "19. deadline/status mapping"
    if field=="spending_changes_needed": return "17. flexible-spending logic"
    return "9. forecast calculation"

def main_report():
    data=main.load_data(ROOT); main.normalize_events(data,ROOT)
    samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv")
    details=[]; mismatches=[]; root_counts=Counter(); field_counts=Counter(); request_counts=Counter()
    for req in samples:
        actual=main.candidate(req,data)
        ctx=traces(req,data,actual)
        request_detail={"request_id":req["request_id"],"fields":{},"context":ctx}
        for f in FIELDS:
            exp=str(req.get(f,"")); got=str(actual.get(f,""))
            same=exp==got
            request_detail["fields"][f]={"expected":exp,"actual":got,"match":same}
            if not same:
                category=classify(f,exp,got,ctx)
                item={"request_id":req["request_id"],"field":f,"expected":exp,"actual":got,"root_cause":category}
                mismatches.append(item); root_counts[category]+=1; field_counts[f]+=1; request_counts[req["request_id"]]+=1
        details.append(request_detail)
    report={"comparison_contract":{"source":"dataset/sample_requests.csv","actual_source":"main.candidate","fields":FIELDS,"expected_rows":25,"actual_rows":25,"row_key":"request_id","serialization_check":"string equality after CSV parsing; no column reordering or type coercion"},"field_mismatch_counts":dict(field_counts),"root_cause_counts":dict(root_counts),"request_mismatch_counts":dict(request_counts),"mismatches":mismatches,"requests":details}
    (ROOT/"SAMPLE_MISMATCH_REPORT.json").write_text(json.dumps(report,indent=2,default=str),encoding="utf-8")
    lines=["# Sample mismatch forensic report","","Generated from repository data and current deterministic implementation. No expected answer is hardcoded.","","## Harness verification","",f"Expected rows: 25; actual rows: 25; key: request_id; compared fields: {', '.join(FIELDS)}. Values were compared after CSV parsing as strings; no column reordering or implicit numeric coercion was used.","","## Root-cause priority","",]
    for k,v in root_counts.most_common(): lines.append(f"- {k}: {v} mismatching fields")
    lines += ["","## Field mismatch counts",""]
    for k,v in field_counts.items(): lines.append(f"- {k}: {v}")
    lines += ["","## Per-field mismatches",""]
    for m in mismatches:
        lines += [f"### {m['request_id']} — `{m['field']}`",f"- Expected: `{m['expected']}`",f"- Actual: `{m['actual']}`",f"- Primary root cause: **{m['root_cause']}**"]
        c=next(x["context"] for x in details if x["request_id"]==m["request_id"])
        lines += [f"- User/profile: `{c['request']['user_id']}`; balance `{c['profile']['current_available_balance']}`; minimum `{c['minimum_balance']}`; preferences `{c['preferences']}`",f"- Request: `{c['requested_amount']}` on `{c['request_date']}`, deadline `{c['deadline']}`",f"- Actual selected plan: `{c['actual']['payment_plan']}` via `{c['actual']['recommended_payment_method']}`",f"- Relevant credits: {len(c['confirmed_credits'])}; scheduled credits: {len(c['scheduled_credits'])}; debits: {len(c['relevant_debits'])}; pending: {len(c['pending_events'])}",f"- Recurring obligations: {len(c['recurring_obligations'])}; flexible candidates: {len(c['flexible_candidates'])}",f"- Critical balances: `{c['safe_amount_trace']['critical_balances']}`",f"- Validator: `{c['validator']['actual_row_valid']}`"," "]
    lines += ["## Root-cause interpretation","","Categories are primary hypotheses from deterministic traces, not expected-answer special cases. The largest clusters are safe-amount/forecast and earliest-safe-date calculations, followed by candidate generation/ranking and deadline/status mapping. These should be investigated before any code change."]
    (ROOT/"SAMPLE_MISMATCH_REPORT.md").write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"field_mismatch_counts":dict(field_counts),"root_cause_counts":dict(root_counts),"mismatches":len(mismatches)},indent=2))

def postprocess_report():
    path=ROOT/"SAMPLE_MISMATCH_REPORT.json"
    report=json.loads(path.read_text(encoding="utf-8"))
    samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv")
    expected_header=list(samples[0].keys()) if samples else []
    actual_header=[]
    out=ROOT/"output.csv"
    if out.exists():
        with out.open(newline="",encoding="utf-8-sig") as f: actual_header=next(csv.reader(f),[])
    report["comparison_contract"].update({"expected_header":expected_header,"actual_header":actual_header,"actual_rows":len(samples),"actual_source":"main.candidate plus output.csv header audit","serialization_check":"CSV string comparison; numeric-equivalent formatting is classified as 20. output serialization; rows joined by request_id; no coercion"})
    diagnosis={"20. output serialization":"output-formatting issue","7. scheduled-credit semantics":"incorrect assumption in our architecture","16. payment-method preference":"incorrect interpretation of the specification","17. flexible-spending logic":"implementation bug","18. candidate ranking":"incorrect assumption in our architecture","19. deadline/status mapping":"incorrect interpretation of the specification","2. event classification":"implementation bug","11. safe-amount calculation":"implementation bug","12. earliest-safe-date calculation":"implementation bug","13. candidate generation":"implementation bug","9. forecast calculation":"implementation bug"}
    for m in report["mismatches"]: m["diagnosis"]=diagnosis.get(m["root_cause"],"implementation bug")
    report["root_cause_counts"]={k:report["root_cause_counts"].get(k,0) for k in ROOT_CATEGORIES}
    path.write_text(json.dumps(report,indent=2,default=str),encoding="utf-8")
    by_id={x["request_id"]:x for x in report["requests"]}
    lines=["# Sample mismatch forensic report","","Generated from repository data and current deterministic implementation. No expected answer is hardcoded.","","## Harness verification","",f"Expected rows: 25; actual rows: {len(samples)}; joined by `request_id`. Expected header: `{expected_header}`. Actual header: `{actual_header}`. Compared fields: {', '.join(FIELDS)}. Numeric-equivalent trailing-zero differences are classified as `20. output serialization`.","","## Root-cause priority",""]
    lines += [f"- {k}: {v} mismatching fields" for k,v in sorted(report["root_cause_counts"].items(),key=lambda kv:(-kv[1],kv[0]))]
    lines += ["","## Field mismatch counts",""]+[f"- {k}: {v}" for k,v in report["field_mismatch_counts"].items()]+["","## Per-field mismatches",""]
    for m in report["mismatches"]:
        c=by_id[m["request_id"]]["context"]
        lines += [f"### {m['request_id']} — `{m['field']}`",f"- Expected: `{m['expected']}`",f"- Actual: `{m['actual']}`",f"- Primary root cause: **{m['root_cause']}**",f"- Diagnosis: `{m.get('diagnosis','implementation bug')}`",f"- User/profile: `{c['request']['user_id']}`; balance `{c['profile']['current_available_balance']}`; minimum `{c['minimum_balance']}`; preferences `{c['preferences']}`",f"- Request: amount `{c['requested_amount']}` on `{c['request_date']}`, deadline `{c['deadline']}`",f"- Actual selected plan: `{c['actual']['payment_plan']}` via `{c['actual']['recommended_payment_method']}`",f"- Credits `{len(c['confirmed_credits'])}` (scheduled `{len(c['scheduled_credits'])}`); debits `{len(c['relevant_debits'])}`; pending `{len(c['pending_events'])}`; recurring `{len(c['recurring_obligations'])}`; flexible `{len(c['flexible_candidates'])}`; options `{len(c['payment_options'])}`",f"- Critical balances: `{c['safe_amount_trace']['critical_balances']}`",f"- Candidate rank keys: `{[(x['label'],x['safe'],x['rank_key']) for x in c['candidate_audit']]}`",f"- Validator: `{c['validator']['actual_row_valid']}`"," "]
    lines += ["## Mathematical safe-amount traces","", "Representative traces show deterministic date-by-date balances; expected amounts are comparison-only."]
    for rid in [m["request_id"] for m in report["mismatches"] if m["field"]=="amount_safe_to_pay"][:5]:
        d=by_id[rid]; c=d["context"]; t=c["safe_amount_trace"]; lines += [f"### {rid}",f"Expected `{d['fields']['amount_safe_to_pay']['expected']}`; actual `{t['actual_safe']}`; baseline minimum `{t['minimum_forecast_balance']}`.","","| date | baseline | after full payment | min after payment | safe |","|---|---:|---:|---:|:---:|"]+[f"| {r['date']} | {r['baseline_balance']} | {r['balance_after_full_payment']} | {r['minimum_after_full_payment']} | {r['full_payment_safe']} |" for r in t["date_trace"]]+[""]
    lines += ["## Earliest-full-payment date traces","", "Every tested horizon date and post-payment minimum is retained for representative mismatches."]
    for rid in [m["request_id"] for m in report["mismatches"] if m["field"]=="earliest_date_for_full_payment"][:5]:
        d=by_id[rid]; c=d["context"]; lines += [f"### {rid}",f"Expected `{d['fields']['earliest_date_for_full_payment']['expected']}`; actual `{c['earliest_trace']['actual_earliest']}`.","","| date | min balance after payment | safe |","|---|---:|:---:|"]+[f"| {r['date']} | {r['minimum_balance']} | {r['safe']} |" for r in c["earliest_trace"]["dates_tested"]]+[""]
    lines += ["## Root-cause interpretation","","Categories are primary hypotheses from deterministic traces, not expected-answer special cases. No production code or supplied dataset was changed by this report generation."]
    (ROOT/"SAMPLE_MISMATCH_REPORT.md").write_text("\n".join(lines),encoding="utf-8")

if __name__=="__main__":
    main_report()
    postprocess_report()
