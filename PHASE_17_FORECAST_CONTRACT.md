# Phase 17 Forecast Contract

The production forecast follows `FACTS → EVIDENCE → MOVEMENTS → SAFETY →
CAPACITY → DECISION`. Explicit confirmed movements and supported stable fixed
recurrences are the only production-eligible future movements. Every other
inference remains visible as `UNRESOLVED_INFERENCE` but contributes no cash.

Excluded cash facts include pending credits, failed/cancelled/unrealized/non-
cash records, duplicate lifecycle rows, unsupported income/replacements and
missing direct FX. Every included movement retains source IDs, description,
category, currency, original and home amount, date, movement type, evidence
class, recurrence identity, lifecycle evidence, confidence and inclusion or
exclusion reason.

Optional baseline and same-day order remain explicit policies. The forecast core
does not rank methods, generate plans/actions, serialize output or explain
decisions; those remain downstream.
