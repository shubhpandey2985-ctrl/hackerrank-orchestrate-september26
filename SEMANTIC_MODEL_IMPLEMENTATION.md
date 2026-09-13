# Semantic Model Implementation

Phase 4 implementation record. This phase follows
`SPECIFICATION_RECONSTRUCTION.md`; it does not modify supplied datasets or
expected outputs and does not create `code.zip`.

## Dependency implemented

```text
source evidence
  -> canonical lifecycle ledger
  -> recurrence evidence (without invented amount)
  -> deterministic Decimal forecast
  -> safe amount / earliest date
  -> existing candidate generation
  -> deterministic validation/ranking
  -> output
```

## Changes

### Canonical recurrence evidence

`main.RecurrenceEvidence` stores the source events, identity, cadence,
amount-policy name, optional estimate, provenance IDs and confidence. The
`main.recurring` detector now retains description/source identity and never
turns repeated variable categories into an arithmetic mean. Variable series
are returned as `unresolved_variable_amount`; historical income is returned as
`no_historical_income_extrapolation`. Only fixed debit obligations with a
resolved source amount are projected.

The interfaces are exposed through `ledger.detect_recurrence` and the existing
`main.recurring` adapter. Detection and estimation are intentionally separate.

### Income and scheduled credits

Historical salary observations no longer create future credits. Explicit
settled/scheduled confirmed salary rows and message-confirmed salary facts
remain dated ledger movements with source/message provenance. Terminal payroll
messages/descriptions continue to suppress later income. Generic scheduled
non-income credits remain excluded by the explicit policy in `policy.py`.

### Lifecycle and classification

`semantic_events` now collapses lifecycle duplicates using a documented status
precedence, while failed/cancelled/unrealized/non-cash rows remain excluded.
Linked live replacements are used only with their supplied date and amount.
`classify_event` is the canonical protected/flexible/optional/fixed/modifiable
classification and requires recurrence evidence before marking a flexible
event modifiable.

### Forecast auditability

`forecast_trace` and `forecast.trace` expose movement-level records containing
date, event/source ID, event type, cash state, currency, home amount, balance
before/after, minimum balance and safety result. The trace also records the
selected same-day-order and horizon policies. Existing `forecast` callers keep
the original `(safe, balances)` interface.

## Deliberately unresolved policies

The implementation does not silently claim rules that the specification leaves
undefined. Variable amount estimation, optional baseline inclusion, recurrence
threshold/gap/month-end behavior, same-day order, generic scheduled credits,
replacement timing, late-deadline mapping, flexible-action ties and decimal
trailing-zero serialization remain explicit policy/configuration questions.

## Non-goals in this phase

Candidate ranking was not redesigned to compensate for forecast changes. No
sample request ID is special-cased, and no expected sample value is embedded
in production code.
