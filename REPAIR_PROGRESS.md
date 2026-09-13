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

## Phase 8 controlled semantic repair

Created checkpoint `phase8-pre-semantic-repair` (`d241695`) before changes.
Added an explicit `OPTIONAL_BASELINE_POLICY` configuration boundary with
`CURRENT_BEHAVIOR`, `INCLUDE_REQUIRED_ONLY`, `INCLUDE_ALL_RECURRING`, and
`EXCLUDE_OPTIONAL_FLEXIBLE` variants. The production default remains
`CURRENT_BEHAVIOR`; recurrence-calendar semantics and downstream ranking were
not changed.

Counterfactual results showed `INCLUDE_REQUIRED_ONLY` and
`EXCLUDE_OPTIONAL_FLEXIBLE` each changed one request and improved method/status
diagnostics, while `INCLUDE_ALL_RECURRING` changed eight requests without an
evidentiary basis. No policy was selected solely by score. Added policy
classification/provenance and Phase 8 metamorphic boundary tests.

Focused tests: 38 passed. Full suite: 47 passed. Production-default sample
matches remain safe 2/25, status 10/25, method 12/25, plan 11/25, earliest
8/25, changes 22/25. Artifacts: `PHASE_8_SEMANTIC_REPAIR.md` and `.json`.

## Phase 9 recurrence calendar forensics

Analysis-only pass completed; no production or dataset changes. Inventoried 728
source-identity series across the 25 solved users, including lifecycle,
flexibility, protection, terminal markers, linked replacements and candidate
calendar dates. Compared exact-interval, weekly, biweekly, monthly,
month-end-clamp, explicit-future-only and stable-fixed conceptual models.

Conclusion: `RECURRENCE_REMAINS_UNRESOLVED`. The strongest defensible baseline
remains explicit confirmed movements plus stable fixed recurrence, with no
invented variable amounts. Month-end, missed-cycle, calendar cadence and
replacement timing require fixture-backed evidence before production changes.
Artifacts: `PHASE_9_RECURRENCE_FORENSICS.md` and `.json`.

## Phase 10 downstream decision forensics

Analysis-only pass completed with the forecast and ledger frozen. The first
divergence grouping places 23 requests at `SAFE_AMOUNT`; two requests are
output-only mismatches in the current field comparison. Earliest-date,
candidate, status, method and plan differences are downstream symptoms of the
frozen upstream capacity/date contract. Candidate audits, preference
eligibility, validation/rejection data and ranking keys were captured without
changing the decision pipeline.

Recommendation: freeze the decision pipeline and document unresolved forecast
semantics before any Phase 11 downstream repair. Artifacts:
`PHASE_10_DECISION_FORENSICS.md` and `.json`.

## Phase 11 decision-pipeline freeze and hidden-test hardening

Baseline frozen at `d2416958be49f40ef9a15fefe3a6795d6d34a7e1`: 38 focused
tests, 47 full tests, sample matches safe 2/25, status 10/25, method 12/25,
plan 11/25, earliest 8/25, changes 22/25. Output has 250 rows and deterministic
SHA-256 `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.

Added seven defensive hardening tests covering malformed inputs, pending and
required-debit monotonicity, lifecycle exclusion, protected/fixed immutability,
output contract and missing FX. Full suite after hardening: 54 passed. No
production decision logic changed. The project remains **BLOCKED** because
safe-amount and earliest-date forecast semantics are unresolved upstream; no
downstream repair or packaging is justified.

## Phase 12 forecast contract resolution

Read-only forecast-contract reconstruction completed. Status remains
**UNRESOLVED**: the strongest defensible model is explicit confirmed cash
movements plus supported stable fixed recurrence, Decimal arithmetic, direct
supplied FX, strict lifecycle handling and deterministic horizon simulation.
Variable amounts, recurrence calendars, optional-baseline scope, generic
scheduled credits, same-day ordering, replacement timing, late-deadline status
mapping and decimal presentation remain unsupported and configurable. The
current baseline was not changed. Focused tests: 45 passed; full suite: 54
passed; evaluator unchanged at safe 2/25, status 10/25, method 12/25, plan
11/25, earliest 8/25, changes 22/25. Output hash remains
`2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.

Artifacts: `FORECAST_CONTRACT.md`, `FORECAST_CONTRACT.json`,
`PHASE_12_FORENSICS.md`, `PHASE_12_FORENSICS.json`, and
`PHASE_12_DECISION.md`. No dataset, expected-output, output.csv, production
logic, or packaging changes were made.

## Phase 13 evidence-to-behavior reconstruction

Completed the controlled, analysis-first reconstruction. The 25-request matrix
and JSON traces show safe amount as the first divergence for 23 requests and
serialization for two. Variable spending was inventoried by source identity;
no arithmetic mean, median, latest, maximum, minimum, or category-only rule was
introduced. Existing counterfactual scores were preserved as evidence only.

Outcome: **PARTIALLY_RESOLVED**. Supported lifecycle, confirmed-credit, fixed
recurrence, FX, Decimal and safety semantics remain frozen; unresolved
variable amounts, recurrence calendar, optional baseline, scheduled credits,
same-day ordering, replacement timing, deadline mapping and decimal
presentation remain explicit policies. No production, dataset, expected-output,
or output.csv changes were made. Full suite remains 54 passed and output hash
remains `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.

Artifacts: `PHASE_13_BASELINE.md`, `PHASE_13_FORECAST_BEHAVIOR_MATRIX.md`,
`PHASE_13_FIRST_DIVERGENCE.md`, `PHASE_13_VARIABLE_SPENDING_ANALYSIS.md`,
`PHASE_13_COUNTERFACTUAL_MODELS.md`, `PHASE_13_EVALUATION.md/.json`, and
`PHASE_13_DECISION.md`. The requested `phase13-analysis-only` tag could not be
created because the checkout denied `.git/refs/tags` lock creation; HEAD was
left unchanged and the failure is documented in the baseline.

## Phase 14 forecast semantic resolution

Baseline reconfirmed at `d2416958…`: 54 full tests, 45 focused tests, sample
matches safe 2/25, status 10/25, method 12/25, plan 11/25, earliest 8/25,
changes 22/25, and output hash
`2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.

Generated the formal movement contract and counterfactual/forensic reports.
Every raw event has explicit inclusion/exclusion reasoning and provenance.
The 23 safe-amount divergences remain upstream but observationally confounded;
no variable estimator, calendar guess, generic scheduled-credit inclusion,
replacement invention, or downstream ranking change is defensible. No
production, dataset, expected-output, or `output.csv` change was made.

Outcome: **BLOCKED** pending fixture-backed evidence that isolates the
remaining forecast semantics. Git checkpoint creation was attempted and
failed only because the checkout denied `.git` ref-lock creation.

## Phase 15 fixture-driven semantic discovery

Created an independent Decimal semantic lab and 66 minimal synthetic fixtures
covering variable spending, recurrence calendars, income, optional baseline,
pending events, same-day ordering, replacements, deadlines, FX and Decimal
boundaries. Lab tests pass 7/7. Resolved behavior is documented for lifecycle,
pending credits, confirmed income, explicit replacements, direct FX and Decimal
arithmetic; unresolved behavior remains isolated for variable amounts, calendar
recurrence, optional baseline, same-day ordering and late-deadline mapping.

No production logic, ranking, datasets, expected outputs or `output.csv` were
changed. Final phase state: **BLOCKED** pending authoritative evidence that
selects among the competing unresolved models.

## Phase 16 evidence-weighted forecast reconstruction

Reverified the actual production call graph and formal forecast state. Stable
fixed recurrence remains the strongest defensible upstream model; variable
estimators and calendar, optional-baseline, same-day and late-deadline
alternatives remain unresolved. Generated the required Phase 16 evidence,
model-matrix, implied-cashflow, calendar, optional-baseline, same-day,
deadline, decision and progress artifacts. No production, ranking, dataset,
expected-output or `output.csv` changes were made. Full suite remains 61
passed; lab tests 7 passed; final state **BLOCKED**.

## Phase 17 forecast contract implementation

Formalized the forecast contract and production-change gate. Added an
analysis-only model lab and three same-day contract tests; full suite is now 64
passed and semantic-lab tests 10 passed. No production semantic change was
promoted because variable estimators and calendar alternatives remain
unsupported or unresolved. Sample evaluation and output hash are unchanged;
datasets, expected outputs and `output.csv` remain untouched.

## Phase 18 authoritative evidence recovery

Audited repository specification, schemas, comments, fixtures, solved examples,
implementation and Phase 1–17 artifacts. No hidden authoritative rule was found
for variable amounts, recurrence calendars, optional baseline, generic
scheduled credits, same-day ordering, replacement timing or late status. The
identifiability matrix shows these semantics remain observationally confounded.

Decision: **AUTHORITATIVE_EVIDENCE_MISSING** / `NO_PRODUCTION_CHANGE_JUSTIFIED`.
Full suite remains 64 passed, semantic-lab 10 passed, sample matches and output
hash are unchanged, and no production/data/output changes were made.

## Phase 19 defensible production policy and hardening

Centralized unresolved policy boundaries, documented the proven core, added 60
deterministic adversarial fixture cases plus invariant checks, and validated
the production output. Full suite: 128 passed; adversarial suite: 74 passed;
semantic lab: 10 passed. Output remains 250 rows with unchanged hash.

The submission gate reached **READY_FOR_PACKAGING**. `code.zip` was created
with production code, the required usage report, README and image-evidence
cache; it excludes datasets and forensic artifacts. Independent packaged run
produced 250 valid rows with the same output hash.
