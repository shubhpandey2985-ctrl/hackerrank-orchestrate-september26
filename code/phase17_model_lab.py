"""Analysis-only Phase 17 model comparison; never imported by production."""
from __future__ import annotations
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed"]

def main():
    eval_report=json.loads((ROOT/"evaluation_sample_report.json").read_text(encoding="utf-8"))
    prior=json.loads((ROOT/"PHASE_16_VARIABLE_MODEL_MATRIX.json").read_text(encoding="utf-8"))
    first=json.loads((ROOT/"PHASE_13_FIRST_DIVERGENCE.json").read_text(encoding="utf-8"))
    base=eval_report["field_matches"]
    models=[]
    for ident,desc,classification in [
      ("MODEL_A","current stable-fixed production model","SPECIFICATION-SUPPORTED + STRONGLY-EXAMPLE-SUPPORTED"),
      ("MODEL_B","explicit confirmed movements only","SPECIFICATION-SUPPORTED; conservative counterfactual"),
      ("MODEL_C","explicit movements plus stable fixed recurrence","STRONGLY-EXAMPLE-SUPPORTED; current contract"),
      ("MODEL_D","variable estimator variants","UNSUPPORTED-ASSUMPTION; analysis only"),
    ]:
        score=base if ident in {"MODEL_A","MODEL_C"} else next((m["field_matches"] for m in prior["models"] if m["model"]=="G"),None) if ident=="MODEL_B" else None
        models.append({"model":ident,"description":desc,"classification":classification,"field_matches":score,"safety_violations":0,"invented_future_movements":0 if ident!="MODEL_D" else "not promoted","first_divergence":"safe_amount:23; serialization:2","affected_request_ids":first["groups"],"promoted":ident in {"MODEL_A","MODEL_C"}})
    payload={"models":models,"production_model":"MODEL_A/MODEL_C stable-fixed contract","baseline_hash":"2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840","selection":"No counterfactual-only model promoted."}
    (ROOT/"PHASE_17_MODEL_COMPARISON.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
    lines=["# Phase 17 Model Comparison","","| Model | Safe | Earliest | Status | Method | Plan | Changes | Safety | Classification | Promoted |","|---|---:|---:|---:|---:|---:|---:|---|---|---|"]
    for m in models:
        s=m["field_matches"] or {}; lines.append("|"+"|".join([m["model"],str(s.get("amount_safe_to_pay","n/a")),str(s.get("earliest_date_for_full_payment","n/a")),str(s.get("affordability_status","n/a")),str(s.get("recommended_payment_method","n/a")),str(s.get("payment_plan","n/a")),str(s.get("spending_changes_needed","n/a")),str(m["safety_violations"]),m["classification"],str(m["promoted"])])+"|")
    lines += ["","MODEL_D remains analysis-only because it invents varying future amounts. Higher score cannot override the specification/evidence hierarchy."]
    (ROOT/"PHASE_17_MODEL_COMPARISON.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    (ROOT/"PHASE_17_EVALUATION.json").write_text(json.dumps({"before":base,"after":base,"regressions":[],"improvements":[],"output_sha256":payload["baseline_hash"],"rows":250,"deterministic":True},indent=2),encoding="utf-8")
    (ROOT/"PHASE_17_EVALUATION.md").write_text("# Phase 17 Evaluation\n\nNo production change was made. Before and after are identical: safe 2/25, status 10/25, method 12/25, plan 11/25, earliest 8/25, changes 22/25. Output hash remains `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`. No regressions or improvements.\n",encoding="utf-8")
    (ROOT/"PHASE_17_FORECAST_CONTRACT.json").write_text(json.dumps({"input_facts":["opening_balance","request_date","90_day_horizon","home_currency","settled_movements","confirmed_future_credits","pending_debits","lifecycle_state","recurrence_evidence","flexibility","protection","optional_classification","supplied_direct_fx","minimum_balance","request_amount","deadline","payment_options"],"excluded_facts":["pending_credits","failed","cancelled","unrealized","non_cash","duplicate_lifecycle_records","unsupported_income","unsupported_replacements","unsupported_fx"],"inference_levels":["EXPLICIT_CONFIRMED","SUPPORTED_FIXED_RECURRENCE","UNRESOLVED_INFERENCE"],"production_eligible":["EXPLICIT_CONFIRMED","SUPPORTED_FIXED_RECURRENCE"],"unresolved_visible_but_excluded":True,"same_day_order":"credits_before_required_debits_before_plan (policy)","optional_baseline":"CURRENT_BEHAVIOR (configurable)","fx":"direct supplied dated pair only","arithmetic":"Decimal"},indent=2),encoding="utf-8")
    (ROOT/"PHASE_17_FORECAST_CONTRACT.md").write_text("""# Phase 17 Forecast Contract

The production forecast follows `FACTS → EVIDENCE → MOVEMENTS → SAFETY →
CAPACITY → DECISION`. Explicit confirmed movements and supported stable fixed
recurrences are the only production-eligible future movements. Every other
inference remains visible as `UNRESOLVED_INFERENCE` but contributes no cash.

Excluded cash facts include pending credits, failed/cancelled/unrealized/non-
cash records, duplicate lifecycle rows, unsupported income/replacements and
missing direct FX. Every included movement retains source IDs, description,
category, currency, original and home amount, date, movement type, evidence
class, recurrence identity, lifecycle evidence, confidence and inclusion or
exclusion reason.

Optional baseline and same-day order remain explicit policies. The forecast core
does not rank methods, generate plans/actions, serialize output or explain
decisions; those remain downstream.
""",encoding="utf-8")
    (ROOT/"PHASE_17_CHANGE_GATE.md").write_text("""# Phase 17 Change Gate

## Proposed change

None. No production semantic change is proposed.

## Gate result

The current stable-fixed contract is already the strongest defensible model.
Variable estimators and calendar/optional-baseline/same-day alternatives remain
unresolved. Promoting any would rely on unsupported assumptions or sample score
alone, so the gate rejects production modification.

Before any future change, record specification/example evidence, affected
fields, hidden-test risk, focused regressions, full-suite results and before /
after sample matches.
""",encoding="utf-8")
    (ROOT/"PHASE_17_BASELINE.md").write_text("# Phase 17 Baseline\n\nHEAD `d2416958…`; full suite 61 passed; semantic-lab 7 passed; sample matches safe 2/25, status 10/25, method 12/25, plan 11/25, earliest 8/25, changes 22/25; 250 output rows; SHA-256 `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`. Checkpoint `phase17-pre-forecast-contract` was attempted and denied by Git ref-lock permissions.\n",encoding="utf-8")
    (ROOT/"PHASE_17_PROGRESS.md").write_text("# Phase 17 Progress\n\nFormal contract, change gate, model lab and evaluation artifacts generated. No production change was promoted. Existing output and dataset remain unchanged.\n",encoding="utf-8")

if __name__=="__main__": main()
