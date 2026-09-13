# Phase 16 Decision

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
