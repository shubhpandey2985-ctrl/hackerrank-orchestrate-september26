# Phase 14 Decision

## Outcome

`BLOCKED`

The supported deterministic core remains intact: explicit confirmed
movements, stable fixed recurrence only, strict lifecycle/pending handling,
direct dated FX, Decimal arithmetic, minimum-balance safety and deterministic
validation.

The high-impact forecast ambiguity is not resolved. The 23 safe-amount first
divergences are observationally confounded by variable amounts, recurrence
calendar/missed-cycle behavior, optional baseline, generic scheduled credits,
same-day ordering and replacement timing. The specification and examples do
not justify selecting one competing model.

No production semantic repair passed the change gate. Ranking, preferences,
plan grammar and explanations were not touched. No code.zip was created and
the output was not regenerated.

Next step: fixture-backed tests that independently isolate variable spending,
month-end/missed recurrence, generic scheduled credits, same-day order,
optional baseline and replacement lifecycle.
