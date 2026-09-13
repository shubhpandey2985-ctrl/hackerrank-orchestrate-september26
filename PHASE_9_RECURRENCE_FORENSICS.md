# Phase 9 — Recurrence Calendar Forensics

Status: analysis-only. No production code, dataset, expected output, output.csv, or code.zip was modified.

## Inventory

Inventoried **728** source-identity series across the 25 solved users. Identity includes user, category, description, direction and currency; unrelated descriptions were not merged.

Classification counts:
- `EXPLICIT_FIXED_RECURRING`: 115
- `EXPLICIT_FUTURE_EVENT`: 11
- `ONE_TIME`: 160
- `TERMINATED`: 1
- `VARIABLE_RECURRING`: 286
- `WEAK_HISTORICAL_PATTERN`: 155

Each JSON series records event IDs, dates, amounts, gaps, lifecycle states, flexibility, protected status, terminal markers, linked lifecycle rows, explicit future rows, candidate exact/monthly dates and provenance.

## Calendar counterfactual score table

| Model | Safe | Status | Method | Plan | Earliest | Changes |
|---|---:|---:|---:|---:|---:|---:|
| A_EXACT_INTERVAL | 2 | 10 | 12 | 11 | 8 | 22 |
| B_CALENDAR_WEEKLY | 2 | 10 | 12 | 11 | 8 | 22 |
| C_CALENDAR_BIWEEKLY | 2 | 10 | 12 | 11 | 8 | 22 |
| D_MONTHLY_DAY_OF_MONTH | 2 | 10 | 12 | 11 | 8 | 22 |
| E_MONTH_END_CLAMP | 2 | 10 | 12 | 11 | 8 | 22 |
| F_EXPLICIT_FUTURE_ONLY | 3 | 12 | 14 | 13 | 9 | 22 |
| G_FIXED_STABLE_ONLY | 2 | 10 | 12 | 11 | 8 | 22 |

These scores are diagnostics only. The current implementation does not actually switch to calendar-month or weekly arithmetic in this analysis; models A–E are represented as date-policy alternatives over the same supported recurrence evidence. No score is treated as specification proof.

## Missed cycles and month-end

Observed irregular gaps do not prove preserve, skip-and-resume, terminate, or explicit-confirmation semantics. Month-end cases (28/29/30/31 and 30-day months) have candidate dates that differ between exact intervals and calendar day-of-month/clamping. No solved fixture uniquely establishes overflow versus clamp versus exact-day behavior. **Month-end remains unresolved.**

## Terminal, amended and lifecycle series

Final/last/ended/terminated descriptions and failed/cancelled rows are terminal evidence and must not produce extrapolated movements. A linked replacement is usable only with its own supplied date and amount. Duplicate lifecycle rows must not create two debits. These rules are specification/evidence-supported and remain production invariants.

## Variable amounts

Variable series are classified `VARIABLE_RECURRING` and remain `VARIABLE_AMOUNT_UNRESOLVED` unless an explicit future amount exists. No mean, median, latest, maximum, minimum or percentile was used.

## Mismatch distinction

Amount/date mismatch classifications are machine-readable in JSON: OTHER=23, RECURRENCE_DATE_ERROR=17.

## Strongest defensible model

The strongest defensible model is explicit confirmed movements plus stable fixed recurrence with source identity, terminal lifecycle checks and no invented variable amount. Calendar date semantics remain configurable because the specification and solved examples do not resolve them.

## Phase 10 recommendation

**RECURRENCE_REMAINS_UNRESOLVED**. The minimum evidence needed is a fixture with at least one repeated series and an authoritative expected next date (including month-end/missed-cycle behavior), amount, lifecycle state, and resulting minimum-balance trace. The smallest Phase 10 change is a fixture-backed recurrence-calendar policy boundary, followed by deterministic regression and metamorphic tests; do not alter production recurrence before that evidence exists.

## Required never-assume rules

Never use category-only recurrence, inferred variable amounts, historical salary cash without confirmation, invented replacement dates/amounts, FX fallbacks, or LLM-authorized financial decisions.
