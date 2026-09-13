# Forecast Contract

## Executive conclusion

The strongest defensible contract is: explicit confirmed cash movements plus
supported fixed recurrence, exact Decimal arithmetic, direct supplied FX,
strict lifecycle handling, and a deterministic 90-day minimum-balance
simulation. Variable amounts, recurrence calendar rules, optional-baseline
scope, generic scheduled credits, same-day ordering, replacement timing and
late-deadline status mapping remain unresolved and configurable. They must not
be inferred from sample scores.

## Evidence hierarchy

1. Authoritative challenge specification.
2. Explicit repository requirements and tests.
3. Explicit solved-example facts.
4. Repeated independent example behavior.
5. Engineering inference, always labelled as such.

## Event classification and lifecycle

| Event | Include? | Cash effect/date | Recurrence/flexibility | Evidence |
|---|---|---|---|---|
| Settled debit | yes | debit on settlement/event date | eligible only if supported recurring | SPECIFICATION-EXPLICIT |
| Settled credit | yes | credit on settlement/event date | historical recurrence does not alone create future cash | SPECIFICATION-EXPLICIT |
| Pending debit | reserve | debit on supplied settlement date | not modifiable unless separately supported flexible recurrence | SPECIFICATION-EXPLICIT / STRONGLY-EXAMPLE-SUPPORTED |
| Pending credit | no | no available capacity | never a usable future credit | SPECIFICATION-EXPLICIT |
| Failed/cancelled/unrealized | no | no cash movement | terminal lifecycle | SPECIFICATION-EXPLICIT |
| Non-cash | no | no cash movement | never available cash | SPECIFICATION-EXPLICIT |
| Confirmed future payment | yes | supplied date/amount | explicit source facts only | SPECIFICATION-EXPLICIT |
| Confirmed future salary | yes | supplied settlement date | amount and date required | SPECIFICATION-EXPLICIT |
| Message-confirmed salary | yes | explicit message date/amount | provenance retained | STRONGLY-EXAMPLE-SUPPORTED |
| Historical salary | historical evidence only | no invented future credit | no automatic extrapolation | STRONGLY-EXAMPLE-SUPPORTED |
| Terminal/final salary | stop | no later extrapolation | terminal marker wins | STRONGLY-EXAMPLE-SUPPORTED |
| Generic scheduled credit | unresolved; conservative exclusion | no capacity unless explicitly confirmed | configurable policy | UNRESOLVED |
| Fixed recurring expense | yes if identity, cadence and amount are stable | projected supported amount | protected/flexible metadata retained | STRONGLY-EXAMPLE-SUPPORTED |
| Variable recurring expense | evidence only | no invented amount | `RECURRING_AMOUNT_UNRESOLVED` | SPECIFICATION-EXPLICIT |
| One-time expense | yes on supplied date | supplied amount only | not recurrence-eligible | SPECIFICATION-EXPLICIT |
| Protected expense | always | supplied/projected movement | never modifiable | SPECIFICATION-EXPLICIT |
| Flexible recurring expense | baseline policy dependent | may be changed only by valid candidate | max three actions | SPECIFICATION-EXPLICIT |
| Linked replacement | only live row with its own date/amount | supplied facts only | no inferred timing | SPECIFICATION-EXPLICIT |
| Foreign-currency event | yes if rate exists | direct dated supplied FX | Decimal multiplication | SPECIFICATION-EXPLICIT |

Lifecycle precedence removes duplicate cash movements while preserving source
provenance. A replacement is never invented from a failed or cancelled row.

## Recurrence rules

Identity uses user, category, description/merchant/source, direction and
currency; category alone is insufficient. Projection requires repeated
occurrence, stable cadence, stable amount, non-terminal lifecycle and no
contradictory cancellation/failure/amendment. The supported production baseline
projects only fixed equal-amount series. Calendar cadence, gap tolerance,
month-end clamping, missed-cycle recovery and observation thresholds remain
`UNRESOLVED`.

## Income and scheduled credits

Only explicit settled/confirmed future credits or message-confirmed salary
facts with both amount and date may create future capacity. Historical salary
observations, missed cycles and generic scheduled labels do not independently
create money. Terminal employment/payroll evidence stops extrapolation.

## Optional baseline

The configurable policies are `CURRENT_BEHAVIOR`, `INCLUDE_REQUIRED_ONLY`,
`INCLUDE_ALL_RECURRING` and `EXCLUDE_OPTIONAL_FLEXIBLE`. The production default
is `CURRENT_BEHAVIOR` because the specification says safe amount is measured
before optional changes while earliest-date/full-plan checks use the complete
required ledger. The samples do not uniquely distinguish the close alternatives
and no policy is selected solely by score.

## Pending, same-day, FX and horizon

Pending credits are excluded; pending debits are reserved at supplied
settlement. Same-day ordering is deterministic credits → debits → plan payment,
but this is an explicit unresolved policy, not a specification fact. FX is only
the supplied direct rate for the required date and currency pair. The forecast
horizon is request date day zero through the next 89 days; every movement and
candidate payment must preserve the minimum balance after movement.

## Safe amount, earliest date and deadlines

`safe_amount` is a monotone Decimal capacity query: the largest payment on the
request date that leaves every post-movement balance at or above the minimum,
capped by the requested amount and independent of candidate ranking.
`earliest_safe_date` independently scans every horizon date for a full payment
and records the first date passing the same movement-level invariant. Payment
preference and ranking do not affect that date. Capacity date, deadline and
candidate completion date remain separate; late-capacity status mapping is
unresolved.

## Hidden-test risks and prohibited inference

Never introduce category-only recurrence, an inferred variable amount, salary
cash from history alone, FX inverse/triangulation/substitute dates, replacement
timing, same-day ordering as if mandated, or LLM-authorized arithmetic or
plans. These are the highest-risk hidden-test failure modes.

## Recommended semantic model

Immutable provenance-aware ledger → explicit lifecycle state → supported fixed
recurrence evidence → deterministic Decimal day-by-day forecast → safe amount
and earliest date → deterministic candidate validation/ranking. Keep unresolved
boundaries configurable and require fixture evidence before changing them.
