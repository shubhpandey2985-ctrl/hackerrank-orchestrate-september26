# Phase 12 Decision

## Status

`UNRESOLVED`

## Definitely known

The specification supports explicit confirmed cash movements, lifecycle
exclusions, pending-credit exclusion, pending-debit reservation, direct dated
FX, Decimal arithmetic, stable fixed recurrence evidence, minimum-balance
protection, a 90-day deterministic horizon, independent safe amount and
earliest-date queries, hard payment preferences and deterministic validation.

## Unresolved

Variable amount estimation, optional-baseline scope, recurrence calendar and
missed cycles, month-end behavior, generic scheduled credits, replacement
timing, same-day ordering, late-deadline status mapping and decimal presentation.

## Production should implement

The current strongest model: explicit confirmed movements plus stable fixed
recurrence, with provenance and fail-closed missing evidence.

## Production must not implement

Category-only recurrence, inferred variable amounts, historical salary cash
without confirmation, FX fallbacks, invented replacements, sample-specific
exceptions, or LLM-authorized financial calculations/plans.

## Configurability

Keep optional baseline, recurrence calendar, scheduled-credit boundary, same-day
ordering and late-deadline status as explicit policies until fixture evidence
resolves them.

## Next step

Create one fixture-backed contract suite for recurrence/calendar and optional-
baseline boundaries before any production forecast change. Do not begin
downstream ranking repair.
