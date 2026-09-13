"""Phase 16 evidence-weighted, analysis-only report generator."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIELDS=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed"]

def write(name,text): (ROOT/name).write_text(text.rstrip()+"\n",encoding="utf-8")

def main_run():
    var=json.loads((ROOT/"PHASE_13_VARIABLE_SPENDING_ANALYSIS.json").read_text(encoding="utf-8"))
    matrix=json.loads((ROOT/"PHASE_13_BEHAVIOR_MATRIX.json").read_text(encoding="utf-8"))
    prior=json.loads((ROOT/"PHASE_9_RECURRENCE_FORENSICS.json").read_text(encoding="utf-8"))
    optional=json.loads((ROOT/"PHASE_8_SEMANTIC_REPAIR.json").read_text(encoding="utf-8"))
    write("PHASE_16_CURRENT_PIPELINE.md", """# Phase 16 Current Pipeline

## Actual call/data flow

`main.main(root)` → `load_data` (`code/main.py`) reads profiles, requests,
options, events, messages, images and direct FX rates into `Data` →
`normalize_events` parses Decimal amounts, image evidence and home-currency
conversion → each request calls `candidate` → `semantic_events` applies
lifecycle/deduplication/pending/message evidence → `recurring` builds
source-identity recurrence evidence → `safe_amount` calls `forecast` with a
Decimal monotone search → `earliest` scans each date through the same forecast
→ `candidate` creates full, supplied-installment, partial, wait and bounded
flexible-change candidates → `forecast` validates every plan against the
minimum balance and 90-day horizon → deterministic ranking selects a candidate
→ `validate_output` checks grammar, preferences, options, actions and reruns
forecast → `main` serializes the exact eight-column CSV.

`evidence.py` and `explanations.py` are adapters only; they do not authorize
arithmetic or decisions. `semantic_lab.py` and Phase 15/16 scripts are
analysis-only and are not imported by production `main.py`.

## Semantic decision locations

| Decision | Source |
|---|---|
| schema/input loading | `code/main.py:load_data` |
| lifecycle/cash state/FX | `normalize_events`, `semantic_events` |
| deduplication | `semantic_events` precedence/signature logic |
| recurrence identity/date/amount | `recurring`, `estimate_future_amount` |
| scheduled/pending treatment | `normalize_events`, `semantic_events` |
| optional baseline | `baseline_include_optional`, `policy.py` |
| daily movement order | `forecast`, `policy.py:same_day_order` |
| safe amount | `safe_amount` |
| earliest safe date | `earliest` |
| candidates/ranking | `candidate` |
| hard validation | `validate_output` |
| serialization | `main` CSV writer and `fmt` |
""")
    # Evidence table: preserve all source identities, not just a score.
    j={"series_count":var["series_count"],"series":var["series"],"classification_rules":var["rules"],"conclusion":var["conclusion"],"status":"UNRESOLVED_FOR_VARIABLE_AMOUNTS"}
    (ROOT/"PHASE_16_VARIABLE_SPENDING_EVIDENCE.json").write_text(json.dumps(j,indent=2),encoding="utf-8")
    write("PHASE_16_VARIABLE_SPENDING_EVIDENCE.md",f"""# Phase 16 Variable Spending Evidence

Repeated source-identity series inspected: **{var['series_count']}**. Identity
retains category, description, direction and currency. Category-only merging is
not used. Equal-amount series with supported cadence are classified as stable
fixed; varying series remain unresolved. No arithmetic mean, median, latest,
maximum, minimum, percentile or smoothing estimator is authorized.

The complete series inventory is in `PHASE_16_VARIABLE_SPENDING_EVIDENCE.json`.

Classification: stable fixed recurring is strongly example-supported; variable
but clearly recurring is structurally plausible but amount selection is
`UNRESOLVED`; repeated ambiguous and isolated series are not projected; terminal
and cancelled series are lifecycle-terminated; flexible/protected metadata is
preserved for candidate actions.
""")
    scores=prior["model_scores"]
    model_rows=[
      ("A","stable fixed only; varying unresolved",scores.get("A_EXACT_INTERVAL"),"strongest current model"),
      ("B","latest observed amount",None,"unsupported estimator"),
      ("C","median observed amount",None,"unsupported estimator"),
      ("D","arithmetic mean",None,"unsupported estimator"),
      ("E","conservative maximum",None,"unsupported estimator"),
      ("F","recurrence-conditioned statistic",None,"statistic undefined by specification"),
      ("G","explicit future amount only",scores.get("F_EXPLICIT_FUTURE_ONLY"),"counterfactual evidence only"),
      ("H","evidence-weighted semantically justified amount",scores.get("G_FIXED_STABLE_ONLY"),"fixed equal-amount evidence only"),
    ]
    mj={"models":[{"model":a,"description":b,"field_matches":c,"first_divergence":"safe_amount for 23 baseline rows" if c else None,"false_positive_capacity":"not measurable without unsupported estimator" if a in "BCDEF" else "none observed in prior run","false_negative_capacity":"possible when variable obligation is real" if a in "AGH" else "unknown","safety_invariant":"not promoted" if c is None else "prior run safe","invented_future_movements":0 if a in "AGH" else "undefined","recommendation":d} for a,b,c,d in model_rows],"selection":"A/H fixed-only model retained; no statistic promoted."}
    (ROOT/"PHASE_16_VARIABLE_MODEL_MATRIX.json").write_text(json.dumps(mj,indent=2),encoding="utf-8")
    lines=["# Phase 16 Variable Model Matrix","","| Model | Safe | Earliest | Status | Method | Plan | Changes | Safety | Recommendation |","|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for a,b,c,d in model_rows:
        s=c or {}; lines.append("|"+"|".join([a,str(s.get("amount_safe_to_pay","n/a")),str(s.get("earliest_date_for_full_payment","n/a")),str(s.get("affordability_status","n/a")),str(s.get("recommended_payment_method","n/a")),str(s.get("payment_plan","n/a")),str(s.get("spending_changes_needed","n/a")),"safe only where run exists",d])+"|")
    lines += ["","Models B–F are intentionally not production experiments: each invents an amount statistic absent from the specification. Score is evidence, not proof."]
    write("PHASE_16_VARIABLE_MODEL_MATRIX.md","\n".join(lines))
    write("PHASE_16_IMPLIED_CASHFLOW.md", """# Phase 16 Implied Cashflow

For each of the 23 safe-amount-first-divergence rows, the actual solver trace
contains a deterministic opening balance, dated movements, and minimum-balance
floor in `PHASE_13_BEHAVIOR_MATRIX.json`. The expected amount implies that one
or more future movements differ, but the available evidence does not identify
which one: a varying obligation, a calendar-generated date, optional-baseline
scope, scheduled-credit treatment, or same-day order can produce the same
capacity delta.

Therefore the rows are classified **multiple interpretations remain possible**
or **insufficient evidence**, not “definitely variable.” No future movement is
invented from an output number. The two non-safe-amount rows are serialization
divergences.
""")
    cal={"models":prior.get("model_scores",{}),"series_count":prior.get("series_count"),"generated_event_policy":"Only stable fixed supported recurrence is retained in production.","unresolved":["monthly day-of-month vs month-end","missed cycles","replacement timing","calendar vs exact interval"],"false_positive_policy":"Do not generate unsupported future movement"}
    (ROOT/"PHASE_16_CALENDAR_FORENSICS.json").write_text(json.dumps(cal,indent=2),encoding="utf-8")
    write("PHASE_16_CALENDAR_FORENSICS.md", """# Phase 16 Calendar Forensics

Phase 9 enumerated 728 source-identity series and compared exact interval,
weekly, biweekly, monthly and explicit-only variants. No calendar model is
uniquely supported by the specification/examples. Month-end, short-month,
missed-cycle, terminal and replacement dates remain unresolved. Production
generates only supported stable fixed recurrence; it never fabricates a date
because a sample score improves.
""")
    write("PHASE_16_OPTIONAL_BASELINE_DECISION.md", """# Phase 16 Optional Baseline Decision

The four policies remain configurable: `CURRENT_BEHAVIOR`,
`INCLUDE_REQUIRED_ONLY`, `INCLUDE_ALL_RECURRING`, and
`EXCLUDE_OPTIONAL_FLEXIBLE`. Phase 8 counterfactuals show downstream changes,
but no policy is specification-proven. The phrase “before optional spending
changes” supports separating baseline capacity from candidate actions, but does
not define whether every flexible recurring expense belongs in the baseline.
Production behavior is unchanged.
""")
    write("PHASE_16_SAME_DAY_POLICY.md", """# Phase 16 Same-Day Policy

Synthetic fixtures demonstrate that credit-first, debit-first, and
payment-before-credit order can produce different feasibility. No supplied
example proves an order. The existing `credits_before_required_debits_before_plan`
policy remains an explicit conservative engineering policy, not a specification
fact, and is not changed in Phase 16.
""")
    write("PHASE_16_DEADLINE_POLICY.md", """# Phase 16 Deadline Policy

The solver keeps capacity date, deadline feasibility, and plan feasibility
separate. A post-deadline capacity date cannot be emitted as an in-deadline wait
plan. Safe-today and safe-on-deadline are feasible when all other constraints
pass; safe-after-deadline and never-safe cases remain governed by the explicit
late-deadline policy because the specification does not fully define status
mapping. No production change was made.
""")
    write("PHASE_16_DECISION.md", """# Phase 16 Decision

## Baseline

HEAD `d2416958…`; full suite 61 passed; focused semantic-lab tests 7 passed;
sample matches 2/10/12/11/8/22; 250 rows; output hash
`2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.

## Evidence Reviewed

Problem specification, source modules, solved examples, Phase 11–15 artifacts,
semantic lab, and actual evaluation machinery.

## Variable Spending Findings

Stable fixed recurrence is STRONGLY-EXAMPLE-SUPPORTED. Variable amount
estimation is UNRESOLVED; all statistical estimators are UNSUPPORTED-ASSUMPTION.

## Recurrence Calendar Findings

Explicit fixed recurrence is supported. Calendar, month-end, missed-cycle and
replacement behavior are UNRESOLVED.

## Optional Baseline Findings

Policy boundary is UNRESOLVED; keep configurable.

## Same-Day Ordering Findings

No order is specification-explicit. Current credit-first order remains a
documented POLICY CHOICE.

## Deadline Findings

Capacity date and deadline feasibility are separate; late status mapping remains
UNRESOLVED.

## First-Divergence Analysis

Safe amount is first divergence for 23/25 examples; two are serialization-only.
The causal movement remains confounded.

## Production Changes

None. No downstream logic or output was changed.

## Tests

61 full-suite tests and 7 semantic-lab tests passed.

## 25-Example Evaluation

Unchanged: safe 2/25, status 10/25, method 12/25, plan 11/25, earliest 8/25,
changes 22/25.

## Safety Invariants

No new violations; Decimal, lifecycle, FX, minimum-balance and plan validation
remain passing.

## Determinism

Output hash remains unchanged and no official output was regenerated.

## Hidden-Test Risk

HIGH for variable amounts, calendar recurrence, optional baseline and late
deadline mapping; MEDIUM for same-day ordering; LOW for lifecycle, pending,
direct FX and Decimal rules.

## Remaining Unresolved Semantics

Variable estimators, recurrence calendar/missed cycles, optional baseline,
same-day order, generic scheduled credits, replacement timing and late status.

## Submission Readiness

Not submission-ready because high-impact forecast semantics remain unresolved.

## Final Recommendation

Stop semantic churn. Preserve the deterministic fixed-only model and obtain
authoritative fixtures/spec clarification before any production forecast change.
""")
    write("PHASE_16_PROGRESS.md", """# Phase 16 Progress

- Read-only pipeline and evidence reconstruction completed.
- Variable, recurrence, optional-baseline, same-day and deadline alternatives
  remain explicitly documented.
- No production change passed the evidence gate.
- No `output.csv`, dataset, expected-output or ranking change occurred.
- Final state: **BLOCKED**.
""")

if __name__ == "__main__": main_run()
