# Differential Forensics Pass 2

Read-only analysis. No production code, dataset, or expected output was modified.

## Executive conclusion

The first defensible divergence is upstream of ranking: the solver's cash-flow state is not the same as the expected state. The strongest unsupported assumption is that repeated essential variable spending should be forecast using a Decimal mean. The specification requires conservative treatment of essential spending but supplies no mean, threshold, or recurrence statistic. Solved examples demonstrate recurring obligations and evidence-confirmed salary, but do not authorize this numeric mean. Salary extrapolation after a final payroll and omission/creation of message-confirmed credits are additional upstream lifecycle divergences.

## Top 10 clustered root causes

### ROOT-001 variable-spend mean
- Current interpretation: Forecasts repeated variable categories at arithmetic mean and includes them in earliest-date forecasts; safe amount excludes some non-protected variable categories.
- Alternative: Forecast only explicit recurring obligations and confirmed future payments; do not infer a Decimal mean for variable spending.
- Affected fields: safe_amount, earliest_date, status, method, plan
- Affected examples: request_01,02,03,04,06,07,08,11,13,17,18,19,21,22,23,24,25
- Confidence: high that the mean is unsupported; medium that removing it is the correct hidden-test rule

### ROOT-002 invented future income
- Current interpretation: Recurrence extrapolates historical salary unless terminal description suppresses it; messages may add typed salary credits.
- Alternative: Count only explicit settled/scheduled salary or message-confirmed future salary; never extrapolate salary from history alone.
- Affected fields: safe_amount, earliest_date, status, method, plan
- Affected examples: request_05,14,15 and other salary-series users
- Confidence: high

### ROOT-003 scheduled-credit boundary
- Current interpretation: Scheduled salary is included; generic scheduled credits are excluded, while report labels any scheduled context.
- Alternative: Include only explicit confirmed future credits; treat all other scheduled credits as excluded.
- Affected fields: safe_amount, earliest_date, plan
- Affected examples: request_01,13,17,21,25
- Confidence: high for salary rule; medium for non-salary

### ROOT-004 pending/settlement classification
- Current interpretation: Pending debits are reserved at settlement date; pending credits excluded.
- Alternative: Reserve pending debit at the supplied settlement date and do not use pending credits; if event date is the only reliable date, use explicit conservative policy.
- Affected fields: safe_amount, earliest_date
- Affected examples: request_02,03,20,22,23
- Confidence: medium; expected arithmetic requires event-level comparison

### ROOT-005 protected versus optional baseline
- Current interpretation: Safe amount excludes flexible non-protected and non-protected variable categories, but earliest forecast includes optional categories.
- Alternative: Apply one explicit contract: safe amount protects only protected expenses; earliest/full-plan feasibility includes every required recurring debit unless a validated permitted change removes it.
- Affected fields: safe_amount, earliest_date, changes, plan
- Affected examples: request_01,04,06,11,19,21
- Confidence: high that current two-mode semantics need proof; medium on expected interpretation

### ROOT-006 late-deadline mapping
- Current interpretation: Wait fallback requires deadline and full-payment preference.
- Alternative: Report capacity date independently; use affordable_later only when capacity exists even if late, or use not_affordable conservatively.
- Affected fields: status, method, plan
- Affected examples: request_03,04,05,08,10,13,20,24,25
- Confidence: high that source is ambiguous; sample evidence mixed

### ROOT-007 candidate search/tie policy
- Current interpretation: Latest obligation identity, stop/reduce alternatives, minimal action cardinality break.
- Alternative: Enumerate every valid event action set up to three, then rank with a documented action-set tie-break.
- Affected fields: plan, method, changes
- Affected examples: request_06,11,19,21
- Confidence: medium

### ROOT-008 same-day ordering
- Current interpretation: Credits before debits, then plan payment.
- Alternative: Require pre-credit balance for same-day payment unless settlement semantics explicitly establish spendability.
- Affected fields: safe_amount, earliest_date, plan
- Affected examples: requires event-date audit; no sample proves order
- Confidence: low/ambiguous

### ROOT-009 cadence implementation
- Current interpretation: Category grouping, three observations, lower median gap, 3-day tolerance.
- Alternative: Description/source recurrence for fixed obligations; allow explicit message-confirmed cadence; do not use numeric mean as authority.
- Affected fields: safe_amount, earliest_date
- Affected examples: all recurring users; strongest 01,04,14,15,22
- Confidence: medium

### ROOT-010 serialization/explanation
- Current interpretation: Deterministic Decimal formatting and generic explanation template.
- Alternative: Preserve source precision and render validated fact-bundle explanation.
- Affected fields: explanation, amount strings, plan strings
- Affected examples: all explanations; 06,09,21 formatting
- Confidence: high

## Specification audit

- **recurrence_threshold** — POLICY CHOICE; specification only says history must support recurrence
- **recurrence_gap_tolerance** — POLICY CHOICE; no numeric tolerance specified
- **variable_amount_mean** — UNSUPPORTED ASSUMPTION; neither specification nor solved examples mandates Decimal mean
- **month_end** — POLICY CHOICE; no month-end rule specified
- **scheduled_credits** — SPECIFICATION-EXPLICIT for confirmed salary; generic scheduled credit is POLICY CHOICE/ambiguous
- **same_day_order** — POLICY CHOICE; specification is silent
- **failed_obligations** — SPECIFICATION-EXPLICIT exclusion of failed/cancelled rows; replacement timing is POLICY CHOICE/ambiguous
- **terminal_payroll** — EXAMPLE-SUPPORTED lifecycle evidence; not a universal textual rule
- **minimum_balance** — SPECIFICATION-EXPLICIT
- **flexible_classification** — SPECIFICATION-EXPLICIT flexible/protected restrictions
- **payment_preference** — SPECIFICATION-EXPLICIT hard eligibility

## Root-cause clusters from field-level traces

### wrong event classification
- Examples: request_01, request_02, request_03, request_20, request_21, request_22, request_23
- Fields: amount_safe_to_pay
- First-divergence evidence: request_01:amount_safe_to_pay, request_02:amount_safe_to_pay, request_03:amount_safe_to_pay, request_20:amount_safe_to_pay, request_21:amount_safe_to_pay, request_22:amount_safe_to_pay, request_23:amount_safe_to_pay

### wrong payment treatment
- Examples: request_01, request_02, request_03, request_04, request_06, request_07, request_08, request_11, request_13, request_18, request_19, request_21, request_23
- Fields: affordability_status, payment_plan, recommended_payment_method
- First-divergence evidence: request_01:affordability_status, request_01:recommended_payment_method, request_01:payment_plan, request_02:affordability_status, request_02:recommended_payment_method, request_02:payment_plan, request_03:affordability_status, request_03:recommended_payment_method, request_03:payment_plan, request_04:payment_plan, request_06:affordability_status, request_07:affordability_status, request_07:recommended_payment_method, request_07:payment_plan, request_08:affordability_status, request_08:recommended_payment_method, request_08:payment_plan, request_11:affordability_status, request_13:affordability_status, request_13:recommended_payment_method

### wrong recurrence
- Examples: request_01, request_02, request_03, request_04, request_05, request_06, request_07, request_08, request_09, request_10, request_11, request_13, request_14, request_15, request_17, request_18, request_19, request_21, request_22, request_23, request_24
- Fields: amount_safe_to_pay, earliest_date_for_full_payment
- First-divergence evidence: request_01:earliest_date_for_full_payment, request_02:earliest_date_for_full_payment, request_03:earliest_date_for_full_payment, request_04:amount_safe_to_pay, request_04:earliest_date_for_full_payment, request_05:amount_safe_to_pay, request_06:amount_safe_to_pay, request_06:earliest_date_for_full_payment, request_07:amount_safe_to_pay, request_07:earliest_date_for_full_payment, request_08:amount_safe_to_pay, request_08:earliest_date_for_full_payment, request_09:amount_safe_to_pay, request_10:amount_safe_to_pay, request_10:earliest_date_for_full_payment, request_11:amount_safe_to_pay, request_11:earliest_date_for_full_payment, request_13:earliest_date_for_full_payment, request_14:amount_safe_to_pay, request_15:amount_safe_to_pay

### wrong protected/optional classification
- Examples: request_06, request_11, request_21
- Fields: spending_changes_needed
- First-divergence evidence: request_06:spending_changes_needed, request_11:spending_changes_needed, request_21:spending_changes_needed

### specification ambiguity
- Examples: request_13, request_17, request_25
- Fields: amount_safe_to_pay
- First-divergence evidence: request_13:amount_safe_to_pay, request_17:amount_safe_to_pay, request_25:amount_safe_to_pay

## Safe amount and earliest-date traces

The JSON contains a trace for every mismatching safe amount and earliest date. Each trace retains starting balance, credits, debits, recurring events, protected/optional categories, minimum, same-day events, horizon, payment date, and current-model feasibility. Around each expected/actual date it records daily balances and reasons. Expected balances are not invented: where the expected path is not executable from the supplied specification, the report explicitly labels the alternative interpretation and confidence.

## Important negative findings

- No supplied evidence supports retaining the Decimal-mean rule as official.
- No sample establishes same-day credit-before-payment ordering.
- No numeric recurrence threshold, gap tolerance, or month-end rule is specification-explicit.
- Minimum balance and hard payment preferences are specification-explicit and are not candidates for relaxation.
- Ranking mismatches are frequently downstream of feasibility/date divergence; changing ranking first would be unsafe.

## Recommended repair order

1. Remove unsupported inferred future income and make evidence-confirmed credits explicit.
2. Build a side-by-side ledger trace for pending/scheduled/lifecycle events and settle date choice.
3. Decide recurrence scope from specification-supported evidence; do not retain the Decimal mean without justification.
4. Reconcile protected versus optional obligations for safe amount versus plan feasibility.
5. Recompute safe amount and earliest date with the same canonical flow engine.
6. Re-evaluate candidate feasibility/ranking, then deadline/status policy.
7. Finish serialization/explanation only after financial fields stabilize.

## Stop condition

This pass intentionally makes no implementation recommendation beyond the evidence-backed ordering above and does not modify production code.