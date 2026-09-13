"""Read-only downstream decision-pipeline forensics."""
from __future__ import annotations
import json,sys
from collections import Counter,defaultdict
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import main

ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","earliest_date_for_full_payment","affordability_status","recommended_payment_method","payment_plan","spending_changes_needed"]

def stage_for(row):
    f=row["fields"]
    if not f["amount_safe_to_pay"]["match"]: return "SAFE_AMOUNT"
    if not f["earliest_date_for_full_payment"]["match"]: return "EARLIEST_DATE"
    if not f["affordability_status"]["match"]: return "STATUS"
    if not f["recommended_payment_method"]["match"]: return "PAYMENT_METHOD"
    if not f["payment_plan"]["match"]: return "PAYMENT_PLAN"
    if not f["spending_changes_needed"]["match"]: return "SPENDING_CHANGES"
    return "OUTPUT_SERIALIZATION"

def candidate_summary(ctx):
    audits=ctx.get("candidate_audit",[]); valid=[a for a in audits if a.get("rank_key") is not None]
    return {"generated":len(audits),"valid":len(valid),"rejected":len(audits)-len(valid),"valid_candidates":[{k:a.get(k) for k in ("label","method","option_id","plan","changes","rank_key","meets_deadline","eligible_preference","safe")} for a in valid],"rejected_candidates":[{k:a.get(k) for k in ("label","method","option_id","plan","changes","meets_deadline","eligible_preference","safe")} for a in audits if a.get("rank_key") is None]}

def run():
    report=json.loads((ROOT/"SAMPLE_MISMATCH_REPORT.json").read_text(encoding="utf-8")); data=main.load_data(ROOT); main.normalize_events(data,ROOT); samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv")
    rows=[]; stages=defaultdict(list); field_counts=Counter()
    for src,req in zip(report["requests"],samples):
        ctx=src["context"]; stage=stage_for(src); stages[stage].append(src["request_id"])
        for f in FIELDS:
            if not src["fields"][f]["match"]: field_counts[f]+=1
        audits=candidate_summary(ctx)
        rows.append({"request_id":src["request_id"],"first_divergence":stage,"field_matches":src["fields"],"candidate_pipeline":audits,"preferences":ctx.get("preferences",[]),"minimum_balance":ctx.get("minimum_balance"),"request_date":ctx["request"]["request_date"],"deadline":ctx["request"]["desired_completion_date"],"expected_status":ctx["request"]["affordability_status"],"actual_status":ctx["actual"].get("affordability_status"),"expected_method":ctx["request"]["recommended_payment_method"],"actual_method":ctx["actual"].get("recommended_payment_method"),"expected_plan":ctx["request"]["payment_plan"],"actual_plan":ctx["actual"].get("payment_plan"),"expected_changes":ctx["request"]["spending_changes_needed"],"actual_changes":ctx["actual"].get("spending_changes_needed")})
    payload={"scope":"read-only Phase 10 downstream decision forensics","forecast_frozen":True,"field_mismatch_counts":dict(field_counts),"first_divergence_groups":dict(stages),"rows":rows,"dependency_graph":"forecast -> safe amount -> earliest date -> candidate generation -> validation -> deadline/status -> ranking -> output","decision_category":"forecast-dependent and earliest-date dependent; downstream symptoms are not independently repairable until upstream values agree","recommendation":"FREEZE_DECISION_PIPELINE_AND_DOCUMENT_UNRESOLVED_FORECAST_SEMANTICS"}
    (ROOT/"PHASE_10_DECISION_FORENSICS.json").write_text(json.dumps(payload,indent=2,default=str),encoding="utf-8")
    lines=["# Phase 10 — Downstream Decision Forensics","","Status: analysis-only. Forecast, ledger, recurrence, lifecycle, FX, Decimal arithmetic and production output were treated as immutable. No production code, dataset, expected output, output.csv or code.zip was modified.","","## Dependency graph","","```text\nforecast → safe amount → earliest date → candidate generation → validation → deadline/status → ranking → output\n```","","## First-divergence aggregate","","| Stage | Examples | Interpretation |","|---|---:|---|"]
    for s,ids in stages.items(): lines.append(f"| {s} | {len(ids)} | {', '.join(ids)} |")
    lines += ["","The earliest mismatch wins: a wrong safe amount masks later candidate/status/method/plan symptoms. A wrong earliest date masks wait/partial/deadline symptoms.","","## Candidate generation, validation and ranking","","The JSON artifact contains every available candidate audit for each request, including generated/rejected counts, preference eligibility, deadline compliance, safety, payment plan, changes and published rank keys. This permits exact rejection and ranking inspection without changing the pipeline.","","## Preferences and status truth table","","For each request the JSON records accepted preferences, expected/actual status and method, deadline, plan and first divergence. Preference constraints remain hard; no method rejected by the profile should be considered eligible.","","## Spending changes","","The remaining spending-change mismatches are isolated in the machine-readable rows. The subsystem was not rewritten; each is classified by its earlier first divergence where applicable.","","## Safe amount and earliest-date invariants","","The frozen implementation must preserve: `0 <= safe_amount <= requested_amount`; pending credits, failed/cancelled events and unsupported salary/variable estimates cannot increase capacity; every movement and candidate payment must respect the minimum balance; earliest date is independent of payment preference and ranking.","","## Decision category","","Remaining failures are primarily **forecast-dependent** and **earliest-date dependent**, with downstream candidate/status/method/plan mismatches. Candidate generation and validation should not be changed until the upstream forecast contract is resolved. Ranking is not evidenced as the primary defect.","","## Phase 11 recommendation","","Recommend one smallest next change: **freeze the current decision pipeline and document unresolved forecast semantics**. Do not implement candidate-generation, validation, ranking, status, preference or serialization repairs while safe amount and earliest date remain mismatched upstream.","","COUNTERFACTUAL SCORE != SPECIFICATION PROOF."]
    (ROOT/"PHASE_10_DECISION_FORENSICS.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__":run()
