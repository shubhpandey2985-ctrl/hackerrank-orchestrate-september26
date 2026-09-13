# Sample mismatch forensic report

Generated from repository data and current deterministic implementation. No expected answer is hardcoded.

## Harness verification

Expected rows: 25; actual rows: 25; joined by `request_id`. Expected header: `['request_id', 'user_id', 'request_date', 'request_type', 'requested_amount', 'desired_completion_date', 'allows_partial_payment', 'request_text', 'amount_safe_to_pay', 'affordability_status', 'recommended_payment_method', 'payment_plan', 'earliest_date_for_full_payment', 'spending_changes_needed', 'decision_explanation']`. Actual header: `['request_id', 'amount_safe_to_pay', 'affordability_status', 'recommended_payment_method', 'payment_plan', 'earliest_date_for_full_payment', 'spending_changes_needed', 'decision_explanation']`. Compared fields: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, spending_changes_needed, decision_explanation. Numeric-equivalent trailing-zero differences are classified as `20. output serialization`.

## Root-cause priority

- 20. output serialization: 25 mismatching fields
- 12. earliest-safe-date calculation: 16 mismatching fields
- 11. safe-amount calculation: 13 mismatching fields
- 18. candidate ranking: 11 mismatching fields
- 19. deadline/status mapping: 10 mismatching fields
- 16. payment-method preference: 8 mismatching fields
- 2. event classification: 5 mismatching fields
- 7. scheduled-credit semantics: 5 mismatching fields
- 17. flexible-spending logic: 3 mismatching fields
- 1. data loading: 0 mismatching fields
- 10. minimum-balance enforcement: 0 mismatching fields
- 13. candidate generation: 0 mismatching fields
- 14. partial-payment logic: 0 mismatching fields
- 15. installment logic: 0 mismatching fields
- 3. deduplication: 0 mismatching fields
- 4. currency conversion: 0 mismatching fields
- 5. date ordering: 0 mismatching fields
- 6. recurrence detection: 0 mismatching fields
- 8. failed/cancelled/replacement lifecycle: 0 mismatching fields
- 9. forecast calculation: 0 mismatching fields

## Field mismatch counts

- amount_safe_to_pay: 23
- affordability_status: 10
- recommended_payment_method: 8
- payment_plan: 11
- earliest_date_for_full_payment: 16
- decision_explanation: 25
- spending_changes_needed: 3

## Per-field mismatches

### request_01 — `amount_safe_to_pay`
- Expected: `25256`
- Actual: `23292.94`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `9`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '70893.01470085470085470085470085470085470', '2024-03-20': '70449.06247863247863247863247863247863248', '2024-05-31': '27942.08487179487179487179487179487179488'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_01', False, None), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None)]`
- Validator: `True`
 
### request_01 — `affordability_status`
- Expected: `affordable_now`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `9`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '70893.01470085470085470085470085470085470', '2024-03-20': '70449.06247863247863247863247863247863248', '2024-05-31': '27942.08487179487179487179487179487179488'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_01', False, None), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None)]`
- Validator: `True`
 
### request_01 — `recommended_payment_method`
- Expected: `full_payment`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `9`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '70893.01470085470085470085470085470085470', '2024-03-20': '70449.06247863247863247863247863247863248', '2024-05-31': '27942.08487179487179487179487179487179488'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_01', False, None), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None)]`
- Validator: `True`
 
### request_01 — `payment_plan`
- Expected: `2024-03-03:25256`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `9`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '70893.01470085470085470085470085470085470', '2024-03-20': '70449.06247863247863247863247863247863248', '2024-05-31': '27942.08487179487179487179487179487179488'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_01', False, None), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None)]`
- Validator: `True`
 
### request_01 — `earliest_date_for_full_payment`
- Expected: `2024-03-03`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `9`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '70893.01470085470085470085470085470085470', '2024-03-20': '70449.06247863247863247863247863247863248', '2024-05-31': '27942.08487179487179487179487179487179488'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_01', False, None), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None)]`
- Validator: `True`
 
### request_01 — `decision_explanation`
- Expected: `Pay ZAR 25,256 today. This leaves at least ZAR 18,000 available over the next 90 days.`
- Actual: `Safe amount today is 23292.94; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `9`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '70893.01470085470085470085470085470085470', '2024-03-20': '70449.06247863247863247863247863247863248', '2024-05-31': '27942.08487179487179487179487179487179488'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_01', False, None), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None)]`
- Validator: `True`
 
### request_02 — `amount_safe_to_pay`
- Expected: `17229139.2`
- Actual: `24911239.26`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `11`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '52418539.26', '2025-10-10': '68786146.87425641025641025641025641025645', '2025-11-02': '94349875.17986324786324786324786324786324'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `11`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '52418539.26', '2025-10-10': '68786146.87425641025641025641025641025645', '2025-11-02': '94349875.17986324786324786324786324786324'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `recommended_payment_method`
- Expected: `installments`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `11`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '52418539.26', '2025-10-10': '68786146.87425641025641025641025641025645', '2025-11-02': '94349875.17986324786324786324786324786324'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `payment_plan`
- Expected: `2025-08-08:15952906.67|2025-09-07:15952906.67|2025-10-07:15952906.67`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `11`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '52418539.26', '2025-10-10': '68786146.87425641025641025641025641025645', '2025-11-02': '94349875.17986324786324786324786324786324'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `earliest_date_for_full_payment`
- Expected: `2025-09-15`
- Actual: `2025-10-13`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `11`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '52418539.26', '2025-10-10': '68786146.87425641025641025641025641025645', '2025-11-02': '94349875.17986324786324786324786324786324'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `decision_explanation`
- Expected: `Use 3 installments of IDR 15,952,906.67, starting 8 August 2025. This leaves at least IDR 29,158,400 available.`
- Actual: `Safe amount today is 24911239.26; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `11`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '52418539.26', '2025-10-10': '68786146.87425641025641025641025641025645', '2025-11-02': '94349875.17986324786324786324786324786324'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_03 — `amount_safe_to_pay`
- Expected: `873000`
- Actual: `1159761.09`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `9`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '7241058.447777777777777777777777777777777', '2019-12-01': '10978775.15888888888888888888888888888889'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_03 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `9`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '7241058.447777777777777777777777777777777', '2019-12-01': '10978775.15888888888888888888888888888889'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_03 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `9`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '7241058.447777777777777777777777777777777', '2019-12-01': '10978775.15888888888888888888888888888889'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_03 — `payment_plan`
- Expected: `2019-11-15:5491000`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `9`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '7241058.447777777777777777777777777777777', '2019-12-01': '10978775.15888888888888888888888888888889'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_03 — `earliest_date_for_full_payment`
- Expected: `2019-11-15`
- Actual: `2019-11-29`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `9`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '7241058.447777777777777777777777777777777', '2019-12-01': '10978775.15888888888888888888888888888889'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_03 — `decision_explanation`
- Expected: `Pay IDR 5,491,000 in full on 15 November 2019. Paying earlier would take the balance below the IDR 2,668,700 minimum.`
- Actual: `Safe amount today is 1159761.09; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `9`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '7241058.447777777777777777777777777777777', '2019-12-01': '10978775.15888888888888888888888888888889'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_04 — `amount_safe_to_pay`
- Expected: `8401800`
- Actual: `12693000`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `2024-06-13:12693000` via `wait`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '42680364.44038461538461538461538461538461', '2024-06-13': '79485163.08638461538461538461538461538461', '2024-06-19': '77153181.19676923076923076923076923076923', '2024-09-01': '85130972.56723076923076923076923076923082'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None), ('wait', True, [0, 0, '12693000', '2024-06-13', 1, ''])]`
- Validator: `True`
 
### request_04 — `payment_plan`
- Expected: `2024-06-15:12693000`
- Actual: `2024-06-13:12693000`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `2024-06-13:12693000` via `wait`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '42680364.44038461538461538461538461538461', '2024-06-13': '79485163.08638461538461538461538461538461', '2024-06-19': '77153181.19676923076923076923076923076923', '2024-09-01': '85130972.56723076923076923076923076923082'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None), ('wait', True, [0, 0, '12693000', '2024-06-13', 1, ''])]`
- Validator: `True`
 
### request_04 — `earliest_date_for_full_payment`
- Expected: `2024-06-15`
- Actual: `2024-06-13`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `2024-06-13:12693000` via `wait`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '42680364.44038461538461538461538461538461', '2024-06-13': '79485163.08638461538461538461538461538461', '2024-06-19': '77153181.19676923076923076923076923076923', '2024-09-01': '85130972.56723076923076923076923076923082'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None), ('wait', True, [0, 0, '12693000', '2024-06-13', 1, ''])]`
- Validator: `True`
 
### request_04 — `decision_explanation`
- Expected: `Wait until 15 June 2024, then pay IDR 12,693,000 in full. Paying sooner would put the IDR 30,686,600 minimum at risk.`
- Actual: `Plan wait completes 12693000 while maintaining the minimum balance; safe today: 12693000.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `2024-06-13:12693000` via `wait`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '42680364.44038461538461538461538461538461', '2024-06-13': '79485163.08638461538461538461538461538461', '2024-06-19': '77153181.19676923076923076923076923076923', '2024-09-01': '85130972.56723076923076923076923076923082'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None), ('wait', True, [0, 0, '12693000', '2024-06-13', 1, ''])]`
- Validator: `True`
 
### request_05 — `amount_safe_to_pay`
- Expected: `737`
- Actual: `5821`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `9`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '17480.94869230769230769230769230769230768', '2026-02-03': '14901.49215384615384615384615384615384614'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_13', False, None), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None)]`
- Validator: `True`
 
### request_05 — `decision_explanation`
- Expected: `Do not make this payment by 12 January 2026. None of the available options keeps the ZAR 13,100 minimum protected.`
- Actual: `Safe amount today is 5821; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `9`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '17480.94869230769230769230769230769230768', '2026-02-03': '14901.49215384615384615384615384615384614'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_13', False, None), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None)]`
- Validator: `True`
 
### request_06 — `amount_safe_to_pay`
- Expected: `603.3`
- Actual: `620.40`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `2026-01-03:620.40` via `full_payment`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `11`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1915.424', '2026-01-14': '2584.284066666666666666666666666666666667', '2026-04-02': '2525.446600000000000000000000000000000003'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '620.4', '2026-01-03', 1, '']), ('option_payment_option_16', True, [0, 0, '620.4', '2026-01-03', 1, 'payment_option_16']), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None), ('wait', True, [0, 0, '620.4', '2026-01-03', 1, ''])]`
- Validator: `True`
 
### request_06 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `affordable_now`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `2026-01-03:620.40` via `full_payment`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `11`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1915.424', '2026-01-14': '2584.284066666666666666666666666666666667', '2026-04-02': '2525.446600000000000000000000000000000003'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '620.4', '2026-01-03', 1, '']), ('option_payment_option_16', True, [0, 0, '620.4', '2026-01-03', 1, 'payment_option_16']), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None), ('wait', True, [0, 0, '620.4', '2026-01-03', 1, ''])]`
- Validator: `True`
 
### request_06 — `earliest_date_for_full_payment`
- Expected: `2026-01-15`
- Actual: `2026-01-03`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `2026-01-03:620.40` via `full_payment`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `11`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1915.424', '2026-01-14': '2584.284066666666666666666666666666666667', '2026-04-02': '2525.446600000000000000000000000000000003'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '620.4', '2026-01-03', 1, '']), ('option_payment_option_16', True, [0, 0, '620.4', '2026-01-03', 1, 'payment_option_16']), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None), ('wait', True, [0, 0, '620.4', '2026-01-03', 1, ''])]`
- Validator: `True`
 
### request_06 — `spending_changes_needed`
- Expected: `stop:event_476`
- Actual: `none`
- Primary root cause: **17. flexible-spending logic**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `2026-01-03:620.40` via `full_payment`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `11`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1915.424', '2026-01-14': '2584.284066666666666666666666666666666667', '2026-04-02': '2525.446600000000000000000000000000000003'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '620.4', '2026-01-03', 1, '']), ('option_payment_option_16', True, [0, 0, '620.4', '2026-01-03', 1, 'payment_option_16']), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None), ('wait', True, [0, 0, '620.4', '2026-01-03', 1, ''])]`
- Validator: `True`
 
### request_06 — `decision_explanation`
- Expected: `Stop the family streaming plan, then pay EUR 620.40 today. This leaves at least EUR 800 available.`
- Actual: `Plan full_payment completes 620.40 while maintaining the minimum balance; safe today: 620.40.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `2026-01-03:620.40` via `full_payment`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `11`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1915.424', '2026-01-14': '2584.284066666666666666666666666666666667', '2026-04-02': '2525.446600000000000000000000000000000003'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '620.4', '2026-01-03', 1, '']), ('option_payment_option_16', True, [0, 0, '620.4', '2026-01-03', 1, 'payment_option_16']), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None), ('wait', True, [0, 0, '620.4', '2026-01-03', 1, ''])]`
- Validator: `True`
 
### request_07 — `amount_safe_to_pay`
- Expected: `87170.56`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `8`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '22975.20666666666666666666666666666666683', '2024-12-03': '8735.298888888888888888888888888888889057'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_07 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `8`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '22975.20666666666666666666666666666666683', '2024-12-03': '8735.298888888888888888888888888888889057'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_07 — `recommended_payment_method`
- Expected: `installments`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `8`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '22975.20666666666666666666666666666666683', '2024-12-03': '8735.298888888888888888888888888888889057'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_07 — `payment_plan`
- Expected: `2024-09-12:68432|2024-10-10:68432|2024-11-07:68432`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `8`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '22975.20666666666666666666666666666666683', '2024-12-03': '8735.298888888888888888888888888888889057'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_07 — `earliest_date_for_full_payment`
- Expected: `2024-10-23`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `8`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '22975.20666666666666666666666666666666683', '2024-12-03': '8735.298888888888888888888888888888889057'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_07 — `decision_explanation`
- Expected: `Use 3 installments of INR 68,432, starting 12 September 2024. This leaves at least INR 93,000 available.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `8`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '22975.20666666666666666666666666666666683', '2024-12-03': '8735.298888888888888888888888888888889057'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_08 — `amount_safe_to_pay`
- Expected: `284.57`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_08`; balance `1536.57`; minimum `800`; preferences `['full_payment']`
- Request: amount `996.6` on `2025-02-07`, deadline `2025-04-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '783.1600000000000000000000000000000000048', '2025-05-07': '-24.77076923076923076923076923076923076446'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_22', False, None), ('option_payment_option_23', False, None)]`
- Validator: `True`
 
### request_08 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_08`; balance `1536.57`; minimum `800`; preferences `['full_payment']`
- Request: amount `996.6` on `2025-02-07`, deadline `2025-04-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '783.1600000000000000000000000000000000048', '2025-05-07': '-24.77076923076923076923076923076923076446'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_22', False, None), ('option_payment_option_23', False, None)]`
- Validator: `True`
 
### request_08 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_08`; balance `1536.57`; minimum `800`; preferences `['full_payment']`
- Request: amount `996.6` on `2025-02-07`, deadline `2025-04-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '783.1600000000000000000000000000000000048', '2025-05-07': '-24.77076923076923076923076923076923076446'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_22', False, None), ('option_payment_option_23', False, None)]`
- Validator: `True`
 
### request_08 — `payment_plan`
- Expected: `2025-04-15:996.60`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_08`; balance `1536.57`; minimum `800`; preferences `['full_payment']`
- Request: amount `996.6` on `2025-02-07`, deadline `2025-04-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '783.1600000000000000000000000000000000048', '2025-05-07': '-24.77076923076923076923076923076923076446'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_22', False, None), ('option_payment_option_23', False, None)]`
- Validator: `True`
 
### request_08 — `earliest_date_for_full_payment`
- Expected: `2025-04-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_08`; balance `1536.57`; minimum `800`; preferences `['full_payment']`
- Request: amount `996.6` on `2025-02-07`, deadline `2025-04-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '783.1600000000000000000000000000000000048', '2025-05-07': '-24.77076923076923076923076923076923076446'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_22', False, None), ('option_payment_option_23', False, None)]`
- Validator: `True`
 
### request_08 — `decision_explanation`
- Expected: `Pay EUR 996.60 in full on 15 April 2025. Paying earlier would take the balance below the EUR 800 minimum.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_08`; balance `1536.57`; minimum `800`; preferences `['full_payment']`
- Request: amount `996.6` on `2025-02-07`, deadline `2025-04-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '783.1600000000000000000000000000000000048', '2025-05-07': '-24.77076923076923076923076923076923076446'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_22', False, None), ('option_payment_option_23', False, None)]`
- Validator: `True`
 
### request_09 — `amount_safe_to_pay`
- Expected: `166.61`
- Actual: `166.6`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_09`; balance `2231.1`; minimum `600`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `166.61` on `2026-07-04`, deadline `2026-07-23`
- Actual selected plan: `2026-07-04:166.61` via `full_payment`
- Credits `3` (scheduled `0`); debits `14`; pending `0`; recurring `9`; flexible `0`; options `3`
- Critical balances: `{'2026-07-04': '2231.1', '2026-07-23': '2336.491333333333333333333333333333333334', '2026-10-01': '2809.910111111111111111111111111111111114'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '166.61', '2026-07-04', 1, '']), ('option_payment_option_24', True, [0, 0, '166.61', '2026-07-04', 1, 'payment_option_24']), ('option_payment_option_25', False, None), ('option_payment_option_26', False, None), ('partial', True, [0, 0, '166.61', '2026-07-04', 2, '']), ('wait', True, [0, 0, '166.61', '2026-07-04', 1, ''])]`
- Validator: `True`
 
### request_09 — `decision_explanation`
- Expected: `Pay EUR 166.61 today. This keeps the EUR 600 minimum available over the next 90 days.`
- Actual: `Plan full_payment completes 166.61 while maintaining the minimum balance; safe today: 166.6.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_09`; balance `2231.1`; minimum `600`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `166.61` on `2026-07-04`, deadline `2026-07-23`
- Actual selected plan: `2026-07-04:166.61` via `full_payment`
- Credits `3` (scheduled `0`); debits `14`; pending `0`; recurring `9`; flexible `0`; options `3`
- Critical balances: `{'2026-07-04': '2231.1', '2026-07-23': '2336.491333333333333333333333333333333334', '2026-10-01': '2809.910111111111111111111111111111111114'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '166.61', '2026-07-04', 1, '']), ('option_payment_option_24', True, [0, 0, '166.61', '2026-07-04', 1, 'payment_option_24']), ('option_payment_option_25', False, None), ('option_payment_option_26', False, None), ('partial', True, [0, 0, '166.61', '2026-07-04', 2, '']), ('wait', True, [0, 0, '166.61', '2026-07-04', 1, ''])]`
- Validator: `True`
 
### request_10 — `amount_safe_to_pay`
- Expected: `12700`
- Actual: `266700`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_10`; balance `750155`; minimum `225400`; preferences `['partial_payment', 'installments']`
- Request: amount `266700` on `2024-12-06`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `6` (scheduled `0`); debits `23`; pending `0`; recurring `10`; flexible `33`; options `2`
- Critical balances: `{'2024-12-06': '744172.2096', '2025-02-10': '799398.0323846153846153846153846153846154', '2025-03-05': '882802.8849538461538461538461538461538462'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_27', False, None), ('option_payment_option_28', False, None)]`
- Validator: `True`
 
### request_10 — `earliest_date_for_full_payment`
- Expected: ``
- Actual: `2024-12-06`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_10`; balance `750155`; minimum `225400`; preferences `['partial_payment', 'installments']`
- Request: amount `266700` on `2024-12-06`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `6` (scheduled `0`); debits `23`; pending `0`; recurring `10`; flexible `33`; options `2`
- Critical balances: `{'2024-12-06': '744172.2096', '2025-02-10': '799398.0323846153846153846153846153846154', '2025-03-05': '882802.8849538461538461538461538461538462'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_27', False, None), ('option_payment_option_28', False, None)]`
- Validator: `True`
 
### request_10 — `decision_explanation`
- Expected: `Do not make this payment by 10 February 2025. None of the available options keeps the INR 225,400 minimum protected.`
- Actual: `Safe amount today is 266700; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_10`; balance `750155`; minimum `225400`; preferences `['partial_payment', 'installments']`
- Request: amount `266700` on `2024-12-06`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `6` (scheduled `0`); debits `23`; pending `0`; recurring `10`; flexible `33`; options `2`
- Critical balances: `{'2024-12-06': '744172.2096', '2025-02-10': '799398.0323846153846153846153846153846154', '2025-03-05': '882802.8849538461538461538461538461538462'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_27', False, None), ('option_payment_option_28', False, None)]`
- Validator: `True`
 
### request_11 — `amount_safe_to_pay`
- Expected: `12510645`
- Actual: `13110000`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `2025-05-03:13110000` via `full_payment`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `11`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '72034683.2', '2025-06-12': '69332215.30870085470085470085470085470083', '2025-07-31': '79173997.45973504273504273504273504273499'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '13110000', '2025-05-03', 1, '']), ('option_payment_option_29', True, [0, 0, '13110000', '2025-05-03', 1, 'payment_option_29']), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None), ('wait', True, [0, 0, '13110000', '2025-05-03', 1, ''])]`
- Validator: `True`
 
### request_11 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `affordable_now`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `2025-05-03:13110000` via `full_payment`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `11`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '72034683.2', '2025-06-12': '69332215.30870085470085470085470085470083', '2025-07-31': '79173997.45973504273504273504273504273499'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '13110000', '2025-05-03', 1, '']), ('option_payment_option_29', True, [0, 0, '13110000', '2025-05-03', 1, 'payment_option_29']), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None), ('wait', True, [0, 0, '13110000', '2025-05-03', 1, ''])]`
- Validator: `True`
 
### request_11 — `earliest_date_for_full_payment`
- Expected: `2025-07-15`
- Actual: `2025-05-03`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `2025-05-03:13110000` via `full_payment`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `11`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '72034683.2', '2025-06-12': '69332215.30870085470085470085470085470083', '2025-07-31': '79173997.45973504273504273504273504273499'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '13110000', '2025-05-03', 1, '']), ('option_payment_option_29', True, [0, 0, '13110000', '2025-05-03', 1, 'payment_option_29']), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None), ('wait', True, [0, 0, '13110000', '2025-05-03', 1, ''])]`
- Validator: `True`
 
### request_11 — `spending_changes_needed`
- Expected: `reduce_to:event_989:665950`
- Actual: `none`
- Primary root cause: **17. flexible-spending logic**
- Diagnosis: `implementation bug`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `2025-05-03:13110000` via `full_payment`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `11`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '72034683.2', '2025-06-12': '69332215.30870085470085470085470085470083', '2025-07-31': '79173997.45973504273504273504273504273499'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '13110000', '2025-05-03', 1, '']), ('option_payment_option_29', True, [0, 0, '13110000', '2025-05-03', 1, 'payment_option_29']), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None), ('wait', True, [0, 0, '13110000', '2025-05-03', 1, ''])]`
- Validator: `True`
 
### request_11 — `decision_explanation`
- Expected: `Reduce the weekend food delivery to IDR 665,950, then pay IDR 13,110,000 today. This leaves at least IDR 34,140,600 available.`
- Actual: `Plan full_payment completes 13110000 while maintaining the minimum balance; safe today: 13110000.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `2025-05-03:13110000` via `full_payment`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `11`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '72034683.2', '2025-06-12': '69332215.30870085470085470085470085470083', '2025-07-31': '79173997.45973504273504273504273504273499'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '13110000', '2025-05-03', 1, '']), ('option_payment_option_29', True, [0, 0, '13110000', '2025-05-03', 1, 'payment_option_29']), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None), ('wait', True, [0, 0, '13110000', '2025-05-03', 1, ''])]`
- Validator: `True`
 
### request_12 — `decision_explanation`
- Expected: `Use 3 installments of ZAR 22,590.19, starting 19 April 2026. This leaves at least ZAR 43,200 available.`
- Actual: `Plan installments completes 65164 while maintaining the minimum balance; safe today: 65164.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_12`; balance `193089.89`; minimum `43200`; preferences `['partial_payment', 'installments']`
- Request: amount `65164` on `2026-04-05`, deadline `2026-06-20`
- Actual selected plan: `2026-04-19:22590.19|2026-05-20:22590.19|2026-06-20:22590.19` via `installments`
- Credits `0` (scheduled `0`); debits `14`; pending `0`; recurring `8`; flexible `19`; options `3`
- Critical balances: `{'2026-04-05': '193089.89', '2026-04-19': '243233.0184444444444444444444444444444445', '2026-05-20': '275843.0585555555555555555555555555555557', '2026-06-20': '304759.2697777777777777777777777777777780', '2026-07-03': '302624.3814444444444444444444444444444447'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_33', True, [0, 0, '67770.57', '2026-04-19', 3, 'payment_option_33']), ('option_payment_option_34', False, None), ('option_payment_option_35', False, None)]`
- Validator: `True`
 
### request_13 — `amount_safe_to_pay`
- Expected: `433.4`
- Actual: `941.60`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `2024-03-07:941.60` via `full_payment`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '3813.300769230769230769230769230769230769', '2024-05-15': '3162.296923076923076923076923076923076920', '2024-06-04': '3476.032307692307692307692307692307692304'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '941.6', '2024-03-07', 1, '']), ('option_payment_option_36', True, [0, 0, '941.6', '2024-03-07', 1, 'payment_option_36']), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None), ('wait', True, [0, 0, '941.6', '2024-03-07', 1, ''])]`
- Validator: `True`
 
### request_13 — `affordability_status`
- Expected: `affordable_later`
- Actual: `affordable_now`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `2024-03-07:941.60` via `full_payment`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '3813.300769230769230769230769230769230769', '2024-05-15': '3162.296923076923076923076923076923076920', '2024-06-04': '3476.032307692307692307692307692307692304'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '941.6', '2024-03-07', 1, '']), ('option_payment_option_36', True, [0, 0, '941.6', '2024-03-07', 1, 'payment_option_36']), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None), ('wait', True, [0, 0, '941.6', '2024-03-07', 1, ''])]`
- Validator: `True`
 
### request_13 — `recommended_payment_method`
- Expected: `wait`
- Actual: `full_payment`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `2024-03-07:941.60` via `full_payment`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '3813.300769230769230769230769230769230769', '2024-05-15': '3162.296923076923076923076923076923076920', '2024-06-04': '3476.032307692307692307692307692307692304'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '941.6', '2024-03-07', 1, '']), ('option_payment_option_36', True, [0, 0, '941.6', '2024-03-07', 1, 'payment_option_36']), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None), ('wait', True, [0, 0, '941.6', '2024-03-07', 1, ''])]`
- Validator: `True`
 
### request_13 — `payment_plan`
- Expected: `2024-05-15:941.60`
- Actual: `2024-03-07:941.60`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `2024-03-07:941.60` via `full_payment`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '3813.300769230769230769230769230769230769', '2024-05-15': '3162.296923076923076923076923076923076920', '2024-06-04': '3476.032307692307692307692307692307692304'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '941.6', '2024-03-07', 1, '']), ('option_payment_option_36', True, [0, 0, '941.6', '2024-03-07', 1, 'payment_option_36']), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None), ('wait', True, [0, 0, '941.6', '2024-03-07', 1, ''])]`
- Validator: `True`
 
### request_13 — `earliest_date_for_full_payment`
- Expected: `2024-05-15`
- Actual: `2024-03-07`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `2024-03-07:941.60` via `full_payment`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '3813.300769230769230769230769230769230769', '2024-05-15': '3162.296923076923076923076923076923076920', '2024-06-04': '3476.032307692307692307692307692307692304'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '941.6', '2024-03-07', 1, '']), ('option_payment_option_36', True, [0, 0, '941.6', '2024-03-07', 1, 'payment_option_36']), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None), ('wait', True, [0, 0, '941.6', '2024-03-07', 1, ''])]`
- Validator: `True`
 
### request_13 — `decision_explanation`
- Expected: `Pay EUR 941.60 in full on 15 May 2024. Paying earlier would take the balance below the EUR 1,300 minimum.`
- Actual: `Plan full_payment completes 941.60 while maintaining the minimum balance; safe today: 941.60.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `2024-03-07:941.60` via `full_payment`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '3813.300769230769230769230769230769230769', '2024-05-15': '3162.296923076923076923076923076923076920', '2024-06-04': '3476.032307692307692307692307692307692304'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '941.6', '2024-03-07', 1, '']), ('option_payment_option_36', True, [0, 0, '941.6', '2024-03-07', 1, 'payment_option_36']), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None), ('wait', True, [0, 0, '941.6', '2024-03-07', 1, ''])]`
- Validator: `True`
 
### request_14 — `amount_safe_to_pay`
- Expected: `597.74`
- Actual: `805.35`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_14`; balance `3931.74`; minimum `2200`; preferences `['partial_payment']`
- Request: amount `5414.2` on `2025-08-04`, deadline `2025-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2025-08-04': '3931.74', '2025-10-04': '5015.788307692307692307692307692307692304', '2025-11-01': '6246.412461538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_39', False, None), ('option_payment_option_40', False, None)]`
- Validator: `True`
 
### request_14 — `decision_explanation`
- Expected: `Do not proceed with the EUR 5,414.20 request. Although EUR 597.74 is available today, the full amount cannot be completed safely within 90 days.`
- Actual: `Safe amount today is 805.35; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_14`; balance `3931.74`; minimum `2200`; preferences `['partial_payment']`
- Request: amount `5414.2` on `2025-08-04`, deadline `2025-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2025-08-04': '3931.74', '2025-10-04': '5015.788307692307692307692307692307692304', '2025-11-01': '6246.412461538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_39', False, None), ('option_payment_option_40', False, None)]`
- Validator: `True`
 
### request_15 — `amount_safe_to_pay`
- Expected: `83.05`
- Actual: `84.42`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_15`; balance `1770.05`; minimum `1200`; preferences `['partial_payment']`
- Request: amount `3685` on `2026-01-06`, deadline `2026-02-01`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `0`; recurring `9`; flexible `13`; options `3`
- Critical balances: `{'2026-01-06': '1709.9416', '2026-02-01': '2616.506830769230769230769230769230769230', '2026-04-05': '3305.519507692307692307692307692307692305'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_41', False, None), ('option_payment_option_42', False, None), ('option_payment_option_43', False, None)]`
- Validator: `True`
 
### request_15 — `decision_explanation`
- Expected: `Do not make this payment by 1 February 2026. None of the available options keeps the EUR 1,200 minimum protected.`
- Actual: `Safe amount today is 84.42; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_15`; balance `1770.05`; minimum `1200`; preferences `['partial_payment']`
- Request: amount `3685` on `2026-01-06`, deadline `2026-02-01`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `0`; recurring `9`; flexible `13`; options `3`
- Critical balances: `{'2026-01-06': '1709.9416', '2026-02-01': '2616.506830769230769230769230769230769230', '2026-04-05': '3305.519507692307692307692307692307692305'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_41', False, None), ('option_payment_option_42', False, None), ('option_payment_option_43', False, None)]`
- Validator: `True`
 
### request_16 — `decision_explanation`
- Expected: `Pay INR 122,500 today. This leaves at least INR 122,400 available over the next 90 days.`
- Actual: `Plan full_payment completes 122500 while maintaining the minimum balance; safe today: 122500.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `2023-08-12:122500` via `full_payment`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `10`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '428309.3684615384615384615384615384615385', '2023-10-11': '312479.1482051282051282051282051282051284', '2023-11-09': '307206.6164102564102564102564102564102567'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '122500', '2023-08-12', 1, '']), ('option_payment_option_44', True, [0, 0, '122500', '2023-08-12', 1, 'payment_option_44']), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None), ('wait', True, [0, 0, '122500', '2023-08-12', 1, ''])]`
- Validator: `True`
 
### request_17 — `amount_safe_to_pay`
- Expected: `243849.58`
- Actual: `261721.97`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_17`; balance `550379.58`; minimum `166100`; preferences `['installments']`
- Request: amount `274600` on `2026-03-01`, deadline `2026-05-04`
- Actual selected plan: `2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67` via `installments`
- Credits `4` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `3`
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '615433.2175213675213675213675213675213675', '2026-03-31': '576814.0050427350427350427350427350427350', '2026-04-30': '603248.4300854700854700854700854700854700', '2026-05-04': '581887.4849999999999999999999999999999999', '2026-05-29': '629682.8551282051282051282051282051282050'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_17 — `earliest_date_for_full_payment`
- Expected: `2026-03-15`
- Actual: `2026-04-15`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_17`; balance `550379.58`; minimum `166100`; preferences `['installments']`
- Request: amount `274600` on `2026-03-01`, deadline `2026-05-04`
- Actual selected plan: `2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67` via `installments`
- Credits `4` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `3`
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '615433.2175213675213675213675213675213675', '2026-03-31': '576814.0050427350427350427350427350427350', '2026-04-30': '603248.4300854700854700854700854700854700', '2026-05-04': '581887.4849999999999999999999999999999999', '2026-05-29': '629682.8551282051282051282051282051282050'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_17 — `decision_explanation`
- Expected: `Use 3 installments of INR 95,194.67, starting 1 March 2026. This leaves at least INR 166,100 available.`
- Actual: `Plan installments completes 274600 while maintaining the minimum balance; safe today: 261721.97.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_17`; balance `550379.58`; minimum `166100`; preferences `['installments']`
- Request: amount `274600` on `2026-03-01`, deadline `2026-05-04`
- Actual selected plan: `2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67` via `installments`
- Credits `4` (scheduled `1`); debits `25`; pending `0`; recurring `10`; flexible `23`; options `3`
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '615433.2175213675213675213675213675213675', '2026-03-31': '576814.0050427350427350427350427350427350', '2026-04-30': '603248.4300854700854700854700854700854700', '2026-05-04': '581887.4849999999999999999999999999999999', '2026-05-29': '629682.8551282051282051282051282051282050'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_18 — `amount_safe_to_pay`
- Expected: `462`
- Actual: `755.15`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `2026-09-13:3246.1` via `wait`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `9`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-13': '6584.091606837606837606837606837606837608', '2026-09-15': '6584.091606837606837606837606837606837608', '2026-10-04': '6100.762461538461538461538461538461538463'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None), ('wait', True, [0, 0, '3246.1', '2026-09-13', 1, ''])]`
- Validator: `True`
 
### request_18 — `payment_plan`
- Expected: `2026-09-15:3246.10`
- Actual: `2026-09-13:3246.1`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `2026-09-13:3246.1` via `wait`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `9`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-13': '6584.091606837606837606837606837606837608', '2026-09-15': '6584.091606837606837606837606837606837608', '2026-10-04': '6100.762461538461538461538461538461538463'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None), ('wait', True, [0, 0, '3246.1', '2026-09-13', 1, ''])]`
- Validator: `True`
 
### request_18 — `earliest_date_for_full_payment`
- Expected: `2026-09-15`
- Actual: `2026-09-13`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `2026-09-13:3246.1` via `wait`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `9`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-13': '6584.091606837606837606837606837606837608', '2026-09-15': '6584.091606837606837606837606837606837608', '2026-10-04': '6100.762461538461538461538461538461538463'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None), ('wait', True, [0, 0, '3246.1', '2026-09-13', 1, ''])]`
- Validator: `True`
 
### request_18 — `decision_explanation`
- Expected: `Pay EUR 3,246.10 in full on 15 September 2026. Paying earlier would take the balance below the EUR 1,400 minimum.`
- Actual: `Plan wait completes 3246.1 while maintaining the minimum balance; safe today: 755.15.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `2026-09-13:3246.1` via `wait`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `9`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-13': '6584.091606837606837606837606837606837608', '2026-09-15': '6584.091606837606837606837606837606837608', '2026-10-04': '6100.762461538461538461538461538461538463'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None), ('wait', True, [0, 0, '3246.1', '2026-09-13', 1, ''])]`
- Validator: `True`
 
### request_19 — `amount_safe_to_pay`
- Expected: `28820`
- Actual: `39660`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `2024-09-04:20623.2|2024-10-02:20623.2` via `installments`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-02': '259922.0233846153846153846153846153846152', '2024-10-04': '223822.0233846153846153846153846153846152', '2024-12-02': '308476.0701538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', True, [0, 0, '41246.4', '2024-09-04', 2, 'payment_option_53']), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `recommended_payment_method`
- Expected: `partial_payment`
- Actual: `installments`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `2024-09-04:20623.2|2024-10-02:20623.2` via `installments`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-02': '259922.0233846153846153846153846153846152', '2024-10-04': '223822.0233846153846153846153846153846152', '2024-12-02': '308476.0701538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', True, [0, 0, '41246.4', '2024-09-04', 2, 'payment_option_53']), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `payment_plan`
- Expected: `2024-09-04:28820|2024-09-15:10840`
- Actual: `2024-09-04:20623.2|2024-10-02:20623.2`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `2024-09-04:20623.2|2024-10-02:20623.2` via `installments`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-02': '259922.0233846153846153846153846153846152', '2024-10-04': '223822.0233846153846153846153846153846152', '2024-12-02': '308476.0701538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', True, [0, 0, '41246.4', '2024-09-04', 2, 'payment_option_53']), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `earliest_date_for_full_payment`
- Expected: `2024-09-15`
- Actual: `2024-09-04`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `2024-09-04:20623.2|2024-10-02:20623.2` via `installments`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-02': '259922.0233846153846153846153846153846152', '2024-10-04': '223822.0233846153846153846153846153846152', '2024-12-02': '308476.0701538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', True, [0, 0, '41246.4', '2024-09-04', 2, 'payment_option_53']), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `decision_explanation`
- Expected: `Pay INR 28,820 today and the remaining INR 10,840 on 15 September 2024. This completes the full request and keeps the INR 92,800 minimum protected.`
- Actual: `Plan installments completes 39660 while maintaining the minimum balance; safe today: 39660.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `2024-09-04:20623.2|2024-10-02:20623.2` via `installments`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-02': '259922.0233846153846153846153846153846152', '2024-10-04': '223822.0233846153846153846153846153846152', '2024-12-02': '308476.0701538461538461538461538461538456'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', True, [0, 0, '41246.4', '2024-09-04', 2, 'payment_option_53']), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_20 — `amount_safe_to_pay`
- Expected: `5400`
- Actual: `37405`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_20`; balance `102609.05`; minimum `64500`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `303700` on `2026-02-07`, deadline `2026-02-22`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `3`; recurring `11`; flexible `19`; options `2`
- Critical balances: `{'2026-02-07': '102609.05', '2026-02-08': '91802.204', '2026-02-09': '87397.62677777777777777777777777777777778', '2026-02-14': '190209.6809316239316239316239316239316239', '2026-02-22': '183085.3625982905982905982905982905982906', '2026-05-07': '282518.5934786324786324786324786324786329'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_55', False, None), ('option_payment_option_56', False, None)]`
- Validator: `True`
 
### request_20 — `decision_explanation`
- Expected: `Do not make this payment by 22 February 2026. None of the available options keeps the INR 64,500 minimum protected.`
- Actual: `Safe amount today is 37405; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_20`; balance `102609.05`; minimum `64500`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `303700` on `2026-02-07`, deadline `2026-02-22`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `3`; recurring `11`; flexible `19`; options `2`
- Critical balances: `{'2026-02-07': '102609.05', '2026-02-08': '91802.204', '2026-02-09': '87397.62677777777777777777777777777777778', '2026-02-14': '190209.6809316239316239316239316239316239', '2026-02-22': '183085.3625982905982905982905982905982906', '2026-05-07': '282518.5934786324786324786324786324786329'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_55', False, None), ('option_payment_option_56', False, None)]`
- Validator: `True`
 
### request_21 — `amount_safe_to_pay`
- Expected: `1543.35`
- Actual: `1574.4`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_21`; balance `3911.35`; minimum `1800`; preferences `['full_payment']`
- Request: amount `1574.4` on `2026-04-03`, deadline `2026-04-14`
- Actual selected plan: `2026-04-03:1574.4` via `full_payment`
- Credits `2` (scheduled `1`); debits `15`; pending `1`; recurring `9`; flexible `24`; options `4`
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3470.227666666666666666666666666666666667', '2026-04-15': '5726.227666666666666666666666666666666667', '2026-07-01': '7019.338777777777777777777777777777777779'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_21 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `affordable_now`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_21`; balance `3911.35`; minimum `1800`; preferences `['full_payment']`
- Request: amount `1574.4` on `2026-04-03`, deadline `2026-04-14`
- Actual selected plan: `2026-04-03:1574.4` via `full_payment`
- Credits `2` (scheduled `1`); debits `15`; pending `1`; recurring `9`; flexible `24`; options `4`
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3470.227666666666666666666666666666666667', '2026-04-15': '5726.227666666666666666666666666666666667', '2026-07-01': '7019.338777777777777777777777777777777779'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_21 — `payment_plan`
- Expected: `2026-04-03:1574.40`
- Actual: `2026-04-03:1574.4`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_21`; balance `3911.35`; minimum `1800`; preferences `['full_payment']`
- Request: amount `1574.4` on `2026-04-03`, deadline `2026-04-14`
- Actual selected plan: `2026-04-03:1574.4` via `full_payment`
- Credits `2` (scheduled `1`); debits `15`; pending `1`; recurring `9`; flexible `24`; options `4`
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3470.227666666666666666666666666666666667', '2026-04-15': '5726.227666666666666666666666666666666667', '2026-07-01': '7019.338777777777777777777777777777777779'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_21 — `earliest_date_for_full_payment`
- Expected: `2026-04-15`
- Actual: `2026-04-03`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_21`; balance `3911.35`; minimum `1800`; preferences `['full_payment']`
- Request: amount `1574.4` on `2026-04-03`, deadline `2026-04-14`
- Actual selected plan: `2026-04-03:1574.4` via `full_payment`
- Credits `2` (scheduled `1`); debits `15`; pending `1`; recurring `9`; flexible `24`; options `4`
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3470.227666666666666666666666666666666667', '2026-04-15': '5726.227666666666666666666666666666666667', '2026-07-01': '7019.338777777777777777777777777777777779'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_21 — `spending_changes_needed`
- Expected: `stop:event_1815|reduce_to:event_1816:23.50`
- Actual: `none`
- Primary root cause: **17. flexible-spending logic**
- Diagnosis: `implementation bug`
- User/profile: `user_21`; balance `3911.35`; minimum `1800`; preferences `['full_payment']`
- Request: amount `1574.4` on `2026-04-03`, deadline `2026-04-14`
- Actual selected plan: `2026-04-03:1574.4` via `full_payment`
- Credits `2` (scheduled `1`); debits `15`; pending `1`; recurring `9`; flexible `24`; options `4`
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3470.227666666666666666666666666666666667', '2026-04-15': '5726.227666666666666666666666666666666667', '2026-07-01': '7019.338777777777777777777777777777777779'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_21 — `decision_explanation`
- Expected: `Stop the online backup subscription and reduce the streaming subscription to USD 23.50, then pay USD 1,574.40 today. This leaves at least USD 1,800 available.`
- Actual: `Plan full_payment completes 1574.4 while maintaining the minimum balance; safe today: 1574.4.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_21`; balance `3911.35`; minimum `1800`; preferences `['full_payment']`
- Request: amount `1574.4` on `2026-04-03`, deadline `2026-04-14`
- Actual selected plan: `2026-04-03:1574.4` via `full_payment`
- Credits `2` (scheduled `1`); debits `15`; pending `1`; recurring `9`; flexible `24`; options `4`
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3470.227666666666666666666666666666666667', '2026-04-15': '5726.227666666666666666666666666666666667', '2026-07-01': '7019.338777777777777777777777777777777779'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_22 — `amount_safe_to_pay`
- Expected: `475.46`
- Actual: `549.9`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `2024-12-08:253.59|2025-01-05:253.59|2025-02-02:253.59` via `installments`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1119.3272', '2024-12-08': '1048.9872', '2025-01-05': '1257.430000000000000000000000000000000000', '2025-02-02': '1616.732800000000000000000000000000000000', '2025-02-10': '1358.033846153846153846153846153846153846', '2025-03-04': '1797.835600000000000000000000000000000000'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', True, [0, 0, '760.77', '2024-12-08', 3, 'payment_option_61']), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `earliest_date_for_full_payment`
- Expected: `2025-01-15`
- Actual: `2025-01-16`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `2024-12-08:253.59|2025-01-05:253.59|2025-02-02:253.59` via `installments`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1119.3272', '2024-12-08': '1048.9872', '2025-01-05': '1257.430000000000000000000000000000000000', '2025-02-02': '1616.732800000000000000000000000000000000', '2025-02-10': '1358.033846153846153846153846153846153846', '2025-03-04': '1797.835600000000000000000000000000000000'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', True, [0, 0, '760.77', '2024-12-08', 3, 'payment_option_61']), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `decision_explanation`
- Expected: `Use 3 installments of EUR 253.59, starting 8 December 2024. This leaves at least EUR 500 available.`
- Actual: `Plan installments completes 731.5 while maintaining the minimum balance; safe today: 549.9.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `2024-12-08:253.59|2025-01-05:253.59|2025-02-02:253.59` via `installments`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1119.3272', '2024-12-08': '1048.9872', '2025-01-05': '1257.430000000000000000000000000000000000', '2025-02-02': '1616.732800000000000000000000000000000000', '2025-02-10': '1358.033846153846153846153846153846153846', '2025-03-04': '1797.835600000000000000000000000000000000'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', True, [0, 0, '760.77', '2024-12-08', 3, 'payment_option_61']), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_23 — `amount_safe_to_pay`
- Expected: `9152`
- Actual: `11407.59`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '50225.424', '2025-05-11': '45992.074', '2025-07-15': '49386.66174358974358974358974358974358976', '2025-08-04': '83178.96435897435897435897435897435897438'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_23 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '50225.424', '2025-05-11': '45992.074', '2025-07-15': '49386.66174358974358974358974358974358976', '2025-08-04': '83178.96435897435897435897435897435897438'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_23 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '50225.424', '2025-05-11': '45992.074', '2025-07-15': '49386.66174358974358974358974358974358976', '2025-08-04': '83178.96435897435897435897435897435897438'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_23 — `payment_plan`
- Expected: `2025-07-15:38016`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '50225.424', '2025-05-11': '45992.074', '2025-07-15': '49386.66174358974358974358974358974358976', '2025-08-04': '83178.96435897435897435897435897435897438'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_23 — `earliest_date_for_full_payment`
- Expected: `2025-07-15`
- Actual: `2025-07-17`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '50225.424', '2025-05-11': '45992.074', '2025-07-15': '49386.66174358974358974358974358974358976', '2025-08-04': '83178.96435897435897435897435897435897438'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_23 — `decision_explanation`
- Expected: `Pay ZAR 38,016 in full on 15 July 2025. Paying earlier would take the balance below the ZAR 27,000 minimum.`
- Actual: `Safe amount today is 11407.59; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `10`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '50225.424', '2025-05-11': '45992.074', '2025-07-15': '49386.66174358974358974358974358974358976', '2025-08-04': '83178.96435897435897435897435897435897438'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None), ('wait', False, None)]`
- Validator: `True`
 
### request_24 — `amount_safe_to_pay`
- Expected: `13420`
- Actual: `26006.51`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_24`; balance `85045`; minimum `51000`; preferences `['partial_payment']`
- Request: amount `109600` on `2026-01-04`, deadline `2026-02-08`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `0`); debits `29`; pending `0`; recurring `11`; flexible `36`; options `2`
- Critical balances: `{'2026-01-04': '81554.5', '2026-01-11': '70152.38573504273504273504273504273504274', '2026-02-08': '83489.79178632478632478632478632478632467', '2026-04-03': '129561.2621538461538461538461538461538457'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_67', False, None), ('option_payment_option_68', False, None)]`
- Validator: `True`
 
### request_24 — `decision_explanation`
- Expected: `Do not proceed with the INR 109,600 request. Although INR 13,420 is available today, the full amount cannot be completed safely within 90 days.`
- Actual: `Safe amount today is 26006.51; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_24`; balance `85045`; minimum `51000`; preferences `['partial_payment']`
- Request: amount `109600` on `2026-01-04`, deadline `2026-02-08`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `0`); debits `29`; pending `0`; recurring `11`; flexible `36`; options `2`
- Critical balances: `{'2026-01-04': '81554.5', '2026-01-11': '70152.38573504273504273504273504273504274', '2026-02-08': '83489.79178632478632478632478632478632467', '2026-04-03': '129561.2621538461538461538461538461538457'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_67', False, None), ('option_payment_option_68', False, None)]`
- Validator: `True`
 
### request_25 — `amount_safe_to_pay`
- Expected: `1425000`
- Actual: `5284985.18`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_25`; balance `32063050`; minimum `23379100`; preferences `['full_payment', 'installments']`
- Request: amount `60496000` on `2024-03-06`, deadline `2024-04-17`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `28`; pending `0`; recurring `11`; flexible `0`; options `3`
- Critical balances: `{'2024-03-06': '31028372.6136', '2024-03-15': '52244009.72631111111111111111111111111112', '2024-04-17': '56679358.27964444444444444444444444444448', '2024-06-03': '56363738.83374444444444444444444444444452'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_69', False, None), ('option_payment_option_70', False, None), ('option_payment_option_71', False, None)]`
- Validator: `True`
 
### request_25 — `decision_explanation`
- Expected: `Do not make this payment by 17 April 2024. None of the available options keeps the IDR 23,379,100 minimum protected.`
- Actual: `Safe amount today is 5284985.18; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_25`; balance `32063050`; minimum `23379100`; preferences `['full_payment', 'installments']`
- Request: amount `60496000` on `2024-03-06`, deadline `2024-04-17`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `28`; pending `0`; recurring `11`; flexible `0`; options `3`
- Critical balances: `{'2024-03-06': '31028372.6136', '2024-03-15': '52244009.72631111111111111111111111111112', '2024-04-17': '56679358.27964444444444444444444444444448', '2024-06-03': '56363738.83374444444444444444444444444452'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_69', False, None), ('option_payment_option_70', False, None), ('option_payment_option_71', False, None)]`
- Validator: `True`
 
## Mathematical safe-amount traces

Representative traces show deterministic date-by-date balances; expected amounts are comparison-only.
### request_01
Expected `25256`; actual `23292.94`; baseline minimum `27942.08487179487179487179487179487179488`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2024-03-03 | 58481.1 | 33225.1 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-04 | 58481.1 | 33225.1 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-05 | 57913.5 | 32657.5 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-06 | 57913.5 | 32657.5 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-07 | 57913.5 | 32657.5 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-08 | 55742.19269230769230769230769230769230769 | 30486.19269230769230769230769230769230769 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-09 | 55742.19269230769230769230769230769230769 | 30486.19269230769230769230769230769230769 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-10 | 52831.40423076923076923076923076923076923 | 27575.40423076923076923076923076923076923 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-11 | 52831.40423076923076923076923076923076923 | 27575.40423076923076923076923076923076923 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-12 | 52387.45200854700854700854700854700854701 | 27131.45200854700854700854700854700854701 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-13 | 48665.05200854700854700854700854700854701 | 23409.05200854700854700854700854700854701 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-14 | 48665.05200854700854700854700854700854701 | 23409.05200854700854700854700854700854701 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-15 | 70893.01470085470085470085470085470085470 | 45637.01470085470085470085470085470085470 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-16 | 70893.01470085470085470085470085470085470 | 45637.01470085470085470085470085470085470 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-17 | 70893.01470085470085470085470085470085470 | 45637.01470085470085470085470085470085470 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-18 | 70893.01470085470085470085470085470085470 | 45637.01470085470085470085470085470085470 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-19 | 70449.06247863247863247863247863247863248 | 45193.06247863247863247863247863247863248 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-20 | 70449.06247863247863247863247863247863248 | 45193.06247863247863247863247863247863248 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-21 | 70449.06247863247863247863247863247863248 | 45193.06247863247863247863247863247863248 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-22 | 69663.92517094017094017094017094017094017 | 44407.92517094017094017094017094017094017 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-23 | 69663.92517094017094017094017094017094017 | 44407.92517094017094017094017094017094017 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-24 | 68574.73670940170940170940170940170940171 | 43318.73670940170940170940170940170940171 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-25 | 68574.73670940170940170940170940170940171 | 43318.73670940170940170940170940170940171 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-26 | 68130.78448717948717948717948717948717949 | 42874.78448717948717948717948717948717949 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-27 | 68130.78448717948717948717948717948717949 | 42874.78448717948717948717948717948717949 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-28 | 68130.78448717948717948717948717948717949 | 42874.78448717948717948717948717948717949 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-29 | 67345.64717948717948717948717948717948718 | 42089.64717948717948717948717948717948718 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-30 | 67345.64717948717948717948717948717948718 | 42089.64717948717948717948717948717948718 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-31 | 67345.64717948717948717948717948717948718 | 42089.64717948717948717948717948717948718 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-01 | 67345.64717948717948717948717948717948718 | 42089.64717948717948717948717948717948718 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-02 | 61753.69495726495726495726495726495726496 | 36497.69495726495726495726495726495726496 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-03 | 61753.69495726495726495726495726495726496 | 36497.69495726495726495726495726495726496 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-04 | 61753.69495726495726495726495726495726496 | 36497.69495726495726495726495726495726496 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-05 | 60968.55764957264957264957264957264957265 | 35712.55764957264957264957264957264957265 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-06 | 60968.55764957264957264957264957264957265 | 35712.55764957264957264957264957264957265 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-07 | 59879.36918803418803418803418803418803419 | 34623.36918803418803418803418803418803419 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-08 | 58493.19918803418803418803418803418803419 | 33237.19918803418803418803418803418803419 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-09 | 58049.24696581196581196581196581196581197 | 32793.24696581196581196581196581196581197 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-10 | 56227.64696581196581196581196581196581197 | 30971.64696581196581196581196581196581197 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-11 | 56227.64696581196581196581196581196581197 | 30971.64696581196581196581196581196581197 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-12 | 55442.50965811965811965811965811965811966 | 30186.50965811965811965811965811965811966 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-13 | 51720.10965811965811965811965811965811966 | 26464.10965811965811965811965811965811966 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-14 | 51720.10965811965811965811965811965811966 | 26464.10965811965811965811965811965811966 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-15 | 51413.20965811965811965811965811965811966 | 26157.20965811965811965811965811965811966 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-16 | 50969.25743589743589743589743589743589744 | 25713.25743589743589743589743589743589744 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-17 | 50969.25743589743589743589743589743589744 | 25713.25743589743589743589743589743589744 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-18 | 50969.25743589743589743589743589743589744 | 25713.25743589743589743589743589743589744 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-19 | 50184.12012820512820512820512820512820513 | 24928.12012820512820512820512820512820513 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-20 | 50184.12012820512820512820512820512820513 | 24928.12012820512820512820512820512820513 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-21 | 49094.93166666666666666666666666666666667 | 23838.93166666666666666666666666666666667 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-22 | 49094.93166666666666666666666666666666667 | 23838.93166666666666666666666666666666667 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-23 | 48650.97944444444444444444444444444444445 | 23394.97944444444444444444444444444444445 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-24 | 48650.97944444444444444444444444444444445 | 23394.97944444444444444444444444444444445 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-25 | 48650.97944444444444444444444444444444445 | 23394.97944444444444444444444444444444445 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-26 | 47865.84213675213675213675213675213675214 | 22609.84213675213675213675213675213675214 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-27 | 47865.84213675213675213675213675213675214 | 22609.84213675213675213675213675213675214 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-28 | 47865.84213675213675213675213675213675214 | 22609.84213675213675213675213675213675214 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-29 | 47865.84213675213675213675213675213675214 | 22609.84213675213675213675213675213675214 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-30 | 47421.88991452991452991452991452991452992 | 22165.88991452991452991452991452991452992 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-01 | 47421.88991452991452991452991452991452992 | 22165.88991452991452991452991452991452992 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-02 | 47421.88991452991452991452991452991452992 | 22165.88991452991452991452991452991452992 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-03 | 41488.75260683760683760683760683760683761 | 16232.75260683760683760683760683760683761 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-04 | 41488.75260683760683760683760683760683761 | 16232.75260683760683760683760683760683761 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-05 | 40399.56414529914529914529914529914529915 | 15143.56414529914529914529914529914529915 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-06 | 40399.56414529914529914529914529914529915 | 15143.56414529914529914529914529914529915 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-07 | 39955.61192307692307692307692307692307693 | 14699.61192307692307692307692307692307693 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-08 | 39955.61192307692307692307692307692307693 | 14699.61192307692307692307692307692307693 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-09 | 38569.44192307692307692307692307692307693 | 13313.44192307692307692307692307692307693 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-10 | 37784.30461538461538461538461538461538462 | 12528.30461538461538461538461538461538462 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-11 | 35962.70461538461538461538461538461538462 | 10706.70461538461538461538461538461538462 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-12 | 35962.70461538461538461538461538461538462 | 10706.70461538461538461538461538461538462 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-13 | 35962.70461538461538461538461538461538462 | 10706.70461538461538461538461538461538462 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-14 | 31796.35239316239316239316239316239316240 | 6540.35239316239316239316239316239316240 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-15 | 31796.35239316239316239316239316239316240 | 6540.35239316239316239316239316239316240 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-16 | 31489.45239316239316239316239316239316240 | 6233.45239316239316239316239316239316240 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-17 | 30704.31508547008547008547008547008547009 | 5448.31508547008547008547008547008547009 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-18 | 30704.31508547008547008547008547008547009 | 5448.31508547008547008547008547008547009 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-19 | 29615.12662393162393162393162393162393163 | 4359.12662393162393162393162393162393163 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-20 | 29615.12662393162393162393162393162393163 | 4359.12662393162393162393162393162393163 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-21 | 29171.17440170940170940170940170940170941 | 3915.17440170940170940170940170940170941 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-22 | 29171.17440170940170940170940170940170941 | 3915.17440170940170940170940170940170941 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-23 | 29171.17440170940170940170940170940170941 | 3915.17440170940170940170940170940170941 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-24 | 28386.03709401709401709401709401709401710 | 3130.03709401709401709401709401709401710 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-25 | 28386.03709401709401709401709401709401710 | 3130.03709401709401709401709401709401710 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-26 | 28386.03709401709401709401709401709401710 | 3130.03709401709401709401709401709401710 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-27 | 28386.03709401709401709401709401709401710 | 3130.03709401709401709401709401709401710 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-28 | 27942.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-29 | 27942.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-30 | 27942.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-31 | 27942.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | 2686.08487179487179487179487179487179488 | False |

### request_02
Expected `17229139.2`; actual `24911239.26`; baseline minimum `47389146.03805128205128205128205128205128`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2025-08-05 | 60383889.2 | 14365889.2 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-06 | 58242039.26 | 12224039.26 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-07 | 57109639.26 | 11091639.26 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-08 | 52418539.26 | 6400539.26 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-09 | 50509657.95666666666666666666666666666667 | 4491657.95666666666666666666666666666667 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-10 | 48970663.98266666666666666666666666666667 | 2952663.98266666666666666666666666666667 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-11 | 48970663.98266666666666666666666666666667 | 2952663.98266666666666666666666666666667 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-12 | 47389146.03805128205128205128205128205128 | 1371146.03805128205128205128205128205128 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-13 | 47389146.03805128205128205128205128205128 | 1371146.03805128205128205128205128205128 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-14 | 79435974.34605128205128205128205128205128 | 33417974.34605128205128205128205128205128 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-15 | 79435974.34605128205128205128205128205128 | 33417974.34605128205128205128205128205128 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-16 | 79435974.34605128205128205128205128205128 | 33417974.34605128205128205128205128205128 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-17 | 79435974.34605128205128205128205128205128 | 33417974.34605128205128205128205128205128 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-18 | 79435974.34605128205128205128205128205128 | 33417974.34605128205128205128205128205128 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-19 | 77527093.04271794871794871794871794871795 | 31509093.04271794871794871794871794871795 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-20 | 76443273.59160683760683760683760683760684 | 30425273.59160683760683760683760683760684 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-21 | 76443273.59160683760683760683760683760684 | 30425273.59160683760683760683760683760684 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-22 | 76443273.59160683760683760683760683760684 | 30425273.59160683760683760683760683760684 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-23 | 76443273.59160683760683760683760683760684 | 30425273.59160683760683760683760683760684 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-24 | 76443273.59160683760683760683760683760684 | 30425273.59160683760683760683760683760684 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-25 | 76443273.59160683760683760683760683760684 | 30425273.59160683760683760683760683760684 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-26 | 75231305.64699145299145299145299145299146 | 29213305.64699145299145299145299145299146 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-27 | 75231305.64699145299145299145299145299146 | 29213305.64699145299145299145299145299146 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-28 | 75231305.64699145299145299145299145299146 | 29213305.64699145299145299145299145299146 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-29 | 73322424.34365811965811965811965811965813 | 27304424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-30 | 73322424.34365811965811965811965811965813 | 27304424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-31 | 73322424.34365811965811965811965811965813 | 27304424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-01 | 73322424.34365811965811965811965811965813 | 27304424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-02 | 73322424.34365811965811965811965811965813 | 27304424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-03 | 73322424.34365811965811965811965811965813 | 27304424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-04 | 69788424.34365811965811965811965811965813 | 23770424.34365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-05 | 67646574.40365811965811965811965811965813 | 21628574.40365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-06 | 66514174.40365811965811965811965811965813 | 20496174.40365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-07 | 63474174.40365811965811965811965811965813 | 17456174.40365811965811965811965811965813 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-08 | 61565293.10032478632478632478632478632480 | 15547293.10032478632478632478632478632480 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-09 | 58814331.18170940170940170940170940170942 | 12796331.18170940170940170940170940170942 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-10 | 57730511.73059829059829059829059829059831 | 11712511.73059829059829059829059829059831 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-11 | 57360961.73059829059829059829059829059831 | 11342961.73059829059829059829059829059831 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-12 | 57360961.73059829059829059829059829059831 | 11342961.73059829059829059829059829059831 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-13 | 89407790.03859829059829059829059829059831 | 43389790.03859829059829059829059829059831 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-14 | 89407790.03859829059829059829059829059831 | 43389790.03859829059829059829059829059831 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-15 | 89407790.03859829059829059829059829059831 | 43389790.03859829059829059829059829059831 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-16 | 89407790.03859829059829059829059829059831 | 43389790.03859829059829059829059829059831 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-17 | 89407790.03859829059829059829059829059831 | 43389790.03859829059829059829059829059831 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-18 | 87498908.73526495726495726495726495726498 | 41480908.73526495726495726495726495726498 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-19 | 87498908.73526495726495726495726495726498 | 41480908.73526495726495726495726495726498 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-20 | 87498908.73526495726495726495726495726498 | 41480908.73526495726495726495726495726498 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-21 | 87498908.73526495726495726495726495726498 | 41480908.73526495726495726495726495726498 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-22 | 87498908.73526495726495726495726495726498 | 41480908.73526495726495726495726495726498 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-23 | 86286940.79064957264957264957264957264960 | 40268940.79064957264957264957264957264960 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-24 | 86286940.79064957264957264957264957264960 | 40268940.79064957264957264957264957264960 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-25 | 86286940.79064957264957264957264957264960 | 40268940.79064957264957264957264957264960 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-26 | 86286940.79064957264957264957264957264960 | 40268940.79064957264957264957264957264960 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-27 | 86286940.79064957264957264957264957264960 | 40268940.79064957264957264957264957264960 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-28 | 84378059.48731623931623931623931623931627 | 38360059.48731623931623931623931623931627 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-29 | 84378059.48731623931623931623931623931627 | 38360059.48731623931623931623931623931627 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-30 | 84378059.48731623931623931623931623931627 | 38360059.48731623931623931623931623931627 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-01 | 83294240.03620512820512820512820512820516 | 37276240.03620512820512820512820512820516 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-02 | 83294240.03620512820512820512820512820516 | 37276240.03620512820512820512820512820516 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-03 | 83294240.03620512820512820512820512820516 | 37276240.03620512820512820512820512820516 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-04 | 83294240.03620512820512820512820512820516 | 37276240.03620512820512820512820512820516 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-05 | 77618390.09620512820512820512820512820516 | 31600390.09620512820512820512820512820516 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-06 | 76485990.09620512820512820512820512820516 | 30467990.09620512820512820512820512820516 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-07 | 72234022.15158974358974358974358974358978 | 26216022.15158974358974358974358974358978 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-08 | 70325140.84825641025641025641025641025645 | 24307140.84825641025641025641025641025645 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-09 | 68786146.87425641025641025641025641025645 | 22768146.87425641025641025641025641025645 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-10 | 68786146.87425641025641025641025641025645 | 22768146.87425641025641025641025641025645 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-11 | 68416596.87425641025641025641025641025645 | 22398596.87425641025641025641025641025645 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-12 | 68416596.87425641025641025641025641025645 | 22398596.87425641025641025641025641025645 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-13 | 100463425.1822564102564102564102564102564 | 54445425.1822564102564102564102564102564 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-14 | 100463425.1822564102564102564102564102564 | 54445425.1822564102564102564102564102564 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-15 | 100463425.1822564102564102564102564102564 | 54445425.1822564102564102564102564102564 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-16 | 100463425.1822564102564102564102564102564 | 54445425.1822564102564102564102564102564 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-17 | 100463425.1822564102564102564102564102564 | 54445425.1822564102564102564102564102564 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-18 | 98554543.87892307692307692307692307692307 | 52536543.87892307692307692307692307692307 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-19 | 98554543.87892307692307692307692307692307 | 52536543.87892307692307692307692307692307 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-20 | 98554543.87892307692307692307692307692307 | 52536543.87892307692307692307692307692307 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-21 | 97342575.93430769230769230769230769230768 | 51324575.93430769230769230769230769230768 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-22 | 96258756.48319658119658119658119658119657 | 50240756.48319658119658119658119658119657 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-23 | 96258756.48319658119658119658119658119657 | 50240756.48319658119658119658119658119657 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-24 | 96258756.48319658119658119658119658119657 | 50240756.48319658119658119658119658119657 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-25 | 96258756.48319658119658119658119658119657 | 50240756.48319658119658119658119658119657 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-26 | 96258756.48319658119658119658119658119657 | 50240756.48319658119658119658119658119657 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-27 | 96258756.48319658119658119658119658119657 | 50240756.48319658119658119658119658119657 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-28 | 94349875.17986324786324786324786324786324 | 48331875.17986324786324786324786324786324 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-29 | 94349875.17986324786324786324786324786324 | 48331875.17986324786324786324786324786324 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-30 | 94349875.17986324786324786324786324786324 | 48331875.17986324786324786324786324786324 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-31 | 94349875.17986324786324786324786324786324 | 48331875.17986324786324786324786324786324 | 47389146.03805128205128205128205128205128 | True |
| 2025-11-01 | 94349875.17986324786324786324786324786324 | 48331875.17986324786324786324786324786324 | 47389146.03805128205128205128205128205128 | True |
| 2025-11-02 | 94349875.17986324786324786324786324786324 | 48331875.17986324786324786324786324786324 | 47389146.03805128205128205128205128205128 | True |

### request_03
Expected `873000`; actual `1159761.09`; baseline minimum `3185109.625555555555555555555555555555555`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2019-09-03 | 4670300 | -820700 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-04 | 4670300 | -820700 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-05 | 4670300 | -820700 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-06 | 4670300 | -820700 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-07 | 4312955.45 | -1178044.55 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-08 | 4119790.664444444444444444444444444444444 | -1371209.335555555555555555555555555555556 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-09 | 4119790.664444444444444444444444444444444 | -1371209.335555555555555555555555555555556 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-10 | 4001990.664444444444444444444444444444444 | -1489009.335555555555555555555555555555556 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-11 | 4001990.664444444444444444444444444444444 | -1489009.335555555555555555555555555555556 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-12 | 4001990.664444444444444444444444444444444 | -1489009.335555555555555555555555555555556 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-13 | 3812392.914444444444444444444444444444444 | -1678607.085555555555555555555555555555556 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-14 | 3662480.261111111111111111111111111111111 | -1828519.738888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-15 | 3662480.261111111111111111111111111111111 | -1828519.738888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-16 | 3662480.261111111111111111111111111111111 | -1828519.738888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-17 | 3662480.261111111111111111111111111111111 | -1828519.738888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-18 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-19 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-20 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-21 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-22 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-23 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-24 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-25 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-26 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-27 | 3378274.411111111111111111111111111111111 | -2112725.588888888888888888888888888888889 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-28 | 3185109.625555555555555555555555555555555 | -2305890.374444444444444444444444444444445 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-29 | 3185109.625555555555555555555555555555555 | -2305890.374444444444444444444444444444445 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-30 | 7550109.625555555555555555555555555555555 | 2059109.625555555555555555555555555555555 | -620993.402222222222222222222222222222223 | False |
| 2019-10-01 | 7550109.625555555555555555555555555555555 | 2059109.625555555555555555555555555555555 | -620993.402222222222222222222222222222223 | False |
| 2019-10-02 | 7550109.625555555555555555555555555555555 | 2059109.625555555555555555555555555555555 | -620993.402222222222222222222222222222223 | False |
| 2019-10-03 | 6410109.625555555555555555555555555555555 | 919109.625555555555555555555555555555555 | -620993.402222222222222222222222222222223 | False |
| 2019-10-04 | 6410109.625555555555555555555555555555555 | 919109.625555555555555555555555555555555 | -620993.402222222222222222222222222222223 | False |
| 2019-10-05 | 6260196.972222222222222222222222222222222 | 769196.972222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-06 | 6260196.972222222222222222222222222222222 | 769196.972222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-07 | 5997852.422222222222222222222222222222222 | 506852.422222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-08 | 5804687.636666666666666666666666666666666 | 313687.636666666666666666666666666666666 | -620993.402222222222222222222222222222223 | False |
| 2019-10-09 | 5713646.572222222222222222222222222222222 | 222646.572222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-10 | 5595846.572222222222222222222222222222222 | 104846.572222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-11 | 5595846.572222222222222222222222222222222 | 104846.572222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-12 | 5595846.572222222222222222222222222222222 | 104846.572222222222222222222222222222222 | -620993.402222222222222222222222222222223 | False |
| 2019-10-13 | 5406248.822222222222222222222222222222222 | -84751.177777777777777777777777777777778 | -620993.402222222222222222222222222222223 | False |
| 2019-10-14 | 5406248.822222222222222222222222222222222 | -84751.177777777777777777777777777777778 | -620993.402222222222222222222222222222223 | False |
| 2019-10-15 | 5406248.822222222222222222222222222222222 | -84751.177777777777777777777777777777778 | -620993.402222222222222222222222222222223 | False |
| 2019-10-16 | 5406248.822222222222222222222222222222222 | -84751.177777777777777777777777777777778 | -620993.402222222222222222222222222222223 | False |
| 2019-10-17 | 5406248.822222222222222222222222222222222 | -84751.177777777777777777777777777777778 | -620993.402222222222222222222222222222223 | False |
| 2019-10-18 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-19 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-20 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-21 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-22 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-23 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-24 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-25 | 5213084.036666666666666666666666666666666 | -277915.963333333333333333333333333333334 | -620993.402222222222222222222222222222223 | False |
| 2019-10-26 | 5063171.383333333333333333333333333333333 | -427828.616666666666666666666666666666667 | -620993.402222222222222222222222222222223 | False |
| 2019-10-27 | 5063171.383333333333333333333333333333333 | -427828.616666666666666666666666666666667 | -620993.402222222222222222222222222222223 | False |
| 2019-10-28 | 4870006.597777777777777777777777777777777 | -620993.402222222222222222222222222222223 | -620993.402222222222222222222222222222223 | False |
| 2019-10-29 | 4870006.597777777777777777777777777777777 | -620993.402222222222222222222222222222223 | -620993.402222222222222222222222222222223 | False |
| 2019-10-30 | 9143965.533333333333333333333333333333333 | 3652965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-10-31 | 9143965.533333333333333333333333333333333 | 3652965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-01 | 9143965.533333333333333333333333333333333 | 3652965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-02 | 8003965.533333333333333333333333333333333 | 2512965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-03 | 8003965.533333333333333333333333333333333 | 2512965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-04 | 8003965.533333333333333333333333333333333 | 2512965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-05 | 8003965.533333333333333333333333333333333 | 2512965.533333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-06 | 7741620.983333333333333333333333333333333 | 2250620.983333333333333333333333333333333 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-07 | 7548456.197777777777777777777777777777777 | 2057456.197777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-08 | 7548456.197777777777777777777777777777777 | 2057456.197777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-09 | 7430656.197777777777777777777777777777777 | 1939656.197777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-10 | 7430656.197777777777777777777777777777777 | 1939656.197777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-11 | 7430656.197777777777777777777777777777777 | 1939656.197777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-12 | 7241058.447777777777777777777777777777777 | 1750058.447777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-13 | 7241058.447777777777777777777777777777777 | 1750058.447777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-14 | 7241058.447777777777777777777777777777777 | 1750058.447777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-15 | 7241058.447777777777777777777777777777777 | 1750058.447777777777777777777777777777777 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-16 | 7091145.794444444444444444444444444444444 | 1600145.794444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-17 | 6897981.008888888888888888888888888888888 | 1406981.008888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-18 | 6897981.008888888888888888888888888888888 | 1406981.008888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-19 | 6897981.008888888888888888888888888888888 | 1406981.008888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-20 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-21 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-22 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-23 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-24 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-25 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-26 | 6806939.944444444444444444444444444444444 | 1315939.944444444444444444444444444444444 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-27 | 6613775.158888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-28 | 6613775.158888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-29 | 10978775.15888888888888888888888888888889 | 5487775.15888888888888888888888888888889 | 3185109.625555555555555555555555555555555 | True |
| 2019-11-30 | 10978775.15888888888888888888888888888889 | 5487775.15888888888888888888888888888889 | 3185109.625555555555555555555555555555555 | True |
| 2019-12-01 | 10978775.15888888888888888888888888888889 | 5487775.15888888888888888888888888888889 | 3185109.625555555555555555555555555555555 | True |

### request_04
Expected `8401800`; actual `12693000.00`; baseline minimum `41295163.08638461538461538461538461538461`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2024-06-04 | 50202831.4 | 37509831.4 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-05 | 50202831.4 | 37509831.4 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-06 | 50202831.4 | 37509831.4 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-07 | 50202831.4 | 37509831.4 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-08 | 47675456.92461538461538461538461538461538 | 34982456.92461538461538461538461538461538 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-09 | 46510449.51038461538461538461538461538461 | 33817449.51038461538461538461538461538461 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-10 | 44761814.44038461538461538461538461538461 | 32068814.44038461538461538461538461538461 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-11 | 42680364.44038461538461538461538461538461 | 29987364.44038461538461538461538461538461 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-12 | 41295163.08638461538461538461538461538461 | 28602163.08638461538461538461538461538461 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-13 | 79485163.08638461538461538461538461538461 | 66792163.08638461538461538461538461538461 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-14 | 79485163.08638461538461538461538461538461 | 66792163.08638461538461538461538461538461 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-15 | 77985688.61100000000000000000000000000000 | 65292688.61100000000000000000000000000000 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-16 | 77153181.19676923076923076923076923076923 | 64460181.19676923076923076923076923076923 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-17 | 77153181.19676923076923076923076923076923 | 64460181.19676923076923076923076923076923 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-18 | 77153181.19676923076923076923076923076923 | 64460181.19676923076923076923076923076923 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-19 | 77153181.19676923076923076923076923076923 | 64460181.19676923076923076923076923076923 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-20 | 77153181.19676923076923076923076923076923 | 64460181.19676923076923076923076923076923 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-21 | 77153181.19676923076923076923076923076923 | 64460181.19676923076923076923076923076923 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-22 | 75653706.72138461538461538461538461538462 | 62960706.72138461538461538461538461538462 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-23 | 74821199.30715384615384615384615384615385 | 62128199.30715384615384615384615384615385 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-24 | 73072564.23715384615384615384615384615385 | 60379564.23715384615384615384615384615385 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-25 | 73072564.23715384615384615384615384615385 | 60379564.23715384615384615384615384615385 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-26 | 73072564.23715384615384615384615384615385 | 60379564.23715384615384615384615384615385 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-27 | 73072564.23715384615384615384615384615385 | 60379564.23715384615384615384615384615385 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-28 | 73072564.23715384615384615384615384615385 | 60379564.23715384615384615384615384615385 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-29 | 71573089.76176923076923076923076923076924 | 58880089.76176923076923076923076923076924 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-30 | 70740582.34753846153846153846153846153847 | 58047582.34753846153846153846153846153847 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-01 | 70740582.34753846153846153846153846153847 | 58047582.34753846153846153846153846153847 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-02 | 58447582.34753846153846153846153846153847 | 45754582.34753846153846153846153846153847 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-03 | 58447582.34753846153846153846153846153847 | 45754582.34753846153846153846153846153847 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-04 | 56443463.74753846153846153846153846153847 | 43750463.74753846153846153846153846153847 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-05 | 56443463.74753846153846153846153846153847 | 43750463.74753846153846153846153846153847 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-06 | 54943989.27215384615384615384615384615386 | 42250989.27215384615384615384615384615386 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-07 | 54111481.85792307692307692307692307692309 | 41418481.85792307692307692307692307692309 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-08 | 51334946.78792307692307692307692307692309 | 38641946.78792307692307692307692307692309 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-09 | 51002446.78792307692307692307692307692309 | 38309446.78792307692307692307692307692309 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-10 | 51002446.78792307692307692307692307692309 | 38309446.78792307692307692307692307692309 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-11 | 50625296.78792307692307692307692307692309 | 37932296.78792307692307692307692307692309 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-12 | 87430095.43392307692307692307692307692309 | 74737095.43392307692307692307692307692309 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-13 | 85930620.95853846153846153846153846153848 | 73237620.95853846153846153846153846153848 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-14 | 85098113.54430769230769230769230769230771 | 72405113.54430769230769230769230769230771 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-15 | 85098113.54430769230769230769230769230771 | 72405113.54430769230769230769230769230771 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-16 | 85098113.54430769230769230769230769230771 | 72405113.54430769230769230769230769230771 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-17 | 85098113.54430769230769230769230769230771 | 72405113.54430769230769230769230769230771 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-18 | 85098113.54430769230769230769230769230771 | 72405113.54430769230769230769230769230771 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-19 | 85098113.54430769230769230769230769230771 | 72405113.54430769230769230769230769230771 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-20 | 83598639.06892307692307692307692307692310 | 70905639.06892307692307692307692307692310 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-21 | 82766131.65469230769230769230769230769233 | 70073131.65469230769230769230769230769233 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-22 | 81017496.58469230769230769230769230769233 | 68324496.58469230769230769230769230769233 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-23 | 81017496.58469230769230769230769230769233 | 68324496.58469230769230769230769230769233 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-24 | 81017496.58469230769230769230769230769233 | 68324496.58469230769230769230769230769233 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-25 | 81017496.58469230769230769230769230769233 | 68324496.58469230769230769230769230769233 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-26 | 81017496.58469230769230769230769230769233 | 68324496.58469230769230769230769230769233 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-27 | 79518022.10930769230769230769230769230772 | 66825022.10930769230769230769230769230772 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-28 | 78685514.69507692307692307692307692307695 | 65992514.69507692307692307692307692307695 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-29 | 78685514.69507692307692307692307692307695 | 65992514.69507692307692307692307692307695 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-30 | 78685514.69507692307692307692307692307695 | 65992514.69507692307692307692307692307695 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-31 | 78685514.69507692307692307692307692307695 | 65992514.69507692307692307692307692307695 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-01 | 78685514.69507692307692307692307692307695 | 65992514.69507692307692307692307692307695 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-02 | 66392514.69507692307692307692307692307695 | 53699514.69507692307692307692307692307695 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-03 | 62888921.61969230769230769230769230769234 | 50195921.61969230769230769230769230769234 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-04 | 62056414.20546153846153846153846153846157 | 49363414.20546153846153846153846153846157 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-05 | 60307779.13546153846153846153846153846157 | 47614779.13546153846153846153846153846157 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-06 | 60307779.13546153846153846153846153846157 | 47614779.13546153846153846153846153846157 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-07 | 59279879.13546153846153846153846153846157 | 46586879.13546153846153846153846153846157 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-08 | 58947379.13546153846153846153846153846157 | 46254379.13546153846153846153846153846157 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-09 | 58947379.13546153846153846153846153846157 | 46254379.13546153846153846153846153846157 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-10 | 95260754.66007692307692307692307692307696 | 82567754.66007692307692307692307692307696 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-11 | 93043045.89184615384615384615384615384619 | 80350045.89184615384615384615384615384619 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-12 | 93043045.89184615384615384615384615384619 | 80350045.89184615384615384615384615384619 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-13 | 93043045.89184615384615384615384615384619 | 80350045.89184615384615384615384615384619 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-14 | 93043045.89184615384615384615384615384619 | 80350045.89184615384615384615384615384619 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-15 | 93043045.89184615384615384615384615384619 | 80350045.89184615384615384615384615384619 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-16 | 93043045.89184615384615384615384615384619 | 80350045.89184615384615384615384615384619 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-17 | 91543571.41646153846153846153846153846158 | 78850571.41646153846153846153846153846158 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-18 | 90711064.00223076923076923076923076923081 | 78018064.00223076923076923076923076923081 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-19 | 88962428.93223076923076923076923076923081 | 76269428.93223076923076923076923076923081 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-20 | 88962428.93223076923076923076923076923081 | 76269428.93223076923076923076923076923081 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-21 | 88962428.93223076923076923076923076923081 | 76269428.93223076923076923076923076923081 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-22 | 88962428.93223076923076923076923076923081 | 76269428.93223076923076923076923076923081 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-23 | 88962428.93223076923076923076923076923081 | 76269428.93223076923076923076923076923081 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-24 | 87462954.45684615384615384615384615384620 | 74769954.45684615384615384615384615384620 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-25 | 86630447.04261538461538461538461538461543 | 73937447.04261538461538461538461538461543 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-26 | 86630447.04261538461538461538461538461543 | 73937447.04261538461538461538461538461543 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-27 | 86630447.04261538461538461538461538461543 | 73937447.04261538461538461538461538461543 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-28 | 86630447.04261538461538461538461538461543 | 73937447.04261538461538461538461538461543 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-29 | 86630447.04261538461538461538461538461543 | 73937447.04261538461538461538461538461543 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-30 | 86630447.04261538461538461538461538461543 | 73937447.04261538461538461538461538461543 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-31 | 85130972.56723076923076923076923076923082 | 72437972.56723076923076923076923076923082 | 41295163.08638461538461538461538461538461 | True |
| 2024-09-01 | 85130972.56723076923076923076923076923082 | 72437972.56723076923076923076923076923082 | 41295163.08638461538461538461538461538461 | True |

### request_05
Expected `737`; actual `5821.00`; baseline minimum `14901.49215384615384615384615384615384614`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2025-11-06 | 46475.1 | 30987.1 | -586.50784615384615384615384615384615386 | False |
| 2025-11-07 | 46475.1 | 30987.1 | -586.50784615384615384615384615384615386 | False |
| 2025-11-08 | 46475.1 | 30987.1 | -586.50784615384615384615384615384615386 | False |
| 2025-11-09 | 45776.092 | 30288.092 | -586.50784615384615384615384615384615386 | False |
| 2025-11-10 | 44808.092 | 29320.092 | -586.50784615384615384615384615384615386 | False |
| 2025-11-11 | 43575.23776923076923076923076923076923077 | 28087.23776923076923076923076923076923077 | -586.50784615384615384615384615384615386 | False |
| 2025-11-12 | 42320.49392307692307692307692307692307692 | 26832.49392307692307692307692307692307692 | -586.50784615384615384615384615384615386 | False |
| 2025-11-13 | 42320.49392307692307692307692307692307692 | 26832.49392307692307692307692307692307692 | -586.50784615384615384615384615384615386 | False |
| 2025-11-14 | 42320.49392307692307692307692307692307692 | 26832.49392307692307692307692307692307692 | -586.50784615384615384615384615384615386 | False |
| 2025-11-15 | 42320.49392307692307692307692307692307692 | 26832.49392307692307692307692307692307692 | -586.50784615384615384615384615384615386 | False |
| 2025-11-16 | 42320.49392307692307692307692307692307692 | 26832.49392307692307692307692307692307692 | -586.50784615384615384615384615384615386 | False |
| 2025-11-17 | 42320.49392307692307692307692307692307692 | 26832.49392307692307692307692307692307692 | -586.50784615384615384615384615384615386 | False |
| 2025-11-18 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-19 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-20 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-21 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-22 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-23 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-24 | 41598.78969230769230769230769230769230769 | 26110.78969230769230769230769230769230769 | -586.50784615384615384615384615384615386 | False |
| 2025-11-25 | 40877.08546153846153846153846153846153846 | 25389.08546153846153846153846153846153846 | -586.50784615384615384615384615384615386 | False |
| 2025-11-26 | 40462.74161538461538461538461538461538461 | 24974.74161538461538461538461538461538461 | -586.50784615384615384615384615384615386 | False |
| 2025-11-27 | 40462.74161538461538461538461538461538461 | 24974.74161538461538461538461538461538461 | -586.50784615384615384615384615384615386 | False |
| 2025-11-28 | 40462.74161538461538461538461538461538461 | 24974.74161538461538461538461538461538461 | -586.50784615384615384615384615384615386 | False |
| 2025-11-29 | 40462.74161538461538461538461538461538461 | 24974.74161538461538461538461538461538461 | -586.50784615384615384615384615384615386 | False |
| 2025-11-30 | 40462.74161538461538461538461538461538461 | 24974.74161538461538461538461538461538461 | -586.50784615384615384615384615384615386 | False |
| 2025-12-01 | 40462.74161538461538461538461538461538461 | 24974.74161538461538461538461538461538461 | -586.50784615384615384615384615384615386 | False |
| 2025-12-02 | 39741.03738461538461538461538461538461538 | 24253.03738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-03 | 34769.03738461538461538461538461538461538 | 19281.03738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-04 | 34769.03738461538461538461538461538461538 | 19281.03738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-05 | 34055.32738461538461538461538461538461538 | 18567.32738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-06 | 34055.32738461538461538461538461538461538 | 18567.32738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-07 | 34055.32738461538461538461538461538461538 | 18567.32738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-08 | 34055.32738461538461538461538461538461538 | 18567.32738461538461538461538461538461538 | -586.50784615384615384615384615384615386 | False |
| 2025-12-09 | 32634.61515384615384615384615384615384615 | 17146.61515384615384615384615384615384615 | -586.50784615384615384615384615384615386 | False |
| 2025-12-10 | 31252.27130769230769230769230769230769230 | 15764.27130769230769230769230769230769230 | -586.50784615384615384615384615384615386 | False |
| 2025-12-11 | 30741.12130769230769230769230769230769230 | 15253.12130769230769230769230769230769230 | -586.50784615384615384615384615384615386 | False |
| 2025-12-12 | 29900.72130769230769230769230769230769230 | 14412.72130769230769230769230769230769230 | -586.50784615384615384615384615384615386 | False |
| 2025-12-13 | 29900.72130769230769230769230769230769230 | 14412.72130769230769230769230769230769230 | -586.50784615384615384615384615384615386 | False |
| 2025-12-14 | 29900.72130769230769230769230769230769230 | 14412.72130769230769230769230769230769230 | -586.50784615384615384615384615384615386 | False |
| 2025-12-15 | 29900.72130769230769230769230769230769230 | 14412.72130769230769230769230769230769230 | -586.50784615384615384615384615384615386 | False |
| 2025-12-16 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-17 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-18 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-19 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-20 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-21 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-22 | 29179.01707692307692307692307692307692307 | 13691.01707692307692307692307692307692307 | -586.50784615384615384615384615384615386 | False |
| 2025-12-23 | 28457.31284615384615384615384615384615384 | 12969.31284615384615384615384615384615384 | -586.50784615384615384615384615384615386 | False |
| 2025-12-24 | 28042.96899999999999999999999999999999999 | 12554.96899999999999999999999999999999999 | -586.50784615384615384615384615384615386 | False |
| 2025-12-25 | 28042.96899999999999999999999999999999999 | 12554.96899999999999999999999999999999999 | -586.50784615384615384615384615384615386 | False |
| 2025-12-26 | 28042.96899999999999999999999999999999999 | 12554.96899999999999999999999999999999999 | -586.50784615384615384615384615384615386 | False |
| 2025-12-27 | 28042.96899999999999999999999999999999999 | 12554.96899999999999999999999999999999999 | -586.50784615384615384615384615384615386 | False |
| 2025-12-28 | 28042.96899999999999999999999999999999999 | 12554.96899999999999999999999999999999999 | -586.50784615384615384615384615384615386 | False |
| 2025-12-29 | 28042.96899999999999999999999999999999999 | 12554.96899999999999999999999999999999999 | -586.50784615384615384615384615384615386 | False |
| 2025-12-30 | 27321.26476923076923076923076923076923076 | 11833.26476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2025-12-31 | 27321.26476923076923076923076923076923076 | 11833.26476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2026-01-01 | 27321.26476923076923076923076923076923076 | 11833.26476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2026-01-02 | 27321.26476923076923076923076923076923076 | 11833.26476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2026-01-03 | 22349.26476923076923076923076923076923076 | 6861.26476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2026-01-04 | 21635.55476923076923076923076923076923076 | 6147.55476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2026-01-05 | 21635.55476923076923076923076923076923076 | 6147.55476923076923076923076923076923076 | -586.50784615384615384615384615384615386 | False |
| 2026-01-06 | 20913.85053846153846153846153846153846153 | 5425.85053846153846153846153846153846153 | -586.50784615384615384615384615384615386 | False |
| 2026-01-07 | 20499.50669230769230769230769230769230768 | 5011.50669230769230769230769230769230768 | -586.50784615384615384615384615384615386 | False |
| 2026-01-08 | 19800.49869230769230769230769230769230768 | 4312.49869230769230769230769230769230768 | -586.50784615384615384615384615384615386 | False |
| 2026-01-09 | 18832.49869230769230769230769230769230768 | 3344.49869230769230769230769230769230768 | -586.50784615384615384615384615384615386 | False |
| 2026-01-10 | 18321.34869230769230769230769230769230768 | 2833.34869230769230769230769230769230768 | -586.50784615384615384615384615384615386 | False |
| 2026-01-11 | 17480.94869230769230769230769230769230768 | 1992.94869230769230769230769230769230768 | -586.50784615384615384615384615384615386 | False |
| 2026-01-12 | 17480.94869230769230769230769230769230768 | 1992.94869230769230769230769230769230768 | -586.50784615384615384615384615384615386 | False |
| 2026-01-13 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-14 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-15 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-16 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-17 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-18 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-19 | 16759.24446153846153846153846153846153845 | 1271.24446153846153846153846153846153845 | -586.50784615384615384615384615384615386 | False |
| 2026-01-20 | 16037.54023076923076923076923076923076922 | 549.54023076923076923076923076923076922 | -586.50784615384615384615384615384615386 | False |
| 2026-01-21 | 15623.19638461538461538461538461538461537 | 135.19638461538461538461538461538461537 | -586.50784615384615384615384615384615386 | False |
| 2026-01-22 | 15623.19638461538461538461538461538461537 | 135.19638461538461538461538461538461537 | -586.50784615384615384615384615384615386 | False |
| 2026-01-23 | 15623.19638461538461538461538461538461537 | 135.19638461538461538461538461538461537 | -586.50784615384615384615384615384615386 | False |
| 2026-01-24 | 15623.19638461538461538461538461538461537 | 135.19638461538461538461538461538461537 | -586.50784615384615384615384615384615386 | False |
| 2026-01-25 | 15623.19638461538461538461538461538461537 | 135.19638461538461538461538461538461537 | -586.50784615384615384615384615384615386 | False |
| 2026-01-26 | 15623.19638461538461538461538461538461537 | 135.19638461538461538461538461538461537 | -586.50784615384615384615384615384615386 | False |
| 2026-01-27 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-01-28 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-01-29 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-01-30 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-01-31 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-02-01 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-02-02 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |
| 2026-02-03 | 14901.49215384615384615384615384615384614 | -586.50784615384615384615384615384615386 | -586.50784615384615384615384615384615386 | False |

## Earliest-full-payment date traces

Every tested horizon date and post-payment minimum is retained for representative mismatches.
### request_01
Expected `2024-03-03`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2024-03-03 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-04 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-05 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-06 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-07 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-08 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-09 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-10 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-11 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-12 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-13 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-14 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-15 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-16 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-17 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-18 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-19 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-20 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-21 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-22 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-23 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-24 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-25 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-26 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-27 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-28 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-29 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-30 | 2686.08487179487179487179487179487179488 | False |
| 2024-03-31 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-01 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-02 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-03 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-04 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-05 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-06 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-07 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-08 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-09 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-10 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-11 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-12 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-13 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-14 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-15 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-16 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-17 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-18 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-19 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-20 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-21 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-22 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-23 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-24 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-25 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-26 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-27 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-28 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-29 | 2686.08487179487179487179487179487179488 | False |
| 2024-04-30 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-01 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-02 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-03 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-04 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-05 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-06 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-07 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-08 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-09 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-10 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-11 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-12 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-13 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-14 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-15 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-16 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-17 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-18 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-19 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-20 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-21 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-22 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-23 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-24 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-25 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-26 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-27 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-28 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-29 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-30 | 2686.08487179487179487179487179487179488 | False |
| 2024-05-31 | 2686.08487179487179487179487179487179488 | False |

### request_02
Expected `2025-09-15`; actual `2025-10-13`.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2025-08-05 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-06 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-07 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-08 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-09 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-10 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-11 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-12 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-13 | 1371146.03805128205128205128205128205128 | False |
| 2025-08-14 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-15 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-16 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-17 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-18 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-19 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-20 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-21 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-22 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-23 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-24 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-25 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-26 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-27 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-28 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-29 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-30 | 11342961.73059829059829059829059829059831 | False |
| 2025-08-31 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-01 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-02 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-03 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-04 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-05 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-06 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-07 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-08 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-09 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-10 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-11 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-12 | 11342961.73059829059829059829059829059831 | False |
| 2025-09-13 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-14 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-15 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-16 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-17 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-18 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-19 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-20 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-21 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-22 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-23 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-24 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-25 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-26 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-27 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-28 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-29 | 22398596.87425641025641025641025641025645 | False |
| 2025-09-30 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-01 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-02 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-03 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-04 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-05 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-06 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-07 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-08 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-09 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-10 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-11 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-12 | 22398596.87425641025641025641025641025645 | False |
| 2025-10-13 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-14 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-15 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-16 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-17 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-18 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-19 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-20 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-21 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-22 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-23 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-24 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-25 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-26 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-27 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-28 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-29 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-30 | 47389146.03805128205128205128205128205128 | True |
| 2025-10-31 | 47389146.03805128205128205128205128205128 | True |
| 2025-11-01 | 47389146.03805128205128205128205128205128 | True |
| 2025-11-02 | 47389146.03805128205128205128205128205128 | True |

### request_03
Expected `2019-11-15`; actual `2019-11-29`.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2019-09-03 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-04 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-05 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-06 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-07 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-08 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-09 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-10 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-11 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-12 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-13 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-14 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-15 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-16 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-17 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-18 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-19 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-20 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-21 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-22 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-23 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-24 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-25 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-26 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-27 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-28 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-29 | -2305890.374444444444444444444444444444445 | False |
| 2019-09-30 | -620993.402222222222222222222222222222223 | False |
| 2019-10-01 | -620993.402222222222222222222222222222223 | False |
| 2019-10-02 | -620993.402222222222222222222222222222223 | False |
| 2019-10-03 | -620993.402222222222222222222222222222223 | False |
| 2019-10-04 | -620993.402222222222222222222222222222223 | False |
| 2019-10-05 | -620993.402222222222222222222222222222223 | False |
| 2019-10-06 | -620993.402222222222222222222222222222223 | False |
| 2019-10-07 | -620993.402222222222222222222222222222223 | False |
| 2019-10-08 | -620993.402222222222222222222222222222223 | False |
| 2019-10-09 | -620993.402222222222222222222222222222223 | False |
| 2019-10-10 | -620993.402222222222222222222222222222223 | False |
| 2019-10-11 | -620993.402222222222222222222222222222223 | False |
| 2019-10-12 | -620993.402222222222222222222222222222223 | False |
| 2019-10-13 | -620993.402222222222222222222222222222223 | False |
| 2019-10-14 | -620993.402222222222222222222222222222223 | False |
| 2019-10-15 | -620993.402222222222222222222222222222223 | False |
| 2019-10-16 | -620993.402222222222222222222222222222223 | False |
| 2019-10-17 | -620993.402222222222222222222222222222223 | False |
| 2019-10-18 | -620993.402222222222222222222222222222223 | False |
| 2019-10-19 | -620993.402222222222222222222222222222223 | False |
| 2019-10-20 | -620993.402222222222222222222222222222223 | False |
| 2019-10-21 | -620993.402222222222222222222222222222223 | False |
| 2019-10-22 | -620993.402222222222222222222222222222223 | False |
| 2019-10-23 | -620993.402222222222222222222222222222223 | False |
| 2019-10-24 | -620993.402222222222222222222222222222223 | False |
| 2019-10-25 | -620993.402222222222222222222222222222223 | False |
| 2019-10-26 | -620993.402222222222222222222222222222223 | False |
| 2019-10-27 | -620993.402222222222222222222222222222223 | False |
| 2019-10-28 | -620993.402222222222222222222222222222223 | False |
| 2019-10-29 | -620993.402222222222222222222222222222223 | False |
| 2019-10-30 | 1122775.158888888888888888888888888888888 | False |
| 2019-10-31 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-01 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-02 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-03 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-04 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-05 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-06 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-07 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-08 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-09 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-10 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-11 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-12 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-13 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-14 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-15 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-16 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-17 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-18 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-19 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-20 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-21 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-22 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-23 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-24 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-25 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-26 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-27 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-28 | 1122775.158888888888888888888888888888888 | False |
| 2019-11-29 | 3185109.625555555555555555555555555555555 | True |
| 2019-11-30 | 3185109.625555555555555555555555555555555 | True |
| 2019-12-01 | 3185109.625555555555555555555555555555555 | True |

### request_04
Expected `2024-06-15`; actual `2024-06-13`.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2024-06-04 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-05 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-06 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-07 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-08 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-09 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-10 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-11 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-12 | 28602163.08638461538461538461538461538461 | False |
| 2024-06-13 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-14 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-15 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-16 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-17 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-18 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-19 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-20 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-21 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-22 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-23 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-24 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-25 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-26 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-27 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-28 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-29 | 37932296.78792307692307692307692307692309 | True |
| 2024-06-30 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-01 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-02 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-03 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-04 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-05 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-06 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-07 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-08 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-09 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-10 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-11 | 37932296.78792307692307692307692307692309 | True |
| 2024-07-12 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-13 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-14 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-15 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-16 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-17 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-18 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-19 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-20 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-21 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-22 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-23 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-24 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-25 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-26 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-27 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-28 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-29 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-30 | 41295163.08638461538461538461538461538461 | True |
| 2024-07-31 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-01 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-02 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-03 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-04 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-05 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-06 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-07 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-08 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-09 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-10 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-11 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-12 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-13 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-14 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-15 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-16 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-17 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-18 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-19 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-20 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-21 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-22 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-23 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-24 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-25 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-26 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-27 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-28 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-29 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-30 | 41295163.08638461538461538461538461538461 | True |
| 2024-08-31 | 41295163.08638461538461538461538461538461 | True |
| 2024-09-01 | 41295163.08638461538461538461538461538461 | True |

### request_06
Expected `2026-01-15`; actual `2026-01-03`.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2026-01-03 | 961.378066666666666666666666666666666667 | True |
| 2026-01-04 | 961.378066666666666666666666666666666667 | True |
| 2026-01-05 | 961.378066666666666666666666666666666667 | True |
| 2026-01-06 | 961.378066666666666666666666666666666667 | True |
| 2026-01-07 | 961.378066666666666666666666666666666667 | True |
| 2026-01-08 | 961.378066666666666666666666666666666667 | True |
| 2026-01-09 | 961.378066666666666666666666666666666667 | True |
| 2026-01-10 | 961.378066666666666666666666666666666667 | True |
| 2026-01-11 | 961.378066666666666666666666666666666667 | True |
| 2026-01-12 | 961.378066666666666666666666666666666667 | True |
| 2026-01-13 | 961.378066666666666666666666666666666667 | True |
| 2026-01-14 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-15 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-16 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-17 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-18 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-19 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-20 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-21 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-22 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-23 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-24 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-25 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-26 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-27 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-28 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-29 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-30 | 1086.319866666666666666666666666666666668 | True |
| 2026-01-31 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-01 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-02 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-03 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-04 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-05 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-06 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-07 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-08 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-09 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-10 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-11 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-12 | 1086.319866666666666666666666666666666668 | True |
| 2026-02-13 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-14 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-15 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-16 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-17 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-18 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-19 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-20 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-21 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-22 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-23 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-24 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-25 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-26 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-27 | 1211.261666666666666666666666666666666669 | True |
| 2026-02-28 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-01 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-02 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-03 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-04 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-05 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-06 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-07 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-08 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-09 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-10 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-11 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-12 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-13 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-14 | 1211.261666666666666666666666666666666669 | True |
| 2026-03-15 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-16 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-17 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-18 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-19 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-20 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-21 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-22 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-23 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-24 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-25 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-26 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-27 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-28 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-29 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-30 | 1581.778066666666666666666666666666666667 | True |
| 2026-03-31 | 1581.778066666666666666666666666666666667 | True |
| 2026-04-01 | 1581.778066666666666666666666666666666667 | True |
| 2026-04-02 | 1581.778066666666666666666666666666666667 | True |

## Root-cause interpretation

Categories are primary hypotheses from deterministic traces, not expected-answer special cases. No production code or supplied dataset was changed by this report generation.