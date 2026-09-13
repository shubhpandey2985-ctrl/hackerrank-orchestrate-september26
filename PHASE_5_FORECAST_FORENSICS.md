# Phase 5 — Forecast Contract Forensics

Status: analysis-only. No production code, dataset, or expected output was modified.

## Scope and method

The traces below reverse-engineer constraints from the supplied expected fields. A residual is arithmetic evidence, not permission to invent a movement. Every movement is labelled by evidence class; UNKNOWN remains unknown.

Evidence classes: DIRECTLY OBSERVED, MESSAGE-CONFIRMED, SCHEDULED/CONFIRMED, RECURRING-INFERRED, UNKNOWN.

## Expected implied cash-flow findings

A positive residual (`actual - expected`) means the current model has more capacity than the expected answer; the missing constraint could be a debit, an omitted credit, a different protected/optional baseline, or a date/order rule. It is not assigned to an invented event.

### request_02

- Safe amount: expected `17229139.2`, current `14334739.38`, residual `-2894399.82`.
- Earliest full payment: expected `2025-09-15`, current `2025-10-13`; deadline `2025-10-10`.
- Starting/minimum: `60383889.2` / `29158400`.
- First divergences: safe `wrong event classification`; earliest `wrong recurrence`.
- Root-cause cluster: **pending/lifecycle semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_185 2025-08-08 debit 1651100 Pending merchant debit [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 1.
- Recurrence evidence series: 11; protected categories `{'housing', 'utilities', 'education'}`; optional `{'cloud_storage', 'entertainment'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2025-09-15", "debits": "0", "ending_balance": "43389790.03859829059829059829059829059831", "feasible_current_model": false, "minimum_required": "29158400", "reason": "current forecast minimum-floor failure", "requested_payment": "46018000", "starting_balance": "89407790.03859829059829059829059829059831"}
  - {"credits": "0", "date": "2025-10-13", "debits": "0", "ending_balance": "54445425.1822564102564102564102564102564", "feasible_current_model": true, "minimum_required": "29158400", "reason": "current forecast predicate", "requested_payment": "46018000", "starting_balance": "68416596.87425641025641025641025641025645"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_03

- Safe amount: expected `873000`, current `0`, residual `-873000`.
- Earliest full payment: expected `2019-11-15`, current `2019-11-29`; deadline `2019-11-15`.
- Starting/minimum: `5810300` / `2668700`.
- First divergences: safe `wrong event classification`; earliest `wrong recurrence`.
- Root-cause cluster: **pending/lifecycle semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_254 2019-09-07 debit 95000 Pending pharmacy card charge [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 1.
- Recurrence evidence series: 9; protected categories `{'groceries', 'utilities', 'rent'}`; optional `{'shopping', 'cloud_storage', 'streaming'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2019-11-15", "debits": "0", "ending_balance": "1750058.447777777777777777777777777777777", "feasible_current_model": false, "minimum_required": "2668700", "reason": "current forecast minimum-floor failure", "requested_payment": "5491000", "starting_balance": "7241058.447777777777777777777777777777777"}
  - {"credits": "0", "date": "2019-11-29", "debits": "0", "ending_balance": "5487775.15888888888888888888888888888889", "feasible_current_model": true, "minimum_required": "2668700", "reason": "current forecast predicate", "requested_payment": "5491000", "starting_balance": "6613775.158888888888888888888888888888888"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_04

- Safe amount: expected `8401800`, current `0`, residual `-8401800`.
- Earliest full payment: expected `2024-06-15`, current `2024-06-13`; deadline `2024-06-19`.
- Starting/minimum: `52206950` / `30686600`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_357 2024-06-11 debit 1704300 Scheduled school fee [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'groceries', 'rent', 'transport'}`; optional `{'music_subscription', 'entertainment'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2024-06-13", "debits": "0", "ending_balance": "66792163.08638461538461538461538461538461", "feasible_current_model": true, "minimum_required": "30686600", "reason": "current forecast predicate", "requested_payment": "12693000", "starting_balance": "41295163.08638461538461538461538461538461"}
  - {"credits": "0", "date": "2024-06-15", "debits": "0", "ending_balance": "65292688.61100000000000000000000000000000", "feasible_current_model": true, "minimum_required": "30686600", "reason": "current forecast predicate", "requested_payment": "12693000", "starting_balance": "79485163.08638461538461538461538461538461"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_05

- Safe amount: expected `737`, current `15488`, residual `14751`.
- Earliest full payment: expected `empty`, current `empty`; deadline `2026-01-12`.
- Starting/minimum: `46475.1` / `13100`.
- First divergences: safe `wrong recurrence`; earliest `None`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 9; protected categories `{'family_support', 'groceries', 'healthcare', 'rent'}`; optional `{'shopping', 'cloud_storage'}`.
- Critical-date balance rows:
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_06

- Safe amount: expected `603.3`, current `385.62`, residual `-217.68`.
- Earliest full payment: expected `2026-01-15`, current `2026-01-03`; deadline `2026-01-14`.
- Starting/minimum: `1942.4` / `800`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 11; protected categories `{'insurance', 'rent', 'transport'}`; optional `{'streaming'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2026-01-03", "debits": "0", "ending_balance": "1295.024", "feasible_current_model": true, "minimum_required": "800", "reason": "current forecast predicate", "requested_payment": "620.4", "starting_balance": "1942.4"}
  - {"credits": "0", "date": "2026-01-15", "debits": "0", "ending_balance": "1963.884066666666666666666666666666666667", "feasible_current_model": true, "minimum_required": "800", "reason": "current forecast predicate", "requested_payment": "620.4", "starting_balance": "2584.284066666666666666666666666666666667"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_07

- Safe amount: expected `87170.56`, current `0`, residual `-87170.56`.
- Earliest full payment: expected `2024-10-23`, current `empty`; deadline `2024-11-14`.
- Starting/minimum: `218945.56` / `93000`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 8; protected categories `{'debt_repayment', 'utilities', 'rent'}`; optional `{'dining', 'music_subscription'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2024-10-23", "debits": "0", "ending_balance": "-96003.8555555555555555555555555555555554", "feasible_current_model": false, "minimum_required": "93000", "reason": "current forecast minimum-floor failure", "requested_payment": "197400", "starting_balance": "101396.1444444444444444444444444444444446"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_08

- Safe amount: expected `284.57`, current `0`, residual `-284.57`.
- Earliest full payment: expected `2025-04-15`, current `empty`; deadline `2025-04-15`.
- Starting/minimum: `1536.57` / `800`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'debt_repayment', 'education', 'groceries', 'rent'}`; optional `{'delivery_membership', 'dining', 'music_subscription'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2025-04-15", "debits": "0", "ending_balance": "-213.4399999999999999999999999999999999952", "feasible_current_model": false, "minimum_required": "800", "reason": "current forecast minimum-floor failure", "requested_payment": "996.6", "starting_balance": "59.63153846153846153846153846153846154328"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_09

- Safe amount: expected `166.61`, current `166.6`, residual `-0.01`.
- Earliest full payment: expected `2026-07-04`, current `2026-07-04`; deadline `2026-07-23`.
- Starting/minimum: `2231.1` / `600`.
- First divergences: safe `wrong recurrence`; earliest `None`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 9; protected categories `{'groceries', 'utilities', 'rent'}`; optional `set()`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2026-07-04", "debits": "0", "ending_balance": "2064.49", "feasible_current_model": true, "minimum_required": "600", "reason": "current forecast predicate", "requested_payment": "166.61", "starting_balance": "2231.1"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_10

- Safe amount: expected `12700`, current `266700`, residual `254000`.
- Earliest full payment: expected `empty`, current `2024-12-06`; deadline `2025-02-10`.
- Starting/minimum: `750155` / `225400`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'groceries', 'rent', 'transport'}`; optional `{'gym', 'music_subscription', 'entertainment', 'delivery_membership', 'dining'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2024-12-06", "debits": "0", "ending_balance": "477472.2096", "feasible_current_model": true, "minimum_required": "225400", "reason": "current forecast predicate", "requested_payment": "266700", "starting_balance": "750155"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_11

- Safe amount: expected `12510645`, current `6496199.46`, residual `-6014445.54`.
- Earliest full payment: expected `2025-07-15`, current `2025-05-03`; deadline `2025-06-12`.
- Starting/minimum: `63531795` / `34140600`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 11; protected categories `{'housing', 'utilities', 'education'}`; optional `{'cloud_storage', 'dining', 'entertainment'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2025-05-03", "debits": "0", "ending_balance": "58924683.2", "feasible_current_model": true, "minimum_required": "34140600", "reason": "current forecast predicate", "requested_payment": "13110000", "starting_balance": "63531795"}
  - {"credits": "0", "date": "2025-07-15", "debits": "0", "ending_balance": "64610889.02253846153846153846153846153842", "feasible_current_model": true, "minimum_required": "34140600", "reason": "current forecast predicate", "requested_payment": "13110000", "starting_balance": "77720889.02253846153846153846153846153842"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_13

- Safe amount: expected `433.4`, current `696.76`, residual `263.36`.
- Earliest full payment: expected `2024-05-15`, current `2024-03-07`; deadline `2024-05-15`.
- Starting/minimum: `2789.52` / `1300`.
- First divergences: safe `specification ambiguity`; earliest `wrong recurrence`.
- Root-cause cluster: **scheduled-credit boundary**.
- Explicit future credits:
  - event_1161 2024-03-15 credit 1343.54 Next confirmed salary [DIRECTLY OBSERVED]
- Explicit future debits:
  - none
- Scheduled credits: 1; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'groceries', 'rent', 'transport'}`; optional `{'gym', 'delivery_membership', 'music_subscription'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2024-03-07", "debits": "0", "ending_balance": "1847.92", "feasible_current_model": true, "minimum_required": "1300", "reason": "current forecast predicate", "requested_payment": "941.6", "starting_balance": "2789.52"}
  - {"credits": "0", "date": "2024-05-15", "debits": "0", "ending_balance": "2220.696923076923076923076923076923076920", "feasible_current_model": true, "minimum_required": "1300", "reason": "current forecast predicate", "requested_payment": "941.6", "starting_balance": "3207.121923076923076923076923076923076920"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_14

- Safe amount: expected `597.74`, current `1228.05`, residual `630.31`.
- Earliest full payment: expected `empty`, current `empty`; deadline `2025-10-04`.
- Starting/minimum: `3931.74` / `2200`.
- First divergences: safe `wrong recurrence`; earliest `None`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'family_support', 'groceries', 'healthcare', 'rent'}`; optional `{'shopping', 'cloud_storage'}`.
- Critical-date balance rows:
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_15

- Safe amount: expected `83.05`, current `363.64`, residual `280.59`.
- Earliest full payment: expected `empty`, current `empty`; deadline `2026-02-01`.
- Starting/minimum: `1770.05` / `1200`.
- First divergences: safe `wrong recurrence`; earliest `None`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 9; protected categories `{'debt_repayment', 'education', 'groceries', 'rent'}`; optional `{'dining'}`.
- Critical-date balance rows:
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_16

- Safe amount: expected `122500`, current `0`, residual `-122500`.
- Earliest full payment: expected `2023-08-12`, current `2023-08-12`; deadline `2023-10-11`.
- Starting/minimum: `362370` / `122400`.
- First divergences: safe `None`; earliest `None`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_1442 2023-08-16 debit 100000 Outstanding rent balance [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'groceries', 'rent', 'transport'}`; optional `set()`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2023-08-12", "debits": "0", "ending_balance": "239870", "feasible_current_model": true, "minimum_required": "122400", "reason": "current forecast predicate", "requested_payment": "122500", "starting_balance": "362370"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_17

- Safe amount: expected `243849.58`, current `274600`, residual `30750.42`.
- Earliest full payment: expected `2026-03-15`, current `2026-04-15`; deadline `2026-05-04`.
- Starting/minimum: `550379.58` / `166100`.
- First divergences: safe `specification ambiguity`; earliest `wrong recurrence`.
- Root-cause cluster: **scheduled-credit boundary**.
- Explicit future credits:
  - event_1546 2026-03-15 credit 206000 Next confirmed salary [DIRECTLY OBSERVED]
- Explicit future debits:
  - none
- Scheduled credits: 1; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'debt_repayment', 'education', 'groceries', 'rent'}`; optional `{'delivery_membership', 'dining', 'music_subscription'}`.
- Critical-date balance rows:
  - {"credits": "206000", "date": "2026-03-15", "debits": "0", "ending_balance": "340833.2175213675213675213675213675213675", "feasible_current_model": false, "minimum_required": "166100", "reason": "current forecast minimum-floor failure", "requested_payment": "274600", "starting_balance": "409433.2175213675213675213675213675213675"}
  - {"credits": "0", "date": "2026-04-15", "debits": "0", "ending_balance": "367267.6425641025641025641025641025641025", "feasible_current_model": true, "minimum_required": "166100", "reason": "current forecast predicate", "requested_payment": "274600", "starting_balance": "435867.6425641025641025641025641025641025"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_18

- Safe amount: expected `462`, current `58.71`, residual `-403.29`.
- Earliest full payment: expected `2026-09-15`, current `2026-09-13`; deadline `2026-09-15`.
- Starting/minimum: `2486` / `1400`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 9; protected categories `{'utilities', 'housing', 'healthcare'}`; optional `{'dining', 'streaming'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2026-09-13", "debits": "0", "ending_balance": "3337.991606837606837606837606837606837608", "feasible_current_model": true, "minimum_required": "1400", "reason": "current forecast predicate", "requested_payment": "3246.1", "starting_balance": "4274.091606837606837606837606837606837608"}
  - {"credits": "0", "date": "2026-09-15", "debits": "0", "ending_balance": "3337.991606837606837606837606837606837608", "feasible_current_model": true, "minimum_required": "1400", "reason": "current forecast predicate", "requested_payment": "3246.1", "starting_balance": "6584.091606837606837606837606837606837608"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_19

- Safe amount: expected `28820`, current `0`, residual `-28820`.
- Earliest full payment: expected `2024-09-15`, current `2024-09-04`; deadline `2024-10-04`.
- Starting/minimum: `199545` / `92800`.
- First divergences: safe `wrong recurrence`; earliest `wrong recurrence`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - none
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 10; protected categories `{'family_support', 'groceries', 'healthcare', 'rent'}`; optional `{'shopping', 'cloud_storage'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2024-09-04", "debits": "0", "ending_balance": "159885", "feasible_current_model": true, "minimum_required": "92800", "reason": "current forecast predicate", "requested_payment": "39660", "starting_balance": "199545"}
  - {"credits": "0", "date": "2024-09-15", "debits": "0", "ending_balance": "237439.2168461538461538461538461538461538", "feasible_current_model": true, "minimum_required": "92800", "reason": "current forecast predicate", "requested_payment": "39660", "starting_balance": "277099.2168461538461538461538461538461538"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_20

- Safe amount: expected `5400`, current `0`, residual `-5400`.
- Earliest full payment: expected `empty`, current `empty`; deadline `2026-02-22`.
- Starting/minimum: `102609.05` / `64500`.
- First divergences: safe `wrong event classification`; earliest `None`.
- Root-cause cluster: **pending/lifecycle semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_1786 2026-02-09 debit 704.05 Outstanding telecom bill [DIRECTLY OBSERVED]; event_1787 2026-02-08 debit 4470 Pending online order charge [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 3.
- Recurrence evidence series: 11; protected categories `{'housing', 'utilities', 'education'}`; optional `{'cloud_storage', 'dining', 'entertainment'}`.
- Critical-date balance rows:
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_21

- Safe amount: expected `1543.35`, current `1574.4`, residual `31.05`.
- Earliest full payment: expected `2026-04-15`, current `2026-04-03`; deadline `2026-04-14`.
- Starting/minimum: `3911.35` / `1800`.
- First divergences: safe `wrong event classification`; earliest `wrong recurrence`.
- Root-cause cluster: **pending/lifecycle semantics**.
- Explicit future credits:
  - event_1858 2026-04-15 credit 2256 Next confirmed salary [DIRECTLY OBSERVED]
- Explicit future debits:
  - event_1857 2026-04-05 debit 53 Pending fuel authorization [DIRECTLY OBSERVED]
- Scheduled credits: 1; pending events: 1.
- Recurrence evidence series: 9; protected categories `{'groceries', 'utilities', 'rent'}`; optional `{'shopping', 'cloud_storage', 'dining', 'streaming'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2026-04-03", "debits": "0", "ending_balance": "2336.95", "feasible_current_model": true, "minimum_required": "1800", "reason": "current forecast predicate", "requested_payment": "1574.4", "starting_balance": "3911.35"}
  - {"credits": "2256", "date": "2026-04-15", "debits": "0", "ending_balance": "4151.827666666666666666666666666666666667", "feasible_current_model": true, "minimum_required": "1800", "reason": "current forecast predicate", "requested_payment": "1574.4", "starting_balance": "3470.227666666666666666666666666666666667"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_22

- Safe amount: expected `475.46`, current `179.04`, residual `-296.42`.
- Earliest full payment: expected `2025-01-15`, current `2025-01-16`; deadline `2025-02-10`.
- Starting/minimum: `1132.46` / `500`.
- First divergences: safe `wrong event classification`; earliest `wrong recurrence`.
- Root-cause cluster: **pending/lifecycle semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_1961 2024-12-08 debit 43 Pending merchant debit [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 1.
- Recurrence evidence series: 10; protected categories `{'groceries', 'rent', 'transport'}`; optional `{'gym', 'music_subscription'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2025-01-15", "debits": "0", "ending_balance": "393.477200000000000000000000000000000000", "feasible_current_model": false, "minimum_required": "500", "reason": "current forecast minimum-floor failure", "requested_payment": "731.5", "starting_balance": "1153.931046153846153846153846153846153846"}
  - {"credits": "0", "date": "2025-01-16", "debits": "0", "ending_balance": "975.478400000000000000000000000000000000", "feasible_current_model": true, "minimum_required": "500", "reason": "current forecast predicate", "requested_payment": "731.5", "starting_balance": "1124.977200000000000000000000000000000000"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_23

- Safe amount: expected `9152`, current `0`, residual `-9152`.
- Earliest full payment: expected `2025-07-15`, current `2025-07-17`; deadline `2025-07-15`.
- Starting/minimum: `51957.9` / `27000`.
- First divergences: safe `wrong event classification`; earliest `wrong recurrence`.
- Root-cause cluster: **pending/lifecycle semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_2042 2025-05-11 debit 1553.2 Pending pharmacy card charge [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 1.
- Recurrence evidence series: 10; protected categories `{'family_support', 'groceries', 'healthcare', 'rent'}`; optional `{'shopping', 'cloud_storage'}`.
- Critical-date balance rows:
  - {"credits": "0", "date": "2025-07-15", "debits": "0", "ending_balance": "11370.66174358974358974358974358974358976", "feasible_current_model": false, "minimum_required": "27000", "reason": "current forecast minimum-floor failure", "requested_payment": "38016", "starting_balance": "55238.66174358974358974358974358974358976"}
  - {"credits": "0", "date": "2025-07-17", "debits": "0", "ending_balance": "49516.35174358974358974358974358974358976", "feasible_current_model": true, "minimum_required": "27000", "reason": "current forecast predicate", "requested_payment": "38016", "starting_balance": "46042.55174358974358974358974358974358976"}
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_24

- Safe amount: expected `13420`, current `0`, residual `-13420`.
- Earliest full payment: expected `empty`, current `empty`; deadline `2026-02-08`.
- Starting/minimum: `85045` / `51000`.
- First divergences: safe `wrong recurrence`; earliest `None`.
- Root-cause cluster: **recurrence/amount semantics**.
- Explicit future credits:
  - none
- Explicit future debits:
  - event_2166 2026-01-11 debit 1830 Scheduled insurance payment [DIRECTLY OBSERVED]
- Scheduled credits: 0; pending events: 0.
- Recurrence evidence series: 11; protected categories `{'insurance', 'rent', 'transport'}`; optional `{'cloud_storage', 'dining', 'streaming'}`.
- Critical-date balance rows:
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

### request_25

- Safe amount: expected `1425000`, current `5877496.33`, residual `4452496.33`.
- Earliest full payment: expected `empty`, current `empty`; deadline `2024-04-17`.
- Starting/minimum: `32063050` / `23379100`.
- First divergences: safe `specification ambiguity`; earliest `None`.
- Root-cause cluster: **scheduled-credit boundary**.
- Explicit future credits:
  - event_2288 2024-03-15 credit 28499994.00 Next confirmed salary [DIRECTLY OBSERVED]
- Explicit future debits:
  - none
- Scheduled credits: 1; pending events: 0.
- Recurrence evidence series: 11; protected categories `{'insurance', 'rent', 'transport'}`; optional `set()`.
- Critical-date balance rows:
- Implied cash-flow conclusion: explicit evidence establishes the listed movements only. The residual is **UNKNOWN** unless a matching supplied event/confirmation is identified; no arithmetic statistic is selected here.

## FORECAST_CONTRACT_TABLE

| Example | Expected safe amount | Expected earliest date | Required future movements | Excluded future movements | Recurring evidence | Income evidence | Pending behavior | First divergence | Root cause | Confidence |
|---|---:|---|---|---|---:|---|---|---|---|---|
| request_02 | 17229139.2 | 2025-09-15 | event_185@2025-08-08:1651100 | event_185 | 11 | none | reserved debit / excluded credit per status | wrong event classification | pending/lifecycle semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_03 | 873000 | 2019-11-15 | event_254@2019-09-07:95000 | event_254 | 9 | none | reserved debit / excluded credit per status | wrong event classification | pending/lifecycle semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_04 | 8401800 | 2024-06-15 | event_357@2024-06-11:1704300 | none observed | 10 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_05 | 737 | empty | none explicitly dated | none observed | 9 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_06 | 603.3 | 2026-01-15 | none explicitly dated | none observed | 11 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_07 | 87170.56 | 2024-10-23 | none explicitly dated | none observed | 8 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_08 | 284.57 | 2025-04-15 | none explicitly dated | none observed | 10 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_09 | 166.61 | 2026-07-04 | none explicitly dated | none observed | 9 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_10 | 12700 | empty | none explicitly dated | none observed | 10 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_11 | 12510645 | 2025-07-15 | none explicitly dated | none observed | 11 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_13 | 433.4 | 2024-05-15 | event_1161@2024-03-15:1343.54 | none observed | 10 | event_1161 | none observed | specification ambiguity | scheduled-credit boundary | high for explicit movements; low/medium for any inferred missing movement |
| request_14 | 597.74 | empty | none explicitly dated | none observed | 10 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_15 | 83.05 | empty | none explicitly dated | none observed | 9 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_16 | 122500 | 2023-08-12 | event_1442@2023-08-16:100000 | none observed | 10 | none | none observed | unknown | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_17 | 243849.58 | 2026-03-15 | event_1546@2026-03-15:206000 | none observed | 10 | event_1546 | none observed | specification ambiguity | scheduled-credit boundary | high for explicit movements; low/medium for any inferred missing movement |
| request_18 | 462 | 2026-09-15 | none explicitly dated | none observed | 9 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_19 | 28820 | 2024-09-15 | none explicitly dated | none observed | 10 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_20 | 5400 | empty | event_1786@2026-02-09:704.05; event_1787@2026-02-08:4470 | event_1785; event_1786; event_1787 | 11 | none | reserved debit / excluded credit per status | wrong event classification | pending/lifecycle semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_21 | 1543.35 | 2026-04-15 | event_1858@2026-04-15:2256; event_1857@2026-04-05:53 | event_1857 | 9 | event_1858 | reserved debit / excluded credit per status | wrong event classification | pending/lifecycle semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_22 | 475.46 | 2025-01-15 | event_1961@2024-12-08:43 | event_1961 | 10 | none | reserved debit / excluded credit per status | wrong event classification | pending/lifecycle semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_23 | 9152 | 2025-07-15 | event_2042@2025-05-11:1553.2 | event_2042 | 10 | none | reserved debit / excluded credit per status | wrong event classification | pending/lifecycle semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_24 | 13420 | empty | event_2166@2026-01-11:1830 | none observed | 11 | none | none observed | wrong recurrence | recurrence/amount semantics | high for explicit movements; low/medium for any inferred missing movement |
| request_25 | 1425000 | empty | event_2288@2024-03-15:28499994.00 | none observed | 11 | event_2288 | none observed | specification ambiguity | scheduled-credit boundary | high for explicit movements; low/medium for any inferred missing movement |

## Recurring-looking series inventory

Every repeated source-description series for the 25 sample users is listed below. This is an inventory of evidence, not a declaration that every series must recur. Category-only grouping is not treated as authoritative.

| User | Category | Description | Direction | Currency | Event IDs | Dates | Amounts | Gaps (days) | Flexibility | Statuses |
|---|---|---|---|---|---|---|---|---|---|---|
| user_01 | debt_repayment | Education loan instalment | debit | ZAR | ['event_04', 'event_10', 'event_16', 'event_22', 'event_29'] | ['2023-10-11', '2023-11-11', '2023-12-11', '2024-01-11', '2024-02-11'] | ['3487', '3487', '3487', '3487', '3487'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | delivery_membership | Delivery service plan | debit | ZAR | ['event_06', 'event_12', 'event_18', 'event_24', 'event_31'] | ['2023-10-13', '2023-11-13', '2023-12-13', '2024-01-13', '2024-02-13'] | ['306.9', '306.9', '306.9', '306.9', '306.9'] | [31, 30, 31, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | dining | Bakery and snacks | debit | ZAR | ['event_85', 'event_86', 'event_95', 'event_96'] | ['2023-09-10', '2023-09-24', '2024-01-28', '2024-02-11'] | ['1213.78', '1243.56', '1222.49', '1016.12'] | [14, 126, 14] | ['reducible'] | ['settled', 'settled', 'settled', 'settled'] |
| user_01 | dining | Coffee shop | debit | ZAR | ['event_92', 'event_94'] | ['2023-12-17', '2024-01-14'] | ['972.88', '1017.11'] | [28] | ['reducible'] | ['settled', 'settled'] |
| user_01 | dining | Quick-service meal | debit | ZAR | ['event_89', 'event_91'] | ['2023-11-05', '2023-12-03'] | ['1070.17', '1160.42'] | [28] | ['reducible'] | ['settled', 'settled'] |
| user_01 | education | Professional training fee | debit | ZAR | ['event_03', 'event_09', 'event_15', 'event_21', 'event_28'] | ['2023-10-08', '2023-11-08', '2023-12-08', '2024-01-08', '2024-02-08'] | ['1821.6', '1821.6', '1821.6', '1821.6', '1821.6'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | groceries | Bulk pantry shop | debit | ZAR | ['event_35', 'event_38', 'event_46'] | ['2023-09-22', '2023-10-13', '2023-12-08'] | ['707.36', '915.12', '602.87'] | [21, 56] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_01 | groceries | Fresh food shop | debit | ZAR | ['event_39', 'event_40', 'event_48', 'event_49'] | ['2023-10-20', '2023-10-27', '2023-12-22', '2023-12-29'] | ['644.3', '663.27', '651.12', '899.04'] | [7, 56, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_01 | groceries | Grocery delivery | debit | ZAR | ['event_36', 'event_41', 'event_57'] | ['2023-09-29', '2023-11-03', '2024-02-23'] | ['629.96', '1030.1', '626.01'] | [35, 112] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_01 | groceries | Household groceries | debit | ZAR | ['event_45', 'event_52', 'event_54'] | ['2023-12-01', '2024-01-19', '2024-02-02'] | ['882.48', '756.39', '719.51'] | [49, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_01 | groceries | Local market purchase | debit | ZAR | ['event_37', 'event_43', 'event_44', 'event_47', 'event_58'] | ['2023-10-06', '2023-11-17', '2023-11-24', '2023-12-15', '2024-03-01'] | ['873.17', '803.55', '644.43', '765.64', '964.05'] | [42, 7, 21, 77] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | groceries | Neighbourhood grocer | debit | ZAR | ['event_33', 'event_34', 'event_42', 'event_50', 'event_55'] | ['2023-09-08', '2023-09-15', '2023-11-10', '2024-01-05', '2024-02-09'] | ['925.62', '939.13', '672.37', '961.46', '755.11'] | [7, 56, 56, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | groceries | Supermarket basket | debit | ZAR | ['event_51', 'event_53', 'event_56'] | ['2024-01-12', '2024-01-26', '2024-02-16'] | ['875.35', '624.94', '881.22'] | [14, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_01 | music_subscription | Music service subscription | debit | ZAR | ['event_05', 'event_11', 'event_17', 'event_23', 'event_30'] | ['2023-10-11', '2023-11-11', '2023-12-11', '2024-01-11', '2024-02-11'] | ['235.4', '235.4', '235.4', '235.4', '235.4'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | rent | Apartment rent transfer | debit | ZAR | ['event_01', 'event_07', 'event_13', 'event_19', 'event_26', 'event_32'] | ['2023-10-02', '2023-11-02', '2023-12-02', '2024-01-02', '2024-02-02', '2024-03-02'] | ['5148', '5148', '5148', '5148', '5148', '5148'] | [31, 30, 31, 31, 29] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | transport | Commuter pass | debit | ZAR | ['event_59', 'event_69', 'event_75', 'event_79', 'event_83'] | ['2023-09-09', '2023-11-18', '2023-12-30', '2024-01-27', '2024-02-24'] | ['399.02', '518.04', '374.6', '560.21', '549.05'] | [70, 42, 28, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | transport | Fuel refill | debit | ZAR | ['event_64', 'event_77'] | ['2023-10-14', '2024-01-13'] | ['503.02', '434.69'] | [91] | ['fixed'] | ['settled', 'settled'] |
| user_01 | transport | Local taxi | debit | ZAR | ['event_65', 'event_74', 'event_84'] | ['2023-10-21', '2023-12-23', '2024-03-02'] | ['351.49', '411.07', '339.29'] | [63, 70] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_01 | transport | Metro and bus fares | debit | ZAR | ['event_61', 'event_63', 'event_66', 'event_68', 'event_80'] | ['2023-09-23', '2023-10-07', '2023-10-28', '2023-11-11', '2024-02-03'] | ['468.47', '373.05', '553.74', '347.86', '406.54'] | [14, 21, 14, 84] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | transport | Parking and tolls | debit | ZAR | ['event_71', 'event_81'] | ['2023-12-02', '2024-02-10'] | ['323.58', '488.36'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_01 | transport | Rail pass | debit | ZAR | ['event_67', 'event_78'] | ['2023-11-04', '2024-01-20'] | ['421.89', '375.73'] | [77] | ['fixed'] | ['settled', 'settled'] |
| user_01 | transport | Ride-hailing trip | debit | ZAR | ['event_60', 'event_62', 'event_70', 'event_76', 'event_82'] | ['2023-09-16', '2023-09-30', '2023-11-25', '2024-01-06', '2024-02-17'] | ['549.8', '428.92', '444.56', '358.85', '424.56'] | [14, 56, 42, 42] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_01 | transport | Vehicle charging | debit | ZAR | ['event_72', 'event_73'] | ['2023-12-09', '2023-12-16'] | ['478.16', '534.56'] | [7] | ['fixed'] | ['settled', 'settled'] |
| user_01 | utilities | Household utility payment | debit | ZAR | ['event_02', 'event_08', 'event_14', 'event_20', 'event_27'] | ['2023-10-06', '2023-11-06', '2023-12-06', '2024-01-06', '2024-02-06'] | ['1475.46', '1483.81', '1541.75', '1651.81', '1386.17'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | cloud_storage | Shared storage plan | debit | IDR | ['event_111', 'event_119', 'event_127', 'event_135', 'event_143'] | ['2025-03-13', '2025-04-13', '2025-05-13', '2025-06-13', '2025-07-13'] | ['369550', '369550', '369550', '369550', '369550'] | [31, 30, 31, 30] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | dining | Bakery and snacks | debit | IDR | ['event_176', 'event_182', 'event_184'] | ['2025-02-12', '2025-06-18', '2025-07-30'] | ['1166644.88', '947892.35', '1204805.34'] | [126, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_02 | education | Course tuition | debit | IDR | ['event_108', 'event_116', 'event_124', 'event_132', 'event_140'] | ['2025-03-09', '2025-04-09', '2025-05-09', '2025-06-09', '2025-07-09'] | ['3040000', '3040000', '3040000', '3040000', '3040000'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | entertainment | Cinema and events | debit | IDR | ['event_110', 'event_118', 'event_126', 'event_134', 'event_142'] | ['2025-03-15', '2025-04-15', '2025-05-15', '2025-06-15', '2025-07-15'] | ['1289187.4', '1367779.89', '1287628.28', '1193699.1', '1352563.79'] | [31, 30, 31, 30] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | groceries | Bulk pantry shop | debit | IDR | ['event_146', 'event_151'] | ['2025-02-20', '2025-04-11'] | ['1667911.86', '1664708.05'] | [50] | ['fixed'] | ['settled', 'settled'] |
| user_02 | groceries | Grocery delivery | debit | IDR | ['event_145', 'event_158'] | ['2025-02-10', '2025-06-20'] | ['2477697.53', '2222527.88'] | [130] | ['fixed'] | ['settled', 'settled'] |
| user_02 | groceries | Household groceries | debit | IDR | ['event_149', 'event_150', 'event_152', 'event_159'] | ['2025-03-22', '2025-04-01', '2025-04-21', '2025-06-30'] | ['1920485.7', '1630631.42', '1478895.05', '2079368.25'] | [10, 20, 70] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_02 | groceries | Local market purchase | debit | IDR | ['event_153', 'event_156', 'event_160'] | ['2025-05-01', '2025-05-31', '2025-07-10'] | ['2192475.45', '1611886.08', '2218141.61'] | [30, 40] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_02 | groceries | Neighbourhood grocer | debit | IDR | ['event_148', 'event_155', 'event_157'] | ['2025-03-12', '2025-05-21', '2025-06-10'] | ['1455258.76', '2030400.43', '2158165.32'] | [70, 20] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_02 | groceries | Supermarket basket | debit | IDR | ['event_154', 'event_162'] | ['2025-05-11', '2025-07-30'] | ['1852958.27', '1913686.86'] | [80] | ['fixed'] | ['settled', 'settled'] |
| user_02 | healthcare | Clinic payment | debit | IDR | ['event_109', 'event_117', 'event_125', 'event_133', 'event_141'] | ['2025-03-11', '2025-04-11', '2025-05-11', '2025-06-11', '2025-07-11'] | ['1594883.08', '1467514.81', '1452405.16', '1641668.72', '1538498.1'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | housing | Home repair reserve | debit | IDR | ['event_105', 'event_113', 'event_121', 'event_129', 'event_137', 'event_144'] | ['2025-03-04', '2025-04-04', '2025-05-04', '2025-06-04', '2025-07-04', '2025-08-04'] | ['3534000', '3534000', '3534000', '3534000', '3534000', '3534000'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | insurance | Household insurance | debit | IDR | ['event_107', 'event_115', 'event_123', 'event_131', 'event_139'] | ['2025-03-08', '2025-04-08', '2025-05-08', '2025-06-08', '2025-07-08'] | ['1132400', '1132400', '1132400', '1132400', '1132400'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | salary | Payroll credit | credit | IDR | ['event_104', 'event_112', 'event_120', 'event_128', 'event_136'] | ['2025-03-15', '2025-04-15', '2025-05-15', '2025-06-15', '2025-07-15'] | ['33345000', '33345000', '33345000', '33345000', '33345000'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_02 | transport | Commuter pass | debit | IDR | ['event_170', 'event_171', 'event_172', 'event_174'] | ['2025-05-20', '2025-06-03', '2025-06-17', '2025-07-15'] | ['1374936.26', '1329347.44', '1309608.46', '1327886.54'] | [14, 14, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_02 | transport | Metro and bus fares | debit | IDR | ['event_165', 'event_175'] | ['2025-03-11', '2025-07-29'] | ['1062246.98', '1062310.27'] | [140] | ['fixed'] | ['settled', 'settled'] |
| user_02 | transport | Rail pass | debit | IDR | ['event_164', 'event_173'] | ['2025-02-25', '2025-07-01'] | ['995704.83', '1111352.32'] | [126] | ['fixed'] | ['settled', 'settled'] |
| user_02 | transport | Ride-hailing trip | debit | IDR | ['event_166', 'event_167', 'event_168'] | ['2025-03-25', '2025-04-08', '2025-04-22'] | ['1053078.61', '1294200.86', '1440242.94'] | [14, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_02 | utilities | Municipal utilities | debit | IDR | ['event_106', 'event_114', 'event_122', 'event_130', 'event_138'] | ['2025-03-07', '2025-04-07', '2025-05-07', '2025-06-07', '2025-07-07'] | ['2143659.02', '2081730.85', '1830311.06', '1981601.61', '2141849.94'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_03 | cloud_storage | Shared storage plan | debit | IDR | ['event_189', 'event_195', 'event_201', 'event_207', 'event_214'] | ['2019-04-14', '2019-05-14', '2019-06-14', '2019-07-14', '2019-08-14'] | ['20900', '20900', '20900', '20900', '20900'] | [30, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_03 | dining | Bakery and snacks | debit | IDR | ['event_244', 'event_245'] | ['2019-03-09', '2019-03-30'] | ['117456.78', '141412.46'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_03 | dining | Coffee shop | debit | IDR | ['event_247', 'event_252'] | ['2019-05-11', '2019-08-24'] | ['132247.64', '135718.35'] | [105] | ['fixed'] | ['settled', 'settled'] |
| user_03 | dining | Lunch with colleagues | debit | IDR | ['event_248', 'event_251'] | ['2019-06-01', '2019-08-03'] | ['158476.5', '171191.99'] | [63] | ['fixed'] | ['settled', 'settled'] |
| user_03 | dining | Quick-service meal | debit | IDR | ['event_246', 'event_250'] | ['2019-04-20', '2019-07-13'] | ['146236.28', '171303.21'] | [84] | ['fixed'] | ['settled', 'settled'] |
| user_03 | groceries | Bulk pantry shop | debit | IDR | ['event_217', 'event_218', 'event_219'] | ['2019-03-12', '2019-03-22', '2019-04-01'] | ['159576.52', '234390.87', '230312.98'] | [10, 10] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_03 | groceries | Grocery delivery | debit | IDR | ['event_225', 'event_227'] | ['2019-05-31', '2019-06-20'] | ['188355.72', '171495.67'] | [20] | ['fixed'] | ['settled', 'settled'] |
| user_03 | groceries | Household groceries | debit | IDR | ['event_224', 'event_226'] | ['2019-05-21', '2019-06-10'] | ['155851.46', '166710.61'] | [20] | ['fixed'] | ['settled', 'settled'] |
| user_03 | groceries | Local market purchase | debit | IDR | ['event_230', 'event_233'] | ['2019-07-20', '2019-08-19'] | ['173004.74', '240706.45'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_03 | groceries | Neighbourhood grocer | debit | IDR | ['event_221', 'event_234'] | ['2019-04-21', '2019-08-29'] | ['209875.85', '200238.72'] | [130] | ['fixed'] | ['settled', 'settled'] |
| user_03 | groceries | Supermarket basket | debit | IDR | ['event_220', 'event_228', 'event_229', 'event_231'] | ['2019-04-11', '2019-06-30', '2019-07-10', '2019-07-30'] | ['234602.65', '145691.38', '171259.18', '214266.98'] | [80, 10, 20] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_03 | groceries | Weekly produce market | debit | IDR | ['event_222', 'event_223', 'event_232'] | ['2019-05-01', '2019-05-11', '2019-08-09'] | ['178469.49', '180577.99', '221578.88'] | [10, 90] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_03 | rent | Landlord standing order | debit | IDR | ['event_187', 'event_193', 'event_199', 'event_205', 'event_212'] | ['2019-04-04', '2019-05-04', '2019-06-04', '2019-07-04', '2019-08-04'] | ['1140000', '1140000', '1140000', '1140000', '1140000'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_03 | salary | Payroll credit | credit | IDR | ['event_186', 'event_192', 'event_198', 'event_204', 'event_210'] | ['2019-04-15', '2019-05-15', '2019-06-15', '2019-07-15', '2019-08-15'] | ['4365000', '4365000', '4365000', '4365000', '4365000'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_03 | shopping | Clothing and household items | debit | IDR | ['event_191', 'event_197', 'event_203', 'event_209', 'event_216'] | ['2019-04-14', '2019-05-14', '2019-06-14', '2019-07-14', '2019-08-14'] | ['151493.37', '184274.02', '153395.26', '173930.81', '180395.29'] | [30, 31, 30, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_03 | streaming | Video streaming plan | debit | IDR | ['event_190', 'event_196', 'event_202', 'event_208', 'event_215'] | ['2019-04-11', '2019-05-11', '2019-06-11', '2019-07-11', '2019-08-11'] | ['117800', '117800', '117800', '117800', '117800'] | [30, 31, 30, 31] | ['reducible_or_stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_03 | transport | Metro and bus fares | debit | IDR | ['event_241', 'event_242'] | ['2019-07-17', '2019-08-07'] | ['83523.33', '99961.13'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_03 | transport | Parking and tolls | debit | IDR | ['event_235', 'event_236', 'event_239'] | ['2019-03-13', '2019-04-03', '2019-06-05'] | ['81510.25', '116319.21', '106806.88'] | [21, 63] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_03 | utilities | Water and power payment | debit | IDR | ['event_188', 'event_194', 'event_200', 'event_206', 'event_213'] | ['2019-04-08', '2019-05-08', '2019-06-08', '2019-07-08', '2019-08-08'] | ['295330.29', '290684.15', '270537.63', '303042.45', '262344.55'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | delivery_membership | Food delivery membership | debit | IDR | ['event_259', 'event_266', 'event_274', 'event_281', 'event_288'] | ['2024-01-12', '2024-02-12', '2024-03-12', '2024-04-12', '2024-05-12'] | ['377150', '377150', '377150', '377150', '377150'] | [31, 29, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | dining | Bakery and snacks | debit | IDR | ['event_353', 'event_355'] | ['2024-04-15', '2024-05-13'] | ['1259307.64', '1886856.1'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_04 | dining | Family dinner | debit | IDR | ['event_349', 'event_351', 'event_354'] | ['2024-02-19', '2024-03-18', '2024-04-29'] | ['1931412.81', '2102251.18', '1661337.11'] | [28, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | dining | Neighbourhood restaurant | debit | IDR | ['event_344', 'event_345', 'event_352'] | ['2023-12-11', '2023-12-25', '2024-04-01'] | ['2111827.25', '1839656.04', '1282286.6'] | [14, 98] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | dining | Takeaway order | debit | IDR | ['event_346', 'event_347'] | ['2024-01-08', '2024-01-22'] | ['1279029.86', '2067659.14'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_04 | entertainment | Local event tickets | debit | IDR | ['event_261', 'event_268', 'event_276', 'event_283', 'event_290'] | ['2024-01-13', '2024-02-13', '2024-03-13', '2024-04-13', '2024-05-13'] | ['1484369.68', '1375854.05', '1542620', '1291303.65', '1231859.39'] | [31, 29, 31, 30] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | groceries | Bulk pantry shop | debit | IDR | ['event_294', 'event_311', 'event_317'] | ['2023-12-23', '2024-04-20', '2024-06-01'] | ['1383275.31', '1617937.79', '1433695.5'] | [119, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | groceries | Fresh food shop | debit | IDR | ['event_293', 'event_310', 'event_314'] | ['2023-12-16', '2024-04-13', '2024-05-11'] | ['1749986.6', '1184189.4', '1698278.31'] | [119, 28] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | groceries | Grocery delivery | debit | IDR | ['event_308', 'event_309', 'event_315'] | ['2024-03-30', '2024-04-06', '2024-05-18'] | ['1261462.72', '1825667.28', '1075064.04'] | [7, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | groceries | Local market purchase | debit | IDR | ['event_292', 'event_297', 'event_302', 'event_303', 'event_305', 'event_316'] | ['2023-12-09', '2024-01-13', '2024-02-17', '2024-02-24', '2024-03-09', '2024-05-25'] | ['1685953.79', '1413898.4', '1753801.95', '1203621.92', '1347842.61', '1809752.54'] | [35, 35, 7, 14, 77] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | groceries | Neighbourhood grocer | debit | IDR | ['event_295', 'event_300', 'event_304', 'event_312', 'event_313'] | ['2023-12-30', '2024-02-03', '2024-03-02', '2024-04-27', '2024-05-04'] | ['1482897.31', '1697006.55', '1674003.66', '1519414.73', '1831437.58'] | [35, 28, 56, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | groceries | Supermarket basket | debit | IDR | ['event_306', 'event_307'] | ['2024-03-16', '2024-03-23'] | ['1453711.32', '1447770.09'] | [7] | ['fixed'] | ['settled', 'settled'] |
| user_04 | groceries | Weekly produce market | debit | IDR | ['event_296', 'event_299', 'event_301'] | ['2024-01-06', '2024-01-27', '2024-02-10'] | ['1818044.76', '1178544.55', '1087788.82'] | [21, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | gym | Gym membership | debit | IDR | ['event_260', 'event_267', 'event_275', 'event_282', 'event_289'] | ['2024-01-09', '2024-02-09', '2024-03-09', '2024-04-09', '2024-05-09'] | ['1027900', '1027900', '1027900', '1027900', '1027900'] | [31, 29, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | music_subscription | Music service subscription | debit | IDR | ['event_258', 'event_265', 'event_273', 'event_280', 'event_287'] | ['2024-01-10', '2024-02-10', '2024-03-10', '2024-04-10', '2024-05-10'] | ['332500', '332500', '332500', '332500', '332500'] | [31, 29, 31, 30] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | rent | Residential rent payment | debit | IDR | ['event_256', 'event_263', 'event_271', 'event_278', 'event_285', 'event_291'] | ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01'] | ['12293000', '12293000', '12293000', '12293000', '12293000', '12293000'] | [31, 29, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | salary | Payroll credit | credit | IDR | ['event_255', 'event_262', 'event_269', 'event_277', 'event_284'] | ['2024-01-15', '2024-02-15', '2024-03-15', '2024-04-15', '2024-05-15'] | ['38190000', '38190000', '38190000', '38190000', '38190000'] | [31, 29, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | transport | Fuel refill | debit | IDR | ['event_318', 'event_323', 'event_324', 'event_328', 'event_329'] | ['2023-12-10', '2024-01-14', '2024-01-21', '2024-02-18', '2024-02-25'] | ['649231.24', '820888.17', '870102.58', '954666.65', '843406.32'] | [35, 7, 28, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | transport | Local taxi | debit | IDR | ['event_319', 'event_320', 'event_334'] | ['2023-12-17', '2023-12-24', '2024-03-31'] | ['876705.51', '825832.49', '842011.07'] | [7, 98] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | transport | Metro and bus fares | debit | IDR | ['event_325', 'event_327', 'event_332'] | ['2024-01-28', '2024-02-11', '2024-03-17'] | ['1011616.29', '595968.94', '677221.86'] | [14, 35] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_04 | transport | Parking and tolls | debit | IDR | ['event_322', 'event_326', 'event_333', 'event_337', 'event_342'] | ['2024-01-07', '2024-02-04', '2024-03-24', '2024-04-21', '2024-05-26'] | ['841811.01', '596927.82', '889762.96', '874634.88', '602450.01'] | [28, 49, 28, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | transport | Rail pass | debit | IDR | ['event_335', 'event_343'] | ['2024-04-07', '2024-06-02'] | ['1000668.29', '1016425.58'] | [56] | ['fixed'] | ['settled', 'settled'] |
| user_04 | transport | Ride-hailing trip | debit | IDR | ['event_321', 'event_330', 'event_338', 'event_339', 'event_340', 'event_341'] | ['2023-12-31', '2024-03-03', '2024-04-28', '2024-05-05', '2024-05-12', '2024-05-19'] | ['769694.2', '589707.32', '766019.04', '1030376.9', '912938.95', '853091.62'] | [63, 56, 7, 7, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_04 | transport | Vehicle charging | debit | IDR | ['event_331', 'event_336'] | ['2024-03-10', '2024-04-14'] | ['997182.25', '935850.82'] | [35] | ['fixed'] | ['settled', 'settled'] |
| user_04 | utilities | Municipal utilities | debit | IDR | ['event_257', 'event_264', 'event_272', 'event_279', 'event_286'] | ['2024-01-05', '2024-02-05', '2024-03-05', '2024-04-05', '2024-05-05'] | ['2017103.37', '1981052.47', '2033868.83', '1980834.82', '2004118.6'] | [31, 29, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | cloud_storage | Cloud storage plan | debit | ZAR | ['event_364', 'event_372', 'event_380', 'event_388', 'event_396'] | ['2025-06-12', '2025-07-12', '2025-08-12', '2025-09-12', '2025-10-12'] | ['113.3', '113.3', '113.3', '113.3', '113.3'] | [30, 31, 31, 30] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | debt_repayment | Vehicle loan payment | debit | ZAR | ['event_361', 'event_369', 'event_377', 'event_385', 'event_393'] | ['2025-06-11', '2025-07-11', '2025-08-11', '2025-09-11', '2025-10-11'] | ['968', '968', '968', '968', '968'] | [30, 31, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | family_support | Dependent care payment | debit | ZAR | ['event_363', 'event_371', 'event_379', 'event_387', 'event_395'] | ['2025-06-13', '2025-07-13', '2025-08-13', '2025-09-13', '2025-10-13'] | ['840.4', '840.4', '840.4', '840.4', '840.4'] | [30, 31, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | groceries | Bulk pantry shop | debit | ZAR | ['event_407', 'event_418'] | ['2025-07-08', '2025-09-23'] | ['567.19', '675.81'] | [77] | ['fixed'] | ['settled', 'settled'] |
| user_05 | groceries | Fresh food shop | debit | ZAR | ['event_409', 'event_415', 'event_424'] | ['2025-07-22', '2025-09-02', '2025-11-04'] | ['807.31', '762.65', '720.51'] | [42, 63] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_05 | groceries | Grocery delivery | debit | ZAR | ['event_404', 'event_405', 'event_416', 'event_421'] | ['2025-06-17', '2025-06-24', '2025-09-09', '2025-10-14'] | ['835', '635.23', '515.4', '768.64'] | [7, 77, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_05 | groceries | Household groceries | debit | ZAR | ['event_400', 'event_410', 'event_414', 'event_420'] | ['2025-05-20', '2025-07-29', '2025-08-26', '2025-10-07'] | ['818.16', '800.63', '845.02', '826.66'] | [70, 28, 42] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_05 | groceries | Local market purchase | debit | ZAR | ['event_401', 'event_402', 'event_417', 'event_419'] | ['2025-05-27', '2025-06-03', '2025-09-16', '2025-09-30'] | ['680.15', '530.44', '682.39', '547.6'] | [7, 105, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_05 | groceries | Neighbourhood grocer | debit | ZAR | ['event_408', 'event_413', 'event_422'] | ['2025-07-15', '2025-08-19', '2025-10-21'] | ['767.92', '773.83', '709.62'] | [35, 63] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_05 | groceries | Supermarket basket | debit | ZAR | ['event_399', 'event_406', 'event_423'] | ['2025-05-13', '2025-07-01', '2025-10-28'] | ['784.81', '661.93', '684.39'] | [49, 119] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_05 | groceries | Weekly produce market | debit | ZAR | ['event_403', 'event_411', 'event_412'] | ['2025-06-10', '2025-08-05', '2025-08-12'] | ['695.96', '813.64', '853.42'] | [56, 7] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_05 | healthcare | Therapy appointment | debit | ZAR | ['event_362', 'event_370', 'event_378', 'event_386', 'event_394'] | ['2025-06-10', '2025-07-10', '2025-08-10', '2025-09-10', '2025-10-10'] | ['777.27', '641.37', '632.59', '721.44', '722.37'] | [30, 31, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | rent | Apartment rent transfer | debit | ZAR | ['event_359', 'event_367', 'event_375', 'event_383', 'event_391', 'event_398'] | ['2025-06-02', '2025-07-02', '2025-08-02', '2025-09-02', '2025-10-02', '2025-11-02'] | ['4972', '4972', '4972', '4972', '4972', '4972'] | [30, 31, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | salary | Payroll credit | credit | ZAR | ['event_358', 'event_366', 'event_374', 'event_382'] | ['2025-06-15', '2025-07-15', '2025-08-15', '2025-09-15'] | ['14740', '14740', '14740', '14740'] | [30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_05 | shopping | Personal shopping | debit | ZAR | ['event_365', 'event_373', 'event_381', 'event_389', 'event_397'] | ['2025-06-12', '2025-07-12', '2025-08-12', '2025-09-12', '2025-10-12'] | ['379.94', '404.24', '422.67', '420.31', '362.09'] | [30, 31, 31, 30] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_05 | transport | Fuel refill | debit | ZAR | ['event_426', 'event_431'] | ['2025-05-28', '2025-08-06'] | ['424.26', '431.81'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_05 | transport | Metro and bus fares | debit | ZAR | ['event_428', 'event_430', 'event_436'] | ['2025-06-25', '2025-07-23', '2025-10-15'] | ['492.86', '311', '352.46'] | [28, 84] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_05 | transport | Parking and tolls | debit | ZAR | ['event_425', 'event_432'] | ['2025-05-14', '2025-08-20'] | ['489.31', '354.2'] | [98] | ['fixed'] | ['settled', 'settled'] |
| user_05 | transport | Ride-hailing trip | debit | ZAR | ['event_429', 'event_433', 'event_435'] | ['2025-07-09', '2025-09-03', '2025-10-01'] | ['363.28', '485.59', '377.26'] | [56, 28] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_05 | utilities | Municipal utilities | debit | ZAR | ['event_360', 'event_368', 'event_376', 'event_384', 'event_392'] | ['2025-06-06', '2025-07-06', '2025-08-06', '2025-09-06', '2025-10-06'] | ['604.15', '658.41', '750.89', '706.37', '713.71'] | [30, 31, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | cloud_storage | Shared storage plan | debit | EUR | ['event_443', 'event_451', 'event_459', 'event_467', 'event_475'] | ['2025-08-13', '2025-09-13', '2025-10-13', '2025-11-13', '2025-12-13'] | ['5', '5', '5', '5', '5'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | dining | Bakery and snacks | debit | EUR | ['event_540', 'event_549', 'event_551'] | ['2025-09-07', '2025-11-09', '2025-11-23'] | ['40.23', '43.17', '55.16'] | [63, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_06 | dining | Family dinner | debit | EUR | ['event_539', 'event_553', 'event_555'] | ['2025-08-31', '2025-12-07', '2025-12-21'] | ['37.25', '45.39', '57.28'] | [98, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_06 | dining | Lunch with colleagues | debit | EUR | ['event_532', 'event_542', 'event_545', 'event_546'] | ['2025-07-13', '2025-09-21', '2025-10-12', '2025-10-19'] | ['53.26', '56.6', '47.33', '54.09'] | [70, 21, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_06 | dining | Neighbourhood restaurant | debit | EUR | ['event_536', 'event_538', 'event_541', 'event_543', 'event_544', 'event_552'] | ['2025-08-10', '2025-08-24', '2025-09-14', '2025-09-28', '2025-10-05', '2025-11-30'] | ['48.98', '38.44', '43.95', '48.14', '37.02', '57.57'] | [14, 21, 14, 7, 56] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | dining | Takeaway order | debit | EUR | ['event_533', 'event_534'] | ['2025-07-20', '2025-07-27'] | ['50.79', '34.99'] | [7] | ['fixed'] | ['settled', 'settled'] |
| user_06 | dining | Weekend food delivery | debit | EUR | ['event_535', 'event_537', 'event_547', 'event_554', 'event_556'] | ['2025-08-03', '2025-08-17', '2025-10-26', '2025-12-14', '2025-12-28'] | ['42.1', '46.84', '53.71', '36', '48.36'] | [14, 70, 49, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | entertainment | Monthly entertainment spend | debit | EUR | ['event_446', 'event_454', 'event_462', 'event_470', 'event_478'] | ['2025-08-15', '2025-09-15', '2025-10-15', '2025-11-15', '2025-12-15'] | ['32.1', '35.1', '32.18', '37.36', '38.33'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | groceries | Bulk pantry shop | debit | EUR | ['event_479', 'event_496'] | ['2025-07-11', '2025-12-28'] | ['43.16', '32.69'] | [170] | ['fixed'] | ['settled', 'settled'] |
| user_06 | groceries | Fresh food shop | debit | EUR | ['event_487', 'event_488', 'event_489'] | ['2025-09-29', '2025-10-09', '2025-10-19'] | ['51.55', '46.22', '32.96'] | [10, 10] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_06 | groceries | Grocery delivery | debit | EUR | ['event_483', 'event_486'] | ['2025-08-20', '2025-09-19'] | ['31.69', '48.32'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_06 | groceries | Household groceries | debit | EUR | ['event_481', 'event_485'] | ['2025-07-31', '2025-09-09'] | ['49.49', '51.97'] | [40] | ['fixed'] | ['settled', 'settled'] |
| user_06 | groceries | Local market purchase | debit | EUR | ['event_484', 'event_490', 'event_493'] | ['2025-08-30', '2025-10-29', '2025-11-28'] | ['50.53', '51.4', '51.23'] | [60, 30] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_06 | groceries | Neighbourhood grocer | debit | EUR | ['event_480', 'event_492', 'event_494', 'event_495'] | ['2025-07-21', '2025-11-18', '2025-12-08', '2025-12-18'] | ['53.56', '45.4', '40.91', '52.76'] | [120, 20, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_06 | insurance | Vehicle insurance premium | debit | EUR | ['event_442', 'event_450', 'event_458', 'event_466', 'event_474'] | ['2025-08-08', '2025-09-08', '2025-10-08', '2025-11-08', '2025-12-08'] | ['26', '26', '26', '26', '26'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | rent | Monthly rent | debit | EUR | ['event_440', 'event_448', 'event_456', 'event_464', 'event_472'] | ['2025-08-03', '2025-09-03', '2025-10-03', '2025-11-03', '2025-12-03'] | ['254.1', '254.1', '254.1', '254.1', '254.1'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | salary | Payroll credit | credit | EUR | ['event_439', 'event_447', 'event_455', 'event_463', 'event_471'] | ['2025-08-15', '2025-09-15', '2025-10-15', '2025-11-15', '2025-12-15'] | ['1441', '1441', '1441', '1037.52', '1037.52'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | shopping | Household shopping | debit | EUR | ['event_445', 'event_453', 'event_461', 'event_469', 'event_477'] | ['2025-08-13', '2025-09-13', '2025-10-13', '2025-11-13', '2025-12-13'] | ['41.44', '46.25', '39.46', '37.96', '39.88'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | streaming | Family streaming plan | debit | EUR | ['event_444', 'event_452', 'event_460', 'event_468', 'event_476'] | ['2025-08-10', '2025-09-10', '2025-10-10', '2025-11-10', '2025-12-10'] | ['19', '19', '19', '19', '19'] | [31, 30, 31, 30] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | transport | Commuter pass | debit | EUR | ['event_499', 'event_500', 'event_505', 'event_514'] | ['2025-07-22', '2025-07-27', '2025-08-21', '2025-10-05'] | ['24.21', '19.73', '27.29', '28.87'] | [5, 25, 45] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_06 | transport | Fuel refill | debit | EUR | ['event_512', 'event_526'] | ['2025-09-25', '2025-12-04'] | ['31.87', '29.57'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_06 | transport | Local taxi | debit | EUR | ['event_503', 'event_510', 'event_522', 'event_523', 'event_527'] | ['2025-08-11', '2025-09-15', '2025-11-14', '2025-11-19', '2025-12-09'] | ['28.03', '29.47', '30.82', '27.59', '19.18'] | [35, 60, 5, 20] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | transport | Metro and bus fares | debit | EUR | ['event_504', 'event_507', 'event_515', 'event_521', 'event_528'] | ['2025-08-16', '2025-08-31', '2025-10-10', '2025-11-09', '2025-12-14'] | ['26.82', '27.65', '28.61', '31.69', '25.9'] | [15, 40, 30, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | transport | Parking and tolls | debit | EUR | ['event_497', 'event_506', 'event_509', 'event_511', 'event_513', 'event_517', 'event_524', 'event_531'] | ['2025-07-12', '2025-08-26', '2025-09-10', '2025-09-20', '2025-09-30', '2025-10-20', '2025-11-24', '2025-12-29'] | ['23.68', '31.89', '21.32', '28.08', '21.1', '28.65', '32.36', '32.9'] | [45, 15, 10, 10, 20, 35, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | transport | Rail pass | debit | EUR | ['event_502', 'event_508', 'event_518', 'event_519', 'event_530'] | ['2025-08-06', '2025-09-05', '2025-10-25', '2025-10-30', '2025-12-24'] | ['27.8', '29.46', '23.31', '29.32', '21.46'] | [30, 50, 5, 55] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_06 | transport | Ride-hailing trip | debit | EUR | ['event_498', 'event_520', 'event_529'] | ['2025-07-17', '2025-11-04', '2025-12-19'] | ['23.83', '24.5', '24.92'] | [110, 45] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_06 | transport | Vehicle charging | debit | EUR | ['event_501', 'event_516', 'event_525'] | ['2025-08-01', '2025-10-15', '2025-11-29'] | ['32.17', '22.14', '27.97'] | [75, 45] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_06 | utilities | Water and power payment | debit | EUR | ['event_441', 'event_449', 'event_457', 'event_465', 'event_473'] | ['2025-08-07', '2025-09-07', '2025-10-07', '2025-11-07', '2025-12-07'] | ['58.34', '52.62', '58.98', '56.71', '51.86'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_07 | debt_repayment | Personal loan payment | debit | INR | ['event_561', 'event_566', 'event_571', 'event_576', 'event_581'] | ['2024-04-13', '2024-05-13', '2024-06-13', '2024-07-13', '2024-08-13'] | ['15650', '15650', '15650', '15650', '15650'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_07 | dining | Bakery and snacks | debit | INR | ['event_609', 'event_614'] | ['2024-05-13', '2024-08-26'] | ['6313.91', '6493.86'] | [105] | ['reducible'] | ['settled', 'settled'] |
| user_07 | dining | Family dinner | debit | INR | ['event_608', 'event_610', 'event_611'] | ['2024-04-22', '2024-06-03', '2024-06-24'] | ['6371.55', '5802.49', '4541.62'] | [42, 21] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_07 | groceries | Household groceries | debit | INR | ['event_586', 'event_591', 'event_594', 'event_596'] | ['2024-04-11', '2024-06-20', '2024-08-01', '2024-08-29'] | ['6022.17', '7968.39', '7913.81', '5710.65'] | [70, 42, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_07 | groceries | Supermarket basket | debit | INR | ['event_588', 'event_592'] | ['2024-05-09', '2024-07-04'] | ['8280.58', '6889.87'] | [56] | ['fixed'] | ['settled', 'settled'] |
| user_07 | groceries | Weekly produce market | debit | INR | ['event_584', 'event_585'] | ['2024-03-14', '2024-03-28'] | ['8380.73', '6433.29'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_07 | music_subscription | Music subscription | debit | INR | ['event_562', 'event_567', 'event_572', 'event_577', 'event_582'] | ['2024-04-13', '2024-05-13', '2024-06-13', '2024-07-13', '2024-08-13'] | ['1005', '1005', '1005', '1005', '1005'] | [30, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_07 | rent | Monthly rent | debit | INR | ['event_559', 'event_564', 'event_569', 'event_574', 'event_579', 'event_583'] | ['2024-04-04', '2024-05-04', '2024-06-04', '2024-07-04', '2024-08-04', '2024-09-04'] | ['34200', '34200', '34200', '34200', '34200', '34200'] | [30, 31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_07 | salary | Payroll credit | credit | INR | ['event_558', 'event_563', 'event_568', 'event_573', 'event_578'] | ['2024-04-15', '2024-05-15', '2024-06-15', '2024-07-15', '2024-08-23'] | ['149000', '149000', '149000', '149000', '149000'] | [30, 31, 30, 39] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_07 | transport | Commuter pass | debit | INR | ['event_598', 'event_605'] | ['2024-04-05', '2024-08-30'] | ['3465.99', '3145.62'] | [147] | ['fixed'] | ['settled', 'settled'] |
| user_07 | transport | Metro and bus fares | debit | INR | ['event_597', 'event_600'] | ['2024-03-15', '2024-05-17'] | ['3690.82', '3104.36'] | [63] | ['fixed'] | ['settled', 'settled'] |
| user_07 | transport | Rail pass | debit | INR | ['event_602', 'event_603', 'event_604'] | ['2024-06-28', '2024-07-19', '2024-08-09'] | ['3822.62', '2751.86', '3773.92'] | [21, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_07 | utilities | Electricity bill | debit | INR | ['event_560', 'event_565', 'event_570', 'event_575', 'event_580'] | ['2024-04-08', '2024-05-08', '2024-06-08', '2024-07-08', '2024-08-08'] | ['7219.31', '7049.68', '7387.41', '6081.25', '6209.57'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | debt_repayment | Personal loan payment | debit | EUR | ['event_619', 'event_626', 'event_633', 'event_640', 'event_647'] | ['2024-09-10', '2024-10-10', '2024-11-10', '2024-12-10', '2025-01-10'] | ['177', '177', '177', '177', '177'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | delivery_membership | Grocery delivery membership | debit | EUR | ['event_621', 'event_628', 'event_635', 'event_642', 'event_649'] | ['2024-09-12', '2024-10-12', '2024-11-12', '2024-12-12', '2025-01-12'] | ['24', '24', '24', '24', '24'] | [30, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | dining | Bakery and snacks | debit | EUR | ['event_709', 'event_716'] | ['2024-10-24', '2025-01-30'] | ['41.5', '42.33'] | [98] | ['reducible'] | ['settled', 'settled'] |
| user_08 | dining | Family dinner | debit | EUR | ['event_705', 'event_707'] | ['2024-08-29', '2024-09-26'] | ['59.94', '60.66'] | [28] | ['reducible'] | ['settled', 'settled'] |
| user_08 | dining | Neighbourhood restaurant | debit | EUR | ['event_706', 'event_708'] | ['2024-09-12', '2024-10-10'] | ['46.25', '48.98'] | [28] | ['reducible'] | ['settled', 'settled'] |
| user_08 | dining | Weekend food delivery | debit | EUR | ['event_704', 'event_710', 'event_713', 'event_715'] | ['2024-08-15', '2024-11-07', '2024-12-19', '2025-01-16'] | ['51.75', '58.15', '49.45', '53.65'] | [84, 42, 28] | ['reducible'] | ['settled', 'settled', 'settled', 'settled'] |
| user_08 | education | School fee payment | debit | EUR | ['event_618', 'event_625', 'event_632', 'event_639', 'event_646'] | ['2024-09-07', '2024-10-07', '2024-11-07', '2024-12-07', '2025-01-07'] | ['89', '89', '89', '89', '89'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | groceries | Bulk pantry shop | debit | EUR | ['event_655', 'event_660', 'event_663', 'event_666', 'event_673'] | ['2024-09-03', '2024-10-08', '2024-10-29', '2024-11-19', '2025-01-07'] | ['52.28', '48.16', '47.78', '69.32', '48'] | [35, 21, 21, 49] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | groceries | Fresh food shop | debit | EUR | ['event_652', 'event_657', 'event_659', 'event_661'] | ['2024-08-13', '2024-09-17', '2024-10-01', '2024-10-15'] | ['78.42', '54.35', '74.35', '68.99'] | [35, 14, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_08 | groceries | Grocery delivery | debit | EUR | ['event_664', 'event_665', 'event_667', 'event_672', 'event_675'] | ['2024-11-05', '2024-11-12', '2024-11-26', '2024-12-31', '2025-01-21'] | ['51.6', '76.07', '60.11', '51.85', '53.96'] | [7, 14, 35, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | groceries | Supermarket basket | debit | EUR | ['event_656', 'event_662', 'event_668', 'event_669', 'event_670', 'event_674', 'event_676'] | ['2024-09-10', '2024-10-22', '2024-12-03', '2024-12-10', '2024-12-17', '2025-01-14', '2025-01-28'] | ['68', '57.01', '51', '56.62', '55.02', '45.99', '65.92'] | [42, 42, 7, 7, 28, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | groceries | Weekly produce market | debit | EUR | ['event_654', 'event_671', 'event_677'] | ['2024-08-27', '2024-12-24', '2025-02-04'] | ['51.01', '53.11', '72.38'] | [119, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_08 | music_subscription | Music subscription | debit | EUR | ['event_620', 'event_627', 'event_634', 'event_641', 'event_648'] | ['2024-09-10', '2024-10-10', '2024-11-10', '2024-12-10', '2025-01-10'] | ['14', '14', '14', '14', '14'] | [30, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | rent | Apartment rent transfer | debit | EUR | ['event_616', 'event_623', 'event_630', 'event_637', 'event_644', 'event_650'] | ['2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01', '2025-01-01', '2025-02-01'] | ['467.5', '467.5', '467.5', '467.5', '467.5', '467.5'] | [30, 31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | salary | Payroll credit | credit | EUR | ['event_615', 'event_622', 'event_629', 'event_636', 'event_643'] | ['2024-09-15', '2024-10-15', '2024-11-15', '2024-12-15', '2025-01-15'] | ['1422.85', '1422.85', '1422.85', '1422.85', '782.57'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | transport | Commuter pass | debit | EUR | ['event_693', 'event_701', 'event_702'] | ['2024-11-27', '2025-01-22', '2025-01-29'] | ['35.69', '31.67', '28.33'] | [56, 7] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_08 | transport | Fuel refill | debit | EUR | ['event_682', 'event_687', 'event_703'] | ['2024-09-11', '2024-10-16', '2025-02-05'] | ['37.62', '26.69', '47.21'] | [35, 112] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_08 | transport | Local taxi | debit | EUR | ['event_683', 'event_686', 'event_696', 'event_698'] | ['2024-09-18', '2024-10-09', '2024-12-18', '2025-01-01'] | ['43.53', '38.07', '43.51', '31.5'] | [21, 70, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_08 | transport | Metro and bus fares | debit | EUR | ['event_679', 'event_690', 'event_691', 'event_692', 'event_700'] | ['2024-08-21', '2024-11-06', '2024-11-13', '2024-11-20', '2025-01-15'] | ['36.65', '39.38', '37', '40.22', '32.95'] | [77, 7, 7, 56] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | transport | Parking and tolls | debit | EUR | ['event_681', 'event_684', 'event_685', 'event_688', 'event_695', 'event_697'] | ['2024-09-04', '2024-09-25', '2024-10-02', '2024-10-23', '2024-12-11', '2024-12-25'] | ['40.21', '30.47', '36.94', '46.08', '35.98', '43.2'] | [21, 7, 21, 49, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_08 | transport | Ride-hailing trip | debit | EUR | ['event_678', 'event_689', 'event_694'] | ['2024-08-14', '2024-10-30', '2024-12-04'] | ['34.09', '45.56', '29.03'] | [77, 35] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_08 | transport | Vehicle charging | debit | EUR | ['event_680', 'event_699'] | ['2024-08-28', '2025-01-08'] | ['41.53', '41.57'] | [133] | ['fixed'] | ['settled', 'settled'] |
| user_08 | utilities | Municipal utilities | debit | EUR | ['event_617', 'event_624', 'event_631', 'event_638', 'event_645', 'event_651'] | ['2024-09-05', '2024-10-05', '2024-11-05', '2024-12-05', '2025-01-05', '2025-02-05'] | ['79.19', '80.9', '68.44', '82.61', '69.28', '80.55'] | [30, 31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_09 | cloud_storage | Cloud storage plan | debit | EUR | ['event_721', 'event_728', 'event_735', 'event_742', 'event_749'] | ['2026-02-12', '2026-03-12', '2026-04-12', '2026-05-12', '2026-06-12'] | ['5', '5', '5', '5', '5'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_09 | dining | Family dinner | debit | EUR | ['event_780', 'event_786'] | ['2026-01-10', '2026-05-16'] | ['34.84', '35.49'] | [126] | ['fixed'] | ['settled', 'settled'] |
| user_09 | dining | Quick-service meal | debit | EUR | ['event_784', 'event_785'] | ['2026-04-04', '2026-04-25'] | ['23.42', '28.41'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_09 | dining | Takeaway order | debit | EUR | ['event_782', 'event_787'] | ['2026-02-21', '2026-06-06'] | ['29.97', '27.38'] | [105] | ['fixed'] | ['settled', 'settled'] |
| user_09 | groceries | Bulk pantry shop | debit | EUR | ['event_758', 'event_767', 'event_770'] | ['2026-02-27', '2026-05-28', '2026-06-27'] | ['37.29', '46.49', '51.3'] | [90, 30] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_09 | groceries | Fresh food shop | debit | EUR | ['event_754', 'event_756', 'event_765', 'event_766'] | ['2026-01-18', '2026-02-07', '2026-05-08', '2026-05-18'] | ['38.34', '41.29', '53.82', '34.74'] | [20, 90, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_09 | groceries | Grocery delivery | debit | EUR | ['event_755', 'event_763', 'event_768', 'event_769'] | ['2026-01-28', '2026-04-18', '2026-06-07', '2026-06-17'] | ['47.6', '48.93', '51.03', '43'] | [80, 50, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_09 | groceries | Household groceries | debit | EUR | ['event_753', 'event_759'] | ['2026-01-08', '2026-03-09'] | ['47.44', '36.79'] | [60] | ['fixed'] | ['settled', 'settled'] |
| user_09 | groceries | Local market purchase | debit | EUR | ['event_757', 'event_760'] | ['2026-02-17', '2026-03-19'] | ['54.9', '53.14'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_09 | groceries | Weekly produce market | debit | EUR | ['event_762', 'event_764'] | ['2026-04-08', '2026-04-28'] | ['31.82', '34.17'] | [20] | ['fixed'] | ['settled', 'settled'] |
| user_09 | rent | Monthly rent | debit | EUR | ['event_719', 'event_726', 'event_733', 'event_740', 'event_747', 'event_752'] | ['2026-02-02', '2026-03-02', '2026-04-02', '2026-05-02', '2026-06-02', '2026-07-02'] | ['211.2', '211.2', '211.2', '211.2', '211.2', '211.2'] | [28, 31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_09 | salary | Application project payment | credit | EUR | ['event_732', 'event_739'] | ['2026-04-20', '2026-05-20'] | ['355.99', '441.96'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_09 | salary | Freelance milestone payment | credit | EUR | ['event_717', 'event_738'] | ['2026-02-07', '2026-05-07'] | ['488.8', '506.35'] | [89] | ['fixed'] | ['settled', 'settled'] |
| user_09 | shopping | Household shopping | debit | EUR | ['event_723', 'event_730', 'event_737', 'event_744', 'event_751'] | ['2026-02-12', '2026-03-12', '2026-04-12', '2026-05-12', '2026-06-12'] | ['25.5', '29.14', '28.32', '24.68', '25.52'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_09 | streaming | Video streaming plan | debit | EUR | ['event_722', 'event_729', 'event_736', 'event_743', 'event_750'] | ['2026-02-09', '2026-03-09', '2026-04-09', '2026-05-09', '2026-06-09'] | ['20', '20', '20', '20', '20'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_09 | transport | Commuter pass | debit | EUR | ['event_777', 'event_779'] | ['2026-05-15', '2026-06-26'] | ['28.34', '24.13'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_09 | transport | Local taxi | debit | EUR | ['event_771', 'event_774', 'event_775'] | ['2026-01-09', '2026-03-13', '2026-04-03'] | ['18.44', '27.94', '26.23'] | [63, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_09 | transport | Rail pass | debit | EUR | ['event_773', 'event_778'] | ['2026-02-20', '2026-06-05'] | ['23.57', '27.2'] | [105] | ['fixed'] | ['settled', 'settled'] |
| user_09 | utilities | Water and power payment | debit | EUR | ['event_720', 'event_727', 'event_734', 'event_741', 'event_748'] | ['2026-02-06', '2026-03-06', '2026-04-06', '2026-05-06', '2026-06-06'] | ['66.84', '59.39', '71.04', '63.66', '60.88'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | delivery_membership | Delivery service plan | debit | INR | ['event_796', 'event_806', 'event_816', 'event_826', 'event_836'] | ['2024-07-14', '2024-08-14', '2024-09-14', '2024-10-14', '2024-11-14'] | ['1895', '1895', '1895', '1895', '1895'] | [31, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | dining | Lunch with colleagues | debit | INR | ['event_896', 'event_899', 'event_900'] | ['2024-08-10', '2024-09-21', '2024-10-05'] | ['9399.4', '10079.99', '10525.43'] | [42, 14] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_10 | dining | Takeaway order | debit | INR | ['event_893', 'event_895', 'event_897', 'event_898', 'event_902', 'event_903', 'event_904'] | ['2024-06-29', '2024-07-27', '2024-08-24', '2024-09-07', '2024-11-02', '2024-11-16', '2024-11-30'] | ['9260.11', '6897.95', '9621.2', '6375.03', '8480.31', '8253.71', '10370.83'] | [28, 28, 14, 56, 14, 14] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | entertainment | Cinema and events | debit | INR | ['event_798', 'event_808', 'event_818', 'event_828', 'event_838'] | ['2024-07-15', '2024-08-15', '2024-09-15', '2024-10-15', '2024-11-15'] | ['4770.41', '4504.6', '4700.56', '4366.61', '4883.78'] | [31, 31, 30, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | groceries | Bulk pantry shop | debit | INR | ['event_850', 'event_852', 'event_856'] | ['2024-08-15', '2024-08-29', '2024-09-26'] | ['11074.05', '8855.55', '8809.04'] | [14, 28] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_10 | groceries | Fresh food shop | debit | INR | ['event_841', 'event_845', 'event_846', 'event_860', 'event_861', 'event_863', 'event_865'] | ['2024-06-13', '2024-07-11', '2024-07-18', '2024-10-24', '2024-10-31', '2024-11-14', '2024-11-28'] | ['10089.49', '9512.16', '10839.89', '12767.81', '9968.28', '12092.24', '8755.75'] | [28, 7, 98, 7, 14, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | groceries | Grocery delivery | debit | INR | ['event_842', 'event_843', 'event_844', 'event_853', 'event_857', 'event_859'] | ['2024-06-20', '2024-06-27', '2024-07-04', '2024-09-05', '2024-10-03', '2024-10-17'] | ['12216.63', '10431.63', '12027.49', '12641.36', '9807.08', '13621.53'] | [7, 7, 63, 28, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | groceries | Household groceries | debit | INR | ['event_848', 'event_851'] | ['2024-08-01', '2024-08-22'] | ['12020.19', '9929.21'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_10 | groceries | Local market purchase | debit | INR | ['event_854', 'event_855', 'event_858', 'event_862'] | ['2024-09-12', '2024-09-19', '2024-10-10', '2024-11-07'] | ['10087.39', '11596.13', '12589.2', '10392.47'] | [7, 21, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_10 | groceries | Weekly produce market | debit | INR | ['event_849', 'event_864', 'event_866'] | ['2024-08-08', '2024-11-21', '2024-12-05'] | ['11986', '8157.98', '8011.08'] | [105, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_10 | gym | Community fitness plan | debit | INR | ['event_797', 'event_807', 'event_817', 'event_827', 'event_837'] | ['2024-07-11', '2024-08-11', '2024-09-11', '2024-10-11', '2024-11-11'] | ['4860', '4860', '4860', '4860', '4860'] | [31, 31, 30, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | music_subscription | Music subscription | debit | INR | ['event_795', 'event_805', 'event_815', 'event_825', 'event_835'] | ['2024-07-12', '2024-08-12', '2024-09-12', '2024-10-12', '2024-11-12'] | ['2800', '2800', '2800', '2800', '2800'] | [31, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | rent | Monthly rent | debit | INR | ['event_793', 'event_803', 'event_813', 'event_823', 'event_833', 'event_840'] | ['2024-07-03', '2024-08-03', '2024-09-03', '2024-10-03', '2024-11-03', '2024-12-03'] | ['69100', '69100', '69100', '69100', '69100', '69100'] | [31, 31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | salary | Delivery platform payout | credit | INR | ['event_789', 'event_791', 'event_799', 'event_800', 'event_811', 'event_812', 'event_819', 'event_822', 'event_832'] | ['2024-07-04', '2024-07-18', '2024-08-04', '2024-08-11', '2024-09-18', '2024-09-25', '2024-10-04', '2024-10-25', '2024-11-25'] | ['74420.35', '54774.8', '72641.37', '59553.07', '79168.24', '69351.86', '78226.16', '40977.52', '82667.27'] | [14, 17, 7, 38, 7, 9, 21, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | salary | Driver platform payout | credit | INR | ['event_821', 'event_829', 'event_831', 'event_839'] | ['2024-10-18', '2024-11-04', '2024-11-18', '2024-12-04'] | ['60517.87', '60877.41', '47802.51', '52239.8'] | [17, 14, 16] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_10 | salary | Task marketplace payout | credit | INR | ['event_801', 'event_802', 'event_809', 'event_830'] | ['2024-08-18', '2024-08-25', '2024-09-04', '2024-11-11'] | ['65056.43', '47245.98', '81755.75', '44415.5'] | [7, 10, 68] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_10 | salary | Weekly app earnings | credit | INR | ['event_790', 'event_792', 'event_810', 'event_820'] | ['2024-07-11', '2024-07-25', '2024-09-11', '2024-10-11'] | ['74852.29', '82410.47', '67741.04', '65488.36'] | [14, 48, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_10 | transport | Commuter pass | debit | INR | ['event_871', 'event_879'] | ['2024-07-12', '2024-09-06'] | ['5489.62', '7448.62'] | [56] | ['fixed'] | ['settled', 'settled'] |
| user_10 | transport | Fuel refill | debit | INR | ['event_886', 'event_887'] | ['2024-10-25', '2024-11-01'] | ['6245.32', '6819.66'] | [7] | ['fixed'] | ['settled', 'settled'] |
| user_10 | transport | Local taxi | debit | INR | ['event_869', 'event_872', 'event_875', 'event_880', 'event_881', 'event_883'] | ['2024-06-28', '2024-07-19', '2024-08-09', '2024-09-13', '2024-09-20', '2024-10-04'] | ['4830.13', '7530.3', '6632.3', '5018.36', '6582.39', '4472.6'] | [21, 21, 35, 7, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | transport | Metro and bus fares | debit | INR | ['event_867', 'event_868', 'event_870', 'event_878', 'event_889'] | ['2024-06-14', '2024-06-21', '2024-07-05', '2024-08-30', '2024-11-15'] | ['6859.81', '7100.47', '4956.67', '5753.54', '4990.01'] | [7, 14, 56, 77] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_10 | transport | Parking and tolls | debit | INR | ['event_873', 'event_877', 'event_882'] | ['2024-07-26', '2024-08-23', '2024-09-27'] | ['7568.88', '5747.77', '6785.52'] | [28, 35] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_10 | transport | Rail pass | debit | INR | ['event_876', 'event_888'] | ['2024-08-16', '2024-11-08'] | ['5641.87', '5350.7'] | [84] | ['fixed'] | ['settled', 'settled'] |
| user_10 | transport | Ride-hailing trip | debit | INR | ['event_884', 'event_885', 'event_891'] | ['2024-10-11', '2024-10-18', '2024-11-29'] | ['4570.28', '5776.08', '6359.49'] | [7, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_10 | transport | Vehicle charging | debit | INR | ['event_874', 'event_890'] | ['2024-08-02', '2024-11-22'] | ['6683.23', '4356.14'] | [112] | ['fixed'] | ['settled', 'settled'] |
| user_10 | utilities | Electricity and water bill | debit | INR | ['event_794', 'event_804', 'event_814', 'event_824', 'event_834'] | ['2024-07-07', '2024-08-07', '2024-09-07', '2024-10-07', '2024-11-07'] | ['19224.83', '17538.11', '15748.74', '15236.94', '17771.13'] | [31, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | cloud_storage | Cloud storage plan | debit | IDR | ['event_913', 'event_922', 'event_931', 'event_940', 'event_949'] | ['2024-12-14', '2025-01-14', '2025-02-14', '2025-03-14', '2025-04-14'] | ['168150', '168150', '168150', '168150', '168150'] | [31, 31, 28, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | dining | Bakery and snacks | debit | IDR | ['event_981', 'event_986'] | ['2024-11-06', '2025-02-19'] | ['1018758.07', '1365643.7'] | [105] | ['reducible'] | ['settled', 'settled'] |
| user_11 | dining | Neighbourhood restaurant | debit | IDR | ['event_982', 'event_985'] | ['2024-11-27', '2025-01-29'] | ['1485097.86', '1052748.56'] | [63] | ['reducible'] | ['settled', 'settled'] |
| user_11 | dining | Weekend food delivery | debit | IDR | ['event_983', 'event_989'] | ['2024-12-18', '2025-04-23'] | ['1528058.96', '1163530.49'] | [126] | ['reducible'] | ['settled', 'settled'] |
| user_11 | education | Child education fee | debit | IDR | ['event_910', 'event_919', 'event_928', 'event_937', 'event_946'] | ['2024-12-10', '2025-01-10', '2025-02-10', '2025-03-10', '2025-04-10'] | ['2544100', '2544100', '2544100', '2544100', '2544100'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | entertainment | Games and recreation | debit | IDR | ['event_912', 'event_921', 'event_930', 'event_939', 'event_948'] | ['2024-12-16', '2025-01-16', '2025-02-16', '2025-03-16', '2025-04-16'] | ['1404572.9', '1688239.04', '1587027.72', '1649906.5', '1674887.61'] | [31, 31, 28, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | groceries | Bulk pantry shop | debit | IDR | ['event_954', 'event_962', 'event_965'] | ['2024-12-19', '2025-03-09', '2025-04-08'] | ['1406401.86', '1655671.41', '1590529.64'] | [80, 30] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_11 | groceries | Fresh food shop | debit | IDR | ['event_957', 'event_961', 'event_967'] | ['2025-01-18', '2025-02-27', '2025-04-28'] | ['1578114.18', '1614291.7', '1341187.18'] | [40, 60] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_11 | groceries | Grocery delivery | debit | IDR | ['event_959', 'event_966'] | ['2025-02-07', '2025-04-18'] | ['1241008.74', '1131582.3'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_11 | groceries | Household groceries | debit | IDR | ['event_955', 'event_960'] | ['2024-12-29', '2025-02-17'] | ['1063530.58', '1222447.75'] | [50] | ['fixed'] | ['settled', 'settled'] |
| user_11 | groceries | Neighbourhood grocer | debit | IDR | ['event_950', 'event_951', 'event_958', 'event_963'] | ['2024-11-09', '2024-11-19', '2025-01-28', '2025-03-19'] | ['1053064.17', '1565130.98', '1763208.29', '1311350.07'] | [10, 70, 50] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_11 | groceries | Supermarket basket | debit | IDR | ['event_952', 'event_953'] | ['2024-11-29', '2024-12-09'] | ['1714643.08', '1644304.53'] | [10] | ['fixed'] | ['settled', 'settled'] |
| user_11 | healthcare | Regular medicine purchase | debit | IDR | ['event_911', 'event_920', 'event_929', 'event_938', 'event_947'] | ['2024-12-12', '2025-01-12', '2025-02-12', '2025-03-12', '2025-04-12'] | ['2635764.61', '3118089.32', '2973572.96', '3165638.3', '2826901.92'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | housing | Home association fee | debit | IDR | ['event_907', 'event_916', 'event_925', 'event_934', 'event_943'] | ['2024-12-05', '2025-01-05', '2025-02-05', '2025-03-05', '2025-04-05'] | ['2954500', '2954500', '2954500', '2954500', '2954500'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | insurance | Vehicle insurance premium | debit | IDR | ['event_909', 'event_918', 'event_927', 'event_936', 'event_945'] | ['2024-12-09', '2025-01-09', '2025-02-09', '2025-03-09', '2025-04-09'] | ['1881000', '1881000', '1881000', '1881000', '1881000'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | salary | Base salary | credit | IDR | ['event_905', 'event_914', 'event_923', 'event_932', 'event_941'] | ['2024-12-15', '2025-01-15', '2025-02-15', '2025-03-15', '2025-04-15'] | ['23256000', '23256000', '23256000', '23256000', '23256000'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_11 | salary | Monthly sales commission | credit | IDR | ['event_933', 'event_942'] | ['2025-03-24', '2025-04-24'] | ['20012106.46', '8502888.2'] | [31] | ['fixed'] | ['settled', 'settled'] |
| user_11 | salary | Performance commission | credit | IDR | ['event_906', 'event_915', 'event_924'] | ['2024-12-24', '2025-01-24', '2025-02-24'] | ['16715584.16', '8908379.93', '15989420'] | [31, 31] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_11 | transport | Local taxi | debit | IDR | ['event_971', 'event_973', 'event_974', 'event_979'] | ['2024-12-22', '2025-01-19', '2025-02-02', '2025-04-13'] | ['893623.46', '1307205.52', '785218.72', '1103949.29'] | [28, 14, 70] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_11 | transport | Metro and bus fares | debit | IDR | ['event_970', 'event_972'] | ['2024-12-08', '2025-01-05'] | ['788053.2', '1212904.33'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_11 | transport | Rail pass | debit | IDR | ['event_968', 'event_976'] | ['2024-11-10', '2025-03-02'] | ['1230316.5', '1200020.76'] | [112] | ['fixed'] | ['settled', 'settled'] |
| user_11 | transport | Ride-hailing trip | debit | IDR | ['event_969', 'event_975', 'event_978'] | ['2024-11-24', '2025-02-16', '2025-03-30'] | ['825660.54', '1185524.72', '1122838.73'] | [84, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_11 | transport | Vehicle charging | debit | IDR | ['event_977', 'event_980'] | ['2025-03-16', '2025-04-27'] | ['1244032.33', '1244835.69'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_11 | utilities | Municipal utilities | debit | IDR | ['event_908', 'event_917', 'event_926', 'event_935', 'event_944'] | ['2024-12-08', '2025-01-08', '2025-02-08', '2025-03-08', '2025-04-08'] | ['2916312.61', '2891149.67', '2508782.45', '2488665.63', '2796165.18'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_12 | cloud_storage | Shared storage plan | debit | ZAR | ['event_993', 'event_999', 'event_1005', 'event_1010', 'event_1015'] | ['2025-11-11', '2025-12-11', '2026-01-11', '2026-02-11', '2026-03-11'] | ['447.7', '447.7', '447.7', '447.7', '447.7'] | [30, 31, 31, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_12 | dining | Coffee shop | debit | ZAR | ['event_1053', 'event_1054'] | ['2026-03-07', '2026-03-28'] | ['2089.92', '1943.35'] | [21] | ['reducible'] | ['settled', 'settled'] |
| user_12 | dining | Lunch with colleagues | debit | ZAR | ['event_1048', 'event_1052'] | ['2025-11-22', '2026-02-14'] | ['2407.92', '1765.33'] | [84] | ['reducible'] | ['settled', 'settled'] |
| user_12 | dining | Takeaway order | debit | ZAR | ['event_1047', 'event_1050', 'event_1051'] | ['2025-11-01', '2026-01-03', '2026-01-24'] | ['2452.07', '2344.45', '2608.96'] | [63, 21] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_12 | groceries | Bulk pantry shop | debit | ZAR | ['event_1024', 'event_1031', 'event_1035'] | ['2025-11-28', '2026-02-06', '2026-03-18'] | ['2177.71', '1587.87', '1806.77'] | [70, 40] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_12 | groceries | Grocery delivery | debit | ZAR | ['event_1019', 'event_1032'] | ['2025-10-09', '2026-02-16'] | ['2484.14', '2404.94'] | [130] | ['fixed'] | ['settled', 'settled'] |
| user_12 | groceries | Household groceries | debit | ZAR | ['event_1023', 'event_1034'] | ['2025-11-18', '2026-03-08'] | ['2333.98', '2469.4'] | [110] | ['fixed'] | ['settled', 'settled'] |
| user_12 | groceries | Supermarket basket | debit | ZAR | ['event_1021', 'event_1025', 'event_1026', 'event_1027', 'event_1028', 'event_1030'] | ['2025-10-29', '2025-12-08', '2025-12-18', '2025-12-28', '2026-01-07', '2026-01-27'] | ['2229.55', '1797.17', '2448', '2432.91', '1930.95', '1539.11'] | [40, 10, 10, 10, 20] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_12 | groceries | Weekly produce market | debit | ZAR | ['event_1020', 'event_1022'] | ['2025-10-19', '2025-11-08'] | ['2333.56', '1622.75'] | [20] | ['fixed'] | ['settled', 'settled'] |
| user_12 | rent | Monthly rent | debit | ZAR | ['event_991', 'event_997', 'event_1003', 'event_1008', 'event_1013', 'event_1018'] | ['2025-11-01', '2025-12-01', '2026-01-01', '2026-02-01', '2026-03-01', '2026-04-01'] | ['11792', '11792', '11792', '11792', '11792', '11792'] | [30, 31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_12 | salary | Seasonal contract payment | credit | ZAR | ['event_990', 'event_996'] | ['2025-11-15', '2025-12-15'] | ['55846.64', '41904.42'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_12 | shopping | Monthly shopping spend | debit | ZAR | ['event_995', 'event_1001', 'event_1007', 'event_1012', 'event_1017'] | ['2025-11-11', '2025-12-11', '2026-01-11', '2026-02-11', '2026-03-11'] | ['1267.67', '1243.49', '1401.99', '1196.86', '1169.42'] | [30, 31, 31, 28] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_12 | streaming | Family streaming plan | debit | ZAR | ['event_994', 'event_1000', 'event_1006', 'event_1011', 'event_1016'] | ['2025-11-08', '2025-12-08', '2026-01-08', '2026-02-08', '2026-03-08'] | ['1504.8', '1504.8', '1504.8', '1504.8', '1504.8'] | [30, 31, 31, 28] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_12 | transport | Parking and tolls | debit | ZAR | ['event_1040', 'event_1045'] | ['2025-12-12', '2026-03-27'] | ['1240.84', '1679.15'] | [105] | ['fixed'] | ['settled', 'settled'] |
| user_12 | transport | Rail pass | debit | ZAR | ['event_1037', 'event_1038'] | ['2025-10-10', '2025-10-31'] | ['1398.61', '1302.02'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_12 | transport | Vehicle charging | debit | ZAR | ['event_1039', 'event_1041', 'event_1043'] | ['2025-11-21', '2026-01-02', '2026-02-13'] | ['1282.01', '1722.14', '1355.85'] | [42, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_12 | utilities | Water and power payment | debit | ZAR | ['event_992', 'event_998', 'event_1004', 'event_1009', 'event_1014'] | ['2025-11-05', '2025-12-05', '2026-01-05', '2026-02-05', '2026-03-05'] | ['3103.78', '3374.49', '3755.96', '3708.19', '3606.2'] | [30, 31, 31, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | delivery_membership | Delivery service plan | debit | EUR | ['event_1060', 'event_1068', 'event_1076', 'event_1084', 'event_1091'] | ['2023-10-13', '2023-11-13', '2023-12-13', '2024-01-13', '2024-02-13'] | ['21', '21', '21', '21', '21'] | [31, 30, 31, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | dining | Family dinner | debit | EUR | ['event_1157', 'event_1158'] | ['2024-01-18', '2024-02-01'] | ['48.2', '60.34'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_13 | dining | Quick-service meal | debit | EUR | ['event_1148', 'event_1153'] | ['2023-09-14', '2023-11-23'] | ['75.47', '80.35'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_13 | dining | Takeaway order | debit | EUR | ['event_1149', 'event_1152'] | ['2023-09-28', '2023-11-09'] | ['68.7', '53.91'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_13 | dining | Weekend food delivery | debit | EUR | ['event_1154', 'event_1159', 'event_1160'] | ['2023-12-07', '2024-02-15', '2024-02-29'] | ['64.45', '48.02', '61.28'] | [70, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | entertainment | Local event tickets | debit | EUR | ['event_1062', 'event_1070', 'event_1078', 'event_1086', 'event_1093'] | ['2023-10-14', '2023-11-14', '2023-12-14', '2024-01-14', '2024-02-14'] | ['33.83', '30.88', '37.9', '31.8', '30.39'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | groceries | Bulk pantry shop | debit | EUR | ['event_1115', 'event_1117', 'event_1121'] | ['2024-01-23', '2024-02-06', '2024-03-05'] | ['120.89', '73.74', '93.66'] | [14, 28] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | groceries | Fresh food shop | debit | EUR | ['event_1097', 'event_1099'] | ['2023-09-19', '2023-10-03'] | ['114.9', '82.38'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_13 | groceries | Grocery delivery | debit | EUR | ['event_1102', 'event_1104', 'event_1116', 'event_1119', 'event_1120'] | ['2023-10-24', '2023-11-07', '2024-01-30', '2024-02-20', '2024-02-27'] | ['91.28', '101.74', '114.53', '118.36', '85.71'] | [14, 84, 21, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | groceries | Local market purchase | debit | EUR | ['event_1100', 'event_1105', 'event_1109', 'event_1110', 'event_1114'] | ['2023-10-10', '2023-11-14', '2023-12-12', '2023-12-19', '2024-01-16'] | ['115.37', '102.05', '102.25', '93.15', '84.23'] | [35, 28, 7, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | groceries | Neighbourhood grocer | debit | EUR | ['event_1096', 'event_1106', 'event_1108'] | ['2023-09-12', '2023-11-21', '2023-12-05'] | ['91.05', '119.05', '106.05'] | [70, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | groceries | Supermarket basket | debit | EUR | ['event_1107', 'event_1112', 'event_1113'] | ['2023-11-28', '2024-01-02', '2024-01-09'] | ['101.87', '86.23', '94.28'] | [35, 7] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | groceries | Weekly produce market | debit | EUR | ['event_1098', 'event_1101', 'event_1103', 'event_1111', 'event_1118'] | ['2023-09-26', '2023-10-17', '2023-10-31', '2023-12-26', '2024-02-13'] | ['120.16', '89.89', '108.75', '81.24', '98.36'] | [21, 14, 56, 49] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | gym | Community fitness plan | debit | EUR | ['event_1061', 'event_1069', 'event_1077', 'event_1085', 'event_1092'] | ['2023-10-10', '2023-11-10', '2023-12-10', '2024-01-10', '2024-02-10'] | ['61', '61', '61', '61', '61'] | [31, 30, 31, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | music_subscription | Music subscription | debit | EUR | ['event_1059', 'event_1067', 'event_1075', 'event_1083', 'event_1090'] | ['2023-10-11', '2023-11-11', '2023-12-11', '2024-01-11', '2024-02-11'] | ['29', '29', '29', '29', '29'] | [31, 30, 31, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | rent | Shared housing rent | debit | EUR | ['event_1057', 'event_1065', 'event_1073', 'event_1081', 'event_1088', 'event_1094'] | ['2023-10-02', '2023-11-02', '2023-12-02', '2024-01-02', '2024-02-02', '2024-03-02'] | ['622.6', '622.6', '622.6', '622.6', '622.6', '622.6'] | [31, 30, 31, 31, 29] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | salary | Primary household salary | credit | EUR | ['event_1055', 'event_1063', 'event_1071', 'event_1079', 'event_1087'] | ['2023-10-15', '2023-11-15', '2023-12-15', '2024-01-15', '2024-02-15'] | ['1343.54', '1343.54', '1343.54', '1343.54', '1343.54'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | salary | Second household income | credit | EUR | ['event_1056', 'event_1064', 'event_1072', 'event_1080'] | ['2023-10-20', '2023-11-20', '2023-12-20', '2024-01-20'] | ['993.88', '771.17', '948.46', '881.45'] | [31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_13 | transport | Commuter pass | debit | EUR | ['event_1122', 'event_1131', 'event_1132', 'event_1133', 'event_1138'] | ['2023-09-13', '2023-11-15', '2023-11-22', '2023-11-29', '2024-01-03'] | ['44.85', '48.13', '54.4', '38.31', '43.41'] | [63, 7, 7, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_13 | transport | Fuel refill | debit | EUR | ['event_1134', 'event_1135', 'event_1144'] | ['2023-12-06', '2023-12-13', '2024-02-14'] | ['44.07', '50.38', '45.37'] | [7, 63] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | transport | Local taxi | debit | EUR | ['event_1125', 'event_1129', 'event_1130', 'event_1142'] | ['2023-10-04', '2023-11-01', '2023-11-08', '2024-01-31'] | ['34.28', '54.58', '33.97', '46.98'] | [28, 7, 84] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_13 | transport | Metro and bus fares | debit | EUR | ['event_1123', 'event_1124', 'event_1137', 'event_1145'] | ['2023-09-20', '2023-09-27', '2023-12-27', '2024-02-21'] | ['35.12', '34.47', '46.73', '39.48'] | [7, 91, 56] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_13 | transport | Parking and tolls | debit | EUR | ['event_1127', 'event_1139'] | ['2023-10-18', '2024-01-10'] | ['55.33', '58.44'] | [84] | ['fixed'] | ['settled', 'settled'] |
| user_13 | transport | Rail pass | debit | EUR | ['event_1126', 'event_1141', 'event_1143'] | ['2023-10-11', '2024-01-24', '2024-02-07'] | ['50.6', '56.63', '45.29'] | [105, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | transport | Ride-hailing trip | debit | EUR | ['event_1136', 'event_1140', 'event_1146'] | ['2023-12-20', '2024-01-17', '2024-02-28'] | ['49.29', '33.5', '50.46'] | [28, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_13 | transport | Vehicle charging | debit | EUR | ['event_1128', 'event_1147'] | ['2023-10-25', '2024-03-06'] | ['34.09', '37.29'] | [133] | ['fixed'] | ['settled', 'settled'] |
| user_13 | utilities | Water and power payment | debit | EUR | ['event_1058', 'event_1066', 'event_1074', 'event_1082', 'event_1089', 'event_1095'] | ['2023-10-06', '2023-11-06', '2023-12-06', '2024-01-06', '2024-02-06', '2024-03-06'] | ['162.77', '143.39', '146.33', '143.7', '131.53', '134.25'] | [31, 30, 31, 31, 29] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | cloud_storage | Cloud storage plan | debit | EUR | ['event_1168', 'event_1176', 'event_1183', 'event_1190', 'event_1198'] | ['2025-03-13', '2025-04-13', '2025-05-13', '2025-06-13', '2025-07-13'] | ['14', '14', '14', '14', '14'] | [31, 30, 31, 30] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | debt_repayment | Credit card repayment | debit | EUR | ['event_1165', 'event_1173', 'event_1180', 'event_1187', 'event_1195'] | ['2025-03-12', '2025-04-12', '2025-05-12', '2025-06-12', '2025-07-12'] | ['350', '350', '350', '350', '350'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | family_support | Family support payment | debit | EUR | ['event_1167', 'event_1175', 'event_1182', 'event_1189', 'event_1197'] | ['2025-03-14', '2025-04-14', '2025-05-14', '2025-06-14', '2025-07-14'] | ['226', '226', '226', '226', '226'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | groceries | Bulk pantry shop | debit | EUR | ['event_1207', 'event_1219', 'event_1226'] | ['2025-03-23', '2025-06-15', '2025-08-03'] | ['87.64', '94.21', '129.56'] | [84, 49] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_14 | groceries | Fresh food shop | debit | EUR | ['event_1204', 'event_1209', 'event_1217'] | ['2025-03-02', '2025-04-06', '2025-06-01'] | ['81.22', '131.02', '129.68'] | [35, 56] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_14 | groceries | Grocery delivery | debit | EUR | ['event_1203', 'event_1205', 'event_1211', 'event_1212', 'event_1218'] | ['2025-02-23', '2025-03-09', '2025-04-20', '2025-04-27', '2025-06-08'] | ['104.91', '92.09', '93.46', '90.76', '123.41'] | [14, 42, 7, 42] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | groceries | Household groceries | debit | EUR | ['event_1206', 'event_1208'] | ['2025-03-16', '2025-03-30'] | ['121.61', '140.51'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_14 | groceries | Local market purchase | debit | EUR | ['event_1202', 'event_1210', 'event_1222', 'event_1224'] | ['2025-02-16', '2025-04-13', '2025-07-06', '2025-07-20'] | ['95.35', '83.71', '102.54', '96.86'] | [56, 84, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_14 | groceries | Neighbourhood grocer | debit | EUR | ['event_1214', 'event_1220'] | ['2025-05-11', '2025-06-22'] | ['93.65', '86.49'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_14 | groceries | Supermarket basket | debit | EUR | ['event_1213', 'event_1215', 'event_1216'] | ['2025-05-04', '2025-05-18', '2025-05-25'] | ['106.55', '96.42', '101.15'] | [14, 7] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_14 | groceries | Weekly produce market | debit | EUR | ['event_1201', 'event_1221', 'event_1223', 'event_1225'] | ['2025-02-09', '2025-06-29', '2025-07-13', '2025-07-27'] | ['103.53', '138.85', '112.72', '86.83'] | [140, 14, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_14 | healthcare | Family healthcare expense | debit | EUR | ['event_1166', 'event_1174', 'event_1181', 'event_1188', 'event_1196'] | ['2025-03-11', '2025-04-11', '2025-05-11', '2025-06-11', '2025-07-11'] | ['92.08', '92.65', '95.17', '91.77', '87.84'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | rent | Monthly rent | debit | EUR | ['event_1163', 'event_1171', 'event_1178', 'event_1185', 'event_1193', 'event_1200'] | ['2025-03-03', '2025-04-03', '2025-05-03', '2025-06-03', '2025-07-03', '2025-08-03'] | ['688.6', '688.6', '688.6', '688.6', '688.6', '688.6'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | salary | Payroll before leave | credit | EUR | ['event_1162', 'event_1170'] | ['2025-03-15', '2025-04-15'] | ['2717', '2717'] | [31] | ['fixed'] | ['settled', 'settled'] |
| user_14 | shopping | Online retail purchases | debit | EUR | ['event_1169', 'event_1177', 'event_1184', 'event_1191', 'event_1199'] | ['2025-03-13', '2025-04-13', '2025-05-13', '2025-06-13', '2025-07-13'] | ['137.03', '123.04', '123.12', '123.77', '140.39'] | [31, 30, 31, 30] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_14 | transport | Fuel refill | debit | EUR | ['event_1232', 'event_1233'] | ['2025-04-21', '2025-05-05'] | ['56.49', '55.52'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_14 | transport | Parking and tolls | debit | EUR | ['event_1229', 'event_1235'] | ['2025-03-10', '2025-06-02'] | ['37.65', '50.48'] | [84] | ['fixed'] | ['settled', 'settled'] |
| user_14 | transport | Rail pass | debit | EUR | ['event_1237', 'event_1238'] | ['2025-06-30', '2025-07-14'] | ['62.3', '43.12'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_14 | transport | Ride-hailing trip | debit | EUR | ['event_1234', 'event_1239'] | ['2025-05-19', '2025-07-28'] | ['52.26', '43.88'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_14 | transport | Vehicle charging | debit | EUR | ['event_1227', 'event_1228'] | ['2025-02-10', '2025-02-24'] | ['46.75', '58.52'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_14 | utilities | Energy provider bill | debit | EUR | ['event_1164', 'event_1172', 'event_1179', 'event_1186', 'event_1194'] | ['2025-03-07', '2025-04-07', '2025-05-07', '2025-06-07', '2025-07-07'] | ['141.46', '156.08', '143.45', '146.41', '153.69'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | debt_repayment | Credit card repayment | debit | EUR | ['event_1243', 'event_1249', 'event_1255', 'event_1262', 'event_1269'] | ['2025-08-13', '2025-09-13', '2025-10-13', '2025-11-13', '2025-12-13'] | ['84', '84', '84', '84', '84'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | delivery_membership | Food delivery membership | debit | EUR | ['event_1245', 'event_1251', 'event_1257', 'event_1264', 'event_1271'] | ['2025-08-15', '2025-09-15', '2025-10-15', '2025-11-15', '2025-12-15'] | ['27', '27', '27', '27', '27'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | dining | Bakery and snacks | debit | EUR | ['event_1332', 'event_1335'] | ['2025-11-15', '2025-12-27'] | ['51.08', '49.35'] | [42] | ['reducible'] | ['settled', 'settled'] |
| user_15 | dining | Neighbourhood restaurant | debit | EUR | ['event_1329', 'event_1331'] | ['2025-10-04', '2025-11-01'] | ['32.17', '38.56'] | [28] | ['reducible'] | ['settled', 'settled'] |
| user_15 | dining | Takeaway order | debit | EUR | ['event_1324', 'event_1328', 'event_1330'] | ['2025-07-26', '2025-09-20', '2025-10-18'] | ['41.42', '36.23', '34.51'] | [56, 28] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_15 | dining | Weekend food delivery | debit | EUR | ['event_1323', 'event_1327', 'event_1333'] | ['2025-07-12', '2025-09-06', '2025-11-29'] | ['33.39', '53.58', '32.62'] | [56, 84] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_15 | education | School fee payment | debit | EUR | ['event_1242', 'event_1248', 'event_1254', 'event_1261', 'event_1268'] | ['2025-08-10', '2025-09-10', '2025-10-10', '2025-11-10', '2025-12-10'] | ['159', '159', '159', '159', '159'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | groceries | Bulk pantry shop | debit | EUR | ['event_1274', 'event_1278', 'event_1281', 'event_1282', 'event_1294'] | ['2025-07-22', '2025-08-19', '2025-09-09', '2025-09-16', '2025-12-09'] | ['63.15', '46.76', '73.5', '71.16', '64.22'] | [28, 21, 7, 84] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | groceries | Fresh food shop | debit | EUR | ['event_1280', 'event_1284', 'event_1287', 'event_1293'] | ['2025-09-02', '2025-09-30', '2025-10-21', '2025-12-02'] | ['49.38', '59.88', '62.21', '64.51'] | [28, 21, 42] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_15 | groceries | Grocery delivery | debit | EUR | ['event_1276', 'event_1277', 'event_1283', 'event_1289', 'event_1295', 'event_1296'] | ['2025-08-05', '2025-08-12', '2025-09-23', '2025-11-04', '2025-12-16', '2025-12-23'] | ['55.63', '68.03', '72.3', '56.7', '52.69', '49.9'] | [7, 42, 42, 42, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | groceries | Household groceries | debit | EUR | ['event_1273', 'event_1275'] | ['2025-07-15', '2025-07-29'] | ['51.57', '64.39'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_15 | groceries | Local market purchase | debit | EUR | ['event_1286', 'event_1290', 'event_1297'] | ['2025-10-14', '2025-11-11', '2025-12-30'] | ['69.83', '52.65', '64.42'] | [28, 49] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_15 | groceries | Neighbourhood grocer | debit | EUR | ['event_1291', 'event_1292'] | ['2025-11-18', '2025-11-25'] | ['53.42', '47.26'] | [7] | ['fixed'] | ['settled', 'settled'] |
| user_15 | groceries | Supermarket basket | debit | EUR | ['event_1279', 'event_1285'] | ['2025-08-26', '2025-10-07'] | ['71.92', '48.88'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_15 | music_subscription | Music subscription | debit | EUR | ['event_1244', 'event_1250', 'event_1256', 'event_1263', 'event_1270'] | ['2025-08-13', '2025-09-13', '2025-10-13', '2025-11-13', '2025-12-13'] | ['11', '11', '11', '11', '11'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | rent | Landlord standing order | debit | EUR | ['event_1240', 'event_1246', 'event_1252', 'event_1259', 'event_1266', 'event_1272'] | ['2025-08-04', '2025-09-04', '2025-10-04', '2025-11-04', '2025-12-04', '2026-01-04'] | ['435.6', '435.6', '435.6', '435.6', '435.6', '435.6'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | salary | First-job payroll | credit | EUR | ['event_1258', 'event_1265'] | ['2025-11-15', '2025-12-15'] | ['1661', '1661'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_15 | transport | Commuter pass | debit | EUR | ['event_1301', 'event_1307', 'event_1315', 'event_1317'] | ['2025-08-06', '2025-09-17', '2025-11-12', '2025-11-26'] | ['29.38', '35.61', '32.48', '38.53'] | [42, 56, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_15 | transport | Fuel refill | debit | EUR | ['event_1298', 'event_1311', 'event_1313'] | ['2025-07-16', '2025-10-15', '2025-10-29'] | ['29.41', '25.57', '34.86'] | [91, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_15 | transport | Local taxi | debit | EUR | ['event_1310', 'event_1314'] | ['2025-10-08', '2025-11-05'] | ['26', '31.09'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_15 | transport | Metro and bus fares | debit | EUR | ['event_1299', 'event_1303', 'event_1305', 'event_1306', 'event_1309', 'event_1320'] | ['2025-07-23', '2025-08-20', '2025-09-03', '2025-09-10', '2025-10-01', '2025-12-17'] | ['39.06', '26.5', '37.01', '29.73', '29.3', '36.86'] | [28, 14, 7, 21, 77] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_15 | transport | Rail pass | debit | EUR | ['event_1302', 'event_1312', 'event_1318', 'event_1321'] | ['2025-08-13', '2025-10-22', '2025-12-03', '2025-12-24'] | ['26.48', '25.35', '25.63', '27.67'] | [70, 42, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_15 | transport | Ride-hailing trip | debit | EUR | ['event_1316', 'event_1319', 'event_1322'] | ['2025-11-19', '2025-12-10', '2025-12-31'] | ['36.7', '41.35', '30.31'] | [21, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_15 | transport | Vehicle charging | debit | EUR | ['event_1300', 'event_1308'] | ['2025-07-30', '2025-09-24'] | ['42.66', '31.28'] | [56] | ['fixed'] | ['settled', 'settled'] |
| user_15 | utilities | Energy provider bill | debit | EUR | ['event_1241', 'event_1247', 'event_1253', 'event_1260', 'event_1267'] | ['2025-08-08', '2025-09-08', '2025-10-08', '2025-11-08', '2025-12-08'] | ['84.12', '85.91', '90.39', '87.14', '84.41'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | cloud_storage | Cloud storage plan | debit | INR | ['event_1341', 'event_1348', 'event_1355', 'event_1362', 'event_1369', 'event_1375'] | ['2023-03-11', '2023-04-11', '2023-05-11', '2023-06-11', '2023-07-11', '2023-08-11'] | ['1055', '1055', '1055', '1055', '1055', '1055'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | debt_repayment | Vehicle loan payment | debit | INR | ['event_1339', 'event_1346', 'event_1353', 'event_1360', 'event_1367', 'event_1373'] | ['2023-03-10', '2023-04-10', '2023-05-10', '2023-06-10', '2023-07-10', '2023-08-10'] | ['17750', '17750', '17750', '17750', '17750', '17750'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | dining | Bakery and snacks | debit | INR | ['event_1436', 'event_1440', 'event_1441'] | ['2023-05-26', '2023-07-21', '2023-08-04'] | ['5905.06', '6354.26', '5256.32'] | [56, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_16 | dining | Coffee shop | debit | INR | ['event_1429', 'event_1437', 'event_1438'] | ['2023-02-17', '2023-06-09', '2023-06-23'] | ['5271.93', '5981.93', '5210.3'] | [112, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_16 | dining | Weekend food delivery | debit | INR | ['event_1430', 'event_1431', 'event_1434', 'event_1439'] | ['2023-03-03', '2023-03-17', '2023-04-28', '2023-07-07'] | ['4791.94', '5478.94', '5461.61', '3835.73'] | [14, 42, 70] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_16 | groceries | Bulk pantry shop | debit | INR | ['event_1383', 'event_1396', 'event_1397'] | ['2023-03-29', '2023-06-28', '2023-07-05'] | ['5583.98', '6091.85', '5623.39'] | [91, 7] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_16 | groceries | Fresh food shop | debit | INR | ['event_1378', 'event_1387', 'event_1390', 'event_1391', 'event_1399'] | ['2023-02-22', '2023-04-26', '2023-05-17', '2023-05-24', '2023-07-19'] | ['8882.85', '5434.36', '8225.29', '8445.69', '7181.79'] | [63, 21, 7, 56] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | groceries | Grocery delivery | debit | INR | ['event_1386', 'event_1388', 'event_1392', 'event_1393'] | ['2023-04-19', '2023-05-03', '2023-05-31', '2023-06-07'] | ['5463.03', '8465.36', '5495.8', '6971.09'] | [14, 28, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_16 | groceries | Neighbourhood grocer | debit | INR | ['event_1379', 'event_1380', 'event_1384', 'event_1385', 'event_1400', 'event_1401', 'event_1402'] | ['2023-03-01', '2023-03-08', '2023-04-05', '2023-04-12', '2023-07-26', '2023-08-02', '2023-08-09'] | ['9038.15', '8137.99', '9111.36', '7101.43', '8883.15', '6568.76', '7930.19'] | [7, 28, 7, 105, 7, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | groceries | Weekly produce market | debit | INR | ['event_1377', 'event_1389', 'event_1395', 'event_1398'] | ['2023-02-15', '2023-05-10', '2023-06-21', '2023-07-12'] | ['6134.32', '5364.38', '6302.62', '6716.29'] | [84, 42, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_16 | rent | Monthly rent | debit | INR | ['event_1337', 'event_1344', 'event_1351', 'event_1358', 'event_1365', 'event_1371'] | ['2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01'] | ['57100', '57100', '57100', '57100', '57100', '57100'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | salary | Payroll credit | credit | INR | ['event_1336', 'event_1343', 'event_1350', 'event_1357', 'event_1364'] | ['2023-03-15', '2023-04-15', '2023-05-15', '2023-06-15', '2023-07-15'] | ['173000', '173000', '173000', '173000', '173000'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | shopping | Clothing and household items | debit | INR | ['event_1342', 'event_1349', 'event_1356', 'event_1363', 'event_1370', 'event_1376'] | ['2023-03-11', '2023-04-11', '2023-05-11', '2023-06-11', '2023-07-11', '2023-08-11'] | ['9307.32', '8486.21', '8885', '8414.47', '9807.5', '10178.56'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | streaming | Video streaming plan | debit | INR | ['event_1340', 'event_1347', 'event_1354', 'event_1361', 'event_1368', 'event_1374'] | ['2023-03-08', '2023-04-08', '2023-05-08', '2023-06-08', '2023-07-08', '2023-08-08'] | ['3510', '3510', '3510', '3510', '3510', '3510'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | transport | Commuter pass | debit | INR | ['event_1410', 'event_1412'] | ['2023-04-06', '2023-04-20'] | ['5236.08', '4859.49'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_16 | transport | Local taxi | debit | INR | ['event_1405', 'event_1413', 'event_1418', 'event_1419', 'event_1424'] | ['2023-03-02', '2023-04-27', '2023-06-01', '2023-06-08', '2023-07-13'] | ['4483.65', '5284.1', '5067.66', '3885.07', '4643.67'] | [56, 35, 7, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | transport | Metro and bus fares | debit | INR | ['event_1409', 'event_1411', 'event_1420'] | ['2023-03-30', '2023-04-13', '2023-06-15'] | ['3170.83', '4284.41', '4175.44'] | [14, 63] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_16 | transport | Parking and tolls | debit | INR | ['event_1406', 'event_1415', 'event_1426', 'event_1428'] | ['2023-03-09', '2023-05-11', '2023-07-27', '2023-08-10'] | ['4106.4', '3143.71', '5251.4', '4978.93'] | [63, 77, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_16 | transport | Rail pass | debit | INR | ['event_1403', 'event_1408', 'event_1414', 'event_1416', 'event_1423', 'event_1427'] | ['2023-02-16', '2023-03-23', '2023-05-04', '2023-05-18', '2023-07-06', '2023-08-03'] | ['4382.18', '3653.49', '5016.88', '4523.27', '5087.33', '5368.95'] | [35, 42, 14, 49, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_16 | transport | Ride-hailing trip | debit | INR | ['event_1404', 'event_1421', 'event_1425'] | ['2023-02-23', '2023-06-22', '2023-07-20'] | ['3464.26', '3688.64', '3888.24'] | [119, 28] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_16 | transport | Vehicle charging | debit | INR | ['event_1407', 'event_1417', 'event_1422'] | ['2023-03-16', '2023-05-25', '2023-06-29'] | ['5267.76', '3624.64', '4368.27'] | [70, 35] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_16 | utilities | Energy provider bill | debit | INR | ['event_1338', 'event_1345', 'event_1352', 'event_1359', 'event_1366', 'event_1372'] | ['2023-03-05', '2023-04-05', '2023-05-05', '2023-06-05', '2023-07-05', '2023-08-05'] | ['11173.73', '9756.03', '10586.37', '9402.67', '10012.92', '11512.87'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | debt_repayment | Credit card repayment | debit | INR | ['event_1447', 'event_1454', 'event_1461', 'event_1468', 'event_1475'] | ['2025-10-11', '2025-11-11', '2025-12-11', '2026-01-11', '2026-02-11'] | ['30200', '30200', '30200', '30200', '30200'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | delivery_membership | Food delivery membership | debit | INR | ['event_1449', 'event_1456', 'event_1463', 'event_1470', 'event_1477'] | ['2025-10-13', '2025-11-13', '2025-12-13', '2026-01-13', '2026-02-13'] | ['1675', '1675', '1675', '1675', '1675'] | [31, 30, 31, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | dining | Bakery and snacks | debit | INR | ['event_1530', 'event_1533', 'event_1537'] | ['2025-09-07', '2025-10-19', '2025-12-14'] | ['5641.06', '5554.91', '6048.91'] | [42, 56] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_17 | dining | Family dinner | debit | INR | ['event_1541', 'event_1542'] | ['2026-02-08', '2026-02-22'] | ['6688.81', '4747.76'] | [14] | ['reducible'] | ['settled', 'settled'] |
| user_17 | dining | Neighbourhood restaurant | debit | INR | ['event_1535', 'event_1536'] | ['2025-11-16', '2025-11-30'] | ['5593.53', '6839.37'] | [14] | ['reducible'] | ['settled', 'settled'] |
| user_17 | dining | Quick-service meal | debit | INR | ['event_1539', 'event_1540'] | ['2026-01-11', '2026-01-25'] | ['6797.26', '5254.41'] | [14] | ['reducible'] | ['settled', 'settled'] |
| user_17 | dining | Takeaway order | debit | INR | ['event_1531', 'event_1534'] | ['2025-09-21', '2025-11-02'] | ['4425.44', '6027.54'] | [42] | ['reducible'] | ['settled', 'settled'] |
| user_17 | education | Course tuition | debit | INR | ['event_1446', 'event_1453', 'event_1460', 'event_1467', 'event_1474'] | ['2025-10-08', '2025-11-08', '2025-12-08', '2026-01-08', '2026-02-08'] | ['13660', '13660', '13660', '13660', '13660'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | groceries | Bulk pantry shop | debit | INR | ['event_1479', 'event_1482'] | ['2025-09-12', '2025-10-03'] | ['7679.25', '7187.32'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_17 | groceries | Fresh food shop | debit | INR | ['event_1483', 'event_1486', 'event_1487', 'event_1489', 'event_1500'] | ['2025-10-10', '2025-10-31', '2025-11-07', '2025-11-21', '2026-02-06'] | ['8574.98', '7585.37', '7446.25', '8500.09', '11342.57'] | [21, 7, 14, 77] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | groceries | Grocery delivery | debit | INR | ['event_1480', 'event_1488', 'event_1502'] | ['2025-09-19', '2025-11-14', '2026-02-20'] | ['10039.54', '10300.07', '8543.01'] | [56, 98] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_17 | groceries | Local market purchase | debit | INR | ['event_1484', 'event_1485', 'event_1490', 'event_1491', 'event_1492', 'event_1494', 'event_1496', 'event_1497', 'event_1499'] | ['2025-10-17', '2025-10-24', '2025-11-28', '2025-12-05', '2025-12-12', '2025-12-26', '2026-01-09', '2026-01-16', '2026-01-30'] | ['11380.46', '6706.54', '7237.45', '8836.99', '10690', '11392.07', '11433.33', '7093.83', '8581.99'] | [7, 35, 7, 7, 14, 14, 7, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | groceries | Neighbourhood grocer | debit | INR | ['event_1478', 'event_1481'] | ['2025-09-05', '2025-09-26'] | ['9392.54', '9785.51'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_17 | groceries | Supermarket basket | debit | INR | ['event_1501', 'event_1503'] | ['2026-02-13', '2026-02-27'] | ['10873.47', '8716.51'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_17 | groceries | Weekly produce market | debit | INR | ['event_1493', 'event_1498'] | ['2025-12-19', '2026-01-23'] | ['10432.03', '8638.54'] | [35] | ['fixed'] | ['settled', 'settled'] |
| user_17 | music_subscription | Music subscription | debit | INR | ['event_1448', 'event_1455', 'event_1462', 'event_1469', 'event_1476'] | ['2025-10-11', '2025-11-11', '2025-12-11', '2026-01-11', '2026-02-11'] | ['2055', '2055', '2055', '2055', '2055'] | [31, 30, 31, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | rent | Apartment rent transfer | debit | INR | ['event_1444', 'event_1451', 'event_1458', 'event_1465', 'event_1472'] | ['2025-10-02', '2025-11-02', '2025-12-02', '2026-01-02', '2026-02-02'] | ['49600', '49600', '49600', '49600', '49600'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | salary | Payroll credit | credit | INR | ['event_1443', 'event_1450', 'event_1457', 'event_1464', 'event_1471'] | ['2025-10-15', '2025-11-15', '2025-12-15', '2026-01-15', '2026-02-15'] | ['206000', '206000', '206000', '206000', '206000'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | transport | Commuter pass | debit | INR | ['event_1509', 'event_1510', 'event_1528'] | ['2025-10-11', '2025-10-18', '2026-02-21'] | ['6225.69', '5386.34', '5741.08'] | [7, 126] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_17 | transport | Local taxi | debit | INR | ['event_1507', 'event_1508', 'event_1512', 'event_1513', 'event_1525'] | ['2025-09-27', '2025-10-04', '2025-11-01', '2025-11-08', '2026-01-31'] | ['5639.47', '4445.42', '5936.87', '6420.35', '4661.7'] | [7, 28, 7, 84] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | transport | Metro and bus fares | debit | INR | ['event_1517', 'event_1518', 'event_1520', 'event_1521', 'event_1526'] | ['2025-12-06', '2025-12-13', '2025-12-27', '2026-01-03', '2026-02-07'] | ['6170.7', '5790.36', '5080.56', '4844.94', '5650.43'] | [7, 14, 7, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | transport | Rail pass | debit | INR | ['event_1504', 'event_1514', 'event_1523', 'event_1524', 'event_1529'] | ['2025-09-06', '2025-11-15', '2026-01-17', '2026-01-24', '2026-02-28'] | ['3913.59', '4008.13', '6406.38', '5758.89', '5372.15'] | [70, 63, 7, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_17 | transport | Ride-hailing trip | debit | INR | ['event_1511', 'event_1515', 'event_1522'] | ['2025-10-25', '2025-11-22', '2026-01-10'] | ['5421.55', '5126.25', '5940.36'] | [28, 49] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_17 | transport | Vehicle charging | debit | INR | ['event_1516', 'event_1519', 'event_1527'] | ['2025-11-29', '2025-12-20', '2026-02-14'] | ['5036.82', '4328.91', '3902.91'] | [21, 56] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_17 | utilities | Municipal utilities | debit | INR | ['event_1445', 'event_1452', 'event_1459', 'event_1466', 'event_1473'] | ['2025-10-06', '2025-11-06', '2025-12-06', '2026-01-06', '2026-02-06'] | ['9481.13', '9530.77', '10246.53', '9948.15', '8487.15'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | dining | Coffee shop | debit | EUR | ['event_1610', 'event_1615', 'event_1617'] | ['2026-01-28', '2026-04-08', '2026-05-06'] | ['69.84', '66.71', '81.05'] | [70, 28] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_18 | dining | Lunch with colleagues | debit | EUR | ['event_1612', 'event_1620'] | ['2026-02-25', '2026-06-17'] | ['98.51', '82.67'] | [112] | ['reducible'] | ['settled', 'settled'] |
| user_18 | dining | Neighbourhood restaurant | debit | EUR | ['event_1611', 'event_1614'] | ['2026-02-11', '2026-03-25'] | ['92.92', '75.46'] | [42] | ['reducible'] | ['settled', 'settled'] |
| user_18 | dining | Quick-service meal | debit | EUR | ['event_1609', 'event_1613', 'event_1619'] | ['2026-01-14', '2026-03-11', '2026-06-03'] | ['66.7', '108.96', '62.87'] | [56, 84] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_18 | groceries | Bulk pantry shop | debit | EUR | ['event_1578', 'event_1590', 'event_1592'] | ['2026-01-12', '2026-05-12', '2026-06-01'] | ['64.84', '83.94', '71.92'] | [120, 20] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_18 | groceries | Grocery delivery | debit | EUR | ['event_1579', 'event_1583'] | ['2026-01-22', '2026-03-03'] | ['101.66', '106.43'] | [40] | ['fixed'] | ['settled', 'settled'] |
| user_18 | groceries | Household groceries | debit | EUR | ['event_1589', 'event_1594'] | ['2026-05-02', '2026-06-21'] | ['115', '90.08'] | [50] | ['fixed'] | ['settled', 'settled'] |
| user_18 | groceries | Local market purchase | debit | EUR | ['event_1580', 'event_1585', 'event_1587'] | ['2026-02-01', '2026-03-23', '2026-04-12'] | ['96.63', '108.09', '82.18'] | [50, 20] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_18 | groceries | Supermarket basket | debit | EUR | ['event_1581', 'event_1584', 'event_1588', 'event_1593', 'event_1595'] | ['2026-02-11', '2026-03-13', '2026-04-22', '2026-06-11', '2026-07-01'] | ['101.08', '66.3', '94.02', '101.9', '111.41'] | [30, 40, 50, 20] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | groceries | Weekly produce market | debit | EUR | ['event_1586', 'event_1591'] | ['2026-04-02', '2026-05-22'] | ['110.8', '87.91'] | [50] | ['fixed'] | ['settled', 'settled'] |
| user_18 | healthcare | Clinic payment | debit | EUR | ['event_1551', 'event_1557', 'event_1563', 'event_1569', 'event_1575'] | ['2026-02-11', '2026-03-11', '2026-04-11', '2026-05-11', '2026-06-11'] | ['164.1', '150.18', '152.41', '162.41', '147.96'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | housing | Building maintenance payment | debit | EUR | ['event_1548', 'event_1554', 'event_1560', 'event_1566', 'event_1572', 'event_1577'] | ['2026-02-04', '2026-03-04', '2026-04-04', '2026-05-04', '2026-06-04', '2026-07-04'] | ['167', '167', '167', '167', '167', '167'] | [28, 31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | insurance | Household insurance | debit | EUR | ['event_1550', 'event_1556', 'event_1562', 'event_1568', 'event_1574'] | ['2026-02-08', '2026-03-08', '2026-04-08', '2026-05-08', '2026-06-08'] | ['68', '68', '68', '68', '68'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | salary | Payroll credit | credit | EUR | ['event_1547', 'event_1553', 'event_1559', 'event_1565', 'event_1571'] | ['2026-02-15', '2026-03-15', '2026-04-15', '2026-05-15', '2026-06-15'] | ['2310', '2310', '2310', '2310', '2310'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | streaming | Family streaming plan | debit | EUR | ['event_1552', 'event_1558', 'event_1564', 'event_1570', 'event_1576'] | ['2026-02-10', '2026-03-10', '2026-04-10', '2026-05-10', '2026-06-10'] | ['68', '68', '68', '68', '68'] | [28, 31, 30, 31] | ['reducible_or_stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | transport | Metro and bus fares | debit | EUR | ['event_1596', 'event_1608'] | ['2026-01-13', '2026-06-30'] | ['36.86', '43.81'] | [168] | ['fixed'] | ['settled', 'settled'] |
| user_18 | transport | Vehicle charging | debit | EUR | ['event_1598', 'event_1601', 'event_1603', 'event_1604', 'event_1606'] | ['2026-02-10', '2026-03-24', '2026-04-21', '2026-05-05', '2026-06-02'] | ['54.53', '52.9', '47.5', '50.57', '36.29'] | [42, 28, 14, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_18 | utilities | Energy provider bill | debit | EUR | ['event_1549', 'event_1555', 'event_1561', 'event_1567', 'event_1573'] | ['2026-02-07', '2026-03-07', '2026-04-07', '2026-05-07', '2026-06-07'] | ['100.59', '101.24', '125.4', '121.67', '107.43'] | [28, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | cloud_storage | Online backup subscription | debit | INR | ['event_1628', 'event_1636', 'event_1644', 'event_1652', 'event_1660'] | ['2024-04-14', '2024-05-14', '2024-06-14', '2024-07-14', '2024-08-14'] | ['395', '395', '395', '395', '395'] | [30, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | debt_repayment | Loan repayment | debit | INR | ['event_1625', 'event_1633', 'event_1641', 'event_1649', 'event_1657'] | ['2024-04-13', '2024-05-13', '2024-06-13', '2024-07-13', '2024-08-13'] | ['11850', '11850', '11850', '11850', '11850'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | family_support | Childcare contribution | debit | INR | ['event_1627', 'event_1635', 'event_1643', 'event_1651', 'event_1659'] | ['2024-04-15', '2024-05-15', '2024-06-15', '2024-07-15', '2024-08-15'] | ['12650', '12650', '12650', '12650', '12650'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | groceries | Bulk pantry shop | debit | INR | ['event_1672', 'event_1673', 'event_1674', 'event_1678', 'event_1681'] | ['2024-05-22', '2024-05-29', '2024-06-05', '2024-07-03', '2024-07-24'] | ['5406.2', '5542.84', '4738.95', '4444.74', '5184.21'] | [7, 7, 28, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | groceries | Fresh food shop | debit | INR | ['event_1664', 'event_1668', 'event_1671'] | ['2024-03-27', '2024-04-24', '2024-05-15'] | ['6070.85', '4056.71', '3852.58'] | [28, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_19 | groceries | Grocery delivery | debit | INR | ['event_1669', 'event_1670', 'event_1676'] | ['2024-05-01', '2024-05-08', '2024-06-19'] | ['4744.13', '3593.25', '5146.94'] | [7, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_19 | groceries | Household groceries | debit | INR | ['event_1675', 'event_1680'] | ['2024-06-12', '2024-07-17'] | ['3575.19', '4493.39'] | [35] | ['fixed'] | ['settled', 'settled'] |
| user_19 | groceries | Local market purchase | debit | INR | ['event_1662', 'event_1665', 'event_1677', 'event_1679', 'event_1682', 'event_1686'] | ['2024-03-13', '2024-04-03', '2024-06-26', '2024-07-10', '2024-07-31', '2024-08-28'] | ['4418.91', '5452.26', '5908.15', '4667.68', '3460.53', '4068.18'] | [21, 84, 14, 21, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | groceries | Neighbourhood grocer | debit | INR | ['event_1663', 'event_1667'] | ['2024-03-20', '2024-04-17'] | ['4871.72', '3877.79'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_19 | groceries | Supermarket basket | debit | INR | ['event_1666', 'event_1684'] | ['2024-04-10', '2024-08-14'] | ['5912.83', '4963.39'] | [126] | ['fixed'] | ['settled', 'settled'] |
| user_19 | groceries | Weekly produce market | debit | INR | ['event_1683', 'event_1685'] | ['2024-08-07', '2024-08-21'] | ['6005.09', '4864.04'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_19 | healthcare | Clinic payment | debit | INR | ['event_1626', 'event_1634', 'event_1642', 'event_1650', 'event_1658'] | ['2024-04-12', '2024-05-12', '2024-06-12', '2024-07-12', '2024-08-12'] | ['8946.09', '9619.88', '8335.2', '8496.34', '8645.36'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | rent | Residential rent payment | debit | INR | ['event_1623', 'event_1631', 'event_1639', 'event_1647', 'event_1655'] | ['2024-04-04', '2024-05-04', '2024-06-04', '2024-07-04', '2024-08-04'] | ['36100', '36100', '36100', '36100', '36100'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | salary | Payroll credit | credit | INR | ['event_1622', 'event_1630', 'event_1638', 'event_1646', 'event_1654'] | ['2024-04-15', '2024-05-15', '2024-06-15', '2024-07-15', '2024-08-15'] | ['131000', '131000', '131000', '131000', '131000'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | shopping | Clothing and household items | debit | INR | ['event_1629', 'event_1637', 'event_1645', 'event_1653', 'event_1661'] | ['2024-04-14', '2024-05-14', '2024-06-14', '2024-07-14', '2024-08-14'] | ['6302.66', '5593.2', '6069.58', '5772.78', '5431.12'] | [30, 31, 30, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_19 | transport | Fuel refill | debit | INR | ['event_1687', 'event_1691', 'event_1699'] | ['2024-03-14', '2024-05-09', '2024-08-29'] | ['3054.24', '2640.96', '2765.93'] | [56, 112] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_19 | transport | Local taxi | debit | INR | ['event_1693', 'event_1697', 'event_1698'] | ['2024-06-06', '2024-08-01', '2024-08-15'] | ['2610.24', '2759.93', '2462.29'] | [56, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_19 | transport | Parking and tolls | debit | INR | ['event_1689', 'event_1696'] | ['2024-04-11', '2024-07-18'] | ['3476.92', '3659.94'] | [98] | ['fixed'] | ['settled', 'settled'] |
| user_19 | transport | Rail pass | debit | INR | ['event_1692', 'event_1694'] | ['2024-05-23', '2024-06-20'] | ['3432.81', '2788.22'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_19 | transport | Ride-hailing trip | debit | INR | ['event_1688', 'event_1690'] | ['2024-03-28', '2024-04-25'] | ['3298.25', '3849.5'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_19 | utilities | Municipal utilities | debit | INR | ['event_1624', 'event_1632', 'event_1640', 'event_1648', 'event_1656'] | ['2024-04-08', '2024-05-08', '2024-06-08', '2024-07-08', '2024-08-08'] | ['6141.28', '5525.82', '6029.9', '5951.99', '6129.19'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | cloud_storage | Shared storage plan | debit | INR | ['event_1708', 'event_1716', 'event_1724', 'event_1732', 'event_1740'] | ['2025-09-11', '2025-10-11', '2025-11-11', '2025-12-11', '2026-01-11'] | ['365', '365', '365', '365', '365'] | [30, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | dining | Bakery and snacks | debit | INR | ['event_1777', 'event_1781', 'event_1783'] | ['2025-09-26', '2025-12-19', '2026-01-30'] | ['3365.58', '2629.91', '3803.95'] | [84, 42] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_20 | dining | Takeaway order | debit | INR | ['event_1775', 'event_1779'] | ['2025-08-15', '2025-11-07'] | ['3150.77', '2857.78'] | [84] | ['reducible'] | ['settled', 'settled'] |
| user_20 | education | School fee payment | debit | INR | ['event_1705', 'event_1713', 'event_1721', 'event_1729', 'event_1737'] | ['2025-09-07', '2025-10-07', '2025-11-07', '2025-12-07', '2026-01-07'] | ['8740', '8740', '8740', '8740', '8740'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | entertainment | Cinema and events | debit | INR | ['event_1707', 'event_1715', 'event_1723', 'event_1731', 'event_1739'] | ['2025-09-13', '2025-10-13', '2025-11-13', '2025-12-13', '2026-01-13'] | ['2298.76', '2279.67', '2115.92', '1949.86', '2097.15'] | [30, 31, 30, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | groceries | Bulk pantry shop | debit | INR | ['event_1747', 'event_1754'] | ['2025-09-12', '2025-11-21'] | ['4104.17', '3796.24'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_20 | groceries | Grocery delivery | debit | INR | ['event_1744', 'event_1746', 'event_1753', 'event_1760'] | ['2025-08-13', '2025-09-02', '2025-11-11', '2026-01-20'] | ['3866.5', '3127.16', '3386.09', '3702.16'] | [20, 70, 70] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_20 | groceries | Household groceries | debit | INR | ['event_1749', 'event_1752', 'event_1755', 'event_1761'] | ['2025-10-02', '2025-11-01', '2025-12-01', '2026-01-30'] | ['4660.33', '3525.04', '3016.03', '4719.22'] | [30, 30, 60] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_20 | groceries | Local market purchase | debit | INR | ['event_1757', 'event_1758'] | ['2025-12-21', '2025-12-31'] | ['3067.82', '3588.1'] | [10] | ['fixed'] | ['settled', 'settled'] |
| user_20 | groceries | Supermarket basket | debit | INR | ['event_1745', 'event_1750'] | ['2025-08-23', '2025-10-12'] | ['3724.49', '4109.13'] | [50] | ['fixed'] | ['settled', 'settled'] |
| user_20 | groceries | Weekly produce market | debit | INR | ['event_1748', 'event_1751', 'event_1756'] | ['2025-09-22', '2025-10-22', '2025-12-11'] | ['2968.61', '2812.26', '4683.37'] | [30, 50] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_20 | healthcare | Family healthcare expense | debit | INR | ['event_1706', 'event_1714', 'event_1722', 'event_1730', 'event_1738'] | ['2025-09-09', '2025-10-09', '2025-11-09', '2025-12-09', '2026-01-09'] | ['5968.18', '6648.5', '5907.73', '6505.49', '6654.33'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | housing | Home association fee | debit | INR | ['event_1702', 'event_1710', 'event_1718', 'event_1726', 'event_1734', 'event_1741'] | ['2025-09-02', '2025-10-02', '2025-11-02', '2025-12-02', '2026-01-02', '2026-02-02'] | ['7950', '7950', '7950', '7950', '7950', '7950'] | [30, 31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | insurance | Household insurance | debit | INR | ['event_1704', 'event_1712', 'event_1720', 'event_1728', 'event_1736', 'event_1743'] | ['2025-09-06', '2025-10-06', '2025-11-06', '2025-12-06', '2026-01-06', '2026-02-06'] | ['3290', '3290', '3290', '3290', '3290', '3290'] | [30, 31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | salary | Payroll credit | credit | INR | ['event_1701', 'event_1709', 'event_1717', 'event_1725', 'event_1733'] | ['2025-09-15', '2025-10-15', '2025-11-15', '2025-12-15', '2026-01-15'] | ['108000', '108000', '108000', '108000', '108000'] | [30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_20 | transport | Fuel refill | debit | INR | ['event_1772', 'event_1773'] | ['2026-01-01', '2026-01-15'] | ['2838.14', '3150.25'] | [14] | ['fixed'] | ['settled', 'settled'] |
| user_20 | transport | Metro and bus fares | debit | INR | ['event_1767', 'event_1771', 'event_1774'] | ['2025-10-23', '2025-12-18', '2026-01-29'] | ['2359.03', '3145.95', '3243.84'] | [56, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_20 | transport | Vehicle charging | debit | INR | ['event_1762', 'event_1764', 'event_1765'] | ['2025-08-14', '2025-09-11', '2025-09-25'] | ['2046.25', '2195.41', '2632'] | [28, 14] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_20 | utilities | Municipal utilities | debit | INR | ['event_1703', 'event_1711', 'event_1719', 'event_1727', 'event_1735', 'event_1742'] | ['2025-09-05', '2025-10-05', '2025-11-05', '2025-12-05', '2026-01-05', '2026-02-05'] | ['7784.29', '7977.68', '8058.75', '6848.62', '7551.74', '7769.87'] | [30, 31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_21 | cloud_storage | Online backup subscription | debit | USD | ['event_1791', 'event_1797', 'event_1803', 'event_1809', 'event_1815'] | ['2025-11-12', '2025-12-12', '2026-01-12', '2026-02-12', '2026-03-12'] | ['11', '11', '11', '11', '11'] | [30, 31, 31, 28] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_21 | dining | Bakery and snacks | debit | USD | ['event_1849', 'event_1851'] | ['2025-12-12', '2026-01-23'] | ['60.18', '100.63'] | [42] | ['reducible'] | ['settled', 'settled'] |
| user_21 | dining | Neighbourhood restaurant | debit | USD | ['event_1853', 'event_1854'] | ['2026-03-06', '2026-03-27'] | ['98.39', '69.31'] | [21] | ['reducible'] | ['settled', 'settled'] |
| user_21 | dining | Quick-service meal | debit | USD | ['event_1847', 'event_1850'] | ['2025-10-31', '2026-01-02'] | ['68.28', '88.07'] | [63] | ['reducible'] | ['settled', 'settled'] |
| user_21 | dining | Takeaway order | debit | USD | ['event_1846', 'event_1852'] | ['2025-10-10', '2026-02-13'] | ['82.43', '97.67'] | [126] | ['reducible'] | ['settled', 'settled'] |
| user_21 | groceries | Bulk pantry shop | debit | USD | ['event_1819', 'event_1830'] | ['2025-10-08', '2026-01-26'] | ['65.93', '66.13'] | [110] | ['fixed'] | ['settled', 'settled'] |
| user_21 | groceries | Fresh food shop | debit | USD | ['event_1822', 'event_1825', 'event_1832', 'event_1835'] | ['2025-11-07', '2025-12-07', '2026-02-15', '2026-03-17'] | ['68.82', '72.06', '90.57', '77.75'] | [30, 70, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_21 | groceries | Household groceries | debit | USD | ['event_1823', 'event_1829', 'event_1834'] | ['2025-11-17', '2026-01-16', '2026-03-07'] | ['95.62', '79', '70.98'] | [60, 50] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_21 | groceries | Local market purchase | debit | USD | ['event_1828', 'event_1833', 'event_1836'] | ['2026-01-06', '2026-02-25', '2026-03-27'] | ['77.2', '71.22', '97.55'] | [50, 30] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_21 | groceries | Supermarket basket | debit | USD | ['event_1820', 'event_1826'] | ['2025-10-18', '2025-12-17'] | ['104.23', '101.34'] | [60] | ['fixed'] | ['settled', 'settled'] |
| user_21 | groceries | Weekly produce market | debit | USD | ['event_1821', 'event_1824', 'event_1827', 'event_1831'] | ['2025-10-28', '2025-11-27', '2025-12-27', '2026-02-05'] | ['92.12', '104.19', '84.7', '85.9'] | [30, 30, 40] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_21 | rent | Residential rent payment | debit | USD | ['event_1789', 'event_1795', 'event_1801', 'event_1807', 'event_1813', 'event_1818'] | ['2025-11-02', '2025-12-02', '2026-01-02', '2026-02-02', '2026-03-02', '2026-04-02'] | ['718.8', '718.8', '718.8', '718.8', '718.8', '718.8'] | [30, 31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_21 | salary | Payroll credit | credit | USD | ['event_1788', 'event_1794', 'event_1800', 'event_1806', 'event_1812'] | ['2025-11-15', '2025-12-15', '2026-01-15', '2026-02-15', '2026-03-15'] | ['2256', '2256', '2256', '2256', '2256'] | [30, 31, 31, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_21 | shopping | Monthly shopping spend | debit | USD | ['event_1793', 'event_1799', 'event_1805', 'event_1811', 'event_1817'] | ['2025-11-12', '2025-12-12', '2026-01-12', '2026-02-12', '2026-03-12'] | ['133.38', '115.86', '120.74', '115.71', '126.38'] | [30, 31, 31, 28] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_21 | streaming | Streaming subscription | debit | USD | ['event_1792', 'event_1798', 'event_1804', 'event_1810', 'event_1816'] | ['2025-11-09', '2025-12-09', '2026-01-09', '2026-02-09', '2026-03-09'] | ['47', '47', '47', '47', '47'] | [30, 31, 31, 28] | ['reducible_or_stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_21 | transport | Local taxi | debit | USD | ['event_1841', 'event_1844'] | ['2026-01-01', '2026-03-05'] | ['40.66', '47.84'] | [63] | ['fixed'] | ['settled', 'settled'] |
| user_21 | transport | Parking and tolls | debit | USD | ['event_1842', 'event_1843'] | ['2026-01-22', '2026-02-12'] | ['33.38', '51.42'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_21 | transport | Rail pass | debit | USD | ['event_1839', 'event_1845'] | ['2025-11-20', '2026-03-26'] | ['34.52', '36.86'] | [126] | ['fixed'] | ['settled', 'settled'] |
| user_21 | utilities | Municipal utilities | debit | USD | ['event_1790', 'event_1796', 'event_1802', 'event_1808', 'event_1814'] | ['2025-11-06', '2025-12-06', '2026-01-06', '2026-02-06', '2026-03-06'] | ['115.31', '123.72', '120.59', '122.18', '124.08'] | [30, 31, 31, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | delivery_membership | Food delivery membership | debit | EUR | ['event_1863', 'event_1870', 'event_1877', 'event_1884', 'event_1891'] | ['2024-07-14', '2024-08-14', '2024-09-14', '2024-10-14', '2024-11-14'] | ['5', '5', '5', '5', '5'] | [31, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | dining | Coffee shop | debit | EUR | ['event_1948', 'event_1950', 'event_1956'] | ['2024-07-12', '2024-08-09', '2024-11-01'] | ['13.59', '20.85', '12.65'] | [28, 84] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_22 | dining | Family dinner | debit | EUR | ['event_1949', 'event_1954'] | ['2024-07-26', '2024-10-04'] | ['14.46', '14.22'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_22 | dining | Neighbourhood restaurant | debit | EUR | ['event_1947', 'event_1952'] | ['2024-06-28', '2024-09-06'] | ['18.82', '17.66'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_22 | dining | Quick-service meal | debit | EUR | ['event_1946', 'event_1951'] | ['2024-06-14', '2024-08-23'] | ['12.25', '15.63'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_22 | dining | Takeaway order | debit | EUR | ['event_1953', 'event_1958'] | ['2024-09-20', '2024-11-29'] | ['16.03', '18.41'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_22 | dining | Weekend food delivery | debit | EUR | ['event_1955', 'event_1957'] | ['2024-10-18', '2024-11-15'] | ['18.53', '15.84'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_22 | entertainment | Weekend entertainment | debit | EUR | ['event_1865', 'event_1872', 'event_1879', 'event_1886', 'event_1893'] | ['2024-07-15', '2024-08-15', '2024-09-15', '2024-10-15', '2024-11-15'] | ['19.64', '18.94', '23.29', '22.03', '20.43'] | [31, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | groceries | Bulk pantry shop | debit | EUR | ['event_1900', 'event_1902', 'event_1907', 'event_1909', 'event_1915', 'event_1918'] | ['2024-07-17', '2024-07-31', '2024-09-04', '2024-09-18', '2024-10-30', '2024-11-20'] | ['28.31', '25.75', '23.02', '22.14', '29.81', '18.6'] | [14, 35, 14, 42, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | groceries | Fresh food shop | debit | EUR | ['event_1896', 'event_1901', 'event_1912', 'event_1920'] | ['2024-06-19', '2024-07-24', '2024-10-09', '2024-12-04'] | ['29.03', '22.88', '27.59', '26.82'] | [35, 77, 56] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_22 | groceries | Grocery delivery | debit | EUR | ['event_1914', 'event_1917'] | ['2024-10-23', '2024-11-13'] | ['21.58', '18.71'] | [21] | ['fixed'] | ['settled', 'settled'] |
| user_22 | groceries | Household groceries | debit | EUR | ['event_1903', 'event_1919'] | ['2024-08-07', '2024-11-27'] | ['20.5', '18.35'] | [112] | ['fixed'] | ['settled', 'settled'] |
| user_22 | groceries | Local market purchase | debit | EUR | ['event_1897', 'event_1906'] | ['2024-06-26', '2024-08-28'] | ['22.38', '23.84'] | [63] | ['fixed'] | ['settled', 'settled'] |
| user_22 | groceries | Neighbourhood grocer | debit | EUR | ['event_1908', 'event_1910', 'event_1913'] | ['2024-09-11', '2024-09-25', '2024-10-16'] | ['28.46', '19.54', '23.94'] | [14, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_22 | groceries | Supermarket basket | debit | EUR | ['event_1895', 'event_1898', 'event_1899', 'event_1904', 'event_1916'] | ['2024-06-12', '2024-07-03', '2024-07-10', '2024-08-14', '2024-11-06'] | ['23.95', '20.6', '26.47', '22.19', '27.33'] | [21, 7, 35, 84] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | groceries | Weekly produce market | debit | EUR | ['event_1905', 'event_1911'] | ['2024-08-21', '2024-10-02'] | ['21.76', '29.25'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_22 | gym | Gym membership | debit | EUR | ['event_1864', 'event_1871', 'event_1878', 'event_1885', 'event_1892'] | ['2024-07-11', '2024-08-11', '2024-09-11', '2024-10-11', '2024-11-11'] | ['17', '17', '17', '17', '17'] | [31, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | music_subscription | Music service subscription | debit | EUR | ['event_1862', 'event_1869', 'event_1876', 'event_1883', 'event_1890'] | ['2024-07-12', '2024-08-12', '2024-09-12', '2024-10-12', '2024-11-12'] | ['6', '6', '6', '6', '6'] | [31, 31, 30, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | rent | Apartment rent transfer | debit | EUR | ['event_1860', 'event_1867', 'event_1874', 'event_1881', 'event_1888', 'event_1894'] | ['2024-07-03', '2024-08-03', '2024-09-03', '2024-10-03', '2024-11-03', '2024-12-03'] | ['178.2', '178.2', '178.2', '178.2', '178.2', '178.2'] | [31, 31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | salary | Payroll credit | credit | EUR | ['event_1859', 'event_1866', 'event_1873', 'event_1880', 'event_1887'] | ['2024-07-15', '2024-08-15', '2024-09-15', '2024-10-15', '2024-11-15'] | ['616', '616', '616', '616', '616'] | [31, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | transport | Commuter pass | debit | EUR | ['event_1922', 'event_1926', 'event_1931'] | ['2024-06-20', '2024-07-18', '2024-08-22'] | ['11.63', '12.7', '10.72'] | [28, 35] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_22 | transport | Fuel refill | debit | EUR | ['event_1924', 'event_1925', 'event_1929', 'event_1939'] | ['2024-07-04', '2024-07-11', '2024-08-08', '2024-10-17'] | ['10.38', '12.33', '9.7', '15.93'] | [7, 28, 70] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_22 | transport | Local taxi | debit | EUR | ['event_1927', 'event_1930', 'event_1935', 'event_1942'] | ['2024-07-25', '2024-08-15', '2024-09-19', '2024-11-07'] | ['12.95', '10.41', '10.09', '14.93'] | [21, 35, 49] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_22 | transport | Metro and bus fares | debit | EUR | ['event_1923', 'event_1934', 'event_1938', 'event_1945'] | ['2024-06-27', '2024-09-12', '2024-10-10', '2024-11-28'] | ['16.34', '15.34', '9.9', '15.02'] | [77, 28, 49] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_22 | transport | Rail pass | debit | EUR | ['event_1928', 'event_1933', 'event_1944'] | ['2024-08-01', '2024-09-05', '2024-11-21'] | ['12.59', '12.65', '15.87'] | [35, 77] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_22 | transport | Ride-hailing trip | debit | EUR | ['event_1921', 'event_1936', 'event_1937', 'event_1940', 'event_1943'] | ['2024-06-13', '2024-09-26', '2024-10-03', '2024-10-24', '2024-11-14'] | ['16.09', '15.68', '13.05', '15.08', '11.44'] | [105, 7, 21, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_22 | utilities | Electricity and water bill | debit | EUR | ['event_1861', 'event_1868', 'event_1875', 'event_1882', 'event_1889'] | ['2024-07-07', '2024-08-07', '2024-09-07', '2024-10-07', '2024-11-07'] | ['32.53', '33.73', '31.52', '27.68', '27.34'] | [31, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | cloud_storage | Cloud storage plan | debit | ZAR | ['event_1968', 'event_1976', 'event_1984', 'event_1992', 'event_2000'] | ['2024-12-14', '2025-01-14', '2025-02-14', '2025-03-14', '2025-04-14'] | ['295.9', '295.9', '295.9', '295.9', '295.9'] | [31, 31, 28, 31] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | debt_repayment | Education loan instalment | debit | ZAR | ['event_1965', 'event_1973', 'event_1981', 'event_1989', 'event_1997'] | ['2024-12-13', '2025-01-13', '2025-02-13', '2025-03-13', '2025-04-13'] | ['5852', '5852', '5852', '5852', '5852'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | family_support | Childcare contribution | debit | ZAR | ['event_1967', 'event_1975', 'event_1983', 'event_1991', 'event_1999'] | ['2024-12-15', '2025-01-15', '2025-02-15', '2025-03-15', '2025-04-15'] | ['4270.2', '4270.2', '4270.2', '4270.2', '4270.2'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | groceries | Bulk pantry shop | debit | ZAR | ['event_2013', 'event_2023', 'event_2024'] | ['2025-01-22', '2025-04-02', '2025-04-09'] | ['1544.99', '1487.69', '1794.76'] | [70, 7] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_23 | groceries | Grocery delivery | debit | ZAR | ['event_2003', 'event_2009', 'event_2012', 'event_2017', 'event_2018'] | ['2024-11-13', '2024-12-25', '2025-01-15', '2025-02-19', '2025-02-26'] | ['1401.85', '1981.14', '2125.65', '2186.26', '2146.88'] | [42, 21, 35, 7] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | groceries | Household groceries | debit | ZAR | ['event_2004', 'event_2011', 'event_2022', 'event_2026'] | ['2024-11-20', '2025-01-08', '2025-03-26', '2025-04-23'] | ['1332.28', '1927.69', '1706.85', '1514.83'] | [49, 77, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_23 | groceries | Local market purchase | debit | ZAR | ['event_2005', 'event_2015'] | ['2024-11-27', '2025-02-05'] | ['1586.85', '1421.88'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_23 | groceries | Neighbourhood grocer | debit | ZAR | ['event_2007', 'event_2014', 'event_2020', 'event_2025', 'event_2027'] | ['2024-12-11', '2025-01-29', '2025-03-12', '2025-04-16', '2025-04-30'] | ['1821.15', '1914.51', '2074.73', '1678.37', '1257.56'] | [49, 42, 35, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | groceries | Supermarket basket | debit | ZAR | ['event_2006', 'event_2008', 'event_2019', 'event_2021'] | ['2024-12-04', '2024-12-18', '2025-03-05', '2025-03-19'] | ['1372.64', '2207.92', '1717.87', '1372.44'] | [14, 77, 14] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_23 | groceries | Weekly produce market | debit | ZAR | ['event_2010', 'event_2016'] | ['2025-01-01', '2025-02-12'] | ['2178.52', '1556.59'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_23 | healthcare | Clinic payment | debit | ZAR | ['event_1966', 'event_1974', 'event_1982', 'event_1990', 'event_1998'] | ['2024-12-12', '2025-01-12', '2025-02-12', '2025-03-12', '2025-04-12'] | ['1341.05', '1331.22', '1439.91', '1317.68', '1377.89'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | rent | Shared housing rent | debit | ZAR | ['event_1963', 'event_1971', 'event_1979', 'event_1987', 'event_1995', 'event_2002'] | ['2024-12-04', '2025-01-04', '2025-02-04', '2025-03-04', '2025-04-04', '2025-05-04'] | ['15312', '15312', '15312', '15312', '15312', '15312'] | [31, 31, 28, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | salary | Payroll credit | credit | ZAR | ['event_1962', 'event_1970', 'event_1978', 'event_1986', 'event_1994'] | ['2024-12-15', '2025-01-15', '2025-02-15', '2025-03-15', '2025-04-15'] | ['45760', '45760', '45760', '45760', '45760'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | shopping | Personal shopping | debit | ZAR | ['event_1969', 'event_1977', 'event_1985', 'event_1993', 'event_2001'] | ['2024-12-14', '2025-01-14', '2025-02-14', '2025-03-14', '2025-04-14'] | ['1279.39', '1396.33', '1389.39', '1232.23', '1281.33'] | [31, 31, 28, 31] | ['reducible'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_23 | transport | Commuter pass | debit | ZAR | ['event_2034', 'event_2037'] | ['2025-02-06', '2025-03-20'] | ['968.71', '956.01'] | [42] | ['fixed'] | ['settled', 'settled'] |
| user_23 | transport | Metro and bus fares | debit | ZAR | ['event_2029', 'event_2032', 'event_2035', 'event_2040'] | ['2024-11-28', '2025-01-09', '2025-02-20', '2025-05-01'] | ['1121.5', '896.02', '1046.56', '783.18'] | [42, 42, 70] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_23 | transport | Parking and tolls | debit | ZAR | ['event_2030', 'event_2036', 'event_2039'] | ['2024-12-12', '2025-03-06', '2025-04-17'] | ['747.69', '738.21', '834'] | [84, 42] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_23 | transport | Ride-hailing trip | debit | ZAR | ['event_2033', 'event_2038'] | ['2025-01-23', '2025-04-03'] | ['904.55', '1092.98'] | [70] | ['fixed'] | ['settled', 'settled'] |
| user_23 | utilities | Electricity bill | debit | ZAR | ['event_1964', 'event_1972', 'event_1980', 'event_1988', 'event_1996'] | ['2024-12-08', '2025-01-08', '2025-02-08', '2025-03-08', '2025-04-08'] | ['2877.85', '2484.32', '2915.67', '2813.94', '2680.15'] | [31, 31, 28, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | cloud_storage | Online backup subscription | debit | INR | ['event_2047', 'event_2055', 'event_2063', 'event_2071', 'event_2079'] | ['2025-08-11', '2025-09-11', '2025-10-11', '2025-11-11', '2025-12-11'] | ['355', '355', '355', '355', '355'] | [31, 30, 31, 30] | ['stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | dining | Bakery and snacks | debit | INR | ['event_2139', 'event_2150'] | ['2025-07-19', '2025-10-04'] | ['1886.97', '1985.64'] | [77] | ['reducible'] | ['settled', 'settled'] |
| user_24 | dining | Coffee shop | debit | INR | ['event_2146', 'event_2147', 'event_2148', 'event_2155'] | ['2025-09-06', '2025-09-13', '2025-09-20', '2025-11-08'] | ['2288.09', '1893.38', '1783.1', '1423.26'] | [7, 7, 49] | ['reducible'] | ['settled', 'settled', 'settled', 'settled'] |
| user_24 | dining | Family dinner | debit | INR | ['event_2153', 'event_2157', 'event_2162'] | ['2025-10-25', '2025-11-22', '2025-12-27'] | ['1942.46', '1345.87', '2151.71'] | [28, 35] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_24 | dining | Lunch with colleagues | debit | INR | ['event_2145', 'event_2149', 'event_2154'] | ['2025-08-30', '2025-09-27', '2025-11-01'] | ['2046.83', '2137.71', '1818.76'] | [28, 35] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_24 | dining | Neighbourhood restaurant | debit | INR | ['event_2142', 'event_2151', 'event_2158'] | ['2025-08-09', '2025-10-11', '2025-11-29'] | ['1328.72', '1496.44', '1415.29'] | [63, 49] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_24 | dining | Quick-service meal | debit | INR | ['event_2141', 'event_2156', 'event_2161'] | ['2025-08-02', '2025-11-15', '2025-12-20'] | ['2239.04', '2198', '2184.47'] | [105, 35] | ['reducible'] | ['settled', 'settled', 'settled'] |
| user_24 | dining | Takeaway order | debit | INR | ['event_2140', 'event_2143', 'event_2144', 'event_2163'] | ['2025-07-26', '2025-08-16', '2025-08-23', '2026-01-03'] | ['2149.97', '1291.44', '2105.67', '1918.02'] | [21, 7, 133] | ['reducible'] | ['settled', 'settled', 'settled', 'settled'] |
| user_24 | dining | Weekend food delivery | debit | INR | ['event_2138', 'event_2152', 'event_2159', 'event_2160'] | ['2025-07-12', '2025-10-18', '2025-12-06', '2025-12-13'] | ['1757.23', '1662.99', '1842.2', '1911.68'] | [98, 49, 7] | ['reducible'] | ['settled', 'settled', 'settled', 'settled'] |
| user_24 | entertainment | Local event tickets | debit | INR | ['event_2050', 'event_2058', 'event_2066', 'event_2074', 'event_2082'] | ['2025-08-13', '2025-09-13', '2025-10-13', '2025-11-13', '2025-12-13'] | ['1870.6', '2124.72', '1916.16', '1845.75', '1896.25'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | groceries | Grocery delivery | debit | INR | ['event_2087', 'event_2090', 'event_2096'] | ['2025-08-09', '2025-09-08', '2025-11-07'] | ['2439.18', '2601.43', '2295.12'] | [30, 60] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_24 | groceries | Household groceries | debit | INR | ['event_2089', 'event_2091', 'event_2093', 'event_2099', 'event_2100'] | ['2025-08-29', '2025-09-18', '2025-10-08', '2025-12-07', '2025-12-17'] | ['2201.87', '2958.79', '2145.69', '2260.73', '2106.55'] | [20, 20, 60, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | groceries | Neighbourhood grocer | debit | INR | ['event_2084', 'event_2085', 'event_2088', 'event_2094', 'event_2097', 'event_2098'] | ['2025-07-10', '2025-07-20', '2025-08-19', '2025-10-18', '2025-11-17', '2025-11-27'] | ['2886.9', '2024.93', '2564.99', '1843.76', '1824.41', '2113.95'] | [10, 30, 60, 30, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | groceries | Supermarket basket | debit | INR | ['event_2086', 'event_2092'] | ['2025-07-30', '2025-09-28'] | ['2236.73', '2042.7'] | [60] | ['fixed'] | ['settled', 'settled'] |
| user_24 | insurance | Insurance policy payment | debit | INR | ['event_2046', 'event_2054', 'event_2062', 'event_2070', 'event_2078'] | ['2025-08-06', '2025-09-06', '2025-10-06', '2025-11-06', '2025-12-06'] | ['2510', '2510', '2510', '2510', '2510'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | rent | Landlord standing order | debit | INR | ['event_2044', 'event_2052', 'event_2060', 'event_2068', 'event_2076', 'event_2083'] | ['2025-08-01', '2025-09-01', '2025-10-01', '2025-11-01', '2025-12-01', '2026-01-01'] | ['18600', '18600', '18600', '18600', '18600', '18600'] | [31, 30, 31, 30, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | salary | Payroll credit | credit | INR | ['event_2043', 'event_2051', 'event_2059', 'event_2067', 'event_2075'] | ['2025-08-15', '2025-09-15', '2025-10-15', '2025-11-15', '2025-12-15'] | ['61000', '61000', '61000', '61000', '61000'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | shopping | Monthly shopping spend | debit | INR | ['event_2049', 'event_2057', 'event_2065', 'event_2073', 'event_2081'] | ['2025-08-11', '2025-09-11', '2025-10-11', '2025-11-11', '2025-12-11'] | ['2409.82', '2514.9', '2680.78', '2398.76', '2564'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | streaming | Family streaming plan | debit | INR | ['event_2048', 'event_2056', 'event_2064', 'event_2072', 'event_2080'] | ['2025-08-08', '2025-09-08', '2025-10-08', '2025-11-08', '2025-12-08'] | ['1200', '1200', '1200', '1200', '1200'] | [31, 30, 31, 30] | ['reducible_or_stoppable'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | transport | Commuter pass | debit | INR | ['event_2102', 'event_2111', 'event_2117', 'event_2118', 'event_2126'] | ['2025-07-11', '2025-08-25', '2025-09-24', '2025-09-29', '2025-11-08'] | ['1663.51', '1091.32', '1586.75', '1218.23', '1514.06'] | [45, 30, 5, 40] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | transport | Fuel refill | debit | INR | ['event_2116', 'event_2124', 'event_2129', 'event_2131', 'event_2134', 'event_2136'] | ['2025-09-19', '2025-10-29', '2025-11-23', '2025-12-03', '2025-12-18', '2025-12-28'] | ['1153.55', '1110.11', '1050.4', '1270.09', '1059.47', '1255.38'] | [40, 25, 10, 15, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | transport | Local taxi | debit | INR | ['event_2104', 'event_2113', 'event_2123'] | ['2025-07-21', '2025-09-04', '2025-10-24'] | ['1760.99', '1370.25', '1731.13'] | [45, 50] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_24 | transport | Metro and bus fares | debit | INR | ['event_2103', 'event_2109', 'event_2114', 'event_2122', 'event_2125', 'event_2127', 'event_2133'] | ['2025-07-16', '2025-08-15', '2025-09-09', '2025-10-19', '2025-11-03', '2025-11-13', '2025-12-13'] | ['1021.64', '1122.2', '1401.3', '1314.27', '1256.01', '1600.18', '1341.45'] | [30, 25, 40, 15, 10, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | transport | Parking and tolls | debit | INR | ['event_2107', 'event_2120', 'event_2128', 'event_2130'] | ['2025-08-05', '2025-10-09', '2025-11-18', '2025-11-28'] | ['1319.2', '1585.39', '1534.77', '1187.92'] | [65, 40, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_24 | transport | Rail pass | debit | INR | ['event_2105', 'event_2135', 'event_2137'] | ['2025-07-26', '2025-12-23', '2026-01-02'] | ['1208.87', '1438', '1593.41'] | [150, 10] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_24 | transport | Ride-hailing trip | debit | INR | ['event_2106', 'event_2108', 'event_2110', 'event_2112', 'event_2115', 'event_2119', 'event_2121'] | ['2025-07-31', '2025-08-10', '2025-08-20', '2025-08-30', '2025-09-14', '2025-10-04', '2025-10-14'] | ['1232.11', '1536.25', '1576.88', '1119.08', '1393.89', '1750.91', '1069.31'] | [10, 10, 10, 15, 20, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_24 | utilities | Household utility payment | debit | INR | ['event_2045', 'event_2053', 'event_2061', 'event_2069', 'event_2077'] | ['2025-08-05', '2025-09-05', '2025-10-05', '2025-11-05', '2025-12-05'] | ['3049.81', '3226.12', '3417.7', '3335.41', '3490.5'] | [31, 30, 31, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | cloud_storage | Cloud storage plan | debit | IDR | ['event_2171', 'event_2179', 'event_2187', 'event_2195', 'event_2203'] | ['2023-10-12', '2023-11-12', '2023-12-12', '2024-01-12', '2024-02-12'] | ['126350', '126350', '126350', '126350', '126350'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | dining | Bakery and snacks | debit | IDR | ['event_2263', 'event_2275', 'event_2278'] | ['2023-09-20', '2023-12-13', '2024-01-03'] | ['1028620.35', '1128974.93', '868921.02'] | [84, 21] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_25 | dining | Coffee shop | debit | IDR | ['event_2264', 'event_2268', 'event_2271', 'event_2273', 'event_2279', 'event_2283'] | ['2023-09-27', '2023-10-25', '2023-11-15', '2023-11-29', '2024-01-10', '2024-02-07'] | ['1117067.23', '1115260.36', '1142868.87', '740801.32', '925855.11', '949118.03'] | [28, 21, 14, 42, 28] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | dining | Lunch with colleagues | debit | IDR | ['event_2262', 'event_2267', 'event_2282', 'event_2285'] | ['2023-09-13', '2023-10-18', '2024-01-31', '2024-02-21'] | ['979886.38', '1232054.29', '1251981.8', '777034.83'] | [35, 105, 21] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | dining | Neighbourhood restaurant | debit | IDR | ['event_2272', 'event_2276', 'event_2280', 'event_2286'] | ['2023-11-22', '2023-12-20', '2024-01-17', '2024-02-28'] | ['897310.27', '956749.83', '1204804.45', '1133036.68'] | [28, 28, 42] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | dining | Quick-service meal | debit | IDR | ['event_2269', 'event_2281'] | ['2023-11-01', '2024-01-24'] | ['1261355.55', '1057617.64'] | [84] | ['fixed'] | ['settled', 'settled'] |
| user_25 | dining | Takeaway order | debit | IDR | ['event_2265', 'event_2277', 'event_2284'] | ['2023-10-04', '2023-12-27', '2024-02-14'] | ['756322.76', '1095978.2', '1051249.87'] | [84, 49] | ['fixed'] | ['settled', 'settled', 'settled'] |
| user_25 | dining | Weekend food delivery | debit | IDR | ['event_2266', 'event_2270'] | ['2023-10-11', '2023-11-08'] | ['1249486.33', '921922.8'] | [28] | ['fixed'] | ['settled', 'settled'] |
| user_25 | entertainment | Games and recreation | debit | IDR | ['event_2174', 'event_2182', 'event_2190', 'event_2198', 'event_2206'] | ['2023-10-14', '2023-11-14', '2023-12-14', '2024-01-14', '2024-02-14'] | ['451681.59', '415734.51', '499510.22', '504697.37', '426338.4'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | groceries | Bulk pantry shop | debit | IDR | ['event_2208', 'event_2213'] | ['2023-09-11', '2023-10-31'] | ['1348940.42', '1066197.78'] | [50] | ['fixed'] | ['settled', 'settled'] |
| user_25 | groceries | Grocery delivery | debit | IDR | ['event_2210', 'event_2221'] | ['2023-10-01', '2024-01-19'] | ['1490390.69', '1388569.11'] | [110] | ['fixed'] | ['settled', 'settled'] |
| user_25 | groceries | Household groceries | debit | IDR | ['event_2220', 'event_2223'] | ['2024-01-09', '2024-02-08'] | ['983053.43', '1369082.68'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_25 | groceries | Neighbourhood grocer | debit | IDR | ['event_2214', 'event_2216', 'event_2217', 'event_2218'] | ['2023-11-10', '2023-11-30', '2023-12-10', '2023-12-20'] | ['893559.78', '1101344.82', '876032.86', '917586.64'] | [20, 10, 10] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | groceries | Supermarket basket | debit | IDR | ['event_2212', 'event_2224'] | ['2023-10-21', '2024-02-18'] | ['1048982.51', '864688.59'] | [120] | ['fixed'] | ['settled', 'settled'] |
| user_25 | groceries | Weekly produce market | debit | IDR | ['event_2209', 'event_2211', 'event_2219', 'event_2222'] | ['2023-09-21', '2023-10-11', '2023-12-30', '2024-01-29'] | ['1510693.45', '1211444.04', '1454933.56', '1335295.2'] | [20, 80, 30] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | insurance | Insurance policy payment | debit | IDR | ['event_2170', 'event_2178', 'event_2186', 'event_2194', 'event_2202'] | ['2023-10-07', '2023-11-07', '2023-12-07', '2024-01-07', '2024-02-07'] | ['904400', '904400', '904400', '904400', '904400'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | rent | Monthly rent | debit | IDR | ['event_2168', 'event_2176', 'event_2184', 'event_2192', 'event_2200', 'event_2207'] | ['2023-10-02', '2023-11-02', '2023-12-02', '2024-01-02', '2024-02-02', '2024-03-02'] | ['6954000', '6954000', '6954000', '6954000', '6954000', '6954000'] | [31, 30, 31, 31, 29] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | salary | International employer payroll | credit | USD | ['event_2167', 'event_2175', 'event_2183', 'event_2191', 'event_2199'] | ['2023-10-15', '2023-11-15', '2023-12-15', '2024-01-15', '2024-02-15'] | ['1800', '1800', '1800', '1800', '1800'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | shopping | Monthly shopping spend | debit | IDR | ['event_2173', 'event_2181', 'event_2189', 'event_2197', 'event_2205'] | ['2023-10-12', '2023-11-12', '2023-12-12', '2024-01-12', '2024-02-12'] | ['966785.96', '1054608.5', '1000693.22', '1102784.74', '1170271.29'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | streaming | Video streaming plan | debit | IDR | ['event_2172', 'event_2180', 'event_2188', 'event_2196', 'event_2204'] | ['2023-10-09', '2023-11-09', '2023-12-09', '2024-01-09', '2024-02-09'] | ['573800', '573800', '573800', '573800', '573800'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Commuter pass | debit | IDR | ['event_2236', 'event_2237', 'event_2246', 'event_2256'] | ['2023-11-01', '2023-11-06', '2023-12-21', '2024-02-09'] | ['507090.88', '454432.04', '593848.06', '448075.32'] | [5, 45, 50] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Fuel refill | debit | IDR | ['event_2235', 'event_2239', 'event_2251', 'event_2258'] | ['2023-10-27', '2023-11-16', '2024-01-15', '2024-02-19'] | ['567772.41', '557483.97', '542331.16', '458596.67'] | [20, 60, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Local taxi | debit | IDR | ['event_2231', 'event_2232', 'event_2233', 'event_2253', 'event_2257'] | ['2023-10-07', '2023-10-12', '2023-10-17', '2024-01-25', '2024-02-14'] | ['591314.74', '458415.57', '445484.16', '745983.26', '560613.2'] | [5, 5, 100, 20] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Metro and bus fares | debit | IDR | ['event_2228', 'event_2229', 'event_2240', 'event_2245', 'event_2250', 'event_2252', 'event_2259'] | ['2023-09-22', '2023-09-27', '2023-11-21', '2023-12-16', '2024-01-10', '2024-01-20', '2024-02-24'] | ['579668.34', '636547.25', '627417.61', '732740.37', '562442.16', '463292.75', '663001.49'] | [5, 55, 25, 25, 10, 35] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Parking and tolls | debit | IDR | ['event_2230', 'event_2234', 'event_2238', 'event_2243', 'event_2247'] | ['2023-10-02', '2023-10-22', '2023-11-11', '2023-12-06', '2023-12-26'] | ['724399.08', '617815.52', '617984.73', '695049.46', '639058'] | [20, 20, 25, 20] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Rail pass | debit | IDR | ['event_2242', 'event_2248'] | ['2023-12-01', '2023-12-31'] | ['522613.77', '721837.88'] | [30] | ['fixed'] | ['settled', 'settled'] |
| user_25 | transport | Ride-hailing trip | debit | IDR | ['event_2226', 'event_2227', 'event_2249', 'event_2260', 'event_2261'] | ['2023-09-12', '2023-09-17', '2024-01-05', '2024-02-29', '2024-03-05'] | ['725793.85', '447746.71', '637250.91', '729004.44', '571596.93'] | [5, 110, 55, 5] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |
| user_25 | transport | Vehicle charging | debit | IDR | ['event_2241', 'event_2244', 'event_2254', 'event_2255'] | ['2023-11-26', '2023-12-11', '2024-01-30', '2024-02-04'] | ['547424.01', '721981.78', '549524.6', '664768.21'] | [15, 50, 5] | ['fixed'] | ['settled', 'settled', 'settled', 'settled'] |
| user_25 | utilities | Household utility payment | debit | IDR | ['event_2169', 'event_2177', 'event_2185', 'event_2193', 'event_2201'] | ['2023-10-06', '2023-11-06', '2023-12-06', '2024-01-06', '2024-02-06'] | ['1338903.44', '1401205.21', '1334719.89', '1341541.39', '1201903.67'] | [31, 30, 31, 31] | ['fixed'] | ['settled', 'settled', 'settled', 'settled', 'settled'] |

## Conceptual forecast models

| Model | Safe | Earliest | Status | Method | Plan | Changes | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| A explicit events only | 3 | 9 | 12 | 14 | 13 | 22 | No inferred recurrence; safe lower-bound evidence only. |
| B explicit fixed recurrence plus confirmed credits | 2 | 8 | 10 | 11 | 10 | 22 | Projects fixed recurring debits and explicit confirmed credits; no variable mean. |
| C fixed recurrence plus evidence-supported variable recurrence | 2 | 8 | 10 | 11 | 10 | 22 | Projects variable series only if an evidence-based amount exists; amount rule remains unresolved. |
| D historical recurrence with inferred amount | 2 | 8 | 10 | 11 | 10 | 22 | Current-style inference; includes unsupported amount extrapolation. |

Scores are supporting diagnostics only. Model D is not defensible merely because it can match a fixture; Model A can omit required recurring obligations; Model B is the strongest currently supported baseline; Model C requires an explicit amount-estimation rule that the specification does not provide.

## Same-day and lifecycle findings

No solved example isolates same-day credit/debit/payment ordering. Pending credits are explicitly excluded; pending debits are reserved at their supplied settlement date; failed/cancelled/unrealized rows have no cash movement. Replacement timing and amount remain UNKNOWN unless supplied by a live linked row.

## Decision gate

1. The challenge requires a deterministic 90-day minimum-balance forecast over explicit confirmed movements and supported fixed recurrence, with no invented income or variable amount.
2. Phase 4 correctly removed the unsupported variable arithmetic mean, but its broad recurrence/lifecycle and baseline choices still alter downstream feasibility.
3. Change next only after resolving fixed-series identity, explicit confirmed credit boundaries, optional-baseline scope, and direct event-level residuals.
4. Do not change ranking, payment preferences, or output serialization to compensate for an upstream cash-flow mismatch.
5. Same-day ordering, recurrence thresholds/month-end rules, generic scheduled credits, replacement timing, late-deadline status mapping, and flexible ties remain genuinely unspecified.

## Required truth table

The machine-readable `PHASE_5_FORECAST_FORENSICS.json` contains one record for every solved example with an incorrect safe amount or earliest date, including explicit movements, pending/lifecycle state, recurrence evidence, critical dates, residual capacity and first-divergence category.
