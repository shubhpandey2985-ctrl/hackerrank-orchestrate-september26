# Phase 16 Implied Cashflow

For each of the 23 safe-amount-first-divergence rows, the actual solver trace
contains a deterministic opening balance, dated movements, and minimum-balance
floor in `PHASE_13_BEHAVIOR_MATRIX.json`. The expected amount implies that one
or more future movements differ, but the available evidence does not identify
which one: a varying obligation, a calendar-generated date, optional-baseline
scope, scheduled-credit treatment, or same-day order can produce the same
capacity delta.

Therefore the rows are classified **multiple interpretations remain possible**
or **insufficient evidence**, not “definitely variable.” No future movement is
invented from an output number. The two non-safe-amount rows are serialization
divergences.
