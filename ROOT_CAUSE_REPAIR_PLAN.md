# Root-Cause Repair Plan

Status: analysis-only. This document proposes repairs; it does not change the
solver, supplied data, or expected outputs.

## Executive diagnosis and blast-radius order

The mismatch report's labels are field-level symptoms, not proof that each
label is an independent defect. The dominant dependency is:

```text
event/lifecycle classification + recurrence model
        -> dated ledger flows
        -> 90-day forecast and minimum-balance floor
        -> safe amount
        -> earliest safe full-payment date
        -> candidate feasibility
        -> candidate ranking / method / payment plan
        -> deadline status and explanation
```

The repair order is therefore:

1. Forecast inputs and recurrence/essential-spending semantics (upstream of 22
   safe-amount and 19 earliest-date mismatches).
2. Safe-amount and earliest-date calculations as independent, monotonic
   deterministic queries over the corrected forecast.
3. Candidate construction and ranking after feasibility is corrected.
4. Deadline/status mapping after the selected candidate and capacity facts are
   separated.
5. Preference eligibility after candidate feasibility is correct.
6. Flexible-change enumeration and output serialization/explanation cleanup.

The current report classifies 103 field differences when the explanation column
is included. The explanation differs on all 25 rows because the current template
does not reproduce the grounded sample style; those are not evidence of a
financial-arithmetic defect. Numeric-equivalent trailing-zero differences are
separately classified as serialization issues.

## Specification/evidence/policy boundary

| Behavior | Source authority | Repair treatment |
|---|---|---|
| Minimum never breached after every required movement and plan payment | Specification-mandated | Hard validator and forecast invariant |
| Pending debits reserved; pending credits and unsupported gains excluded | Specification-mandated | Canonical ledger state |
| Confirmed salary counted on settlement date | Specification-mandated | Dated credit movement |
| Full/partial/installment preference eligibility and exact plan grammar | Specification-mandated | Candidate eligibility and validator |
| Recurrence only when history supports it; essential variable spend forecast conservatively | Specification-mandated direction; exact threshold unspecified | Configurable, documented recurrence policy |
| Same-day credit/payment order | Unspecified | Explicit conservative policy, fixture-tested |
| Generic scheduled-credit treatment | Partly unspecified | Count only explicitly confirmed future credits |
| Failed replacement date/amount | Unspecified | Never invent; preserve unresolved obligation evidence |
| Safe-after-deadline status mapping | Unspecified boundary | Separate capacity date from recommendation eligibility; conservative documented mapping |
| Decimal scale/trailing zeros | Unspecified, examples are observational | Preserve supplied option text where possible; deterministic Decimal serializer |
| Flexible-set ties | Unspecified | Stable event/action key only after published ranking keys tie |

## A. Earliest-safe-date calculation — priority 1

### Root cause

`main.earliest()` is mechanically consistent with `main.forecast()`, but the
forecast under-represents future required spending. `recurring()` only accepts
three observations for categories whose event type/category is in a narrow
allow-list (`subscription`, `debt_payment`, `income`, `rent`, `utilities`,
`cloud_storage`, `music_subscription`, `streaming`, `gym`, `childcare`,
`debt`). Repeated groceries, transport, dining, healthcare, education, and
other essential variable series are therefore omitted. The resulting earliest
date is often the request date or the next visible salary, instead of the first
date after all projected commitments leave the minimum balance protected.

### Affected examples and fields

Affected examples: `request_02`, `request_03`, `request_04`, `request_05`,
`request_06`, `request_07`, `request_08`, `request_10`, `request_11`,
`request_13`, `request_17`, `request_18`, `request_19`, `request_20`,
`request_21`, `request_22`, `request_23`, `request_24`, `request_25`.

Affected field: `earliest_date_for_full_payment` (19/25). Downstream affected
fields include payment plans (wait/partial second payment), status, method, and
safe amount where the date is used as a candidate constraint.

Representative evidence: `request_04` expects 2024-06-15 while the current
forecast reports 2024-06-04; `request_13` expects 2024-05-15 while the current
forecast reports 2024-03-07. These are not isolated date-format errors: the
current forecast's future minimum remains well above the floor because repeated
essential variable flows are absent.

### Exact current behavior

`earliest()` scans each date from `request_date` through `request_date + 89` and
returns the first date for which `forecast(..., ((date, requested_amount),))`
returns true. It has no separate deadline test and no independent cash-flow
model. Because the forecast omits unsupported recurring/variable events, the
predicate becomes true too early.

### Expected behavior and why current behavior is wrong

The specification defines earliest date as the first conservative projected date
on which one full payment is safe while every required expense is covered and
the minimum balance is maintained. Repeated essential variable spending is part
of that conservative forecast even when it is not a subscription. Returning a
date before an upcoming required groceries/transport/utility movement proves
only that the incomplete ledger is safe, not that the user's reconstructed
financial state is safe.

### General replacement rule

Construct a canonical dated flow model first. Detect repeated same-user,
same-category/description/direction series across all cash categories, using a
configurable cadence policy and robust amount statistic. For essential or
protected variable categories, forecast conservative future occurrences through
the inclusive 90-day horizon. Keep optional flexible spending in the ledger as
required by the published policy unless a validated permitted action removes or
reduces it. Then scan the corrected model for the first safe date. The date scan
must remain independent of payment-method preferences.

Mandated: minimum protection, confirmed settlement timing, no unsupported
income, and 90-day horizon. Example-derived: sample rows demonstrate that
recurring/essential commitments delay dates and can require flexible changes.
Policy: observation threshold, cadence tolerance, amount statistic, month-end
rollover, and same-day ordering remain explicit configuration.

### Files/functions affected

`code/main.py`: `recurring`, `forecast`, `earliest`, `semantic_events`.
`code/ledger.py`: canonical recurrence metadata and provenance.
`code/forecast.py`: dated movement simulation.
`code/policy.py`: recurrence and same-day policy values.

### Required regression tests

- Repeated groceries/transport/dining/healthcare with three-plus observations
  must produce future required movements.
- Monthly cadence crossing February and month-end must be deterministic.
- A full payment immediately before a required debit must be rejected if the
  post-debit floor fails.
- A future confirmed salary must make the first safe date exactly its settlement
  date or later, never earlier.
- Horizon day 90 must be excluded when the contract is an inclusive 90-day
  window from day 0 through day 89.
- Adding an excluded pending credit must not make earliest date earlier.
- Repeated runs must return the same date and trace.

### Risk

High. Expanding recurrence can lower safe amounts and move dates later across
many users, changing status/method/plan fields. Over-forecasting one-off
discretionary events would be equally damaging, so recurrence evidence and
essential-category classification must be tested separately from arithmetic.

## B. Safe-amount calculation — priority 2

### Root cause

`safe_amount()` performs a cent-quantized binary search over a forecast that is
missing repeated essential/variable movements. The binary search itself is
monotonic only relative to that incomplete forecast. It also uses a hard-coded
two-decimal serialization/search quantum even though the specification does not
mandate a scale. The result is too large in 22/25 rows, including four rows whose
classification is affected by scheduled/pending evidence.

### Affected examples and fields

All amount mismatches: `request_02`, `request_03`, `request_04`, `request_05`,
`request_06`, `request_07`, `request_08`, `request_09`, `request_10`,
`request_11`, `request_13`, `request_14`, `request_15`, `request_17`,
`request_18`, `request_19`, `request_20`, `request_21`, `request_22`,
`request_23`, `request_24`, `request_25`.

Affected field: `amount_safe_to_pay` (22/25), with downstream status, partial
plan, flexible-change, and ranking effects.

### Exact current behavior

The implementation starts with `lo=0`, `hi=requested_amount`, repeatedly tests
the midpoint rounded to `CENT`, and returns the largest tested safe value. The
test is `forecast(request_date, one payment today)`, which applies all ledger
flows and then subtracts the candidate payment from every balance on and after
the payment date. It does not apply optional spending changes unless a caller
passes them.

### Expected behavior and why current behavior is wrong

The maximum safe amount must be the largest amount that leaves every post-event
balance at or above the configured minimum under the corrected baseline ledger.
For example, `request_05` expects only 737 while the current result is 15488;
the difference is a cash-flow forecast discrepancy, not a request-specific
exception. `request_06` expects 603.3 and a streaming stop action, showing that
future required commitments can reduce capacity below the requested amount.

### General replacement rule

After canonical flows are complete, calculate capacity as a deterministic
minimum slack over all affected balance checkpoints (or use a minor-unit binary
search over the same exact simulator). Do not round intermediate balances.
Use Decimal/fixed-point values, preserve exact input precision until final
serialization, and assert monotonicity: reducing today's payment cannot make a
previously safe forecast unsafe.

Mandated: amount bounds, minimum floor, no binary floating point, and no pending
credit/invented income. Example-derived: expected values demonstrate that
future essential obligations reduce today's capacity. Policy: minor-unit scale
and final trailing-zero formatting.

### Files/functions affected

`code/main.py`: `safe_amount`, `forecast`, `fmt`.
`code/forecast.py`: safe-capacity API.
`code/ledger.py`: complete dated flows.
`code/policy.py`: Decimal scale/rounding policy.

### Required regression tests

- Exact minimum equality is safe; one minor unit below is unsafe.
- A temporary dip before a later salary rejects the amount.
- Zero safe amount is represented as `0`, never blank or negative.
- Pending debit lowers capacity; pending credit does not raise it.
- Missing direct FX never silently creates capacity.
- Decimal values such as 603.30, 620.40, and half-cent inputs remain exact.
- Property test: safe amount is bounded, deterministic, and monotonic with
  respect to adding a required debit.

### Risk

Very high. This field is upstream of partial-payment generation and is used by
the sample evaluator as the most visible arithmetic output. Any recurrence or
rounding change can alter most rows.

## C. Candidate generation and ranking — priority 3

### Root cause

The current tuple sort is broadly aligned with the published ranking, but many
candidate comparisons are made against incorrect safe amounts/earliest dates.
Thus a downstream ranking symptom is often an upstream feasibility defect. A
clear independent issue is that flexible-change enumeration retains only the
latest event per category and truncates possible actions to eight before
combination search. This can discard a valid lower-cost/earlier action set.

### Affected examples and fields

`payment_plan` mismatches: `request_03`, `request_04`, `request_05`, `request_06`,
`request_08`, `request_10`, `request_13`, `request_18`, `request_19`,
`request_20`, `request_21`, `request_23`, `request_24`, `request_25` (14).

The `request_19` mismatch is especially diagnostic: expected partial payment
beats the selected installment option once the corrected safe amount is 28820;
the current lower safe amount makes the partial candidate less attractive or
invalid. Wait/full mismatches likewise follow dates that are currently too
early.

### Exact current behavior

`candidate()` adds full payment, supplied options, partial payment, wait, and
flexible variants, rejects plans outside the 90-day horizon or deadline, and
sorts by `(deadline, no changes, total payable, first date, number of payments,
option_id)`. It only considers flexible events after no baseline candidate
exists, chooses one latest event per category, and caps actions at eight.

### Expected behavior and why current behavior is wrong

The specification requires all safe eligible candidates to be validated and
ranked. Preference is a hard eligibility constraint, supplied installment
plans must be exact, and a plan that is safe only after a permitted spending
change must remain available for consideration. Ranking should not be allowed
to compensate for an incomplete forecast, and candidate generation must not
silently discard valid flexible sets.

### General replacement rule

Separate candidate phases: generate every structurally possible candidate;
validate each against the corrected forecast; then apply the exact lexicographic
ranking. Generate flexible action sets up to three actions without category
deduplication unless the policy explicitly says one action per obligation.
Deduplicate only identical canonical action sets. Add a stable sorted
`(event_id, action, target_amount)` key after the specified ranking keys.

Mandated: hard preferences, exact partial two-payment contract, exact supplied
installments, three-action cap, and deadline feasibility. Example-derived:
partial beats a more expensive option when it is valid and completes on time.
Policy: final tie-break for otherwise equal action sets.

### Files/functions affected

`code/main.py`: `candidate`, `option_plan`.
`code/plans.py`: generation/ranking boundary.
`code/validator.py`: independent candidate validator.

### Required regression tests

- Partial vs installment with different total payable amounts.
- Supplied option rejected by preference or installment-month limit.
- Wait candidate rejected when it misses deadline but earliest capacity remains
  separately reported.
- Multiple flexible sets with equal totals use stable event/action tie-break.
- Three-action maximum and duplicate-action rejection.
- Every selected plan re-simulates safely; validator rejects rather than repairs.

### Risk

High, but most current ranking mismatches should disappear after forecast/date
repair. Changing the ranking before repairing feasibility would mask the true
cause and risk overfitting visible examples.

## D. Deadline/status mapping — priority 4

### Root cause

The current fallback returns `affordable_later` with a `wait` plan whenever any
safe date exists in the 90-day horizon, even if that date is after the user's
desired completion date. Conversely, candidate selection can call a full
payment `affordable_now` when the corrected forecast should reject today. The
implementation conflates capacity (`earliest`) with recommendation eligibility.

### Affected examples and fields

Status mismatches: `request_04`, `request_05`, `request_06`, `request_08`,
`request_10`, `request_11`, `request_13`, `request_20`, `request_21`,
`request_24`, `request_25` (11). Their methods/plans/earliest dates are often
also mismatched downstream.

### Exact current behavior

If no candidate survives, `candidate()` emits `affordable_later` and a wait plan
whenever `earliest_date` is non-null, without requiring that date to meet the
deadline. If no date exists, it emits `not_affordable`. For a selected full
payment today, status is `affordable_now`; for a wait candidate, it is
`affordable_later`.

### Expected behavior and why current behavior is wrong

The specification requires plans to complete by the desired deadline and says
`not_affordable` applies when the request cannot be completed safely within the
forecast period. It does not formally define every safe-after-deadline case.
The current behavior is therefore an unsafe universal claim: it presents a late
wait as a recommendation despite the deadline constraint.

### General replacement rule

Compute and retain `earliest_safe_full_payment_date` as a capacity fact. Mark a
candidate eligible only if every payment is on or before the deadline. If no
eligible plan exists, map the result using an explicit conservative policy:
`not_affordable` when the request cannot meet the deadline; do not emit a late
payment plan as a recommendation. Preserve the capacity date separately only
where the output contract permits it. Add a policy switch for the unspecified
late-deadline boundary, but keep one default documented and tested.

Mandated: deadline-compliant plans and distinct status vocabulary. Example-
derived: requests 05/10/20/24/25 show late capacity should not become a wait
recommendation. Policy: exact safe-after-deadline mapping.

### Files/functions affected

`code/main.py`: `candidate`, status mapping.
`code/plans.py`: eligibility.
`code/policy.py`: late-deadline mode.
`code/validator.py`: deadline assertions.

### Required regression tests

- Earliest date exactly on deadline is eligible.
- Earliest date one day after deadline is not an eligible wait plan.
- No safe date in horizon yields `not_affordable` and `none`.
- Safe date exists after deadline: verify configured conservative mapping.
- `affordable_now` requires a safe full payment today and accepted preference.

### Risk

High for status/method/plan fields, but low arithmetic risk if implemented after
forecast repair. The policy must be visible because the source is silent at the
boundary.

## E. Payment-method preference — priority 5

### Root cause

The implementation does enforce preference membership as a hard filter, but the
reported nine method mismatches are mostly downstream effects: corrected
forecast feasibility changes whether full payment, wait, partial, or
installments exist. The current report's `payment-method preference` label is
therefore too broad to justify changing preference semantics directly.

### Affected examples and fields

`request_04`, `request_05`, `request_08`, `request_10`, `request_13`,
`request_19`, `request_20`, `request_24`, `request_25` (9 method fields).
Expected methods are generally `wait`, `not_recommended`, or `partial_payment`
where the current output selects full payment, wait, or installments using the
incomplete forecast.

### Exact current behavior

`add()` rejects a method unless it is in `payment_methods_user_will_consider`,
except that `wait` is admitted as a special method. Full payment today is only
added when `full_payment` is in preferences; installments additionally observe
`max_installment_months`.

### Expected behavior and why current behavior is wrong

The hard-preference rule itself agrees with the specification. The defect is
that preference is evaluated against wrong candidate feasibility and wrong
earliest dates. `wait` must also require accepted `full_payment` and a
deadline-compliant safe date; it must not be a universal escape hatch.

### General replacement rule

Keep preferences as hard eligibility constraints. Recompute all candidates after
forecast/date repair. Treat `wait` as eligible only when `full_payment` is
accepted and the wait plan meets the deadline. Never infer a preference from
request text, balance, or a supplied option.

Mandated: hard preference semantics and installment limit. Example-derived:
sample users with enough cash still reject full payment when preference excludes
it. Policy: none beyond explicit wait/deadline treatment.

### Files/functions affected

`code/main.py`: `parse_pref`, `candidate`.
`code/plans.py`: eligibility generation.
`code/validator.py`: method preference checks.

### Required regression tests

- Full payment excluded by profile cannot be selected despite safe balance.
- Installments excluded by profile cannot be selected despite supplied option.
- Wait excluded when full payment is not accepted.
- Partial payment requires both request permission and profile preference.
- A corrected forecast that removes full-payment feasibility must select the best
  remaining accepted method, not bypass preferences.

### Risk

Medium. Directly changing preference logic could reduce already-correct method
matches. Repair feasibility first and add differential tests proving that only
eligibility, not ranking, is controlled by preferences.

## Cross-cutting event/scheduled/evidence causes

### Event classification and scheduled-credit semantics

The report attributes five safe-amount mismatches to pending/event
classification (`request_02`, `03`, `20`, `22`, `23`) and four to scheduled
credits (`request_13`, `17`, `21`, `25`). These are upstream ledger inputs, but
they must not be “fixed” by counting every scheduled credit. The current policy
excludes pending credits and non-salary scheduled credits; that is aligned with
the conservative specification unless explicit evidence confirms a future
credit. Repair work should first audit each affected event's status, settlement
date, lifecycle link, message/image evidence, and direct FX provenance. Only a
typed confirmed salary/future-credit fact may enter the forecast.

Affected functions: `load_data`, `normalize_events`, `semantic_events`, evidence
resolution, and `forecast`. Tests must cover pending debit/credit asymmetry,
scheduled salary, unsupported scheduled non-salary credit, lifecycle
cancellation, and missing amounts. Missing FX must remain an explicit error;
no inverse, triangulated, nearest-date, or invented rate is permitted.

### Flexible-spending logic

The three mismatches (`request_06`, `request_11`, `request_21`) indicate that
future flexible recurring obligations are not being projected/used consistently.
The current search chooses only the latest event per category and considers
changes only after baseline candidates fail. Once recurring flows are complete,
enumerate allowed stop/reduce actions against canonical recurring obligations,
validate each set, and rank no-change sets before changed sets. Never modify
protected categories or fixed events. The expected action can be required even
when a superficially safe baseline plan exists under the incomplete forecast.

## F. Output serialization and explanation generation

### Root cause

Every sample explanation differs (25/25), and several financial strings differ
only by trailing zeros (`620.40` versus `620.4`, `1574.40` versus `1574.4`).
The current `fmt()` always quantizes to two decimals and strips trailing zeros;
the explanation template is a generic implementation sentence rather than the
sample-style grounded rationale.

### Affected examples and fields

All 25 examples mismatch `decision_explanation`. Numeric-equivalent formatting
appears in at least requests 06, 09, and 21 and affects amount or plan strings.

### Exact current behavior

`fmt()` quantizes with `ROUND_HALF_EVEN` at two decimal places, then removes all
trailing zeroes. `candidate()` emits a fixed English template that does not
mention the user's currency-specific minimum, deadline, waiting rationale, or
selected flexible action in the same grounded structure as the examples.

### Expected behavior and why current behavior is wrong

The output contract requires valid decimal/date/plan serialization and a concise,
grounded explanation. It does not mandate a single scale or prose template, so
numeric-equivalent values are not arithmetic failures. However, preserving
meaningful supplied option precision is safer, and explanations must not claim
facts absent from the validated trace.

### General replacement rule

Keep Decimal values exact through validation. Preserve the original serialized
amount for supplied installment options where it is semantically unchanged;
otherwise use one documented deterministic serializer with tests. Generate the
explanation only from the finalized validated decision facts (currency, amount,
dates, minimum, status, and changes). An LLM may paraphrase only after a fact
bundle check and can never alter a numeric/date/status token.

Mandated: exact eight-column CSV contract and grounded explanation. Example-
derived: meaningful trailing zeroes are observed in sample plans. Policy: exact
serialization scale and prose template.

### Files/functions affected

`code/main.py`: `fmt`, output writer, explanation template.
`code/explanations.py`: fact-bundle renderer and post-generation checks.
`code/validator.py`: serialization and explanation fact assertions.

### Required regression tests

- Header order and one row per evaluation request.
- Numeric-equivalent values are parsed as Decimal for semantic validation but
  serialized deterministically.
- Exact supplied option strings such as `620.40` survive plan generation.
- Explanations contain only selected-plan facts and no unsupported promise.
- Repeated runs are byte-identical.

### Risk

Low for financial feasibility, medium for strict field matching. Serialization
must not alter the underlying Decimal comparisons or plan sums.

## Implementation gate and sequencing

No fix should be started until this plan is reviewed. The safe sequence is:

1. Add ledger/forecast trace fixtures and repair canonical flow classification.
2. Repair recurrence/essential variable spending with configurable policies.
3. Re-run safe amount and earliest-date tests; inspect all field diffs.
4. Repair candidate generation/ranking and flexible action enumeration.
5. Repair deadline/status mapping and preference eligibility only where traces
   show a remaining defect.
6. Repair Decimal serialization and grounded explanation formatting.
7. Re-run all existing tests, all 25 solved examples, and adversarial/property
   regressions. Do not proceed to packaging until the diff is explained.

The next implementation turn must preserve deterministic arithmetic and ensure
that no LLM output can authorize, alter, or repair a financial plan.
