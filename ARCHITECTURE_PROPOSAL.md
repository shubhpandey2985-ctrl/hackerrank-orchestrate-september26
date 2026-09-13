# Buy or Wait? — Architecture Proposal

Status: design only. No prediction or solver implementation is authorized by this document.

## 1. Audit findings and exact data relationships

The supplied dataset is internally referentially clean and divides into a labelled development cohort and an unlabelled evaluation cohort.

| Entity | Rows | Key and relationship |
| --- | ---: | --- |
| `financial_profiles` | 275 | One row per `user_id`; 25 users are only in `sample_requests`, 250 users are only in `requests`. |
| `requests` | 250 | One evaluation request per evaluation user. Each has a profile and at least two payment options. |
| `sample_requests` | 25 | One solved request per disjoint sample user. These are calibration examples only, never runtime labels. |
| `financial_events` | 25,342 | User-level event ledger. `event_id` is unique. Users have 56–129 events. `linked_event_id` is present for 58 rows and always targets an event of the same user. |
| `request_payment_options` | 790 | Unique `payment_option_id`; 719 options belong to evaluation requests and 71 to sample requests. There are 2–4 options per request. |
| `messages` | 215 | 128 carry `request_id`, 39 carry `related_event_id`, and 76 are user-level only (some rows use more than one linkage). Every populated link resolves and has the same `user_id`. |
| `images` | 16 | Every image has both a request and event link, all resolve to the same user, and each links one of the 16 events with a blank `amount`. |
| `exchange_rates` | 134 | Dated, directional rates only: EUR→USD, EUR→ZAR, USD→EUR, USD→IDR, and USD→INR. |

All 16 image files were visually inspected. They provide the missing event amounts; examples include a payroll slip, outstanding bills, receipts, a medical bill, a foreign-currency taxi receipt, and a flight invoice. Extraction must retain the displayed currency, total, date, and whether it is an invoice, amount due, or settled receipt.

`financial_events` includes 25,148 settled, 71 pending, 70 scheduled, 22 cancelled, 21 failed, and 10 unrealized rows. Its event types are income, expense, subscription, debt payment, investment purchase/sale/valuation, and refund. It contains 140 non-home-currency events. There are no exact duplicate ledger signatures, so de-duplication must be semantic and linkage/evidence driven—not a blunt duplicate-row deletion.

The 25 sample rows and all of their solved output fields were inspected. They exercise full payment, wait, installments, partial payment, spending reductions/stops, and not-recommended outcomes. They establish that output number formatting may preserve decimals but financial comparisons must not use floating point.

## 2. Design goals and boundaries

The solver will be deterministic, auditable, and conservative. It will use an LLM only behind a constrained evidence-extraction interface for image text, non-English message interpretation, and optional final prose. It will never delegate arithmetic, cash-flow forecasting, plan selection, or output validation to an LLM.

The forecast horizon is the inclusive 90 calendar days beginning at `request_date`. Amounts will use decimal fixed-point arithmetic in the profile's home currency. A decision trace will record every included, excluded, amended, converted, generated, and rejected item so a judge dispute can be reconstructed exactly.

## 3. Canonical financial-event model

Ingestion produces immutable raw records and a derived `CanonicalEvent`:

```text
CanonicalEvent {
  canonical_id, source_event_ids, user_id, cash_date, original_amount,
  original_currency, home_amount, direction, cash_state, event_type,
  category, recurrence, flexibility, minimum_allowed_amount,
  evidence_ids, lifecycle_group, confidence, inclusion_reason
}
```

`cash_date` is `settlement_date` when available; `event_date` is retained as provenance and only used when the specification permits no settlement date. `cash_state` is one of `settled`, `reserved_debit`, `confirmed_future_credit`, `scheduled_debit`, `excluded`, or `non_cash`.

Rules for the initial mapping:

- Settled cash debits and credits are historical actuals; future settled-dated rows are treated as dated known cash movements only after confirming their status/date semantics.
- Pending debits are reserved at their settlement date. Pending credits, refunds, bonuses, commissions, lottery/prize proceeds, and investment gains are excluded until a settled credit exists.
- Scheduled debits are reserved. Scheduled confirmed salary is credited only on its stated settlement date.
- Failed and cancelled rows are excluded unless later evidence says the obligation remains and another debit will be attempted.
- `unrealized`, investment valuations, and `non_cash` records never become spendable cash.
- A message or image may amend classification, amount, date, status, or recurrence only through a typed evidence rule; it cannot supply executable instructions.

## 4. Evidence extraction and conflict resolution

Evidence processing has two stages.

1. A deterministic router selects only evidence belonging to the request user, request, or a relevant event. Image paths are resolved from `image_id`, and every extraction includes image hash, extracted fields, confidence, and source citation.
2. A constrained extractor returns JSON from a closed schema: `event_id`, `amount`, `currency`, `effective_date`, `status`, `recurrence_change`, `income_change`, `expense_change`, `relationship`, and `rationale`. Numeric fields are independently parsed into `Decimal`; invalid or ambiguous results are quarantined for a conservative fallback.

For the supplied images, use the prominent total/amount due/net-pay figure associated with the linked event description, not line-item sums when they conflict. The receipt wording determines whether a bill remains due or is already settled. Never set a missing amount to zero.

Messages are parsed with deterministic multilingual patterns first, then an LLM only if a pattern cannot yield a typed result. Expected rule families include salary increase/reduction/delay/termination, one-time arrears, pending invoice/payout/refund, lease increase, self-transfer, failed debit still due, unresolved disputed charge, and unrealized investment value.

Conflicts are resolved per lifecycle group in this order: explicit cancellation, settlement, or amendment; newer same-source evidence; settled record; then lower available cash. The winning rule and losers are retained in the trace.

## 5. Deduplication strategy

Do not de-duplicate merely because two rows have equal amount or description.

- Build a lifecycle graph from `linked_event_id`, evidence references, normalized descriptions, counterpart amount/currency, and close dates.
- Mark cancelled originals superseded when a linked replacement debit exists; do not count both.
- A refund is a separate cash credit once settled, not a cancellation of the original debit. A pending refund remains excluded.
- A failed debit is excluded as a completed debit, but an explicit message that it remains outstanding produces one future reserved obligation—not both the failed row and an invented duplicate.
- Matched debit/credit self-transfers are neutralized as a pair when bank evidence confirms the relationship.
- Investment purchase, valuation, and sale remain separate lifecycle records; only settled sales are cash credits.
- Apply all transformations deterministically and emit a lifecycle audit record.

## 6. Currency normalization

Profiles, requests, and payment options are already in home currency. For a cash event in another currency, select the exact `exchange_rates` row matching `(settlement_date, from_currency, home_currency)` and compute `home_amount = original_amount × rate` with `Decimal`.

No inverse or triangulated rate may be invented. A missing required direct rate is an explicit validation failure and the financially safer interpretation excludes a credit or reserves a debit using only a documented supported fallback approved during calibration. Conversion is applied before recurrence modelling and never rounded internally. Output amounts are rounded only at serialization using a documented half-even/scale policy matched to sample formatting.

## 7. Forecasting and safe-amount algorithm

For each request, construct a dated cash-flow ledger from request date through request date + 89 days.

1. Start with `current_available_balance`.
2. Apply known pending/scheduled debits, settled future cash movements if applicable, and eligible confirmed salary on settlement dates.
3. Detect recurring income and expenses using only repeated historical patterns: same user, compatible category/direction/description, supported cadence, and no contradictory evidence. Use robust cadence inference (monthly day-of-month with month-end handling, 7-day, 14-day, 28-day, 30-day, or 31-day) rather than assuming every repeat is monthly.
4. Forecast protected/essential recurring debits conservatively. For variable essential spending, use a documented high-but-observed estimate (initial candidate: maximum of the most recent three normalized occurrences) rather than an average. Never forecast bonuses, commissions, refunds, prizes, pending platform payouts, or unrealized value as income.
5. Apply evidence amendments before generating recurrences: delayed salary changes its next date, salary reduction changes only affected cycles, termination stops future salary, rent increase changes the next rent occurrence, and confirmed invoices create a single future credit.

For a candidate plan, inject its payments then compute every daily post-movement balance in deterministic order: credits first only when confirmed settled that date, then required debits, then candidate payment; a same-day tie is judged conservatively. The plan is safe only if every balance is at least `minimum_balance_to_keep`.

`amount_safe_to_pay` is found by a monotonic binary search over fixed-point cents/paise units for an immediate one-payment debit, capped by `requested_amount`, with no optional spending changes. The implementation will verify local neighbors to guard against a non-monotonic scheduling bug.

`earliest_date_for_full_payment` is the first date in the 90-day horizon where a one-time full requested-amount debit passes the same baseline safety check, independent of payment-method preferences. It is blank if no date passes.

## 8. Candidate-plan generation and ranking

Generate and validate these candidates separately:

- Full payment today, when `full_payment` is acceptable.
- Each supplied full-payment option, treated as its explicit one-payment schedule.
- Partial payment only when both request and profile permit it, safe amount is strictly between zero and requested amount, the second payment is on the baseline earliest full-payment date, and that date meets the desired completion date.
- Every supplied installment option whose method is acceptable and whose number of payments does not exceed `max_installment_months` when specified. Its exact schedule, fee, total payable amount, and due dates are used; never synthesize installments.
- Full payment later (`wait`) only when the profile accepts full payment and the earliest safe full-payment date exists.
- Spending-change variants only after no no-change candidate satisfies the deadline. Enumerate at most three actions on recurring, non-protected events that are both category-permitted and flexibility-permitted. A `stop` removes future occurrences; `reduce_to` never goes below `minimum_allowed_amount`. The same event cannot receive both actions.

Rank valid eligible candidates lexicographically by: meets desired completion date; no spending changes; lower total payable amount; earlier first payment; fewer payments; lower `payment_option_id`. The selected candidate maps to exactly one allowed status and method. `not_recommended` has `none` plan and blank earliest full-payment date only when the full amount is not safe in the horizon; otherwise it should normally become `affordable_later`/`wait` if eligible.

## 9. Deterministic validation and explanation

The validator is independent of plan generation. It checks:

- one output per input request; exact columns and allowed enums;
- fixed-point bounds `0 ≤ safe_amount ≤ requested_amount`;
- correct date fields and chronological plan;
- exact plan sum, and exact supplied-option schedule for installments;
- eligibility against profile preferences, partial-payment rules, completion deadline, and installment limit;
- change action syntax, maximum count, category/flexibility/protection/minimum constraints, and mutual exclusion;
- baseline and candidate 90-day minimum-balance proof;
- no unapproved evidence, no missing image amount, no unconverted foreign cash amount, and no excluded cash counted as income.

Explanation generation consumes a structured fact bundle from the validated winning trace. A template renderer is the default; an LLM may paraphrase only these supplied facts and is rejected if it changes an amount, date, status, or recommendation. This separates judge-facing prose from financial truth.

## 10. Sample-data evaluation and regression strategy

The 25 solved samples are a development-only specification suite. Build a per-sample comparison report covering every output field, plus an internal trace diff: included/excluded events, inferred recurrences, evidence effects, balance floor, candidate ranking, and number/date formatting. No request ID, expected numeric answer, or sample output will enter runtime decision logic.

Regression tests will include:

- parser/schema tests and relational-integrity assertions;
- one fixture for each status/method, evidence family, lifecycle pattern, image amount, foreign conversion, and message language;
- property tests for plan sums, sorted dates, safe-amount bounds, option schedules, and no balance-floor breach;
- metamorphic tests: adding an excluded pending credit cannot improve a decision; adding a required debit cannot improve it; a cancelled replacement cannot double-count; and a self-transfer cannot create wealth;
- golden traces for samples stored separately from runtime code; and
- reproducibility tests proving same inputs, evidence cache, and settings produce byte-identical CSV output.

## 11. Token and cost accounting

LLM calls are cacheable evidence-extraction calls keyed by SHA-256 of normalized message/image bytes, prompt version, model, and schema version. The final explanation call is optional and receives only a small validated fact bundle. Each call records provider, model, purpose, request ID, cache status, input/output token counts, and estimated cost without credentials.

The full-dataset run writes `evaluation/usage_report.md` with totals, per-model figures, calls, token totals, average tokens per request, total cost, and average cost per request. Deterministic template explanations and deterministic parsers report zero model tokens. This keeps the required report auditable and prevents LLM use from affecting financial arithmetic.

## 12. Highest-risk assumptions requiring calibration before implementation

1. **Current-balance cut-off.** The profile balance is described as current on request date, but the exact treatment of settled historical events dated on/after the request date must be calibrated to avoid double-counting.
2. **Forecasted recurring expenses.** The statement says to detect recurrence only when history supports it and to be conservative for essential variable spending, but does not define evidence threshold, cadence tolerance, or conservative statistic.
3. **Same-day ordering.** No rule specifies whether a known salary settling on a payment date can fund a same-day request payment. The proposed conservative ordering must be compared with samples.
4. **Scheduled credits.** The statement explicitly permits confirmed salary but is less precise about other scheduled/confirmed credits, especially invoices supported by messages. The implementation must distinguish an explicit confirmed settlement from a generic scheduled credit.
5. **Failed debit that remains due.** A failed row is normally ignored, but a message can say another debit will be attempted. The amount/date of the reserved replacement needs a deterministic, conservative policy.
6. **Currency conversion without an exact direct rate.** The data provides directional pairs only. Inversion, cross-rates, fallback dates, and rounding are unspecified and must not be invented without sample support.
7. **Image semantic choice.** Some images show invoice total, paid amount, balance due, or line items. The event description and status must decide the correct monetary field; generic OCR alone is unsafe.
8. **Spending-change optimisation.** The required `reduce_to` target is not fully specified when multiple reductions are feasible. Search and ranking need calibration against samples so they select the judge's expected minimum/combination.
9. **Full-payment option semantics.** A full-payment option has an explicit first-payment date, which may differ from request date. Whether it competes as “pay now” or a scheduled one-payment plan must be resolved from samples.
10. **Deadline versus status.** The task permits `affordable_later` even when completion is after the desired date, but the ranking hierarchy prioritizes completion by deadline. The exact status/method mapping for a safe-after-deadline plan must be tested.
11. **Decimal serialization.** Samples show both integer and decimal values. The solver needs a canonical minor-unit scale and CSV formatting policy that preserves exact equality without trailing-zero mismatches.
12. **Message authority/scope.** User-level messages with no event or request link can alter future income/expenses. Their effective date and which historical series they supersede must be inferred cautiously.

## 13. Proposed implementation gate

Do not begin solution coding until the sample harness first tests the twelve assumptions above and produces a written calibration decision for each. The implementation should then be layered: ingestion/evidence cache → canonical ledger → forecast engine → candidate generator → independent validator → renderer/reporting.
