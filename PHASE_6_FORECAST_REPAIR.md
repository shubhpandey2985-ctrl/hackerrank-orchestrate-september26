# Phase 6 — Controlled Forecast Repair

Status: implementation completed for this controlled upstream change. No
supplied dataset, solved example, expected output, or `code.zip` was modified.

## Checkpoint and baseline

Checkpoint: `phase6-pre-forecast-repair` (`ad6dd80`).

Baseline before the repair:

- Full suite: 39 passed.
- Safe amount: 2/25.
- Status: 10/25.
- Payment method: 11/25.
- Payment plan: 10/25.
- Earliest safe date: 8/25.
- Spending changes: 22/25.
- Mismatch counts: safe 23, status 15, method 14, plan 15, earliest 17,
  changes 3 (explanations are separately serialized and mismatch on all 25).

## Controlled changes

1. Added `estimate_future_amount(recurrence)` as a separate deterministic
   interface. It returns a policy, observations, selected amount and
   confidence.
2. A recurring series is projected only when its source identity is stable and
   all observed home-currency amounts are equal. The selected value is the
   observed fixed amount, not an arithmetic mean or latest observation.
3. Any varying series is retained as
   `RECURRING_AMOUNT_UNRESOLVED` and produces no invented future movement.
4. Historical salary remains `UNSUPPORTED_HISTORICAL_INCOME`; only explicit
   dated confirmed salary evidence is forecast.
5. Exposed the amount-estimation boundary through `ledger.estimate_future_amount`.
6. Added `POLICY_DECISIONS.md`, documenting explicit, example-supported and
   unresolved-policy classifications.

Ranking, output serialization and candidate search were not redesigned.

## Tests added

The semantic-model tests now cover:

- stable fixed recurrence;
- unresolved variable recurrence;
- same-category unrelated descriptions;
- explicit and missed salary cycles;
- terminal salary behavior;
- message-confirmed salary;
- confirmed versus generic scheduled credits;
- pending credit/debit and lifecycle replacement;
- failed/cancelled events;
- Decimal/FX behavior;
- same-day ordering policy;
- 90-day boundary;
- movement-level forecast trace;
- protected/flexible modification eligibility.

Focused semantic/adversarial run: **36 passed**.
Complete suite: **45 passed**.

## Before / after evaluation

| Field | Before | After | Change |
|---|---:|---:|---:|
| safe amount | 2/25 | 2/25 | unchanged |
| status | 10/25 | 10/25 | unchanged |
| payment method | 11/25 | 12/25 | +1 |
| payment plan | 10/25 | 11/25 | +1 |
| earliest safe date | 8/25 | 8/25 | unchanged |
| spending changes | 22/25 | 22/25 | unchanged |

Total exact field matches improved by **2**, regressed by **0**, and remained
unchanged for **4** fields. Eleven requests had safe-amount values changed by
the upstream forecast; only two downstream exact fields improved, and no
field-match count regressed.

The changed safe amounts were requests 02, 06, 07, 11, 13, 14, 15, 18, 20,
22 and 25. The only downstream row whose candidate changed was request 11:
the stable-amount rule allowed the full-payment candidate, improving its
method and plan matches. Its status and earliest date remain mismatches, so
this is not evidence for a request-specific rule.

## First-divergence analysis

| Observed change | First changed stage | Explanation |
|---|---|---|
| Safe amount values on 11 requests | RECURRENCE → FORECAST | Varying source series stopped producing an inferred amount; the capacity query then changed deterministically. |
| Request 11 method/plan improvement | FORECAST → CANDIDATE | Candidate feasibility changed after the upstream forecast; ranking itself was not altered. |
| Request 11 status unchanged | CANDIDATE/DEADLINE | The selected full-payment candidate still maps to the existing status policy; no downstream patch was made. |
| Request 11 earliest date changed | FORECAST → EARLIEST_DATE | Earliest scans the corrected forecast independently; it remains semantically unresolved against the sample. |
| No other field-match changes | — | No ranking, validator or serializer behavior was changed. |

No regression requires a downstream workaround. The remaining mismatch counts
are still dominated by forecast semantics: safe amount 23, earliest date 17,
status 15, method 13, plan 14 and changes 3.

## Remaining unresolved semantics

- recurrence observation threshold, gap tolerance, month-end and missed-cycle
  rules;
- whether a repeated but variable essential series should be forecast at all;
- generic scheduled-credit usability;
- optional-spending baseline semantics;
- same-day settlement ordering (current explicit policy is credits before
  debits before plan payment);
- failed/cancelled replacement timing when no live replacement facts exist;
- safe-after-deadline status mapping;
- flexible-action tie-breaking;
- decimal trailing-zero serialization.

## Decision gate

The repair is an upstream semantic correction, not a submission-readiness
claim. The score does not establish that the fixed-series rule is the hidden
truth; it only shows that removing unsupported amount inference improves two
downstream fields without regressions. A further forensic pass is justified
before changing optional-baseline, recurrence-calendar, scheduled-credit or
deadline policies.
