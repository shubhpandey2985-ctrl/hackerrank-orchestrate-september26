# Repair Progress

This log records only the repair phase. Supplied dataset files and expected
sample outputs are not modified.

| Step | Changes | Tests | Before match rate | After match rate | New regressions | Root cause confirmed? |
|---|---|---|---|---|---|---|
| Baseline | No production change; forensic baseline | `python code/evaluation.py` | safe 3/25; status 14/25; method 16/25; plan 11/25; earliest 6/25; changes 22/25 | — | — | Forecast/recurrence and downstream feasibility suspected |

Detailed entries will be appended after each repair step and its focused,
regression, and 25-example evaluation runs.

| Step 1-2 | Added explicit `cash_state` classification; broadened recurrence identity to category/direction/currency; forecasted repeated variable categories with Decimal means; separated baseline safe-amount simulation from optional flexible spending; repaired flexible partial-plan invariant; replaced arbitrary eight-action truncation with latest-obligation representatives and minimal-action stopping. | Focused adversarial tests passed; full suite 32 passed; 25-example evaluation completed | safe 3/25; status 14/25; method 16/25; plan 11/25; earliest 6/25; changes 22/25 | safe 2/25; status 16/25; method 17/25; plan 12/25; earliest 10/25; changes 22/25 | Safe amount regressed by one match; no test regressions. Broadened recurrence remains over/under-conservative on several sample profiles and requires further forensic calibration before treating as final. | Upstream recurrence/forecast explains many downstream date/status/method changes; exact variable-spend policy remains unresolved. |
| Step 2 lifecycle refinement | Suppressed recurrence extrapolation after terminal payroll descriptions (`final`, `last`, `ended`, `termination`). | New terminal-payroll regression plus full suite 32 passed; 25-example evaluation completed | safe 2/25; status 16/25; method 17/25; plan 12/25; earliest 10/25; changes 22/25 | safe 2/25; status 17/25; method 18/25; plan 13/25; earliest 11/25; changes 22/25 | No test regressions; runtime remains deterministic. | Confirmed one systemic lifecycle defect: invented future salary after final payroll caused downstream affordability/method/date errors. |
| Steps 3-4 | Rebuilt safe-amount queries on a complete Decimal simulation with optional flexible spending excluded from the baseline capacity query; kept earliest-date scanning independent and deadline-aware. Added explicit employer-message salary credits, lower-median cadence handling for missed cycles, and output-only preservation of meaningful requested amount precision. | Focused salary/Decimal/deadline tests; full suite 32 passed; 25-example evaluation completed | safe 2/25; status 17/25; method 18/25; plan 13/25; earliest 11/25; changes 22/25 | safe 2/25; status 15/25; method 17/25; plan 14/25; earliest 9/25; changes 22/25 | No test regressions; status/earliest moved backward on some examples after conservative evidence treatment and requires further audit. | Confirmed message-confirmed salary and final-payroll lifecycle as upstream causes; safe/earliest policy still needs calibration against protected versus optional obligations. |
| Step 5-10 | Flexible candidate pruning now uses latest obligation identities, enumerates stop and reduce alternatives, rejects duplicate-event combinations, and stops at the first feasible minimal-action cardinality. Late wait fallback requires deadline and full-payment preference. | Full suite 32 passed; 25-example evaluation completed | safe 2/25; status 17/25; method 18/25; plan 13/25; earliest 11/25; changes 22/25 | safe 2/25; status 15/25; method 17/25; plan 14/25; earliest 9/25; changes 22/25 | No test regressions; late-deadline policy reduced visible sample status matches. | Flexible search is bounded by an explicit minimal-action tie policy; late-deadline mapping remains an intentional unspecified-policy choice. |
| Step 10 | Added deterministic request-text precision preservation for requested full-payment amounts and exact output-only formatting fallback. | Full suite 32 passed; evaluation completed | plan 13/25; formatting differences present | plan 14/25; request 06/21-style trailing-zero plans improved | No test regressions. | Serialization is separate from financial arithmetic. |

## Current final repair-pass snapshot

Latest complete run: full suite `32 passed`; 25-example evaluation completed;
forensic report regenerated. Current field matches are safe amount `2/25`,
status `15/25`, payment method `17/25`, payment plan `14/25`, earliest safe date
`9/25`, and spending changes `22/25`. The arithmetic/date fields remain below
submission quality, so this is explicitly not a readiness declaration. The
remaining mismatches are retained in `SAMPLE_MISMATCH_REPORT.md/.json` for the
next repair iteration.

## Phase 4 semantic-model implementation

Created the requested `semantic-model-preimplementation` Git checkpoint before
code changes. Replaced the unsupported variable-spend arithmetic mean with
explicit `RecurrenceEvidence`; variable amounts and historical salary amounts
remain unresolved rather than generating invented future movements. Added
lifecycle status precedence, canonical event classification, and movement-level
`forecast_trace` audit records. Added four semantic-model regression tests and
retained all existing invariants.

Focused semantic tests: 12 passed. Full suite: 39 passed. 25-example semantic
model run: safe amount 2/25, status 10/25, payment method 11/25, payment plan
10/25, earliest safe date 8/25, spending changes 22/25. The downstream
regressions are recorded in `SEMANTIC_MODEL_TEST_REPORT.md`; no sample-specific
patches were applied. Remaining unresolved semantics are listed in
`SPECIFICATION_RECONSTRUCTION.md`.

## Phase 6 controlled forecast repair

Created checkpoint `phase6-pre-forecast-repair` (`ad6dd80`) before production
changes. Added a separate `estimate_future_amount` interface and now project a
recurring series only when its source identity and every observed home amount
are stable. Varying series are recorded as `RECURRING_AMOUNT_UNRESOLVED`; no
mean, median, maximum, minimum, percentile or latest-value substitution is
used. Added `POLICY_DECISIONS.md` and focused regression coverage.

Focused tests: 36 passed. Full suite: 45 passed. Before → after sample matches:
safe amount 2/25 → 2/25; status 10/25 → 10/25; payment method 11/25 → 12/25;
payment plan 10/25 → 11/25; earliest date 8/25 → 8/25; spending changes
22/25 → 22/25. Exact field matches improved by 2, regressed by 0, and four
fields were unchanged. Remaining mismatches and first-divergence categories
are documented in `PHASE_6_FORECAST_REPAIR.md`.
