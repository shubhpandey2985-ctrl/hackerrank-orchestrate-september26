# Phase 15 System Boundary

`load_data` validates CSV schemas and creates canonical `Data`/`Event` values.
`normalize_events` resolves Decimal amounts, direct dated FX and cash state.
`semantic_events` applies lifecycle exclusions, duplicate resolution, pending
credit exclusion and explicit message-confirmed salary extraction.
`recurring` detects source-identity series and resolves only stable fixed debit
amounts. `forecast` constructs the 90-day ledger and applies same-day policy.
`safe_amount` performs a Decimal monotone search; `earliest` scans each date.
`candidate` generates payment plans and flexible actions; `validate_output`
checks hard constraints and re-simulates the plan. Ranking and serialization
are downstream of forecast state. `semantic_lab.py` is analysis-only and does
not call or mutate these production functions.

