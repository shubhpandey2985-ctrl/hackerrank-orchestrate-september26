# Sample mismatch forensic report

Generated from repository data and current deterministic implementation. No expected answer is hardcoded.

## Harness verification

Expected rows: 25; actual rows: 25; joined by `request_id`. Expected header: `['request_id', 'user_id', 'request_date', 'request_type', 'requested_amount', 'desired_completion_date', 'allows_partial_payment', 'request_text', 'amount_safe_to_pay', 'affordability_status', 'recommended_payment_method', 'payment_plan', 'earliest_date_for_full_payment', 'spending_changes_needed', 'decision_explanation']`. Actual header: `['request_id', 'amount_safe_to_pay', 'affordability_status', 'recommended_payment_method', 'payment_plan', 'earliest_date_for_full_payment', 'spending_changes_needed', 'decision_explanation']`. Compared fields: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, spending_changes_needed, decision_explanation. Numeric-equivalent trailing-zero differences are classified as `20. output serialization`.

## Root-cause priority

- 20. output serialization: 25 mismatching fields
- 12. earliest-safe-date calculation: 17 mismatching fields
- 18. candidate ranking: 15 mismatching fields
- 19. deadline/status mapping: 15 mismatching fields
- 11. safe-amount calculation: 14 mismatching fields
- 16. payment-method preference: 14 mismatching fields
- 2. event classification: 5 mismatching fields
- 7. scheduled-credit semantics: 4 mismatching fields
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

- decision_explanation: 25
- amount_safe_to_pay: 23
- affordability_status: 15
- recommended_payment_method: 14
- payment_plan: 15
- earliest_date_for_full_payment: 17
- spending_changes_needed: 3

## Per-field mismatches

### request_01 — `decision_explanation`
- Expected: `Pay ZAR 25,256 today. This leaves at least ZAR 18,000 available over the next 90 days.`
- Actual: `Plan full_payment completes 25256 while maintaining the minimum balance; safe today: 25256.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_01`; balance `58481.1`; minimum `18000`; preferences `['full_payment']`
- Request: amount `25256` on `2024-03-03`, deadline `2024-03-20`
- Actual selected plan: `2024-03-03:25256` via `full_payment`
- Credits `3` (scheduled `1`); debits `28`; pending `1`; recurring `16`; flexible `18`; options `4`
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '75818.03', '2024-03-20': '75818.03', '2024-05-31': '54691.09'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '25256', '2024-03-03', 1, '']), ('option_payment_option_01', True, [0, 0, '25256', '2024-03-03', 1, 'payment_option_01']), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None), ('wait', True, [0, 0, '25256', '2024-03-03', 1, ''])]`
- Validator: `True`
 
### request_02 — `amount_safe_to_pay`
- Expected: `17229139.2`
- Actual: `14334739.38`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '55458539.26', '2025-10-10': '41102939.38', '2025-11-02': '40733389.38'}`
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
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '55458539.26', '2025-10-10': '41102939.38', '2025-11-02': '40733389.38'}`
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
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '55458539.26', '2025-10-10': '41102939.38', '2025-11-02': '40733389.38'}`
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
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '55458539.26', '2025-10-10': '41102939.38', '2025-11-02': '40733389.38'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `earliest_date_for_full_payment`
- Expected: `2025-09-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '55458539.26', '2025-10-10': '41102939.38', '2025-11-02': '40733389.38'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `decision_explanation`
- Expected: `Use 3 installments of IDR 15,952,906.67, starting 8 August 2025. This leaves at least IDR 29,158,400 available.`
- Actual: `Safe amount today is 14334739.38; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '55458539.26', '2025-10-10': '41102939.38', '2025-11-02': '40733389.38'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_03 — `amount_safe_to_pay`
- Expected: `873000`
- Actual: `0`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `8`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '1092166.35', '2019-12-01': '1092166.35'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None)]`
- Validator: `True`
 
### request_03 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `8`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '1092166.35', '2019-12-01': '1092166.35'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None)]`
- Validator: `True`
 
### request_03 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `8`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '1092166.35', '2019-12-01': '1092166.35'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None)]`
- Validator: `True`
 
### request_03 — `payment_plan`
- Expected: `2019-11-15:5491000`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `8`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '1092166.35', '2019-12-01': '1092166.35'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None)]`
- Validator: `True`
 
### request_03 — `earliest_date_for_full_payment`
- Expected: `2019-11-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `8`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '1092166.35', '2019-12-01': '1092166.35'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None)]`
- Validator: `True`
 
### request_03 — `decision_explanation`
- Expected: `Pay IDR 5,491,000 in full on 15 November 2019. Paying earlier would take the balance below the IDR 2,668,700 minimum.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_03`; balance `5810300`; minimum `2668700`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `5491000` on `2019-09-03`, deadline `2019-11-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `15`; pending `1`; recurring `8`; flexible `15`; options `3`
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4312955.45', '2019-11-15': '1092166.35', '2019-12-01': '1092166.35'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_08', False, None), ('option_payment_option_09', False, None), ('option_payment_option_10', False, None)]`
- Validator: `True`
 
### request_04 — `amount_safe_to_pay`
- Expected: `8401800`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `15`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '46760981.4', '2024-06-19': '46760981.4', '2024-09-01': '14691644.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None)]`
- Validator: `True`
 
### request_04 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `15`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '46760981.4', '2024-06-19': '46760981.4', '2024-09-01': '14691644.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None)]`
- Validator: `True`
 
### request_04 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `15`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '46760981.4', '2024-06-19': '46760981.4', '2024-09-01': '14691644.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None)]`
- Validator: `True`
 
### request_04 — `payment_plan`
- Expected: `2024-06-15:12693000`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `15`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '46760981.4', '2024-06-19': '46760981.4', '2024-09-01': '14691644.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None)]`
- Validator: `True`
 
### request_04 — `earliest_date_for_full_payment`
- Expected: `2024-06-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `15`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '46760981.4', '2024-06-19': '46760981.4', '2024-09-01': '14691644.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None)]`
- Validator: `True`
 
### request_04 — `decision_explanation`
- Expected: `Wait until 15 June 2024, then pay IDR 12,693,000 in full. Paying sooner would put the IDR 30,686,600 minimum at risk.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_04`; balance `52206950`; minimum `30686600`; preferences `['full_payment']`
- Request: amount `12693000` on `2024-06-04`, deadline `2024-06-19`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `15`; flexible `10`; options `2`
- Critical balances: `{'2024-06-04': '50202831.4', '2024-06-11': '46760981.4', '2024-06-19': '46760981.4', '2024-09-01': '14691644.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_11', False, None), ('option_payment_option_12', False, None)]`
- Validator: `True`
 
### request_05 — `amount_safe_to_pay`
- Expected: `737`
- Actual: `15488`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `2025-11-06:15488` via `full_payment`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '31859.78', '2026-02-03': '31859.78'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_05 — `affordability_status`
- Expected: `not_affordable`
- Actual: `affordable_now`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `2025-11-06:15488` via `full_payment`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '31859.78', '2026-02-03': '31859.78'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_05 — `recommended_payment_method`
- Expected: `not_recommended`
- Actual: `full_payment`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `2025-11-06:15488` via `full_payment`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '31859.78', '2026-02-03': '31859.78'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_05 — `payment_plan`
- Expected: `none`
- Actual: `2025-11-06:15488`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `2025-11-06:15488` via `full_payment`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '31859.78', '2026-02-03': '31859.78'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_05 — `earliest_date_for_full_payment`
- Expected: ``
- Actual: `2025-11-06`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `2025-11-06:15488` via `full_payment`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '31859.78', '2026-02-03': '31859.78'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_05 — `decision_explanation`
- Expected: `Do not make this payment by 12 January 2026. None of the available options keeps the ZAR 13,100 minimum protected.`
- Actual: `Plan full_payment completes 15488 while maintaining the minimum balance; safe today: 15488.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_05`; balance `46475.1`; minimum `13100`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `15488` on `2025-11-06`, deadline `2026-01-12`
- Actual selected plan: `2025-11-06:15488` via `full_payment`
- Credits `1` (scheduled `0`); debits `19`; pending `0`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '31859.78', '2026-02-03': '31859.78'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_06 — `amount_safe_to_pay`
- Expected: `603.3`
- Actual: `385.62`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `recommended_payment_method`
- Expected: `full_payment`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `payment_plan`
- Expected: `2026-01-03:620.40`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `earliest_date_for_full_payment`
- Expected: `2026-01-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `spending_changes_needed`
- Expected: `stop:event_476`
- Actual: `none`
- Primary root cause: **17. flexible-spending logic**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `decision_explanation`
- Expected: `Stop the family streaming plan, then pay EUR 620.40 today. This leaves at least EUR 800 available.`
- Actual: `Safe amount today is 385.62; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1840.54', '2026-04-02': '1128.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_07 — `amount_safe_to_pay`
- Expected: `87170.56`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '83975.85', '2024-12-03': '83975.85'}`
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
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '83975.85', '2024-12-03': '83975.85'}`
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
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '83975.85', '2024-12-03': '83975.85'}`
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
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '83975.85', '2024-12-03': '83975.85'}`
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
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '83975.85', '2024-12-03': '83975.85'}`
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
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '83975.85', '2024-12-03': '83975.85'}`
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
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `17`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-204.53', '2025-05-07': '-672.03'}`
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
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `17`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-204.53', '2025-05-07': '-672.03'}`
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
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `17`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-204.53', '2025-05-07': '-672.03'}`
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
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `17`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-204.53', '2025-05-07': '-672.03'}`
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
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `17`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-204.53', '2025-05-07': '-672.03'}`
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
- Credits `1` (scheduled `0`); debits `25`; pending `0`; recurring `17`; flexible `23`; options `2`
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-204.53', '2025-05-07': '-672.03'}`
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
- Credits `3` (scheduled `0`); debits `14`; pending `0`; recurring `7`; flexible `0`; options `3`
- Critical balances: `{'2026-07-04': '2231.1', '2026-07-23': '2145.22', '2026-10-01': '1339.86'}`
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
- Credits `3` (scheduled `0`); debits `14`; pending `0`; recurring `7`; flexible `0`; options `3`
- Critical balances: `{'2026-07-04': '2231.1', '2026-07-23': '2145.22', '2026-10-01': '1339.86'}`
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
- Credits `6` (scheduled `0`); debits `23`; pending `0`; recurring `15`; flexible `33`; options `2`
- Critical balances: `{'2024-12-06': '750155', '2025-02-10': '539531.61', '2025-03-05': '529976.61'}`
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
- Credits `6` (scheduled `0`); debits `23`; pending `0`; recurring `15`; flexible `33`; options `2`
- Critical balances: `{'2024-12-06': '750155', '2025-02-10': '539531.61', '2025-03-05': '529976.61'}`
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
- Credits `6` (scheduled `0`); debits `23`; pending `0`; recurring `15`; flexible `33`; options `2`
- Critical balances: `{'2024-12-06': '750155', '2025-02-10': '539531.61', '2025-03-05': '529976.61'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_27', False, None), ('option_payment_option_28', False, None)]`
- Validator: `True`
 
### request_11 — `amount_safe_to_pay`
- Expected: `12510645`
- Actual: `6496199.46`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_11 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_11 — `recommended_payment_method`
- Expected: `full_payment`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_11 — `payment_plan`
- Expected: `2025-05-03:13110000`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_11 — `earliest_date_for_full_payment`
- Expected: `2025-07-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_11 — `spending_changes_needed`
- Expected: `reduce_to:event_989:665950`
- Actual: `none`
- Primary root cause: **17. flexible-spending logic**
- Diagnosis: `implementation bug`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_11 — `decision_explanation`
- Expected: `Reduce the weekend food delivery to IDR 665,950, then pay IDR 13,110,000 today. This leaves at least IDR 34,140,600 available.`
- Actual: `Safe amount today is 6496199.46; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_11`; balance `63531795`; minimum `34140600`; preferences `['full_payment']`
- Request: amount `13110000` on `2025-05-03`, deadline `2025-06-12`
- Actual selected plan: `none` via `not_recommended`
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '48100314.64', '2025-07-31': '40132349.46'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_29', False, None), ('option_payment_option_30', False, None), ('option_payment_option_31', False, None), ('option_payment_option_32', False, None)]`
- Validator: `True`
 
### request_12 — `decision_explanation`
- Expected: `Use 3 installments of ZAR 22,590.19, starting 19 April 2026. This leaves at least ZAR 43,200 available.`
- Actual: `Plan installments completes 65164 while maintaining the minimum balance; safe today: 65164.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_12`; balance `193089.89`; minimum `43200`; preferences `['partial_payment', 'installments']`
- Request: amount `65164` on `2026-04-05`, deadline `2026-06-20`
- Actual selected plan: `2026-04-19:22590.19|2026-05-20:22590.19|2026-06-20:22590.19` via `installments`
- Credits `0` (scheduled `0`); debits `14`; pending `0`; recurring `6`; flexible `19`; options `3`
- Critical balances: `{'2026-04-05': '193089.89', '2026-04-19': '191137.39', '2026-05-20': '173786.69', '2026-06-20': '156435.99', '2026-07-03': '156435.99'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_33', True, [0, 0, '67770.57', '2026-04-19', 3, 'payment_option_33']), ('option_payment_option_34', False, None), ('option_payment_option_35', False, None)]`
- Validator: `True`
 
### request_13 — `amount_safe_to_pay`
- Expected: `433.4`
- Actual: `696.76`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2307.36', '2024-06-04': '1663.76'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_13 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2307.36', '2024-06-04': '1663.76'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_13 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2307.36', '2024-06-04': '1663.76'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_13 — `payment_plan`
- Expected: `2024-05-15:941.60`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2307.36', '2024-06-04': '1663.76'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_13 — `earliest_date_for_full_payment`
- Expected: `2024-05-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2307.36', '2024-06-04': '1663.76'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_13 — `decision_explanation`
- Expected: `Pay EUR 941.60 in full on 15 May 2024. Paying earlier would take the balance below the EUR 1,300 minimum.`
- Actual: `Safe amount today is 696.76; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2307.36', '2024-06-04': '1663.76'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_14 — `amount_safe_to_pay`
- Expected: `597.74`
- Actual: `1228.05`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_14`; balance `3931.74`; minimum `2200`; preferences `['partial_payment']`
- Request: amount `5414.2` on `2025-08-04`, deadline `2025-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2025-08-04': '3931.74', '2025-10-04': '4236.16', '2025-11-01': '3718.47'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_39', False, None), ('option_payment_option_40', False, None)]`
- Validator: `True`
 
### request_14 — `decision_explanation`
- Expected: `Do not proceed with the EUR 5,414.20 request. Although EUR 597.74 is available today, the full amount cannot be completed safely within 90 days.`
- Actual: `Safe amount today is 1228.05; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_14`; balance `3931.74`; minimum `2200`; preferences `['partial_payment']`
- Request: amount `5414.2` on `2025-08-04`, deadline `2025-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2025-08-04': '3931.74', '2025-10-04': '4236.16', '2025-11-01': '3718.47'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_39', False, None), ('option_payment_option_40', False, None)]`
- Validator: `True`
 
### request_15 — `amount_safe_to_pay`
- Expected: `83.05`
- Actual: `363.64`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_15`; balance `1770.05`; minimum `1200`; preferences `['partial_payment']`
- Request: amount `3685` on `2026-01-06`, deadline `2026-02-01`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `0`; recurring `15`; flexible `13`; options `3`
- Critical balances: `{'2026-01-06': '1770.05', '2026-02-01': '3224.64', '2026-04-05': '1940.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_41', False, None), ('option_payment_option_42', False, None), ('option_payment_option_43', False, None)]`
- Validator: `True`
 
### request_15 — `decision_explanation`
- Expected: `Do not make this payment by 1 February 2026. None of the available options keeps the EUR 1,200 minimum protected.`
- Actual: `Safe amount today is 363.64; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_15`; balance `1770.05`; minimum `1200`; preferences `['partial_payment']`
- Request: amount `3685` on `2026-01-06`, deadline `2026-02-01`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `0`; recurring `15`; flexible `13`; options `3`
- Critical balances: `{'2026-01-06': '1770.05', '2026-02-01': '3224.64', '2026-04-05': '1940.62'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_41', False, None), ('option_payment_option_42', False, None), ('option_payment_option_43', False, None)]`
- Validator: `True`
 
### request_16 — `amount_safe_to_pay`
- Expected: `122500`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `18`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '81569.26', '2023-11-09': '11901.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_44', False, None), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None)]`
- Validator: `True`
 
### request_16 — `affordability_status`
- Expected: `affordable_now`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `18`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '81569.26', '2023-11-09': '11901.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_44', False, None), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None)]`
- Validator: `True`
 
### request_16 — `recommended_payment_method`
- Expected: `full_payment`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `18`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '81569.26', '2023-11-09': '11901.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_44', False, None), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None)]`
- Validator: `True`
 
### request_16 — `payment_plan`
- Expected: `2023-08-12:122500`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `18`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '81569.26', '2023-11-09': '11901.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_44', False, None), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None)]`
- Validator: `True`
 
### request_16 — `earliest_date_for_full_payment`
- Expected: `2023-08-12`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `18`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '81569.26', '2023-11-09': '11901.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_44', False, None), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None)]`
- Validator: `True`
 
### request_16 — `decision_explanation`
- Expected: `Pay INR 122,500 today. This leaves at least INR 122,400 available over the next 90 days.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_16`; balance `362370`; minimum `122400`; preferences `['full_payment', 'installments']`
- Request: amount `122500` on `2023-08-12`, deadline `2023-10-11`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `30`; pending `0`; recurring `18`; flexible `0`; options `3`
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '81569.26', '2023-11-09': '11901.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_44', False, None), ('option_payment_option_45', False, None), ('option_payment_option_46', False, None)]`
- Validator: `True`
 
### request_17 — `amount_safe_to_pay`
- Expected: `243849.58`
- Actual: `274600`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_17`; balance `550379.58`; minimum `166100`; preferences `['installments']`
- Request: amount `274600` on `2026-03-01`, deadline `2026-05-04`
- Actual selected plan: `2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67` via `installments`
- Credits `4` (scheduled `1`); debits `25`; pending `0`; recurring `15`; flexible `23`; options `3`
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '666037.43', '2026-03-31': '664362.43', '2026-04-30': '572345.28', '2026-05-04': '572345.28', '2026-05-29': '480328.13'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_17 — `earliest_date_for_full_payment`
- Expected: `2026-03-15`
- Actual: `2026-03-01`
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_17`; balance `550379.58`; minimum `166100`; preferences `['installments']`
- Request: amount `274600` on `2026-03-01`, deadline `2026-05-04`
- Actual selected plan: `2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67` via `installments`
- Credits `4` (scheduled `1`); debits `25`; pending `0`; recurring `15`; flexible `23`; options `3`
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '666037.43', '2026-03-31': '664362.43', '2026-04-30': '572345.28', '2026-05-04': '572345.28', '2026-05-29': '480328.13'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_17 — `decision_explanation`
- Expected: `Use 3 installments of INR 95,194.67, starting 1 March 2026. This leaves at least INR 166,100 available.`
- Actual: `Plan installments completes 274600 while maintaining the minimum balance; safe today: 274600.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_17`; balance `550379.58`; minimum `166100`; preferences `['installments']`
- Request: amount `274600` on `2026-03-01`, deadline `2026-05-04`
- Actual selected plan: `2026-03-01:95194.67|2026-03-31:95194.67|2026-04-30:95194.67` via `installments`
- Credits `4` (scheduled `1`); debits `25`; pending `0`; recurring `15`; flexible `23`; options `3`
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '666037.43', '2026-03-31': '664362.43', '2026-04-30': '572345.28', '2026-05-04': '572345.28', '2026-05-29': '480328.13'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_18 — `amount_safe_to_pay`
- Expected: `462`
- Actual: `58.71`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-15': '1421.71', '2026-10-04': '1254.71'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_18 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-15': '1421.71', '2026-10-04': '1254.71'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_18 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-15': '1421.71', '2026-10-04': '1254.71'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_18 — `payment_plan`
- Expected: `2026-09-15:3246.10`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-15': '1421.71', '2026-10-04': '1254.71'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_18 — `earliest_date_for_full_payment`
- Expected: `2026-09-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-15': '1421.71', '2026-10-04': '1254.71'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_18 — `decision_explanation`
- Expected: `Pay EUR 3,246.10 in full on 15 September 2026. Paying earlier would take the balance below the EUR 1,400 minimum.`
- Actual: `Safe amount today is 58.71; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2378.57', '2026-09-15': '1421.71', '2026-10-04': '1254.71'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_19 — `amount_safe_to_pay`
- Expected: `28820`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '145070.81', '2024-12-02': '72222.43'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '145070.81', '2024-12-02': '72222.43'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `recommended_payment_method`
- Expected: `partial_payment`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '145070.81', '2024-12-02': '72222.43'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `payment_plan`
- Expected: `2024-09-04:28820|2024-09-15:10840`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '145070.81', '2024-12-02': '72222.43'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `earliest_date_for_full_payment`
- Expected: `2024-09-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '145070.81', '2024-12-02': '72222.43'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_19 — `decision_explanation`
- Expected: `Pay INR 28,820 today and the remaining INR 10,840 on 15 September 2024. This completes the full request and keeps the INR 92,800 minimum protected.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_19`; balance `199545`; minimum `92800`; preferences `['partial_payment', 'installments']`
- Request: amount `39660` on `2024-09-04`, deadline `2024-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `17`; pending `0`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '145070.81', '2024-12-02': '72222.43'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_20 — `amount_safe_to_pay`
- Expected: `5400`
- Actual: `0`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_20`; balance `102609.05`; minimum `64500`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `303700` on `2026-02-07`, deadline `2026-02-22`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `3`; recurring `12`; flexible `19`; options `2`
- Critical balances: `{'2026-02-07': '102609.05', '2026-02-08': '98139.05', '2026-02-09': '97435.00', '2026-02-14': '97070.00', '2026-02-22': '97070.00', '2026-05-07': '50370.26'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_55', False, None), ('option_payment_option_56', False, None)]`
- Validator: `True`
 
### request_20 — `decision_explanation`
- Expected: `Do not make this payment by 22 February 2026. None of the available options keeps the INR 64,500 minimum protected.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_20`; balance `102609.05`; minimum `64500`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `303700` on `2026-02-07`, deadline `2026-02-22`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `3`; recurring `12`; flexible `19`; options `2`
- Critical balances: `{'2026-02-07': '102609.05', '2026-02-08': '98139.05', '2026-02-09': '97435.00', '2026-02-14': '97070.00', '2026-02-22': '97070.00', '2026-05-07': '50370.26'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3676.27', '2026-04-15': '5932.27', '2026-07-01': '4130.51'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3676.27', '2026-04-15': '5932.27', '2026-07-01': '4130.51'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3676.27', '2026-04-15': '5932.27', '2026-07-01': '4130.51'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3676.27', '2026-04-15': '5932.27', '2026-07-01': '4130.51'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3676.27', '2026-04-15': '5932.27', '2026-07-01': '4130.51'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3734.27', '2026-04-14': '3676.27', '2026-04-15': '5932.27', '2026-07-01': '4130.51'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_22 — `amount_safe_to_pay`
- Expected: `475.46`
- Actual: `179.04`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1062.12', '2025-02-10': '595.04', '2025-03-04': '567.04'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `affordability_status`
- Expected: `affordable_with_plan`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1062.12', '2025-02-10': '595.04', '2025-03-04': '567.04'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `recommended_payment_method`
- Expected: `installments`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1062.12', '2025-02-10': '595.04', '2025-03-04': '567.04'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `payment_plan`
- Expected: `2024-12-08:253.59|2025-01-05:253.59|2025-02-02:253.59`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1062.12', '2025-02-10': '595.04', '2025-03-04': '567.04'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `earliest_date_for_full_payment`
- Expected: `2025-01-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1062.12', '2025-02-10': '595.04', '2025-03-04': '567.04'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `decision_explanation`
- Expected: `Use 3 installments of EUR 253.59, starting 8 December 2024. This leaves at least EUR 500 available.`
- Actual: `Safe amount today is 179.04; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1062.12', '2025-02-10': '595.04', '2025-03-04': '567.04'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_23 — `amount_safe_to_pay`
- Expected: `9152`
- Actual: `0`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `13`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '47724.55', '2025-07-15': '-6407.55', '2025-08-04': '-6703.45'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None)]`
- Validator: `True`
 
### request_23 — `affordability_status`
- Expected: `affordable_later`
- Actual: `not_affordable`
- Primary root cause: **19. deadline/status mapping**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `13`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '47724.55', '2025-07-15': '-6407.55', '2025-08-04': '-6703.45'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None)]`
- Validator: `True`
 
### request_23 — `recommended_payment_method`
- Expected: `wait`
- Actual: `not_recommended`
- Primary root cause: **16. payment-method preference**
- Diagnosis: `incorrect interpretation of the specification`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `13`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '47724.55', '2025-07-15': '-6407.55', '2025-08-04': '-6703.45'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None)]`
- Validator: `True`
 
### request_23 — `payment_plan`
- Expected: `2025-07-15:38016`
- Actual: `none`
- Primary root cause: **18. candidate ranking**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `13`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '47724.55', '2025-07-15': '-6407.55', '2025-08-04': '-6703.45'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None)]`
- Validator: `True`
 
### request_23 — `earliest_date_for_full_payment`
- Expected: `2025-07-15`
- Actual: ``
- Primary root cause: **12. earliest-safe-date calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `13`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '47724.55', '2025-07-15': '-6407.55', '2025-08-04': '-6703.45'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None)]`
- Validator: `True`
 
### request_23 — `decision_explanation`
- Expected: `Pay ZAR 38,016 in full on 15 July 2025. Paying earlier would take the balance below the ZAR 27,000 minimum.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_23`; balance `51957.9`; minimum `27000`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `38016` on `2025-05-07`, deadline `2025-07-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `13`; flexible `10`; options `3`
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '47724.55', '2025-07-15': '-6407.55', '2025-08-04': '-6703.45'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_64', False, None), ('option_payment_option_65', False, None), ('option_payment_option_66', False, None)]`
- Validator: `True`
 
### request_24 — `amount_safe_to_pay`
- Expected: `13420`
- Actual: `0`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_24`; balance `85045`; minimum `51000`; preferences `['partial_payment']`
- Request: amount `109600` on `2026-01-04`, deadline `2026-02-08`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `0`); debits `29`; pending `0`; recurring `19`; flexible `36`; options `2`
- Critical balances: `{'2026-01-04': '81554.5', '2026-01-11': '75659.5', '2026-02-08': '49859.0', '2026-04-03': '23348.5'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_67', False, None), ('option_payment_option_68', False, None)]`
- Validator: `True`
 
### request_24 — `decision_explanation`
- Expected: `Do not proceed with the INR 109,600 request. Although INR 13,420 is available today, the full amount cannot be completed safely within 90 days.`
- Actual: `Safe amount today is 0; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_24`; balance `85045`; minimum `51000`; preferences `['partial_payment']`
- Request: amount `109600` on `2026-01-04`, deadline `2026-02-08`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `0`); debits `29`; pending `0`; recurring `19`; flexible `36`; options `2`
- Critical balances: `{'2026-01-04': '81554.5', '2026-01-11': '75659.5', '2026-02-08': '49859.0', '2026-04-03': '23348.5'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_67', False, None), ('option_payment_option_68', False, None)]`
- Validator: `True`
 
### request_25 — `amount_safe_to_pay`
- Expected: `1425000`
- Actual: `5877496.33`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_25`; balance `32063050`; minimum `23379100`; preferences `['full_payment', 'installments']`
- Request: amount `60496000` on `2024-03-06`, deadline `2024-04-17`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `28`; pending `0`; recurring `19`; flexible `0`; options `3`
- Critical balances: `{'2024-03-06': '32063050', '2024-03-15': '57756590.33', '2024-04-17': '47996136.66', '2024-06-03': '38235682.99'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_69', False, None), ('option_payment_option_70', False, None), ('option_payment_option_71', False, None)]`
- Validator: `True`
 
### request_25 — `decision_explanation`
- Expected: `Do not make this payment by 17 April 2024. None of the available options keeps the IDR 23,379,100 minimum protected.`
- Actual: `Safe amount today is 5877496.33; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_25`; balance `32063050`; minimum `23379100`; preferences `['full_payment', 'installments']`
- Request: amount `60496000` on `2024-03-06`, deadline `2024-04-17`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `28`; pending `0`; recurring `19`; flexible `0`; options `3`
- Critical balances: `{'2024-03-06': '32063050', '2024-03-15': '57756590.33', '2024-04-17': '47996136.66', '2024-06-03': '38235682.99'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_69', False, None), ('option_payment_option_70', False, None), ('option_payment_option_71', False, None)]`
- Validator: `True`
 
## Mathematical safe-amount traces

Representative traces show deterministic date-by-date balances; expected amounts are comparison-only.
### request_02
Expected `17229139.2`; actual `14334739.38`; baseline minimum `40733389.38`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2025-08-05 | 60383889.2 | 14365889.2 | -5284610.62 | False |
| 2025-08-06 | 58242039.26 | 12224039.26 | -5284610.62 | False |
| 2025-08-07 | 57109639.26 | 11091639.26 | -5284610.62 | False |
| 2025-08-08 | 55458539.26 | 9440539.26 | -5284610.62 | False |
| 2025-08-09 | 55458539.26 | 9440539.26 | -5284610.62 | False |
| 2025-08-10 | 55458539.26 | 9440539.26 | -5284610.62 | False |
| 2025-08-11 | 55458539.26 | 9440539.26 | -5284610.62 | False |
| 2025-08-12 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-13 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-14 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-15 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-16 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-17 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-18 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-19 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-20 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-21 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-22 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-23 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-24 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-25 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-26 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-27 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-28 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-29 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-30 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-08-31 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-09-01 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-09-02 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-09-03 | 55088989.26 | 9070989.26 | -5284610.62 | False |
| 2025-09-04 | 51554989.26 | 5536989.26 | -5284610.62 | False |
| 2025-09-05 | 49413139.32 | 3395139.32 | -5284610.62 | False |
| 2025-09-06 | 48280739.32 | 2262739.32 | -5284610.62 | False |
| 2025-09-07 | 48280739.32 | 2262739.32 | -5284610.62 | False |
| 2025-09-08 | 48280739.32 | 2262739.32 | -5284610.62 | False |
| 2025-09-09 | 48280739.32 | 2262739.32 | -5284610.62 | False |
| 2025-09-10 | 48280739.32 | 2262739.32 | -5284610.62 | False |
| 2025-09-11 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-12 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-13 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-14 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-15 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-16 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-17 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-18 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-19 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-20 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-21 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-22 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-23 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-24 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-25 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-26 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-27 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-28 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-29 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-09-30 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-10-01 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-10-02 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-10-03 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-10-04 | 47911189.32 | 1893189.32 | -5284610.62 | False |
| 2025-10-05 | 42235339.38 | -3782660.62 | -5284610.62 | False |
| 2025-10-06 | 41102939.38 | -4915060.62 | -5284610.62 | False |
| 2025-10-07 | 41102939.38 | -4915060.62 | -5284610.62 | False |
| 2025-10-08 | 41102939.38 | -4915060.62 | -5284610.62 | False |
| 2025-10-09 | 41102939.38 | -4915060.62 | -5284610.62 | False |
| 2025-10-10 | 41102939.38 | -4915060.62 | -5284610.62 | False |
| 2025-10-11 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-12 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-13 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-14 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-15 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-16 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-17 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-18 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-19 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-20 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-21 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-22 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-23 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-24 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-25 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-26 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-27 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-28 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-29 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-30 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-10-31 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-11-01 | 40733389.38 | -5284610.62 | -5284610.62 | False |
| 2025-11-02 | 40733389.38 | -5284610.62 | -5284610.62 | False |

### request_03
Expected `873000`; actual `0`; baseline minimum `1092166.35`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2019-09-03 | 4670300 | -820700 | -4398833.65 | False |
| 2019-09-04 | 4670300 | -820700 | -4398833.65 | False |
| 2019-09-05 | 4670300 | -820700 | -4398833.65 | False |
| 2019-09-06 | 4670300 | -820700 | -4398833.65 | False |
| 2019-09-07 | 4312955.45 | -1178044.55 | -4398833.65 | False |
| 2019-09-08 | 4312955.45 | -1178044.55 | -4398833.65 | False |
| 2019-09-09 | 4312955.45 | -1178044.55 | -4398833.65 | False |
| 2019-09-10 | 4195155.45 | -1295844.55 | -4398833.65 | False |
| 2019-09-11 | 4195155.45 | -1295844.55 | -4398833.65 | False |
| 2019-09-12 | 4195155.45 | -1295844.55 | -4398833.65 | False |
| 2019-09-13 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-14 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-15 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-16 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-17 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-18 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-19 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-20 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-21 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-22 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-23 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-24 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-25 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-26 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-27 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-28 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-29 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-09-30 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-10-01 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-10-02 | 4174255.45 | -1316744.55 | -4398833.65 | False |
| 2019-10-03 | 3034255.45 | -2456744.55 | -4398833.65 | False |
| 2019-10-04 | 3034255.45 | -2456744.55 | -4398833.65 | False |
| 2019-10-05 | 3034255.45 | -2456744.55 | -4398833.65 | False |
| 2019-10-06 | 3034255.45 | -2456744.55 | -4398833.65 | False |
| 2019-10-07 | 2771910.90 | -2719089.10 | -4398833.65 | False |
| 2019-10-08 | 2771910.90 | -2719089.10 | -4398833.65 | False |
| 2019-10-09 | 2771910.90 | -2719089.10 | -4398833.65 | False |
| 2019-10-10 | 2654110.90 | -2836889.10 | -4398833.65 | False |
| 2019-10-11 | 2654110.90 | -2836889.10 | -4398833.65 | False |
| 2019-10-12 | 2654110.90 | -2836889.10 | -4398833.65 | False |
| 2019-10-13 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-14 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-15 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-16 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-17 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-18 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-19 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-20 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-21 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-22 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-23 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-24 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-25 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-26 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-27 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-28 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-29 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-30 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-10-31 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-11-01 | 2633210.90 | -2857789.10 | -4398833.65 | False |
| 2019-11-02 | 1493210.90 | -3997789.10 | -4398833.65 | False |
| 2019-11-03 | 1493210.90 | -3997789.10 | -4398833.65 | False |
| 2019-11-04 | 1493210.90 | -3997789.10 | -4398833.65 | False |
| 2019-11-05 | 1493210.90 | -3997789.10 | -4398833.65 | False |
| 2019-11-06 | 1230866.35 | -4260133.65 | -4398833.65 | False |
| 2019-11-07 | 1230866.35 | -4260133.65 | -4398833.65 | False |
| 2019-11-08 | 1230866.35 | -4260133.65 | -4398833.65 | False |
| 2019-11-09 | 1113066.35 | -4377933.65 | -4398833.65 | False |
| 2019-11-10 | 1113066.35 | -4377933.65 | -4398833.65 | False |
| 2019-11-11 | 1113066.35 | -4377933.65 | -4398833.65 | False |
| 2019-11-12 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-13 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-14 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-15 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-16 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-17 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-18 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-19 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-20 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-21 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-22 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-23 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-24 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-25 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-26 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-27 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-28 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-29 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-11-30 | 1092166.35 | -4398833.65 | -4398833.65 | False |
| 2019-12-01 | 1092166.35 | -4398833.65 | -4398833.65 | False |

### request_04
Expected `8401800`; actual `0`; baseline minimum `14691644.2`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2024-06-04 | 50202831.4 | 37509831.4 | 1998644.2 | False |
| 2024-06-05 | 50202831.4 | 37509831.4 | 1998644.2 | False |
| 2024-06-06 | 50202831.4 | 37509831.4 | 1998644.2 | False |
| 2024-06-07 | 50202831.4 | 37509831.4 | 1998644.2 | False |
| 2024-06-08 | 49174931.4 | 36481931.4 | 1998644.2 | False |
| 2024-06-09 | 48842431.4 | 36149431.4 | 1998644.2 | False |
| 2024-06-10 | 48842431.4 | 36149431.4 | 1998644.2 | False |
| 2024-06-11 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-12 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-13 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-14 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-15 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-16 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-17 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-18 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-19 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-20 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-21 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-22 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-23 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-24 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-25 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-26 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-27 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-28 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-29 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-06-30 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-07-01 | 46760981.4 | 34067981.4 | 1998644.2 | False |
| 2024-07-02 | 34467981.4 | 21774981.4 | 1998644.2 | False |
| 2024-07-03 | 34467981.4 | 21774981.4 | 1998644.2 | False |
| 2024-07-04 | 32463862.8 | 19770862.8 | 1998644.2 | False |
| 2024-07-05 | 32463862.8 | 19770862.8 | 1998644.2 | False |
| 2024-07-06 | 32463862.8 | 19770862.8 | 1998644.2 | False |
| 2024-07-07 | 32463862.8 | 19770862.8 | 1998644.2 | False |
| 2024-07-08 | 31435962.8 | 18742962.8 | 1998644.2 | False |
| 2024-07-09 | 31103462.8 | 18410462.8 | 1998644.2 | False |
| 2024-07-10 | 31103462.8 | 18410462.8 | 1998644.2 | False |
| 2024-07-11 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-12 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-13 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-14 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-15 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-16 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-17 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-18 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-19 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-20 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-21 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-22 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-23 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-24 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-25 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-26 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-27 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-28 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-29 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-30 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-07-31 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-08-01 | 30726312.8 | 18033312.8 | 1998644.2 | False |
| 2024-08-02 | 18433312.8 | 5740312.8 | 1998644.2 | False |
| 2024-08-03 | 16429194.2 | 3736194.2 | 1998644.2 | False |
| 2024-08-04 | 16429194.2 | 3736194.2 | 1998644.2 | False |
| 2024-08-05 | 16429194.2 | 3736194.2 | 1998644.2 | False |
| 2024-08-06 | 16429194.2 | 3736194.2 | 1998644.2 | False |
| 2024-08-07 | 15401294.2 | 2708294.2 | 1998644.2 | False |
| 2024-08-08 | 15068794.2 | 2375794.2 | 1998644.2 | False |
| 2024-08-09 | 15068794.2 | 2375794.2 | 1998644.2 | False |
| 2024-08-10 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-11 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-12 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-13 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-14 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-15 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-16 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-17 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-18 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-19 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-20 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-21 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-22 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-23 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-24 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-25 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-26 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-27 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-28 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-29 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-30 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-08-31 | 14691644.2 | 1998644.2 | 1998644.2 | False |
| 2024-09-01 | 14691644.2 | 1998644.2 | 1998644.2 | False |

### request_05
Expected `737`; actual `15488.00`; baseline minimum `31859.78`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2025-11-06 | 46475.1 | 30987.1 | 16371.78 | True |
| 2025-11-07 | 46475.1 | 30987.1 | 16371.78 | True |
| 2025-11-08 | 46475.1 | 30987.1 | 16371.78 | True |
| 2025-11-09 | 46475.1 | 30987.1 | 16371.78 | True |
| 2025-11-10 | 45507.1 | 30019.1 | 16371.78 | True |
| 2025-11-11 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-12 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-13 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-14 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-15 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-16 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-17 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-18 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-19 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-20 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-21 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-22 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-23 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-24 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-25 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-26 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-27 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-28 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-29 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-11-30 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-12-01 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-12-02 | 45393.8 | 29905.8 | 16371.78 | True |
| 2025-12-03 | 40421.8 | 24933.8 | 16371.78 | True |
| 2025-12-04 | 40421.8 | 24933.8 | 16371.78 | True |
| 2025-12-05 | 39708.09 | 24220.09 | 16371.78 | True |
| 2025-12-06 | 39708.09 | 24220.09 | 16371.78 | True |
| 2025-12-07 | 39708.09 | 24220.09 | 16371.78 | True |
| 2025-12-08 | 39708.09 | 24220.09 | 16371.78 | True |
| 2025-12-09 | 39708.09 | 24220.09 | 16371.78 | True |
| 2025-12-10 | 38740.09 | 23252.09 | 16371.78 | True |
| 2025-12-11 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-12 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-13 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-14 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-15 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-16 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-17 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-18 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-19 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-20 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-21 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-22 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-23 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-24 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-25 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-26 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-27 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-28 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-29 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-30 | 38626.79 | 23138.79 | 16371.78 | True |
| 2025-12-31 | 38626.79 | 23138.79 | 16371.78 | True |
| 2026-01-01 | 38626.79 | 23138.79 | 16371.78 | True |
| 2026-01-02 | 38626.79 | 23138.79 | 16371.78 | True |
| 2026-01-03 | 33654.79 | 18166.79 | 16371.78 | True |
| 2026-01-04 | 32941.08 | 17453.08 | 16371.78 | True |
| 2026-01-05 | 32941.08 | 17453.08 | 16371.78 | True |
| 2026-01-06 | 32941.08 | 17453.08 | 16371.78 | True |
| 2026-01-07 | 32941.08 | 17453.08 | 16371.78 | True |
| 2026-01-08 | 32941.08 | 17453.08 | 16371.78 | True |
| 2026-01-09 | 31973.08 | 16485.08 | 16371.78 | True |
| 2026-01-10 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-11 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-12 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-13 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-14 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-15 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-16 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-17 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-18 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-19 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-20 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-21 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-22 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-23 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-24 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-25 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-26 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-27 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-28 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-29 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-30 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-01-31 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-02-01 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-02-02 | 31859.78 | 16371.78 | 16371.78 | True |
| 2026-02-03 | 31859.78 | 16371.78 | 16371.78 | True |

### request_06
Expected `603.3`; actual `385.62`; baseline minimum `1128.62`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2026-01-03 | 1942.4 | 1322.0 | 508.22 | False |
| 2026-01-04 | 1942.4 | 1322.0 | 508.22 | False |
| 2026-01-05 | 1942.4 | 1322.0 | 508.22 | False |
| 2026-01-06 | 1890.54 | 1270.14 | 508.22 | False |
| 2026-01-07 | 1864.54 | 1244.14 | 508.22 | False |
| 2026-01-08 | 1864.54 | 1244.14 | 508.22 | False |
| 2026-01-09 | 1845.54 | 1225.14 | 508.22 | False |
| 2026-01-10 | 1845.54 | 1225.14 | 508.22 | False |
| 2026-01-11 | 1845.54 | 1225.14 | 508.22 | False |
| 2026-01-12 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-13 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-14 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-15 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-16 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-17 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-18 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-19 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-20 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-21 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-22 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-23 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-24 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-25 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-26 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-27 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-28 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-29 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-30 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-01-31 | 1840.54 | 1220.14 | 508.22 | False |
| 2026-02-01 | 1586.44 | 966.04 | 508.22 | False |
| 2026-02-02 | 1586.44 | 966.04 | 508.22 | False |
| 2026-02-03 | 1586.44 | 966.04 | 508.22 | False |
| 2026-02-04 | 1586.44 | 966.04 | 508.22 | False |
| 2026-02-05 | 1534.58 | 914.18 | 508.22 | False |
| 2026-02-06 | 1508.58 | 888.18 | 508.22 | False |
| 2026-02-07 | 1508.58 | 888.18 | 508.22 | False |
| 2026-02-08 | 1489.58 | 869.18 | 508.22 | False |
| 2026-02-09 | 1489.58 | 869.18 | 508.22 | False |
| 2026-02-10 | 1489.58 | 869.18 | 508.22 | False |
| 2026-02-11 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-12 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-13 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-14 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-15 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-16 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-17 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-18 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-19 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-20 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-21 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-22 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-23 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-24 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-25 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-26 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-27 | 1484.58 | 864.18 | 508.22 | False |
| 2026-02-28 | 1484.58 | 864.18 | 508.22 | False |
| 2026-03-01 | 1484.58 | 864.18 | 508.22 | False |
| 2026-03-02 | 1484.58 | 864.18 | 508.22 | False |
| 2026-03-03 | 1230.48 | 610.08 | 508.22 | False |
| 2026-03-04 | 1230.48 | 610.08 | 508.22 | False |
| 2026-03-05 | 1230.48 | 610.08 | 508.22 | False |
| 2026-03-06 | 1230.48 | 610.08 | 508.22 | False |
| 2026-03-07 | 1178.62 | 558.22 | 508.22 | False |
| 2026-03-08 | 1152.62 | 532.22 | 508.22 | False |
| 2026-03-09 | 1152.62 | 532.22 | 508.22 | False |
| 2026-03-10 | 1133.62 | 513.22 | 508.22 | False |
| 2026-03-11 | 1133.62 | 513.22 | 508.22 | False |
| 2026-03-12 | 1133.62 | 513.22 | 508.22 | False |
| 2026-03-13 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-14 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-15 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-16 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-17 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-18 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-19 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-20 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-21 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-22 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-23 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-24 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-25 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-26 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-27 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-28 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-29 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-30 | 1128.62 | 508.22 | 508.22 | False |
| 2026-03-31 | 1128.62 | 508.22 | 508.22 | False |
| 2026-04-01 | 1128.62 | 508.22 | 508.22 | False |
| 2026-04-02 | 1128.62 | 508.22 | 508.22 | False |

## Earliest-full-payment date traces

Every tested horizon date and post-payment minimum is retained for representative mismatches.
### request_02
Expected `2025-09-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2025-08-05 | -5284610.62 | False |
| 2025-08-06 | -5284610.62 | False |
| 2025-08-07 | -5284610.62 | False |
| 2025-08-08 | -5284610.62 | False |
| 2025-08-09 | -5284610.62 | False |
| 2025-08-10 | -5284610.62 | False |
| 2025-08-11 | -5284610.62 | False |
| 2025-08-12 | -5284610.62 | False |
| 2025-08-13 | -5284610.62 | False |
| 2025-08-14 | -5284610.62 | False |
| 2025-08-15 | -5284610.62 | False |
| 2025-08-16 | -5284610.62 | False |
| 2025-08-17 | -5284610.62 | False |
| 2025-08-18 | -5284610.62 | False |
| 2025-08-19 | -5284610.62 | False |
| 2025-08-20 | -5284610.62 | False |
| 2025-08-21 | -5284610.62 | False |
| 2025-08-22 | -5284610.62 | False |
| 2025-08-23 | -5284610.62 | False |
| 2025-08-24 | -5284610.62 | False |
| 2025-08-25 | -5284610.62 | False |
| 2025-08-26 | -5284610.62 | False |
| 2025-08-27 | -5284610.62 | False |
| 2025-08-28 | -5284610.62 | False |
| 2025-08-29 | -5284610.62 | False |
| 2025-08-30 | -5284610.62 | False |
| 2025-08-31 | -5284610.62 | False |
| 2025-09-01 | -5284610.62 | False |
| 2025-09-02 | -5284610.62 | False |
| 2025-09-03 | -5284610.62 | False |
| 2025-09-04 | -5284610.62 | False |
| 2025-09-05 | -5284610.62 | False |
| 2025-09-06 | -5284610.62 | False |
| 2025-09-07 | -5284610.62 | False |
| 2025-09-08 | -5284610.62 | False |
| 2025-09-09 | -5284610.62 | False |
| 2025-09-10 | -5284610.62 | False |
| 2025-09-11 | -5284610.62 | False |
| 2025-09-12 | -5284610.62 | False |
| 2025-09-13 | -5284610.62 | False |
| 2025-09-14 | -5284610.62 | False |
| 2025-09-15 | -5284610.62 | False |
| 2025-09-16 | -5284610.62 | False |
| 2025-09-17 | -5284610.62 | False |
| 2025-09-18 | -5284610.62 | False |
| 2025-09-19 | -5284610.62 | False |
| 2025-09-20 | -5284610.62 | False |
| 2025-09-21 | -5284610.62 | False |
| 2025-09-22 | -5284610.62 | False |
| 2025-09-23 | -5284610.62 | False |
| 2025-09-24 | -5284610.62 | False |
| 2025-09-25 | -5284610.62 | False |
| 2025-09-26 | -5284610.62 | False |
| 2025-09-27 | -5284610.62 | False |
| 2025-09-28 | -5284610.62 | False |
| 2025-09-29 | -5284610.62 | False |
| 2025-09-30 | -5284610.62 | False |
| 2025-10-01 | -5284610.62 | False |
| 2025-10-02 | -5284610.62 | False |
| 2025-10-03 | -5284610.62 | False |
| 2025-10-04 | -5284610.62 | False |
| 2025-10-05 | -5284610.62 | False |
| 2025-10-06 | -5284610.62 | False |
| 2025-10-07 | -5284610.62 | False |
| 2025-10-08 | -5284610.62 | False |
| 2025-10-09 | -5284610.62 | False |
| 2025-10-10 | -5284610.62 | False |
| 2025-10-11 | -5284610.62 | False |
| 2025-10-12 | -5284610.62 | False |
| 2025-10-13 | -5284610.62 | False |
| 2025-10-14 | -5284610.62 | False |
| 2025-10-15 | -5284610.62 | False |
| 2025-10-16 | -5284610.62 | False |
| 2025-10-17 | -5284610.62 | False |
| 2025-10-18 | -5284610.62 | False |
| 2025-10-19 | -5284610.62 | False |
| 2025-10-20 | -5284610.62 | False |
| 2025-10-21 | -5284610.62 | False |
| 2025-10-22 | -5284610.62 | False |
| 2025-10-23 | -5284610.62 | False |
| 2025-10-24 | -5284610.62 | False |
| 2025-10-25 | -5284610.62 | False |
| 2025-10-26 | -5284610.62 | False |
| 2025-10-27 | -5284610.62 | False |
| 2025-10-28 | -5284610.62 | False |
| 2025-10-29 | -5284610.62 | False |
| 2025-10-30 | -5284610.62 | False |
| 2025-10-31 | -5284610.62 | False |
| 2025-11-01 | -5284610.62 | False |
| 2025-11-02 | -5284610.62 | False |

### request_03
Expected `2019-11-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2019-09-03 | -4398833.65 | False |
| 2019-09-04 | -4398833.65 | False |
| 2019-09-05 | -4398833.65 | False |
| 2019-09-06 | -4398833.65 | False |
| 2019-09-07 | -4398833.65 | False |
| 2019-09-08 | -4398833.65 | False |
| 2019-09-09 | -4398833.65 | False |
| 2019-09-10 | -4398833.65 | False |
| 2019-09-11 | -4398833.65 | False |
| 2019-09-12 | -4398833.65 | False |
| 2019-09-13 | -4398833.65 | False |
| 2019-09-14 | -4398833.65 | False |
| 2019-09-15 | -4398833.65 | False |
| 2019-09-16 | -4398833.65 | False |
| 2019-09-17 | -4398833.65 | False |
| 2019-09-18 | -4398833.65 | False |
| 2019-09-19 | -4398833.65 | False |
| 2019-09-20 | -4398833.65 | False |
| 2019-09-21 | -4398833.65 | False |
| 2019-09-22 | -4398833.65 | False |
| 2019-09-23 | -4398833.65 | False |
| 2019-09-24 | -4398833.65 | False |
| 2019-09-25 | -4398833.65 | False |
| 2019-09-26 | -4398833.65 | False |
| 2019-09-27 | -4398833.65 | False |
| 2019-09-28 | -4398833.65 | False |
| 2019-09-29 | -4398833.65 | False |
| 2019-09-30 | -4398833.65 | False |
| 2019-10-01 | -4398833.65 | False |
| 2019-10-02 | -4398833.65 | False |
| 2019-10-03 | -4398833.65 | False |
| 2019-10-04 | -4398833.65 | False |
| 2019-10-05 | -4398833.65 | False |
| 2019-10-06 | -4398833.65 | False |
| 2019-10-07 | -4398833.65 | False |
| 2019-10-08 | -4398833.65 | False |
| 2019-10-09 | -4398833.65 | False |
| 2019-10-10 | -4398833.65 | False |
| 2019-10-11 | -4398833.65 | False |
| 2019-10-12 | -4398833.65 | False |
| 2019-10-13 | -4398833.65 | False |
| 2019-10-14 | -4398833.65 | False |
| 2019-10-15 | -4398833.65 | False |
| 2019-10-16 | -4398833.65 | False |
| 2019-10-17 | -4398833.65 | False |
| 2019-10-18 | -4398833.65 | False |
| 2019-10-19 | -4398833.65 | False |
| 2019-10-20 | -4398833.65 | False |
| 2019-10-21 | -4398833.65 | False |
| 2019-10-22 | -4398833.65 | False |
| 2019-10-23 | -4398833.65 | False |
| 2019-10-24 | -4398833.65 | False |
| 2019-10-25 | -4398833.65 | False |
| 2019-10-26 | -4398833.65 | False |
| 2019-10-27 | -4398833.65 | False |
| 2019-10-28 | -4398833.65 | False |
| 2019-10-29 | -4398833.65 | False |
| 2019-10-30 | -4398833.65 | False |
| 2019-10-31 | -4398833.65 | False |
| 2019-11-01 | -4398833.65 | False |
| 2019-11-02 | -4398833.65 | False |
| 2019-11-03 | -4398833.65 | False |
| 2019-11-04 | -4398833.65 | False |
| 2019-11-05 | -4398833.65 | False |
| 2019-11-06 | -4398833.65 | False |
| 2019-11-07 | -4398833.65 | False |
| 2019-11-08 | -4398833.65 | False |
| 2019-11-09 | -4398833.65 | False |
| 2019-11-10 | -4398833.65 | False |
| 2019-11-11 | -4398833.65 | False |
| 2019-11-12 | -4398833.65 | False |
| 2019-11-13 | -4398833.65 | False |
| 2019-11-14 | -4398833.65 | False |
| 2019-11-15 | -4398833.65 | False |
| 2019-11-16 | -4398833.65 | False |
| 2019-11-17 | -4398833.65 | False |
| 2019-11-18 | -4398833.65 | False |
| 2019-11-19 | -4398833.65 | False |
| 2019-11-20 | -4398833.65 | False |
| 2019-11-21 | -4398833.65 | False |
| 2019-11-22 | -4398833.65 | False |
| 2019-11-23 | -4398833.65 | False |
| 2019-11-24 | -4398833.65 | False |
| 2019-11-25 | -4398833.65 | False |
| 2019-11-26 | -4398833.65 | False |
| 2019-11-27 | -4398833.65 | False |
| 2019-11-28 | -4398833.65 | False |
| 2019-11-29 | -4398833.65 | False |
| 2019-11-30 | -4398833.65 | False |
| 2019-12-01 | -4398833.65 | False |

### request_04
Expected `2024-06-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2024-06-04 | 1998644.2 | False |
| 2024-06-05 | 1998644.2 | False |
| 2024-06-06 | 1998644.2 | False |
| 2024-06-07 | 1998644.2 | False |
| 2024-06-08 | 1998644.2 | False |
| 2024-06-09 | 1998644.2 | False |
| 2024-06-10 | 1998644.2 | False |
| 2024-06-11 | 1998644.2 | False |
| 2024-06-12 | 1998644.2 | False |
| 2024-06-13 | 1998644.2 | False |
| 2024-06-14 | 1998644.2 | False |
| 2024-06-15 | 1998644.2 | False |
| 2024-06-16 | 1998644.2 | False |
| 2024-06-17 | 1998644.2 | False |
| 2024-06-18 | 1998644.2 | False |
| 2024-06-19 | 1998644.2 | False |
| 2024-06-20 | 1998644.2 | False |
| 2024-06-21 | 1998644.2 | False |
| 2024-06-22 | 1998644.2 | False |
| 2024-06-23 | 1998644.2 | False |
| 2024-06-24 | 1998644.2 | False |
| 2024-06-25 | 1998644.2 | False |
| 2024-06-26 | 1998644.2 | False |
| 2024-06-27 | 1998644.2 | False |
| 2024-06-28 | 1998644.2 | False |
| 2024-06-29 | 1998644.2 | False |
| 2024-06-30 | 1998644.2 | False |
| 2024-07-01 | 1998644.2 | False |
| 2024-07-02 | 1998644.2 | False |
| 2024-07-03 | 1998644.2 | False |
| 2024-07-04 | 1998644.2 | False |
| 2024-07-05 | 1998644.2 | False |
| 2024-07-06 | 1998644.2 | False |
| 2024-07-07 | 1998644.2 | False |
| 2024-07-08 | 1998644.2 | False |
| 2024-07-09 | 1998644.2 | False |
| 2024-07-10 | 1998644.2 | False |
| 2024-07-11 | 1998644.2 | False |
| 2024-07-12 | 1998644.2 | False |
| 2024-07-13 | 1998644.2 | False |
| 2024-07-14 | 1998644.2 | False |
| 2024-07-15 | 1998644.2 | False |
| 2024-07-16 | 1998644.2 | False |
| 2024-07-17 | 1998644.2 | False |
| 2024-07-18 | 1998644.2 | False |
| 2024-07-19 | 1998644.2 | False |
| 2024-07-20 | 1998644.2 | False |
| 2024-07-21 | 1998644.2 | False |
| 2024-07-22 | 1998644.2 | False |
| 2024-07-23 | 1998644.2 | False |
| 2024-07-24 | 1998644.2 | False |
| 2024-07-25 | 1998644.2 | False |
| 2024-07-26 | 1998644.2 | False |
| 2024-07-27 | 1998644.2 | False |
| 2024-07-28 | 1998644.2 | False |
| 2024-07-29 | 1998644.2 | False |
| 2024-07-30 | 1998644.2 | False |
| 2024-07-31 | 1998644.2 | False |
| 2024-08-01 | 1998644.2 | False |
| 2024-08-02 | 1998644.2 | False |
| 2024-08-03 | 1998644.2 | False |
| 2024-08-04 | 1998644.2 | False |
| 2024-08-05 | 1998644.2 | False |
| 2024-08-06 | 1998644.2 | False |
| 2024-08-07 | 1998644.2 | False |
| 2024-08-08 | 1998644.2 | False |
| 2024-08-09 | 1998644.2 | False |
| 2024-08-10 | 1998644.2 | False |
| 2024-08-11 | 1998644.2 | False |
| 2024-08-12 | 1998644.2 | False |
| 2024-08-13 | 1998644.2 | False |
| 2024-08-14 | 1998644.2 | False |
| 2024-08-15 | 1998644.2 | False |
| 2024-08-16 | 1998644.2 | False |
| 2024-08-17 | 1998644.2 | False |
| 2024-08-18 | 1998644.2 | False |
| 2024-08-19 | 1998644.2 | False |
| 2024-08-20 | 1998644.2 | False |
| 2024-08-21 | 1998644.2 | False |
| 2024-08-22 | 1998644.2 | False |
| 2024-08-23 | 1998644.2 | False |
| 2024-08-24 | 1998644.2 | False |
| 2024-08-25 | 1998644.2 | False |
| 2024-08-26 | 1998644.2 | False |
| 2024-08-27 | 1998644.2 | False |
| 2024-08-28 | 1998644.2 | False |
| 2024-08-29 | 1998644.2 | False |
| 2024-08-30 | 1998644.2 | False |
| 2024-08-31 | 1998644.2 | False |
| 2024-09-01 | 1998644.2 | False |

### request_05
Expected ``; actual `2025-11-06`.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2025-11-06 | 16371.78 | True |
| 2025-11-07 | 16371.78 | True |
| 2025-11-08 | 16371.78 | True |
| 2025-11-09 | 16371.78 | True |
| 2025-11-10 | 16371.78 | True |
| 2025-11-11 | 16371.78 | True |
| 2025-11-12 | 16371.78 | True |
| 2025-11-13 | 16371.78 | True |
| 2025-11-14 | 16371.78 | True |
| 2025-11-15 | 16371.78 | True |
| 2025-11-16 | 16371.78 | True |
| 2025-11-17 | 16371.78 | True |
| 2025-11-18 | 16371.78 | True |
| 2025-11-19 | 16371.78 | True |
| 2025-11-20 | 16371.78 | True |
| 2025-11-21 | 16371.78 | True |
| 2025-11-22 | 16371.78 | True |
| 2025-11-23 | 16371.78 | True |
| 2025-11-24 | 16371.78 | True |
| 2025-11-25 | 16371.78 | True |
| 2025-11-26 | 16371.78 | True |
| 2025-11-27 | 16371.78 | True |
| 2025-11-28 | 16371.78 | True |
| 2025-11-29 | 16371.78 | True |
| 2025-11-30 | 16371.78 | True |
| 2025-12-01 | 16371.78 | True |
| 2025-12-02 | 16371.78 | True |
| 2025-12-03 | 16371.78 | True |
| 2025-12-04 | 16371.78 | True |
| 2025-12-05 | 16371.78 | True |
| 2025-12-06 | 16371.78 | True |
| 2025-12-07 | 16371.78 | True |
| 2025-12-08 | 16371.78 | True |
| 2025-12-09 | 16371.78 | True |
| 2025-12-10 | 16371.78 | True |
| 2025-12-11 | 16371.78 | True |
| 2025-12-12 | 16371.78 | True |
| 2025-12-13 | 16371.78 | True |
| 2025-12-14 | 16371.78 | True |
| 2025-12-15 | 16371.78 | True |
| 2025-12-16 | 16371.78 | True |
| 2025-12-17 | 16371.78 | True |
| 2025-12-18 | 16371.78 | True |
| 2025-12-19 | 16371.78 | True |
| 2025-12-20 | 16371.78 | True |
| 2025-12-21 | 16371.78 | True |
| 2025-12-22 | 16371.78 | True |
| 2025-12-23 | 16371.78 | True |
| 2025-12-24 | 16371.78 | True |
| 2025-12-25 | 16371.78 | True |
| 2025-12-26 | 16371.78 | True |
| 2025-12-27 | 16371.78 | True |
| 2025-12-28 | 16371.78 | True |
| 2025-12-29 | 16371.78 | True |
| 2025-12-30 | 16371.78 | True |
| 2025-12-31 | 16371.78 | True |
| 2026-01-01 | 16371.78 | True |
| 2026-01-02 | 16371.78 | True |
| 2026-01-03 | 16371.78 | True |
| 2026-01-04 | 16371.78 | True |
| 2026-01-05 | 16371.78 | True |
| 2026-01-06 | 16371.78 | True |
| 2026-01-07 | 16371.78 | True |
| 2026-01-08 | 16371.78 | True |
| 2026-01-09 | 16371.78 | True |
| 2026-01-10 | 16371.78 | True |
| 2026-01-11 | 16371.78 | True |
| 2026-01-12 | 16371.78 | True |
| 2026-01-13 | 16371.78 | True |
| 2026-01-14 | 16371.78 | True |
| 2026-01-15 | 16371.78 | True |
| 2026-01-16 | 16371.78 | True |
| 2026-01-17 | 16371.78 | True |
| 2026-01-18 | 16371.78 | True |
| 2026-01-19 | 16371.78 | True |
| 2026-01-20 | 16371.78 | True |
| 2026-01-21 | 16371.78 | True |
| 2026-01-22 | 16371.78 | True |
| 2026-01-23 | 16371.78 | True |
| 2026-01-24 | 16371.78 | True |
| 2026-01-25 | 16371.78 | True |
| 2026-01-26 | 16371.78 | True |
| 2026-01-27 | 16371.78 | True |
| 2026-01-28 | 16371.78 | True |
| 2026-01-29 | 16371.78 | True |
| 2026-01-30 | 16371.78 | True |
| 2026-01-31 | 16371.78 | True |
| 2026-02-01 | 16371.78 | True |
| 2026-02-02 | 16371.78 | True |
| 2026-02-03 | 16371.78 | True |

### request_06
Expected `2026-01-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2026-01-03 | 508.22 | False |
| 2026-01-04 | 508.22 | False |
| 2026-01-05 | 508.22 | False |
| 2026-01-06 | 508.22 | False |
| 2026-01-07 | 508.22 | False |
| 2026-01-08 | 508.22 | False |
| 2026-01-09 | 508.22 | False |
| 2026-01-10 | 508.22 | False |
| 2026-01-11 | 508.22 | False |
| 2026-01-12 | 508.22 | False |
| 2026-01-13 | 508.22 | False |
| 2026-01-14 | 508.22 | False |
| 2026-01-15 | 508.22 | False |
| 2026-01-16 | 508.22 | False |
| 2026-01-17 | 508.22 | False |
| 2026-01-18 | 508.22 | False |
| 2026-01-19 | 508.22 | False |
| 2026-01-20 | 508.22 | False |
| 2026-01-21 | 508.22 | False |
| 2026-01-22 | 508.22 | False |
| 2026-01-23 | 508.22 | False |
| 2026-01-24 | 508.22 | False |
| 2026-01-25 | 508.22 | False |
| 2026-01-26 | 508.22 | False |
| 2026-01-27 | 508.22 | False |
| 2026-01-28 | 508.22 | False |
| 2026-01-29 | 508.22 | False |
| 2026-01-30 | 508.22 | False |
| 2026-01-31 | 508.22 | False |
| 2026-02-01 | 508.22 | False |
| 2026-02-02 | 508.22 | False |
| 2026-02-03 | 508.22 | False |
| 2026-02-04 | 508.22 | False |
| 2026-02-05 | 508.22 | False |
| 2026-02-06 | 508.22 | False |
| 2026-02-07 | 508.22 | False |
| 2026-02-08 | 508.22 | False |
| 2026-02-09 | 508.22 | False |
| 2026-02-10 | 508.22 | False |
| 2026-02-11 | 508.22 | False |
| 2026-02-12 | 508.22 | False |
| 2026-02-13 | 508.22 | False |
| 2026-02-14 | 508.22 | False |
| 2026-02-15 | 508.22 | False |
| 2026-02-16 | 508.22 | False |
| 2026-02-17 | 508.22 | False |
| 2026-02-18 | 508.22 | False |
| 2026-02-19 | 508.22 | False |
| 2026-02-20 | 508.22 | False |
| 2026-02-21 | 508.22 | False |
| 2026-02-22 | 508.22 | False |
| 2026-02-23 | 508.22 | False |
| 2026-02-24 | 508.22 | False |
| 2026-02-25 | 508.22 | False |
| 2026-02-26 | 508.22 | False |
| 2026-02-27 | 508.22 | False |
| 2026-02-28 | 508.22 | False |
| 2026-03-01 | 508.22 | False |
| 2026-03-02 | 508.22 | False |
| 2026-03-03 | 508.22 | False |
| 2026-03-04 | 508.22 | False |
| 2026-03-05 | 508.22 | False |
| 2026-03-06 | 508.22 | False |
| 2026-03-07 | 508.22 | False |
| 2026-03-08 | 508.22 | False |
| 2026-03-09 | 508.22 | False |
| 2026-03-10 | 508.22 | False |
| 2026-03-11 | 508.22 | False |
| 2026-03-12 | 508.22 | False |
| 2026-03-13 | 508.22 | False |
| 2026-03-14 | 508.22 | False |
| 2026-03-15 | 508.22 | False |
| 2026-03-16 | 508.22 | False |
| 2026-03-17 | 508.22 | False |
| 2026-03-18 | 508.22 | False |
| 2026-03-19 | 508.22 | False |
| 2026-03-20 | 508.22 | False |
| 2026-03-21 | 508.22 | False |
| 2026-03-22 | 508.22 | False |
| 2026-03-23 | 508.22 | False |
| 2026-03-24 | 508.22 | False |
| 2026-03-25 | 508.22 | False |
| 2026-03-26 | 508.22 | False |
| 2026-03-27 | 508.22 | False |
| 2026-03-28 | 508.22 | False |
| 2026-03-29 | 508.22 | False |
| 2026-03-30 | 508.22 | False |
| 2026-03-31 | 508.22 | False |
| 2026-04-01 | 508.22 | False |
| 2026-04-02 | 508.22 | False |

## Root-cause interpretation

Categories are primary hypotheses from deterministic traces, not expected-answer special cases. No production code or supplied dataset was changed by this report generation.