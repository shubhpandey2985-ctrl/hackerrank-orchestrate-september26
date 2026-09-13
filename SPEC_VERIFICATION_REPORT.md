# Final specification verification report

Scope: `AGENTS.md`, `problem_statement.md`, `README.md`, the supplied CSV schemas,
and all 25 rows of `dataset/sample_requests.csv`. The architecture proposal is
treated as a design, not as authority. No production code or dataset file was
changed during this verification pass.

## 1. Exact output contract and serialization

**Rule found:** The output has exactly these eight columns, in this order:
`request_id,amount_safe_to_pay,affordability_status,recommended_payment_method,payment_plan,earliest_date_for_full_payment,spending_changes_needed,decision_explanation`.
There must be one row per evaluation request. Amount safe must satisfy
`0 <= amount_safe_to_pay <= requested_amount`. Dates use `YYYY-MM-DD`.
Payment-plan entries use `date:amount` joined by `|`; `none` is required when no
plan is recommended. Empty earliest date is required when no safe full payment is
expected within the forecast period. The specification does not define a fixed
decimal scale, trailing-zero policy, or rounding mode.

**Architecture assumption:** Use fixed-point arithmetic internally and a single
deterministic serializer, preserving meaningful decimal precision and emitting
valid CSV with exact columns.

**Agreement:** Yes on columns, bounds, date/plan grammar, and empty/`none` rules.
The proposed explicit half-even/cent policy is not specified by the challenge.

**Required change:** Treat numeric serialization as an implementation choice,
not a claimed challenge rule. Calibrate it against solved examples (which include
`620.40`, `1574.40`, and integer-looking values) and preserve exact option amounts
for installment plans. Record the chosen policy in tests and usage documentation.

## 2. Status, method, and payment-plan semantics

**Rule found:** Status values are `affordable_now`, `affordable_with_plan`,
`affordable_later`, and `not_affordable`. Method values are `full_payment`,
`partial_payment`, `installments`, `wait`, and `not_recommended`.
`affordable_now` means full amount safe on request date and accepted full payment.
`affordable_with_plan` means completion through partial payment, installments, or
permitted spending changes. `partial_payment` is exactly two payments, first equal
to `amount_safe_to_pay`, second equal to the remainder, with the second date no
later than the desired completion date. Installments must exactly match a supplied
option.

**Architecture assumption:** Generate typed candidates, validate them independently,
then map the selected candidate to these enums.

**Agreement:** Yes.

**Required change:** Validator must enforce every stated relationship, including
exact partial-plan sum/order and exact supplied installment schedule, rather than
only checking enum membership.

## 3. Full payment today and profile preference

**Rule found:** Immediate methods—full payment, partial payment, and installments—
are eligible only if present in `payment_methods_user_will_consider`. `wait` is
eligible when full payment becomes safe later and the user accepts `full_payment`.
The sample set confirms users with sufficient balances can still receive
installments or wait when their preferences exclude full payment.

**Architecture assumption:** Full payment today requires `full_payment` in profile
preferences; a full-payment option does not override that preference.

**Agreement:** Yes.

**Required change:** Keep this as a hard eligibility constraint, not merely a
ranking feature. Do not infer preference from request wording.

## 4. Ranking and preference rules

**Rule found:** Among safe eligible plans, rank: (1) complete by desired deadline,
(2) no spending changes, (3) minimize total amount paid, (4) start earlier,
(5) fewer payments, (6) lowest `payment_option_id`. Spending changes are allowed
only for permitted flexible recurring expenses. Partial payment additionally
requires request permission and user acceptance. An option can be rejected despite
being supplied because of profile preferences or installment limit.

**Architecture assumption:** Enumerate full, partial, supplied installments, wait,
and permitted spending-change variants; validate all; rank with the exact sequence.

**Agreement:** Yes, except the specification does not state how to compare two
spending-change sets that tie on all listed dimensions.

**Required change:** Add a deterministic final tie-break for action sets (for
example sorted event IDs and action strings) solely for reproducibility, while
documenting that this is an implementation tie-break rather than a supplied rule.

## 5. Same-day settlement ordering

**Rule found:** The specification requires confirmed salary on its settlement date
and says the balance must never fall below minimum after projected expense/payment.
It does not state whether a credit settling on the same date can fund a payment
on that date, nor whether credits or debits are ordered first.

**Architecture assumption:** Use an explicit conservative same-day ordering and
test it; do not let incidental iteration order decide.

**Agreement:** Partially. The need for determinism agrees; the specific ordering
is not supported by the specification or samples.

**Required change:** Mark same-day ordering as unresolved. Implement a configurable
policy with a fixture and calibrate against any judge feedback; default to the
financially safer interpretation when no evidence establishes spendability.

## 6. Scheduled versus confirmed credits

**Rule found:** Reserve pending debits. Do not count pending credits, bonuses,
commissions, refunds, lottery proceeds, or investment gains until settled. Count
confirmed salary on its settlement date. Scheduled debits are explicitly part of
the forecast. The text is silent on generic scheduled credits and message-confirmed
invoice/payout credits unless their settlement is explicitly confirmed.

**Architecture assumption:** Count only confirmed, dated salary/future credits;
exclude pending and unsupported scheduled credits.

**Agreement:** Yes for salary/pending categories; the generic scheduled-credit
boundary is intentionally conservative because the specification is silent.

**Required change:** Require an explicit evidence fact for non-salary future
credits (`confirmed`, amount, currency, settlement date). Otherwise exclude the
credit and record the reason.

## 7. Recurrence and month-end behavior

**Rule found:** Detect recurrence only when history supports it and forecast
essential variable spending conservatively. No numeric minimum observation count,
cadence tolerance, or month-end rule is supplied. One-off purchases, transfers,
refunds, and unusual events must not be treated as recurring.

**Architecture assumption:** Infer cadence from repeated same-user/category/source
history and explicitly handle weekly/monthly patterns, including month-end.

**Agreement:** Direction agrees; exact thresholds do not exist in the source.

**Required change:** Keep thresholds configurable and versioned. Add fixtures for
28/30/31-day cadence, February/month-end rollovers, missing occurrences, amount
variation, and coincidental discretionary events. Never claim one threshold is
mandated by the challenge.

## 8. Failed/cancelled obligations and replacement debits

**Rule found:** The 90-day check says ignore failed or cancelled transactions.
Linked events represent a lifecycle but the link alone does not determine cash
flow. Conflict precedence prefers explicit cancellation/settlement/amendment,
then newer same-source evidence, then settled event, then safer interpretation.
A message may clarify that a failed bill remains outstanding or another debit will
be attempted.

**Architecture assumption:** Exclude failed/cancelled cash movements; if explicit
evidence establishes a replacement obligation, represent exactly one future
reserved debit and retain the lifecycle provenance.

**Agreement:** Yes for exclusion and precedence; the exact replacement date when a
message gives no date is unspecified.

**Required change:** Never invent a replacement date or amount. If evidence does
not fully specify it, reserve the known obligation only under a deterministic
conservative rule or quarantine it as unresolved and explain the safer choice.

## 9. FX behavior when direct rate is unavailable

**Rule found:** Use the supplied fixed rate matched by settlement date and stated
`from_currency`→`to_currency` direction. No live rates are needed. The challenge
does not authorize inversion, triangulation, nearest-date substitution, or a rate
fallback when a direct row is missing.

**Architecture assumption:** Require an exact direct rate; never invent an inverse
or cross-rate.

**Agreement:** Yes.

**Required change:** Treat missing direct FX as an explicit data/decision error and
apply a documented financially safer fallback (exclude unconfirmed credit or
reserve debit conservatively) only where the output contract requires a result.
Do not silently substitute another date or direction.

## 10. Deadline failure versus affordable_later/not_affordable

**Rule found:** `affordable_later` means the full amount is expected to become safe
later; `not_affordable` means the full request cannot be completed safely within
the forecast period. Plans must complete by desired completion date. A wait plan
is eligible only when full payment is accepted and the safe date exists; ranking
prefers deadline completion.

**Architecture assumption:** Reject candidates missing the requested deadline;
return wait/affordable_later only for a safe later completion represented by the
contract; otherwise not_recommended/not_affordable.

**Agreement:** Partially. The source does not explicitly define whether a safe date
after the user's desired deadline should be `affordable_later` or
`not_affordable`, nor whether a late wait plan should be emitted.

**Required change:** Separate `earliest_date_for_full_payment` (capacity fact) from
recommendation eligibility. Do not emit a late payment plan as a deadline-compliant
recommendation. Use a documented conservative mapping and test both sides of the
deadline boundary.

## 11. Decimal rounding and trailing zeros

**Rule found:** Amounts may be decimal; plans must sum exactly; no rounding mode or
scale is specified. Solved outputs preserve meaningful decimal forms (`620.40`,
`15952906.67`, integers without a decimal suffix), but this is observational, not
an explicit formal serialization rule.

**Architecture assumption:** Keep high-precision fixed-point values internally and
serialize deterministically, preserving exact supplied option amounts.

**Agreement:** Yes in principle; any particular scale/rounding choice is not
specified.

**Required change:** Add exact Decimal tests for half-cent/paise boundaries,
installment sums, and trailing-zero preservation. Never use binary floating point.

## 12. Ties between flexible-spending changes

**Rule found:** Up to three `stop:`/`reduce_to:` actions are allowed, only on
non-protected flexible recurring events in permitted categories. The same event
cannot be both stopped and reduced. Ranking says avoid changes but gives no final
event/action tie-break.

**Architecture assumption:** Enumerate valid sets, prefer no-change sets, then use
the published ranking, with a deterministic sorted-ID tie-break for otherwise
equal sets.

**Agreement:** Yes except the final tie-break is an implementation addition.

**Required change:** Explicitly label sorted event/action ordering as a reproducible
fallback. Test multiple equally sufficient sets, protected categories, minimum
allowed reduction, and the three-action limit.

## Verification conclusion and implementation gate

The architecture agrees with all explicit challenge rules when its unspecified
policies are treated as configurable conservative defaults rather than facts. The
following must remain visible in implementation and interview explanation:

- arithmetic, forecasting, candidate feasibility, ranking, and validation are
  deterministic;
- LLM output is typed evidence or prose only and can never authorize a plan;
- no sample output is hardcoded;
- unresolved semantics (same-day ordering, recurrence threshold, generic scheduled
  credits, failed replacement timing, late-deadline mapping, serialization, and
  flexible-set ties) are covered by explicit tests and provenance.

Only after this report is accepted should production modules be implemented in the
requested order: `io.py`, `ledger.py`, `forecast.py`, `plans.py`, validator,
`evidence.py`, `explanations.py`, `main.py`, tests, usage report, and output.
