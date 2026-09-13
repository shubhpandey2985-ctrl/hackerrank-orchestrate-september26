# Sample mismatch forensic report

Generated from repository data and current deterministic implementation. No expected answer is hardcoded.

## Harness verification

Expected rows: 25; actual rows: 25; joined by `request_id`. Expected header: `['request_id', 'user_id', 'request_date', 'request_type', 'requested_amount', 'desired_completion_date', 'allows_partial_payment', 'request_text', 'amount_safe_to_pay', 'affordability_status', 'recommended_payment_method', 'payment_plan', 'earliest_date_for_full_payment', 'spending_changes_needed', 'decision_explanation']`. Actual header: `['request_id', 'amount_safe_to_pay', 'affordability_status', 'recommended_payment_method', 'payment_plan', 'earliest_date_for_full_payment', 'spending_changes_needed', 'decision_explanation']`. Compared fields: amount_safe_to_pay, affordability_status, recommended_payment_method, payment_plan, earliest_date_for_full_payment, spending_changes_needed, decision_explanation. Numeric-equivalent trailing-zero differences are classified as `20. output serialization`.

## Root-cause priority

- 20. output serialization: 25 mismatching fields
- 12. earliest-safe-date calculation: 17 mismatching fields
- 19. deadline/status mapping: 15 mismatching fields
- 11. safe-amount calculation: 14 mismatching fields
- 18. candidate ranking: 14 mismatching fields
- 16. payment-method preference: 13 mismatching fields
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
- recommended_payment_method: 13
- payment_plan: 14
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
- Critical balances: `{'2024-03-03': '58481.1', '2024-03-05': '57913.5', '2024-03-15': '77204.2', '2024-03-20': '77204.2', '2024-05-31': '58849.6'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '25256', '2024-03-03', 1, '']), ('option_payment_option_01', True, [0, 0, '25256', '2024-03-03', 1, 'payment_option_01']), ('option_payment_option_02', False, None), ('option_payment_option_03', False, None), ('option_payment_option_04', False, None), ('wait', True, [0, 0, '25256', '2024-03-03', 1, ''])]`
- Validator: `True`
 
### request_02 — `amount_safe_to_pay`
- Expected: `17229139.2`
- Actual: `20760289.2`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '57600389.2', '2025-10-10': '47528489.2', '2025-11-02': '47158939.2'}`
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
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '57600389.2', '2025-10-10': '47528489.2', '2025-11-02': '47158939.2'}`
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
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '57600389.2', '2025-10-10': '47528489.2', '2025-11-02': '47158939.2'}`
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
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '57600389.2', '2025-10-10': '47528489.2', '2025-11-02': '47158939.2'}`
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
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '57600389.2', '2025-10-10': '47528489.2', '2025-11-02': '47158939.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_05', False, None), ('option_payment_option_06', False, None), ('option_payment_option_07', False, None)]`
- Validator: `True`
 
### request_02 — `decision_explanation`
- Expected: `Use 3 installments of IDR 15,952,906.67, starting 8 August 2025. This leaves at least IDR 29,158,400 available.`
- Actual: `Safe amount today is 20760289.2; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_02`; balance `60383889.2`; minimum `29158400`; preferences `['partial_payment', 'installments']`
- Request: amount `46018000` on `2025-08-05`, deadline `2025-10-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `1`; recurring `12`; flexible `10`; options `3`
- Critical balances: `{'2025-08-05': '60383889.2', '2025-08-08': '57600389.2', '2025-10-10': '47528489.2', '2025-11-02': '47158939.2'}`
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
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4575300', '2019-11-15': '1879200', '2019-12-01': '1879200'}`
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
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4575300', '2019-11-15': '1879200', '2019-12-01': '1879200'}`
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
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4575300', '2019-11-15': '1879200', '2019-12-01': '1879200'}`
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
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4575300', '2019-11-15': '1879200', '2019-12-01': '1879200'}`
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
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4575300', '2019-11-15': '1879200', '2019-12-01': '1879200'}`
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
- Critical balances: `{'2019-09-03': '4670300', '2019-09-07': '4575300', '2019-11-15': '1879200', '2019-12-01': '1879200'}`
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
- Critical balances: `{'2024-06-04': '52206950', '2024-06-11': '48765100', '2024-06-19': '48765100', '2024-09-01': '20704000'}`
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
- Critical balances: `{'2024-06-04': '52206950', '2024-06-11': '48765100', '2024-06-19': '48765100', '2024-09-01': '20704000'}`
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
- Critical balances: `{'2024-06-04': '52206950', '2024-06-11': '48765100', '2024-06-19': '48765100', '2024-09-01': '20704000'}`
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
- Critical balances: `{'2024-06-04': '52206950', '2024-06-11': '48765100', '2024-06-19': '48765100', '2024-09-01': '20704000'}`
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
- Critical balances: `{'2024-06-04': '52206950', '2024-06-11': '48765100', '2024-06-19': '48765100', '2024-09-01': '20704000'}`
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
- Critical balances: `{'2024-06-04': '52206950', '2024-06-11': '48765100', '2024-06-19': '48765100', '2024-09-01': '20704000'}`
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
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '33287.2', '2026-02-03': '33287.2'}`
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
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '33287.2', '2026-02-03': '33287.2'}`
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
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '33287.2', '2026-02-03': '33287.2'}`
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
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '33287.2', '2026-02-03': '33287.2'}`
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
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '33287.2', '2026-02-03': '33287.2'}`
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
- Critical balances: `{'2025-11-06': '46475.1', '2026-01-12': '33287.2', '2026-02-03': '33287.2'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '15488', '2025-11-06', 1, '']), ('option_payment_option_13', True, [0, 0, '15488', '2025-11-06', 1, 'payment_option_13']), ('option_payment_option_14', False, None), ('option_payment_option_15', False, None), ('wait', True, [0, 0, '15488', '2025-11-06', 1, ''])]`
- Validator: `True`
 
### request_06 — `amount_safe_to_pay`
- Expected: `603.3`
- Actual: `541.2`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
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
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
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
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
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
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
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
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
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
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_06 — `decision_explanation`
- Expected: `Stop the family streaming plan, then pay EUR 620.40 today. This leaves at least EUR 800 available.`
- Actual: `Safe amount today is 541.2; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_06`; balance `1942.4`; minimum `800`; preferences `['full_payment', 'partial_payment']`
- Request: amount `620.4` on `2026-01-03`, deadline `2026-01-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `27`; pending `0`; recurring `20`; flexible `5`; options `3`
- Critical balances: `{'2026-01-03': '1942.4', '2026-01-14': '1892.4', '2026-04-02': '1284.2'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_16', False, None), ('option_payment_option_17', False, None), ('option_payment_option_18', False, None)]`
- Validator: `True`
 
### request_07 — `amount_safe_to_pay`
- Expected: `87170.56`
- Actual: `12619.56`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '102604.56', '2024-12-03': '102604.56'}`
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
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '102604.56', '2024-12-03': '102604.56'}`
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
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '102604.56', '2024-12-03': '102604.56'}`
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
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '102604.56', '2024-12-03': '102604.56'}`
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
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '102604.56', '2024-12-03': '102604.56'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_19', False, None), ('option_payment_option_20', False, None), ('option_payment_option_21', False, None)]`
- Validator: `True`
 
### request_07 — `decision_explanation`
- Expected: `Use 3 installments of INR 68,432, starting 12 September 2024. This leaves at least INR 93,000 available.`
- Actual: `Safe amount today is 12619.56; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_07`; balance `218945.56`; minimum `93000`; preferences `['installments']`
- Request: amount `197400` on `2024-09-05`, deadline `2024-11-14`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `12`; pending `0`; recurring `7`; flexible `14`; options `3`
- Critical balances: `{'2024-09-05': '218945.56', '2024-11-14': '102604.56', '2024-12-03': '102604.56'}`
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
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-43.43', '2025-05-07': '-510.93'}`
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
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-43.43', '2025-05-07': '-510.93'}`
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
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-43.43', '2025-05-07': '-510.93'}`
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
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-43.43', '2025-05-07': '-510.93'}`
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
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-43.43', '2025-05-07': '-510.93'}`
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
- Critical balances: `{'2025-02-07': '1536.57', '2025-04-15': '-43.43', '2025-05-07': '-510.93'}`
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
- Critical balances: `{'2026-07-04': '2231.1', '2026-07-23': '2206.1', '2026-10-01': '1522.5'}`
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
- Critical balances: `{'2026-07-04': '2231.1', '2026-07-23': '2206.1', '2026-10-01': '1522.5'}`
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
- Critical balances: `{'2024-12-06': '750155', '2025-02-10': '592845', '2025-03-05': '583290'}`
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
- Critical balances: `{'2024-12-06': '750155', '2025-02-10': '592845', '2025-03-05': '583290'}`
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
- Critical balances: `{'2024-12-06': '750155', '2025-02-10': '592845', '2025-03-05': '583290'}`
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
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '53692645', '2025-07-31': '48520845'}`
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
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '53692645', '2025-07-31': '48520845'}`
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
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '53692645', '2025-07-31': '48520845'}`
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
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '53692645', '2025-07-31': '48520845'}`
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
- Credits `3` (scheduled `0`); debits `17`; pending `0`; recurring `13`; flexible `19`; options `4`
- Critical balances: `{'2025-05-03': '63531795', '2025-06-12': '53692645', '2025-07-31': '48520845'}`
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
- Credits `0` (scheduled `0`); debits `14`; pending `0`; recurring `6`; flexible `19`; options `3`
- Critical balances: `{'2026-04-05': '193089.89', '2026-04-19': '191137.39', '2026-05-20': '177392.89', '2026-06-20': '163648.39', '2026-07-03': '163648.39'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_33', True, [0, 0, '67770.57', '2026-04-19', 3, 'payment_option_33']), ('option_payment_option_34', False, None), ('option_payment_option_35', False, None)]`
- Validator: `True`
 
### request_13 — `amount_safe_to_pay`
- Expected: `433.4`
- Actual: `941.6`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2575.86', '2024-06-04': '1932.26'}`
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
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2575.86', '2024-06-04': '1932.26'}`
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
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2575.86', '2024-06-04': '1932.26'}`
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
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2575.86', '2024-06-04': '1932.26'}`
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
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2575.86', '2024-06-04': '1932.26'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_13 — `decision_explanation`
- Expected: `Pay EUR 941.60 in full on 15 May 2024. Paying earlier would take the balance below the EUR 1,300 minimum.`
- Actual: `Safe amount today is 941.6; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_13`; balance `2789.52`; minimum `1300`; preferences `['full_payment']`
- Request: amount `941.6` on `2024-03-07`, deadline `2024-05-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `25`; pending `0`; recurring `16`; flexible `15`; options `3`
- Critical balances: `{'2024-03-07': '2789.52', '2024-03-15': '4022.06', '2024-05-15': '2575.86', '2024-06-04': '1932.26'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_36', False, None), ('option_payment_option_37', False, None), ('option_payment_option_38', False, None)]`
- Validator: `True`
 
### request_14 — `amount_safe_to_pay`
- Expected: `597.74`
- Actual: `1381.74`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_14`; balance `3931.74`; minimum `2200`; preferences `['partial_payment']`
- Request: amount `5414.2` on `2025-08-04`, deadline `2025-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2025-08-04': '3931.74', '2025-10-04': '4543.54', '2025-11-01': '4179.54'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_39', False, None), ('option_payment_option_40', False, None)]`
- Validator: `True`
 
### request_14 — `decision_explanation`
- Expected: `Do not proceed with the EUR 5,414.20 request. Although EUR 597.74 is available today, the full amount cannot be completed safely within 90 days.`
- Actual: `Safe amount today is 1381.74; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_14`; balance `3931.74`; minimum `2200`; preferences `['partial_payment']`
- Request: amount `5414.2` on `2025-08-04`, deadline `2025-10-04`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `18`; pending `0`; recurring `10`; flexible `10`; options `2`
- Critical balances: `{'2025-08-04': '3931.74', '2025-10-04': '4543.54', '2025-11-01': '4179.54'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_39', False, None), ('option_payment_option_40', False, None)]`
- Validator: `True`
 
### request_15 — `amount_safe_to_pay`
- Expected: `83.05`
- Actual: `448.05`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_15`; balance `1770.05`; minimum `1200`; preferences `['partial_payment']`
- Request: amount `3685` on `2026-01-06`, deadline `2026-02-01`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `0`; recurring `15`; flexible `13`; options `3`
- Critical balances: `{'2026-01-06': '1770.05', '2026-02-01': '3309.05', '2026-04-05': '2193.85'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_41', False, None), ('option_payment_option_42', False, None), ('option_payment_option_43', False, None)]`
- Validator: `True`
 
### request_15 — `decision_explanation`
- Expected: `Do not make this payment by 1 February 2026. None of the available options keeps the EUR 1,200 minimum protected.`
- Actual: `Safe amount today is 448.05; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_15`; balance `1770.05`; minimum `1200`; preferences `['partial_payment']`
- Request: amount `3685` on `2026-01-06`, deadline `2026-02-01`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `0`; recurring `15`; flexible `13`; options `3`
- Critical balances: `{'2026-01-06': '1770.05', '2026-02-01': '3309.05', '2026-04-05': '2193.85'}`
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
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '104595', '2023-11-09': '46440'}`
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
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '104595', '2023-11-09': '46440'}`
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
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '104595', '2023-11-09': '46440'}`
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
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '104595', '2023-11-09': '46440'}`
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
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '104595', '2023-11-09': '46440'}`
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
- Critical balances: `{'2023-08-12': '362370', '2023-08-16': '262370', '2023-10-11': '104595', '2023-11-09': '46440'}`
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
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '674524.58', '2026-03-31': '672849.58', '2026-04-30': '589319.58', '2026-05-04': '589319.58', '2026-05-29': '505789.58'}`
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
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '674524.58', '2026-03-31': '672849.58', '2026-04-30': '589319.58', '2026-05-04': '589319.58', '2026-05-29': '505789.58'}`
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
- Critical balances: `{'2026-03-01': '550379.58', '2026-03-15': '674524.58', '2026-03-31': '672849.58', '2026-04-30': '589319.58', '2026-05-04': '589319.58', '2026-05-29': '505789.58'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_47', True, [0, 0, '285584.01', '2026-03-01', 3, 'payment_option_47']), ('option_payment_option_48', False, None), ('option_payment_option_49', False, None)]`
- Validator: `True`
 
### request_18 — `amount_safe_to_pay`
- Expected: `462`
- Actual: `381`
- Primary root cause: **11. safe-amount calculation**
- Diagnosis: `implementation bug`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2486', '2026-09-15': '1744', '2026-10-04': '1577'}`
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
- Critical balances: `{'2026-07-07': '2486', '2026-09-15': '1744', '2026-10-04': '1577'}`
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
- Critical balances: `{'2026-07-07': '2486', '2026-09-15': '1744', '2026-10-04': '1577'}`
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
- Critical balances: `{'2026-07-07': '2486', '2026-09-15': '1744', '2026-10-04': '1577'}`
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
- Critical balances: `{'2026-07-07': '2486', '2026-09-15': '1744', '2026-10-04': '1577'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_50', False, None), ('option_payment_option_51', False, None)]`
- Validator: `True`
 
### request_18 — `decision_explanation`
- Expected: `Pay EUR 3,246.10 in full on 15 September 2026. Paying earlier would take the balance below the EUR 1,400 minimum.`
- Actual: `Safe amount today is 381; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_18`; balance `2486`; minimum `1400`; preferences `['full_payment', 'partial_payment']`
- Request: amount `3246.1` on `2026-07-07`, deadline `2026-09-15`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `16`; pending `0`; recurring `10`; flexible `18`; options `2`
- Critical balances: `{'2026-07-07': '2486', '2026-09-15': '1744', '2026-10-04': '1577'}`
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
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '151200', '2024-12-02': '90610'}`
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
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '151200', '2024-12-02': '90610'}`
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
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '151200', '2024-12-02': '90610'}`
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
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '151200', '2024-12-02': '90610'}`
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
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '151200', '2024-12-02': '90610'}`
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
- Critical balances: `{'2024-09-04': '199545', '2024-10-04': '151200', '2024-12-02': '90610'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_52', False, None), ('option_payment_option_53', False, None), ('option_payment_option_54', False, None)]`
- Validator: `True`
 
### request_20 — `amount_safe_to_pay`
- Expected: `5400`
- Actual: `6975`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_20`; balance `102609.05`; minimum `64500`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `303700` on `2026-02-07`, deadline `2026-02-22`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `3`; recurring `12`; flexible `19`; options `2`
- Critical balances: `{'2026-02-07': '102609.05', '2026-02-08': '98139.05', '2026-02-09': '97435.00', '2026-02-14': '97070.00', '2026-02-22': '97070.00', '2026-05-07': '65910.00'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_55', False, None), ('option_payment_option_56', False, None)]`
- Validator: `True`
 
### request_20 — `decision_explanation`
- Expected: `Do not make this payment by 22 February 2026. None of the available options keeps the INR 64,500 minimum protected.`
- Actual: `Safe amount today is 6975; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_20`; balance `102609.05`; minimum `64500`; preferences `['full_payment', 'partial_payment', 'installments']`
- Request: amount `303700` on `2026-02-07`, deadline `2026-02-22`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `22`; pending `3`; recurring `12`; flexible `19`; options `2`
- Critical balances: `{'2026-02-07': '102609.05', '2026-02-08': '98139.05', '2026-02-09': '97435.00', '2026-02-14': '97070.00', '2026-02-22': '97070.00', '2026-05-07': '65910.00'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3858.35', '2026-04-14': '3800.35', '2026-04-15': '6056.35', '2026-07-01': '4502.75'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3858.35', '2026-04-14': '3800.35', '2026-04-15': '6056.35', '2026-07-01': '4502.75'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3858.35', '2026-04-14': '3800.35', '2026-04-15': '6056.35', '2026-07-01': '4502.75'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3858.35', '2026-04-14': '3800.35', '2026-04-15': '6056.35', '2026-07-01': '4502.75'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3858.35', '2026-04-14': '3800.35', '2026-04-15': '6056.35', '2026-07-01': '4502.75'}`
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
- Critical balances: `{'2026-04-03': '3911.35', '2026-04-05': '3858.35', '2026-04-14': '3800.35', '2026-04-15': '6056.35', '2026-07-01': '4502.75'}`
- Candidate rank keys: `[('full_today', True, [0, 0, '1574.4', '2026-04-03', 1, '']), ('option_payment_option_57', True, [0, 0, '1574.4', '2026-04-03', 1, 'payment_option_57']), ('option_payment_option_58', False, None), ('option_payment_option_59', False, None), ('option_payment_option_60', False, None), ('wait', True, [0, 0, '1574.4', '2026-04-03', 1, ''])]`
- Validator: `True`
 
### request_22 — `amount_safe_to_pay`
- Expected: `475.46`
- Actual: `261.06`
- Primary root cause: **2. event classification**
- Diagnosis: `implementation bug`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1089.46', '2025-02-10': '677.06', '2025-03-04': '649.06'}`
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
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1089.46', '2025-02-10': '677.06', '2025-03-04': '649.06'}`
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
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1089.46', '2025-02-10': '677.06', '2025-03-04': '649.06'}`
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
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1089.46', '2025-02-10': '677.06', '2025-03-04': '649.06'}`
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
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1089.46', '2025-02-10': '677.06', '2025-03-04': '649.06'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_61', False, None), ('option_payment_option_62', False, None), ('option_payment_option_63', False, None)]`
- Validator: `True`
 
### request_22 — `decision_explanation`
- Expected: `Use 3 installments of EUR 253.59, starting 8 December 2024. This leaves at least EUR 500 available.`
- Actual: `Safe amount today is 261.06; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_22`; balance `1132.46`; minimum `500`; preferences `['installments']`
- Request: amount `731.5` on `2024-12-05`, deadline `2025-02-10`
- Actual selected plan: `none` via `not_recommended`
- Credits `1` (scheduled `0`); debits `24`; pending `1`; recurring `15`; flexible `10`; options `3`
- Critical balances: `{'2024-12-05': '1132.46', '2024-12-08': '1089.46', '2025-02-10': '677.06', '2025-03-04': '649.06'}`
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
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '50404.7', '2025-07-15': '1632.9', '2025-08-04': '1337.0'}`
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
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '50404.7', '2025-07-15': '1632.9', '2025-08-04': '1337.0'}`
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
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '50404.7', '2025-07-15': '1632.9', '2025-08-04': '1337.0'}`
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
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '50404.7', '2025-07-15': '1632.9', '2025-08-04': '1337.0'}`
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
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '50404.7', '2025-07-15': '1632.9', '2025-08-04': '1337.0'}`
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
- Critical balances: `{'2025-05-07': '51957.9', '2025-05-11': '50404.7', '2025-07-15': '1632.9', '2025-08-04': '1337.0'}`
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
- Critical balances: `{'2026-01-04': '85045', '2026-01-11': '79150', '2026-02-08': '56840', '2026-04-03': '33820'}`
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
- Critical balances: `{'2026-01-04': '85045', '2026-01-11': '79150', '2026-02-08': '56840', '2026-04-03': '33820'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_67', False, None), ('option_payment_option_68', False, None)]`
- Validator: `True`
 
### request_25 — `amount_safe_to_pay`
- Expected: `1425000`
- Actual: `7079400`
- Primary root cause: **7. scheduled-credit semantics**
- Diagnosis: `incorrect assumption in our architecture`
- User/profile: `user_25`; balance `32063050`; minimum `23379100`; preferences `['full_payment', 'installments']`
- Request: amount `60496000` on `2024-03-06`, deadline `2024-04-17`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `28`; pending `0`; recurring `19`; flexible `0`; options `3`
- Critical balances: `{'2024-03-06': '32063050', '2024-03-15': '58958494.00', '2024-04-17': '50399944.00', '2024-06-03': '41841394.00'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_69', False, None), ('option_payment_option_70', False, None), ('option_payment_option_71', False, None)]`
- Validator: `True`
 
### request_25 — `decision_explanation`
- Expected: `Do not make this payment by 17 April 2024. None of the available options keeps the IDR 23,379,100 minimum protected.`
- Actual: `Safe amount today is 7079400; the full amount is not safe within the requested plan.`
- Primary root cause: **20. output serialization**
- Diagnosis: `output-formatting issue`
- User/profile: `user_25`; balance `32063050`; minimum `23379100`; preferences `['full_payment', 'installments']`
- Request: amount `60496000` on `2024-03-06`, deadline `2024-04-17`
- Actual selected plan: `none` via `not_recommended`
- Credits `2` (scheduled `1`); debits `28`; pending `0`; recurring `19`; flexible `0`; options `3`
- Critical balances: `{'2024-03-06': '32063050', '2024-03-15': '58958494.00', '2024-04-17': '50399944.00', '2024-06-03': '41841394.00'}`
- Candidate rank keys: `[('full_today', False, None), ('option_payment_option_69', False, None), ('option_payment_option_70', False, None), ('option_payment_option_71', False, None)]`
- Validator: `True`
 
## Mathematical safe-amount traces

Representative traces show deterministic date-by-date balances; expected amounts are comparison-only.
### request_02
Expected `17229139.2`; actual `20760289.20`; baseline minimum `47158939.2`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2025-08-05 | 60383889.2 | 14365889.2 | 1140939.2 | False |
| 2025-08-06 | 60383889.2 | 14365889.2 | 1140939.2 | False |
| 2025-08-07 | 59251489.2 | 13233489.2 | 1140939.2 | False |
| 2025-08-08 | 57600389.2 | 11582389.2 | 1140939.2 | False |
| 2025-08-09 | 57600389.2 | 11582389.2 | 1140939.2 | False |
| 2025-08-10 | 57600389.2 | 11582389.2 | 1140939.2 | False |
| 2025-08-11 | 57600389.2 | 11582389.2 | 1140939.2 | False |
| 2025-08-12 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-13 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-14 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-15 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-16 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-17 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-18 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-19 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-20 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-21 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-22 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-23 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-24 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-25 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-26 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-27 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-28 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-29 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-30 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-08-31 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-09-01 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-09-02 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-09-03 | 57230839.2 | 11212839.2 | 1140939.2 | False |
| 2025-09-04 | 53696839.2 | 7678839.2 | 1140939.2 | False |
| 2025-09-05 | 53696839.2 | 7678839.2 | 1140939.2 | False |
| 2025-09-06 | 52564439.2 | 6546439.2 | 1140939.2 | False |
| 2025-09-07 | 52564439.2 | 6546439.2 | 1140939.2 | False |
| 2025-09-08 | 52564439.2 | 6546439.2 | 1140939.2 | False |
| 2025-09-09 | 52564439.2 | 6546439.2 | 1140939.2 | False |
| 2025-09-10 | 52564439.2 | 6546439.2 | 1140939.2 | False |
| 2025-09-11 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-12 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-13 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-14 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-15 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-16 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-17 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-18 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-19 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-20 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-21 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-22 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-23 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-24 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-25 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-26 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-27 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-28 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-29 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-09-30 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-10-01 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-10-02 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-10-03 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-10-04 | 52194889.2 | 6176889.2 | 1140939.2 | False |
| 2025-10-05 | 48660889.2 | 2642889.2 | 1140939.2 | False |
| 2025-10-06 | 47528489.2 | 1510489.2 | 1140939.2 | False |
| 2025-10-07 | 47528489.2 | 1510489.2 | 1140939.2 | False |
| 2025-10-08 | 47528489.2 | 1510489.2 | 1140939.2 | False |
| 2025-10-09 | 47528489.2 | 1510489.2 | 1140939.2 | False |
| 2025-10-10 | 47528489.2 | 1510489.2 | 1140939.2 | False |
| 2025-10-11 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-12 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-13 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-14 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-15 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-16 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-17 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-18 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-19 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-20 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-21 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-22 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-23 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-24 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-25 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-26 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-27 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-28 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-29 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-30 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-10-31 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-11-01 | 47158939.2 | 1140939.2 | 1140939.2 | False |
| 2025-11-02 | 47158939.2 | 1140939.2 | 1140939.2 | False |

### request_03
Expected `873000`; actual `0`; baseline minimum `1879200`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2019-09-03 | 4670300 | -820700 | -3611800 | False |
| 2019-09-04 | 4670300 | -820700 | -3611800 | False |
| 2019-09-05 | 4670300 | -820700 | -3611800 | False |
| 2019-09-06 | 4670300 | -820700 | -3611800 | False |
| 2019-09-07 | 4575300 | -915700 | -3611800 | False |
| 2019-09-08 | 4575300 | -915700 | -3611800 | False |
| 2019-09-09 | 4575300 | -915700 | -3611800 | False |
| 2019-09-10 | 4457500 | -1033500 | -3611800 | False |
| 2019-09-11 | 4457500 | -1033500 | -3611800 | False |
| 2019-09-12 | 4457500 | -1033500 | -3611800 | False |
| 2019-09-13 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-14 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-15 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-16 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-17 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-18 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-19 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-20 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-21 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-22 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-23 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-24 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-25 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-26 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-27 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-28 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-29 | 4436600 | -1054400 | -3611800 | False |
| 2019-09-30 | 4436600 | -1054400 | -3611800 | False |
| 2019-10-01 | 4436600 | -1054400 | -3611800 | False |
| 2019-10-02 | 4436600 | -1054400 | -3611800 | False |
| 2019-10-03 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-04 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-05 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-06 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-07 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-08 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-09 | 3296600 | -2194400 | -3611800 | False |
| 2019-10-10 | 3178800 | -2312200 | -3611800 | False |
| 2019-10-11 | 3178800 | -2312200 | -3611800 | False |
| 2019-10-12 | 3178800 | -2312200 | -3611800 | False |
| 2019-10-13 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-14 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-15 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-16 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-17 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-18 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-19 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-20 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-21 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-22 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-23 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-24 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-25 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-26 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-27 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-28 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-29 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-30 | 3157900 | -2333100 | -3611800 | False |
| 2019-10-31 | 3157900 | -2333100 | -3611800 | False |
| 2019-11-01 | 3157900 | -2333100 | -3611800 | False |
| 2019-11-02 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-03 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-04 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-05 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-06 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-07 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-08 | 2017900 | -3473100 | -3611800 | False |
| 2019-11-09 | 1900100 | -3590900 | -3611800 | False |
| 2019-11-10 | 1900100 | -3590900 | -3611800 | False |
| 2019-11-11 | 1900100 | -3590900 | -3611800 | False |
| 2019-11-12 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-13 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-14 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-15 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-16 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-17 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-18 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-19 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-20 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-21 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-22 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-23 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-24 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-25 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-26 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-27 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-28 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-29 | 1879200 | -3611800 | -3611800 | False |
| 2019-11-30 | 1879200 | -3611800 | -3611800 | False |
| 2019-12-01 | 1879200 | -3611800 | -3611800 | False |

### request_04
Expected `8401800`; actual `0`; baseline minimum `20704000`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2024-06-04 | 52206950 | 39513950 | 8011000 | False |
| 2024-06-05 | 52206950 | 39513950 | 8011000 | False |
| 2024-06-06 | 52206950 | 39513950 | 8011000 | False |
| 2024-06-07 | 52206950 | 39513950 | 8011000 | False |
| 2024-06-08 | 51179050 | 38486050 | 8011000 | False |
| 2024-06-09 | 50846550 | 38153550 | 8011000 | False |
| 2024-06-10 | 50846550 | 38153550 | 8011000 | False |
| 2024-06-11 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-12 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-13 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-14 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-15 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-16 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-17 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-18 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-19 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-20 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-21 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-22 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-23 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-24 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-25 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-26 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-27 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-28 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-29 | 48765100 | 36072100 | 8011000 | False |
| 2024-06-30 | 48765100 | 36072100 | 8011000 | False |
| 2024-07-01 | 48765100 | 36072100 | 8011000 | False |
| 2024-07-02 | 36472100 | 23779100 | 8011000 | False |
| 2024-07-03 | 36472100 | 23779100 | 8011000 | False |
| 2024-07-04 | 36472100 | 23779100 | 8011000 | False |
| 2024-07-05 | 36472100 | 23779100 | 8011000 | False |
| 2024-07-06 | 36472100 | 23779100 | 8011000 | False |
| 2024-07-07 | 36472100 | 23779100 | 8011000 | False |
| 2024-07-08 | 35444200 | 22751200 | 8011000 | False |
| 2024-07-09 | 35111700 | 22418700 | 8011000 | False |
| 2024-07-10 | 35111700 | 22418700 | 8011000 | False |
| 2024-07-11 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-12 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-13 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-14 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-15 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-16 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-17 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-18 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-19 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-20 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-21 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-22 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-23 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-24 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-25 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-26 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-27 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-28 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-29 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-30 | 34734550 | 22041550 | 8011000 | False |
| 2024-07-31 | 34734550 | 22041550 | 8011000 | False |
| 2024-08-01 | 34734550 | 22041550 | 8011000 | False |
| 2024-08-02 | 22441550 | 9748550 | 8011000 | False |
| 2024-08-03 | 22441550 | 9748550 | 8011000 | False |
| 2024-08-04 | 22441550 | 9748550 | 8011000 | False |
| 2024-08-05 | 22441550 | 9748550 | 8011000 | False |
| 2024-08-06 | 22441550 | 9748550 | 8011000 | False |
| 2024-08-07 | 21413650 | 8720650 | 8011000 | False |
| 2024-08-08 | 21081150 | 8388150 | 8011000 | False |
| 2024-08-09 | 21081150 | 8388150 | 8011000 | False |
| 2024-08-10 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-11 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-12 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-13 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-14 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-15 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-16 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-17 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-18 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-19 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-20 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-21 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-22 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-23 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-24 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-25 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-26 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-27 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-28 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-29 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-30 | 20704000 | 8011000 | 8011000 | False |
| 2024-08-31 | 20704000 | 8011000 | 8011000 | False |
| 2024-09-01 | 20704000 | 8011000 | 8011000 | False |

### request_05
Expected `737`; actual `15488.00`; baseline minimum `33287.2`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2025-11-06 | 46475.1 | 30987.1 | 17799.2 | True |
| 2025-11-07 | 46475.1 | 30987.1 | 17799.2 | True |
| 2025-11-08 | 46475.1 | 30987.1 | 17799.2 | True |
| 2025-11-09 | 46475.1 | 30987.1 | 17799.2 | True |
| 2025-11-10 | 45507.1 | 30019.1 | 17799.2 | True |
| 2025-11-11 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-12 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-13 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-14 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-15 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-16 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-17 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-18 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-19 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-20 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-21 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-22 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-23 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-24 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-25 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-26 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-27 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-28 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-29 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-11-30 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-12-01 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-12-02 | 45393.8 | 29905.8 | 17799.2 | True |
| 2025-12-03 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-04 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-05 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-06 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-07 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-08 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-09 | 40421.8 | 24933.8 | 17799.2 | True |
| 2025-12-10 | 39453.8 | 23965.8 | 17799.2 | True |
| 2025-12-11 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-12 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-13 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-14 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-15 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-16 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-17 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-18 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-19 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-20 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-21 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-22 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-23 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-24 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-25 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-26 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-27 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-28 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-29 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-30 | 39340.5 | 23852.5 | 17799.2 | True |
| 2025-12-31 | 39340.5 | 23852.5 | 17799.2 | True |
| 2026-01-01 | 39340.5 | 23852.5 | 17799.2 | True |
| 2026-01-02 | 39340.5 | 23852.5 | 17799.2 | True |
| 2026-01-03 | 34368.5 | 18880.5 | 17799.2 | True |
| 2026-01-04 | 34368.5 | 18880.5 | 17799.2 | True |
| 2026-01-05 | 34368.5 | 18880.5 | 17799.2 | True |
| 2026-01-06 | 34368.5 | 18880.5 | 17799.2 | True |
| 2026-01-07 | 34368.5 | 18880.5 | 17799.2 | True |
| 2026-01-08 | 34368.5 | 18880.5 | 17799.2 | True |
| 2026-01-09 | 33400.5 | 17912.5 | 17799.2 | True |
| 2026-01-10 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-11 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-12 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-13 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-14 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-15 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-16 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-17 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-18 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-19 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-20 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-21 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-22 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-23 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-24 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-25 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-26 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-27 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-28 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-29 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-30 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-01-31 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-02-01 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-02-02 | 33287.2 | 17799.2 | 17799.2 | True |
| 2026-02-03 | 33287.2 | 17799.2 | 17799.2 | True |

### request_06
Expected `603.3`; actual `541.20`; baseline minimum `1284.2`.

| date | baseline | after full payment | min after payment | safe |
|---|---:|---:|---:|:---:|
| 2026-01-03 | 1942.4 | 1322.0 | 663.8 | False |
| 2026-01-04 | 1942.4 | 1322.0 | 663.8 | False |
| 2026-01-05 | 1942.4 | 1322.0 | 663.8 | False |
| 2026-01-06 | 1942.4 | 1322.0 | 663.8 | False |
| 2026-01-07 | 1916.4 | 1296.0 | 663.8 | False |
| 2026-01-08 | 1916.4 | 1296.0 | 663.8 | False |
| 2026-01-09 | 1897.4 | 1277.0 | 663.8 | False |
| 2026-01-10 | 1897.4 | 1277.0 | 663.8 | False |
| 2026-01-11 | 1897.4 | 1277.0 | 663.8 | False |
| 2026-01-12 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-13 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-14 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-15 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-16 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-17 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-18 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-19 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-20 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-21 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-22 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-23 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-24 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-25 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-26 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-27 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-28 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-29 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-30 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-01-31 | 1892.4 | 1272.0 | 663.8 | False |
| 2026-02-01 | 1638.3 | 1017.9 | 663.8 | False |
| 2026-02-02 | 1638.3 | 1017.9 | 663.8 | False |
| 2026-02-03 | 1638.3 | 1017.9 | 663.8 | False |
| 2026-02-04 | 1638.3 | 1017.9 | 663.8 | False |
| 2026-02-05 | 1638.3 | 1017.9 | 663.8 | False |
| 2026-02-06 | 1612.3 | 991.9 | 663.8 | False |
| 2026-02-07 | 1612.3 | 991.9 | 663.8 | False |
| 2026-02-08 | 1593.3 | 972.9 | 663.8 | False |
| 2026-02-09 | 1593.3 | 972.9 | 663.8 | False |
| 2026-02-10 | 1593.3 | 972.9 | 663.8 | False |
| 2026-02-11 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-12 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-13 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-14 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-15 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-16 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-17 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-18 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-19 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-20 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-21 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-22 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-23 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-24 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-25 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-26 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-27 | 1588.3 | 967.9 | 663.8 | False |
| 2026-02-28 | 1588.3 | 967.9 | 663.8 | False |
| 2026-03-01 | 1588.3 | 967.9 | 663.8 | False |
| 2026-03-02 | 1588.3 | 967.9 | 663.8 | False |
| 2026-03-03 | 1334.2 | 713.8 | 663.8 | False |
| 2026-03-04 | 1334.2 | 713.8 | 663.8 | False |
| 2026-03-05 | 1334.2 | 713.8 | 663.8 | False |
| 2026-03-06 | 1334.2 | 713.8 | 663.8 | False |
| 2026-03-07 | 1334.2 | 713.8 | 663.8 | False |
| 2026-03-08 | 1308.2 | 687.8 | 663.8 | False |
| 2026-03-09 | 1308.2 | 687.8 | 663.8 | False |
| 2026-03-10 | 1289.2 | 668.8 | 663.8 | False |
| 2026-03-11 | 1289.2 | 668.8 | 663.8 | False |
| 2026-03-12 | 1289.2 | 668.8 | 663.8 | False |
| 2026-03-13 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-14 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-15 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-16 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-17 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-18 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-19 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-20 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-21 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-22 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-23 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-24 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-25 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-26 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-27 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-28 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-29 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-30 | 1284.2 | 663.8 | 663.8 | False |
| 2026-03-31 | 1284.2 | 663.8 | 663.8 | False |
| 2026-04-01 | 1284.2 | 663.8 | 663.8 | False |
| 2026-04-02 | 1284.2 | 663.8 | 663.8 | False |

## Earliest-full-payment date traces

Every tested horizon date and post-payment minimum is retained for representative mismatches.
### request_02
Expected `2025-09-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2025-08-05 | 1140939.2 | False |
| 2025-08-06 | 1140939.2 | False |
| 2025-08-07 | 1140939.2 | False |
| 2025-08-08 | 1140939.2 | False |
| 2025-08-09 | 1140939.2 | False |
| 2025-08-10 | 1140939.2 | False |
| 2025-08-11 | 1140939.2 | False |
| 2025-08-12 | 1140939.2 | False |
| 2025-08-13 | 1140939.2 | False |
| 2025-08-14 | 1140939.2 | False |
| 2025-08-15 | 1140939.2 | False |
| 2025-08-16 | 1140939.2 | False |
| 2025-08-17 | 1140939.2 | False |
| 2025-08-18 | 1140939.2 | False |
| 2025-08-19 | 1140939.2 | False |
| 2025-08-20 | 1140939.2 | False |
| 2025-08-21 | 1140939.2 | False |
| 2025-08-22 | 1140939.2 | False |
| 2025-08-23 | 1140939.2 | False |
| 2025-08-24 | 1140939.2 | False |
| 2025-08-25 | 1140939.2 | False |
| 2025-08-26 | 1140939.2 | False |
| 2025-08-27 | 1140939.2 | False |
| 2025-08-28 | 1140939.2 | False |
| 2025-08-29 | 1140939.2 | False |
| 2025-08-30 | 1140939.2 | False |
| 2025-08-31 | 1140939.2 | False |
| 2025-09-01 | 1140939.2 | False |
| 2025-09-02 | 1140939.2 | False |
| 2025-09-03 | 1140939.2 | False |
| 2025-09-04 | 1140939.2 | False |
| 2025-09-05 | 1140939.2 | False |
| 2025-09-06 | 1140939.2 | False |
| 2025-09-07 | 1140939.2 | False |
| 2025-09-08 | 1140939.2 | False |
| 2025-09-09 | 1140939.2 | False |
| 2025-09-10 | 1140939.2 | False |
| 2025-09-11 | 1140939.2 | False |
| 2025-09-12 | 1140939.2 | False |
| 2025-09-13 | 1140939.2 | False |
| 2025-09-14 | 1140939.2 | False |
| 2025-09-15 | 1140939.2 | False |
| 2025-09-16 | 1140939.2 | False |
| 2025-09-17 | 1140939.2 | False |
| 2025-09-18 | 1140939.2 | False |
| 2025-09-19 | 1140939.2 | False |
| 2025-09-20 | 1140939.2 | False |
| 2025-09-21 | 1140939.2 | False |
| 2025-09-22 | 1140939.2 | False |
| 2025-09-23 | 1140939.2 | False |
| 2025-09-24 | 1140939.2 | False |
| 2025-09-25 | 1140939.2 | False |
| 2025-09-26 | 1140939.2 | False |
| 2025-09-27 | 1140939.2 | False |
| 2025-09-28 | 1140939.2 | False |
| 2025-09-29 | 1140939.2 | False |
| 2025-09-30 | 1140939.2 | False |
| 2025-10-01 | 1140939.2 | False |
| 2025-10-02 | 1140939.2 | False |
| 2025-10-03 | 1140939.2 | False |
| 2025-10-04 | 1140939.2 | False |
| 2025-10-05 | 1140939.2 | False |
| 2025-10-06 | 1140939.2 | False |
| 2025-10-07 | 1140939.2 | False |
| 2025-10-08 | 1140939.2 | False |
| 2025-10-09 | 1140939.2 | False |
| 2025-10-10 | 1140939.2 | False |
| 2025-10-11 | 1140939.2 | False |
| 2025-10-12 | 1140939.2 | False |
| 2025-10-13 | 1140939.2 | False |
| 2025-10-14 | 1140939.2 | False |
| 2025-10-15 | 1140939.2 | False |
| 2025-10-16 | 1140939.2 | False |
| 2025-10-17 | 1140939.2 | False |
| 2025-10-18 | 1140939.2 | False |
| 2025-10-19 | 1140939.2 | False |
| 2025-10-20 | 1140939.2 | False |
| 2025-10-21 | 1140939.2 | False |
| 2025-10-22 | 1140939.2 | False |
| 2025-10-23 | 1140939.2 | False |
| 2025-10-24 | 1140939.2 | False |
| 2025-10-25 | 1140939.2 | False |
| 2025-10-26 | 1140939.2 | False |
| 2025-10-27 | 1140939.2 | False |
| 2025-10-28 | 1140939.2 | False |
| 2025-10-29 | 1140939.2 | False |
| 2025-10-30 | 1140939.2 | False |
| 2025-10-31 | 1140939.2 | False |
| 2025-11-01 | 1140939.2 | False |
| 2025-11-02 | 1140939.2 | False |

### request_03
Expected `2019-11-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2019-09-03 | -3611800 | False |
| 2019-09-04 | -3611800 | False |
| 2019-09-05 | -3611800 | False |
| 2019-09-06 | -3611800 | False |
| 2019-09-07 | -3611800 | False |
| 2019-09-08 | -3611800 | False |
| 2019-09-09 | -3611800 | False |
| 2019-09-10 | -3611800 | False |
| 2019-09-11 | -3611800 | False |
| 2019-09-12 | -3611800 | False |
| 2019-09-13 | -3611800 | False |
| 2019-09-14 | -3611800 | False |
| 2019-09-15 | -3611800 | False |
| 2019-09-16 | -3611800 | False |
| 2019-09-17 | -3611800 | False |
| 2019-09-18 | -3611800 | False |
| 2019-09-19 | -3611800 | False |
| 2019-09-20 | -3611800 | False |
| 2019-09-21 | -3611800 | False |
| 2019-09-22 | -3611800 | False |
| 2019-09-23 | -3611800 | False |
| 2019-09-24 | -3611800 | False |
| 2019-09-25 | -3611800 | False |
| 2019-09-26 | -3611800 | False |
| 2019-09-27 | -3611800 | False |
| 2019-09-28 | -3611800 | False |
| 2019-09-29 | -3611800 | False |
| 2019-09-30 | -3611800 | False |
| 2019-10-01 | -3611800 | False |
| 2019-10-02 | -3611800 | False |
| 2019-10-03 | -3611800 | False |
| 2019-10-04 | -3611800 | False |
| 2019-10-05 | -3611800 | False |
| 2019-10-06 | -3611800 | False |
| 2019-10-07 | -3611800 | False |
| 2019-10-08 | -3611800 | False |
| 2019-10-09 | -3611800 | False |
| 2019-10-10 | -3611800 | False |
| 2019-10-11 | -3611800 | False |
| 2019-10-12 | -3611800 | False |
| 2019-10-13 | -3611800 | False |
| 2019-10-14 | -3611800 | False |
| 2019-10-15 | -3611800 | False |
| 2019-10-16 | -3611800 | False |
| 2019-10-17 | -3611800 | False |
| 2019-10-18 | -3611800 | False |
| 2019-10-19 | -3611800 | False |
| 2019-10-20 | -3611800 | False |
| 2019-10-21 | -3611800 | False |
| 2019-10-22 | -3611800 | False |
| 2019-10-23 | -3611800 | False |
| 2019-10-24 | -3611800 | False |
| 2019-10-25 | -3611800 | False |
| 2019-10-26 | -3611800 | False |
| 2019-10-27 | -3611800 | False |
| 2019-10-28 | -3611800 | False |
| 2019-10-29 | -3611800 | False |
| 2019-10-30 | -3611800 | False |
| 2019-10-31 | -3611800 | False |
| 2019-11-01 | -3611800 | False |
| 2019-11-02 | -3611800 | False |
| 2019-11-03 | -3611800 | False |
| 2019-11-04 | -3611800 | False |
| 2019-11-05 | -3611800 | False |
| 2019-11-06 | -3611800 | False |
| 2019-11-07 | -3611800 | False |
| 2019-11-08 | -3611800 | False |
| 2019-11-09 | -3611800 | False |
| 2019-11-10 | -3611800 | False |
| 2019-11-11 | -3611800 | False |
| 2019-11-12 | -3611800 | False |
| 2019-11-13 | -3611800 | False |
| 2019-11-14 | -3611800 | False |
| 2019-11-15 | -3611800 | False |
| 2019-11-16 | -3611800 | False |
| 2019-11-17 | -3611800 | False |
| 2019-11-18 | -3611800 | False |
| 2019-11-19 | -3611800 | False |
| 2019-11-20 | -3611800 | False |
| 2019-11-21 | -3611800 | False |
| 2019-11-22 | -3611800 | False |
| 2019-11-23 | -3611800 | False |
| 2019-11-24 | -3611800 | False |
| 2019-11-25 | -3611800 | False |
| 2019-11-26 | -3611800 | False |
| 2019-11-27 | -3611800 | False |
| 2019-11-28 | -3611800 | False |
| 2019-11-29 | -3611800 | False |
| 2019-11-30 | -3611800 | False |
| 2019-12-01 | -3611800 | False |

### request_04
Expected `2024-06-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2024-06-04 | 8011000 | False |
| 2024-06-05 | 8011000 | False |
| 2024-06-06 | 8011000 | False |
| 2024-06-07 | 8011000 | False |
| 2024-06-08 | 8011000 | False |
| 2024-06-09 | 8011000 | False |
| 2024-06-10 | 8011000 | False |
| 2024-06-11 | 8011000 | False |
| 2024-06-12 | 8011000 | False |
| 2024-06-13 | 8011000 | False |
| 2024-06-14 | 8011000 | False |
| 2024-06-15 | 8011000 | False |
| 2024-06-16 | 8011000 | False |
| 2024-06-17 | 8011000 | False |
| 2024-06-18 | 8011000 | False |
| 2024-06-19 | 8011000 | False |
| 2024-06-20 | 8011000 | False |
| 2024-06-21 | 8011000 | False |
| 2024-06-22 | 8011000 | False |
| 2024-06-23 | 8011000 | False |
| 2024-06-24 | 8011000 | False |
| 2024-06-25 | 8011000 | False |
| 2024-06-26 | 8011000 | False |
| 2024-06-27 | 8011000 | False |
| 2024-06-28 | 8011000 | False |
| 2024-06-29 | 8011000 | False |
| 2024-06-30 | 8011000 | False |
| 2024-07-01 | 8011000 | False |
| 2024-07-02 | 8011000 | False |
| 2024-07-03 | 8011000 | False |
| 2024-07-04 | 8011000 | False |
| 2024-07-05 | 8011000 | False |
| 2024-07-06 | 8011000 | False |
| 2024-07-07 | 8011000 | False |
| 2024-07-08 | 8011000 | False |
| 2024-07-09 | 8011000 | False |
| 2024-07-10 | 8011000 | False |
| 2024-07-11 | 8011000 | False |
| 2024-07-12 | 8011000 | False |
| 2024-07-13 | 8011000 | False |
| 2024-07-14 | 8011000 | False |
| 2024-07-15 | 8011000 | False |
| 2024-07-16 | 8011000 | False |
| 2024-07-17 | 8011000 | False |
| 2024-07-18 | 8011000 | False |
| 2024-07-19 | 8011000 | False |
| 2024-07-20 | 8011000 | False |
| 2024-07-21 | 8011000 | False |
| 2024-07-22 | 8011000 | False |
| 2024-07-23 | 8011000 | False |
| 2024-07-24 | 8011000 | False |
| 2024-07-25 | 8011000 | False |
| 2024-07-26 | 8011000 | False |
| 2024-07-27 | 8011000 | False |
| 2024-07-28 | 8011000 | False |
| 2024-07-29 | 8011000 | False |
| 2024-07-30 | 8011000 | False |
| 2024-07-31 | 8011000 | False |
| 2024-08-01 | 8011000 | False |
| 2024-08-02 | 8011000 | False |
| 2024-08-03 | 8011000 | False |
| 2024-08-04 | 8011000 | False |
| 2024-08-05 | 8011000 | False |
| 2024-08-06 | 8011000 | False |
| 2024-08-07 | 8011000 | False |
| 2024-08-08 | 8011000 | False |
| 2024-08-09 | 8011000 | False |
| 2024-08-10 | 8011000 | False |
| 2024-08-11 | 8011000 | False |
| 2024-08-12 | 8011000 | False |
| 2024-08-13 | 8011000 | False |
| 2024-08-14 | 8011000 | False |
| 2024-08-15 | 8011000 | False |
| 2024-08-16 | 8011000 | False |
| 2024-08-17 | 8011000 | False |
| 2024-08-18 | 8011000 | False |
| 2024-08-19 | 8011000 | False |
| 2024-08-20 | 8011000 | False |
| 2024-08-21 | 8011000 | False |
| 2024-08-22 | 8011000 | False |
| 2024-08-23 | 8011000 | False |
| 2024-08-24 | 8011000 | False |
| 2024-08-25 | 8011000 | False |
| 2024-08-26 | 8011000 | False |
| 2024-08-27 | 8011000 | False |
| 2024-08-28 | 8011000 | False |
| 2024-08-29 | 8011000 | False |
| 2024-08-30 | 8011000 | False |
| 2024-08-31 | 8011000 | False |
| 2024-09-01 | 8011000 | False |

### request_05
Expected ``; actual `2025-11-06`.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2025-11-06 | 17799.2 | True |
| 2025-11-07 | 17799.2 | True |
| 2025-11-08 | 17799.2 | True |
| 2025-11-09 | 17799.2 | True |
| 2025-11-10 | 17799.2 | True |
| 2025-11-11 | 17799.2 | True |
| 2025-11-12 | 17799.2 | True |
| 2025-11-13 | 17799.2 | True |
| 2025-11-14 | 17799.2 | True |
| 2025-11-15 | 17799.2 | True |
| 2025-11-16 | 17799.2 | True |
| 2025-11-17 | 17799.2 | True |
| 2025-11-18 | 17799.2 | True |
| 2025-11-19 | 17799.2 | True |
| 2025-11-20 | 17799.2 | True |
| 2025-11-21 | 17799.2 | True |
| 2025-11-22 | 17799.2 | True |
| 2025-11-23 | 17799.2 | True |
| 2025-11-24 | 17799.2 | True |
| 2025-11-25 | 17799.2 | True |
| 2025-11-26 | 17799.2 | True |
| 2025-11-27 | 17799.2 | True |
| 2025-11-28 | 17799.2 | True |
| 2025-11-29 | 17799.2 | True |
| 2025-11-30 | 17799.2 | True |
| 2025-12-01 | 17799.2 | True |
| 2025-12-02 | 17799.2 | True |
| 2025-12-03 | 17799.2 | True |
| 2025-12-04 | 17799.2 | True |
| 2025-12-05 | 17799.2 | True |
| 2025-12-06 | 17799.2 | True |
| 2025-12-07 | 17799.2 | True |
| 2025-12-08 | 17799.2 | True |
| 2025-12-09 | 17799.2 | True |
| 2025-12-10 | 17799.2 | True |
| 2025-12-11 | 17799.2 | True |
| 2025-12-12 | 17799.2 | True |
| 2025-12-13 | 17799.2 | True |
| 2025-12-14 | 17799.2 | True |
| 2025-12-15 | 17799.2 | True |
| 2025-12-16 | 17799.2 | True |
| 2025-12-17 | 17799.2 | True |
| 2025-12-18 | 17799.2 | True |
| 2025-12-19 | 17799.2 | True |
| 2025-12-20 | 17799.2 | True |
| 2025-12-21 | 17799.2 | True |
| 2025-12-22 | 17799.2 | True |
| 2025-12-23 | 17799.2 | True |
| 2025-12-24 | 17799.2 | True |
| 2025-12-25 | 17799.2 | True |
| 2025-12-26 | 17799.2 | True |
| 2025-12-27 | 17799.2 | True |
| 2025-12-28 | 17799.2 | True |
| 2025-12-29 | 17799.2 | True |
| 2025-12-30 | 17799.2 | True |
| 2025-12-31 | 17799.2 | True |
| 2026-01-01 | 17799.2 | True |
| 2026-01-02 | 17799.2 | True |
| 2026-01-03 | 17799.2 | True |
| 2026-01-04 | 17799.2 | True |
| 2026-01-05 | 17799.2 | True |
| 2026-01-06 | 17799.2 | True |
| 2026-01-07 | 17799.2 | True |
| 2026-01-08 | 17799.2 | True |
| 2026-01-09 | 17799.2 | True |
| 2026-01-10 | 17799.2 | True |
| 2026-01-11 | 17799.2 | True |
| 2026-01-12 | 17799.2 | True |
| 2026-01-13 | 17799.2 | True |
| 2026-01-14 | 17799.2 | True |
| 2026-01-15 | 17799.2 | True |
| 2026-01-16 | 17799.2 | True |
| 2026-01-17 | 17799.2 | True |
| 2026-01-18 | 17799.2 | True |
| 2026-01-19 | 17799.2 | True |
| 2026-01-20 | 17799.2 | True |
| 2026-01-21 | 17799.2 | True |
| 2026-01-22 | 17799.2 | True |
| 2026-01-23 | 17799.2 | True |
| 2026-01-24 | 17799.2 | True |
| 2026-01-25 | 17799.2 | True |
| 2026-01-26 | 17799.2 | True |
| 2026-01-27 | 17799.2 | True |
| 2026-01-28 | 17799.2 | True |
| 2026-01-29 | 17799.2 | True |
| 2026-01-30 | 17799.2 | True |
| 2026-01-31 | 17799.2 | True |
| 2026-02-01 | 17799.2 | True |
| 2026-02-02 | 17799.2 | True |
| 2026-02-03 | 17799.2 | True |

### request_06
Expected `2026-01-15`; actual ``.

| date | min balance after payment | safe |
|---|---:|:---:|
| 2026-01-03 | 663.8 | False |
| 2026-01-04 | 663.8 | False |
| 2026-01-05 | 663.8 | False |
| 2026-01-06 | 663.8 | False |
| 2026-01-07 | 663.8 | False |
| 2026-01-08 | 663.8 | False |
| 2026-01-09 | 663.8 | False |
| 2026-01-10 | 663.8 | False |
| 2026-01-11 | 663.8 | False |
| 2026-01-12 | 663.8 | False |
| 2026-01-13 | 663.8 | False |
| 2026-01-14 | 663.8 | False |
| 2026-01-15 | 663.8 | False |
| 2026-01-16 | 663.8 | False |
| 2026-01-17 | 663.8 | False |
| 2026-01-18 | 663.8 | False |
| 2026-01-19 | 663.8 | False |
| 2026-01-20 | 663.8 | False |
| 2026-01-21 | 663.8 | False |
| 2026-01-22 | 663.8 | False |
| 2026-01-23 | 663.8 | False |
| 2026-01-24 | 663.8 | False |
| 2026-01-25 | 663.8 | False |
| 2026-01-26 | 663.8 | False |
| 2026-01-27 | 663.8 | False |
| 2026-01-28 | 663.8 | False |
| 2026-01-29 | 663.8 | False |
| 2026-01-30 | 663.8 | False |
| 2026-01-31 | 663.8 | False |
| 2026-02-01 | 663.8 | False |
| 2026-02-02 | 663.8 | False |
| 2026-02-03 | 663.8 | False |
| 2026-02-04 | 663.8 | False |
| 2026-02-05 | 663.8 | False |
| 2026-02-06 | 663.8 | False |
| 2026-02-07 | 663.8 | False |
| 2026-02-08 | 663.8 | False |
| 2026-02-09 | 663.8 | False |
| 2026-02-10 | 663.8 | False |
| 2026-02-11 | 663.8 | False |
| 2026-02-12 | 663.8 | False |
| 2026-02-13 | 663.8 | False |
| 2026-02-14 | 663.8 | False |
| 2026-02-15 | 663.8 | False |
| 2026-02-16 | 663.8 | False |
| 2026-02-17 | 663.8 | False |
| 2026-02-18 | 663.8 | False |
| 2026-02-19 | 663.8 | False |
| 2026-02-20 | 663.8 | False |
| 2026-02-21 | 663.8 | False |
| 2026-02-22 | 663.8 | False |
| 2026-02-23 | 663.8 | False |
| 2026-02-24 | 663.8 | False |
| 2026-02-25 | 663.8 | False |
| 2026-02-26 | 663.8 | False |
| 2026-02-27 | 663.8 | False |
| 2026-02-28 | 663.8 | False |
| 2026-03-01 | 663.8 | False |
| 2026-03-02 | 663.8 | False |
| 2026-03-03 | 663.8 | False |
| 2026-03-04 | 663.8 | False |
| 2026-03-05 | 663.8 | False |
| 2026-03-06 | 663.8 | False |
| 2026-03-07 | 663.8 | False |
| 2026-03-08 | 663.8 | False |
| 2026-03-09 | 663.8 | False |
| 2026-03-10 | 663.8 | False |
| 2026-03-11 | 663.8 | False |
| 2026-03-12 | 663.8 | False |
| 2026-03-13 | 663.8 | False |
| 2026-03-14 | 663.8 | False |
| 2026-03-15 | 663.8 | False |
| 2026-03-16 | 663.8 | False |
| 2026-03-17 | 663.8 | False |
| 2026-03-18 | 663.8 | False |
| 2026-03-19 | 663.8 | False |
| 2026-03-20 | 663.8 | False |
| 2026-03-21 | 663.8 | False |
| 2026-03-22 | 663.8 | False |
| 2026-03-23 | 663.8 | False |
| 2026-03-24 | 663.8 | False |
| 2026-03-25 | 663.8 | False |
| 2026-03-26 | 663.8 | False |
| 2026-03-27 | 663.8 | False |
| 2026-03-28 | 663.8 | False |
| 2026-03-29 | 663.8 | False |
| 2026-03-30 | 663.8 | False |
| 2026-03-31 | 663.8 | False |
| 2026-04-01 | 663.8 | False |
| 2026-04-02 | 663.8 | False |

## Root-cause interpretation

Categories are primary hypotheses from deterministic traces, not expected-answer special cases. No production code or supplied dataset was changed by this report generation.