# Semantic Model Test Report

## Verification run

Commands:

```text
pytest -q code
python code/evaluation.py
python code/main.py
```

Results:

- Focused semantic tests: **12 passed**
- Complete suite: **39 passed**
- 25-example evaluation completed successfully
- Output generation completed successfully

## Added focused coverage

- unresolved variable recurrence does not invent an amount or future debit;
- historical salary recurrence does not invent future credit;
- pending/settled lifecycle rows collapse to the settled movement;
- flexible events are modifiable only with recurrence evidence;
- movement-level forecast trace records provenance, balances and policy;
- existing pending, cancelled, failed, duplicate, Decimal, FX, deadline,
  minimum-balance, installment, partial-payment and preference tests remain
  green.

## 25-example comparison

| Field | Previous repair baseline | Semantic-model phase |
|---|---:|---:|
| safe amount | 2/25 | 2/25 |
| status | 15/25 | 10/25 |
| payment method | 17/25 | 11/25 |
| payment plan | 14/25 | 10/25 |
| earliest safe date | 9/25 | 8/25 |
| spending changes | 22/25 | 22/25 |

The regression in downstream fields is expected evidence that removing
unsupported inferred flows changes feasibility and candidate selection. It is
not repaired with example-specific rules. The first-divergence category for
most changed rows is still ledger/recurrence semantics; remaining independent
categories include optional-baseline scope, scheduled-credit policy,
same-day ordering, deadline mapping and unresolved flexible ties.

## Determinism and safety checks

- all arithmetic remains `Decimal`;
- no binary floating-point arithmetic was introduced;
- no FX fallback or invented event was introduced;
- validator and ranking remain downstream of the forecast;
- supplied datasets and expected outputs were not modified;
- no `code.zip` was created.
