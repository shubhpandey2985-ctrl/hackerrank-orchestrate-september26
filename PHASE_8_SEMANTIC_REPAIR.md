# Phase 8 — Controlled Semantic Repair

Status: one controlled optional-baseline experiment. Recurrence-calendar semantics, ranking, preferences, status mapping, same-day ordering and serialization were not changed.

## Baseline

- Checkpoint before repair: `phase8-pre-semantic-repair` (`d241695`).
- Full suite before repair: 45 passed.
- Baseline matches: safe 2/25, status 10/25, method 12/25, plan 11/25, earliest 8/25, changes 22/25.
- Dataset/sample hashes were captured before the checkpoint and remain unchanged.
- Production default remains `CURRENT_BEHAVIOR`; no policy variant was selected.

## Policy variants

| Policy | Safe | Status | Method | Plan | Earliest | Changes |
|---|---:|---:|---:|---:|---:|---:|
| CURRENT_BEHAVIOR | 2 | 10 | 12 | 11 | 8 | 22 |
| INCLUDE_REQUIRED_ONLY | 2 | 11 | 13 | 11 | 8 | 22 |
| INCLUDE_ALL_RECURRING | 2 | 10 | 12 | 11 | 8 | 22 |
| EXCLUDE_OPTIONAL_FLEXIBLE | 2 | 11 | 13 | 11 | 8 | 22 |

Scores are counterfactual diagnostics, not specification proof. The default remains CURRENT_BEHAVIOR.

## Validation after experiment

- Focused semantic/adversarial tests after the policy boundary: 38 passed.
- Complete suite after the policy boundary: 47 passed.
- Production-default evaluator: safe 2/25, status 10/25, method 12/25, plan
  11/25, earliest 8/25, changes 22/25.
- No recurrence-calendar, ranking, preference, status, same-day or
  serialization behavior was changed.
- Production output is reproducible under the unchanged default.

## Event-level changed results

For every non-default variant, the JSON artifact records all changed requests, relevant future debits, flexible/protected metadata, and critical-date balances. An event is evidence for a policy effect only when its supplied date/amount and lifecycle state support that interpretation.

### INCLUDE_REQUIRED_ONLY
Changed requests: 1
- `request_13` fields `affordability_status,recommended_payment_method,payment_plan,earliest_date_for_full_payment`; first affected stage `FORECAST` or downstream; candidate debit events ``.
### INCLUDE_ALL_RECURRING
Changed requests: 8
- `request_02` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events `event_185`.
- `request_06` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events ``.
- `request_07` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events ``.
- `request_13` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events ``.
- `request_14` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events ``.
- `request_18` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events ``.
- `request_20` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events `event_1786,event_1787`.
- `request_22` fields `amount_safe_to_pay`; first affected stage `FORECAST` or downstream; candidate debit events `event_1961`.
### EXCLUDE_OPTIONAL_FLEXIBLE
Changed requests: 1
- `request_13` fields `affordability_status,recommended_payment_method,payment_plan,earliest_date_for_full_payment`; first affected stage `FORECAST` or downstream; candidate debit events ``.

## Evidence classification

Events are classified from profile protection, flexibility, recurrence evidence, lifecycle and provenance. Category names alone do not establish protection. The canonical classifier exposes `PROTECTED`, `FIXED_REQUIRED`, `RECURRING_REQUIRED`, `RECURRING_OPTIONAL`, `ONE_TIME`, `UNSUPPORTED_RECURRING` or `UNKNOWN` with provenance.

## Safety invariants

- Adding an excluded pending credit cannot increase capacity.
- Adding a required future debit cannot increase capacity.
- Removing an optional flexible expense cannot decrease capacity.
- Protected/fixed events cannot be removed or modified.
- Self-transfer cannot create wealth.
- Terminal salary cannot create future salary.
- Failed/cancelled lifecycle rows cannot create a second debit.
- Every candidate payment is checked after each movement against minimum balance.
- Repeated runs are deterministic.

## Decision gate

No optional-baseline policy is selected solely by score. INCLUDE_ALL_RECURRING is inconsistent with the phrase “before optional spending changes” unless optional events are separately validated; INCLUDE_REQUIRED_ONLY and EXCLUDE_OPTIONAL_FLEXIBLE are semantically close under the current fixed-recurrence model. Because samples do not uniquely establish the distinction, production default remains CURRENT_BEHAVIOR and the boundary remains configurable.

## Proposed Phase 9 investigation

Do not change recurrence in Phase 8. Build fixtures before altering weekly, biweekly, 28/30/31-day, monthly day-of-month, month-end clamp, missed-cycle, terminal, amendment or duplicate-lifecycle semantics. Each fixture must identify expected next date, amount, lifecycle state, minimum-balance effect and provenance.
