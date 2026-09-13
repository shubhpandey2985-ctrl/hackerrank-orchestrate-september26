# Phase 13 Decision

## Outcome

`PARTIALLY_RESOLVED`

Supported semantics remain implemented and frozen: explicit confirmed cash
movements, lifecycle exclusions, pending-credit exclusion, pending-debit
reservation, direct dated FX, Decimal arithmetic, protected minimum-balance
simulation, hard payment preferences and deterministic validation. The
analysis reconstructs these as the strongest defensible core model.

The unresolved boundaries cannot be distinguished from the available evidence:
variable amount estimation, recurrence calendar and missed-cycle behavior,
optional-baseline scope, generic scheduled credits, same-day ordering,
replacement timing, late-deadline status mapping and decimal presentation.
No production change is justified by sample score alone.

## Production change

None. The frozen production behavior is preserved. Analysis-only artifacts
contain the 25-request matrix, causal traces, variable-series inventory,
counterfactual model table and before/after evaluation.

## Anti-overfitting gate

No request IDs, user IDs, expected answers, sample-specific dates or amounts,
fixture branches, expected-output lookup, or arbitrary scoring constants were
added to production. Variable spending uses no mean, median, latest, maximum,
minimum or smoothing estimator.

## Safety and validation

The 54-test suite passes. No safety violations were observed in the analysis
run: no negative payments, unsupported FX, duplicate lifecycle movements, or
below-minimum balances were introduced. The output hash remains unchanged.

## Next highest-value investigation

Add fixture-backed contract tests that isolate recurrence calendar/month-end
and optional-baseline boundaries, then rerun counterfactuals. Do not repair
downstream ranking while safe-amount semantics remain upstream-unresolved.
