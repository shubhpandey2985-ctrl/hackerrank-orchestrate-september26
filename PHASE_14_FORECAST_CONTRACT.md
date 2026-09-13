# Phase 14 Forecast Contract

Analysis-only canonical movement contract generated from the supplied schemas and frozen production classifier.

- Raw movement rows: 25342
- Canonically included live rows: 25281
- Explicitly excluded rows: 61
- Horizon: 90 days
- Same-day policy: `credits_before_required_debits_before_plan` (explicit engineering policy, not specification-mandated)

## Required movement fields

Each row in `PHASE_14_FORECAST_CONTRACT.json` records source ID, user, event/settlement/forecast dates, amount/currency/home amount, direction, lifecycle, cash classification, pending/settled/confirmed state, recurrence identity/cadence/stability, flexibility/protection/optional status, terminal marker, linked lifecycle, confirmation, provenance, inclusion flag, and an explicit reason.

## Contract boundary

Supported: explicit dated cash movements, lifecycle exclusion, pending-credit exclusion, pending-debit reservation, direct supplied FX, Decimal arithmetic, stable fixed recurrence evidence and minimum-balance simulation.

Unresolved: variable amounts, recurrence calendars/missed cycles/month-end, generic scheduled credits, optional baseline, same-day order, replacement timing and late-deadline mapping. These are not silently promoted to specification rules.
