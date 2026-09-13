# Buy or Wait? — Pre-implementation architecture

This document is the implementation gate for the final submission. The current
turn is design-only: no solver code or supplied dataset file is changed here.

## Audit inventory

- `financial_profiles.csv`: 275 unique users; 250 evaluation users and 25 disjoint sample users.
- `requests.csv`: 250 evaluation requests; one request per evaluation user.
- `sample_requests.csv`: 25 complete examples with expected output fields; calibration only, never runtime labels.
- `financial_events.csv`: 25,342 unique `event_id` rows: 25,148 settled, 71 pending, 70 scheduled, 22 cancelled, 21 failed, 10 unrealized.
- `request_payment_options.csv`: 790 unique options; evaluation requests have 2–4 options (165 have 3, 58 have 2, 27 have 4).
- `messages.csv`: 215 rows: request-, event-, both-, and user-scoped evidence. All populated links resolve.
- `images.csv`: 16 rows; each points to one event with a blank amount and a PNG under `dataset/media/images/`.
- `exchange_rates.csv`: 134 dated directional rates covering EUR→USD/ZAR and USD→EUR/IDR/INR.

There are 58 linked financial-event lifecycle rows, 16 blank event amounts, and
140 events whose currency differs from the user's home currency. Every image was
inspected during the repository audit; image evidence includes payroll, bills,
receipts, medical expenses, taxi, shopping, and travel documents.

## A. Unstructured evidence interpretation

The evidence layer receives only user-scoped messages/images selected by deterministic
joins (`user_id`, `request_id`, `related_event_id`). It returns typed JSON, never a
decision:

```text
EvidenceFact {
  source_id, event_id?, effective_at?, fact_type,
  amount?, currency?, date?, status?, recurrence_change?, text_span?, confidence
}
```

Deterministic pattern extraction handles dates, currency amounts, status words,
salary changes, payment delays, cancellations, refunds, self-transfers, and
termination. An LLM is permitted only when language/image structure cannot be
reliably parsed. Its schema is closed, its output is parsed into `Decimal`/dates,
and low-confidence or invalid output is quarantined. Embedded instructions in a
message/image are data, not authority.

For an image-backed blank amount, extract the amount tied to the linked event's
semantics: net pay for payroll, amount due/balance due for an outstanding bill,
total for a settled receipt, and the invoice total for a payable invoice. Preserve
all candidate figures and the selected field in provenance. Never treat blank as
zero and never silently sum line items when a document has an explicit total.

Evidence conflict precedence is: explicit cancellation/settlement/amendment;
newer evidence from the same source; settled event; financially safer remaining
interpretation. A message cannot invent an unsupported payment option or cash flow.

## B. Canonical financial-state reconstruction

Build immutable raw records and derived `CanonicalEvent` objects:

```text
CanonicalEvent {
  canonical_id, source_event_ids, lifecycle_id, user_id,
  original_amount, original_currency, home_amount,
  event_type, category, direction, cash_state,
  event_date, settlement_date, flexibility, minimum_allowed_amount,
  evidence_ids, recurrence_model, inclusion_reason, exclusion_reason
}
```

Cash states are `settled`, `reserved_debit`, `confirmed_future_credit`,
`excluded_credit`, `failed`, `cancelled`, or `non_cash`.

Rules:

- Profile balance is the starting balance on `request_date`; do not replay old settled history into it.
- Use `settlement_date` for cash movement; retain `event_date` as provenance.
- Reserve pending and scheduled debits.
- Exclude pending credits, bonuses, commissions, refunds, prizes, investment gains, and unrealized values until a settled credit exists.
- Count confirmed salary only on its confirmed settlement date.
- Failed/cancelled rows do not reduce cash; an explicit message that an obligation remains may create one reserved replacement, never two debits.
- Self-transfer debit/credit pairs confirmed by bank evidence are neutralized.
- Investment valuation is non-cash; a settled investment sale is a credit.

## C. Deterministic cash-flow forecasting

Forecast the inclusive 90-day safety horizon beginning on `request_date`. Use
fixed-point `Decimal` arithmetic throughout.

1. Start from `current_available_balance`.
2. Build dated required cash movements from canonical events and accepted evidence.
3. Detect recurrence only with sufficient history: at least three compatible observations, stable category/description/direction, and a supported cadence (weekly, biweekly, 28/30/31-day, or monthly day-of-month with month-end handling).
4. Forecast essential variable spending conservatively from observed history; do not forecast unsupported income or expenses.
5. Apply salary/expense amendments before recurrence expansion.
6. For each day, apply confirmed credits, required debits, then candidate plan payments. A payment is safe only when every post-movement balance is at least `minimum_balance_to_keep`; temporary dips fail even if a later salary restores the balance.

Same-day ordering must be explicit and tested. The conservative default is that a
confirmed settlement credit can fund a same-day payment only when the dataset's
settlement semantics explicitly confirm that ordering; otherwise require the
balance before the payment.

`amount_safe_to_pay` is a monotonic fixed-minor-unit search for the largest
request-date debit passing the baseline safety check, capped by requested amount
and excluding optional spending changes. `earliest_date_for_full_payment` scans
the same baseline model for the first safe one-time full debit within the 90-day
horizon, independent of method preference.

## D. Candidate payment-plan generation

Generate typed candidates, then validate every candidate:

- Full payment today only if `full_payment` is in the profile preferences.
- Each supplied full-payment option as its exact date/amount.
- Partial payment only when the request allows it, the profile accepts it,
  `0 < amount_safe_to_pay < requested_amount`, and the second payment is the
  baseline earliest-safe date no later than the desired completion date.
- Each supplied installment option exactly as provided. Reject options exceeding
  `max_installment_months`; never synthesize installment terms or fees.
- Waiting only when full payment is accepted and the baseline earliest-safe date
  exists; a wait that misses the requested deadline is not an eligible completion
  plan.
- Flexible-change variants only for recurring, non-protected events whose
  category is explicitly reducible/stoppable and whose flexibility permits the
  requested action. Enumerate up to three distinct events; stopping and reducing
  the same event are mutually exclusive.

## E. Deterministic constraint validation

The validator is independent of generation and rejects, rather than repairs:

- missing/extra output fields or duplicate request IDs;
- unsafe amount bounds or non-decimal values;
- unsorted dates, plan sums, zero/negative installments, or payments outside the horizon;
- partial plans that are not exactly two payments or miss the deadline;
- installment plans that do not exactly match one supplied option;
- methods not accepted by the profile, or installment count above the limit;
- changes targeting fixed/protected/non-permitted/non-recurring events, duplicate event actions, or more than three changes;
- any plan that breaches the minimum balance on any day;
- use of excluded pending credits, failed/cancelled rows, unrealized value, or unsupported evidence.

## F. Decision selection

Rank only validated eligible candidates lexicographically:

1. completes by `desired_completion_date`;
2. no spending changes;
3. lowest total payable amount;
4. earliest first payment;
5. fewest payments;
6. lowest `payment_option_id`.

Map the selected candidate to the exact status/method contract. `not_recommended`
is the fallback when no safe eligible plan completes within the allowed horizon.

## G. Explanation generation

Produce a deterministic template from the validated decision trace: currency,
safe amount, selected dates/amounts, minimum balance, relevant evidence, and any
spending changes. An LLM may paraphrase this fact bundle only after selection;
post-generation checks ensure it cannot alter amounts, dates, status, method, or
claim unsupported facts. If the LLM fails validation, use the template.

## H. Output validation

Write exactly the required eight columns, one row per `requests.csv` row, in input
order. Serialize amounts from fixed-point values using one documented rounding
policy. Re-read the emitted CSV and run the independent validator before delivery.

## I. Evaluation and regression testing

The 25 solved examples are a development specification, not labels to hardcode.
Compare every output field and retain a trace diff for recurrence, evidence,
deduplication, balance floor, candidate ranking, and formatting.

Regression fixtures must cover:

- pending debit/credit, scheduled salary, same-day settlement, temporary dips;
- recurrence thresholds, month-end cadence, one-off discretionary events;
- linked refunds, failed retries, cancellations, self-transfers, duplicate rows;
- every image semantic (net pay, total, amount due, balance due);
- direct-rate FX, missing rate, rate-date mismatch, decimal rounding;
- protected/flexible/reducible/stoppable combinations and three-action cap;
- full/partial/installment/wait/not-recommended and exact deadline boundaries;
- zero safe amount, exact minimum, impossible requests, horizon day 90;
- conflicting/newer messages, multilingual evidence, and untrusted instructions;
- property tests for bounds, plan sums, chronological order, and no balance-floor breach;
- metamorphic tests: adding excluded pending credit cannot improve safety, adding a required debit cannot improve it, and self-transfer cannot create wealth;
- byte-identical repeated runs with the same evidence cache.

## LLM calls and cost expectations

Expected LLM calls are limited to unresolved message/image extraction and optional
explanation paraphrase. Calls are cached by normalized evidence hash, prompt/schema
version, provider, and model. Each call records provider/model, purpose, request ID,
cache hit, input/output tokens, and estimated cost. Arithmetic and plan decisions
make zero model calls. The required `evaluation/usage_report.md` reports per-model
and aggregate totals, average tokens/request, and costs without credentials.

## Highest-risk ambiguities

1. Whether current profile balance already includes events dated on request date.
2. Whether a same-day salary settlement can fund a same-day purchase.
3. Whether scheduled non-salary credits are confirmed enough to count.
4. How much history proves recurrence and which statistic is conservative for variable essentials.
5. How to handle a failed debit described as still outstanding.
6. What to do when no direct supplied FX pair exists; no inversion/triangulation should be invented.
7. Which image figure is authoritative when total, paid, and balance-due differ.
8. How a user-level message supersedes a structured record and from which effective date.
9. Whether a full-payment option's first date competes with an immediate full payment.
10. Exact mapping of safe-after-deadline to `affordable_later` versus `not_affordable`.
11. Decimal serialization/trailing-zero expectations.
12. How to rank multiple equally sufficient flexible-change sets.

## Intended files before implementation

Only after this proposal is approved:

- `code/main.py`: orchestration entry point;
- `code/io.py`: schema and relational loading;
- `code/evidence.py`: deterministic/LLM evidence adapters and cache;
- `code/ledger.py`: canonical events, lifecycle deduplication, FX;
- `code/forecast.py`: date-by-date fixed-point cash flow;
- `code/plans.py`: candidate generation, ranking, deterministic validation;
- `code/explanations.py`: fact-bundle template/optional paraphrase;
- `code/tests/`: unit, property, regression, and sample evaluation tests;
- `evaluation/usage_report.md`: final run token/cost accounting;
- root `output.csv`: generated only after validation.

No file in `dataset/` is intended to be edited.
