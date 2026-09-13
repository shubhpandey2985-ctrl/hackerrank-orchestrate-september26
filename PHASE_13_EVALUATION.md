# Phase 13 Evaluation

## Baseline and production

No production semantic change was justified. Therefore before → after is unchanged for every field:

| field | before | after | regressions | improvements |
|---|---:|---:|---:|---:|
|amount_safe_to_pay|2/25|2/25|0|0|
|affordability_status|10/25|10/25|0|0|
|recommended_payment_method|12/25|12/25|0|0|
|payment_plan|11/25|11/25|0|0|
|earliest_date_for_full_payment|8/25|8/25|0|0|
|spending_changes_needed|22/25|22/25|0|0|

- Tests: 54 full-suite tests passed.
- Output rows: 250.
- Output SHA-256: `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.
- Safety violations: none observed.
- First divergence: safe amount for 23 requests; serialization for 2.
- No dataset, expected-output, or output.csv changes were made.

Counterfactual model scores are supporting evidence only and do not authorize a semantic change.
