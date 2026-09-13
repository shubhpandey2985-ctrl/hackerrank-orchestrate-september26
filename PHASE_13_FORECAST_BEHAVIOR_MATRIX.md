# Phase 13 Forecast Behavior Matrix

Generated from the supplied 25 solved requests and the frozen deterministic solver. Full event/trace detail is in `PHASE_13_BEHAVIOR_MATRIX.json`.

| request | first divergence | expected safe | actual safe | expected earliest | actual earliest | expected status | actual status | expected method | actual method | expected plan | actual plan | expected changes | actual changes |
|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|
|request_01|none|25256|25256|2024-03-03|2024-03-03|affordable_now|affordable_now|full_payment|full_payment|2024-03-03:25256|2024-03-03:25256|none|none|
|request_02|amount_safe_to_pay|17229139.2|20760289.2|2025-09-15||affordable_with_plan|not_affordable|installments|not_recommended|2025-08-08:15952906.67\|2025-09-07:15952906.67\|2025-10-07:15952906.67|none|none|none|
|request_03|amount_safe_to_pay|873000|0|2019-11-15||affordable_later|not_affordable|wait|not_recommended|2019-11-15:5491000|none|none|none|
|request_04|amount_safe_to_pay|8401800|0|2024-06-15||affordable_later|not_affordable|wait|not_recommended|2024-06-15:12693000|none|none|none|
|request_05|amount_safe_to_pay|737|15488||2025-11-06|not_affordable|affordable_now|not_recommended|full_payment|none|2025-11-06:15488|none|none|
|request_06|amount_safe_to_pay|603.3|541.2|2026-01-15||affordable_with_plan|not_affordable|full_payment|not_recommended|2026-01-03:620.40|none|stop:event_476|none|
|request_07|amount_safe_to_pay|87170.56|12619.56|2024-10-23||affordable_with_plan|not_affordable|installments|not_recommended|2024-09-12:68432\|2024-10-10:68432\|2024-11-07:68432|none|none|none|
|request_08|amount_safe_to_pay|284.57|0|2025-04-15||affordable_later|not_affordable|wait|not_recommended|2025-04-15:996.60|none|none|none|
|request_09|amount_safe_to_pay|166.61|166.6|2026-07-04|2026-07-04|affordable_now|affordable_now|full_payment|full_payment|2026-07-04:166.61|2026-07-04:166.61|none|none|
|request_10|amount_safe_to_pay|12700|266700||2024-12-06|not_affordable|not_affordable|not_recommended|not_recommended|none|none|none|none|
|request_11|amount_safe_to_pay|12510645|13110000|2025-07-15|2025-05-03|affordable_with_plan|affordable_now|full_payment|full_payment|2025-05-03:13110000|2025-05-03:13110000|reduce_to:event_989:665950|none|
|request_12|none|65164|65164|2026-04-05|2026-04-05|affordable_with_plan|affordable_with_plan|installments|installments|2026-04-19:22590.19\|2026-05-20:22590.19\|2026-06-20:22590.19|2026-04-19:22590.19\|2026-05-20:22590.19\|2026-06-20:22590.19|none|none|
|request_13|amount_safe_to_pay|433.4|941.6|2024-05-15||affordable_later|not_affordable|wait|not_recommended|2024-05-15:941.60|none|none|none|
|request_14|amount_safe_to_pay|597.74|1381.74|||not_affordable|not_affordable|not_recommended|not_recommended|none|none|none|none|
|request_15|amount_safe_to_pay|83.05|448.05|||not_affordable|not_affordable|not_recommended|not_recommended|none|none|none|none|
|request_16|amount_safe_to_pay|122500|0|2023-08-12||affordable_now|not_affordable|full_payment|not_recommended|2023-08-12:122500|none|none|none|
|request_17|amount_safe_to_pay|243849.58|274600|2026-03-15|2026-03-01|affordable_with_plan|affordable_with_plan|installments|installments|2026-03-01:95194.67\|2026-03-31:95194.67\|2026-04-30:95194.67|2026-03-01:95194.67\|2026-03-31:95194.67\|2026-04-30:95194.67|none|none|
|request_18|amount_safe_to_pay|462|381|2026-09-15||affordable_later|not_affordable|wait|not_recommended|2026-09-15:3246.10|none|none|none|
|request_19|amount_safe_to_pay|28820|0|2024-09-15||affordable_with_plan|not_affordable|partial_payment|not_recommended|2024-09-04:28820\|2024-09-15:10840|none|none|none|
|request_20|amount_safe_to_pay|5400|6975|||not_affordable|not_affordable|not_recommended|not_recommended|none|none|none|none|
|request_21|amount_safe_to_pay|1543.35|1574.4|2026-04-15|2026-04-03|affordable_with_plan|affordable_now|full_payment|full_payment|2026-04-03:1574.40|2026-04-03:1574.4|stop:event_1815\|reduce_to:event_1816:23.50|none|
|request_22|amount_safe_to_pay|475.46|261.06|2025-01-15||affordable_with_plan|not_affordable|installments|not_recommended|2024-12-08:253.59\|2025-01-05:253.59\|2025-02-02:253.59|none|none|none|
|request_23|amount_safe_to_pay|9152|0|2025-07-15||affordable_later|not_affordable|wait|not_recommended|2025-07-15:38016|none|none|none|
|request_24|amount_safe_to_pay|13420|0|||not_affordable|not_affordable|not_recommended|not_recommended|none|none|none|none|
|request_25|amount_safe_to_pay|1425000|7079400|||not_affordable|not_affordable|not_recommended|not_recommended|none|none|none|none|

## Causal trace index

Each row's JSON record includes starting/minimum balances, relevant credits/debits, pending and failed/cancelled events, recurrence evidence, FX, lifecycle markers, and the deterministic movement trace. `first_divergent_date` is the earliest modeled movement date, not a claim that the expected answer endorses that movement.

### First-divergence distribution

- `amount_safe_to_pay`: 23 (request_02, request_03, request_04, request_05, request_06, request_07, request_08, request_09, request_10, request_11, request_13, request_14, request_15, request_16, request_17, request_18, request_19, request_20, request_21, request_22, request_23, request_24, request_25)
- `none`: 2 (request_01, request_12)
