# Phase 13 Variable Spending Analysis

The frozen solver groups by category, description, direction and currency; it does not collapse category-only observations. It projects only equal-amount fixed series with supported recurrence evidence. Variable series are retained as evidence and receive no mean/median/latest/max/min estimator.

Repeated source-identity series inspected: **6109**.

| user | identity | observations | amounts | classification | gap | amount policy |
|---|---|---:|---|---|---:|---|
|user_01|rent/Apartment rent transfer/debit/ZAR|6|5148, 5148, 5148, 5148, 5148, 5148|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_01|utilities/Household utility payment/debit/ZAR|5|1475.46, 1483.81, 1541.75, 1651.81, 1386.17|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_01|education/Professional training fee/debit/ZAR|5|1821.6, 1821.6, 1821.6, 1821.6, 1821.6|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_01|debt_repayment/Education loan instalment/debit/ZAR|5|3487, 3487, 3487, 3487, 3487|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_01|music_subscription/Music service subscription/debit/ZAR|5|235.4, 235.4, 235.4, 235.4, 235.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_01|delivery_membership/Delivery service plan/debit/ZAR|5|306.9, 306.9, 306.9, 306.9, 306.9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_01|groceries/Neighbourhood grocer/debit/ZAR|5|925.62, 939.13, 672.37, 961.46, 755.11|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_01|groceries/Bulk pantry shop/debit/ZAR|3|707.36, 915.12, 602.87|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_01|groceries/Grocery delivery/debit/ZAR|3|629.96, 1030.1, 626.01|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_01|groceries/Local market purchase/debit/ZAR|5|873.17, 803.55, 644.43, 765.64, 964.05|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_01|groceries/Fresh food shop/debit/ZAR|4|644.3, 663.27, 651.12, 899.04|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_01|groceries/Household groceries/debit/ZAR|3|882.48, 756.39, 719.51|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_01|groceries/Supermarket basket/debit/ZAR|3|875.35, 624.94, 881.22|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_01|transport/Commuter pass/debit/ZAR|5|399.02, 518.04, 374.6, 560.21, 549.05|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_01|transport/Ride-hailing trip/debit/ZAR|5|549.8, 428.92, 444.56, 358.85, 424.56|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_01|transport/Metro and bus fares/debit/ZAR|5|468.47, 373.05, 553.74, 347.86, 406.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_01|transport/Fuel refill/debit/ZAR|2|503.02, 434.69|repeated but not demonstrably recurrent|||
|user_01|transport/Local taxi/debit/ZAR|3|351.49, 411.07, 339.29|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_01|transport/Rail pass/debit/ZAR|2|421.89, 375.73|repeated but not demonstrably recurrent|||
|user_01|transport/Parking and tolls/debit/ZAR|2|323.58, 488.36|repeated but not demonstrably recurrent|||
|user_01|transport/Vehicle charging/debit/ZAR|2|478.16, 534.56|repeated but not demonstrably recurrent|||
|user_01|dining/Bakery and snacks/debit/ZAR|4|1213.78, 1243.56, 1222.49, 1016.12|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_01|dining/Quick-service meal/debit/ZAR|2|1070.17, 1160.42|repeated but not demonstrably recurrent|||
|user_01|dining/Coffee shop/debit/ZAR|2|972.88, 1017.11|repeated but not demonstrably recurrent|||
|user_02|salary/Payroll credit/credit/IDR|5|33345000, 33345000, 33345000, 33345000, 33345000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_02|housing/Home repair reserve/debit/IDR|6|3534000, 3534000, 3534000, 3534000, 3534000, 3534000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_02|utilities/Municipal utilities/debit/IDR|5|2143659.02, 2081730.85, 1830311.06, 1981601.61, 2141849.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_02|insurance/Household insurance/debit/IDR|5|1132400, 1132400, 1132400, 1132400, 1132400|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_02|education/Course tuition/debit/IDR|5|3040000, 3040000, 3040000, 3040000, 3040000|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_02|healthcare/Clinic payment/debit/IDR|5|1594883.08, 1467514.81, 1452405.16, 1641668.72, 1538498.1|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_02|entertainment/Cinema and events/debit/IDR|5|1289187.4, 1367779.89, 1287628.28, 1193699.1, 1352563.79|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_02|cloud_storage/Shared storage plan/debit/IDR|5|369550, 369550, 369550, 369550, 369550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_02|groceries/Grocery delivery/debit/IDR|2|2477697.53, 2222527.88|repeated but not demonstrably recurrent|||
|user_02|groceries/Bulk pantry shop/debit/IDR|2|1667911.86, 1664708.05|repeated but not demonstrably recurrent|||
|user_02|groceries/Neighbourhood grocer/debit/IDR|3|1455258.76, 2030400.43, 2158165.32|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_02|groceries/Household groceries/debit/IDR|4|1920485.7, 1630631.42, 1478895.05, 2079368.25|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_02|groceries/Local market purchase/debit/IDR|3|2192475.45, 1611886.08, 2218141.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_02|groceries/Supermarket basket/debit/IDR|2|1852958.27, 1913686.86|repeated but not demonstrably recurrent|||
|user_02|transport/Rail pass/debit/IDR|2|995704.83, 1111352.32|repeated but not demonstrably recurrent|||
|user_02|transport/Metro and bus fares/debit/IDR|2|1062246.98, 1062310.27|repeated but not demonstrably recurrent|||
|user_02|transport/Ride-hailing trip/debit/IDR|3|1053078.61, 1294200.86, 1440242.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_02|transport/Commuter pass/debit/IDR|4|1374936.26, 1329347.44, 1309608.46, 1327886.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_02|dining/Bakery and snacks/debit/IDR|3|1166644.88, 947892.35, 1204805.34|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_03|salary/Payroll credit/credit/IDR|5|4365000, 4365000, 4365000, 4365000, 4365000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_03|rent/Landlord standing order/debit/IDR|5|1140000, 1140000, 1140000, 1140000, 1140000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_03|utilities/Water and power payment/debit/IDR|5|295330.29, 290684.15, 270537.63, 303042.45, 262344.55|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_03|cloud_storage/Shared storage plan/debit/IDR|5|20900, 20900, 20900, 20900, 20900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_03|streaming/Video streaming plan/debit/IDR|5|117800, 117800, 117800, 117800, 117800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_03|shopping/Clothing and household items/debit/IDR|5|151493.37, 184274.02, 153395.26, 173930.81, 180395.29|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_03|groceries/Bulk pantry shop/debit/IDR|3|159576.52, 234390.87, 230312.98|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_03|groceries/Supermarket basket/debit/IDR|4|234602.65, 145691.38, 171259.18, 214266.98|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_03|groceries/Neighbourhood grocer/debit/IDR|2|209875.85, 200238.72|repeated but not demonstrably recurrent|||
|user_03|groceries/Weekly produce market/debit/IDR|3|178469.49, 180577.99, 221578.88|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_03|groceries/Household groceries/debit/IDR|2|155851.46, 166710.61|repeated but not demonstrably recurrent|||
|user_03|groceries/Grocery delivery/debit/IDR|2|188355.72, 171495.67|repeated but not demonstrably recurrent|||
|user_03|groceries/Local market purchase/debit/IDR|2|173004.74, 240706.45|repeated but not demonstrably recurrent|||
|user_03|transport/Parking and tolls/debit/IDR|3|81510.25, 116319.21, 106806.88|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_03|transport/Metro and bus fares/debit/IDR|2|83523.33, 99961.13|repeated but not demonstrably recurrent|||
|user_03|dining/Bakery and snacks/debit/IDR|2|117456.78, 141412.46|repeated but not demonstrably recurrent|||
|user_03|dining/Quick-service meal/debit/IDR|2|146236.28, 171303.21|repeated but not demonstrably recurrent|||
|user_03|dining/Coffee shop/debit/IDR|2|132247.64, 135718.35|repeated but not demonstrably recurrent|||
|user_03|dining/Lunch with colleagues/debit/IDR|2|158476.5, 171191.99|repeated but not demonstrably recurrent|||
|user_04|salary/Payroll credit/credit/IDR|5|38190000, 38190000, 38190000, 38190000, 38190000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_04|rent/Residential rent payment/debit/IDR|6|12293000, 12293000, 12293000, 12293000, 12293000, 12293000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_04|utilities/Municipal utilities/debit/IDR|5|2017103.37, 1981052.47, 2033868.83, 1980834.82, 2004118.6|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_04|music_subscription/Music service subscription/debit/IDR|5|332500, 332500, 332500, 332500, 332500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_04|delivery_membership/Food delivery membership/debit/IDR|5|377150, 377150, 377150, 377150, 377150|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_04|gym/Gym membership/debit/IDR|5|1027900, 1027900, 1027900, 1027900, 1027900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_04|entertainment/Local event tickets/debit/IDR|5|1484369.68, 1375854.05, 1542620, 1291303.65, 1231859.39|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_04|groceries/Local market purchase/debit/IDR|6|1685953.79, 1413898.4, 1753801.95, 1203621.92, 1347842.61, 1809752.54|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_04|groceries/Fresh food shop/debit/IDR|3|1749986.6, 1184189.4, 1698278.31|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_04|groceries/Bulk pantry shop/debit/IDR|3|1383275.31, 1617937.79, 1433695.5|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_04|groceries/Neighbourhood grocer/debit/IDR|5|1482897.31, 1697006.55, 1674003.66, 1519414.73, 1831437.58|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_04|groceries/Weekly produce market/debit/IDR|3|1818044.76, 1178544.55, 1087788.82|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_04|groceries/Supermarket basket/debit/IDR|2|1453711.32, 1447770.09|repeated but not demonstrably recurrent|||
|user_04|groceries/Grocery delivery/debit/IDR|3|1261462.72, 1825667.28, 1075064.04|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_04|transport/Fuel refill/debit/IDR|5|649231.24, 820888.17, 870102.58, 954666.65, 843406.32|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_04|transport/Local taxi/debit/IDR|3|876705.51, 825832.49, 842011.07|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_04|transport/Ride-hailing trip/debit/IDR|6|769694.2, 589707.32, 766019.04, 1030376.9, 912938.95, 853091.62|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_04|transport/Parking and tolls/debit/IDR|5|841811.01, 596927.82, 889762.96, 874634.88, 602450.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_04|transport/Metro and bus fares/debit/IDR|3|1011616.29, 595968.94, 677221.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_04|transport/Vehicle charging/debit/IDR|2|997182.25, 935850.82|repeated but not demonstrably recurrent|||
|user_04|transport/Rail pass/debit/IDR|2|1000668.29, 1016425.58|repeated but not demonstrably recurrent|||
|user_04|dining/Neighbourhood restaurant/debit/IDR|3|2111827.25, 1839656.04, 1282286.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_04|dining/Takeaway order/debit/IDR|2|1279029.86, 2067659.14|repeated but not demonstrably recurrent|||
|user_04|dining/Family dinner/debit/IDR|3|1931412.81, 2102251.18, 1661337.11|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_04|dining/Bakery and snacks/debit/IDR|2|1259307.64, 1886856.1|repeated but not demonstrably recurrent|||
|user_05|salary/Payroll credit/credit/ZAR|4|14740, 14740, 14740, 14740|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_05|rent/Apartment rent transfer/debit/ZAR|6|4972, 4972, 4972, 4972, 4972, 4972|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_05|utilities/Municipal utilities/debit/ZAR|5|604.15, 658.41, 750.89, 706.37, 713.71|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_05|debt_repayment/Vehicle loan payment/debit/ZAR|5|968, 968, 968, 968, 968|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_05|healthcare/Therapy appointment/debit/ZAR|5|777.27, 641.37, 632.59, 721.44, 722.37|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_05|family_support/Dependent care payment/debit/ZAR|5|840.4, 840.4, 840.4, 840.4, 840.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_05|cloud_storage/Cloud storage plan/debit/ZAR|5|113.3, 113.3, 113.3, 113.3, 113.3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_05|shopping/Personal shopping/debit/ZAR|5|379.94, 404.24, 422.67, 420.31, 362.09|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Supermarket basket/debit/ZAR|3|784.81, 661.93, 684.39|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Household groceries/debit/ZAR|4|818.16, 800.63, 845.02, 826.66|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Local market purchase/debit/ZAR|4|680.15, 530.44, 682.39, 547.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Weekly produce market/debit/ZAR|3|695.96, 813.64, 853.42|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Grocery delivery/debit/ZAR|4|835, 635.23, 515.4, 768.64|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Bulk pantry shop/debit/ZAR|2|567.19, 675.81|repeated but not demonstrably recurrent|||
|user_05|groceries/Neighbourhood grocer/debit/ZAR|3|767.92, 773.83, 709.62|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_05|groceries/Fresh food shop/debit/ZAR|3|807.31, 762.65, 720.51|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_05|transport/Parking and tolls/debit/ZAR|2|489.31, 354.2|repeated but not demonstrably recurrent|||
|user_05|transport/Fuel refill/debit/ZAR|2|424.26, 431.81|repeated but not demonstrably recurrent|||
|user_05|transport/Metro and bus fares/debit/ZAR|3|492.86, 311, 352.46|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_05|transport/Ride-hailing trip/debit/ZAR|3|363.28, 485.59, 377.26|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_06|salary/Payroll credit/credit/EUR|5|1441, 1441, 1441, 1037.52, 1037.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|rent/Monthly rent/debit/EUR|5|254.1, 254.1, 254.1, 254.1, 254.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_06|utilities/Water and power payment/debit/EUR|5|58.34, 52.62, 58.98, 56.71, 51.86|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|insurance/Vehicle insurance premium/debit/EUR|5|26, 26, 26, 26, 26|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_06|cloud_storage/Shared storage plan/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_06|streaming/Family streaming plan/debit/EUR|5|19, 19, 19, 19, 19|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_06|shopping/Household shopping/debit/EUR|5|41.44, 46.25, 39.46, 37.96, 39.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|entertainment/Monthly entertainment spend/debit/EUR|5|32.1, 35.1, 32.18, 37.36, 38.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|groceries/Bulk pantry shop/debit/EUR|2|43.16, 32.69|repeated but not demonstrably recurrent|||
|user_06|groceries/Neighbourhood grocer/debit/EUR|4|53.56, 45.4, 40.91, 52.76|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_06|groceries/Household groceries/debit/EUR|2|49.49, 51.97|repeated but not demonstrably recurrent|||
|user_06|groceries/Grocery delivery/debit/EUR|2|31.69, 48.32|repeated but not demonstrably recurrent|||
|user_06|groceries/Local market purchase/debit/EUR|3|50.53, 51.4, 51.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|groceries/Fresh food shop/debit/EUR|3|51.55, 46.22, 32.96|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Parking and tolls/debit/EUR|8|23.68, 31.89, 21.32, 28.08, 21.1, 28.65, 32.36, 32.9|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Ride-hailing trip/debit/EUR|3|23.83, 24.5, 24.92|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Commuter pass/debit/EUR|4|24.21, 19.73, 27.29, 28.87|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Vehicle charging/debit/EUR|3|32.17, 22.14, 27.97|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Rail pass/debit/EUR|5|27.8, 29.46, 23.31, 29.32, 21.46|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Local taxi/debit/EUR|5|28.03, 29.47, 30.82, 27.59, 19.18|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Metro and bus fares/debit/EUR|5|26.82, 27.65, 28.61, 31.69, 25.9|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_06|transport/Fuel refill/debit/EUR|2|31.87, 29.57|repeated but not demonstrably recurrent|||
|user_06|dining/Lunch with colleagues/debit/EUR|4|53.26, 56.6, 47.33, 54.09|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_06|dining/Takeaway order/debit/EUR|2|50.79, 34.99|repeated but not demonstrably recurrent|||
|user_06|dining/Weekend food delivery/debit/EUR|5|42.1, 46.84, 53.71, 36, 48.36|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_06|dining/Neighbourhood restaurant/debit/EUR|6|48.98, 38.44, 43.95, 48.14, 37.02, 57.57|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_06|dining/Family dinner/debit/EUR|3|37.25, 45.39, 57.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_06|dining/Bakery and snacks/debit/EUR|3|40.23, 43.17, 55.16|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_07|salary/Payroll credit/credit/INR|5|149000, 149000, 149000, 149000, 149000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_07|rent/Monthly rent/debit/INR|6|34200, 34200, 34200, 34200, 34200, 34200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_07|utilities/Electricity bill/debit/INR|5|7219.31, 7049.68, 7387.41, 6081.25, 6209.57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_07|debt_repayment/Personal loan payment/debit/INR|5|15650, 15650, 15650, 15650, 15650|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_07|music_subscription/Music subscription/debit/INR|5|1005, 1005, 1005, 1005, 1005|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_07|groceries/Weekly produce market/debit/INR|2|8380.73, 6433.29|repeated but not demonstrably recurrent|||
|user_07|groceries/Household groceries/debit/INR|4|6022.17, 7968.39, 7913.81, 5710.65|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_07|groceries/Supermarket basket/debit/INR|2|8280.58, 6889.87|repeated but not demonstrably recurrent|||
|user_07|transport/Metro and bus fares/debit/INR|2|3690.82, 3104.36|repeated but not demonstrably recurrent|||
|user_07|transport/Commuter pass/debit/INR|2|3465.99, 3145.62|repeated but not demonstrably recurrent|||
|user_07|transport/Rail pass/debit/INR|3|3822.62, 2751.86, 3773.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_07|dining/Family dinner/debit/INR|3|6371.55, 5802.49, 4541.62|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_07|dining/Bakery and snacks/debit/INR|2|6313.91, 6493.86|repeated but not demonstrably recurrent|||
|user_08|salary/Payroll credit/credit/EUR|5|1422.85, 1422.85, 1422.85, 1422.85, 782.57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_08|rent/Apartment rent transfer/debit/EUR|6|467.5, 467.5, 467.5, 467.5, 467.5, 467.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_08|utilities/Municipal utilities/debit/EUR|6|79.19, 80.9, 68.44, 82.61, 69.28, 80.55|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_08|education/School fee payment/debit/EUR|5|89, 89, 89, 89, 89|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_08|debt_repayment/Personal loan payment/debit/EUR|5|177, 177, 177, 177, 177|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_08|music_subscription/Music subscription/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_08|delivery_membership/Grocery delivery membership/debit/EUR|5|24, 24, 24, 24, 24|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_08|groceries/Fresh food shop/debit/EUR|4|78.42, 54.35, 74.35, 68.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_08|groceries/Weekly produce market/debit/EUR|3|51.01, 53.11, 72.38|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_08|groceries/Bulk pantry shop/debit/EUR|5|52.28, 48.16, 47.78, 69.32, 48|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_08|groceries/Supermarket basket/debit/EUR|7|68, 57.01, 51, 56.62, 55.02, 45.99, 65.92|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_08|groceries/Grocery delivery/debit/EUR|5|51.6, 76.07, 60.11, 51.85, 53.96|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_08|transport/Ride-hailing trip/debit/EUR|3|34.09, 45.56, 29.03|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_08|transport/Metro and bus fares/debit/EUR|5|36.65, 39.38, 37, 40.22, 32.95|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_08|transport/Vehicle charging/debit/EUR|2|41.53, 41.57|repeated but not demonstrably recurrent|||
|user_08|transport/Parking and tolls/debit/EUR|6|40.21, 30.47, 36.94, 46.08, 35.98, 43.2|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_08|transport/Fuel refill/debit/EUR|3|37.62, 26.69, 47.21|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_08|transport/Local taxi/debit/EUR|4|43.53, 38.07, 43.51, 31.5|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_08|transport/Commuter pass/debit/EUR|3|35.69, 31.67, 28.33|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_08|dining/Weekend food delivery/debit/EUR|4|51.75, 58.15, 49.45, 53.65|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_08|dining/Family dinner/debit/EUR|2|59.94, 60.66|repeated but not demonstrably recurrent|||
|user_08|dining/Neighbourhood restaurant/debit/EUR|2|46.25, 48.98|repeated but not demonstrably recurrent|||
|user_08|dining/Bakery and snacks/debit/EUR|2|41.5, 42.33|repeated but not demonstrably recurrent|||
|user_09|salary/Freelance milestone payment/credit/EUR|2|488.8, 506.35|repeated but not demonstrably recurrent|||
|user_09|rent/Monthly rent/debit/EUR|6|211.2, 211.2, 211.2, 211.2, 211.2, 211.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_09|utilities/Water and power payment/debit/EUR|5|66.84, 59.39, 71.04, 63.66, 60.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_09|cloud_storage/Cloud storage plan/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_09|streaming/Video streaming plan/debit/EUR|5|20, 20, 20, 20, 20|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_09|shopping/Household shopping/debit/EUR|5|25.5, 29.14, 28.32, 24.68, 25.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_09|salary/Application project payment/credit/EUR|2|355.99, 441.96|repeated but not demonstrably recurrent|||
|user_09|groceries/Household groceries/debit/EUR|2|47.44, 36.79|repeated but not demonstrably recurrent|||
|user_09|groceries/Fresh food shop/debit/EUR|4|38.34, 41.29, 53.82, 34.74|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_09|groceries/Grocery delivery/debit/EUR|4|47.6, 48.93, 51.03, 43|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_09|groceries/Local market purchase/debit/EUR|2|54.9, 53.14|repeated but not demonstrably recurrent|||
|user_09|groceries/Bulk pantry shop/debit/EUR|3|37.29, 46.49, 51.3|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_09|groceries/Weekly produce market/debit/EUR|2|31.82, 34.17|repeated but not demonstrably recurrent|||
|user_09|transport/Local taxi/debit/EUR|3|18.44, 27.94, 26.23|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_09|transport/Rail pass/debit/EUR|2|23.57, 27.2|repeated but not demonstrably recurrent|||
|user_09|transport/Commuter pass/debit/EUR|2|28.34, 24.13|repeated but not demonstrably recurrent|||
|user_09|dining/Family dinner/debit/EUR|2|34.84, 35.49|repeated but not demonstrably recurrent|||
|user_09|dining/Takeaway order/debit/EUR|2|29.97, 27.38|repeated but not demonstrably recurrent|||
|user_09|dining/Quick-service meal/debit/EUR|2|23.42, 28.41|repeated but not demonstrably recurrent|||
|user_10|salary/Delivery platform payout/credit/INR|9|74420.35, 54774.8, 72641.37, 59553.07, 79168.24, 69351.86, 78226.16, 40977.52, 82667.27|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|salary/Weekly app earnings/credit/INR|4|74852.29, 82410.47, 67741.04, 65488.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_10|rent/Monthly rent/debit/INR|6|69100, 69100, 69100, 69100, 69100, 69100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_10|utilities/Electricity and water bill/debit/INR|5|19224.83, 17538.11, 15748.74, 15236.94, 17771.13|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_10|music_subscription/Music subscription/debit/INR|5|2800, 2800, 2800, 2800, 2800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_10|delivery_membership/Delivery service plan/debit/INR|5|1895, 1895, 1895, 1895, 1895|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_10|gym/Community fitness plan/debit/INR|5|4860, 4860, 4860, 4860, 4860|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_10|entertainment/Cinema and events/debit/INR|5|4770.41, 4504.6, 4700.56, 4366.61, 4883.78|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_10|salary/Task marketplace payout/credit/INR|4|65056.43, 47245.98, 81755.75, 44415.5|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_10|salary/Driver platform payout/credit/INR|4|60517.87, 60877.41, 47802.51, 52239.8|variable but recurrent|16|RECURRING_AMOUNT_UNRESOLVED|
|user_10|groceries/Fresh food shop/debit/INR|7|10089.49, 9512.16, 10839.89, 12767.81, 9968.28, 12092.24, 8755.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|groceries/Grocery delivery/debit/INR|6|12216.63, 10431.63, 12027.49, 12641.36, 9807.08, 13621.53|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|groceries/Household groceries/debit/INR|2|12020.19, 9929.21|repeated but not demonstrably recurrent|||
|user_10|groceries/Weekly produce market/debit/INR|3|11986, 8157.98, 8011.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|groceries/Bulk pantry shop/debit/INR|3|11074.05, 8855.55, 8809.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|groceries/Local market purchase/debit/INR|4|10087.39, 11596.13, 12589.2, 10392.47|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_10|transport/Metro and bus fares/debit/INR|5|6859.81, 7100.47, 4956.67, 5753.54, 4990.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|transport/Local taxi/debit/INR|6|4830.13, 7530.3, 6632.3, 5018.36, 6582.39, 4472.6|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_10|transport/Commuter pass/debit/INR|2|5489.62, 7448.62|repeated but not demonstrably recurrent|||
|user_10|transport/Parking and tolls/debit/INR|3|7568.88, 5747.77, 6785.52|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_10|transport/Vehicle charging/debit/INR|2|6683.23, 4356.14|repeated but not demonstrably recurrent|||
|user_10|transport/Rail pass/debit/INR|2|5641.87, 5350.7|repeated but not demonstrably recurrent|||
|user_10|transport/Ride-hailing trip/debit/INR|3|4570.28, 5776.08, 6359.49|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_10|transport/Fuel refill/debit/INR|2|6245.32, 6819.66|repeated but not demonstrably recurrent|||
|user_10|dining/Takeaway order/debit/INR|7|9260.11, 6897.95, 9621.2, 6375.03, 8480.31, 8253.71, 10370.83|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_10|dining/Lunch with colleagues/debit/INR|3|9399.4, 10079.99, 10525.43|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_11|salary/Base salary/credit/IDR|5|23256000, 23256000, 23256000, 23256000, 23256000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_11|salary/Performance commission/credit/IDR|3|16715584.16, 8908379.93, 15989420|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_11|housing/Home association fee/debit/IDR|5|2954500, 2954500, 2954500, 2954500, 2954500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_11|utilities/Municipal utilities/debit/IDR|5|2916312.61, 2891149.67, 2508782.45, 2488665.63, 2796165.18|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_11|insurance/Vehicle insurance premium/debit/IDR|5|1881000, 1881000, 1881000, 1881000, 1881000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_11|education/Child education fee/debit/IDR|5|2544100, 2544100, 2544100, 2544100, 2544100|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_11|healthcare/Regular medicine purchase/debit/IDR|5|2635764.61, 3118089.32, 2973572.96, 3165638.3, 2826901.92|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_11|entertainment/Games and recreation/debit/IDR|5|1404572.9, 1688239.04, 1587027.72, 1649906.5, 1674887.61|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_11|cloud_storage/Cloud storage plan/debit/IDR|5|168150, 168150, 168150, 168150, 168150|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_11|salary/Monthly sales commission/credit/IDR|2|20012106.46, 8502888.2|repeated but not demonstrably recurrent|||
|user_11|groceries/Neighbourhood grocer/debit/IDR|4|1053064.17, 1565130.98, 1763208.29, 1311350.07|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_11|groceries/Supermarket basket/debit/IDR|2|1714643.08, 1644304.53|repeated but not demonstrably recurrent|||
|user_11|groceries/Bulk pantry shop/debit/IDR|3|1406401.86, 1655671.41, 1590529.64|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_11|groceries/Household groceries/debit/IDR|2|1063530.58, 1222447.75|repeated but not demonstrably recurrent|||
|user_11|groceries/Fresh food shop/debit/IDR|3|1578114.18, 1614291.7, 1341187.18|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_11|groceries/Grocery delivery/debit/IDR|2|1241008.74, 1131582.3|repeated but not demonstrably recurrent|||
|user_11|transport/Rail pass/debit/IDR|2|1230316.5, 1200020.76|repeated but not demonstrably recurrent|||
|user_11|transport/Ride-hailing trip/debit/IDR|3|825660.54, 1185524.72, 1122838.73|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_11|transport/Metro and bus fares/debit/IDR|2|788053.2, 1212904.33|repeated but not demonstrably recurrent|||
|user_11|transport/Local taxi/debit/IDR|4|893623.46, 1307205.52, 785218.72, 1103949.29|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_11|transport/Vehicle charging/debit/IDR|2|1244032.33, 1244835.69|repeated but not demonstrably recurrent|||
|user_11|dining/Bakery and snacks/debit/IDR|2|1018758.07, 1365643.7|repeated but not demonstrably recurrent|||
|user_11|dining/Neighbourhood restaurant/debit/IDR|2|1485097.86, 1052748.56|repeated but not demonstrably recurrent|||
|user_11|dining/Weekend food delivery/debit/IDR|2|1528058.96, 1163530.49|repeated but not demonstrably recurrent|||
|user_12|salary/Seasonal contract payment/credit/ZAR|2|55846.64, 41904.42|repeated but not demonstrably recurrent|||
|user_12|rent/Monthly rent/debit/ZAR|6|11792, 11792, 11792, 11792, 11792, 11792|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_12|utilities/Water and power payment/debit/ZAR|5|3103.78, 3374.49, 3755.96, 3708.19, 3606.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_12|cloud_storage/Shared storage plan/debit/ZAR|5|447.7, 447.7, 447.7, 447.7, 447.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_12|streaming/Family streaming plan/debit/ZAR|5|1504.8, 1504.8, 1504.8, 1504.8, 1504.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_12|shopping/Monthly shopping spend/debit/ZAR|5|1267.67, 1243.49, 1401.99, 1196.86, 1169.42|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_12|groceries/Grocery delivery/debit/ZAR|2|2484.14, 2404.94|repeated but not demonstrably recurrent|||
|user_12|groceries/Weekly produce market/debit/ZAR|2|2333.56, 1622.75|repeated but not demonstrably recurrent|||
|user_12|groceries/Supermarket basket/debit/ZAR|6|2229.55, 1797.17, 2448, 2432.91, 1930.95, 1539.11|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_12|groceries/Household groceries/debit/ZAR|2|2333.98, 2469.4|repeated but not demonstrably recurrent|||
|user_12|groceries/Bulk pantry shop/debit/ZAR|3|2177.71, 1587.87, 1806.77|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_12|transport/Rail pass/debit/ZAR|2|1398.61, 1302.02|repeated but not demonstrably recurrent|||
|user_12|transport/Vehicle charging/debit/ZAR|3|1282.01, 1722.14, 1355.85|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_12|transport/Parking and tolls/debit/ZAR|2|1240.84, 1679.15|repeated but not demonstrably recurrent|||
|user_12|dining/Takeaway order/debit/ZAR|3|2452.07, 2344.45, 2608.96|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_12|dining/Lunch with colleagues/debit/ZAR|2|2407.92, 1765.33|repeated but not demonstrably recurrent|||
|user_12|dining/Coffee shop/debit/ZAR|2|2089.92, 1943.35|repeated but not demonstrably recurrent|||
|user_13|salary/Primary household salary/credit/EUR|5|1343.54, 1343.54, 1343.54, 1343.54, 1343.54|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_13|salary/Second household income/credit/EUR|4|993.88, 771.17, 948.46, 881.45|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_13|rent/Shared housing rent/debit/EUR|6|622.6, 622.6, 622.6, 622.6, 622.6, 622.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_13|utilities/Water and power payment/debit/EUR|6|162.77, 143.39, 146.33, 143.7, 131.53, 134.25|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_13|music_subscription/Music subscription/debit/EUR|5|29, 29, 29, 29, 29|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_13|delivery_membership/Delivery service plan/debit/EUR|5|21, 21, 21, 21, 21|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_13|gym/Community fitness plan/debit/EUR|5|61, 61, 61, 61, 61|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_13|entertainment/Local event tickets/debit/EUR|5|33.83, 30.88, 37.9, 31.8, 30.39|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_13|groceries/Neighbourhood grocer/debit/EUR|3|91.05, 119.05, 106.05|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_13|groceries/Fresh food shop/debit/EUR|2|114.9, 82.38|repeated but not demonstrably recurrent|||
|user_13|groceries/Weekly produce market/debit/EUR|5|120.16, 89.89, 108.75, 81.24, 98.36|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_13|groceries/Local market purchase/debit/EUR|5|115.37, 102.05, 102.25, 93.15, 84.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_13|groceries/Grocery delivery/debit/EUR|5|91.28, 101.74, 114.53, 118.36, 85.71|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_13|groceries/Supermarket basket/debit/EUR|3|101.87, 86.23, 94.28|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_13|groceries/Bulk pantry shop/debit/EUR|3|120.89, 73.74, 93.66|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_13|transport/Commuter pass/debit/EUR|5|44.85, 48.13, 54.4, 38.31, 43.41|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_13|transport/Metro and bus fares/debit/EUR|4|35.12, 34.47, 46.73, 39.48|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_13|transport/Local taxi/debit/EUR|4|34.28, 54.58, 33.97, 46.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_13|transport/Rail pass/debit/EUR|3|50.6, 56.63, 45.29|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_13|transport/Parking and tolls/debit/EUR|2|55.33, 58.44|repeated but not demonstrably recurrent|||
|user_13|transport/Vehicle charging/debit/EUR|2|34.09, 37.29|repeated but not demonstrably recurrent|||
|user_13|transport/Fuel refill/debit/EUR|3|44.07, 50.38, 45.37|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_13|transport/Ride-hailing trip/debit/EUR|3|49.29, 33.5, 50.46|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_13|dining/Quick-service meal/debit/EUR|2|75.47, 80.35|repeated but not demonstrably recurrent|||
|user_13|dining/Takeaway order/debit/EUR|2|68.7, 53.91|repeated but not demonstrably recurrent|||
|user_13|dining/Weekend food delivery/debit/EUR|3|64.45, 48.02, 61.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_13|dining/Family dinner/debit/EUR|2|48.2, 60.34|repeated but not demonstrably recurrent|||
|user_14|salary/Payroll before leave/credit/EUR|2|2717, 2717|repeated but not demonstrably recurrent|||
|user_14|rent/Monthly rent/debit/EUR|6|688.6, 688.6, 688.6, 688.6, 688.6, 688.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_14|utilities/Energy provider bill/debit/EUR|5|141.46, 156.08, 143.45, 146.41, 153.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_14|debt_repayment/Credit card repayment/debit/EUR|5|350, 350, 350, 350, 350|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_14|healthcare/Family healthcare expense/debit/EUR|5|92.08, 92.65, 95.17, 91.77, 87.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_14|family_support/Family support payment/debit/EUR|5|226, 226, 226, 226, 226|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_14|cloud_storage/Cloud storage plan/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_14|shopping/Online retail purchases/debit/EUR|5|137.03, 123.04, 123.12, 123.77, 140.39|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Weekly produce market/debit/EUR|4|103.53, 138.85, 112.72, 86.83|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Local market purchase/debit/EUR|4|95.35, 83.71, 102.54, 96.86|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Grocery delivery/debit/EUR|5|104.91, 92.09, 93.46, 90.76, 123.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Fresh food shop/debit/EUR|3|81.22, 131.02, 129.68|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Household groceries/debit/EUR|2|121.61, 140.51|repeated but not demonstrably recurrent|||
|user_14|groceries/Bulk pantry shop/debit/EUR|3|87.64, 94.21, 129.56|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Supermarket basket/debit/EUR|3|106.55, 96.42, 101.15|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_14|groceries/Neighbourhood grocer/debit/EUR|2|93.65, 86.49|repeated but not demonstrably recurrent|||
|user_14|transport/Vehicle charging/debit/EUR|2|46.75, 58.52|repeated but not demonstrably recurrent|||
|user_14|transport/Parking and tolls/debit/EUR|2|37.65, 50.48|repeated but not demonstrably recurrent|||
|user_14|transport/Fuel refill/debit/EUR|2|56.49, 55.52|repeated but not demonstrably recurrent|||
|user_14|transport/Ride-hailing trip/debit/EUR|2|52.26, 43.88|repeated but not demonstrably recurrent|||
|user_14|transport/Rail pass/debit/EUR|2|62.3, 43.12|repeated but not demonstrably recurrent|||
|user_15|rent/Landlord standing order/debit/EUR|6|435.6, 435.6, 435.6, 435.6, 435.6, 435.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_15|utilities/Energy provider bill/debit/EUR|5|84.12, 85.91, 90.39, 87.14, 84.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_15|education/School fee payment/debit/EUR|5|159, 159, 159, 159, 159|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_15|debt_repayment/Credit card repayment/debit/EUR|5|84, 84, 84, 84, 84|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_15|music_subscription/Music subscription/debit/EUR|5|11, 11, 11, 11, 11|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_15|delivery_membership/Food delivery membership/debit/EUR|5|27, 27, 27, 27, 27|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_15|salary/First-job payroll/credit/EUR|2|1661, 1661|repeated but not demonstrably recurrent|||
|user_15|groceries/Household groceries/debit/EUR|2|51.57, 64.39|repeated but not demonstrably recurrent|||
|user_15|groceries/Bulk pantry shop/debit/EUR|5|63.15, 46.76, 73.5, 71.16, 64.22|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_15|groceries/Grocery delivery/debit/EUR|6|55.63, 68.03, 72.3, 56.7, 52.69, 49.9|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_15|groceries/Supermarket basket/debit/EUR|2|71.92, 48.88|repeated but not demonstrably recurrent|||
|user_15|groceries/Fresh food shop/debit/EUR|4|49.38, 59.88, 62.21, 64.51|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_15|groceries/Local market purchase/debit/EUR|3|69.83, 52.65, 64.42|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_15|groceries/Neighbourhood grocer/debit/EUR|2|53.42, 47.26|repeated but not demonstrably recurrent|||
|user_15|transport/Fuel refill/debit/EUR|3|29.41, 25.57, 34.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_15|transport/Metro and bus fares/debit/EUR|6|39.06, 26.5, 37.01, 29.73, 29.3, 36.86|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_15|transport/Vehicle charging/debit/EUR|2|42.66, 31.28|repeated but not demonstrably recurrent|||
|user_15|transport/Commuter pass/debit/EUR|4|29.38, 35.61, 32.48, 38.53|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_15|transport/Rail pass/debit/EUR|4|26.48, 25.35, 25.63, 27.67|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_15|transport/Local taxi/debit/EUR|2|26, 31.09|repeated but not demonstrably recurrent|||
|user_15|transport/Ride-hailing trip/debit/EUR|3|36.7, 41.35, 30.31|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_15|dining/Weekend food delivery/debit/EUR|3|33.39, 53.58, 32.62|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_15|dining/Takeaway order/debit/EUR|3|41.42, 36.23, 34.51|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_15|dining/Neighbourhood restaurant/debit/EUR|2|32.17, 38.56|repeated but not demonstrably recurrent|||
|user_15|dining/Bakery and snacks/debit/EUR|2|51.08, 49.35|repeated but not demonstrably recurrent|||
|user_16|salary/Payroll credit/credit/INR|5|173000, 173000, 173000, 173000, 173000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_16|rent/Monthly rent/debit/INR|6|57100, 57100, 57100, 57100, 57100, 57100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_16|utilities/Energy provider bill/debit/INR|6|11173.73, 9756.03, 10586.37, 9402.67, 10012.92, 11512.87|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_16|debt_repayment/Vehicle loan payment/debit/INR|6|17750, 17750, 17750, 17750, 17750, 17750|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_16|streaming/Video streaming plan/debit/INR|6|3510, 3510, 3510, 3510, 3510, 3510|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_16|cloud_storage/Cloud storage plan/debit/INR|6|1055, 1055, 1055, 1055, 1055, 1055|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_16|shopping/Clothing and household items/debit/INR|6|9307.32, 8486.21, 8885, 8414.47, 9807.5, 10178.56|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_16|groceries/Weekly produce market/debit/INR|4|6134.32, 5364.38, 6302.62, 6716.29|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_16|groceries/Fresh food shop/debit/INR|5|8882.85, 5434.36, 8225.29, 8445.69, 7181.79|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_16|groceries/Neighbourhood grocer/debit/INR|7|9038.15, 8137.99, 9111.36, 7101.43, 8883.15, 6568.76, 7930.19|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_16|groceries/Bulk pantry shop/debit/INR|3|5583.98, 6091.85, 5623.39|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_16|groceries/Grocery delivery/debit/INR|4|5463.03, 8465.36, 5495.8, 6971.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Rail pass/debit/INR|6|4382.18, 3653.49, 5016.88, 4523.27, 5087.33, 5368.95|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Ride-hailing trip/debit/INR|3|3464.26, 3688.64, 3888.24|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Local taxi/debit/INR|5|4483.65, 5284.1, 5067.66, 3885.07, 4643.67|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Parking and tolls/debit/INR|4|4106.4, 3143.71, 5251.4, 4978.93|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Vehicle charging/debit/INR|3|5267.76, 3624.64, 4368.27|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Metro and bus fares/debit/INR|3|3170.83, 4284.41, 4175.44|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_16|transport/Commuter pass/debit/INR|2|5236.08, 4859.49|repeated but not demonstrably recurrent|||
|user_16|dining/Coffee shop/debit/INR|3|5271.93, 5981.93, 5210.3|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_16|dining/Weekend food delivery/debit/INR|4|4791.94, 5478.94, 5461.61, 3835.73|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_16|dining/Bakery and snacks/debit/INR|3|5905.06, 6354.26, 5256.32|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_17|salary/Payroll credit/credit/INR|5|206000, 206000, 206000, 206000, 206000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_17|rent/Apartment rent transfer/debit/INR|5|49600, 49600, 49600, 49600, 49600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_17|utilities/Municipal utilities/debit/INR|5|9481.13, 9530.77, 10246.53, 9948.15, 8487.15|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_17|education/Course tuition/debit/INR|5|13660, 13660, 13660, 13660, 13660|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_17|debt_repayment/Credit card repayment/debit/INR|5|30200, 30200, 30200, 30200, 30200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_17|music_subscription/Music subscription/debit/INR|5|2055, 2055, 2055, 2055, 2055|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_17|delivery_membership/Food delivery membership/debit/INR|5|1675, 1675, 1675, 1675, 1675|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_17|groceries/Neighbourhood grocer/debit/INR|2|9392.54, 9785.51|repeated but not demonstrably recurrent|||
|user_17|groceries/Bulk pantry shop/debit/INR|2|7679.25, 7187.32|repeated but not demonstrably recurrent|||
|user_17|groceries/Grocery delivery/debit/INR|3|10039.54, 10300.07, 8543.01|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_17|groceries/Fresh food shop/debit/INR|5|8574.98, 7585.37, 7446.25, 8500.09, 11342.57|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_17|groceries/Local market purchase/debit/INR|9|11380.46, 6706.54, 7237.45, 8836.99, 10690, 11392.07, 11433.33, 7093.83, 8581.99|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_17|groceries/Weekly produce market/debit/INR|2|10432.03, 8638.54|repeated but not demonstrably recurrent|||
|user_17|groceries/Supermarket basket/debit/INR|2|10873.47, 8716.51|repeated but not demonstrably recurrent|||
|user_17|transport/Rail pass/debit/INR|5|3913.59, 4008.13, 6406.38, 5758.89, 5372.15|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_17|transport/Local taxi/debit/INR|5|5639.47, 4445.42, 5936.87, 6420.35, 4661.7|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_17|transport/Commuter pass/debit/INR|3|6225.69, 5386.34, 5741.08|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_17|transport/Ride-hailing trip/debit/INR|3|5421.55, 5126.25, 5940.36|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_17|transport/Vehicle charging/debit/INR|3|5036.82, 4328.91, 3902.91|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_17|transport/Metro and bus fares/debit/INR|5|6170.7, 5790.36, 5080.56, 4844.94, 5650.43|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_17|dining/Bakery and snacks/debit/INR|3|5641.06, 5554.91, 6048.91|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_17|dining/Takeaway order/debit/INR|2|4425.44, 6027.54|repeated but not demonstrably recurrent|||
|user_17|dining/Neighbourhood restaurant/debit/INR|2|5593.53, 6839.37|repeated but not demonstrably recurrent|||
|user_17|dining/Quick-service meal/debit/INR|2|6797.26, 5254.41|repeated but not demonstrably recurrent|||
|user_17|dining/Family dinner/debit/INR|2|6688.81, 4747.76|repeated but not demonstrably recurrent|||
|user_18|salary/Payroll credit/credit/EUR|5|2310, 2310, 2310, 2310, 2310|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_18|housing/Building maintenance payment/debit/EUR|6|167, 167, 167, 167, 167, 167|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_18|utilities/Energy provider bill/debit/EUR|5|100.59, 101.24, 125.4, 121.67, 107.43|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_18|insurance/Household insurance/debit/EUR|5|68, 68, 68, 68, 68|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_18|healthcare/Clinic payment/debit/EUR|5|164.1, 150.18, 152.41, 162.41, 147.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_18|streaming/Family streaming plan/debit/EUR|5|68, 68, 68, 68, 68|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_18|groceries/Bulk pantry shop/debit/EUR|3|64.84, 83.94, 71.92|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_18|groceries/Grocery delivery/debit/EUR|2|101.66, 106.43|repeated but not demonstrably recurrent|||
|user_18|groceries/Local market purchase/debit/EUR|3|96.63, 108.09, 82.18|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_18|groceries/Supermarket basket/debit/EUR|5|101.08, 66.3, 94.02, 101.9, 111.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_18|groceries/Weekly produce market/debit/EUR|2|110.8, 87.91|repeated but not demonstrably recurrent|||
|user_18|groceries/Household groceries/debit/EUR|2|115, 90.08|repeated but not demonstrably recurrent|||
|user_18|transport/Metro and bus fares/debit/EUR|2|36.86, 43.81|repeated but not demonstrably recurrent|||
|user_18|transport/Vehicle charging/debit/EUR|5|54.53, 52.9, 47.5, 50.57, 36.29|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_18|dining/Quick-service meal/debit/EUR|3|66.7, 108.96, 62.87|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_18|dining/Coffee shop/debit/EUR|3|69.84, 66.71, 81.05|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_18|dining/Neighbourhood restaurant/debit/EUR|2|92.92, 75.46|repeated but not demonstrably recurrent|||
|user_18|dining/Lunch with colleagues/debit/EUR|2|98.51, 82.67|repeated but not demonstrably recurrent|||
|user_19|salary/Payroll credit/credit/INR|5|131000, 131000, 131000, 131000, 131000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_19|rent/Residential rent payment/debit/INR|5|36100, 36100, 36100, 36100, 36100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_19|utilities/Municipal utilities/debit/INR|5|6141.28, 5525.82, 6029.9, 5951.99, 6129.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_19|debt_repayment/Loan repayment/debit/INR|5|11850, 11850, 11850, 11850, 11850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_19|healthcare/Clinic payment/debit/INR|5|8946.09, 9619.88, 8335.2, 8496.34, 8645.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_19|family_support/Childcare contribution/debit/INR|5|12650, 12650, 12650, 12650, 12650|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_19|cloud_storage/Online backup subscription/debit/INR|5|395, 395, 395, 395, 395|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_19|shopping/Clothing and household items/debit/INR|5|6302.66, 5593.2, 6069.58, 5772.78, 5431.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_19|groceries/Local market purchase/debit/INR|6|4418.91, 5452.26, 5908.15, 4667.68, 3460.53, 4068.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_19|groceries/Neighbourhood grocer/debit/INR|2|4871.72, 3877.79|repeated but not demonstrably recurrent|||
|user_19|groceries/Fresh food shop/debit/INR|3|6070.85, 4056.71, 3852.58|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_19|groceries/Supermarket basket/debit/INR|2|5912.83, 4963.39|repeated but not demonstrably recurrent|||
|user_19|groceries/Grocery delivery/debit/INR|3|4744.13, 3593.25, 5146.94|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_19|groceries/Bulk pantry shop/debit/INR|5|5406.2, 5542.84, 4738.95, 4444.74, 5184.21|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_19|groceries/Household groceries/debit/INR|2|3575.19, 4493.39|repeated but not demonstrably recurrent|||
|user_19|groceries/Weekly produce market/debit/INR|2|6005.09, 4864.04|repeated but not demonstrably recurrent|||
|user_19|transport/Fuel refill/debit/INR|3|3054.24, 2640.96, 2765.93|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_19|transport/Ride-hailing trip/debit/INR|2|3298.25, 3849.5|repeated but not demonstrably recurrent|||
|user_19|transport/Parking and tolls/debit/INR|2|3476.92, 3659.94|repeated but not demonstrably recurrent|||
|user_19|transport/Rail pass/debit/INR|2|3432.81, 2788.22|repeated but not demonstrably recurrent|||
|user_19|transport/Local taxi/debit/INR|3|2610.24, 2759.93, 2462.29|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_20|salary/Payroll credit/credit/INR|5|108000, 108000, 108000, 108000, 108000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_20|housing/Home association fee/debit/INR|6|7950, 7950, 7950, 7950, 7950, 7950|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_20|utilities/Municipal utilities/debit/INR|6|7784.29, 7977.68, 8058.75, 6848.62, 7551.74, 7769.87|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_20|insurance/Household insurance/debit/INR|6|3290, 3290, 3290, 3290, 3290, 3290|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_20|education/School fee payment/debit/INR|5|8740, 8740, 8740, 8740, 8740|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_20|healthcare/Family healthcare expense/debit/INR|5|5968.18, 6648.5, 5907.73, 6505.49, 6654.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_20|entertainment/Cinema and events/debit/INR|5|2298.76, 2279.67, 2115.92, 1949.86, 2097.15|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_20|cloud_storage/Shared storage plan/debit/INR|5|365, 365, 365, 365, 365|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_20|groceries/Grocery delivery/debit/INR|4|3866.5, 3127.16, 3386.09, 3702.16|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_20|groceries/Supermarket basket/debit/INR|2|3724.49, 4109.13|repeated but not demonstrably recurrent|||
|user_20|groceries/Bulk pantry shop/debit/INR|2|4104.17, 3796.24|repeated but not demonstrably recurrent|||
|user_20|groceries/Weekly produce market/debit/INR|3|2968.61, 2812.26, 4683.37|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_20|groceries/Household groceries/debit/INR|4|4660.33, 3525.04, 3016.03, 4719.22|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_20|groceries/Local market purchase/debit/INR|2|3067.82, 3588.1|repeated but not demonstrably recurrent|||
|user_20|transport/Vehicle charging/debit/INR|3|2046.25, 2195.41, 2632|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_20|transport/Metro and bus fares/debit/INR|3|2359.03, 3145.95, 3243.84|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_20|transport/Fuel refill/debit/INR|2|2838.14, 3150.25|repeated but not demonstrably recurrent|||
|user_20|dining/Takeaway order/debit/INR|2|3150.77, 2857.78|repeated but not demonstrably recurrent|||
|user_20|dining/Bakery and snacks/debit/INR|3|3365.58, 2629.91, 3803.95|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_21|salary/Payroll credit/credit/USD|5|2256, 2256, 2256, 2256, 2256|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_21|rent/Residential rent payment/debit/USD|6|718.8, 718.8, 718.8, 718.8, 718.8, 718.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_21|utilities/Municipal utilities/debit/USD|5|115.31, 123.72, 120.59, 122.18, 124.08|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_21|cloud_storage/Online backup subscription/debit/USD|5|11, 11, 11, 11, 11|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_21|streaming/Streaming subscription/debit/USD|5|47, 47, 47, 47, 47|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_21|shopping/Monthly shopping spend/debit/USD|5|133.38, 115.86, 120.74, 115.71, 126.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_21|groceries/Bulk pantry shop/debit/USD|2|65.93, 66.13|repeated but not demonstrably recurrent|||
|user_21|groceries/Supermarket basket/debit/USD|2|104.23, 101.34|repeated but not demonstrably recurrent|||
|user_21|groceries/Weekly produce market/debit/USD|4|92.12, 104.19, 84.7, 85.9|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_21|groceries/Fresh food shop/debit/USD|4|68.82, 72.06, 90.57, 77.75|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_21|groceries/Household groceries/debit/USD|3|95.62, 79, 70.98|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_21|groceries/Local market purchase/debit/USD|3|77.2, 71.22, 97.55|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_21|transport/Rail pass/debit/USD|2|34.52, 36.86|repeated but not demonstrably recurrent|||
|user_21|transport/Local taxi/debit/USD|2|40.66, 47.84|repeated but not demonstrably recurrent|||
|user_21|transport/Parking and tolls/debit/USD|2|33.38, 51.42|repeated but not demonstrably recurrent|||
|user_21|dining/Takeaway order/debit/USD|2|82.43, 97.67|repeated but not demonstrably recurrent|||
|user_21|dining/Quick-service meal/debit/USD|2|68.28, 88.07|repeated but not demonstrably recurrent|||
|user_21|dining/Bakery and snacks/debit/USD|2|60.18, 100.63|repeated but not demonstrably recurrent|||
|user_21|dining/Neighbourhood restaurant/debit/USD|2|98.39, 69.31|repeated but not demonstrably recurrent|||
|user_22|salary/Payroll credit/credit/EUR|5|616, 616, 616, 616, 616|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_22|rent/Apartment rent transfer/debit/EUR|6|178.2, 178.2, 178.2, 178.2, 178.2, 178.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_22|utilities/Electricity and water bill/debit/EUR|5|32.53, 33.73, 31.52, 27.68, 27.34|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_22|music_subscription/Music service subscription/debit/EUR|5|6, 6, 6, 6, 6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_22|delivery_membership/Food delivery membership/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_22|gym/Gym membership/debit/EUR|5|17, 17, 17, 17, 17|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_22|entertainment/Weekend entertainment/debit/EUR|5|19.64, 18.94, 23.29, 22.03, 20.43|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_22|groceries/Supermarket basket/debit/EUR|5|23.95, 20.6, 26.47, 22.19, 27.33|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_22|groceries/Fresh food shop/debit/EUR|4|29.03, 22.88, 27.59, 26.82|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_22|groceries/Local market purchase/debit/EUR|2|22.38, 23.84|repeated but not demonstrably recurrent|||
|user_22|groceries/Bulk pantry shop/debit/EUR|6|28.31, 25.75, 23.02, 22.14, 29.81, 18.6|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_22|groceries/Household groceries/debit/EUR|2|20.5, 18.35|repeated but not demonstrably recurrent|||
|user_22|groceries/Weekly produce market/debit/EUR|2|21.76, 29.25|repeated but not demonstrably recurrent|||
|user_22|groceries/Neighbourhood grocer/debit/EUR|3|28.46, 19.54, 23.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_22|groceries/Grocery delivery/debit/EUR|2|21.58, 18.71|repeated but not demonstrably recurrent|||
|user_22|transport/Ride-hailing trip/debit/EUR|5|16.09, 15.68, 13.05, 15.08, 11.44|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_22|transport/Commuter pass/debit/EUR|3|11.63, 12.7, 10.72|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_22|transport/Metro and bus fares/debit/EUR|4|16.34, 15.34, 9.9, 15.02|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_22|transport/Fuel refill/debit/EUR|4|10.38, 12.33, 9.7, 15.93|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_22|transport/Local taxi/debit/EUR|4|12.95, 10.41, 10.09, 14.93|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_22|transport/Rail pass/debit/EUR|3|12.59, 12.65, 15.87|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_22|dining/Quick-service meal/debit/EUR|2|12.25, 15.63|repeated but not demonstrably recurrent|||
|user_22|dining/Neighbourhood restaurant/debit/EUR|2|18.82, 17.66|repeated but not demonstrably recurrent|||
|user_22|dining/Coffee shop/debit/EUR|3|13.59, 20.85, 12.65|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_22|dining/Family dinner/debit/EUR|2|14.46, 14.22|repeated but not demonstrably recurrent|||
|user_22|dining/Takeaway order/debit/EUR|2|16.03, 18.41|repeated but not demonstrably recurrent|||
|user_22|dining/Weekend food delivery/debit/EUR|2|18.53, 15.84|repeated but not demonstrably recurrent|||
|user_23|salary/Payroll credit/credit/ZAR|5|45760, 45760, 45760, 45760, 45760|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_23|rent/Shared housing rent/debit/ZAR|6|15312, 15312, 15312, 15312, 15312, 15312|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_23|utilities/Electricity bill/debit/ZAR|5|2877.85, 2484.32, 2915.67, 2813.94, 2680.15|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_23|debt_repayment/Education loan instalment/debit/ZAR|5|5852, 5852, 5852, 5852, 5852|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_23|healthcare/Clinic payment/debit/ZAR|5|1341.05, 1331.22, 1439.91, 1317.68, 1377.89|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_23|family_support/Childcare contribution/debit/ZAR|5|4270.2, 4270.2, 4270.2, 4270.2, 4270.2|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_23|cloud_storage/Cloud storage plan/debit/ZAR|5|295.9, 295.9, 295.9, 295.9, 295.9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_23|shopping/Personal shopping/debit/ZAR|5|1279.39, 1396.33, 1389.39, 1232.23, 1281.33|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_23|groceries/Grocery delivery/debit/ZAR|5|1401.85, 1981.14, 2125.65, 2186.26, 2146.88|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_23|groceries/Household groceries/debit/ZAR|4|1332.28, 1927.69, 1706.85, 1514.83|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_23|groceries/Local market purchase/debit/ZAR|2|1586.85, 1421.88|repeated but not demonstrably recurrent|||
|user_23|groceries/Supermarket basket/debit/ZAR|4|1372.64, 2207.92, 1717.87, 1372.44|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_23|groceries/Neighbourhood grocer/debit/ZAR|5|1821.15, 1914.51, 2074.73, 1678.37, 1257.56|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_23|groceries/Weekly produce market/debit/ZAR|2|2178.52, 1556.59|repeated but not demonstrably recurrent|||
|user_23|groceries/Bulk pantry shop/debit/ZAR|3|1544.99, 1487.69, 1794.76|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_23|transport/Metro and bus fares/debit/ZAR|4|1121.5, 896.02, 1046.56, 783.18|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_23|transport/Parking and tolls/debit/ZAR|3|747.69, 738.21, 834|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_23|transport/Ride-hailing trip/debit/ZAR|2|904.55, 1092.98|repeated but not demonstrably recurrent|||
|user_23|transport/Commuter pass/debit/ZAR|2|968.71, 956.01|repeated but not demonstrably recurrent|||
|user_24|salary/Payroll credit/credit/INR|5|61000, 61000, 61000, 61000, 61000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_24|rent/Landlord standing order/debit/INR|6|18600, 18600, 18600, 18600, 18600, 18600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_24|utilities/Household utility payment/debit/INR|5|3049.81, 3226.12, 3417.7, 3335.41, 3490.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_24|insurance/Insurance policy payment/debit/INR|5|2510, 2510, 2510, 2510, 2510|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_24|cloud_storage/Online backup subscription/debit/INR|5|355, 355, 355, 355, 355|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_24|streaming/Family streaming plan/debit/INR|5|1200, 1200, 1200, 1200, 1200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_24|shopping/Monthly shopping spend/debit/INR|5|2409.82, 2514.9, 2680.78, 2398.76, 2564|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_24|entertainment/Local event tickets/debit/INR|5|1870.6, 2124.72, 1916.16, 1845.75, 1896.25|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_24|groceries/Neighbourhood grocer/debit/INR|6|2886.9, 2024.93, 2564.99, 1843.76, 1824.41, 2113.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_24|groceries/Supermarket basket/debit/INR|2|2236.73, 2042.7|repeated but not demonstrably recurrent|||
|user_24|groceries/Grocery delivery/debit/INR|3|2439.18, 2601.43, 2295.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_24|groceries/Household groceries/debit/INR|5|2201.87, 2958.79, 2145.69, 2260.73, 2106.55|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Commuter pass/debit/INR|5|1663.51, 1091.32, 1586.75, 1218.23, 1514.06|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Metro and bus fares/debit/INR|7|1021.64, 1122.2, 1401.3, 1314.27, 1256.01, 1600.18, 1341.45|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Local taxi/debit/INR|3|1760.99, 1370.25, 1731.13|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Rail pass/debit/INR|3|1208.87, 1438, 1593.41|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Ride-hailing trip/debit/INR|7|1232.11, 1536.25, 1576.88, 1119.08, 1393.89, 1750.91, 1069.31|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Parking and tolls/debit/INR|4|1319.2, 1585.39, 1534.77, 1187.92|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_24|transport/Fuel refill/debit/INR|6|1153.55, 1110.11, 1050.4, 1270.09, 1059.47, 1255.38|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Weekend food delivery/debit/INR|4|1757.23, 1662.99, 1842.2, 1911.68|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Bakery and snacks/debit/INR|2|1886.97, 1985.64|repeated but not demonstrably recurrent|||
|user_24|dining/Takeaway order/debit/INR|4|2149.97, 1291.44, 2105.67, 1918.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Quick-service meal/debit/INR|3|2239.04, 2198, 2184.47|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Neighbourhood restaurant/debit/INR|3|1328.72, 1496.44, 1415.29|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Lunch with colleagues/debit/INR|3|2046.83, 2137.71, 1818.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Coffee shop/debit/INR|4|2288.09, 1893.38, 1783.1, 1423.26|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_24|dining/Family dinner/debit/INR|3|1942.46, 1345.87, 2151.71|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_25|salary/International employer payroll/credit/USD|5|28499994.00, 28499994.00, 28499994.00, 28499994.00, 28499994.00|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_25|rent/Monthly rent/debit/IDR|6|6954000, 6954000, 6954000, 6954000, 6954000, 6954000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_25|utilities/Household utility payment/debit/IDR|5|1338903.44, 1401205.21, 1334719.89, 1341541.39, 1201903.67|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_25|insurance/Insurance policy payment/debit/IDR|5|904400, 904400, 904400, 904400, 904400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_25|cloud_storage/Cloud storage plan/debit/IDR|5|126350, 126350, 126350, 126350, 126350|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_25|streaming/Video streaming plan/debit/IDR|5|573800, 573800, 573800, 573800, 573800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_25|shopping/Monthly shopping spend/debit/IDR|5|966785.96, 1054608.5, 1000693.22, 1102784.74, 1170271.29|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_25|entertainment/Games and recreation/debit/IDR|5|451681.59, 415734.51, 499510.22, 504697.37, 426338.4|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_25|groceries/Bulk pantry shop/debit/IDR|2|1348940.42, 1066197.78|repeated but not demonstrably recurrent|||
|user_25|groceries/Weekly produce market/debit/IDR|4|1510693.45, 1211444.04, 1454933.56, 1335295.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_25|groceries/Grocery delivery/debit/IDR|2|1490390.69, 1388569.11|repeated but not demonstrably recurrent|||
|user_25|groceries/Supermarket basket/debit/IDR|2|1048982.51, 864688.59|repeated but not demonstrably recurrent|||
|user_25|groceries/Neighbourhood grocer/debit/IDR|4|893559.78, 1101344.82, 876032.86, 917586.64|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_25|groceries/Household groceries/debit/IDR|2|983053.43, 1369082.68|repeated but not demonstrably recurrent|||
|user_25|transport/Ride-hailing trip/debit/IDR|5|725793.85, 447746.71, 637250.91, 729004.44, 571596.93|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Metro and bus fares/debit/IDR|7|579668.34, 636547.25, 627417.61, 732740.37, 562442.16, 463292.75, 663001.49|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Parking and tolls/debit/IDR|5|724399.08, 617815.52, 617984.73, 695049.46, 639058|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Local taxi/debit/IDR|5|591314.74, 458415.57, 445484.16, 745983.26, 560613.2|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Fuel refill/debit/IDR|4|567772.41, 557483.97, 542331.16, 458596.67|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Commuter pass/debit/IDR|4|507090.88, 454432.04, 593848.06, 448075.32|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Vehicle charging/debit/IDR|4|547424.01, 721981.78, 549524.6, 664768.21|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_25|transport/Rail pass/debit/IDR|2|522613.77, 721837.88|repeated but not demonstrably recurrent|||
|user_25|dining/Lunch with colleagues/debit/IDR|4|979886.38, 1232054.29, 1251981.8, 777034.83|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_25|dining/Bakery and snacks/debit/IDR|3|1028620.35, 1128974.93, 868921.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_25|dining/Coffee shop/debit/IDR|6|1117067.23, 1115260.36, 1142868.87, 740801.32, 925855.11, 949118.03|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_25|dining/Takeaway order/debit/IDR|3|756322.76, 1095978.2, 1051249.87|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_25|dining/Weekend food delivery/debit/IDR|2|1249486.33, 921922.8|repeated but not demonstrably recurrent|||
|user_25|dining/Quick-service meal/debit/IDR|2|1261355.55, 1057617.64|repeated but not demonstrably recurrent|||
|user_25|dining/Neighbourhood restaurant/debit/IDR|4|897310.27, 956749.83, 1204804.45, 1133036.68|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_26|salary/Website project payment/credit/IDR|3|15665368.16, 17700485.3, 9250911.66|variable but recurrent|61|RECURRING_AMOUNT_UNRESOLVED|
|user_26|salary/Content contract payment/credit/IDR|2|15189344.33, 12465196.73|repeated but not demonstrably recurrent|||
|user_26|rent/Residential rent payment/debit/IDR|5|10374000, 10374000, 10374000, 10374000, 10374000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_26|utilities/Water and power payment/debit/IDR|5|2031034.93, 1920158.26, 2021261.52, 1786852.6, 2081148.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_26|cloud_storage/Cloud storage plan/debit/IDR|5|214700, 214700, 214700, 214700, 214700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_26|streaming/Video streaming plan/debit/IDR|5|560500, 560500, 560500, 560500, 560500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_26|shopping/Clothing and household items/debit/IDR|5|1464056.31, 1465974.22, 1335058.52, 1346357.78, 1241687.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_26|groceries/Household groceries/debit/IDR|2|1272286.93, 1452744.4|repeated but not demonstrably recurrent|||
|user_26|groceries/Bulk pantry shop/debit/IDR|4|1187604.88, 1075544.02, 1317793.77, 1197331.19|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_26|groceries/Local market purchase/debit/IDR|5|1104670.55, 1284616.44, 1278730.52, 1322230.21, 1164380.05|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_26|groceries/Neighbourhood grocer/debit/IDR|2|913664.59, 844694.38|repeated but not demonstrably recurrent|||
|user_26|groceries/Supermarket basket/debit/IDR|2|1463040.01, 1171160.69|repeated but not demonstrably recurrent|||
|user_26|transport/Parking and tolls/debit/IDR|2|880731.59, 592159.83|repeated but not demonstrably recurrent|||
|user_26|transport/Vehicle charging/debit/IDR|2|563023.31, 715741.39|repeated but not demonstrably recurrent|||
|user_26|transport/Metro and bus fares/debit/IDR|2|733311.86, 924411.52|repeated but not demonstrably recurrent|||
|user_26|dining/Coffee shop/debit/IDR|2|708193.07, 888704.7|repeated but not demonstrably recurrent|||
|user_26|dining/Quick-service meal/debit/IDR|2|747988.04, 700278.86|repeated but not demonstrably recurrent|||
|user_26|dining/Takeaway order/debit/IDR|2|759912.71, 932713.32|repeated but not demonstrably recurrent|||
|user_27|salary/Delivery platform payout/credit/ZAR|5|8889.72, 6497.52, 9823.12, 10460.18, 7962.61|variable but recurrent|24|RECURRING_AMOUNT_UNRESOLVED|
|user_27|salary/Task marketplace payout/credit/ZAR|2|10012.65, 6273.02|repeated but not demonstrably recurrent|||
|user_27|salary/Weekly app earnings/credit/ZAR|10|8237.81, 8598.13, 6123.58, 5780.26, 9943.4, 8636.57, 9996.09, 10169.29, 5959.02, 7599.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_27|rent/Monthly rent/debit/ZAR|6|8360, 8360, 8360, 8360, 8360, 8360|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_27|utilities/Municipal utilities/debit/ZAR|5|1834.93, 2189.78, 2123.65, 2084.27, 1901.63|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_27|music_subscription/Audio streaming plan/debit/ZAR|5|344.3, 344.3, 344.3, 344.3, 344.3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_27|delivery_membership/Delivery service plan/debit/ZAR|5|401.5, 401.5, 401.5, 401.5, 401.5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_27|gym/Community fitness plan/debit/ZAR|5|611.6, 611.6, 611.6, 611.6, 611.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_27|entertainment/Weekend entertainment/debit/ZAR|5|1211.57, 1204.44, 1257.93, 1240.82, 1186.49|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_27|salary/Driver platform payout/credit/ZAR|3|8232.97, 6286.27, 10716.93|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_27|groceries/Bulk pantry shop/debit/ZAR|5|1018.68, 1431.91, 1273.9, 1227.54, 1261.31|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_27|groceries/Household groceries/debit/ZAR|3|1317.42, 1110.88, 927.62|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_27|groceries/Supermarket basket/debit/ZAR|8|1474.35, 1369.53, 1221.89, 1230.73, 1093.03, 1365.49, 1101.74, 958.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_27|groceries/Fresh food shop/debit/ZAR|2|1549.98, 1098.58|repeated but not demonstrably recurrent|||
|user_27|groceries/Grocery delivery/debit/ZAR|2|900.66, 1154.39|repeated but not demonstrably recurrent|||
|user_27|groceries/Neighbourhood grocer/debit/ZAR|4|1494.99, 1324.18, 995.77, 1107.78|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_27|transport/Fuel refill/debit/ZAR|5|751.29, 853.86, 838.95, 708.98, 572.29|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_27|transport/Local taxi/debit/ZAR|3|528.25, 793.95, 827.83|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_27|transport/Vehicle charging/debit/ZAR|4|609.97, 752.36, 806.18, 787.37|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_27|transport/Rail pass/debit/ZAR|3|821.62, 622.78, 632.32|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_27|transport/Parking and tolls/debit/ZAR|5|811.01, 710.81, 788.78, 820.65, 850.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_27|transport/Metro and bus fares/debit/ZAR|3|751.51, 721.86, 743.93|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_27|dining/Neighbourhood restaurant/debit/ZAR|2|1446.74, 1357.65|repeated but not demonstrably recurrent|||
|user_27|dining/Lunch with colleagues/debit/ZAR|3|1631.19, 1373.31, 1268.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_27|dining/Family dinner/debit/ZAR|3|1140.95, 1395.26, 1309.72|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_27|dining/Weekend food delivery/debit/ZAR|2|1839.57, 1186.91|repeated but not demonstrably recurrent|||
|user_27|dining/Takeaway order/debit/ZAR|2|1377.14, 1179.23|repeated but not demonstrably recurrent|||
|user_28|salary/Payroll credit/credit/EUR|5|1452, 1452, 1452, 1452, 1452|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_28|rent/Shared housing rent/debit/EUR|6|358.6, 358.6, 358.6, 358.6, 358.6, 358.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_28|utilities/Household utility payment/debit/EUR|6|74.98, 84.3, 78.33, 72.66, 86.6, 87.94|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_28|debt_repayment/Personal loan payment/debit/EUR|5|192, 192, 192, 192, 192|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_28|streaming/Streaming subscription/debit/EUR|5|30, 30, 30, 30, 30|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_28|cloud_storage/Cloud storage plan/debit/EUR|5|11, 11, 11, 11, 11|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_28|shopping/Clothing and household items/debit/EUR|5|28.08, 31.14, 29.54, 28.48, 26.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_28|groceries/Grocery delivery/debit/EUR|4|69.68, 55.36, 62.46, 61.96|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_28|groceries/Supermarket basket/debit/EUR|8|71.21, 66.78, 53.92, 72.46, 70.65, 77.57, 62.39, 76.34|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_28|groceries/Local market purchase/debit/EUR|3|79.63, 72, 84.95|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_28|groceries/Household groceries/debit/EUR|2|52.22, 74.56|repeated but not demonstrably recurrent|||
|user_28|groceries/Weekly produce market/debit/EUR|2|63.82, 66.28|repeated but not demonstrably recurrent|||
|user_28|groceries/Bulk pantry shop/debit/EUR|2|81.99, 64|repeated but not demonstrably recurrent|||
|user_28|groceries/Neighbourhood grocer/debit/EUR|4|84.99, 79.85, 75.11, 52.3|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Parking and tolls/debit/EUR|3|30.27, 32.64, 25.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Local taxi/debit/EUR|6|35.51, 32.78, 34.97, 23.8, 30.3, 36|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Ride-hailing trip/debit/EUR|6|28.74, 32.8, 35.9, 36.58, 31.22, 36.48|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Vehicle charging/debit/EUR|3|28.7, 25.93, 29.66|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Fuel refill/debit/EUR|3|21.58, 21.92, 35.89|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Commuter pass/debit/EUR|3|32.31, 25.96, 27.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_28|transport/Metro and bus fares/debit/EUR|2|25.26, 25.41|repeated but not demonstrably recurrent|||
|user_28|dining/Takeaway order/debit/EUR|3|34.8, 34.25, 50.13|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_28|dining/Weekend food delivery/debit/EUR|3|32.52, 48.37, 47.29|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_28|dining/Family dinner/debit/EUR|2|37.93, 47.12|repeated but not demonstrably recurrent|||
|user_28|dining/Bakery and snacks/debit/EUR|2|29.13, 29.4|repeated but not demonstrably recurrent|||
|user_29|housing/Building maintenance payment/debit/ZAR|6|3806, 3806, 3806, 3806, 3806, 3806|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_29|utilities/Electricity and water bill/debit/ZAR|5|2377.32, 2705.96, 2654.23, 2410.63, 2697.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_29|insurance/Insurance policy payment/debit/ZAR|5|1962.4, 1962.4, 1962.4, 1962.4, 1962.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_29|education/School fee payment/debit/ZAR|5|5170, 5170, 5170, 5170, 5170|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_29|healthcare/Diagnostic test/debit/ZAR|5|3322.86, 3227.06, 2946.58, 3308.26, 2855.03|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_29|entertainment/Games and recreation/debit/ZAR|5|1689.25, 1351.5, 1689.24, 1499.59, 1596.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_29|cloud_storage/Online backup subscription/debit/ZAR|5|181.5, 181.5, 181.5, 181.5, 181.5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_29|salary/Seasonal contract payment/credit/ZAR|2|49319.59, 48165.7|repeated but not demonstrably recurrent|||
|user_29|groceries/Fresh food shop/debit/ZAR|3|1843.23, 1575.34, 1870.78|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_29|groceries/Household groceries/debit/ZAR|3|1741.7, 1603.87, 1610.49|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_29|groceries/Bulk pantry shop/debit/ZAR|3|2084.51, 1574.93, 2167.16|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_29|groceries/Grocery delivery/debit/ZAR|2|1668.71, 1979.39|repeated but not demonstrably recurrent|||
|user_29|groceries/Weekly produce market/debit/ZAR|3|1770.2, 2189, 1640.26|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_29|groceries/Neighbourhood grocer/debit/ZAR|2|2078.42, 2033.84|repeated but not demonstrably recurrent|||
|user_29|transport/Rail pass/debit/ZAR|3|1133.42, 1588.15, 1659.66|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_29|transport/Fuel refill/debit/ZAR|3|1192.55, 1239.04, 1033.87|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_29|transport/Metro and bus fares/debit/ZAR|3|1411.65, 1534.8, 1387.42|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_29|transport/Ride-hailing trip/debit/ZAR|3|1114.85, 1476.26, 1651.06|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_29|dining/Lunch with colleagues/debit/ZAR|3|1581.91, 1373.88, 1295.93|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_29|dining/Bakery and snacks/debit/ZAR|2|1752.77, 1670.72|repeated but not demonstrably recurrent|||
|user_29|dining/Coffee shop/debit/ZAR|2|1182.22, 1682.08|repeated but not demonstrably recurrent|||
|user_30|salary/Independent work payment/credit/USD|2|393, 383.98|repeated but not demonstrably recurrent|||
|user_30|rent/Landlord standing order/debit/USD|6|396, 396, 396, 396, 396, 396|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_30|utilities/Household utility payment/debit/USD|5|93.15, 85.8, 76.37, 94.01, 89.89|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_30|cloud_storage/Online backup subscription/debit/USD|5|7, 7, 7, 7, 7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_30|streaming/Family streaming plan/debit/USD|5|35, 35, 35, 35, 35|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_30|shopping/Monthly shopping spend/debit/USD|5|47.56, 41.98, 49.95, 42.71, 52.34|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_30|salary/Consulting invoice payment/credit/USD|3|619.21, 741.7, 513.88|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_30|salary/Content contract payment/credit/USD|2|487.69, 404.31|repeated but not demonstrably recurrent|||
|user_30|groceries/Weekly produce market/debit/USD|3|46.07, 67.73, 45.43|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_30|groceries/Local market purchase/debit/USD|2|48.71, 46.42|repeated but not demonstrably recurrent|||
|user_30|groceries/Bulk pantry shop/debit/USD|4|52.12, 58.95, 60.95, 46.98|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_30|groceries/Neighbourhood grocer/debit/USD|3|49.31, 45.63, 66.17|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_30|groceries/Supermarket basket/debit/USD|3|57.19, 50.7, 50.39|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_30|transport/Metro and bus fares/debit/USD|2|38.29, 39.42|repeated but not demonstrably recurrent|||
|user_30|transport/Parking and tolls/debit/USD|2|42.9, 32.64|repeated but not demonstrably recurrent|||
|user_30|transport/Fuel refill/debit/USD|2|30.12, 44.08|repeated but not demonstrably recurrent|||
|user_30|dining/Family dinner/debit/USD|3|42.42, 44, 55.92|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_30|dining/Takeaway order/debit/USD|2|70.96, 45.05|repeated but not demonstrably recurrent|||
|user_31|salary/Payroll credit/credit/IDR|5|27740000, 27740000, 27740000, 19972800, 19972800|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_31|rent/Residential rent payment/debit/IDR|5|6080000, 6080000, 6080000, 6080000, 6080000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_31|utilities/Household utility payment/debit/IDR|5|1152185.52, 1090457.82, 1253938.07, 1008797.67, 1213040.64|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_31|music_subscription/Music service subscription/debit/IDR|5|123500, 123500, 123500, 123500, 123500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_31|delivery_membership/Delivery service plan/debit/IDR|5|325850, 325850, 325850, 325850, 325850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_31|gym/Gym membership/debit/IDR|5|475000, 475000, 475000, 475000, 475000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_31|entertainment/Weekend entertainment/debit/IDR|5|385049.16, 353108.58, 313503.16, 335667.02, 367474.01|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Grocery delivery/debit/IDR|3|880673.91, 963093.38, 827773.81|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Local market purchase/debit/IDR|3|960812.35, 761405.85, 713890.65|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Bulk pantry shop/debit/IDR|4|686976.81, 871577.52, 602252.81, 821390.61|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Supermarket basket/debit/IDR|3|674490.17, 744675.82, 1039124.97|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Fresh food shop/debit/IDR|5|998982.76, 630477, 941055.42, 974215.97, 662547.7|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Weekly produce market/debit/IDR|3|603303.09, 818438.89, 691399.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_31|groceries/Neighbourhood grocer/debit/IDR|3|906044.77, 948824.63, 903983.35|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_31|transport/Local taxi/debit/IDR|4|526287.57, 520256.97, 411186.22, 635414.88|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_31|transport/Fuel refill/debit/IDR|4|401405.12, 402309.66, 679222.41, 571993.55|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_31|transport/Metro and bus fares/debit/IDR|2|577180.19, 480468.94|repeated but not demonstrably recurrent|||
|user_31|transport/Vehicle charging/debit/IDR|2|594937.41, 596620.87|repeated but not demonstrably recurrent|||
|user_31|transport/Rail pass/debit/IDR|2|439360.43, 583267.82|repeated but not demonstrably recurrent|||
|user_31|transport/Parking and tolls/debit/IDR|3|581657.19, 625657.98, 640350.31|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_31|transport/Commuter pass/debit/IDR|5|485020.29, 613625.1, 477687.65, 462621.62, 435203.22|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_31|transport/Ride-hailing trip/debit/IDR|3|614803.27, 502509.29, 451671.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_31|dining/Family dinner/debit/IDR|3|543929.35, 815420.06, 585293.82|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_31|dining/Weekend food delivery/debit/IDR|4|581388.06, 575104.28, 520858.99, 725631.67|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_31|dining/Coffee shop/debit/IDR|2|706016.17, 549847.19|repeated but not demonstrably recurrent|||
|user_31|dining/Bakery and snacks/debit/IDR|2|469958.96, 525633.67|repeated but not demonstrably recurrent|||
|user_32|rent/Monthly rent/debit/ZAR|6|15664, 15664, 15664, 15664, 15664, 15664|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_32|utilities/Municipal utilities/debit/ZAR|5|3248.06, 3334.92, 3372.96, 3787.62, 3497.74|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_32|education/Course tuition/debit/ZAR|5|4180, 4180, 4180, 4180, 4180|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_32|debt_repayment/Personal loan payment/debit/ZAR|5|4631, 4631, 4631, 4631, 4631|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_32|music_subscription/Music service subscription/debit/ZAR|5|398.2, 398.2, 398.2, 398.2, 398.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_32|delivery_membership/Grocery delivery membership/debit/ZAR|5|897.6, 897.6, 897.6, 897.6, 897.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_32|salary/First-job payroll/credit/ZAR|2|54120, 54120|repeated but not demonstrably recurrent|||
|user_32|groceries/Weekly produce market/debit/ZAR|2|2598.19, 2516.24|repeated but not demonstrably recurrent|||
|user_32|groceries/Bulk pantry shop/debit/ZAR|6|1825.59, 2546.89, 3042.09, 2488.9, 2938.21, 2166.99|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_32|groceries/Fresh food shop/debit/ZAR|5|2323.19, 2992.96, 2576.83, 3060.48, 3083.84|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_32|groceries/Local market purchase/debit/ZAR|6|2544.15, 2590.01, 2150.36, 2458.31, 2202.47, 2798.61|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_32|groceries/Supermarket basket/debit/ZAR|3|1861.12, 2924.42, 2540.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_32|groceries/Grocery delivery/debit/ZAR|3|2320.83, 2789.31, 2628.3|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Vehicle charging/debit/ZAR|5|1517.06, 1865.09, 1832.74, 1177.93, 1081.46|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Rail pass/debit/ZAR|3|1601.42, 1164.16, 1269.83|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Ride-hailing trip/debit/ZAR|4|1537.9, 1456.23, 1296.18, 1632.82|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Parking and tolls/debit/ZAR|4|1581.28, 1455.01, 1505.41, 1056.38|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Metro and bus fares/debit/ZAR|5|1833.57, 1808.1, 1491.59, 1510.49, 1695.69|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Commuter pass/debit/ZAR|3|1133.97, 1141.5, 1206.04|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_32|transport/Fuel refill/debit/ZAR|2|1147.25, 1630.13|repeated but not demonstrably recurrent|||
|user_32|dining/Bakery and snacks/debit/ZAR|6|2198.36, 2631.33, 2765.53, 2286.7, 1751.49, 1728.94|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_32|dining/Coffee shop/debit/ZAR|2|2326.58, 2964.91|repeated but not demonstrably recurrent|||
|user_33|salary/Payroll credit/credit/INR|5|150000, 150000, 150000, 150000, 150000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_33|rent/Apartment rent transfer/debit/INR|6|41900, 41900, 41900, 41900, 41900, 41900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_33|utilities/Electricity bill/debit/INR|6|7059.3, 6552.65, 7696.86, 8063.79, 6866.56, 6927.74|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_33|insurance/Household insurance/debit/INR|5|5620, 5620, 5620, 5620, 5620|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_33|cloud_storage/Cloud storage plan/debit/INR|5|720, 720, 720, 720, 720|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_33|streaming/Video streaming plan/debit/INR|5|3270, 3270, 3270, 3270, 3270|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_33|shopping/Household shopping/debit/INR|5|6137.05, 4976.38, 5286.54, 6144.25, 5508.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_33|entertainment/Games and recreation/debit/INR|5|4296.59, 3659.83, 3976.25, 3976.26, 3899.76|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_33|groceries/Neighbourhood grocer/debit/INR|2|5440.08, 8501.57|repeated but not demonstrably recurrent|||
|user_33|groceries/Supermarket basket/debit/INR|4|5106.42, 7617.05, 5733.72, 6740.27|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_33|groceries/Weekly produce market/debit/INR|2|8267.8, 8284.25|repeated but not demonstrably recurrent|||
|user_33|groceries/Household groceries/debit/INR|2|6825.28, 7138.6|repeated but not demonstrably recurrent|||
|user_33|groceries/Local market purchase/debit/INR|3|5641.55, 7805.13, 5019.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_33|groceries/Fresh food shop/debit/INR|3|5338.91, 5390.26, 5225.57|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Metro and bus fares/debit/INR|5|2608.92, 3156.6, 2969.87, 3333.12, 3668.72|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Parking and tolls/debit/INR|2|3509.68, 2982.47|repeated but not demonstrably recurrent|||
|user_33|transport/Fuel refill/debit/INR|5|2571.2, 3432.17, 2332.67, 3564.23, 3574.87|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Local taxi/debit/INR|4|3065.18, 3442.26, 2164.33, 2230.51|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Ride-hailing trip/debit/INR|4|2498.15, 3347.24, 3499.02, 2217.74|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Commuter pass/debit/INR|8|3232.73, 3726.2, 2984.85, 3080.68, 2400.12, 3451.61, 2840.45, 3705.4|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Rail pass/debit/INR|4|3047.16, 3176.83, 3619.97, 3300.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_33|transport/Vehicle charging/debit/INR|4|2283.91, 2938.43, 3151.5, 2407.44|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_33|dining/Takeaway order/debit/INR|2|5786.14, 5883.95|repeated but not demonstrably recurrent|||
|user_33|dining/Lunch with colleagues/debit/INR|5|4801.97, 4855.04, 6830.33, 5777.37, 5378.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_33|dining/Quick-service meal/debit/INR|4|7641.48, 5668.24, 5069.58, 6968.86|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_33|dining/Coffee shop/debit/INR|2|5429.67, 7610.07|repeated but not demonstrably recurrent|||
|user_33|dining/Bakery and snacks/debit/INR|5|7309.28, 6584.26, 5473.05, 7761.99, 5737.46|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_33|dining/Weekend food delivery/debit/INR|4|6117.69, 4721.33, 6921.56, 5063.81|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_33|dining/Neighbourhood restaurant/debit/INR|2|5427.49, 6596.34|repeated but not demonstrably recurrent|||
|user_34|salary/Consulting invoice payment/credit/INR|2|70555.14, 120827.25|repeated but not demonstrably recurrent|||
|user_34|rent/Monthly rent/debit/INR|6|51200, 51200, 51200, 51200, 51200, 51200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_34|utilities/Electricity and water bill/debit/INR|5|11559.06, 10693.69, 10464.04, 10869.87, 12130.82|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_34|cloud_storage/Online backup subscription/debit/INR|5|610, 610, 610, 610, 610|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_34|streaming/Streaming subscription/debit/INR|5|4970, 4970, 4970, 4970, 4970|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_34|shopping/Online retail purchases/debit/INR|5|7842.28, 8423.11, 7034.18, 6843.44, 7090.02|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_34|salary/Website project payment/credit/INR|2|65923.21, 80848.14|repeated but not demonstrably recurrent|||
|user_34|salary/Client retainer payment/credit/INR|2|125797.91, 54151.71|repeated but not demonstrably recurrent|||
|user_34|groceries/Supermarket basket/debit/INR|2|9609.76, 10315.07|repeated but not demonstrably recurrent|||
|user_34|groceries/Weekly produce market/debit/INR|4|7582.88, 6807.65, 8859.06, 10894.43|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_34|groceries/Bulk pantry shop/debit/INR|2|9277.95, 8514.93|repeated but not demonstrably recurrent|||
|user_34|groceries/Fresh food shop/debit/INR|3|9632.06, 8482.21, 6258.21|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_34|groceries/Grocery delivery/debit/INR|4|6731.19, 7545.01, 8461.48, 9524.24|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_34|transport/Rail pass/debit/INR|2|4498.17, 4587.5|repeated but not demonstrably recurrent|||
|user_34|transport/Local taxi/debit/INR|3|5254.37, 4355.1, 5568.9|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_34|transport/Metro and bus fares/debit/INR|2|3246.76, 5152.46|repeated but not demonstrably recurrent|||
|user_34|dining/Family dinner/debit/INR|2|5308.3, 8241.06|repeated but not demonstrably recurrent|||
|user_34|dining/Quick-service meal/debit/INR|3|4968.15, 7421.07, 8124.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_34|dining/Lunch with colleagues/debit/INR|2|7315.45, 7893.89|repeated but not demonstrably recurrent|||
|user_35|salary/Payroll credit/credit/INR|6|162000, 162000, 162000, 162000, 162000, 162000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_35|rent/Shared housing rent/debit/INR|6|37000, 37000, 37000, 37000, 37000, 37000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_35|utilities/Energy provider bill/debit/INR|6|11445.46, 12109.61, 9781.39, 10711.25, 11638.22, 11671.34|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_35|education/Professional training fee/debit/INR|6|9710, 9710, 9710, 9710, 9710, 9710|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_35|debt_repayment/Vehicle loan payment/debit/INR|6|9100, 9100, 9100, 9100, 9100, 9100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_35|music_subscription/Music subscription/debit/INR|6|1070, 1070, 1070, 1070, 1070, 1070|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_35|delivery_membership/Grocery delivery membership/debit/INR|6|1275, 1275, 1275, 1275, 1275, 1275|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_35|groceries/Weekly produce market/debit/INR|3|6030.94, 4644.6, 4343.79|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_35|groceries/Fresh food shop/debit/INR|4|4126.32, 4657.69, 6385.74, 5846|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_35|groceries/Household groceries/debit/INR|6|6504.21, 5556.58, 5908.29, 5004.93, 6655.85, 4780.71|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_35|groceries/Neighbourhood grocer/debit/INR|2|5042.88, 5576.71|repeated but not demonstrably recurrent|||
|user_35|groceries/Supermarket basket/debit/INR|2|5415.59, 6837.95|repeated but not demonstrably recurrent|||
|user_35|groceries/Local market purchase/debit/INR|2|5915.59, 4399.03|repeated but not demonstrably recurrent|||
|user_35|groceries/Bulk pantry shop/debit/INR|6|7155.79, 6657.5, 5024.87, 6821.33, 6236.06, 6159.79|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_35|transport/Fuel refill/debit/INR|7|3988.25, 3888.55, 4019.42, 3478.47, 3126.09, 3686.46, 4153.43|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_35|transport/Metro and bus fares/debit/INR|4|5406.79, 3660.49, 3463.39, 3340.44|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_35|transport/Commuter pass/debit/INR|2|5438.92, 3799.13|repeated but not demonstrably recurrent|||
|user_35|transport/Vehicle charging/debit/INR|3|4973.25, 3266.25, 3598.16|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_35|transport/Rail pass/debit/INR|3|3574.56, 4615.04, 3531.85|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_35|transport/Parking and tolls/debit/INR|4|4193.76, 5019.34, 4140.57, 3894.67|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_35|dining/Bakery and snacks/debit/INR|7|5404.46, 4608.5, 5510.39, 4045.52, 5893.45, 4848.04, 4706.22|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_35|dining/Family dinner/debit/INR|2|4954.67, 4235.28|repeated but not demonstrably recurrent|||
|user_35|dining/Neighbourhood restaurant/debit/INR|2|3514.2, 3919.21|repeated but not demonstrably recurrent|||
|user_36|salary/Payroll credit/credit/USD|5|2330.64, 2330.64, 2330.64, 2330.64, 2330.64|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_36|housing/Home association fee/debit/USD|6|260, 260, 260, 260, 260, 260|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_36|utilities/Water and power payment/debit/USD|5|150.63, 167.23, 188.45, 157, 172.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_36|insurance/Insurance policy payment/debit/USD|5|94, 94, 94, 94, 94|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_36|healthcare/Clinic payment/debit/USD|5|174.4, 189.35, 186.47, 186.19, 186.99|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_36|streaming/Video streaming plan/debit/USD|5|72, 72, 72, 72, 72|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_36|groceries/Household groceries/debit/USD|4|168.42, 139.24, 154.99, 100.7|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_36|groceries/Weekly produce market/debit/USD|4|173.55, 135.38, 129.71, 165.75|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_36|groceries/Neighbourhood grocer/debit/USD|3|115.64, 160.58, 130.95|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_36|groceries/Bulk pantry shop/debit/USD|2|131.42, 162.53|repeated but not demonstrably recurrent|||
|user_36|groceries/Grocery delivery/debit/USD|3|174.61, 147.52, 121.83|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_36|transport/Vehicle charging/debit/USD|2|65.95, 72.01|repeated but not demonstrably recurrent|||
|user_36|transport/Rail pass/debit/USD|4|46.5, 63.03, 65, 56.9|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_36|transport/Fuel refill/debit/USD|2|57.79, 58.04|repeated but not demonstrably recurrent|||
|user_36|transport/Commuter pass/debit/USD|3|45.12, 68.64, 60.1|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_36|dining/Coffee shop/debit/USD|3|155.99, 118.32, 132.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_36|dining/Family dinner/debit/USD|3|148.25, 149.17, 127.37|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_36|dining/Neighbourhood restaurant/debit/USD|4|142.95, 134.21, 136.61, 141.29|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_37|salary/Payroll credit/credit/IDR|5|21090000, 21090000, 21090000, 21090000, 21090000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_37|rent/Monthly rent/debit/IDR|6|6802000, 6802000, 6802000, 6802000, 6802000, 6802000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_37|utilities/Electricity bill/debit/IDR|5|1341134.66, 1395569.91, 1378424.13, 1319874.42, 1334626.93|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_37|debt_repayment/Loan repayment/debit/IDR|5|2945000, 2945000, 2945000, 2945000, 2945000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_37|streaming/Streaming subscription/debit/IDR|5|406600, 406600, 406600, 406600, 406600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_37|cloud_storage/Shared storage plan/debit/IDR|5|121600, 121600, 121600, 121600, 121600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_37|shopping/Online retail purchases/debit/IDR|5|389820.28, 462899.27, 440819.97, 453407.03, 432058.92|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_37|groceries/Local market purchase/debit/IDR|5|1183513.31, 821510.22, 1131276.83, 1136734.11, 1113864.66|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_37|groceries/Fresh food shop/debit/IDR|2|975344.72, 942462.65|repeated but not demonstrably recurrent|||
|user_37|groceries/Supermarket basket/debit/IDR|5|905217.57, 1207692.58, 977144.43, 781207.66, 956184.71|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_37|groceries/Bulk pantry shop/debit/IDR|3|1102926.17, 978528.33, 817747.22|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_37|groceries/Neighbourhood grocer/debit/IDR|3|1216491.71, 865332.85, 713728.21|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_37|groceries/Household groceries/debit/IDR|6|924782.45, 966491.34, 1168493.31, 1199659.31, 1127709.46, 926605.37|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_37|transport/Rail pass/debit/IDR|4|711176.83, 654819.15, 593664.77, 671554.37|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_37|transport/Vehicle charging/debit/IDR|2|539717.14, 453458.18|repeated but not demonstrably recurrent|||
|user_37|transport/Parking and tolls/debit/IDR|5|641489.94, 571716.03, 648746.23, 696746.25, 680684.38|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_37|transport/Ride-hailing trip/debit/IDR|5|414595.7, 584506.2, 689431.99, 461083.61, 420924.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_37|transport/Local taxi/debit/IDR|3|473100.8, 466009.55, 639487.68|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_37|transport/Commuter pass/debit/IDR|2|493762.29, 427444.02|repeated but not demonstrably recurrent|||
|user_37|transport/Fuel refill/debit/IDR|3|414774.56, 473747.97, 717412.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_37|transport/Metro and bus fares/debit/IDR|2|644312.34, 477533.41|repeated but not demonstrably recurrent|||
|user_37|dining/Quick-service meal/debit/IDR|4|710878.49, 841290.42, 933107.39, 653548|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_37|dining/Bakery and snacks/debit/IDR|2|1100750.6, 1036425.76|repeated but not demonstrably recurrent|||
|user_37|dining/Weekend food delivery/debit/IDR|3|869927.19, 1058454.05, 1044964.61|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_37|dining/Takeaway order/debit/IDR|2|745968.36, 773404.6|repeated but not demonstrably recurrent|||
|user_38|salary/Payroll credit/credit/EUR|5|737, 737, 737, 737, 737|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_38|housing/Property maintenance contribution/debit/EUR|6|68, 68, 68, 68, 68, 68|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_38|utilities/Household utility payment/debit/EUR|5|42.49, 39.22, 43.52, 46.31, 39.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_38|insurance/Household insurance/debit/EUR|5|19, 19, 19, 19, 19|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_38|education/Professional training fee/debit/EUR|5|57, 57, 57, 57, 57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_38|healthcare/Clinic payment/debit/EUR|5|31.03, 34.22, 32.34, 37.34, 33.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_38|entertainment/Local event tickets/debit/EUR|5|11.78, 10.78, 10.8, 9.98, 12.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_38|cloud_storage/Cloud storage plan/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_38|groceries/Household groceries/debit/EUR|5|24.07, 23.54, 34.47, 36.45, 27.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_38|groceries/Weekly produce market/debit/EUR|2|32.11, 38.95|repeated but not demonstrably recurrent|||
|user_38|groceries/Grocery delivery/debit/EUR|2|38, 38.43|repeated but not demonstrably recurrent|||
|user_38|groceries/Local market purchase/debit/EUR|2|32.62, 23.7|repeated but not demonstrably recurrent|||
|user_38|groceries/Fresh food shop/debit/EUR|3|32.49, 36.95, 34.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_38|groceries/Bulk pantry shop/debit/EUR|2|24.15, 28.11|repeated but not demonstrably recurrent|||
|user_38|transport/Vehicle charging/debit/EUR|5|17.65, 22.77, 17.11, 15.1, 21.29|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_38|transport/Local taxi/debit/EUR|2|17.51, 22.85|repeated but not demonstrably recurrent|||
|user_38|transport/Ride-hailing trip/debit/EUR|4|20.86, 22.39, 17.97, 14.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_38|dining/Lunch with colleagues/debit/EUR|5|22.66, 21.16, 27.25, 28.62, 16.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_39|salary/Payroll credit/credit/USD|5|253989.84, 253989.84, 253989.84, 253989.84, 253989.84|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_39|rent/Residential rent payment/debit/INR|5|78000, 78000, 78000, 78000, 78000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_39|utilities/Energy provider bill/debit/INR|5|12624.54, 14652.43, 14231.07, 12888.91, 15188.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_39|insurance/Vehicle insurance premium/debit/INR|5|10200, 10200, 10200, 10200, 10200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_39|cloud_storage/Shared storage plan/debit/INR|5|1265, 1265, 1265, 1265, 1265|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_39|streaming/Family streaming plan/debit/INR|5|5580, 5580, 5580, 5580, 5580|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_39|shopping/Clothing and household items/debit/INR|5|10365.01, 9687.98, 8883.54, 9153.47, 10493.1|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_39|entertainment/Local event tickets/debit/INR|5|8391.59, 8414.85, 9050.61, 10083.9, 10303.77|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_39|groceries/Bulk pantry shop/debit/INR|4|7190.87, 7990.94, 6706.17, 10600.82|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_39|groceries/Local market purchase/debit/INR|5|8628.65, 8670.25, 7560.07, 7815.26, 11274.71|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_39|groceries/Grocery delivery/debit/INR|3|6795.88, 7375.89, 8118.26|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_39|groceries/Fresh food shop/debit/INR|2|8249.03, 7762.27|repeated but not demonstrably recurrent|||
|user_39|transport/Vehicle charging/debit/INR|9|3374.1, 5551.38, 5318.27, 5592.03, 5474.3, 3345.92, 3970.83, 5400.47, 4801.49|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_39|transport/Local taxi/debit/INR|7|4107.61, 5234.19, 3653.47, 3599.19, 4597.09, 4515.72, 5491.75|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_39|transport/Parking and tolls/debit/INR|7|4237.74, 4305.65, 5370.06, 4578.2, 5073.39, 3696.04, 5296.85|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_39|transport/Rail pass/debit/INR|3|5415.1, 3639.28, 5167.04|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_39|transport/Ride-hailing trip/debit/INR|3|3474.47, 3785.95, 4491.07|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_39|transport/Fuel refill/debit/INR|3|4906.65, 4873.71, 5003.12|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_39|transport/Commuter pass/debit/INR|2|4042.7, 5852.46|repeated but not demonstrably recurrent|||
|user_39|dining/Weekend food delivery/debit/INR|2|12069.74, 9836.35|repeated but not demonstrably recurrent|||
|user_39|dining/Family dinner/debit/INR|2|11060.84, 7054.43|repeated but not demonstrably recurrent|||
|user_39|dining/Bakery and snacks/debit/INR|4|8094.72, 10788.78, 12277.03, 8798.28|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_39|dining/Takeaway order/debit/INR|2|8195.46, 8286.79|repeated but not demonstrably recurrent|||
|user_39|dining/Coffee shop/debit/INR|7|11141.53, 10194.7, 11632.09, 9461.85, 10045.3, 8817.62, 9668.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_39|dining/Lunch with colleagues/debit/INR|4|6979.9, 8744.79, 9516.94, 10022.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_39|dining/Neighbourhood restaurant/debit/INR|3|11580.79, 8133, 7105.79|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_39|dining/Quick-service meal/debit/INR|2|7303.28, 8098.78|repeated but not demonstrably recurrent|||
|user_40|rent/Shared housing rent/debit/EUR|6|581.9, 581.9, 581.9, 581.9, 581.9, 581.9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_40|utilities/Household utility payment/debit/EUR|6|122.69, 125.8, 103.23, 109.61, 107.23, 108.96|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_40|education/Professional training fee/debit/EUR|5|156, 156, 156, 156, 156|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_40|debt_repayment/Education loan instalment/debit/EUR|5|112, 112, 112, 112, 112|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_40|music_subscription/Music subscription/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_40|delivery_membership/Grocery delivery membership/debit/EUR|5|29, 29, 29, 29, 29|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_40|salary/First-job payroll/credit/EUR|2|1760, 1760|repeated but not demonstrably recurrent|||
|user_40|groceries/Weekly produce market/debit/EUR|4|71.52, 77.53, 67.02, 60.27|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_40|groceries/Grocery delivery/debit/EUR|4|91.12, 65.2, 84.31, 72.06|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_40|groceries/Supermarket basket/debit/EUR|5|79.22, 62.71, 82.94, 82.82, 90.75|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_40|groceries/Fresh food shop/debit/EUR|3|88.47, 82.11, 65.27|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_40|groceries/Local market purchase/debit/EUR|3|58.02, 76.96, 94.58|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_40|groceries/Neighbourhood grocer/debit/EUR|4|67.1, 58.16, 68.07, 62.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_40|groceries/Bulk pantry shop/debit/EUR|2|81, 57.42|repeated but not demonstrably recurrent|||
|user_40|transport/Metro and bus fares/debit/EUR|4|32.41, 32.58, 37.07, 42.66|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_40|transport/Rail pass/debit/EUR|6|46.26, 38.4, 35.25, 28.76, 37.37, 46.54|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_40|transport/Local taxi/debit/EUR|3|39.23, 38.84, 46.52|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_40|transport/Vehicle charging/debit/EUR|3|29.75, 38.99, 33.24|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_40|transport/Ride-hailing trip/debit/EUR|2|45.56, 32.53|repeated but not demonstrably recurrent|||
|user_40|transport/Parking and tolls/debit/EUR|4|36.45, 43.3, 29.93, 32.13|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_40|transport/Commuter pass/debit/EUR|3|44.6, 28.18, 35.83|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_40|dining/Family dinner/debit/EUR|3|54.86, 67.12, 88.06|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_40|dining/Quick-service meal/debit/EUR|3|71.56, 80.17, 84.66|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_40|dining/Weekend food delivery/debit/EUR|2|66.17, 55.3|repeated but not demonstrably recurrent|||
|user_40|dining/Lunch with colleagues/debit/EUR|2|65.51, 71.4|repeated but not demonstrably recurrent|||
|user_41|salary/International employer payroll/credit/USD|5|42559991.04, 42559991.04, 42559991.04, 42559991.04, 42559991.04|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_41|rent/Residential rent payment/debit/IDR|6|9481000, 9481000, 9481000, 9481000, 9481000, 9481000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_41|utilities/Water and power payment/debit/IDR|5|3289546.81, 3180849.97, 2768119.17, 2876099.03, 2844686.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_41|insurance/Insurance policy payment/debit/IDR|5|2074800, 2074800, 2074800, 2074800, 2074800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_41|cloud_storage/Shared storage plan/debit/IDR|5|280250, 280250, 280250, 280250, 280250|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_41|streaming/Family streaming plan/debit/IDR|5|868300, 868300, 868300, 868300, 868300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_41|shopping/Monthly shopping spend/debit/IDR|5|834688.72, 910854.26, 890189.08, 1020016.13, 866138.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_41|entertainment/Weekend entertainment/debit/IDR|5|1248432.91, 1120516.5, 1131200.82, 1250235.16, 1059461.44|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_41|groceries/Local market purchase/debit/IDR|2|2101085.81, 1656866.98|repeated but not demonstrably recurrent|||
|user_41|groceries/Household groceries/debit/IDR|4|1554704.76, 1770666.45, 1972340.56, 1504239.64|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_41|groceries/Supermarket basket/debit/IDR|4|2047197.38, 1903537.62, 1683203.41, 1500372.11|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_41|groceries/Neighbourhood grocer/debit/IDR|2|1648489.14, 2074784.86|repeated but not demonstrably recurrent|||
|user_41|groceries/Bulk pantry shop/debit/IDR|3|1454619.85, 1848201.26, 2045655|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_41|groceries/Fresh food shop/debit/IDR|3|1516927.14, 2161076.98, 1653749.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_41|transport/Ride-hailing trip/debit/IDR|2|1189932.92, 965182.5|repeated but not demonstrably recurrent|||
|user_41|transport/Local taxi/debit/IDR|3|1330667.83, 1303795.21, 944289.2|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_41|transport/Commuter pass/debit/IDR|2|1161634.8, 806631.07|repeated but not demonstrably recurrent|||
|user_41|transport/Parking and tolls/debit/IDR|7|786847.39, 889230.23, 779377.47, 1160601.31, 1097807.42, 953463.2, 802592.24|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_41|transport/Metro and bus fares/debit/IDR|3|921381.18, 822238.47, 981549.23|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_41|transport/Rail pass/debit/IDR|5|912201.33, 780896.21, 1196957.66, 795941.48, 1010163.17|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_41|transport/Fuel refill/debit/IDR|7|933696.56, 1094945.55, 797867.84, 1336805.67, 978814.58, 889413.78, 936369.57|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_41|transport/Vehicle charging/debit/IDR|7|1079644.05, 1258004.31, 1121579.27, 974042.31, 1339348.81, 982311.17, 1099391.61|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_41|dining/Takeaway order/debit/IDR|4|1167974.45, 966580.92, 995834.06, 1140271.72|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_41|dining/Lunch with colleagues/debit/IDR|3|1087683.23, 1199665.17, 872759.45|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_41|dining/Coffee shop/debit/IDR|5|1428610.73, 841278.9, 1200758.48, 1045939.43, 1128622.17|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_41|dining/Quick-service meal/debit/IDR|5|1404838.13, 1243094.22, 1102894.26, 948636.58, 917569.75|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_41|dining/Bakery and snacks/debit/IDR|5|1414517.63, 978666.15, 843363.3, 875721.91, 967177.63|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_42|salary/Primary household salary/credit/INR|5|91760, 91760, 91760, 91760, 91760|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_42|salary/Second household income/credit/INR|4|54639.34, 73857.43, 55354.29, 64982.45|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_42|rent/Apartment rent transfer/debit/INR|6|40200, 40200, 40200, 40200, 40200, 40200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_42|utilities/Electricity bill/debit/INR|5|7480.84, 8328.16, 7397.6, 8833.75, 8212.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_42|insurance/Vehicle insurance premium/debit/INR|5|4930, 4930, 4930, 4930, 4930|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_42|cloud_storage/Online backup subscription/debit/INR|5|1275, 1275, 1275, 1275, 1275|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_42|streaming/Video streaming plan/debit/INR|5|3910, 3910, 3910, 3910, 3910|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_42|shopping/Clothing and household items/debit/INR|5|3515.6, 3295.86, 3406.05, 3196.37, 3534.51|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_42|entertainment/Local event tickets/debit/INR|5|6006.3, 5387.5, 5808.83, 5009.99, 5649.79|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_42|groceries/Household groceries/debit/INR|3|7930.42, 6402.79, 7903.46|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_42|groceries/Local market purchase/debit/INR|2|4792.86, 6569.24|repeated but not demonstrably recurrent|||
|user_42|groceries/Neighbourhood grocer/debit/INR|2|8164.28, 5660.19|repeated but not demonstrably recurrent|||
|user_42|groceries/Grocery delivery/debit/INR|4|5986.36, 6887.13, 6395.38, 6363.31|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_42|groceries/Weekly produce market/debit/INR|4|6876.75, 8246.4, 4906.62, 7685.97|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Fuel refill/debit/INR|6|3026.58, 3259.53, 3615.25, 3219.89, 2946.1, 2476.73|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Commuter pass/debit/INR|5|2614.87, 3405.79, 4238.32, 2469.77, 3910.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Local taxi/debit/INR|5|2609.68, 3197.78, 2860.93, 3604.65, 3185.05|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Metro and bus fares/debit/INR|4|4146.92, 4261.08, 3374.4, 2607.32|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Ride-hailing trip/debit/INR|4|3042.63, 3527.32, 3258.36, 2462.58|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Vehicle charging/debit/INR|4|2639.58, 2548.78, 2886.7, 2802.17|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_42|transport/Rail pass/debit/INR|6|3725.47, 4101.77, 3044.92, 3568, 3102.23, 2651.4|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_42|dining/Lunch with colleagues/debit/INR|5|6196.55, 5084.86, 4847.75, 4589.41, 6733.24|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_42|dining/Family dinner/debit/INR|6|6568.34, 4557.61, 4075.3, 4656.93, 4957.44, 4672.84|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_42|dining/Bakery and snacks/debit/INR|3|6598.14, 4496.49, 4599.24|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_42|dining/Coffee shop/debit/INR|5|5414.53, 4829.77, 5908.71, 4094.65, 6236.17|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_42|dining/Quick-service meal/debit/INR|3|4940.63, 6647.99, 4355.63|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_42|dining/Takeaway order/debit/INR|2|4677.59, 4895.77|repeated but not demonstrably recurrent|||
|user_43|salary/Previous employer payroll/credit/IDR|4|32870000, 32870000, 32870000, 32870000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_43|rent/Monthly rent/debit/IDR|6|8911000, 8911000, 8911000, 8911000, 8911000, 8911000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_43|utilities/Municipal utilities/debit/IDR|5|1685410.09, 1708050.9, 1583105.94, 1682559.51, 1617233.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_43|debt_repayment/Credit card repayment/debit/IDR|5|2261000, 2261000, 2261000, 2261000, 2261000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_43|music_subscription/Music subscription/debit/IDR|5|242250, 242250, 242250, 242250, 242250|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_43|groceries/Neighbourhood grocer/debit/IDR|2|1862305.14, 1765704.13|repeated but not demonstrably recurrent|||
|user_43|groceries/Grocery delivery/debit/IDR|3|1458199.97, 1408011.92, 1462990.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_43|groceries/Supermarket basket/debit/IDR|3|1359366.81, 1736392.56, 1424509.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_43|transport/Ride-hailing trip/debit/IDR|2|592728.21, 554179.5|repeated but not demonstrably recurrent|||
|user_43|transport/Parking and tolls/debit/IDR|2|684683.75, 724222.29|repeated but not demonstrably recurrent|||
|user_43|transport/Commuter pass/debit/IDR|3|777838.4, 698532.15, 646510.77|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_43|dining/Lunch with colleagues/debit/IDR|2|1023567.2, 1005523.88|repeated but not demonstrably recurrent|||
|user_43|dining/Bakery and snacks/debit/IDR|2|978866.42, 1048033.4|repeated but not demonstrably recurrent|||
|user_44|rent/Apartment rent transfer/debit/INR|6|30200, 30200, 30200, 30200, 30200, 30200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_44|utilities/Municipal utilities/debit/INR|5|7385.43, 7895.92, 7321.8, 8642.12, 7930.55|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_44|education/Professional training fee/debit/INR|5|8760, 8760, 8760, 8760, 8760|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_44|debt_repayment/Loan repayment/debit/INR|5|12650, 12650, 12650, 12650, 12650|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_44|music_subscription/Music service subscription/debit/INR|5|1550, 1550, 1550, 1550, 1550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_44|delivery_membership/Food delivery membership/debit/INR|5|1440, 1440, 1440, 1440, 1440|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_44|salary/First-job payroll/credit/INR|2|115000, 115000|repeated but not demonstrably recurrent|||
|user_44|groceries/Weekly produce market/debit/INR|3|4119.93, 4968.17, 4553.39|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_44|groceries/Fresh food shop/debit/INR|2|6085.82, 5921.61|repeated but not demonstrably recurrent|||
|user_44|groceries/Neighbourhood grocer/debit/INR|7|5028.69, 6658.41, 6503.89, 4112.17, 4836.93, 3854.1, 5852.75|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_44|groceries/Local market purchase/debit/INR|6|4776.5, 5087.92, 4933.3, 4543.97, 6151.15, 4742.05|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_44|groceries/Household groceries/debit/INR|2|4703.51, 5409.25|repeated but not demonstrably recurrent|||
|user_44|groceries/Grocery delivery/debit/INR|2|6319.21, 6365.09|repeated but not demonstrably recurrent|||
|user_44|groceries/Supermarket basket/debit/INR|3|4203.29, 5004.8, 6657.46|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_44|transport/Local taxi/debit/INR|6|2618.38, 2244.56, 1922.99, 2823.22, 2685.99, 2948.25|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_44|transport/Rail pass/debit/INR|4|2639.02, 1821.57, 2385.51, 2817.78|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_44|transport/Commuter pass/debit/INR|2|2394.25, 3018.86|repeated but not demonstrably recurrent|||
|user_44|transport/Ride-hailing trip/debit/INR|4|2925.83, 1919.43, 3008.85, 2745.34|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_44|transport/Fuel refill/debit/INR|4|2394.09, 2198.85, 1896.11, 2109.96|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_44|transport/Parking and tolls/debit/INR|3|1861.46, 1965.48, 1981.96|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_44|transport/Metro and bus fares/debit/INR|2|2286.38, 2713.85|repeated but not demonstrably recurrent|||
|user_44|dining/Weekend food delivery/debit/INR|3|4930.56, 4376.63, 4947.48|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_44|dining/Quick-service meal/debit/INR|2|4117.85, 4119.72|repeated but not demonstrably recurrent|||
|user_44|dining/Lunch with colleagues/debit/INR|4|5041.84, 3921.53, 4129.11, 3593.85|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_44|dining/Neighbourhood restaurant/debit/INR|2|3767.16, 4302.86|repeated but not demonstrably recurrent|||
|user_45|salary/Payroll credit/credit/IDR|5|13486200, 13486200, 13486200, 13486200, 13486200|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_45|housing/Building maintenance payment/debit/IDR|6|1805000, 1805000, 1805000, 1805000, 1805000, 1805000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_45|utilities/Household utility payment/debit/IDR|5|1228559.79, 1225368.81, 1013909.42, 1213848.32, 1152956.21|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_45|insurance/Health insurance premium/debit/IDR|5|803700, 803700, 803700, 803700, 803700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_45|healthcare/Clinic payment/debit/IDR|5|1148608.81, 1234481.57, 1306215.24, 1225900.99, 1183829.25|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_45|streaming/Video streaming plan/debit/IDR|5|421800, 421800, 421800, 421800, 421800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_45|groceries/Grocery delivery/debit/IDR|3|977279.33, 566430.29, 703870.69|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_45|groceries/Weekly produce market/debit/IDR|4|766024.75, 965227.33, 885888.67, 552745.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_45|groceries/Fresh food shop/debit/IDR|2|698888.91, 842318.91|repeated but not demonstrably recurrent|||
|user_45|groceries/Local market purchase/debit/IDR|4|753157.3, 763685.19, 687181.49, 725310.9|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_45|groceries/Supermarket basket/debit/IDR|2|685990.47, 788275.84|repeated but not demonstrably recurrent|||
|user_45|groceries/Bulk pantry shop/debit/IDR|3|580659.39, 634323.46, 895951.35|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_45|transport/Parking and tolls/debit/IDR|2|284718.87, 368195.5|repeated but not demonstrably recurrent|||
|user_45|transport/Vehicle charging/debit/IDR|4|328960.63, 360940.42, 380591.63, 364018.74|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_45|transport/Ride-hailing trip/debit/IDR|4|333028.78, 430058.46, 285028.77, 476974.64|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_45|transport/Rail pass/debit/IDR|2|419220.18, 368913.89|repeated but not demonstrably recurrent|||
|user_45|dining/Takeaway order/debit/IDR|3|634646.92, 694869.75, 784805.26|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_45|dining/Bakery and snacks/debit/IDR|2|697673.24, 876568.34|repeated but not demonstrably recurrent|||
|user_45|dining/Coffee shop/debit/IDR|4|886566.82, 595657.61, 812461.01, 551455.65|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_45|dining/Family dinner/debit/IDR|2|839259.57, 533606.53|repeated but not demonstrably recurrent|||
|user_46|salary/Payroll credit/credit/INR|5|145000, 145000, 145000, 145000, 145000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_46|rent/Shared housing rent/debit/INR|5|33800, 33800, 33800, 33800, 33800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_46|utilities/Electricity and water bill/debit/INR|5|7190.22, 6669.77, 7303.04, 7363.21, 7551.34|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_46|debt_repayment/Credit card repayment/debit/INR|5|14300, 14300, 14300, 14300, 14300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_46|streaming/Streaming subscription/debit/INR|5|4030, 4030, 4030, 4030, 4030|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_46|cloud_storage/Online backup subscription/debit/INR|5|1015, 1015, 1015, 1015, 1015|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_46|shopping/Monthly shopping spend/debit/INR|5|5908.19, 5190.1, 5990.36, 5691.76, 5163.45|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_46|groceries/Grocery delivery/debit/INR|3|5425.65, 7664.05, 6252.54|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_46|groceries/Supermarket basket/debit/INR|4|6093.89, 6346.56, 4896.78, 7421.57|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_46|groceries/Household groceries/debit/INR|8|7699.83, 8444.33, 5505.03, 8365.64, 6569.95, 6222.01, 5756.42, 6228.33|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_46|groceries/Fresh food shop/debit/INR|3|6642.41, 7465.05, 6486.99|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_46|groceries/Weekly produce market/debit/INR|5|8064.83, 7203.28, 6470.02, 8465.21, 5268.99|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_46|groceries/Local market purchase/debit/INR|2|6086.63, 7472.5|repeated but not demonstrably recurrent|||
|user_46|transport/Fuel refill/debit/INR|2|3092.8, 2903.51|repeated but not demonstrably recurrent|||
|user_46|transport/Commuter pass/debit/INR|4|2407.75, 2793.87, 3896.51, 2669.57|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_46|transport/Local taxi/debit/INR|5|3432.18, 3312.65, 3469.32, 3565.2, 3820.95|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_46|transport/Ride-hailing trip/debit/INR|3|2728.1, 3754.36, 3792.13|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_46|transport/Vehicle charging/debit/INR|4|2399.14, 2396.69, 3507.27, 2786.59|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_46|transport/Parking and tolls/debit/INR|3|2380.02, 3793.17, 3416.06|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_46|transport/Rail pass/debit/INR|3|3450.29, 3843.93, 3068.6|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_46|dining/Takeaway order/debit/INR|2|4037.72, 3964.73|repeated but not demonstrably recurrent|||
|user_46|dining/Weekend food delivery/debit/INR|2|3435.86, 3251.28|repeated but not demonstrably recurrent|||
|user_46|dining/Lunch with colleagues/debit/INR|3|3508.7, 3097.12, 5093.66|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_46|dining/Coffee shop/debit/INR|3|4114.65, 4690.61, 3755.96|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|salary/Delivery platform payout/credit/IDR|9|9332890.49, 11009151.24, 7092232.98, 9520134.17, 8485361.48, 7828070.03, 8136054.17, 10789727.74, 7214390.64|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_47|salary/Driver platform payout/credit/IDR|4|7628376.71, 12178714.02, 6226625.12, 7396022.86|variable but recurrent|52|RECURRING_AMOUNT_UNRESOLVED|
|user_47|rent/Shared housing rent/debit/IDR|6|12065000, 12065000, 12065000, 12065000, 12065000, 12065000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_47|utilities/Household utility payment/debit/IDR|5|2342844.46, 2279644.26, 2097774.61, 2367661.34, 2171424.17|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_47|music_subscription/Music service subscription/debit/IDR|5|497800, 497800, 497800, 497800, 497800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_47|delivery_membership/Delivery service plan/debit/IDR|5|390450, 390450, 390450, 390450, 390450|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_47|gym/Community fitness plan/debit/IDR|5|1060200, 1060200, 1060200, 1060200, 1060200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_47|entertainment/Cinema and events/debit/IDR|5|1078404.28, 1145687.68, 1123695.85, 1315156.69, 1286741.75|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_47|salary/Task marketplace payout/credit/IDR|4|7274235.16, 9502005.24, 6069851.66, 6938278.02|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|salary/Weekly app earnings/credit/IDR|3|9697934.32, 9557056.93, 11952445.07|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|groceries/Local market purchase/debit/IDR|4|1532552.23, 1473050.77, 1428318.59, 1571252.48|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_47|groceries/Supermarket basket/debit/IDR|7|1383610.76, 1278781.69, 1408580.21, 1426244.6, 1594457, 1205276.71, 1273652.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|groceries/Weekly produce market/debit/IDR|2|1225002.13, 1013560.97|repeated but not demonstrably recurrent|||
|user_47|groceries/Neighbourhood grocer/debit/IDR|4|1620477.34, 1046711.61, 1007246.7, 1042275.72|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|groceries/Grocery delivery/debit/IDR|2|1606242.66, 1024252.12|repeated but not demonstrably recurrent|||
|user_47|groceries/Household groceries/debit/IDR|3|1510803.38, 1575906.35, 1368753.52|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_47|groceries/Fresh food shop/debit/IDR|2|1513951.89, 1590917.92|repeated but not demonstrably recurrent|||
|user_47|transport/Local taxi/debit/IDR|7|1272741.07, 1021122.71, 836955.92, 950773.84, 916573.6, 1078289.86, 978487.95|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|transport/Ride-hailing trip/debit/IDR|4|1029488.57, 982544.02, 1213709.76, 1162031.19|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_47|transport/Parking and tolls/debit/IDR|2|1026048.96, 959061.11|repeated but not demonstrably recurrent|||
|user_47|transport/Commuter pass/debit/IDR|3|1068077.02, 1269994.5, 735084.99|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_47|transport/Vehicle charging/debit/IDR|3|1161557.07, 754981.18, 1183026.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_47|transport/Metro and bus fares/debit/IDR|4|1279381.85, 1154111.35, 961791.44, 818855.62|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_47|dining/Weekend food delivery/debit/IDR|3|1888663.82, 1709728.42, 1131260.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_47|dining/Coffee shop/debit/IDR|2|1239585.68, 1599781.09|repeated but not demonstrably recurrent|||
|user_47|dining/Quick-service meal/debit/IDR|2|1791024.46, 1126142.18|repeated but not demonstrably recurrent|||
|user_47|dining/Takeaway order/debit/IDR|2|1178000.19, 1930284.82|repeated but not demonstrably recurrent|||
|user_47|dining/Family dinner/debit/IDR|2|1911185.2, 1444095.01|repeated but not demonstrably recurrent|||
|user_48|salary/Payroll credit/credit/USD|6|81996.72, 81996.72, 81996.72, 81996.72, 81996.72, 81996.72|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_48|rent/Apartment rent transfer/debit/INR|6|25200, 25200, 25200, 25200, 25200, 25200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_48|utilities/Electricity bill/debit/INR|6|5883.7, 5715.18, 5452, 5161.18, 5670.13, 6006.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_48|insurance/Insurance policy payment/debit/INR|6|3460, 3460, 3460, 3460, 3460, 3460|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_48|cloud_storage/Shared storage plan/debit/INR|6|630, 630, 630, 630, 630, 630|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_48|streaming/Streaming subscription/debit/INR|6|1850, 1850, 1850, 1850, 1850, 1850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_48|shopping/Household shopping/debit/INR|6|2326.78, 2712.12, 2788.29, 2750.87, 2327.82, 2936.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_48|entertainment/Weekend entertainment/debit/INR|6|1894.74, 2219.95, 2091.53, 2134.53, 2342.85, 2208.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_48|groceries/Neighbourhood grocer/debit/INR|4|3149.87, 3868.87, 3662.92, 3222.05|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_48|groceries/Supermarket basket/debit/INR|4|2677.94, 2441.22, 3459.86, 3765.67|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_48|groceries/Local market purchase/debit/INR|3|3644.22, 3711.25, 3062.19|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_48|groceries/Weekly produce market/debit/INR|3|3333.99, 2773.86, 2504.07|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_48|groceries/Fresh food shop/debit/INR|2|3153.08, 3604.87|repeated but not demonstrably recurrent|||
|user_48|transport/Commuter pass/debit/INR|6|1691.7, 1816.76, 1723.43, 1540.44, 2072.87, 1584.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_48|transport/Local taxi/debit/INR|5|1966.11, 1476.47, 1218.45, 1733.88, 1755.81|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_48|transport/Metro and bus fares/debit/INR|10|1684.77, 2111.35, 1518.38, 1714.15, 1311.25, 1684.81, 1909.47, 1239.53, 1613.29, 1973.27|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_48|transport/Vehicle charging/debit/INR|4|1978.89, 1832.51, 1849.69, 1991.72|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_48|transport/Fuel refill/debit/INR|4|1605.3, 1489.96, 1348.66, 1964.37|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_48|transport/Rail pass/debit/INR|4|1733.84, 1232.62, 1469.15, 1592.6|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_48|transport/Ride-hailing trip/debit/INR|2|1254.93, 1319.57|repeated but not demonstrably recurrent|||
|user_48|dining/Bakery and snacks/debit/INR|3|3475.46, 4202.49, 4105.91|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_48|dining/Coffee shop/debit/INR|7|3623.63, 3368.92, 3855.96, 3675.8, 4283.79, 2812.75, 2701.42|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_48|dining/Quick-service meal/debit/INR|2|2962.03, 3611.72|repeated but not demonstrably recurrent|||
|user_48|dining/Lunch with colleagues/debit/INR|4|3897.74, 3139.26, 3866.59, 3688.81|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_48|dining/Weekend food delivery/debit/INR|4|4369.13, 3846.44, 3759.79, 3795.19|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_48|dining/Family dinner/debit/INR|4|2747.31, 2964.58, 4334.2, 4069.39|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_49|salary/Payroll credit/credit/IDR|5|43700000, 43700000, 43700000, 31464000, 31464000|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_49|rent/Shared housing rent/debit/IDR|6|9747000, 9747000, 9747000, 9747000, 9747000, 9747000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_49|utilities/Water and power payment/debit/IDR|5|1939160.88, 2202310.34, 1812360.01, 1958058.84, 2279326.25|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_49|music_subscription/Music service subscription/debit/IDR|5|206150, 206150, 206150, 206150, 206150|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_49|delivery_membership/Grocery delivery membership/debit/IDR|5|479750, 479750, 479750, 479750, 479750|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_49|gym/Community fitness plan/debit/IDR|5|737200, 737200, 737200, 737200, 737200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_49|entertainment/Games and recreation/debit/IDR|5|692872.78, 613672.21, 667524.28, 675299.32, 740156.74|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_49|groceries/Household groceries/debit/IDR|3|1238683.25, 1476242.14, 1201037.97|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_49|groceries/Grocery delivery/debit/IDR|5|1590009.53, 1439456.63, 1065790.49, 1560103.7, 1614960.21|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_49|groceries/Bulk pantry shop/debit/IDR|3|1324109.5, 1705196.37, 1546003.29|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_49|groceries/Supermarket basket/debit/IDR|4|1665203.4, 1213419.5, 1530991.93, 1263823.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_49|groceries/Weekly produce market/debit/IDR|5|1741625.34, 1520536.11, 1813662.25, 1157959.16, 1659705.36|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_49|groceries/Local market purchase/debit/IDR|2|1247626.44, 1600001.54|repeated but not demonstrably recurrent|||
|user_49|groceries/Neighbourhood grocer/debit/IDR|3|1743313.01, 1234308.86, 1449278.03|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Vehicle charging/debit/IDR|4|751997.24, 686614.82, 798204.2, 664534.43|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Metro and bus fares/debit/IDR|3|524586.27, 658959.75, 792501.71|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Rail pass/debit/IDR|5|554140.91, 579352.32, 708444.94, 623657.54, 600711.09|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Local taxi/debit/IDR|4|826714.51, 576353.95, 576824.86, 855973.38|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Parking and tolls/debit/IDR|3|682409.51, 720773.15, 676374.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Ride-hailing trip/debit/IDR|4|557666.9, 776642.16, 874816.16, 775429.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_49|transport/Fuel refill/debit/IDR|2|622524.31, 885876.31|repeated but not demonstrably recurrent|||
|user_49|dining/Coffee shop/debit/IDR|3|1362064.22, 1021643.77, 1296343.56|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_49|dining/Lunch with colleagues/debit/IDR|3|1134366.91, 1505248.31, 1160891.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_49|dining/Quick-service meal/debit/IDR|2|1022280.58, 1717169.93|repeated but not demonstrably recurrent|||
|user_49|dining/Neighbourhood restaurant/debit/IDR|2|1440364.38, 1136010.74|repeated but not demonstrably recurrent|||
|user_50|salary/Primary household salary/credit/INR|5|78120, 78120, 78120, 78120, 78120|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_50|salary/Second household income/credit/INR|4|48467.91, 47047.04, 62918.4, 45331.36|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_50|rent/Monthly rent/debit/INR|6|38800, 38800, 38800, 38800, 38800, 38800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_50|utilities/Energy provider bill/debit/INR|5|6574.62, 6204.77, 6857.48, 6157.86, 6542.17|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_50|debt_repayment/Education loan instalment/debit/INR|5|13800, 13800, 13800, 13800, 13800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_50|healthcare/Family healthcare expense/debit/INR|5|6450.99, 5877.66, 5467.16, 6363.57, 5904.1|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_50|family_support/Family support payment/debit/INR|5|9050, 9050, 9050, 9050, 9050|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_50|cloud_storage/Cloud storage plan/debit/INR|5|985, 985, 985, 985, 985|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_50|shopping/Household shopping/debit/INR|5|4505.07, 5116.96, 4833.46, 5255.01, 5108.63|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_50|groceries/Grocery delivery/debit/INR|4|3401.22, 3586.42, 3849.73, 5063.21|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_50|groceries/Household groceries/debit/INR|4|3501.05, 5473.05, 5560.8, 4156.3|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_50|groceries/Supermarket basket/debit/INR|4|3545.22, 5870.11, 3309.83, 4641.37|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_50|groceries/Local market purchase/debit/INR|2|5190.57, 3592.82|repeated but not demonstrably recurrent|||
|user_50|groceries/Neighbourhood grocer/debit/INR|3|5543.41, 4360.43, 5103.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_50|groceries/Weekly produce market/debit/INR|3|5866.67, 4499.55, 4658.19|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_50|groceries/Fresh food shop/debit/INR|5|4962.6, 5312.19, 5011.31, 5754.38, 4169.43|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_50|transport/Fuel refill/debit/INR|3|2926.05, 2851.29, 3423.11|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_50|transport/Metro and bus fares/debit/INR|3|3331.72, 2649.29, 2357.1|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_50|transport/Commuter pass/debit/INR|5|2629.5, 3028.84, 2196.38, 3520.87, 2174.92|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|salary/Driver platform payout/credit/IDR|4|2888167.35, 2326063.43, 3417951.21, 3575977.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|salary/Delivery platform payout/credit/IDR|8|2013905.23, 1957227.41, 2917473.72, 1876077.64, 3215027.74, 3207382.52, 2553078.12, 2038913.81|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|salary/Task marketplace payout/credit/IDR|5|3304136, 3357218.37, 1746918.47, 2646724.54, 1919893.33|variable but recurrent|16|RECURRING_AMOUNT_UNRESOLVED|
|user_51|rent/Residential rent payment/debit/IDR|5|2945000, 2945000, 2945000, 2945000, 2945000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_51|utilities/Water and power payment/debit/IDR|5|764737.03, 769950.17, 650667.31, 782054.34, 740272.53|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_51|music_subscription/Music subscription/debit/IDR|5|112100, 112100, 112100, 112100, 112100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_51|delivery_membership/Food delivery membership/debit/IDR|5|152000, 152000, 152000, 152000, 152000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_51|gym/Gym membership/debit/IDR|5|267900, 267900, 267900, 267900, 267900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_51|entertainment/Monthly entertainment spend/debit/IDR|5|238385.63, 241129.82, 242265.51, 226071.45, 240121.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_51|salary/Weekly app earnings/credit/IDR|3|3613213.16, 2869332.52, 3589888.8|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|groceries/Bulk pantry shop/debit/IDR|4|546466.51, 518705.02, 426067.08, 387800.92|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_51|groceries/Neighbourhood grocer/debit/IDR|4|394985.58, 328906.77, 431119.46, 464372.91|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_51|groceries/Grocery delivery/debit/IDR|6|530914.64, 494498.79, 328029.7, 485498.26, 374608.34, 453198.22|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_51|groceries/Local market purchase/debit/IDR|4|412532.49, 498054.28, 517595.74, 414309.29|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_51|groceries/Weekly produce market/debit/IDR|2|416582.76, 433346.15|repeated but not demonstrably recurrent|||
|user_51|groceries/Supermarket basket/debit/IDR|3|365973.56, 331094.27, 440581.3|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Vehicle charging/debit/IDR|4|163221.8, 248220.4, 192005.79, 271525.47|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Ride-hailing trip/debit/IDR|3|235044.15, 248387.95, 241764.66|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Commuter pass/debit/IDR|3|261857.69, 263530.86, 229897.17|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Local taxi/debit/IDR|4|176159.37, 264387.91, 262924.05, 270837.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Fuel refill/debit/IDR|4|168743.47, 198521.25, 191088.75, 259745.75|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Parking and tolls/debit/IDR|4|186680.91, 268111.56, 183811.02, 195917.62|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_51|transport/Metro and bus fares/debit/IDR|2|175904.89, 197280.64|repeated but not demonstrably recurrent|||
|user_51|dining/Weekend food delivery/debit/IDR|4|435838.46, 525538.38, 443008.24, 447694.16|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_51|dining/Quick-service meal/debit/IDR|2|616580.77, 518939.61|repeated but not demonstrably recurrent|||
|user_51|dining/Neighbourhood restaurant/debit/IDR|2|368692.92, 568020.11|repeated but not demonstrably recurrent|||
|user_52|salary/Previous employer payroll/credit/INR|4|69000, 69000, 69000, 69000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_52|rent/Monthly rent/debit/INR|6|21100, 21100, 21100, 21100, 21100, 21100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_52|utilities/Household utility payment/debit/INR|5|4279.06, 4466.58, 4459.73, 5012.69, 4602.14|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_52|debt_repayment/Loan repayment/debit/INR|5|6850, 6850, 6850, 6850, 6850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_52|music_subscription/Music service subscription/debit/INR|5|440, 440, 440, 440, 440|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_52|groceries/Grocery delivery/debit/INR|4|2260.07, 2306.2, 3687.95, 3243.09|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_52|groceries/Supermarket basket/debit/INR|3|2674.71, 2731.03, 2188.25|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_52|groceries/Bulk pantry shop/debit/INR|2|2886.24, 3225.89|repeated but not demonstrably recurrent|||
|user_52|groceries/Local market purchase/debit/INR|2|2532.29, 3353.99|repeated but not demonstrably recurrent|||
|user_52|transport/Commuter pass/debit/INR|3|1533.36, 1380.34, 1082.17|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_52|transport/Rail pass/debit/INR|2|1602.33, 1530.06|repeated but not demonstrably recurrent|||
|user_52|dining/Weekend food delivery/debit/INR|4|2988.68, 2209.58, 2895.62, 2097.45|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_53|salary/Payroll credit/credit/USD|5|2880, 2880, 2880, 2880, 2880|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_53|rent/Residential rent payment/debit/USD|6|774, 774, 774, 774, 774, 774|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_53|utilities/Water and power payment/debit/USD|6|186.52, 163.57, 163.12, 168.42, 153.43, 162.58|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_53|education/School fee payment/debit/USD|5|169, 169, 169, 169, 169|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_53|debt_repayment/Vehicle loan payment/debit/USD|5|463, 463, 463, 463, 463|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_53|music_subscription/Music subscription/debit/USD|5|36, 36, 36, 36, 36|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_53|delivery_membership/Delivery service plan/debit/USD|5|41, 41, 41, 41, 41|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_53|groceries/Fresh food shop/debit/USD|6|100.5, 88.82, 85.51, 118.84, 137.84, 86.11|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_53|groceries/Local market purchase/debit/USD|2|108.75, 100.87|repeated but not demonstrably recurrent|||
|user_53|groceries/Grocery delivery/debit/USD|3|116.38, 127.54, 108.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_53|groceries/Bulk pantry shop/debit/USD|5|83.46, 138.52, 119.94, 125.07, 111.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_53|groceries/Weekly produce market/debit/USD|6|85.67, 90.59, 95.25, 83.29, 103.23, 90.87|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_53|groceries/Supermarket basket/debit/USD|2|99.97, 105.07|repeated but not demonstrably recurrent|||
|user_53|groceries/Household groceries/debit/USD|2|97.11, 106.56|repeated but not demonstrably recurrent|||
|user_53|transport/Rail pass/debit/USD|6|69.88, 55.44, 62.58, 50.5, 70.7, 43.02|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_53|transport/Local taxi/debit/USD|6|48.02, 44.88, 46.88, 51.24, 50.51, 54.16|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_53|transport/Ride-hailing trip/debit/USD|3|57.49, 65.92, 64.21|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_53|transport/Parking and tolls/debit/USD|2|50.87, 51.48|repeated but not demonstrably recurrent|||
|user_53|transport/Vehicle charging/debit/USD|3|56.74, 57.29, 67.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_53|transport/Commuter pass/debit/USD|4|54.84, 55.86, 55.53, 68.18|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_53|dining/Weekend food delivery/debit/USD|4|108.94, 95.41, 69.95, 83.34|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_53|dining/Neighbourhood restaurant/debit/USD|3|95.81, 66.01, 107.55|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_53|dining/Family dinner/debit/USD|2|68.05, 105.95|repeated but not demonstrably recurrent|||
|user_54|salary/Payroll credit/credit/ZAR|5|33118.8, 33118.8, 33118.8, 33118.8, 33118.8|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_54|housing/Home association fee/debit/ZAR|5|3630, 3630, 3630, 3630, 3630|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_54|utilities/Household utility payment/debit/ZAR|5|2835.58, 2793.05, 3060.44, 2660.37, 3100.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_54|insurance/Vehicle insurance premium/debit/ZAR|5|1168.2, 1168.2, 1168.2, 1168.2, 1168.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_54|healthcare/Clinic payment/debit/ZAR|5|1375.21, 1519.5, 1503.11, 1479.75, 1363.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_54|streaming/Video streaming plan/debit/ZAR|5|860.2, 860.2, 860.2, 860.2, 860.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_54|groceries/Neighbourhood grocer/debit/ZAR|3|2098.94, 1598.81, 2134.94|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_54|groceries/Fresh food shop/debit/ZAR|4|1338.49, 2134.22, 2200.63, 2077.53|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_54|groceries/Grocery delivery/debit/ZAR|3|1838.57, 1742.16, 1687.07|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_54|groceries/Supermarket basket/debit/ZAR|4|1278.7, 1332.61, 1808.38, 1491.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_54|transport/Vehicle charging/debit/ZAR|2|813.7, 1214.5|repeated but not demonstrably recurrent|||
|user_54|transport/Local taxi/debit/ZAR|3|894.6, 970.82, 1210.49|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_54|transport/Fuel refill/debit/ZAR|3|1176.55, 834.23, 1160.58|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_54|transport/Metro and bus fares/debit/ZAR|2|1207.03, 1231.14|repeated but not demonstrably recurrent|||
|user_54|transport/Commuter pass/debit/ZAR|2|1052.49, 1336.48|repeated but not demonstrably recurrent|||
|user_54|dining/Coffee shop/debit/ZAR|3|1224.66, 1239.36, 1971.15|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_54|dining/Quick-service meal/debit/ZAR|2|1307.04, 2065.78|repeated but not demonstrably recurrent|||
|user_54|dining/Takeaway order/debit/ZAR|2|1990.7, 1967.36|repeated but not demonstrably recurrent|||
|user_54|dining/Weekend food delivery/debit/ZAR|2|2061.54, 1461.87|repeated but not demonstrably recurrent|||
|user_55|salary/Payroll credit/credit/INR|5|216000, 216000, 216000, 216000, 216000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_55|rent/Apartment rent transfer/debit/INR|6|54400, 54400, 54400, 54400, 54400, 54400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_55|utilities/Water and power payment/debit/INR|5|13529.34, 14594.03, 13286.23, 12810.93, 15199.62|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_55|debt_repayment/Personal loan payment/debit/INR|5|15550, 15550, 15550, 15550, 15550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_55|streaming/Family streaming plan/debit/INR|5|5240, 5240, 5240, 5240, 5240|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_55|cloud_storage/Online backup subscription/debit/INR|5|855, 855, 855, 855, 855|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_55|shopping/Online retail purchases/debit/INR|5|5973.39, 7021.57, 6320.18, 6359.43, 5898|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_55|groceries/Household groceries/debit/INR|4|11547.05, 9223.8, 8280.78, 7986.73|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_55|groceries/Supermarket basket/debit/INR|2|10423.15, 11116.5|repeated but not demonstrably recurrent|||
|user_55|groceries/Local market purchase/debit/INR|3|12129.43, 7277.92, 7158.29|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_55|groceries/Weekly produce market/debit/INR|2|10118.61, 7713.15|repeated but not demonstrably recurrent|||
|user_55|groceries/Grocery delivery/debit/INR|3|10309.48, 10954.96, 9650.49|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_55|groceries/Neighbourhood grocer/debit/INR|4|11921.2, 7548.48, 7645.77, 8026.49|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_55|groceries/Fresh food shop/debit/INR|5|7600.58, 8734.08, 11847.4, 7301.97, 10792.62|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_55|groceries/Bulk pantry shop/debit/INR|2|9016.64, 7860.56|repeated but not demonstrably recurrent|||
|user_55|transport/Local taxi/debit/INR|2|3660.69, 4519.01|repeated but not demonstrably recurrent|||
|user_55|transport/Commuter pass/debit/INR|7|4964.8, 4321.75, 5769.99, 4441.48, 3618.38, 5985.25, 3475.47|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_55|transport/Rail pass/debit/INR|3|5229.32, 4002.52, 5129.84|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_55|transport/Ride-hailing trip/debit/INR|5|5801.03, 5000.88, 5987.92, 5073.03, 5365.21|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_55|transport/Metro and bus fares/debit/INR|3|5802.39, 4281.81, 4776.4|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_55|transport/Parking and tolls/debit/INR|3|3817.66, 5822.34, 4178.27|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_55|transport/Vehicle charging/debit/INR|2|4584.57, 3581.16|repeated but not demonstrably recurrent|||
|user_55|dining/Quick-service meal/debit/INR|4|5744.44, 5247.78, 5839.62, 5515.86|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_55|dining/Neighbourhood restaurant/debit/INR|2|6496.54, 5462.1|repeated but not demonstrably recurrent|||
|user_55|dining/Lunch with colleagues/debit/INR|2|6144.4, 4324.58|repeated but not demonstrably recurrent|||
|user_55|dining/Bakery and snacks/debit/INR|2|4312.57, 5881.52|repeated but not demonstrably recurrent|||
|user_56|salary/Payroll credit/credit/USD|5|2388, 2388, 2388, 2388, 2388|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_56|housing/Home association fee/debit/USD|6|212, 212, 212, 212, 212, 212|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_56|utilities/Electricity bill/debit/USD|5|111.11, 127.41, 107.12, 121.47, 104.64|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_56|insurance/Insurance policy payment/debit/USD|5|63, 63, 63, 63, 63|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_56|education/Professional training fee/debit/USD|5|207, 207, 207, 207, 207|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_56|healthcare/Diagnostic test/debit/USD|5|113.72, 104.66, 113.94, 119.31, 123.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_56|entertainment/Cinema and events/debit/USD|5|50.53, 52.02, 50.98, 45.43, 49.27|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_56|cloud_storage/Cloud storage plan/debit/USD|5|8, 8, 8, 8, 8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_56|groceries/Fresh food shop/debit/USD|2|84.92, 98.78|repeated but not demonstrably recurrent|||
|user_56|groceries/Neighbourhood grocer/debit/USD|2|78.22, 110.88|repeated but not demonstrably recurrent|||
|user_56|groceries/Household groceries/debit/USD|2|100.55, 101.46|repeated but not demonstrably recurrent|||
|user_56|groceries/Bulk pantry shop/debit/USD|5|70.79, 83.44, 71.37, 77.83, 98.85|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_56|groceries/Local market purchase/debit/USD|3|96.26, 100.5, 115.09|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_56|groceries/Weekly produce market/debit/USD|3|88.2, 99.82, 111.12|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_56|transport/Fuel refill/debit/USD|3|62.46, 50.04, 44.27|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_56|transport/Vehicle charging/debit/USD|3|60.69, 39.17, 38.51|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_56|transport/Local taxi/debit/USD|2|39.36, 52.76|repeated but not demonstrably recurrent|||
|user_56|transport/Rail pass/debit/USD|3|62.62, 41.78, 38.37|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_56|dining/Lunch with colleagues/debit/USD|2|108.25, 107.36|repeated but not demonstrably recurrent|||
|user_56|dining/Coffee shop/debit/USD|2|127.3, 101.29|repeated but not demonstrably recurrent|||
|user_56|dining/Quick-service meal/debit/USD|2|114.21, 89.27|repeated but not demonstrably recurrent|||
|user_57|salary/Payroll credit/credit/ZAR|5|50160, 50160, 50160, 50160, 50160|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_57|rent/Monthly rent/debit/ZAR|6|15004, 15004, 15004, 15004, 15004, 15004|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_57|utilities/Electricity and water bill/debit/ZAR|5|3150.19, 2770.52, 2907.73, 3055.13, 3218.83|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_57|cloud_storage/Cloud storage plan/debit/ZAR|5|325.6, 325.6, 325.6, 325.6, 325.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_57|streaming/Video streaming plan/debit/ZAR|5|1029.6, 1029.6, 1029.6, 1029.6, 1029.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_57|shopping/Clothing and household items/debit/ZAR|5|1639.94, 1971.76, 1580.6, 1602.51, 1916.55|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_57|groceries/Local market purchase/debit/ZAR|3|2252.51, 2743.65, 2066.84|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_57|groceries/Fresh food shop/debit/ZAR|2|1945.94, 2509.7|repeated but not demonstrably recurrent|||
|user_57|groceries/Bulk pantry shop/debit/ZAR|2|2231.88, 2759.62|repeated but not demonstrably recurrent|||
|user_57|groceries/Supermarket basket/debit/ZAR|5|2699.01, 2283.42, 1866.04, 2374.19, 2055.94|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_57|groceries/Household groceries/debit/ZAR|2|1913.1, 2128.24|repeated but not demonstrably recurrent|||
|user_57|groceries/Weekly produce market/debit/ZAR|2|2402.87, 2156.51|repeated but not demonstrably recurrent|||
|user_57|transport/Metro and bus fares/debit/ZAR|2|1099.33, 1527.95|repeated but not demonstrably recurrent|||
|user_57|transport/Ride-hailing trip/debit/ZAR|3|997.54, 1512.58, 1504.58|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_57|dining/Coffee shop/debit/ZAR|2|1472.17, 1352.97|repeated but not demonstrably recurrent|||
|user_57|dining/Weekend food delivery/debit/ZAR|2|1288.98, 1219.19|repeated but not demonstrably recurrent|||
|user_57|dining/Quick-service meal/debit/ZAR|2|1693.82, 1188.36|repeated but not demonstrably recurrent|||
|user_58|salary/Primary household salary/credit/IDR|5|16020800, 16020800, 16020800, 16020800, 16020800|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_58|salary/Second household income/credit/IDR|4|10248053.98, 11104789.08, 12543308.32, 12310253.66|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_58|rent/Landlord standing order/debit/IDR|6|7676000, 7676000, 7676000, 7676000, 7676000, 7676000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_58|utilities/Municipal utilities/debit/IDR|5|1484132.55, 1791244.63, 1580260.82, 1609612.89, 1776974.42|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_58|music_subscription/Music subscription/debit/IDR|5|249850, 249850, 249850, 249850, 249850|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_58|delivery_membership/Food delivery membership/debit/IDR|5|218500, 218500, 218500, 218500, 218500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_58|gym/Community fitness plan/debit/IDR|5|701100, 701100, 701100, 701100, 701100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_58|entertainment/Monthly entertainment spend/debit/IDR|5|690896.88, 792368.31, 692107.38, 811878.97, 800437.48|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_58|groceries/Weekly produce market/debit/IDR|7|1153616.41, 1060071.31, 781629.57, 1135834.58, 724519.58, 765127.37, 724603.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_58|groceries/Neighbourhood grocer/debit/IDR|2|720701.65, 1026599.06|repeated but not demonstrably recurrent|||
|user_58|groceries/Local market purchase/debit/IDR|5|816552.21, 1054790.36, 918126.17, 933496.4, 836783.02|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_58|groceries/Bulk pantry shop/debit/IDR|3|874772.74, 735104.88, 947288.04|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_58|groceries/Fresh food shop/debit/IDR|4|790180.09, 818257.53, 898997.18, 826735.15|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_58|groceries/Supermarket basket/debit/IDR|2|805097.78, 1009523.56|repeated but not demonstrably recurrent|||
|user_58|groceries/Household groceries/debit/IDR|2|1119034.1, 1021287.68|repeated but not demonstrably recurrent|||
|user_58|transport/Commuter pass/debit/IDR|3|728825.49, 605251.94, 584820.91|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_58|transport/Local taxi/debit/IDR|5|505332.36, 691502.17, 627709.38, 454395.39, 728609.56|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_58|transport/Metro and bus fares/debit/IDR|2|637143.47, 454772.65|repeated but not demonstrably recurrent|||
|user_58|transport/Rail pass/debit/IDR|6|461882.7, 448705.76, 730484.06, 741140.69, 646822.3, 513690.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_58|transport/Ride-hailing trip/debit/IDR|5|654795.38, 488358.24, 443068.64, 660776.73, 621999.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_58|transport/Parking and tolls/debit/IDR|2|445298.26, 684983.63|repeated but not demonstrably recurrent|||
|user_58|dining/Neighbourhood restaurant/debit/IDR|4|743460.86, 742936.04, 1051845.26, 999175.38|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_58|dining/Coffee shop/debit/IDR|3|1000375.17, 889358.12, 1046558.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_58|dining/Family dinner/debit/IDR|3|951924.39, 714462.14, 788752.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_59|salary/Task marketplace payout/credit/INR|5|62459.05, 43456.15, 64269.78, 42321.15, 56448.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_59|salary/Delivery platform payout/credit/INR|4|66700.14, 65199.81, 65795.24, 34644.22|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_59|salary/Driver platform payout/credit/INR|3|65917.02, 36019.49, 59413.99|variable but recurrent|55|RECURRING_AMOUNT_UNRESOLVED|
|user_59|salary/Weekly app earnings/credit/INR|8|37928.9, 49704.62, 48024.99, 47596.18, 65095.75, 34537.14, 33571.89, 58200.21|variable but recurrent|17|RECURRING_AMOUNT_UNRESOLVED|
|user_59|rent/Monthly rent/debit/INR|5|53800, 53800, 53800, 53800, 53800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_59|utilities/Electricity and water bill/debit/INR|5|11566.1, 10794.07, 9900.11, 10418.38, 10142.38|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_59|music_subscription/Music subscription/debit/INR|5|2780, 2780, 2780, 2780, 2780|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_59|delivery_membership/Delivery service plan/debit/INR|5|2660, 2660, 2660, 2660, 2660|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_59|gym/Fitness club membership/debit/INR|5|4940, 4940, 4940, 4940, 4940|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_59|entertainment/Monthly entertainment spend/debit/INR|5|5170.02, 5062.72, 5095.71, 4872.04, 4598.72|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_59|groceries/Bulk pantry shop/debit/INR|3|8617.16, 7641.49, 8471.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_59|groceries/Fresh food shop/debit/INR|2|7455.25, 10012.25|repeated but not demonstrably recurrent|||
|user_59|groceries/Grocery delivery/debit/INR|4|8369.65, 7881.49, 7877.04, 9338.57|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_59|groceries/Weekly produce market/debit/INR|4|8004.19, 8261.77, 8776.91, 9335.44|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_59|groceries/Neighbourhood grocer/debit/INR|3|6452.83, 6054.84, 10628.01|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_59|groceries/Household groceries/debit/INR|2|10507.15, 8431.66|repeated but not demonstrably recurrent|||
|user_59|groceries/Local market purchase/debit/INR|6|8553.28, 6533.88, 7228.22, 6666.07, 6945.84, 9266.04|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_59|transport/Local taxi/debit/INR|3|4724.17, 4840.24, 4113.55|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_59|transport/Vehicle charging/debit/INR|7|4106.84, 5360.39, 3496.33, 5364.06, 3441.77, 5089.71, 5475.4|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_59|transport/Commuter pass/debit/INR|3|5490.97, 3579.3, 5047.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_59|transport/Ride-hailing trip/debit/INR|4|4476.41, 5380.97, 5205.47, 5236.78|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_59|transport/Fuel refill/debit/INR|2|4757.81, 4058.87|repeated but not demonstrably recurrent|||
|user_59|transport/Parking and tolls/debit/INR|4|3959.18, 4904.12, 4014.41, 3705.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_59|transport/Rail pass/debit/INR|2|4536.4, 4070.27|repeated but not demonstrably recurrent|||
|user_59|dining/Neighbourhood restaurant/debit/INR|5|8142.25, 9453.87, 8052.22, 7525.78, 7043.41|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_59|dining/Quick-service meal/debit/INR|3|8426.41, 6686.86, 8503.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_60|salary/Payroll credit/credit/USD|5|530.4, 530.4, 530.4, 530.4, 291.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_60|rent/Apartment rent transfer/debit/USD|6|122.4, 122.4, 122.4, 122.4, 122.4, 122.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_60|utilities/Electricity and water bill/debit/USD|6|40.96, 38.5, 34.61, 36.89, 32.59, 37.75|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_60|insurance/Household insurance/debit/USD|5|18, 18, 18, 18, 18|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_60|cloud_storage/Online backup subscription/debit/USD|5|3, 3, 3, 3, 3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_60|streaming/Video streaming plan/debit/USD|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_60|shopping/Clothing and household items/debit/USD|5|20.9, 19.39, 17.27, 19.31, 16.75|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_60|entertainment/Local event tickets/debit/USD|5|14.75, 14.91, 14.29, 12.43, 15.49|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_60|groceries/Local market purchase/debit/USD|2|17.19, 20.64|repeated but not demonstrably recurrent|||
|user_60|groceries/Weekly produce market/debit/USD|4|19.08, 15.12, 21.16, 16.42|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_60|groceries/Grocery delivery/debit/USD|2|14.8, 20.88|repeated but not demonstrably recurrent|||
|user_60|groceries/Bulk pantry shop/debit/USD|3|24.35, 17.74, 19.89|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_60|groceries/Fresh food shop/debit/USD|4|20.54, 19, 21.72, 22.91|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Vehicle charging/debit/USD|6|13.87, 13.36, 16.48, 10.35, 14.73, 15.11|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Rail pass/debit/USD|5|13.56, 10.5, 16.53, 15.65, 10.96|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Fuel refill/debit/USD|5|17.1, 13.02, 16.65, 12.7, 14.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Ride-hailing trip/debit/USD|2|11.64, 13.67|repeated but not demonstrably recurrent|||
|user_60|transport/Commuter pass/debit/USD|6|11.77, 10.77, 11, 15.16, 15.96, 16.1|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Parking and tolls/debit/USD|6|16.76, 12.94, 14.74, 16.48, 15.98, 16.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Local taxi/debit/USD|4|15.12, 15.95, 12.68, 12.84|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_60|transport/Metro and bus fares/debit/USD|2|14.24, 12.89|repeated but not demonstrably recurrent|||
|user_60|dining/Family dinner/debit/USD|6|17.16, 16.38, 15.66, 23.81, 24.47, 18.07|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_60|dining/Takeaway order/debit/USD|3|17.06, 15.43, 16.81|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_60|dining/Quick-service meal/debit/USD|3|20.98, 20.81, 23.77|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_60|dining/Lunch with colleagues/debit/USD|2|24.34, 15.27|repeated but not demonstrably recurrent|||
|user_60|dining/Neighbourhood restaurant/debit/USD|5|14.83, 15.78, 16.76, 20.41, 18.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_60|dining/Bakery and snacks/debit/USD|2|19.42, 16.69|repeated but not demonstrably recurrent|||
|user_60|dining/Weekend food delivery/debit/USD|3|16.84, 21.99, 22.18|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_60|dining/Coffee shop/debit/USD|2|23.78, 22.39|repeated but not demonstrably recurrent|||
|user_61|rent/Landlord standing order/debit/ZAR|6|11792, 11792, 11792, 11792, 11792, 11792|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_61|utilities/Household utility payment/debit/ZAR|5|2539.9, 2676.42, 2538.35, 2474.01, 2215.99|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_61|debt_repayment/Credit card repayment/debit/ZAR|5|7161, 7161, 7161, 7161, 7161|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_61|music_subscription/Music service subscription/debit/ZAR|5|305.8, 305.8, 305.8, 305.8, 305.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_61|salary/Temporary assignment pay/credit/ZAR|2|44313.68, 51511.04|repeated but not demonstrably recurrent|||
|user_61|groceries/Grocery delivery/debit/ZAR|5|1786.46, 2016.05, 1863.22, 1856.8, 1598.65|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_61|groceries/Household groceries/debit/ZAR|2|1903.83, 2171.19|repeated but not demonstrably recurrent|||
|user_61|groceries/Fresh food shop/debit/ZAR|2|1535.04, 2019.03|repeated but not demonstrably recurrent|||
|user_61|groceries/Neighbourhood grocer/debit/ZAR|3|1684.42, 1960.6, 1404.06|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_61|transport/Ride-hailing trip/debit/ZAR|3|1071.51, 1307.41, 1359.89|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_61|transport/Rail pass/debit/ZAR|2|1170.64, 1437.33|repeated but not demonstrably recurrent|||
|user_61|dining/Bakery and snacks/debit/ZAR|2|1778.44, 1908.87|repeated but not demonstrably recurrent|||
|user_61|dining/Quick-service meal/debit/ZAR|3|1751.43, 1600.05, 1188.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_61|dining/Neighbourhood restaurant/debit/ZAR|2|1800.21, 1715.22|repeated but not demonstrably recurrent|||
|user_62|rent/Monthly rent/debit/USD|6|530.4, 530.4, 530.4, 530.4, 530.4, 530.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_62|utilities/Energy provider bill/debit/USD|5|113.14, 124.31, 106.31, 124.55, 124.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_62|cloud_storage/Online backup subscription/debit/USD|5|11, 11, 11, 11, 11|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_62|streaming/Streaming subscription/debit/USD|5|42, 42, 42, 42, 42|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_62|shopping/Clothing and household items/debit/USD|5|62.63, 59.08, 70.68, 62.15, 72.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_62|salary/Independent work payment/credit/USD|2|911.13, 1237.03|repeated but not demonstrably recurrent|||
|user_62|salary/Website project payment/credit/USD|3|703.09, 1285.77, 727.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_62|salary/Client retainer payment/credit/USD|2|563.41, 912.27|repeated but not demonstrably recurrent|||
|user_62|groceries/Supermarket basket/debit/USD|2|66.61, 92.58|repeated but not demonstrably recurrent|||
|user_62|groceries/Neighbourhood grocer/debit/USD|3|88.05, 110.98, 110.84|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_62|groceries/Bulk pantry shop/debit/USD|5|78.57, 100.56, 64.55, 108.68, 78.26|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_62|groceries/Weekly produce market/debit/USD|3|93.43, 73.61, 106.08|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_62|groceries/Grocery delivery/debit/USD|2|80.75, 111.76|repeated but not demonstrably recurrent|||
|user_62|transport/Parking and tolls/debit/USD|3|45.26, 49.37, 41.41|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_62|transport/Fuel refill/debit/USD|2|31.62, 37.11|repeated but not demonstrably recurrent|||
|user_62|dining/Quick-service meal/debit/USD|3|110.63, 110.4, 95.88|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_62|dining/Bakery and snacks/debit/USD|2|77.93, 96.14|repeated but not demonstrably recurrent|||
|user_62|dining/Neighbourhood restaurant/debit/USD|2|120.58, 100.53|repeated but not demonstrably recurrent|||
|user_62|dining/Family dinner/debit/USD|2|109, 111.43|repeated but not demonstrably recurrent|||
|user_63|salary/Payroll credit/credit/USD|5|189992.40, 189992.40, 189992.40, 189992.40, 189992.40|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_63|rent/Monthly rent/debit/INR|6|50000, 50000, 50000, 50000, 50000, 50000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_63|utilities/Water and power payment/debit/INR|5|10629.37, 11012.72, 10427.62, 11575.24, 9613.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_63|insurance/Insurance policy payment/debit/INR|5|6720, 6720, 6720, 6720, 6720|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_63|cloud_storage/Online backup subscription/debit/INR|5|585, 585, 585, 585, 585|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_63|streaming/Family streaming plan/debit/INR|5|4830, 4830, 4830, 4830, 4830|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_63|shopping/Clothing and household items/debit/INR|5|7882.99, 7439.52, 8038.75, 7552.58, 7886.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_63|entertainment/Games and recreation/debit/INR|5|4881.96, 5596.18, 5290.79, 4928.32, 5081.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_63|groceries/Local market purchase/debit/INR|2|8244.22, 7914.01|repeated but not demonstrably recurrent|||
|user_63|groceries/Bulk pantry shop/debit/INR|5|6816.41, 6806.41, 7751.96, 7183.12, 5505.78|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_63|groceries/Household groceries/debit/INR|4|6470.09, 7968.05, 5364.31, 7799.21|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_63|groceries/Grocery delivery/debit/INR|3|7024.29, 4913.15, 4909.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Fuel refill/debit/INR|6|3491.5, 5261.88, 3944.47, 3581.65, 4833.74, 4939.58|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Metro and bus fares/debit/INR|6|3016.1, 5145.52, 3781.78, 5235.35, 3769.64, 3152.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Parking and tolls/debit/INR|6|3178.09, 4130.62, 4769.22, 3217.55, 3808.35, 4044.35|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Rail pass/debit/INR|3|3356.65, 3806.72, 3805.05|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Local taxi/debit/INR|3|3832.04, 3761, 4612.83|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Vehicle charging/debit/INR|5|3166.16, 4783.4, 5147.53, 5202.63, 3883.31|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Commuter pass/debit/INR|4|4028.24, 3531.2, 5198.92, 3946.26|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_63|transport/Ride-hailing trip/debit/INR|2|4946.08, 5031.44|repeated but not demonstrably recurrent|||
|user_63|dining/Quick-service meal/debit/INR|2|7431.52, 8259.28|repeated but not demonstrably recurrent|||
|user_63|dining/Coffee shop/debit/INR|5|5616.46, 7208.49, 7248.76, 7753.25, 8738.44|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_63|dining/Family dinner/debit/INR|3|7865.79, 6019.88, 8356.9|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_63|dining/Weekend food delivery/debit/INR|2|7532.06, 6058.71|repeated but not demonstrably recurrent|||
|user_63|dining/Takeaway order/debit/INR|4|8059.46, 7954.94, 7570.91, 6161.34|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_63|dining/Bakery and snacks/debit/INR|4|5949.17, 8394.37, 6947.91, 5792.84|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_63|dining/Lunch with colleagues/debit/INR|3|8064.5, 5566.37, 8083.93|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_63|dining/Neighbourhood restaurant/debit/INR|3|6029.18, 6281.89, 6327.59|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_64|salary/Payroll credit/credit/USD|5|54997.80, 54997.80, 54997.80, 54997.80, 54997.80|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_64|rent/Landlord standing order/debit/INR|6|12800, 12800, 12800, 12800, 12800, 12800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_64|utilities/Household utility payment/debit/INR|5|3503.05, 3177.14, 3170.43, 3839.55, 3699.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_64|insurance/Insurance policy payment/debit/INR|5|1460, 1460, 1460, 1460, 1460|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_64|cloud_storage/Online backup subscription/debit/INR|5|380, 380, 380, 380, 380|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_64|streaming/Family streaming plan/debit/INR|5|1060, 1060, 1060, 1060, 1060|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_64|shopping/Household shopping/debit/INR|5|2635.53, 2989.57, 3303.46, 3196.96, 3269.08|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_64|entertainment/Weekend entertainment/debit/INR|5|2043.65, 2041.44, 2006.74, 2012.98, 2122.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_64|groceries/Local market purchase/debit/INR|2|2566.36, 2191.83|repeated but not demonstrably recurrent|||
|user_64|groceries/Neighbourhood grocer/debit/INR|4|2532.74, 2275.63, 1710.02, 2672.83|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_64|groceries/Supermarket basket/debit/INR|2|2933.91, 1740.85|repeated but not demonstrably recurrent|||
|user_64|groceries/Bulk pantry shop/debit/INR|3|2791.08, 2619.78, 2859.71|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_64|groceries/Fresh food shop/debit/INR|4|2719.19, 1689.2, 1918.57, 2880.68|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_64|groceries/Grocery delivery/debit/INR|2|1972.4, 2679.13|repeated but not demonstrably recurrent|||
|user_64|transport/Metro and bus fares/debit/INR|8|1092.93, 951.17, 1240.53, 1440.24, 1363.82, 1088.08, 1437.06, 1135.79|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_64|transport/Vehicle charging/debit/INR|8|1395.27, 935.78, 1173.14, 1065.35, 1062.78, 859.63, 935.06, 1083.41|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_64|transport/Fuel refill/debit/INR|2|1295.79, 1048.17|repeated but not demonstrably recurrent|||
|user_64|transport/Ride-hailing trip/debit/INR|3|1283.54, 902.25, 1085.08|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_64|transport/Rail pass/debit/INR|2|1201.79, 837.43|repeated but not demonstrably recurrent|||
|user_64|transport/Parking and tolls/debit/INR|7|1132.4, 1356.57, 1079.93, 1030.84, 1163.15, 1386.76, 886.57|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_64|transport/Local taxi/debit/INR|3|1187.2, 1233.83, 1096.93|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_64|transport/Commuter pass/debit/INR|3|1462.76, 910.2, 1042.47|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_64|dining/Family dinner/debit/INR|4|1451.51, 1496.12, 1836, 1621.05|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_64|dining/Weekend food delivery/debit/INR|2|1501.29, 1126.83|repeated but not demonstrably recurrent|||
|user_64|dining/Lunch with colleagues/debit/INR|2|1232.86, 1277.94|repeated but not demonstrably recurrent|||
|user_64|dining/Coffee shop/debit/INR|2|1752.89, 1760.41|repeated but not demonstrably recurrent|||
|user_64|dining/Neighbourhood restaurant/debit/INR|3|1158.79, 1652.22, 1651.4|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_64|dining/Bakery and snacks/debit/INR|7|1185.22, 1426.05, 1161.78, 1238.34, 1093.26, 1796.32, 1090.24|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_64|dining/Takeaway order/debit/INR|2|1639.34, 1160.62|repeated but not demonstrably recurrent|||
|user_64|dining/Quick-service meal/debit/INR|4|1556.37, 1852.03, 1144.29, 1166.25|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_65|salary/Payroll credit/credit/ZAR|5|22220, 22220, 22220, 22220, 22220|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_65|housing/Home association fee/debit/ZAR|6|2519, 2519, 2519, 2519, 2519, 2519|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_65|utilities/Electricity and water bill/debit/ZAR|5|1165.24, 1168.11, 1270.04, 1137.69, 1244.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_65|insurance/Insurance policy payment/debit/ZAR|5|739.2, 739.2, 739.2, 739.2, 739.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_65|education/Professional training fee/debit/ZAR|5|1465.2, 1465.2, 1465.2, 1465.2, 1465.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_65|healthcare/Therapy appointment/debit/ZAR|5|1390.65, 1339.59, 1473.07, 1462.01, 1538.45|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_65|entertainment/Cinema and events/debit/ZAR|5|660.34, 797.15, 822.9, 779.41, 791.97|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_65|cloud_storage/Shared storage plan/debit/ZAR|5|129.8, 129.8, 129.8, 129.8, 129.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_65|groceries/Fresh food shop/debit/ZAR|4|839.15, 993.69, 931.29, 625.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_65|groceries/Neighbourhood grocer/debit/ZAR|3|1088.46, 888.26, 816.24|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_65|groceries/Supermarket basket/debit/ZAR|2|711.7, 1051.66|repeated but not demonstrably recurrent|||
|user_65|groceries/Grocery delivery/debit/ZAR|5|720.45, 910.69, 952.89, 843.28, 676.83|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_65|transport/Ride-hailing trip/debit/ZAR|3|665.01, 575.06, 409.47|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_65|transport/Commuter pass/debit/ZAR|2|523.5, 510.76|repeated but not demonstrably recurrent|||
|user_65|transport/Local taxi/debit/ZAR|3|638.62, 491.61, 653.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_65|dining/Family dinner/debit/ZAR|4|683.2, 1041.85, 826.19, 832.94|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_65|dining/Takeaway order/debit/ZAR|2|702.26, 754.58|repeated but not demonstrably recurrent|||
|user_66|rent/Apartment rent transfer/debit/INR|5|26300, 26300, 26300, 26300, 26300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_66|utilities/Municipal utilities/debit/INR|5|5079.84, 6267.73, 5612.49, 6255.6, 5776|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_66|cloud_storage/Cloud storage plan/debit/INR|5|420, 420, 420, 420, 420|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_66|streaming/Video streaming plan/debit/INR|5|2520, 2520, 2520, 2520, 2520|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_66|shopping/Online retail purchases/debit/INR|5|4429, 4825.86, 4938.86, 4615.97, 4477.83|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_66|salary/Consulting invoice payment/credit/INR|4|44394.3, 40297.18, 67978.07, 38872.32|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_66|salary/Content contract payment/credit/INR|2|53966.1, 47090.56|repeated but not demonstrably recurrent|||
|user_66|salary/Application project payment/credit/INR|2|38124.12, 64555.84|repeated but not demonstrably recurrent|||
|user_66|groceries/Supermarket basket/debit/INR|2|4314.19, 5057.03|repeated but not demonstrably recurrent|||
|user_66|groceries/Grocery delivery/debit/INR|2|6375.01, 5267.36|repeated but not demonstrably recurrent|||
|user_66|groceries/Neighbourhood grocer/debit/INR|3|5311.94, 6116.35, 4005.53|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_66|groceries/Bulk pantry shop/debit/INR|4|5844.47, 5016.01, 5530.59, 4310.76|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_66|groceries/Fresh food shop/debit/INR|3|4266.59, 6518.74, 3881|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_66|groceries/Household groceries/debit/INR|2|4862.58, 4354.36|repeated but not demonstrably recurrent|||
|user_66|transport/Metro and bus fares/debit/INR|2|2733.48, 2057.33|repeated but not demonstrably recurrent|||
|user_66|transport/Local taxi/debit/INR|3|2516.55, 2742.45, 2719.67|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_66|dining/Neighbourhood restaurant/debit/INR|4|4056.11, 4893.47, 4329.1, 4427.74|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_66|dining/Bakery and snacks/debit/INR|2|4648.88, 4740.02|repeated but not demonstrably recurrent|||
|user_67|salary/Payroll credit/credit/USD|5|2844, 2844, 2844, 2047.68, 2047.68|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_67|rent/Monthly rent/debit/USD|6|514.8, 514.8, 514.8, 514.8, 514.8, 514.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_67|utilities/Electricity and water bill/debit/USD|5|104.89, 121.05, 117.09, 128.02, 115.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_67|music_subscription/Music service subscription/debit/USD|5|27, 27, 27, 27, 27|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_67|delivery_membership/Delivery service plan/debit/USD|5|18, 18, 18, 18, 18|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_67|gym/Community fitness plan/debit/USD|5|41, 41, 41, 41, 41|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_67|entertainment/Games and recreation/debit/USD|5|66.18, 67.72, 63.95, 64.31, 64.39|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Local market purchase/debit/USD|3|74.47, 87.43, 77.76|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Fresh food shop/debit/USD|3|80.24, 92.43, 87.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Bulk pantry shop/debit/USD|3|94.14, 61.22, 79.69|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Household groceries/debit/USD|3|57.06, 65.98, 87.83|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Neighbourhood grocer/debit/USD|3|66.73, 90.37, 67.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Supermarket basket/debit/USD|3|65.51, 86.48, 63.38|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Grocery delivery/debit/USD|4|73.3, 69.37, 68.63, 61.74|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_67|groceries/Weekly produce market/debit/USD|3|78.21, 76.84, 74.3|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_67|transport/Vehicle charging/debit/USD|8|35.53, 38.96, 49.58, 45.94, 31.5, 48.23, 36.31, 29.56|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_67|transport/Rail pass/debit/USD|5|31.38, 49.54, 40.48, 47.48, 41.99|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_67|transport/Parking and tolls/debit/USD|2|39.82, 38.84|repeated but not demonstrably recurrent|||
|user_67|transport/Metro and bus fares/debit/USD|6|48.21, 44.48, 49.75, 46.39, 47.17, 33.41|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_67|transport/Local taxi/debit/USD|2|34.08, 39.25|repeated but not demonstrably recurrent|||
|user_67|dining/Bakery and snacks/debit/USD|2|79.55, 98|repeated but not demonstrably recurrent|||
|user_67|dining/Lunch with colleagues/debit/USD|3|73.81, 57.22, 97.14|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_67|dining/Takeaway order/debit/USD|2|59.38, 62.92|repeated but not demonstrably recurrent|||
|user_67|dining/Family dinner/debit/USD|4|72.27, 60.72, 61.72, 61.31|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_68|salary/Payroll credit/credit/USD|5|2496, 2496, 2496, 2496, 2496|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_68|rent/Apartment rent transfer/debit/USD|6|750, 750, 750, 750, 750, 750|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_68|utilities/Municipal utilities/debit/USD|6|176.05, 181.59, 153.66, 145.47, 181.31, 151.01|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_68|debt_repayment/Vehicle loan payment/debit/USD|5|178, 178, 178, 178, 178|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_68|healthcare/Clinic payment/debit/USD|5|116.15, 108.71, 109.57, 117.43, 108.25|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_68|family_support/Childcare contribution/debit/USD|5|173, 173, 173, 173, 173|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_68|cloud_storage/Online backup subscription/debit/USD|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_68|shopping/Household shopping/debit/USD|5|66.23, 56.41, 57.32, 62.92, 57.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_68|groceries/Household groceries/debit/USD|5|96.54, 122.94, 126.19, 87.56, 122.35|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_68|groceries/Weekly produce market/debit/USD|3|98.6, 98.1, 122.24|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_68|groceries/Supermarket basket/debit/USD|5|99.34, 82.55, 127.96, 132.85, 137.4|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_68|groceries/Grocery delivery/debit/USD|2|130.8, 118.12|repeated but not demonstrably recurrent|||
|user_68|groceries/Fresh food shop/debit/USD|4|97.8, 92.74, 138.37, 138.16|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_68|groceries/Neighbourhood grocer/debit/USD|3|93.08, 101.58, 106.62|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_68|groceries/Bulk pantry shop/debit/USD|3|85.58, 125.38, 93.93|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_68|transport/Local taxi/debit/USD|2|70.19, 64.93|repeated but not demonstrably recurrent|||
|user_68|transport/Commuter pass/debit/USD|4|81.5, 77.4, 60.36, 81.58|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_68|transport/Rail pass/debit/USD|3|50.42, 67.35, 53.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_68|transport/Metro and bus fares/debit/USD|2|71.12, 74.72|repeated but not demonstrably recurrent|||
|user_69|salary/Payroll credit/credit/EUR|5|1177, 1177, 1177, 1177, 1177|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_69|rent/Monthly rent/debit/EUR|6|388.3, 388.3, 388.3, 388.3, 388.3, 388.3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_69|utilities/Energy provider bill/debit/EUR|5|78.88, 74.92, 70.38, 84.39, 78.57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_69|debt_repayment/Credit card repayment/debit/EUR|5|121, 121, 121, 121, 121|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_69|streaming/Family streaming plan/debit/EUR|5|24, 24, 24, 24, 24|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_69|cloud_storage/Online backup subscription/debit/EUR|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_69|shopping/Personal shopping/debit/EUR|5|42.01, 42.89, 38.19, 40.49, 42.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_69|groceries/Local market purchase/debit/EUR|5|42.28, 39.2, 42.15, 37.73, 47.9|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_69|groceries/Bulk pantry shop/debit/EUR|6|35.35, 37.69, 50.07, 38.01, 45.77, 43.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_69|groceries/Grocery delivery/debit/EUR|2|42.86, 40.07|repeated but not demonstrably recurrent|||
|user_69|groceries/Fresh food shop/debit/EUR|4|52.92, 47.22, 36.39, 33.49|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_69|groceries/Neighbourhood grocer/debit/EUR|2|40.18, 35.32|repeated but not demonstrably recurrent|||
|user_69|groceries/Weekly produce market/debit/EUR|6|49.59, 40.61, 49.49, 48.66, 37.19, 53.56|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_69|transport/Commuter pass/debit/EUR|5|24.78, 34.79, 24.9, 35.79, 30.6|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_69|transport/Ride-hailing trip/debit/EUR|5|24.72, 25.54, 30.56, 23.4, 25.49|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_69|transport/Vehicle charging/debit/EUR|2|39.32, 25.65|repeated but not demonstrably recurrent|||
|user_69|transport/Local taxi/debit/EUR|3|32.3, 37.32, 24.69|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_69|transport/Metro and bus fares/debit/EUR|3|32.33, 35.43, 25.36|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_69|transport/Rail pass/debit/EUR|4|22.97, 25.89, 28.48, 23.97|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_69|transport/Fuel refill/debit/EUR|2|38.57, 30.3|repeated but not demonstrably recurrent|||
|user_69|transport/Parking and tolls/debit/EUR|2|24.61, 37.35|repeated but not demonstrably recurrent|||
|user_69|dining/Quick-service meal/debit/EUR|3|48.83, 30.25, 41.84|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_69|dining/Weekend food delivery/debit/EUR|4|47.29, 33.68, 43.49, 35.59|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_69|dining/Lunch with colleagues/debit/EUR|2|50.72, 41.62|repeated but not demonstrably recurrent|||
|user_69|dining/Family dinner/debit/EUR|2|38.85, 46.54|repeated but not demonstrably recurrent|||
|user_70|salary/Payroll credit/credit/INR|5|203000, 203000, 203000, 203000, 203000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_70|rent/Landlord standing order/debit/INR|6|66100, 66100, 66100, 66100, 66100, 66100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_70|utilities/Electricity bill/debit/INR|5|11446.37, 11373.53, 11534.19, 12364.52, 12717.79|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_70|debt_repayment/Education loan instalment/debit/INR|5|18750, 18750, 18750, 18750, 18750|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_70|music_subscription/Audio streaming plan/debit/INR|5|1940, 1940, 1940, 1940, 1940|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_70|groceries/Local market purchase/debit/INR|4|11730.16, 9404.04, 9360.53, 8132.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_70|groceries/Weekly produce market/debit/INR|2|11478.06, 11723.03|repeated but not demonstrably recurrent|||
|user_70|groceries/Neighbourhood grocer/debit/INR|2|7598.12, 11360.93|repeated but not demonstrably recurrent|||
|user_70|groceries/Household groceries/debit/INR|3|8409.56, 11669.37, 10762.2|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_70|transport/Rail pass/debit/INR|3|3517.31, 3299.84, 3304.29|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_70|transport/Parking and tolls/debit/INR|3|3421.7, 4551.25, 4344.3|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_70|transport/Metro and bus fares/debit/INR|2|2917.8, 4260.75|repeated but not demonstrably recurrent|||
|user_70|dining/Neighbourhood restaurant/debit/INR|2|7939, 6224.22|repeated but not demonstrably recurrent|||
|user_70|dining/Weekend food delivery/debit/INR|3|6003.02, 7106.49, 6603.29|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_70|dining/Lunch with colleagues/debit/INR|3|7724.19, 8218.34, 6861.9|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_71|salary/International employer payroll/credit/USD|5|11019997.68, 11019997.68, 11019997.68, 11019997.68, 11019997.68|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_71|rent/Apartment rent transfer/debit/IDR|5|3648000, 3648000, 3648000, 3648000, 3648000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_71|utilities/Energy provider bill/debit/IDR|5|730154.23, 728596.19, 761942.18, 647373.55, 775045.22|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_71|insurance/Health insurance premium/debit/IDR|5|286900, 286900, 286900, 286900, 286900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_71|cloud_storage/Cloud storage plan/debit/IDR|5|57950, 57950, 57950, 57950, 57950|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_71|streaming/Streaming subscription/debit/IDR|5|207100, 207100, 207100, 207100, 207100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_71|shopping/Household shopping/debit/IDR|5|346380.03, 351876.2, 300830.9, 303838.17, 337205.75|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_71|entertainment/Weekend entertainment/debit/IDR|5|356863.2, 412818.13, 400538.29, 393224.83, 414853.49|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_71|groceries/Weekly produce market/debit/IDR|5|489109.13, 561694.5, 609976.36, 508419.18, 623202.22|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_71|groceries/Grocery delivery/debit/IDR|4|436323.9, 472173.57, 394014.92, 650694.31|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_71|groceries/Supermarket basket/debit/IDR|2|418652.55, 563385.33|repeated but not demonstrably recurrent|||
|user_71|groceries/Bulk pantry shop/debit/IDR|2|434349.35, 449983.14|repeated but not demonstrably recurrent|||
|user_71|groceries/Neighbourhood grocer/debit/IDR|2|444496.36, 560407.68|repeated but not demonstrably recurrent|||
|user_71|transport/Parking and tolls/debit/IDR|2|273287.35, 235676.62|repeated but not demonstrably recurrent|||
|user_71|transport/Ride-hailing trip/debit/IDR|6|270058.98, 237396.13, 263255.07, 285073.18, 243167.46, 270464.28|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_71|transport/Local taxi/debit/IDR|4|216146.29, 253003.91, 277789.03, 221169.29|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_71|transport/Metro and bus fares/debit/IDR|5|242248.04, 237979.08, 245267.88, 267112.11, 245204.49|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_71|transport/Fuel refill/debit/IDR|6|296613.83, 184697.24, 189307.39, 240331.78, 272576.52, 314728.69|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_71|transport/Rail pass/debit/IDR|4|313488.52, 199147.98, 187232.95, 266131.08|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_71|transport/Vehicle charging/debit/IDR|4|254019.64, 293845.06, 198600.59, 196780.49|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_71|transport/Commuter pass/debit/IDR|4|197878.57, 265266.4, 275349, 264138.97|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Bakery and snacks/debit/IDR|3|365101.08, 410867, 289944.75|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Coffee shop/debit/IDR|6|418221.47, 316478.24, 257385.02, 431965.14, 272780.99, 345313.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Weekend food delivery/debit/IDR|3|345421.52, 380468.3, 355845.81|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Takeaway order/debit/IDR|4|432395.84, 366737.25, 401754.75, 268202.35|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Lunch with colleagues/debit/IDR|2|250886.29, 393195.12|repeated but not demonstrably recurrent|||
|user_71|dining/Quick-service meal/debit/IDR|3|352077.58, 380087.16, 361631.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Neighbourhood restaurant/debit/IDR|3|433624.8, 361888.47, 316664.03|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_71|dining/Family dinner/debit/IDR|2|412325.59, 420526.78|repeated but not demonstrably recurrent|||
|user_72|rent/Apartment rent transfer/debit/ZAR|6|4312, 4312, 4312, 4312, 4312, 4312|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_72|utilities/Electricity bill/debit/ZAR|5|1284.83, 1170.17, 1089.41, 1183.46, 1039.01|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_72|education/Professional training fee/debit/ZAR|5|2004.2, 2004.2, 2004.2, 2004.2, 2004.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_72|debt_repayment/Loan repayment/debit/ZAR|5|1210, 1210, 1210, 1210, 1210|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_72|music_subscription/Music subscription/debit/ZAR|5|134.2, 134.2, 134.2, 134.2, 134.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_72|delivery_membership/Delivery service plan/debit/ZAR|5|136.4, 136.4, 136.4, 136.4, 136.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_72|salary/First-job payroll/credit/ZAR|2|18700, 18700|repeated but not demonstrably recurrent|||
|user_72|groceries/Neighbourhood grocer/debit/ZAR|5|838.89, 702.94, 544.04, 546.98, 712|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_72|groceries/Supermarket basket/debit/ZAR|3|737.35, 855.99, 782.06|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_72|groceries/Household groceries/debit/ZAR|4|831, 712.3, 504.2, 586.78|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_72|groceries/Local market purchase/debit/ZAR|4|704.44, 834.29, 781.83, 853.56|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_72|groceries/Grocery delivery/debit/ZAR|4|727.21, 843.77, 697.11, 521.9|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_72|groceries/Weekly produce market/debit/ZAR|2|813.84, 652.85|repeated but not demonstrably recurrent|||
|user_72|groceries/Fresh food shop/debit/ZAR|2|769.85, 627.94|repeated but not demonstrably recurrent|||
|user_72|groceries/Bulk pantry shop/debit/ZAR|2|804.27, 492.76|repeated but not demonstrably recurrent|||
|user_72|transport/Ride-hailing trip/debit/ZAR|3|285.62, 445.48, 388.56|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_72|transport/Metro and bus fares/debit/ZAR|4|324.8, 399.31, 288.7, 381.67|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_72|transport/Local taxi/debit/ZAR|2|415.55, 393.5|repeated but not demonstrably recurrent|||
|user_72|transport/Commuter pass/debit/ZAR|5|460.56, 260.25, 369.73, 337.9, 361.06|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_72|transport/Fuel refill/debit/ZAR|3|431.83, 442.39, 400.22|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_72|transport/Parking and tolls/debit/ZAR|3|260.22, 406.01, 455.8|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_72|transport/Vehicle charging/debit/ZAR|3|327.87, 303.24, 429.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_72|transport/Rail pass/debit/ZAR|3|273.52, 383.94, 281.96|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_72|dining/Neighbourhood restaurant/debit/ZAR|4|1041.39, 771.04, 846.7, 932.3|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_72|dining/Takeaway order/debit/ZAR|4|786.48, 778.33, 936.71, 1010.92|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_72|dining/Coffee shop/debit/ZAR|2|772.03, 989.25|repeated but not demonstrably recurrent|||
|user_72|dining/Family dinner/debit/ZAR|2|660.71, 750.5|repeated but not demonstrably recurrent|||
|user_73|salary/Payroll credit/credit/INR|6|132000, 132000, 132000, 132000, 132000, 132000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_73|rent/Residential rent payment/debit/INR|6|37300, 37300, 37300, 37300, 37300, 37300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_73|utilities/Municipal utilities/debit/INR|6|7192.11, 6230.21, 7828.45, 6378.43, 6498.18, 7587.41|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_73|debt_repayment/Education loan instalment/debit/INR|6|11000, 11000, 11000, 11000, 11000, 11000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_73|streaming/Streaming subscription/debit/INR|6|2850, 2850, 2850, 2850, 2850, 2850|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_73|cloud_storage/Cloud storage plan/debit/INR|6|485, 485, 485, 485, 485, 485|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_73|shopping/Online retail purchases/debit/INR|6|5227.88, 4992, 4790.75, 4552.65, 4490.47, 4679.32|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_73|groceries/Neighbourhood grocer/debit/INR|2|6153, 5003.25|repeated but not demonstrably recurrent|||
|user_73|groceries/Local market purchase/debit/INR|2|5355.29, 5977.43|repeated but not demonstrably recurrent|||
|user_73|groceries/Grocery delivery/debit/INR|2|3695.04, 5222.55|repeated but not demonstrably recurrent|||
|user_73|groceries/Supermarket basket/debit/INR|9|4438.47, 5642.16, 4692.34, 4013.79, 4692.49, 5220.77, 5043.58, 4228.34, 5609.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_73|groceries/Household groceries/debit/INR|3|4258.65, 5403.6, 5182.71|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_73|groceries/Fresh food shop/debit/INR|3|5960.28, 5775.64, 4299.63|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_73|groceries/Bulk pantry shop/debit/INR|4|5642.16, 4417.24, 5719.62, 5496.85|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_73|transport/Rail pass/debit/INR|5|1922.78, 1879.75, 2265.6, 2106.57, 2578.23|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_73|transport/Vehicle charging/debit/INR|5|2206.8, 2405.69, 2226.24, 2832.33, 2507.21|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_73|transport/Fuel refill/debit/INR|3|2363.48, 1801.06, 2988.15|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_73|transport/Commuter pass/debit/INR|2|1977.7, 2536.79|repeated but not demonstrably recurrent|||
|user_73|transport/Ride-hailing trip/debit/INR|3|2047.96, 2504.2, 1985.68|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_73|transport/Parking and tolls/debit/INR|3|1865.09, 2948.23, 3105.78|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_73|transport/Metro and bus fares/debit/INR|2|3081.31, 2036.3|repeated but not demonstrably recurrent|||
|user_73|transport/Local taxi/debit/INR|3|2339.17, 2763.9, 2814.41|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_73|dining/Weekend food delivery/debit/INR|3|3712.19, 4229.18, 3860.04|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_73|dining/Bakery and snacks/debit/INR|3|4540.04, 3738.46, 5055.8|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_73|dining/Neighbourhood restaurant/debit/INR|3|4299.06, 3722.59, 4062.7|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_74|salary/Design contract payment/credit/ZAR|2|13154.13, 11653.61|repeated but not demonstrably recurrent|||
|user_74|salary/Independent work payment/credit/ZAR|2|16102.14, 8960.33|repeated but not demonstrably recurrent|||
|user_74|rent/Shared housing rent/debit/ZAR|6|7590, 7590, 7590, 7590, 7590, 7590|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_74|utilities/Electricity and water bill/debit/ZAR|5|1520.49, 1244.61, 1364.92, 1382.37, 1401.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_74|cloud_storage/Shared storage plan/debit/ZAR|5|146.3, 146.3, 146.3, 146.3, 146.3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_74|streaming/Family streaming plan/debit/ZAR|5|686.4, 686.4, 686.4, 686.4, 686.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_74|shopping/Online retail purchases/debit/ZAR|5|1043.52, 1094.86, 1213.5, 1134.39, 1086.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_74|salary/Website project payment/credit/ZAR|2|15308.05, 11128.25|repeated but not demonstrably recurrent|||
|user_74|salary/Content contract payment/credit/ZAR|2|14381.72, 8317.44|repeated but not demonstrably recurrent|||
|user_74|groceries/Neighbourhood grocer/debit/ZAR|4|1146.76, 1142.97, 730.7, 1017.08|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_74|groceries/Weekly produce market/debit/ZAR|3|1151, 939.58, 1176.36|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_74|groceries/Grocery delivery/debit/ZAR|3|1159.39, 718.11, 1060.75|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_74|groceries/Fresh food shop/debit/ZAR|3|943.92, 998.11, 1190.61|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_74|groceries/Household groceries/debit/ZAR|4|1077.28, 703.56, 882.83, 824.83|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_74|transport/Parking and tolls/debit/ZAR|2|694.33, 778.57|repeated but not demonstrably recurrent|||
|user_74|transport/Local taxi/debit/ZAR|2|850.31, 813.15|repeated but not demonstrably recurrent|||
|user_74|transport/Vehicle charging/debit/ZAR|2|550.54, 665.01|repeated but not demonstrably recurrent|||
|user_74|dining/Quick-service meal/debit/ZAR|2|1123.9, 936.29|repeated but not demonstrably recurrent|||
|user_74|dining/Lunch with colleagues/debit/ZAR|2|930.37, 878.65|repeated but not demonstrably recurrent|||
|user_75|salary/Payroll credit/credit/ZAR|4|50820, 50820, 50820, 50820|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_75|rent/Shared housing rent/debit/ZAR|6|15642, 15642, 15642, 15642, 15642, 15642|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_75|utilities/Water and power payment/debit/ZAR|5|2136.08, 2544.7, 2177.61, 2525.65, 2243.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_75|cloud_storage/Shared storage plan/debit/ZAR|5|410.3, 410.3, 410.3, 410.3, 410.3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_75|streaming/Family streaming plan/debit/ZAR|5|959.2, 959.2, 959.2, 959.2, 959.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_75|shopping/Online retail purchases/debit/ZAR|5|975.23, 1082.49, 925.62, 1015.68, 1114.29|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_75|groceries/Bulk pantry shop/debit/ZAR|7|2498.61, 1772.58, 2016.24, 1585.09, 2324.36, 2024.48, 2004.79|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_75|groceries/Weekly produce market/debit/ZAR|4|2058.32, 2426.23, 2608.75, 2009.99|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_75|groceries/Supermarket basket/debit/ZAR|2|2012.92, 1724.38|repeated but not demonstrably recurrent|||
|user_75|groceries/Local market purchase/debit/ZAR|2|2176.81, 2368.36|repeated but not demonstrably recurrent|||
|user_75|transport/Parking and tolls/debit/ZAR|3|1201.53, 1214.86, 1000.44|variable but recurrent|84|RECURRING_AMOUNT_UNRESOLVED|
|user_75|transport/Local taxi/debit/ZAR|2|1314.04, 1093.79|repeated but not demonstrably recurrent|||
|user_75|transport/Commuter pass/debit/ZAR|2|1421.27, 1292.57|repeated but not demonstrably recurrent|||
|user_75|dining/Weekend food delivery/debit/ZAR|2|2478.11, 1927.47|repeated but not demonstrably recurrent|||
|user_75|dining/Quick-service meal/debit/ZAR|4|1699.18, 2525.38, 1942.45, 2508.66|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_76|salary/Base salary/credit/USD|5|1843.2, 1843.2, 1843.2, 1843.2, 1843.2|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_76|salary/Account commission payment/credit/USD|2|420.15, 1504.17|repeated but not demonstrably recurrent|||
|user_76|rent/Shared housing rent/debit/USD|6|694.8, 694.8, 694.8, 694.8, 694.8, 694.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_76|utilities/Household utility payment/debit/USD|5|175.66, 159.67, 171.49, 175.62, 153.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_76|music_subscription/Music subscription/debit/USD|5|42, 42, 42, 42, 42|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_76|delivery_membership/Food delivery membership/debit/USD|5|45, 45, 45, 45, 45|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_76|gym/Fitness club membership/debit/USD|5|70, 70, 70, 70, 70|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_76|entertainment/Games and recreation/debit/USD|5|106.31, 106.75, 98.25, 123.11, 111.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_76|salary/Monthly sales commission/credit/USD|2|1051.27, 1817.02|repeated but not demonstrably recurrent|||
|user_76|groceries/Neighbourhood grocer/debit/USD|4|130.92, 146.88, 99.68, 144.86|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_76|groceries/Local market purchase/debit/USD|3|104.72, 114.63, 134|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_76|groceries/Grocery delivery/debit/USD|3|112.05, 129.06, 152.91|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_76|groceries/Fresh food shop/debit/USD|5|93.42, 101.52, 96.15, 153.36, 98.31|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_76|groceries/Household groceries/debit/USD|3|98.95, 103.05, 108.51|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_76|groceries/Supermarket basket/debit/USD|5|121.37, 113.46, 131.31, 127.34, 112.19|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_76|groceries/Bulk pantry shop/debit/USD|2|124.36, 97.97|repeated but not demonstrably recurrent|||
|user_76|transport/Commuter pass/debit/USD|3|41.53, 53.5, 65.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_76|transport/Metro and bus fares/debit/USD|7|44.76, 41.12, 44.51, 61.87, 53.04, 68.43, 45.67|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_76|transport/Rail pass/debit/USD|6|58.72, 53.86, 69.91, 55.42, 55.24, 44.52|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_76|transport/Local taxi/debit/USD|2|57.73, 63.39|repeated but not demonstrably recurrent|||
|user_76|transport/Vehicle charging/debit/USD|2|59.84, 51.55|repeated but not demonstrably recurrent|||
|user_76|transport/Fuel refill/debit/USD|3|57.81, 42.16, 42.92|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_76|transport/Ride-hailing trip/debit/USD|3|54.85, 62.91, 51.12|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_76|dining/Neighbourhood restaurant/debit/USD|3|108.74, 99.95, 75.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_76|dining/Bakery and snacks/debit/USD|3|111.49, 116.64, 100.43|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_76|dining/Takeaway order/debit/USD|2|99.34, 98.09|repeated but not demonstrably recurrent|||
|user_76|dining/Family dinner/debit/USD|2|72.19, 82.72|repeated but not demonstrably recurrent|||
|user_77|salary/Payroll credit/credit/INR|5|111000, 111000, 111000, 111000, 111000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_77|rent/Apartment rent transfer/debit/INR|6|25200, 25200, 25200, 25200, 25200, 25200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_77|utilities/Household utility payment/debit/INR|5|7085.13, 7056.24, 7787.06, 7725.2, 7704.51|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_77|debt_repayment/Vehicle loan payment/debit/INR|5|12500, 12500, 12500, 12500, 12500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_77|healthcare/Family healthcare expense/debit/INR|5|7019.28, 8445.84, 7872.68, 8570.67, 7860.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_77|family_support/Childcare contribution/debit/INR|5|6740, 6740, 6740, 6740, 6740|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_77|cloud_storage/Online backup subscription/debit/INR|5|705, 705, 705, 705, 705|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_77|shopping/Clothing and household items/debit/INR|5|6004.91, 5011.43, 5512.74, 5977.11, 5091.25|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_77|groceries/Bulk pantry shop/debit/INR|4|5160.97, 3660.42, 4686.49, 4301.35|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_77|groceries/Local market purchase/debit/INR|5|4685.01, 4185.43, 4174.56, 5169.17, 3764.63|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_77|groceries/Weekly produce market/debit/INR|4|3281.2, 3302.75, 3969.3, 5350.69|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_77|groceries/Grocery delivery/debit/INR|5|4740.84, 4779.5, 4352.32, 3377.97, 3766.71|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_77|groceries/Household groceries/debit/INR|3|4279.4, 5051.79, 4542.72|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_77|groceries/Supermarket basket/debit/INR|2|3871.9, 3907.17|repeated but not demonstrably recurrent|||
|user_77|groceries/Fresh food shop/debit/INR|2|3381.19, 4451.38|repeated but not demonstrably recurrent|||
|user_77|transport/Local taxi/debit/INR|2|2288.15, 2118.65|repeated but not demonstrably recurrent|||
|user_77|transport/Rail pass/debit/INR|2|2926.14, 2951.66|repeated but not demonstrably recurrent|||
|user_77|transport/Metro and bus fares/debit/INR|2|1975.26, 2410.98|repeated but not demonstrably recurrent|||
|user_77|transport/Ride-hailing trip/debit/INR|2|2083.9, 3113.53|repeated but not demonstrably recurrent|||
|user_77|transport/Fuel refill/debit/INR|2|2725.56, 2848.16|repeated but not demonstrably recurrent|||
|user_78|salary/Payroll credit/credit/INR|5|89000, 89000, 89000, 89000, 89000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_78|rent/Shared housing rent/debit/INR|5|28200, 28200, 28200, 28200, 28200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_78|utilities/Household utility payment/debit/INR|5|4762.24, 5823.32, 5651.47, 5267.31, 5540.95|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_78|insurance/Household insurance/debit/INR|5|2790, 2790, 2790, 2790, 2790|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_78|cloud_storage/Shared storage plan/debit/INR|5|415, 415, 415, 415, 415|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_78|streaming/Video streaming plan/debit/INR|5|1610, 1610, 1610, 1610, 1610|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_78|shopping/Monthly shopping spend/debit/INR|5|3639.86, 3836.29, 3419.39, 3387.54, 3269.8|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_78|entertainment/Weekend entertainment/debit/INR|5|2403.53, 2306.75, 2422.15, 2147.14, 2143.02|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_78|groceries/Local market purchase/debit/INR|4|4050.69, 2719.43, 2621.25, 3659.36|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_78|groceries/Weekly produce market/debit/INR|5|2943.4, 4425.95, 3944.85, 2642.51, 3212.8|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_78|groceries/Fresh food shop/debit/INR|3|2570.47, 4168.42, 4182.27|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_78|groceries/Grocery delivery/debit/INR|3|4408.14, 2983.18, 3070.23|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_78|groceries/Supermarket basket/debit/INR|2|3627.75, 2915.51|repeated but not demonstrably recurrent|||
|user_78|transport/Local taxi/debit/INR|3|2232.57, 2620.67, 2221.3|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Ride-hailing trip/debit/INR|8|2136.49, 1572.68, 1817.83, 2193.36, 1588.3, 2412.56, 1538.3, 1822.99|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Commuter pass/debit/INR|5|2516.55, 1772.1, 2015.56, 2546.62, 2671.76|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Vehicle charging/debit/INR|3|1824.75, 2155.87, 2099.4|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Metro and bus fares/debit/INR|3|2246.83, 2169.89, 2099.04|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Rail pass/debit/INR|6|2576, 2437.71, 1859.98, 2345.25, 1701.8, 1597.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Parking and tolls/debit/INR|5|2447.74, 2506.98, 2277.91, 2604.17, 2650.2|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_78|transport/Fuel refill/debit/INR|2|1986.92, 1538.73|repeated but not demonstrably recurrent|||
|user_78|dining/Coffee shop/debit/INR|4|2708.09, 2314.01, 2501.84, 3074.98|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_78|dining/Bakery and snacks/debit/INR|5|2259.42, 2457.26, 2511.67, 3582.95, 2163.72|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_78|dining/Weekend food delivery/debit/INR|2|3588.18, 2508.7|repeated but not demonstrably recurrent|||
|user_78|dining/Quick-service meal/debit/INR|4|3149.29, 2790.25, 3492.42, 3014.62|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_78|dining/Family dinner/debit/INR|3|2187.14, 3366.96, 3641.76|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_78|dining/Takeaway order/debit/INR|4|3300.19, 2764.7, 3023.93, 3171.37|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_78|dining/Lunch with colleagues/debit/INR|2|3558.88, 3442.44|repeated but not demonstrably recurrent|||
|user_79|salary/Payroll credit/credit/USD|5|1313.76, 1313.76, 1313.76, 1313.76, 1313.76|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_79|rent/Monthly rent/debit/EUR|5|386.1, 386.1, 386.1, 386.1, 386.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_79|utilities/Energy provider bill/debit/EUR|5|87.61, 83.48, 86.65, 81.09, 97.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_79|insurance/Insurance policy payment/debit/EUR|5|52, 52, 52, 52, 52|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_79|cloud_storage/Shared storage plan/debit/EUR|5|11, 11, 11, 11, 11|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_79|streaming/Video streaming plan/debit/EUR|5|33, 33, 33, 33, 33|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_79|shopping/Personal shopping/debit/EUR|5|51.83, 48.22, 53.38, 52.01, 54.45|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_79|entertainment/Cinema and events/debit/EUR|5|32.82, 35.46, 35.99, 30.15, 30.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_79|groceries/Household groceries/debit/EUR|4|53.05, 50.76, 59.79, 46.76|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_79|groceries/Bulk pantry shop/debit/EUR|3|40.99, 48.74, 64.35|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_79|groceries/Grocery delivery/debit/EUR|2|62.44, 48.8|repeated but not demonstrably recurrent|||
|user_79|groceries/Supermarket basket/debit/EUR|4|56.81, 62.37, 46.05, 61.72|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_79|groceries/Fresh food shop/debit/EUR|2|62.94, 64.97|repeated but not demonstrably recurrent|||
|user_79|transport/Metro and bus fares/debit/EUR|3|27.35, 32.44, 35.99|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_79|transport/Parking and tolls/debit/EUR|2|32.79, 32.29|repeated but not demonstrably recurrent|||
|user_79|transport/Fuel refill/debit/EUR|10|30.37, 22.83, 28.18, 36.96, 27.5, 24.01, 23.62, 35.34, 30.74, 28.21|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_79|transport/Commuter pass/debit/EUR|4|31.33, 24.7, 22.03, 27.69|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_79|transport/Ride-hailing trip/debit/EUR|5|38.35, 37.33, 34.45, 30.65, 26.17|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_79|transport/Vehicle charging/debit/EUR|6|34.72, 27.02, 24.07, 27.46, 22.55, 34.56|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_79|transport/Local taxi/debit/EUR|4|34.18, 35.05, 23.67, 29.74|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Quick-service meal/debit/EUR|4|70.36, 67.76, 49.55, 42.22|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Weekend food delivery/debit/EUR|3|58.13, 51.76, 67.22|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Takeaway order/debit/EUR|5|41.09, 69.26, 44.48, 64.9, 45.76|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Neighbourhood restaurant/debit/EUR|3|56.03, 63.17, 51.14|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Lunch with colleagues/debit/EUR|3|51.46, 43.77, 61.56|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Coffee shop/debit/EUR|2|43.37, 55.57|repeated but not demonstrably recurrent|||
|user_79|dining/Family dinner/debit/EUR|4|50.89, 55.21, 48.2, 43.53|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_79|dining/Bakery and snacks/debit/EUR|2|64.18, 57.38|repeated but not demonstrably recurrent|||
|user_80|salary/Base salary/credit/INR|5|94800, 94800, 94800, 94800, 94800|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_80|salary/Performance commission/credit/INR|2|27075.02, 44891.71|repeated but not demonstrably recurrent|||
|user_80|rent/Residential rent payment/debit/INR|6|52000, 52000, 52000, 52000, 52000, 52000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_80|utilities/Electricity bill/debit/INR|6|7945.29, 7332.77, 6807.36, 6811.42, 6790.9, 6413.34|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_80|education/School fee payment/debit/INR|5|15360, 15360, 15360, 15360, 15360|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_80|debt_repayment/Personal loan payment/debit/INR|5|9000, 9000, 9000, 9000, 9000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_80|music_subscription/Music service subscription/debit/INR|5|1225, 1225, 1225, 1225, 1225|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_80|delivery_membership/Delivery service plan/debit/INR|5|1120, 1120, 1120, 1120, 1120|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_80|salary/Account commission payment/credit/INR|2|36545.35, 93724.2|repeated but not demonstrably recurrent|||
|user_80|groceries/Supermarket basket/debit/INR|10|5200.31, 5601.9, 5342.51, 5267.09, 5564.97, 7248.93, 5013.24, 7153.61, 7307.2, 5617.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_80|groceries/Household groceries/debit/INR|5|5064.01, 6756.28, 5033.99, 5507.76, 5158.53|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_80|groceries/Local market purchase/debit/INR|2|5926.41, 6036.43|repeated but not demonstrably recurrent|||
|user_80|groceries/Grocery delivery/debit/INR|3|7283.7, 4757.32, 6620.4|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_80|groceries/Neighbourhood grocer/debit/INR|3|6262.46, 7164.01, 5264.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_80|transport/Commuter pass/debit/INR|4|3156.38, 3891.11, 4599.94, 3308.8|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_80|transport/Fuel refill/debit/INR|4|3463.71, 4174.96, 4648.2, 4851.43|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_80|transport/Local taxi/debit/INR|2|3716.45, 5059.67|repeated but not demonstrably recurrent|||
|user_80|transport/Rail pass/debit/INR|2|4121.36, 5464.28|repeated but not demonstrably recurrent|||
|user_80|transport/Parking and tolls/debit/INR|3|3166.82, 3223.86, 3363.5|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_80|transport/Metro and bus fares/debit/INR|4|3500.85, 4969.7, 5376, 4441.52|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_80|transport/Ride-hailing trip/debit/INR|5|5302.5, 4469.23, 3611, 4720.43, 4141.71|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_80|transport/Vehicle charging/debit/INR|2|4483.73, 4147.72|repeated but not demonstrably recurrent|||
|user_80|dining/Neighbourhood restaurant/debit/INR|2|3935.16, 5172.93|repeated but not demonstrably recurrent|||
|user_80|dining/Weekend food delivery/debit/INR|4|3863.42, 5910.44, 5904.48, 6694.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_80|dining/Quick-service meal/debit/INR|2|5002.93, 6616.25|repeated but not demonstrably recurrent|||
|user_80|dining/Takeaway order/debit/INR|3|3951.41, 6439.4, 3938.12|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_81|salary/Payroll credit/credit/USD|5|2808, 2808, 2808, 2808, 2808|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_81|rent/Apartment rent transfer/debit/USD|6|926.4, 926.4, 926.4, 926.4, 926.4, 926.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_81|utilities/Electricity bill/debit/USD|5|157.66, 180.83, 190.4, 192.07, 182.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_81|debt_repayment/Credit card repayment/debit/USD|5|454, 454, 454, 454, 454|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_81|streaming/Streaming subscription/debit/USD|5|76, 76, 76, 76, 76|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_81|cloud_storage/Online backup subscription/debit/USD|5|16, 16, 16, 16, 16|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_81|shopping/Clothing and household items/debit/USD|5|82.98, 79.06, 72.68, 68.95, 72.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_81|groceries/Weekly produce market/debit/USD|3|97.56, 127.53, 128.46|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_81|groceries/Fresh food shop/debit/USD|5|79.67, 101.22, 84.32, 99.17, 96.06|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_81|groceries/Bulk pantry shop/debit/USD|2|113.21, 116.38|repeated but not demonstrably recurrent|||
|user_81|groceries/Grocery delivery/debit/USD|4|75.54, 118.9, 109.13, 111.61|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_81|groceries/Supermarket basket/debit/USD|6|119.38, 100.63, 129.41, 117.23, 92.86, 76.67|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_81|groceries/Household groceries/debit/USD|2|80.56, 110.85|repeated but not demonstrably recurrent|||
|user_81|groceries/Local market purchase/debit/USD|3|121.79, 120.19, 113.99|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_81|transport/Vehicle charging/debit/USD|6|76.44, 73.68, 75.1, 84.68, 76.51, 53.44|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_81|transport/Local taxi/debit/USD|4|51.09, 56.33, 51.39, 59.3|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_81|transport/Metro and bus fares/debit/USD|3|75.96, 68.29, 83.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_81|transport/Ride-hailing trip/debit/USD|5|73.22, 71.04, 81.86, 68.08, 60.48|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_81|transport/Commuter pass/debit/USD|3|67.48, 70.14, 65.06|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_81|transport/Fuel refill/debit/USD|4|51.93, 68.15, 83.29, 83.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_81|dining/Neighbourhood restaurant/debit/USD|2|65.56, 79.83|repeated but not demonstrably recurrent|||
|user_81|dining/Quick-service meal/debit/USD|3|65.11, 92.52, 91.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_81|dining/Weekend food delivery/debit/USD|3|74.8, 79.28, 95.21|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_81|dining/Family dinner/debit/USD|2|58.62, 71.21|repeated but not demonstrably recurrent|||
|user_82|salary/Payroll credit/credit/USD|5|1752, 1752, 1752, 1752, 1752|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_82|rent/Shared housing rent/debit/USD|6|405.6, 405.6, 405.6, 405.6, 405.6, 405.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_82|utilities/Household utility payment/debit/USD|5|104.35, 99.97, 94.12, 99.65, 93.66|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_82|debt_repayment/Education loan instalment/debit/USD|5|244, 244, 244, 244, 244|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_82|streaming/Family streaming plan/debit/USD|5|32, 32, 32, 32, 32|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_82|cloud_storage/Shared storage plan/debit/USD|5|13, 13, 13, 13, 13|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_82|shopping/Personal shopping/debit/USD|5|79.37, 83.13, 81.08, 74.8, 85.29|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Household groceries/debit/USD|4|89.81, 96.47, 60.03, 94.86|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Grocery delivery/debit/USD|5|67.91, 91.73, 69, 77.57, 79.47|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Weekly produce market/debit/USD|3|78.23, 87.66, 79.97|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Supermarket basket/debit/USD|5|66.32, 57.23, 60.92, 90.76, 82.78|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Neighbourhood grocer/debit/USD|3|63.45, 70.76, 77.11|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Fresh food shop/debit/USD|3|59.23, 82.95, 68.53|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_82|groceries/Local market purchase/debit/USD|2|85.42, 83.98|repeated but not demonstrably recurrent|||
|user_82|transport/Local taxi/debit/USD|4|36.94, 46.25, 42.76, 39.87|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_82|transport/Metro and bus fares/debit/USD|4|42.4, 49.11, 43.55, 36.83|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_82|transport/Rail pass/debit/USD|5|50.45, 46.48, 40.22, 45.68, 53.4|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_82|transport/Commuter pass/debit/USD|3|40.1, 33.92, 33|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_82|transport/Vehicle charging/debit/USD|3|35.38, 40.84, 38.19|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_82|transport/Ride-hailing trip/debit/USD|4|53.12, 31.4, 30.59, 43.53|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_82|dining/Lunch with colleagues/debit/USD|5|67.55, 67.27, 54.77, 83.45, 73.71|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_82|dining/Quick-service meal/debit/USD|2|62.19, 84.69|repeated but not demonstrably recurrent|||
|user_83|salary/Payroll before leave/credit/INR|2|62000, 62000|repeated but not demonstrably recurrent|||
|user_83|housing/Home repair reserve/debit/INR|6|6700, 6700, 6700, 6700, 6700, 6700|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_83|utilities/Municipal utilities/debit/INR|5|3677.77, 3967.64, 3731.16, 4586.06, 4288.27|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_83|insurance/Health insurance premium/debit/INR|5|3020, 3020, 3020, 3020, 3020|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_83|education/Course tuition/debit/INR|5|6100, 6100, 6100, 6100, 6100|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_83|healthcare/Therapy appointment/debit/INR|5|5067.26, 4611.74, 4802.9, 4522.3, 4681.41|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_83|entertainment/Local event tickets/debit/INR|5|1172.8, 986.9, 961.69, 1014.59, 1063.98|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_83|cloud_storage/Shared storage plan/debit/INR|5|500, 500, 500, 500, 500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_83|groceries/Weekly produce market/debit/INR|4|2289.9, 2989.65, 2857.02, 2971.64|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_83|groceries/Fresh food shop/debit/INR|5|2296.2, 2178.74, 2532, 3310.94, 2544.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_83|groceries/Household groceries/debit/INR|2|3418.3, 2061.4|repeated but not demonstrably recurrent|||
|user_83|groceries/Local market purchase/debit/INR|4|2849.43, 2278.31, 2329.73, 2497.63|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_83|transport/Fuel refill/debit/INR|4|1723.58, 1454.68, 2083.11, 2113.78|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_83|transport/Parking and tolls/debit/INR|2|1967.21, 1973.26|repeated but not demonstrably recurrent|||
|user_83|transport/Vehicle charging/debit/INR|2|2151.96, 1340.8|repeated but not demonstrably recurrent|||
|user_83|transport/Metro and bus fares/debit/INR|2|1248.03, 1537.23|repeated but not demonstrably recurrent|||
|user_83|dining/Lunch with colleagues/debit/INR|2|2067.39, 2252.46|repeated but not demonstrably recurrent|||
|user_83|dining/Family dinner/debit/INR|3|3045.17, 1910.09, 2137.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_83|dining/Coffee shop/debit/INR|3|1946.94, 2921.72, 1742.86|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_84|salary/Payroll credit/credit/USD|5|107995.68, 107995.68, 107995.68, 107995.68, 107995.68|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_84|rent/Shared housing rent/debit/INR|6|26200, 26200, 26200, 26200, 26200, 26200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_84|utilities/Household utility payment/debit/INR|5|5843.3, 5522.8, 5513.09, 5386.81, 4737.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_84|insurance/Vehicle insurance premium/debit/INR|5|4790, 4790, 4790, 4790, 4790|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_84|cloud_storage/Cloud storage plan/debit/INR|5|405, 405, 405, 405, 405|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_84|streaming/Family streaming plan/debit/INR|5|2390, 2390, 2390, 2390, 2390|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_84|shopping/Household shopping/debit/INR|5|5102.24, 6291.13, 6280.65, 6011, 5861.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_84|entertainment/Games and recreation/debit/INR|5|4140.81, 4428.25, 3763.85, 3721.43, 3831.07|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_84|groceries/Household groceries/debit/INR|7|3561.36, 4957.21, 4278.21, 5878.02, 5228.32, 4966.85, 3596.02|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_84|groceries/Fresh food shop/debit/INR|2|4153.46, 4440.76|repeated but not demonstrably recurrent|||
|user_84|groceries/Grocery delivery/debit/INR|2|5864.53, 5174.14|repeated but not demonstrably recurrent|||
|user_84|groceries/Bulk pantry shop/debit/INR|2|4114.73, 5472.66|repeated but not demonstrably recurrent|||
|user_84|groceries/Neighbourhood grocer/debit/INR|2|5622.65, 3692.8|repeated but not demonstrably recurrent|||
|user_84|groceries/Supermarket basket/debit/INR|2|3975.45, 3421.26|repeated but not demonstrably recurrent|||
|user_84|transport/Metro and bus fares/debit/INR|4|1638.42, 2053.22, 1781.1, 1655.31|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Local taxi/debit/INR|5|2489.79, 1764.93, 1865.45, 2283.33, 2327.06|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Fuel refill/debit/INR|4|1968.64, 2398.08, 2518.68, 1718.43|variable but recurrent|55|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Ride-hailing trip/debit/INR|6|2030.92, 2078.62, 1796.33, 2031.97, 1802.35, 2348.3|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Rail pass/debit/INR|4|2624.34, 1811.39, 2072.59, 2284|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Commuter pass/debit/INR|4|1895.31, 1805.48, 2328.08, 2185.83|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Vehicle charging/debit/INR|4|1737.85, 1603.33, 1988.51, 1591.9|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_84|transport/Parking and tolls/debit/INR|5|2413.62, 2268.15, 2352.37, 1540.49, 2028.16|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_84|dining/Quick-service meal/debit/INR|4|3968.07, 3627.92, 4016.77, 3922.48|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_84|dining/Takeaway order/debit/INR|4|3346.99, 2927.06, 3658.71, 4100.28|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_84|dining/Bakery and snacks/debit/INR|6|4203.19, 3385.48, 3533.52, 3015.8, 2869.78, 3957.84|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_84|dining/Neighbourhood restaurant/debit/INR|4|3820.66, 4028.99, 4014.08, 4191.31|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_84|dining/Weekend food delivery/debit/INR|4|3807.8, 4117.92, 3700.51, 2931.51|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_84|dining/Family dinner/debit/INR|2|3461.42, 3465.77|repeated but not demonstrably recurrent|||
|user_85|salary/Payroll credit/credit/IDR|5|11970000, 11970000, 11970000, 8618400, 8618400|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_85|rent/Apartment rent transfer/debit/IDR|6|2527000, 2527000, 2527000, 2527000, 2527000, 2527000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_85|utilities/Municipal utilities/debit/IDR|5|486483.88, 408477.25, 447504.57, 469562.86, 438642.78|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_85|music_subscription/Music service subscription/debit/IDR|5|88350, 88350, 88350, 88350, 88350|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_85|delivery_membership/Grocery delivery membership/debit/IDR|5|135850, 135850, 135850, 135850, 135850|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_85|gym/Fitness club membership/debit/IDR|5|161500, 161500, 161500, 161500, 161500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_85|entertainment/Local event tickets/debit/IDR|5|292839.09, 264634.75, 275599.63, 330784.55, 327064.93|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_85|groceries/Household groceries/debit/IDR|3|371927.81, 284259.82, 316978.13|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_85|groceries/Neighbourhood grocer/debit/IDR|4|342076.7, 284582.5, 379934.63, 267279.85|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_85|groceries/Grocery delivery/debit/IDR|9|292087.13, 281575.93, 334660.39, 384407.04, 254575.18, 287895.24, 276196.39, 351521.87, 302278.67|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_85|groceries/Bulk pantry shop/debit/IDR|2|290178.18, 346966.79|repeated but not demonstrably recurrent|||
|user_85|groceries/Local market purchase/debit/IDR|3|374521.14, 239478.29, 271720.07|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_85|groceries/Supermarket basket/debit/IDR|2|359651.92, 287467.32|repeated but not demonstrably recurrent|||
|user_85|groceries/Weekly produce market/debit/IDR|2|318036.52, 241772.45|repeated but not demonstrably recurrent|||
|user_85|transport/Fuel refill/debit/IDR|4|239117, 200309.28, 222081.32, 190154.84|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_85|transport/Metro and bus fares/debit/IDR|5|154445.49, 250953, 162204.96, 223100.43, 186459.46|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_85|transport/Commuter pass/debit/IDR|2|167874.22, 226951.07|repeated but not demonstrably recurrent|||
|user_85|transport/Parking and tolls/debit/IDR|3|250765.06, 170293.37, 236207.13|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_85|transport/Vehicle charging/debit/IDR|6|166781.87, 174481.44, 154366.33, 170374.26, 233129.05, 200977.42|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_85|transport/Ride-hailing trip/debit/IDR|5|241857.78, 214016.35, 207670.55, 184618.75, 195680.3|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_85|dining/Bakery and snacks/debit/IDR|2|288438.08, 300461.6|repeated but not demonstrably recurrent|||
|user_85|dining/Family dinner/debit/IDR|2|334430.72, 443786.92|repeated but not demonstrably recurrent|||
|user_85|dining/Coffee shop/debit/IDR|3|457457.54, 308691.17, 316903.32|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_85|dining/Weekend food delivery/debit/IDR|2|448698.54, 452754.2|repeated but not demonstrably recurrent|||
|user_85|dining/Quick-service meal/debit/IDR|2|433514.42, 453900.61|repeated but not demonstrably recurrent|||
|user_86|salary/Payroll credit/credit/INR|5|124000, 124000, 124000, 124000, 124000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_86|rent/Residential rent payment/debit/INR|5|38800, 38800, 38800, 38800, 38800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_86|utilities/Municipal utilities/debit/INR|5|6931.79, 6602.15, 6208.44, 6174.58, 6377.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_86|debt_repayment/Loan repayment/debit/INR|5|15800, 15800, 15800, 15800, 15800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_86|healthcare/Diagnostic test/debit/INR|5|4428.1, 4030.03, 3832.01, 4041.38, 3802.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_86|family_support/Dependent care payment/debit/INR|5|7620, 7620, 7620, 7620, 7620|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_86|cloud_storage/Shared storage plan/debit/INR|5|755, 755, 755, 755, 755|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_86|shopping/Online retail purchases/debit/INR|5|6219.49, 5570.15, 5493.01, 6270.72, 6464.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_86|groceries/Household groceries/debit/INR|5|6301.28, 6238.3, 5605.74, 5842.05, 5474.45|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_86|groceries/Fresh food shop/debit/INR|3|5226.45, 6525.46, 4569.43|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_86|groceries/Grocery delivery/debit/INR|3|4935.12, 5042.34, 5261.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_86|groceries/Neighbourhood grocer/debit/INR|6|4968.63, 4873.2, 6512.98, 6256.67, 5697.65, 6467.51|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_86|groceries/Local market purchase/debit/INR|3|5593.46, 5070.72, 5218.69|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_86|groceries/Supermarket basket/debit/INR|2|6410.75, 5092.29|repeated but not demonstrably recurrent|||
|user_86|groceries/Bulk pantry shop/debit/INR|3|4518.28, 6300.09, 6326.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_86|transport/Local taxi/debit/INR|3|3440.74, 2747.52, 2634.06|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_86|transport/Fuel refill/debit/INR|2|3752.77, 3035.63|repeated but not demonstrably recurrent|||
|user_86|transport/Parking and tolls/debit/INR|3|2538, 3520.67, 3139.59|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_86|transport/Commuter pass/debit/INR|3|3763.9, 2689.08, 3826.66|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_86|transport/Vehicle charging/debit/INR|2|2264.88, 3425.66|repeated but not demonstrably recurrent|||
|user_87|salary/Payroll before leave/credit/INR|2|251000, 251000|repeated but not demonstrably recurrent|||
|user_87|rent/Landlord standing order/debit/INR|6|74900, 74900, 74900, 74900, 74900, 74900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_87|utilities/Electricity bill/debit/INR|5|16221.4, 16229.85, 15086.91, 16998.34, 15679.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_87|insurance/Health insurance premium/debit/INR|5|9990, 9990, 9990, 9990, 9990|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_87|cloud_storage/Shared storage plan/debit/INR|5|1230, 1230, 1230, 1230, 1230|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_87|streaming/Streaming subscription/debit/INR|5|6450, 6450, 6450, 6450, 6450|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_87|shopping/Monthly shopping spend/debit/INR|5|10657.86, 12019.51, 10798.32, 12013.13, 10790.77|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_87|entertainment/Monthly entertainment spend/debit/INR|5|6423.05, 6018.66, 6902.39, 7010.18, 6875.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_87|groceries/Neighbourhood grocer/debit/INR|4|14013.15, 14418.48, 12764.95, 14547.71|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_87|groceries/Weekly produce market/debit/INR|2|8474.02, 11318.97|repeated but not demonstrably recurrent|||
|user_87|groceries/Bulk pantry shop/debit/INR|6|14128.09, 12609.41, 12249.95, 13407.1, 11577.22, 8577.23|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_87|groceries/Fresh food shop/debit/INR|3|13181.38, 10801.13, 10183.93|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Commuter pass/debit/INR|4|3807.18, 4740.75, 4621.05, 3574.96|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Ride-hailing trip/debit/INR|4|3760.17, 4969.31, 4447.58, 4861.7|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Parking and tolls/debit/INR|10|5192.65, 5859.12, 3952.16, 5195.58, 5453.39, 5511.65, 4626.98, 4851.27, 4931.36, 6019.7|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Local taxi/debit/INR|4|4595.81, 5904.86, 3879.45, 3828.97|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Rail pass/debit/INR|4|3913.6, 5434.38, 4819.5, 5589.97|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Vehicle charging/debit/INR|2|4418.1, 4496.44|repeated but not demonstrably recurrent|||
|user_87|transport/Metro and bus fares/debit/INR|4|4595.85, 5480.26, 4582.26, 3732.72|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_87|transport/Fuel refill/debit/INR|3|4597.6, 4264.06, 4461.2|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_87|dining/Weekend food delivery/debit/INR|6|10505.01, 9595.3, 11150.12, 7767.51, 11518.52, 10862.3|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_87|dining/Coffee shop/debit/INR|4|9276.9, 10354.47, 9812.76, 7051.12|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_87|dining/Lunch with colleagues/debit/INR|2|6701.25, 10988.81|repeated but not demonstrably recurrent|||
|user_87|dining/Quick-service meal/debit/INR|4|10231.27, 9578.34, 11108.36, 7065.99|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_87|dining/Bakery and snacks/debit/INR|3|9090.27, 7459.56, 9267.83|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_87|dining/Takeaway order/debit/INR|5|7674.38, 7041.29, 10163.85, 11436.07, 8791.54|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_88|salary/Payroll credit/credit/ZAR|5|34760, 34760, 34760, 34760, 34760|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_88|rent/Monthly rent/debit/ZAR|6|9614, 9614, 9614, 9614, 9614, 9614|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_88|utilities/Water and power payment/debit/ZAR|6|1804.34, 1696.68, 1683.3, 1894.2, 1782.31, 1773.56|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_88|debt_repayment/Education loan instalment/debit/ZAR|5|3322, 3322, 3322, 3322, 3322|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_88|music_subscription/Music service subscription/debit/ZAR|5|276.1, 276.1, 276.1, 276.1, 276.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_88|groceries/Neighbourhood grocer/debit/ZAR|2|984.7, 914.13|repeated but not demonstrably recurrent|||
|user_88|groceries/Bulk pantry shop/debit/ZAR|3|1136.41, 1539.52, 1262.47|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_88|groceries/Supermarket basket/debit/ZAR|3|990.59, 1418.65, 1462.17|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_88|groceries/Grocery delivery/debit/ZAR|2|1192.12, 951.36|repeated but not demonstrably recurrent|||
|user_88|groceries/Household groceries/debit/ZAR|2|1445.58, 1225.79|repeated but not demonstrably recurrent|||
|user_88|transport/Ride-hailing trip/debit/ZAR|2|908.23, 1002.27|repeated but not demonstrably recurrent|||
|user_88|transport/Parking and tolls/debit/ZAR|2|1185.82, 709.55|repeated but not demonstrably recurrent|||
|user_88|dining/Takeaway order/debit/ZAR|3|1392.28, 1130.63, 1266.81|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_88|dining/Weekend food delivery/debit/ZAR|2|1208.87, 1089.44|repeated but not demonstrably recurrent|||
|user_88|dining/Lunch with colleagues/debit/ZAR|2|1424.56, 1597.73|repeated but not demonstrably recurrent|||
|user_89|salary/Payroll credit/credit/IDR|5|15200000, 15200000, 15200000, 15200000, 15200000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_89|rent/Shared housing rent/debit/IDR|6|3819000, 3819000, 3819000, 3819000, 3819000, 3819000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_89|utilities/Municipal utilities/debit/IDR|5|713128.15, 724935.36, 783240.35, 876562.83, 828342.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_89|debt_repayment/Credit card repayment/debit/IDR|5|1985500, 1985500, 1985500, 1985500, 1985500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_89|streaming/Video streaming plan/debit/IDR|5|323000, 323000, 323000, 323000, 323000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_89|cloud_storage/Online backup subscription/debit/IDR|5|81700, 81700, 81700, 81700, 81700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_89|shopping/Monthly shopping spend/debit/IDR|5|673661.62, 676460.2, 698960.74, 659996, 633240.3|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Household groceries/debit/IDR|5|764462.19, 576622.85, 766431.08, 782814.43, 764239.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Weekly produce market/debit/IDR|4|744071.45, 627811.11, 639996.3, 812854.78|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Grocery delivery/debit/IDR|3|827796.8, 579382.21, 500190.37|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Supermarket basket/debit/IDR|3|666549.86, 779682.2, 639007.61|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Bulk pantry shop/debit/IDR|4|799494.14, 766454.92, 831303.1, 813836.79|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Neighbourhood grocer/debit/IDR|5|643753.91, 809114.11, 813723.53, 510985.32, 790188.39|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_89|groceries/Fresh food shop/debit/IDR|2|751911.36, 677807.03|repeated but not demonstrably recurrent|||
|user_89|transport/Local taxi/debit/IDR|5|396601.34, 367879.81, 416667.79, 449393.9, 432108.51|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_89|transport/Parking and tolls/debit/IDR|4|305934.75, 460534.85, 500636.51, 315413.6|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_89|transport/Ride-hailing trip/debit/IDR|2|438170.06, 414876.97|repeated but not demonstrably recurrent|||
|user_89|transport/Rail pass/debit/IDR|2|486026.05, 479737.83|repeated but not demonstrably recurrent|||
|user_89|transport/Fuel refill/debit/IDR|5|332746.99, 428135.9, 480303.5, 413001.48, 473510.05|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_89|transport/Metro and bus fares/debit/IDR|3|337606.68, 327341.18, 383645.89|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_89|transport/Commuter pass/debit/IDR|2|453569.88, 454552.67|repeated but not demonstrably recurrent|||
|user_89|transport/Vehicle charging/debit/IDR|3|423713.81, 421539.64, 501078.1|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_89|dining/Coffee shop/debit/IDR|5|334559.91, 358047.32, 391334.77, 494494.24, 441897.24|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_89|dining/Weekend food delivery/debit/IDR|2|461705.7, 451183.13|repeated but not demonstrably recurrent|||
|user_89|dining/Family dinner/debit/IDR|2|435168.84, 499883.79|repeated but not demonstrably recurrent|||
|user_90|salary/Consulting invoice payment/credit/ZAR|2|6335.02, 5057.14|repeated but not demonstrably recurrent|||
|user_90|salary/Content contract payment/credit/ZAR|2|8162.86, 8558.54|repeated but not demonstrably recurrent|||
|user_90|rent/Monthly rent/debit/ZAR|6|3234, 3234, 3234, 3234, 3234, 3234|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_90|utilities/Electricity and water bill/debit/ZAR|5|656.36, 707.42, 735.95, 653.69, 687.32|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_90|cloud_storage/Cloud storage plan/debit/ZAR|5|106.7, 106.7, 106.7, 106.7, 106.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_90|streaming/Streaming subscription/debit/ZAR|5|387.2, 387.2, 387.2, 387.2, 387.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_90|shopping/Personal shopping/debit/ZAR|5|528.8, 633.05, 534.89, 531.32, 588.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_90|salary/Website project payment/credit/ZAR|2|8046.82, 5218.77|repeated but not demonstrably recurrent|||
|user_90|salary/Independent work payment/credit/ZAR|3|5891.87, 4701.54, 5651.46|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_90|groceries/Grocery delivery/debit/ZAR|4|411.11, 402.98, 660.57, 486.35|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_90|groceries/Household groceries/debit/ZAR|4|649.34, 545.34, 561.68, 546.45|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_90|groceries/Fresh food shop/debit/ZAR|3|489.4, 448.58, 574.06|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_90|groceries/Neighbourhood grocer/debit/ZAR|2|432.31, 473.25|repeated but not demonstrably recurrent|||
|user_90|groceries/Bulk pantry shop/debit/ZAR|2|477.99, 508.5|repeated but not demonstrably recurrent|||
|user_90|groceries/Local market purchase/debit/ZAR|2|614.9, 623.22|repeated but not demonstrably recurrent|||
|user_90|transport/Vehicle charging/debit/ZAR|4|316.12, 448.67, 311.63, 357.77|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_90|transport/Commuter pass/debit/ZAR|3|389.58, 308.5, 441.64|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_90|dining/Bakery and snacks/debit/ZAR|3|428.76, 633.18, 423.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_90|dining/Neighbourhood restaurant/debit/ZAR|2|515.02, 498.58|repeated but not demonstrably recurrent|||
|user_91|salary/Payroll credit/credit/EUR|5|2387, 2387, 2387, 2387, 2387|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_91|rent/Shared housing rent/debit/EUR|5|695.2, 695.2, 695.2, 695.2, 695.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_91|utilities/Electricity bill/debit/EUR|5|154.74, 171.62, 156.12, 178.65, 168.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_91|debt_repayment/Education loan instalment/debit/EUR|5|170, 170, 170, 170, 170|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_91|streaming/Streaming subscription/debit/EUR|5|48, 48, 48, 48, 48|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_91|cloud_storage/Online backup subscription/debit/EUR|5|21, 21, 21, 21, 21|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_91|shopping/Online retail purchases/debit/EUR|5|95.13, 107.11, 112.67, 105.04, 112.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_91|groceries/Bulk pantry shop/debit/EUR|5|129.07, 122.2, 90.09, 130.37, 85.4|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_91|groceries/Household groceries/debit/EUR|4|99.82, 106.79, 81, 123.15|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_91|groceries/Neighbourhood grocer/debit/EUR|3|120.96, 91.41, 93.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_91|groceries/Weekly produce market/debit/EUR|5|123.98, 126.55, 109.9, 122.77, 133.17|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_91|groceries/Fresh food shop/debit/EUR|2|135.62, 84.9|repeated but not demonstrably recurrent|||
|user_91|groceries/Local market purchase/debit/EUR|4|92.83, 125.61, 111.77, 119.81|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_91|transport/Parking and tolls/debit/EUR|3|43.44, 38.12, 60.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_91|transport/Rail pass/debit/EUR|2|63.63, 54.42|repeated but not demonstrably recurrent|||
|user_91|transport/Commuter pass/debit/EUR|3|43.57, 54.07, 51.93|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_91|transport/Metro and bus fares/debit/EUR|2|48.55, 63.07|repeated but not demonstrably recurrent|||
|user_91|transport/Fuel refill/debit/EUR|5|66.1, 42.91, 47.9, 42.91, 39.98|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_91|transport/Vehicle charging/debit/EUR|3|64.16, 57.12, 61.25|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_91|transport/Ride-hailing trip/debit/EUR|3|61.95, 45.02, 45.63|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_91|transport/Local taxi/debit/EUR|4|56.5, 57.43, 46.21, 65.66|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_91|dining/Neighbourhood restaurant/debit/EUR|3|108.09, 100.67, 75.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_91|dining/Bakery and snacks/debit/EUR|3|90.63, 114.67, 82.7|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_91|dining/Family dinner/debit/EUR|2|114.32, 76.26|repeated but not demonstrably recurrent|||
|user_91|dining/Weekend food delivery/debit/EUR|2|97.74, 110|repeated but not demonstrably recurrent|||
|user_92|salary/Base salary/credit/ZAR|5|29568, 29568, 29568, 29568, 29568|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_92|housing/Home association fee/debit/ZAR|6|3762, 3762, 3762, 3762, 3762, 3762|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_92|utilities/Energy provider bill/debit/ZAR|5|2742.93, 2579.43, 2669.24, 2341.04, 2739.46|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_92|insurance/Health insurance premium/debit/ZAR|5|1606, 1606, 1606, 1606, 1606|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_92|education/Child education fee/debit/ZAR|5|2939.2, 2939.2, 2939.2, 2939.2, 2939.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_92|healthcare/Clinic payment/debit/ZAR|5|3474.75, 3123.86, 3127.6, 3197.82, 3137.83|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_92|entertainment/Local event tickets/debit/ZAR|5|1176.59, 1025.78, 1100.6, 1055.42, 1143.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_92|cloud_storage/Shared storage plan/debit/ZAR|5|150.7, 150.7, 150.7, 150.7, 150.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_92|salary/Monthly sales commission/credit/ZAR|3|23173.06, 27435, 10916.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_92|groceries/Weekly produce market/debit/ZAR|2|2561.71, 1992.52|repeated but not demonstrably recurrent|||
|user_92|groceries/Fresh food shop/debit/ZAR|4|1632.28, 1994.07, 1462.56, 1710.34|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_92|groceries/Grocery delivery/debit/ZAR|2|1699.94, 1826.47|repeated but not demonstrably recurrent|||
|user_92|groceries/Household groceries/debit/ZAR|3|1875.09, 2209.47, 1955.04|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_92|groceries/Local market purchase/debit/ZAR|4|1708.36, 1978.16, 2003.51, 2087.47|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_92|groceries/Neighbourhood grocer/debit/ZAR|3|1857.54, 2534.61, 2061.87|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_92|transport/Local taxi/debit/ZAR|4|1299.01, 1552.19, 1576.63, 1271.19|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_92|transport/Commuter pass/debit/ZAR|4|1398.87, 1108.41, 1149.83, 1478.73|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_92|transport/Rail pass/debit/ZAR|2|942.03, 1070.63|repeated but not demonstrably recurrent|||
|user_92|dining/Weekend food delivery/debit/ZAR|2|1457.98, 2330.57|repeated but not demonstrably recurrent|||
|user_92|dining/Family dinner/debit/ZAR|3|2009.2, 1557.67, 1535.43|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_92|dining/Quick-service meal/debit/ZAR|3|1945.37, 1810.6, 1995.74|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_93|salary/Payroll credit/credit/USD|5|2412, 2412, 2412, 2412, 2412|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_93|rent/Apartment rent transfer/debit/USD|6|808.8, 808.8, 808.8, 808.8, 808.8, 808.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_93|utilities/Electricity bill/debit/USD|6|102.26, 123.19, 123.81, 117.5, 109.41, 109.22|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_93|cloud_storage/Online backup subscription/debit/USD|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_93|streaming/Video streaming plan/debit/USD|5|59, 59, 59, 59, 59|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_93|shopping/Online retail purchases/debit/USD|5|60, 69.12, 61.24, 72.53, 73.43|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_93|groceries/Supermarket basket/debit/USD|4|80.66, 109.54, 115.55, 76.52|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_93|groceries/Weekly produce market/debit/USD|4|90.35, 78.46, 81.12, 93|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_93|groceries/Neighbourhood grocer/debit/USD|3|94.79, 95.7, 108.14|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_93|groceries/Fresh food shop/debit/USD|2|79.6, 112.52|repeated but not demonstrably recurrent|||
|user_93|groceries/Grocery delivery/debit/USD|3|89.36, 117.48, 108.18|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_93|groceries/Household groceries/debit/USD|2|88.3, 73.81|repeated but not demonstrably recurrent|||
|user_93|transport/Ride-hailing trip/debit/USD|2|58.4, 47.62|repeated but not demonstrably recurrent|||
|user_93|transport/Fuel refill/debit/USD|2|73.72, 69.53|repeated but not demonstrably recurrent|||
|user_93|transport/Vehicle charging/debit/USD|2|50.04, 67.85|repeated but not demonstrably recurrent|||
|user_93|transport/Local taxi/debit/USD|2|68.59, 70.24|repeated but not demonstrably recurrent|||
|user_93|dining/Lunch with colleagues/debit/USD|2|91.12, 86.52|repeated but not demonstrably recurrent|||
|user_93|dining/Coffee shop/debit/USD|3|109.2, 80.25, 101.33|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_94|salary/Design contract payment/credit/EUR|2|519.12, 508.44|repeated but not demonstrably recurrent|||
|user_94|rent/Monthly rent/debit/EUR|6|287.1, 287.1, 287.1, 287.1, 287.1, 287.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_94|utilities/Municipal utilities/debit/EUR|5|50.02, 51.75, 56.92, 49.91, 53.21|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_94|cloud_storage/Shared storage plan/debit/EUR|5|7, 7, 7, 7, 7|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_94|streaming/Streaming subscription/debit/EUR|5|28, 28, 28, 28, 28|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_94|shopping/Clothing and household items/debit/EUR|5|46.2, 50.31, 50.56, 47.62, 48.16|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_94|salary/Consulting invoice payment/credit/EUR|2|376.35, 524.45|repeated but not demonstrably recurrent|||
|user_94|salary/Client retainer payment/credit/EUR|2|309.79, 387.16|repeated but not demonstrably recurrent|||
|user_94|groceries/Household groceries/debit/EUR|5|32.16, 40.24, 49.57, 48.16, 39.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_94|groceries/Supermarket basket/debit/EUR|3|42.29, 34.53, 55.03|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_94|groceries/Weekly produce market/debit/EUR|3|53.71, 33.71, 54.08|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_94|groceries/Local market purchase/debit/EUR|4|52.45, 34.35, 32.32, 46.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_94|transport/Commuter pass/debit/EUR|2|13.95, 18.42|repeated but not demonstrably recurrent|||
|user_94|transport/Parking and tolls/debit/EUR|4|16.55, 13.57, 13.78, 18.44|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_94|dining/Quick-service meal/debit/EUR|2|37.13, 48.38|repeated but not demonstrably recurrent|||
|user_94|dining/Takeaway order/debit/EUR|2|37.96, 40.23|repeated but not demonstrably recurrent|||
|user_94|dining/Family dinner/debit/EUR|3|31.81, 50.11, 48.01|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_94|dining/Neighbourhood restaurant/debit/EUR|2|48.27, 41.68|repeated but not demonstrably recurrent|||
|user_95|salary/Payroll credit/credit/INR|5|251000, 251000, 251000, 251000, 251000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_95|rent/Residential rent payment/debit/INR|6|62900, 62900, 62900, 62900, 62900, 62900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_95|utilities/Municipal utilities/debit/INR|5|14267.39, 15545.89, 14364.32, 14076.96, 14004.78|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_95|debt_repayment/Vehicle loan payment/debit/INR|5|37900, 37900, 37900, 37900, 37900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_95|healthcare/Therapy appointment/debit/INR|5|15086.66, 15545.1, 14519.05, 15809.42, 16130.1|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_95|family_support/Childcare contribution/debit/INR|5|21620, 21620, 21620, 21620, 21620|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_95|cloud_storage/Online backup subscription/debit/INR|5|1925, 1925, 1925, 1925, 1925|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_95|shopping/Monthly shopping spend/debit/INR|5|8964.74, 9872.8, 8337.78, 9870.21, 8279.95|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_95|groceries/Household groceries/debit/INR|5|9145.27, 6704.37, 7220.42, 10349.88, 7076.32|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_95|groceries/Grocery delivery/debit/INR|3|9833.77, 9830.1, 7906.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_95|groceries/Supermarket basket/debit/INR|3|10818.62, 8508.07, 7346.2|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_95|groceries/Weekly produce market/debit/INR|2|10694.76, 6385.89|repeated but not demonstrably recurrent|||
|user_95|groceries/Local market purchase/debit/INR|5|7793, 9963.12, 9169.44, 11214.6, 7986.81|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_95|groceries/Neighbourhood grocer/debit/INR|3|10299.12, 8156.25, 10659.54|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_95|groceries/Fresh food shop/debit/INR|3|7010.09, 7882.11, 9284.88|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_95|transport/Parking and tolls/debit/INR|2|6337.3, 4959.81|repeated but not demonstrably recurrent|||
|user_95|transport/Metro and bus fares/debit/INR|3|4663.05, 6371.57, 6136.79|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_95|transport/Commuter pass/debit/INR|3|5298.31, 7014.37, 4983.81|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_95|transport/Vehicle charging/debit/INR|2|7374.94, 7858.86|repeated but not demonstrably recurrent|||
|user_96|rent/Apartment rent transfer/debit/INR|6|21400, 21400, 21400, 21400, 21400, 21400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_96|utilities/Municipal utilities/debit/INR|5|5453.24, 4428.84, 5230.2, 4929.42, 5431.14|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_96|education/Child education fee/debit/INR|5|5260, 5260, 5260, 5260, 5260|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_96|debt_repayment/Loan repayment/debit/INR|5|7900, 7900, 7900, 7900, 7900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_96|music_subscription/Music service subscription/debit/INR|5|1005, 1005, 1005, 1005, 1005|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_96|delivery_membership/Food delivery membership/debit/INR|5|775, 775, 775, 775, 775|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_96|salary/First-job payroll/credit/INR|2|80000, 80000|repeated but not demonstrably recurrent|||
|user_96|groceries/Grocery delivery/debit/INR|6|3160.78, 2722.81, 3653.91, 3048.18, 4456.78, 2842.26|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_96|groceries/Household groceries/debit/INR|4|3415.26, 4452.11, 3877.74, 2766.73|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_96|groceries/Fresh food shop/debit/INR|4|3818.52, 4178.68, 3883.37, 3705.61|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_96|groceries/Bulk pantry shop/debit/INR|6|2674.49, 3668.53, 3393.19, 4421.92, 4477.24, 2922.68|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_96|groceries/Local market purchase/debit/INR|3|4240.75, 4418.22, 3542.7|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_96|groceries/Weekly produce market/debit/INR|2|4700.18, 2703.04|repeated but not demonstrably recurrent|||
|user_96|transport/Local taxi/debit/INR|5|1845.8, 1497.72, 1919.66, 1637.82, 1309.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_96|transport/Metro and bus fares/debit/INR|6|1501.97, 2125.43, 1399.21, 2022.24, 1388.97, 2262.96|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_96|transport/Commuter pass/debit/INR|2|1897.81, 1574.14|repeated but not demonstrably recurrent|||
|user_96|transport/Rail pass/debit/INR|2|1606.85, 1922.56|repeated but not demonstrably recurrent|||
|user_96|transport/Parking and tolls/debit/INR|4|1453.26, 1696.38, 1893.64, 2284.88|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_96|transport/Vehicle charging/debit/INR|3|1803.54, 2153.84, 1636.74|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_96|transport/Ride-hailing trip/debit/INR|3|1309.72, 2156.67, 2176.77|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_96|dining/Weekend food delivery/debit/INR|2|2384.33, 3499.8|repeated but not demonstrably recurrent|||
|user_96|dining/Quick-service meal/debit/INR|3|3901.59, 3546.88, 3298.64|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_96|dining/Lunch with colleagues/debit/INR|4|2464.89, 3334.73, 3996.78, 3235.38|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_96|dining/Neighbourhood restaurant/debit/INR|2|2650.36, 3348.7|repeated but not demonstrably recurrent|||
|user_97|salary/Previous employer payroll/credit/ZAR|4|35420, 35420, 35420, 35420|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_97|rent/Landlord standing order/debit/ZAR|6|11792, 11792, 11792, 11792, 11792, 11792|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_97|utilities/Water and power payment/debit/ZAR|5|2080.64, 1763.97, 2205.47, 2155.74, 2186.55|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_97|debt_repayment/Loan repayment/debit/ZAR|5|3531, 3531, 3531, 3531, 3531|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_97|music_subscription/Audio streaming plan/debit/ZAR|5|218.9, 218.9, 218.9, 218.9, 218.9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_97|groceries/Bulk pantry shop/debit/ZAR|3|1116.12, 1159.6, 1056.37|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_97|groceries/Household groceries/debit/ZAR|4|1748.99, 1587.5, 1705.34, 1095.57|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_97|groceries/Grocery delivery/debit/ZAR|3|1625.34, 1681.01, 1284.98|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_97|groceries/Neighbourhood grocer/debit/ZAR|2|1433.44, 1505.89|repeated but not demonstrably recurrent|||
|user_97|transport/Vehicle charging/debit/ZAR|2|880.21, 661.86|repeated but not demonstrably recurrent|||
|user_97|transport/Rail pass/debit/ZAR|2|845.74, 618.31|repeated but not demonstrably recurrent|||
|user_97|transport/Fuel refill/debit/ZAR|4|1008.01, 670.07, 859.92, 932.14|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_97|dining/Lunch with colleagues/debit/ZAR|2|1077.34, 1187.4|repeated but not demonstrably recurrent|||
|user_97|dining/Family dinner/debit/ZAR|3|1435.2, 946.09, 1188.51|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_98|salary/International employer payroll/credit/EUR|5|36080, 36080, 36080, 36080, 36080|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_98|rent/Residential rent payment/debit/ZAR|6|7986, 7986, 7986, 7986, 7986, 7986|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_98|utilities/Energy provider bill/debit/ZAR|5|1933.21, 1831.3, 1822.5, 1928.74, 2109.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_98|insurance/Vehicle insurance premium/debit/ZAR|5|1766.6, 1766.6, 1766.6, 1766.6, 1766.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_98|cloud_storage/Shared storage plan/debit/ZAR|5|192.5, 192.5, 192.5, 192.5, 192.5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_98|streaming/Video streaming plan/debit/ZAR|5|684.2, 684.2, 684.2, 684.2, 684.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_98|shopping/Household shopping/debit/ZAR|5|1419.53, 1394.94, 1249.65, 1512.37, 1332.22|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_98|entertainment/Games and recreation/debit/ZAR|5|1188.48, 1281.59, 1127.26, 1255.7, 1371.15|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_98|groceries/Supermarket basket/debit/ZAR|2|1372.2, 1187.98|repeated but not demonstrably recurrent|||
|user_98|groceries/Weekly produce market/debit/ZAR|3|1582.25, 1646.8, 1329.75|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_98|groceries/Household groceries/debit/ZAR|4|1415, 1762.55, 1684.03, 1932.51|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_98|groceries/Grocery delivery/debit/ZAR|3|1403.77, 1459.28, 1257.2|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_98|groceries/Bulk pantry shop/debit/ZAR|3|1265.86, 2009.75, 1404.14|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Ride-hailing trip/debit/ZAR|3|1076.61, 880.93, 737.21|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Local taxi/debit/ZAR|11|733.48, 1235.43, 925.4, 987.83, 802.39, 1096.76, 846.11, 1084.42, 1134.5, 1095.96, 995.52|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Commuter pass/debit/ZAR|4|873.39, 716.6, 878.68, 714.64|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Vehicle charging/debit/ZAR|3|856.2, 1022.58, 1056.51|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Rail pass/debit/ZAR|2|916.97, 738.17|repeated but not demonstrably recurrent|||
|user_98|transport/Fuel refill/debit/ZAR|3|845.24, 1164.41, 811.68|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Parking and tolls/debit/ZAR|7|1263.95, 1179.56, 764.87, 939.57, 812.02, 1253.89, 1013.11|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_98|transport/Metro and bus fares/debit/ZAR|2|910.21, 831.41|repeated but not demonstrably recurrent|||
|user_98|dining/Quick-service meal/debit/ZAR|5|1621.76, 1586.55, 997.56, 1318.2, 1168.95|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_98|dining/Family dinner/debit/ZAR|2|1480.63, 1506.68|repeated but not demonstrably recurrent|||
|user_98|dining/Weekend food delivery/debit/ZAR|3|1598.17, 1669.14, 1610.71|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_98|dining/Coffee shop/debit/ZAR|6|1194.36, 980.87, 1011.08, 1409.85, 1381.61, 1558|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_98|dining/Bakery and snacks/debit/ZAR|3|1525.6, 1533.43, 1216.68|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_98|dining/Lunch with colleagues/debit/ZAR|2|1053.69, 998.76|repeated but not demonstrably recurrent|||
|user_98|dining/Takeaway order/debit/ZAR|3|1478.81, 1245, 1144.66|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_99|salary/Payroll credit/credit/ZAR|5|44444.4, 44444.4, 44444.4, 44444.4, 44444.4|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_99|housing/Building maintenance payment/debit/ZAR|5|5115, 5115, 5115, 5115, 5115|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_99|utilities/Water and power payment/debit/ZAR|5|3965.98, 4308, 4266.19, 4140.28, 3655.51|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_99|insurance/Vehicle insurance premium/debit/ZAR|5|1522.4, 1522.4, 1522.4, 1522.4, 1522.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_99|healthcare/Therapy appointment/debit/ZAR|5|2762.75, 2315.88, 2621.3, 2674.06, 2690.86|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_99|streaming/Family streaming plan/debit/ZAR|5|1051.6, 1051.6, 1051.6, 1051.6, 1051.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_99|groceries/Household groceries/debit/ZAR|3|2748.12, 2465.96, 3295.37|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_99|groceries/Fresh food shop/debit/ZAR|2|2799.92, 3040.43|repeated but not demonstrably recurrent|||
|user_99|groceries/Grocery delivery/debit/ZAR|5|2961.64, 2538.82, 3116.66, 2136.92, 3266.74|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_99|groceries/Local market purchase/debit/ZAR|4|2405.31, 3275.36, 2419.85, 2601.07|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_99|groceries/Bulk pantry shop/debit/ZAR|2|1890.23, 2424.03|repeated but not demonstrably recurrent|||
|user_99|transport/Ride-hailing trip/debit/ZAR|3|1292.51, 1146.42, 835.89|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_99|transport/Local taxi/debit/ZAR|2|906.43, 1018.9|repeated but not demonstrably recurrent|||
|user_99|transport/Parking and tolls/debit/ZAR|2|1259.55, 1340.59|repeated but not demonstrably recurrent|||
|user_99|transport/Fuel refill/debit/ZAR|3|827.19, 1080.9, 1032.8|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_99|transport/Rail pass/debit/ZAR|3|831.65, 1115.86, 865.35|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_99|dining/Family dinner/debit/ZAR|4|1869.1, 2286.56, 1881.93, 2380.77|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_99|dining/Bakery and snacks/debit/ZAR|3|2118.56, 2619.17, 2159.84|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_99|dining/Weekend food delivery/debit/ZAR|4|1975.07, 1822.66, 1729.8, 2002.73|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_100|salary/Payroll credit/credit/ZAR|5|42680, 42680, 42680, 42680, 42680|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_100|rent/Apartment rent transfer/debit/ZAR|6|12716, 12716, 12716, 12716, 12716, 12716|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_100|utilities/Municipal utilities/debit/ZAR|6|2995.95, 2505.98, 2455.32, 2953.25, 2514.48, 2522.13|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_100|debt_repayment/Personal loan payment/debit/ZAR|5|2222, 2222, 2222, 2222, 2222|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_100|streaming/Streaming subscription/debit/ZAR|5|1016.4, 1016.4, 1016.4, 1016.4, 1016.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_100|cloud_storage/Shared storage plan/debit/ZAR|5|238.7, 238.7, 238.7, 238.7, 238.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_100|shopping/Household shopping/debit/ZAR|5|1826.81, 1868.05, 1735.99, 1742.28, 1742.86|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_100|groceries/Local market purchase/debit/ZAR|2|2091.8, 1689.79|repeated but not demonstrably recurrent|||
|user_100|groceries/Weekly produce market/debit/ZAR|4|1715.74, 1905.58, 2470.13, 1978.03|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_100|groceries/Neighbourhood grocer/debit/ZAR|4|2483.66, 1862.05, 2502.08, 1489.03|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_100|groceries/Fresh food shop/debit/ZAR|7|2180.43, 2080.99, 1630.34, 1745.45, 2308.53, 2384.31, 1461.82|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_100|groceries/Bulk pantry shop/debit/ZAR|4|1845.36, 2361.33, 1531.21, 1460.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_100|groceries/Supermarket basket/debit/ZAR|2|1615.66, 2549.51|repeated but not demonstrably recurrent|||
|user_100|groceries/Household groceries/debit/ZAR|2|2034.93, 2059.78|repeated but not demonstrably recurrent|||
|user_100|transport/Metro and bus fares/debit/ZAR|6|877.33, 724.49, 958.51, 857.71, 901.81, 661.32|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_100|transport/Parking and tolls/debit/ZAR|2|975.22, 918.29|repeated but not demonstrably recurrent|||
|user_100|transport/Commuter pass/debit/ZAR|3|642, 676.47, 904.4|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_100|transport/Ride-hailing trip/debit/ZAR|3|602.69, 756.55, 727.25|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_100|transport/Vehicle charging/debit/ZAR|2|861.7, 921.39|repeated but not demonstrably recurrent|||
|user_100|transport/Local taxi/debit/ZAR|2|769.26, 1010.36|repeated but not demonstrably recurrent|||
|user_100|transport/Fuel refill/debit/ZAR|3|755.67, 705.81, 948.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_100|transport/Rail pass/debit/ZAR|5|966.12, 878.28, 742, 637.48, 856.5|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_100|dining/Coffee shop/debit/ZAR|3|1734.95, 1434.93, 1402.48|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_100|dining/Takeaway order/debit/ZAR|2|1913.77, 1685.94|repeated but not demonstrably recurrent|||
|user_100|dining/Family dinner/debit/ZAR|2|1630.55, 2015.19|repeated but not demonstrably recurrent|||
|user_100|dining/Neighbourhood restaurant/debit/ZAR|2|1481.09, 1997.75|repeated but not demonstrably recurrent|||
|user_100|dining/Weekend food delivery/debit/ZAR|3|1793.99, 1289.67, 1255.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_101|salary/Payroll credit/credit/INR|5|254000, 254000, 254000, 254000, 254000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_101|housing/Property maintenance contribution/debit/INR|5|30050, 30050, 30050, 30050, 30050|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_101|utilities/Household utility payment/debit/INR|5|15241.17, 13273.01, 16002.55, 14626.59, 14756.34|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_101|insurance/Health insurance premium/debit/INR|5|9470, 9470, 9470, 9470, 9470|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_101|education/Child education fee/debit/INR|5|25020, 25020, 25020, 25020, 25020|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_101|healthcare/Diagnostic test/debit/INR|5|9509.61, 10213.89, 10657.14, 9429.82, 9351.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_101|entertainment/Monthly entertainment spend/debit/INR|5|4698.74, 5456.3, 5758.84, 5693.25, 5692.37|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_101|cloud_storage/Online backup subscription/debit/INR|5|1985, 1985, 1985, 1985, 1985|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_101|groceries/Bulk pantry shop/debit/INR|4|7758.03, 10539.28, 7626.89, 9611.15|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_101|groceries/Supermarket basket/debit/INR|2|8339.77, 8829.16|repeated but not demonstrably recurrent|||
|user_101|groceries/Household groceries/debit/INR|2|8559.29, 7662.76|repeated but not demonstrably recurrent|||
|user_101|groceries/Grocery delivery/debit/INR|3|6898.76, 10520.24, 9284.83|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_101|groceries/Weekly produce market/debit/INR|4|9628.7, 10599.26, 11448.89, 9843.13|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_101|transport/Local taxi/debit/INR|2|7075.65, 7350.51|repeated but not demonstrably recurrent|||
|user_101|transport/Rail pass/debit/INR|3|7920.95, 5148.1, 6388.48|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_101|transport/Fuel refill/debit/INR|2|7053.33, 6205.3|repeated but not demonstrably recurrent|||
|user_101|transport/Parking and tolls/debit/INR|2|6584.88, 6706.8|repeated but not demonstrably recurrent|||
|user_101|transport/Vehicle charging/debit/INR|2|6120.3, 5313.26|repeated but not demonstrably recurrent|||
|user_101|transport/Ride-hailing trip/debit/INR|2|6453.41, 4862.87|repeated but not demonstrably recurrent|||
|user_101|dining/Quick-service meal/debit/INR|3|7539.2, 9431.1, 8440.53|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_101|dining/Neighbourhood restaurant/debit/INR|2|10731.05, 9953.77|repeated but not demonstrably recurrent|||
|user_101|dining/Bakery and snacks/debit/INR|2|8799.07, 6531.97|repeated but not demonstrably recurrent|||
|user_101|dining/Takeaway order/debit/INR|2|7770.21, 8604.7|repeated but not demonstrably recurrent|||
|user_102|salary/Application project payment/credit/EUR|2|723.56, 697.81|repeated but not demonstrably recurrent|||
|user_102|rent/Shared housing rent/debit/EUR|6|345.4, 345.4, 345.4, 345.4, 345.4, 345.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_102|utilities/Energy provider bill/debit/EUR|5|62.68, 60.24, 61.28, 60.43, 74.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_102|cloud_storage/Online backup subscription/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_102|streaming/Family streaming plan/debit/EUR|5|35, 35, 35, 35, 35|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_102|shopping/Household shopping/debit/EUR|5|66.94, 62.58, 66.83, 57.81, 62.9|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_102|salary/Freelance milestone payment/credit/EUR|2|579.45, 726.88|repeated but not demonstrably recurrent|||
|user_102|salary/Website project payment/credit/EUR|2|477.3, 562.7|repeated but not demonstrably recurrent|||
|user_102|salary/Content contract payment/credit/EUR|2|756.86, 848.7|repeated but not demonstrably recurrent|||
|user_102|groceries/Household groceries/debit/EUR|5|46.4, 70.3, 43.35, 50.19, 48.53|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_102|groceries/Fresh food shop/debit/EUR|2|43.58, 58.78|repeated but not demonstrably recurrent|||
|user_102|groceries/Neighbourhood grocer/debit/EUR|3|60.01, 47.95, 66.28|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_102|groceries/Weekly produce market/debit/EUR|3|55.38, 48.88, 65.93|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_102|groceries/Local market purchase/debit/EUR|2|43.77, 56.43|repeated but not demonstrably recurrent|||
|user_102|transport/Local taxi/debit/EUR|2|35.51, 32.43|repeated but not demonstrably recurrent|||
|user_102|transport/Metro and bus fares/debit/EUR|3|27.11, 25.94, 35.23|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_102|transport/Commuter pass/debit/EUR|3|41.68, 33.85, 26.57|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_102|dining/Quick-service meal/debit/EUR|2|45.58, 47.13|repeated but not demonstrably recurrent|||
|user_102|dining/Neighbourhood restaurant/debit/EUR|2|28.63, 38.39|repeated but not demonstrably recurrent|||
|user_102|dining/Weekend food delivery/debit/EUR|3|39.7, 33.2, 30.51|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_102|dining/Takeaway order/debit/EUR|2|47.57, 29.32|repeated but not demonstrably recurrent|||
|user_103|salary/Payroll credit/credit/INR|5|229000, 229000, 229000, 164880, 164880|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_103|rent/Monthly rent/debit/INR|6|53400, 53400, 53400, 53400, 53400, 53400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_103|utilities/Household utility payment/debit/INR|5|7721.54, 8095.92, 8313.58, 7382.03, 8912.34|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_103|music_subscription/Music subscription/debit/INR|5|995, 995, 995, 995, 995|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_103|delivery_membership/Grocery delivery membership/debit/INR|5|1755, 1755, 1755, 1755, 1755|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_103|gym/Community fitness plan/debit/INR|5|4140, 4140, 4140, 4140, 4140|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_103|entertainment/Games and recreation/debit/INR|5|6752.45, 6704.24, 6299.7, 6151.21, 6393.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_103|groceries/Weekly produce market/debit/INR|2|7731.01, 7671.2|repeated but not demonstrably recurrent|||
|user_103|groceries/Household groceries/debit/INR|4|7753.66, 7204.05, 4526.18, 7164.58|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_103|groceries/Supermarket basket/debit/INR|2|4430.16, 5030.58|repeated but not demonstrably recurrent|||
|user_103|groceries/Bulk pantry shop/debit/INR|4|7484.72, 5444.47, 6199.92, 6726.46|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_103|groceries/Grocery delivery/debit/INR|4|6644.83, 6677.81, 7263.62, 5478.04|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_103|groceries/Local market purchase/debit/INR|6|5656.14, 7371.07, 6534.34, 4632.66, 6407.98, 4638.69|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_103|groceries/Fresh food shop/debit/INR|2|6050.09, 5576.66|repeated but not demonstrably recurrent|||
|user_103|transport/Ride-hailing trip/debit/INR|3|3983.86, 3752.46, 2868.74|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_103|transport/Commuter pass/debit/INR|5|3560.47, 3288.05, 3376.72, 3513.39, 3329.19|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_103|transport/Local taxi/debit/INR|3|3733.14, 2889.51, 3560.5|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_103|transport/Rail pass/debit/INR|5|3339.13, 3405.44, 2926.3, 3359.09, 4423.99|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_103|transport/Vehicle charging/debit/INR|3|3874.96, 3112.64, 2497.9|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_103|transport/Parking and tolls/debit/INR|4|3308.98, 3550.95, 3683.22, 2774.18|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_103|dining/Family dinner/debit/INR|2|5665.51, 4619.99|repeated but not demonstrably recurrent|||
|user_103|dining/Neighbourhood restaurant/debit/INR|2|5342.09, 4183.14|repeated but not demonstrably recurrent|||
|user_103|dining/Lunch with colleagues/debit/INR|3|4632.35, 4143.79, 5097.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_103|dining/Coffee shop/debit/INR|3|3326.08, 3366.1, 3602.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_104|salary/Base salary/credit/ZAR|5|21516, 21516, 21516, 21516, 21516|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_104|rent/Apartment rent transfer/debit/ZAR|6|7920, 7920, 7920, 7920, 7920, 7920|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_104|utilities/Energy provider bill/debit/ZAR|5|2497.65, 2163.23, 2422.97, 2341.92, 2314|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_104|debt_repayment/Vehicle loan payment/debit/ZAR|5|5093, 5093, 5093, 5093, 5093|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_104|healthcare/Regular medicine purchase/debit/ZAR|5|2155.15, 2027.23, 2256.49, 2230.6, 2467.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_104|family_support/Family support payment/debit/ZAR|5|2323.2, 2323.2, 2323.2, 2323.2, 2323.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_104|cloud_storage/Online backup subscription/debit/ZAR|5|214.5, 214.5, 214.5, 214.5, 214.5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_104|shopping/Personal shopping/debit/ZAR|5|839.99, 829.48, 800.17, 778.79, 731.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_104|salary/Account commission payment/credit/ZAR|3|7634.57, 16401.99, 20060.26|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_104|groceries/Weekly produce market/debit/ZAR|2|1712.45, 1717.73|repeated but not demonstrably recurrent|||
|user_104|groceries/Grocery delivery/debit/ZAR|3|1004.35, 1595.13, 1490.08|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_104|groceries/Bulk pantry shop/debit/ZAR|2|1666.53, 1648.87|repeated but not demonstrably recurrent|||
|user_104|groceries/Local market purchase/debit/ZAR|5|1083.92, 1144.86, 1241.83, 1244.72, 1146.3|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_104|groceries/Supermarket basket/debit/ZAR|5|1004.28, 1062.11, 1169.71, 1427.81, 1356.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_104|groceries/Fresh food shop/debit/ZAR|7|1046.03, 1420.66, 1121.14, 1427.66, 1582.37, 1737.79, 1562.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_104|transport/Metro and bus fares/debit/ZAR|3|835.26, 1188.79, 1195.69|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_104|transport/Ride-hailing trip/debit/ZAR|2|910.69, 976.16|repeated but not demonstrably recurrent|||
|user_104|transport/Rail pass/debit/ZAR|2|961.71, 769.96|repeated but not demonstrably recurrent|||
|user_104|transport/Commuter pass/debit/ZAR|3|734.58, 933.76, 951.84|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_105|salary/Payroll credit/credit/INR|5|117000, 117000, 117000, 117000, 117000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_105|rent/Apartment rent transfer/debit/INR|6|31200, 31200, 31200, 31200, 31200, 31200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_105|utilities/Water and power payment/debit/INR|6|5658.42, 5699.9, 6609.44, 6847.76, 6072.91, 6178.74|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_105|insurance/Household insurance/debit/INR|6|3760, 3760, 3760, 3760, 3760, 3760|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_105|cloud_storage/Online backup subscription/debit/INR|5|405, 405, 405, 405, 405|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_105|streaming/Streaming subscription/debit/INR|5|3360, 3360, 3360, 3360, 3360|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_105|shopping/Household shopping/debit/INR|5|3634.89, 4530.01, 3992.96, 3827.75, 4094.05|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_105|entertainment/Monthly entertainment spend/debit/INR|5|3721.95, 3799.96, 3787.57, 3270.04, 3084.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_105|groceries/Grocery delivery/debit/INR|3|5785.57, 4759.27, 6356.21|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_105|groceries/Supermarket basket/debit/INR|4|6311.56, 4540.44, 5651.07, 4891.23|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_105|groceries/Bulk pantry shop/debit/INR|2|4140.82, 3748.71|repeated but not demonstrably recurrent|||
|user_105|groceries/Neighbourhood grocer/debit/INR|3|4909.7, 4151.15, 4418.41|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_105|groceries/Fresh food shop/debit/INR|2|5606.3, 4406.85|repeated but not demonstrably recurrent|||
|user_105|groceries/Household groceries/debit/INR|2|5216.06, 4646.89|repeated but not demonstrably recurrent|||
|user_105|groceries/Local market purchase/debit/INR|2|4728.59, 5440.34|repeated but not demonstrably recurrent|||
|user_105|transport/Rail pass/debit/INR|4|2621.1, 1573.99, 2073.38, 2345.79|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_105|transport/Parking and tolls/debit/INR|4|1667.68, 2487.16, 1953.45, 2089.2|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_105|transport/Fuel refill/debit/INR|5|1952.07, 1919.52, 2100.2, 1859.61, 2204.87|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_105|transport/Ride-hailing trip/debit/INR|3|1553.92, 2615.76, 1851.53|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_105|transport/Metro and bus fares/debit/INR|7|2691.17, 2665.2, 1785.03, 2400.56, 2228.82, 2679.11, 1823.43|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_105|transport/Vehicle charging/debit/INR|4|2659.57, 1733.73, 1587.29, 1614.46|variable but recurrent|55|RECURRING_AMOUNT_UNRESOLVED|
|user_105|transport/Local taxi/debit/INR|8|2405.75, 2229.46, 1623.2, 1677.25, 2520.52, 2411.63, 1691.82, 1869.83|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_105|dining/Family dinner/debit/INR|4|4691.81, 5140.31, 4301.31, 4459.1|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_105|dining/Bakery and snacks/debit/INR|6|3115.34, 3084.7, 3260.17, 5190.5, 5096.14, 4942|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_105|dining/Quick-service meal/debit/INR|3|2967.2, 4481.39, 4610.86|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_105|dining/Neighbourhood restaurant/debit/INR|5|3699.04, 3093.6, 4697.37, 3341.8, 4928.59|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_105|dining/Lunch with colleagues/debit/INR|2|3689.43, 4844.56|repeated but not demonstrably recurrent|||
|user_105|dining/Coffee shop/debit/INR|2|4750.59, 3083.72|repeated but not demonstrably recurrent|||
|user_105|dining/Weekend food delivery/debit/INR|2|4133.38, 4552.02|repeated but not demonstrably recurrent|||
|user_106|salary/Previous employer payroll/credit/EUR|4|1815, 1815, 1815, 1815|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_106|rent/Landlord standing order/debit/EUR|5|524.7, 524.7, 524.7, 524.7, 524.7|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_106|utilities/Household utility payment/debit/EUR|5|99.3, 83.44, 100.56, 93.63, 99.16|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_106|debt_repayment/Credit card repayment/debit/EUR|5|215, 215, 215, 215, 215|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_106|music_subscription/Audio streaming plan/debit/EUR|5|23, 23, 23, 23, 23|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_106|groceries/Household groceries/debit/EUR|2|66.69, 99.72|repeated but not demonstrably recurrent|||
|user_106|groceries/Bulk pantry shop/debit/EUR|2|60.22, 102.91|repeated but not demonstrably recurrent|||
|user_106|groceries/Supermarket basket/debit/EUR|2|100.42, 70.51|repeated but not demonstrably recurrent|||
|user_106|groceries/Local market purchase/debit/EUR|2|64.63, 79.63|repeated but not demonstrably recurrent|||
|user_106|groceries/Neighbourhood grocer/debit/EUR|2|60.32, 86.98|repeated but not demonstrably recurrent|||
|user_106|groceries/Weekly produce market/debit/EUR|2|79.96, 81.7|repeated but not demonstrably recurrent|||
|user_106|transport/Commuter pass/debit/EUR|4|54.33, 36.33, 35.89, 38.2|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_106|transport/Vehicle charging/debit/EUR|2|47.38, 40.48|repeated but not demonstrably recurrent|||
|user_106|dining/Takeaway order/debit/EUR|2|58.05, 46.88|repeated but not demonstrably recurrent|||
|user_106|dining/Bakery and snacks/debit/EUR|3|48.64, 60.51, 62.64|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_107|rent/Landlord standing order/debit/EUR|6|693, 693, 693, 693, 693, 693|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_107|utilities/Energy provider bill/debit/EUR|5|128.9, 121.68, 135.96, 130.54, 119.9|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_107|education/School fee payment/debit/EUR|5|228, 228, 228, 228, 228|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_107|debt_repayment/Vehicle loan payment/debit/EUR|5|355, 355, 355, 355, 355|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_107|music_subscription/Audio streaming plan/debit/EUR|5|13, 13, 13, 13, 13|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_107|delivery_membership/Food delivery membership/debit/EUR|5|36, 36, 36, 36, 36|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_107|groceries/Fresh food shop/debit/EUR|3|85.8, 83.46, 92.7|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_107|groceries/Bulk pantry shop/debit/EUR|3|68.55, 74.97, 87.88|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_107|groceries/Weekly produce market/debit/EUR|4|69.58, 62.12, 60.04, 61.1|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_107|groceries/Local market purchase/debit/EUR|3|61.49, 78.3, 54.17|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_107|groceries/Neighbourhood grocer/debit/EUR|3|68.56, 81.09, 58.15|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_107|groceries/Household groceries/debit/EUR|2|58.84, 66.5|repeated but not demonstrably recurrent|||
|user_107|groceries/Supermarket basket/debit/EUR|3|59, 59.61, 81.55|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_107|groceries/Grocery delivery/debit/EUR|4|82.35, 93.42, 57.04, 58.57|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_107|transport/Parking and tolls/debit/EUR|2|37.27, 36.78|repeated but not demonstrably recurrent|||
|user_107|transport/Metro and bus fares/debit/EUR|4|37.74, 42.12, 33.16, 38.1|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_107|transport/Commuter pass/debit/EUR|7|44.22, 35.82, 43.98, 35.82, 49.44, 40.13, 44.24|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_107|transport/Vehicle charging/debit/EUR|3|41.44, 45.26, 44.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_107|transport/Ride-hailing trip/debit/EUR|2|37.73, 38.06|repeated but not demonstrably recurrent|||
|user_107|transport/Fuel refill/debit/EUR|3|54.16, 48.1, 44.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_107|transport/Local taxi/debit/EUR|3|56, 57.39, 57.71|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_107|dining/Lunch with colleagues/debit/EUR|2|72.71, 69.08|repeated but not demonstrably recurrent|||
|user_107|dining/Takeaway order/debit/EUR|3|90.13, 99.58, 90.95|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_107|dining/Family dinner/debit/EUR|3|97.45, 96.87, 64.83|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_107|dining/Coffee shop/debit/EUR|2|80.11, 104.78|repeated but not demonstrably recurrent|||
|user_108|salary/Base salary/credit/ZAR|5|20064, 20064, 20064, 20064, 20064|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_108|salary/Performance commission/credit/ZAR|4|13332.41, 4299.05, 11418.74, 10946.21|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_108|housing/Building maintenance payment/debit/ZAR|6|3366, 3366, 3366, 3366, 3366, 3366|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_108|utilities/Electricity bill/debit/ZAR|6|1734.35, 2002.9, 1887.15, 1605.32, 1865.86, 1677.64|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_108|insurance/Health insurance premium/debit/ZAR|6|1031.8, 1031.8, 1031.8, 1031.8, 1031.8, 1031.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_108|healthcare/Therapy appointment/debit/ZAR|5|2233.61, 2303.25, 2158.57, 2256.88, 2046.14|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_108|streaming/Streaming subscription/debit/ZAR|5|842.6, 842.6, 842.6, 842.6, 842.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_108|groceries/Supermarket basket/debit/ZAR|3|1255.84, 1639.45, 1137.33|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_108|groceries/Neighbourhood grocer/debit/ZAR|4|1252.52, 1530.21, 1881.78, 1198.66|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_108|groceries/Weekly produce market/debit/ZAR|3|1716.96, 1190.93, 1856.02|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_108|groceries/Household groceries/debit/ZAR|3|1253.58, 1696.16, 1183.52|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_108|groceries/Fresh food shop/debit/ZAR|2|1244.04, 1504.22|repeated but not demonstrably recurrent|||
|user_108|transport/Ride-hailing trip/debit/ZAR|2|573.63, 444.1|repeated but not demonstrably recurrent|||
|user_108|transport/Metro and bus fares/debit/ZAR|2|595.15, 757.9|repeated but not demonstrably recurrent|||
|user_108|transport/Vehicle charging/debit/ZAR|2|466.97, 646.86|repeated but not demonstrably recurrent|||
|user_108|transport/Local taxi/debit/ZAR|3|655.2, 670.61, 690.5|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_108|transport/Parking and tolls/debit/ZAR|2|671.96, 499.12|repeated but not demonstrably recurrent|||
|user_108|dining/Takeaway order/debit/ZAR|2|1064.14, 1033.78|repeated but not demonstrably recurrent|||
|user_108|dining/Quick-service meal/debit/ZAR|3|844.37, 1177.01, 1136.82|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_108|dining/Lunch with colleagues/debit/ZAR|3|1188.87, 1265.63, 747.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_108|dining/Bakery and snacks/debit/ZAR|2|1264.51, 827.77|repeated but not demonstrably recurrent|||
|user_109|salary/Payroll credit/credit/USD|5|2395.68, 2395.68, 2395.68, 2395.68, 2395.68|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_109|rent/Apartment rent transfer/debit/EUR|6|718.3, 718.3, 718.3, 718.3, 718.3, 718.3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_109|utilities/Electricity bill/debit/EUR|5|129.37, 120.4, 116.33, 132.99, 108.76|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_109|insurance/Household insurance/debit/EUR|5|86, 86, 86, 86, 86|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_109|cloud_storage/Shared storage plan/debit/EUR|5|20, 20, 20, 20, 20|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_109|streaming/Video streaming plan/debit/EUR|5|53, 53, 53, 53, 53|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_109|shopping/Online retail purchases/debit/EUR|5|102.85, 86.48, 93.58, 93, 95.33|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_109|entertainment/Cinema and events/debit/EUR|5|88.89, 104.44, 101.64, 96.76, 96.14|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_109|groceries/Fresh food shop/debit/EUR|4|78.41, 103.59, 92.56, 81.23|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_109|groceries/Supermarket basket/debit/EUR|3|86.95, 68.28, 98.56|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_109|groceries/Weekly produce market/debit/EUR|3|97.29, 69.32, 89.16|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_109|groceries/Grocery delivery/debit/EUR|2|107.88, 91.85|repeated but not demonstrably recurrent|||
|user_109|groceries/Bulk pantry shop/debit/EUR|2|75.59, 87.83|repeated but not demonstrably recurrent|||
|user_109|groceries/Local market purchase/debit/EUR|2|78.14, 87.45|repeated but not demonstrably recurrent|||
|user_109|transport/Ride-hailing trip/debit/EUR|3|61, 39.22, 40.48|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_109|transport/Fuel refill/debit/EUR|4|54.07, 60.41, 60.31, 53.7|variable but recurrent|55|RECURRING_AMOUNT_UNRESOLVED|
|user_109|transport/Parking and tolls/debit/EUR|6|43.81, 46.73, 61.83, 42.65, 38.86, 35.92|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_109|transport/Rail pass/debit/EUR|2|51.62, 41.42|repeated but not demonstrably recurrent|||
|user_109|transport/Vehicle charging/debit/EUR|4|55.91, 55.68, 53.22, 41.3|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_109|transport/Local taxi/debit/EUR|8|49.87, 52.02, 51.28, 45.72, 47.82, 50.87, 59.98, 42.09|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_109|transport/Commuter pass/debit/EUR|5|40.38, 52, 51.61, 51.82, 44.86|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_109|transport/Metro and bus fares/debit/EUR|4|61.23, 38.92, 37.79, 53.78|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_109|dining/Weekend food delivery/debit/EUR|4|59.28, 68.03, 90.11, 73.91|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_109|dining/Coffee shop/debit/EUR|3|57.7, 58.54, 69.28|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_109|dining/Bakery and snacks/debit/EUR|3|77.39, 71, 79.92|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_109|dining/Lunch with colleagues/debit/EUR|4|63.93, 93.3, 61.9, 80.77|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_109|dining/Family dinner/debit/EUR|6|74.49, 92.53, 88.16, 56.69, 64.23, 80.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_109|dining/Neighbourhood restaurant/debit/EUR|2|82.01, 61.66|repeated but not demonstrably recurrent|||
|user_109|dining/Quick-service meal/debit/EUR|2|86.51, 80.64|repeated but not demonstrably recurrent|||
|user_110|salary/Consulting invoice payment/credit/ZAR|2|6419.08, 7437.5|repeated but not demonstrably recurrent|||
|user_110|salary/Application project payment/credit/ZAR|2|9255.43, 8884.61|repeated but not demonstrably recurrent|||
|user_110|rent/Monthly rent/debit/ZAR|6|5148, 5148, 5148, 5148, 5148, 5148|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_110|utilities/Water and power payment/debit/ZAR|5|1103.24, 1104.67, 1113.35, 1149.83, 1244.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_110|cloud_storage/Online backup subscription/debit/ZAR|5|85.8, 85.8, 85.8, 85.8, 85.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_110|streaming/Streaming subscription/debit/ZAR|5|497.2, 497.2, 497.2, 497.2, 497.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_110|shopping/Monthly shopping spend/debit/ZAR|5|472.47, 432.33, 519.46, 453.84, 450.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_110|salary/Freelance milestone payment/credit/ZAR|2|9971.76, 7537.53|repeated but not demonstrably recurrent|||
|user_110|salary/Content contract payment/credit/ZAR|2|4400.62, 6933|repeated but not demonstrably recurrent|||
|user_110|groceries/Supermarket basket/debit/ZAR|3|699.79, 750.65, 881.87|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_110|groceries/Grocery delivery/debit/ZAR|4|755.1, 798.96, 696.49, 499.1|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_110|groceries/Weekly produce market/debit/ZAR|3|827.79, 688.93, 871.21|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_110|groceries/Household groceries/debit/ZAR|2|666.93, 595.7|repeated but not demonstrably recurrent|||
|user_110|groceries/Neighbourhood grocer/debit/ZAR|3|684.8, 738.29, 505.32|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_110|transport/Local taxi/debit/ZAR|3|278.74, 403.39, 326.69|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_110|transport/Fuel refill/debit/ZAR|3|382.46, 355.37, 321.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_110|transport/Parking and tolls/debit/ZAR|2|432.68, 407.8|repeated but not demonstrably recurrent|||
|user_110|dining/Family dinner/debit/ZAR|2|542.72, 461.36|repeated but not demonstrably recurrent|||
|user_110|dining/Neighbourhood restaurant/debit/ZAR|2|463.27, 397.25|repeated but not demonstrably recurrent|||
|user_110|dining/Lunch with colleagues/debit/ZAR|2|623.04, 548.15|repeated but not demonstrably recurrent|||
|user_111|salary/Payroll credit/credit/IDR|4|26220000, 26220000, 26220000, 26220000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_111|rent/Monthly rent/debit/IDR|5|6422000, 6422000, 6422000, 6422000, 6422000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_111|utilities/Electricity bill/debit/IDR|5|1519038.39, 1658575.19, 1639681.82, 1731685.53, 1776011.08|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_111|cloud_storage/Online backup subscription/debit/IDR|5|186200, 186200, 186200, 186200, 186200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_111|streaming/Video streaming plan/debit/IDR|5|668800, 668800, 668800, 668800, 668800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_111|shopping/Personal shopping/debit/IDR|5|529065.46, 586667.79, 594479.55, 569958, 512473.62|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_111|groceries/Fresh food shop/debit/IDR|4|1142969.39, 1310307.26, 1381388.4, 1220765.79|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_111|groceries/Supermarket basket/debit/IDR|2|921410.52, 1297358.28|repeated but not demonstrably recurrent|||
|user_111|groceries/Weekly produce market/debit/IDR|4|1411861.98, 1150848.4, 1136934.41, 903438.06|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_111|groceries/Household groceries/debit/IDR|2|1156904.56, 1145964.31|repeated but not demonstrably recurrent|||
|user_111|groceries/Bulk pantry shop/debit/IDR|2|975357.07, 906240.35|repeated but not demonstrably recurrent|||
|user_111|groceries/Local market purchase/debit/IDR|2|1411027.52, 1377237.14|repeated but not demonstrably recurrent|||
|user_111|transport/Fuel refill/debit/IDR|2|777144.95, 585236.21|repeated but not demonstrably recurrent|||
|user_111|transport/Parking and tolls/debit/IDR|2|794077.18, 818537.7|repeated but not demonstrably recurrent|||
|user_111|transport/Local taxi/debit/IDR|2|916133.13, 832323.62|repeated but not demonstrably recurrent|||
|user_111|transport/Rail pass/debit/IDR|2|877024.58, 525014.18|repeated but not demonstrably recurrent|||
|user_111|dining/Lunch with colleagues/debit/IDR|2|665965.39, 577550.34|repeated but not demonstrably recurrent|||
|user_111|dining/Bakery and snacks/debit/IDR|2|779469.79, 640595.82|repeated but not demonstrably recurrent|||
|user_112|rent/Landlord standing order/debit/EUR|6|174.9, 174.9, 174.9, 174.9, 174.9, 174.9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_112|utilities/Electricity bill/debit/EUR|5|44.34, 44.4, 43.62, 41.92, 40.44|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_112|education/Child education fee/debit/EUR|5|33, 33, 33, 33, 33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_112|debt_repayment/Education loan instalment/debit/EUR|5|81, 81, 81, 81, 81|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_112|music_subscription/Music service subscription/debit/EUR|5|6, 6, 6, 6, 6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_112|delivery_membership/Delivery service plan/debit/EUR|5|4, 4, 4, 4, 4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_112|salary/First-job payroll/credit/EUR|2|627, 627|repeated but not demonstrably recurrent|||
|user_112|groceries/Weekly produce market/debit/EUR|4|27.17, 24.9, 30.84, 26.63|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_112|groceries/Local market purchase/debit/EUR|6|28.27, 36.12, 33.82, 22.32, 23.31, 30.56|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|groceries/Bulk pantry shop/debit/EUR|5|27.84, 33.43, 29.39, 24.8, 30.25|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|groceries/Neighbourhood grocer/debit/EUR|2|35.4, 33.21|repeated but not demonstrably recurrent|||
|user_112|groceries/Supermarket basket/debit/EUR|4|29.9, 21.45, 26.85, 29.21|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_112|groceries/Fresh food shop/debit/EUR|4|21.62, 32.6, 32.45, 36.82|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|transport/Commuter pass/debit/EUR|6|16.59, 16.64, 17.95, 17.74, 16.41, 18.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|transport/Parking and tolls/debit/EUR|5|15.26, 12.35, 16.94, 17.81, 16.11|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|transport/Vehicle charging/debit/EUR|4|13.26, 16.69, 13.21, 16.38|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_112|transport/Ride-hailing trip/debit/EUR|3|17.02, 19.19, 16.35|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_112|transport/Local taxi/debit/EUR|4|11.65, 12.28, 11.98, 11.78|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_112|transport/Rail pass/debit/EUR|2|12.5, 18.54|repeated but not demonstrably recurrent|||
|user_112|dining/Neighbourhood restaurant/debit/EUR|3|30.64, 30.8, 21.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|dining/Weekend food delivery/debit/EUR|4|20.1, 19.69, 25.07, 32.6|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_112|dining/Coffee shop/debit/EUR|3|21.24, 26.73, 32.59|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_113|salary/International employer payroll/credit/USD|5|107995.68, 107995.68, 107995.68, 107995.68, 107995.68|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_113|rent/Landlord standing order/debit/INR|6|27300, 27300, 27300, 27300, 27300, 27300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_113|utilities/Electricity and water bill/debit/INR|5|5407.29, 4457.96, 4563.95, 5381.91, 5205.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_113|insurance/Health insurance premium/debit/INR|5|5270, 5270, 5270, 5270, 5270|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_113|cloud_storage/Shared storage plan/debit/INR|5|550, 550, 550, 550, 550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_113|streaming/Streaming subscription/debit/INR|5|3130, 3130, 3130, 3130, 3130|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_113|shopping/Online retail purchases/debit/INR|5|5297.73, 4960.44, 4820.14, 5357.79, 5360.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_113|entertainment/Weekend entertainment/debit/INR|5|2701.27, 2890.01, 3154.17, 2831.59, 2704.51|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_113|groceries/Local market purchase/debit/INR|3|3689.19, 4132.55, 5562.79|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_113|groceries/Neighbourhood grocer/debit/INR|4|4861.96, 3977.47, 6011.95, 4336.51|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_113|groceries/Supermarket basket/debit/INR|2|6016.92, 5280.29|repeated but not demonstrably recurrent|||
|user_113|groceries/Fresh food shop/debit/INR|3|3771.88, 5722.66, 5317.78|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_113|groceries/Household groceries/debit/INR|3|4349.35, 5098.03, 3986.45|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_113|groceries/Grocery delivery/debit/INR|2|4752.54, 4384.33|repeated but not demonstrably recurrent|||
|user_113|transport/Parking and tolls/debit/INR|5|2277.68, 2775.62, 2112.49, 1756.58, 1885.59|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Vehicle charging/debit/INR|5|1766.52, 2437.89, 2566.94, 1914.87, 2262.02|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Local taxi/debit/INR|3|2585.67, 2759.56, 2457.18|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Metro and bus fares/debit/INR|4|1910.23, 2388.25, 1830.87, 2316.92|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Rail pass/debit/INR|8|1878.72, 2334.5, 2019.8, 2318.11, 1902.85, 2601.49, 2362.44, 1984.49|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Ride-hailing trip/debit/INR|4|1856.54, 1881.31, 2615.41, 1909.97|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Commuter pass/debit/INR|3|2224.23, 2016.64, 2602.41|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_113|transport/Fuel refill/debit/INR|4|2018.76, 2605.26, 2279.15, 2249.26|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_113|dining/Neighbourhood restaurant/debit/INR|3|5081.45, 4592.76, 5379.73|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_113|dining/Lunch with colleagues/debit/INR|8|4810.76, 4978.13, 4020.08, 5702.67, 4252.56, 5131.84, 4092.77, 3966.21|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_113|dining/Takeaway order/debit/INR|2|3917.18, 4076.39|repeated but not demonstrably recurrent|||
|user_113|dining/Family dinner/debit/INR|3|5496.52, 3629.74, 3491.43|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_113|dining/Coffee shop/debit/INR|5|5310.41, 4762.63, 3572.4, 4722.72, 5511.38|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_113|dining/Weekend food delivery/debit/INR|2|3470.04, 3264.31|repeated but not demonstrably recurrent|||
|user_114|salary/Payroll credit/credit/INR|5|148200, 148200, 148200, 148200, 81510|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_114|rent/Landlord standing order/debit/INR|6|41700, 41700, 41700, 41700, 41700, 41700|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_114|utilities/Water and power payment/debit/INR|5|6859.86, 6570.23, 6525.67, 6203.99, 6360.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_114|insurance/Household insurance/debit/INR|5|6360, 6360, 6360, 6360, 6360|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_114|cloud_storage/Cloud storage plan/debit/INR|5|580, 580, 580, 580, 580|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_114|streaming/Streaming subscription/debit/INR|5|2900, 2900, 2900, 2900, 2900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_114|shopping/Monthly shopping spend/debit/INR|5|7560.9, 8023.59, 8182.74, 8202.8, 6639.49|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_114|entertainment/Games and recreation/debit/INR|5|3479.18, 3329.91, 3429.22, 3676.11, 4015.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_114|groceries/Local market purchase/debit/INR|3|5101.64, 5057.55, 6014.28|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_114|groceries/Bulk pantry shop/debit/INR|3|7844.85, 6905.82, 6695.05|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_114|groceries/Neighbourhood grocer/debit/INR|3|5675.72, 6552.72, 7219.42|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_114|groceries/Grocery delivery/debit/INR|5|8496.62, 4955.39, 6279.62, 5789.04, 6823.82|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_114|groceries/Household groceries/debit/INR|4|5709, 6185.85, 6163.36, 6008.45|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Ride-hailing trip/debit/INR|5|4394.45, 2946.51, 4468.66, 4631.79, 5130.66|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Metro and bus fares/debit/INR|4|3966.38, 3884.22, 3963.29, 4554.5|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Vehicle charging/debit/INR|7|2985.04, 4887.7, 4999.24, 4521.08, 4916.5, 3182.7, 3136.73|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Commuter pass/debit/INR|5|3936.45, 4650.18, 3748.9, 4318.33, 3393.11|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Parking and tolls/debit/INR|3|3292.1, 4448.31, 3511.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Fuel refill/debit/INR|5|3533.16, 4421.53, 3148.84, 3145.86, 3538.3|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Rail pass/debit/INR|3|4574.74, 3507.91, 4640.53|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_114|transport/Local taxi/debit/INR|3|4901.06, 4984.05, 3825.3|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_114|dining/Takeaway order/debit/INR|2|4176.73, 3653.01|repeated but not demonstrably recurrent|||
|user_114|dining/Bakery and snacks/debit/INR|4|3932.41, 4635.23, 5086.12, 3766.82|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_114|dining/Lunch with colleagues/debit/INR|5|4118.79, 4200.33, 3181.13, 3370.28, 4794.09|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_114|dining/Family dinner/debit/INR|5|3584.36, 4015.25, 4764.58, 4273.82, 3756|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_114|dining/Weekend food delivery/debit/INR|6|4809.84, 4760.94, 5023.76, 5083.05, 4330.35, 3600.16|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_115|salary/Payroll credit/credit/INR|5|59000, 59000, 59000, 59000, 59000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_115|rent/Landlord standing order/debit/INR|6|13300, 13300, 13300, 13300, 13300, 13300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_115|utilities/Water and power payment/debit/INR|5|3148.16, 3109.9, 3156.16, 3233.95, 3588.29|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_115|debt_repayment/Loan repayment/debit/INR|5|6600, 6600, 6600, 6600, 6600|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_115|music_subscription/Music subscription/debit/INR|5|575, 575, 575, 575, 575|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_115|groceries/Household groceries/debit/INR|5|1955.76, 2224.45, 2554.73, 2299.96, 1819.51|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_115|groceries/Local market purchase/debit/INR|2|1971.22, 1766.32|repeated but not demonstrably recurrent|||
|user_115|groceries/Weekly produce market/debit/INR|3|1930.11, 2456.66, 1945.27|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_115|transport/Local taxi/debit/INR|3|1051.23, 1591.35, 1394.81|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_115|dining/Coffee shop/debit/INR|4|1520.63, 1339.17, 1747.3, 1837.06|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_115|dining/Neighbourhood restaurant/debit/INR|2|1922.72, 1758.63|repeated but not demonstrably recurrent|||
|user_116|salary/Payroll credit/credit/INR|5|124000, 124000, 124000, 124000, 124000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_116|rent/Residential rent payment/debit/INR|6|41100, 41100, 41100, 41100, 41100, 41100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_116|utilities/Water and power payment/debit/INR|5|5528.12, 5626.02, 6571.21, 6031.33, 5489.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_116|education/Child education fee/debit/INR|5|12160, 12160, 12160, 12160, 12160|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_116|debt_repayment/Vehicle loan payment/debit/INR|5|10250, 10250, 10250, 10250, 10250|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_116|music_subscription/Music service subscription/debit/INR|5|1375, 1375, 1375, 1375, 1375|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_116|delivery_membership/Delivery service plan/debit/INR|5|1120, 1120, 1120, 1120, 1120|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_116|groceries/Fresh food shop/debit/INR|3|5268.67, 4737.3, 4454.73|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_116|groceries/Supermarket basket/debit/INR|5|4254.52, 4276.95, 6036.99, 5204.82, 3911.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_116|groceries/Weekly produce market/debit/INR|6|5403.15, 4377.45, 6064.81, 6267.84, 5800.94, 6089.38|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_116|groceries/Bulk pantry shop/debit/INR|6|4479.56, 4086.15, 4116.4, 4500.31, 5835.67, 5291.28|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_116|groceries/Household groceries/debit/INR|3|4764.16, 4867.46, 6288.77|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_116|transport/Ride-hailing trip/debit/INR|6|3294.26, 3765.71, 3420.59, 3490.06, 2447.21, 2728.84|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_116|transport/Commuter pass/debit/INR|4|2720.47, 3078.64, 2315.86, 3761.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_116|transport/Local taxi/debit/INR|2|3190.18, 2894.11|repeated but not demonstrably recurrent|||
|user_116|transport/Vehicle charging/debit/INR|6|2726.23, 3586.69, 2655.05, 3021.07, 2854.48, 3748.9|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_116|transport/Metro and bus fares/debit/INR|2|2696.08, 2960.67|repeated but not demonstrably recurrent|||
|user_116|transport/Parking and tolls/debit/INR|2|3272.44, 3535.75|repeated but not demonstrably recurrent|||
|user_116|transport/Rail pass/debit/INR|2|2455.89, 3273.48|repeated but not demonstrably recurrent|||
|user_116|transport/Fuel refill/debit/INR|2|3201.47, 2899.96|repeated but not demonstrably recurrent|||
|user_116|dining/Neighbourhood restaurant/debit/INR|4|5922.28, 3836.01, 5857.79, 5051.05|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_116|dining/Lunch with colleagues/debit/INR|5|4362.1, 4861.17, 3483.86, 5445.75, 4883.25|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_117|salary/Payroll credit/credit/EUR|5|926.64, 926.64, 926.64, 926.64, 926.64|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_117|housing/Home association fee/debit/EUR|6|102, 102, 102, 102, 102, 102|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_117|utilities/Electricity and water bill/debit/EUR|5|56.68, 56.62, 58.16, 54.36, 57.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_117|insurance/Household insurance/debit/EUR|5|31, 31, 31, 31, 31|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_117|healthcare/Regular medicine purchase/debit/EUR|5|73.55, 87.15, 85.87, 81.96, 89.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_117|streaming/Family streaming plan/debit/EUR|5|22, 22, 22, 22, 22|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_117|groceries/Fresh food shop/debit/EUR|7|37.94, 44.85, 42.16, 52.32, 34.35, 46.2, 38.3|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_117|groceries/Neighbourhood grocer/debit/EUR|3|48.33, 43.37, 51.03|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_117|groceries/Weekly produce market/debit/EUR|3|45.56, 48.38, 44.6|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_117|groceries/Supermarket basket/debit/EUR|2|41.17, 35.57|repeated but not demonstrably recurrent|||
|user_117|transport/Local taxi/debit/EUR|3|35.73, 32.02, 34.77|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_117|transport/Fuel refill/debit/EUR|3|25.21, 31.89, 25.85|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_117|transport/Vehicle charging/debit/EUR|2|33.36, 24.26|repeated but not demonstrably recurrent|||
|user_117|transport/Ride-hailing trip/debit/EUR|2|31.29, 30.91|repeated but not demonstrably recurrent|||
|user_117|dining/Bakery and snacks/debit/EUR|5|34.41, 33.38, 39.01, 32.73, 41.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_117|dining/Quick-service meal/debit/EUR|2|36.02, 34.99|repeated but not demonstrably recurrent|||
|user_117|dining/Neighbourhood restaurant/debit/EUR|2|42.85, 45.2|repeated but not demonstrably recurrent|||
|user_118|salary/Payroll credit/credit/EUR|5|759, 759, 759, 759, 759|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_118|rent/Monthly rent/debit/EUR|6|234.3, 234.3, 234.3, 234.3, 234.3, 234.3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_118|utilities/Electricity bill/debit/EUR|5|45.83, 44.92, 53.75, 48.2, 47.9|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_118|debt_repayment/Education loan instalment/debit/EUR|5|110, 110, 110, 110, 110|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_118|streaming/Streaming subscription/debit/EUR|5|22, 22, 22, 22, 22|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_118|cloud_storage/Shared storage plan/debit/EUR|5|3, 3, 3, 3, 3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_118|shopping/Monthly shopping spend/debit/EUR|5|35.81, 39.08, 38.28, 34.27, 37.49|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_118|groceries/Household groceries/debit/EUR|4|34.78, 36, 25.03, 30.35|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_118|groceries/Supermarket basket/debit/EUR|2|32.24, 22.12|repeated but not demonstrably recurrent|||
|user_118|groceries/Local market purchase/debit/EUR|5|25.74, 29.12, 23.81, 25.44, 36.91|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_118|groceries/Weekly produce market/debit/EUR|2|34.76, 29.27|repeated but not demonstrably recurrent|||
|user_118|groceries/Grocery delivery/debit/EUR|5|35.08, 25.04, 33.21, 29.01, 28.59|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_118|groceries/Neighbourhood grocer/debit/EUR|2|26.63, 35.88|repeated but not demonstrably recurrent|||
|user_118|groceries/Bulk pantry shop/debit/EUR|4|28.19, 35.62, 33.27, 34.41|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_118|groceries/Fresh food shop/debit/EUR|2|36.97, 30.11|repeated but not demonstrably recurrent|||
|user_118|transport/Metro and bus fares/debit/EUR|3|22.28, 23.46, 19.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_118|transport/Fuel refill/debit/EUR|4|16.95, 17.04, 13.71, 13.71|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_118|transport/Ride-hailing trip/debit/EUR|5|18.39, 20.57, 22.96, 22.91, 14.1|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_118|transport/Commuter pass/debit/EUR|4|15.91, 22.03, 15.9, 18.63|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_118|transport/Local taxi/debit/EUR|4|24.03, 14.44, 18.99, 21.55|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_118|transport/Rail pass/debit/EUR|2|22.37, 22.57|repeated but not demonstrably recurrent|||
|user_118|transport/Vehicle charging/debit/EUR|2|20.43, 13.81|repeated but not demonstrably recurrent|||
|user_118|dining/Takeaway order/debit/EUR|2|22.85, 23.65|repeated but not demonstrably recurrent|||
|user_118|dining/Weekend food delivery/debit/EUR|3|23.02, 23.08, 16.91|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_118|dining/Family dinner/debit/EUR|2|22.37, 15.32|repeated but not demonstrably recurrent|||
|user_118|dining/Quick-service meal/debit/EUR|2|17.86, 15.4|repeated but not demonstrably recurrent|||
|user_119|salary/Payroll before leave/credit/INR|2|176000, 176000|repeated but not demonstrably recurrent|||
|user_119|housing/Property maintenance contribution/debit/INR|5|17050, 17050, 17050, 17050, 17050|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_119|utilities/Electricity and water bill/debit/INR|5|11155.13, 12068.81, 11470.73, 12732.95, 12508.3|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_119|insurance/Vehicle insurance premium/debit/INR|5|7590, 7590, 7590, 7590, 7590|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_119|education/Course tuition/debit/INR|5|14850, 14850, 14850, 14850, 14850|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_119|healthcare/Therapy appointment/debit/INR|5|7681.41, 7589.02, 8043.37, 7576.48, 7475.93|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_119|entertainment/Weekend entertainment/debit/INR|5|4909.47, 5138.73, 5444.94, 4834.39, 4860.59|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_119|cloud_storage/Cloud storage plan/debit/INR|5|1280, 1280, 1280, 1280, 1280|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_119|groceries/Neighbourhood grocer/debit/INR|2|6479.54, 6804.71|repeated but not demonstrably recurrent|||
|user_119|groceries/Weekly produce market/debit/INR|2|6865.59, 7324.65|repeated but not demonstrably recurrent|||
|user_119|groceries/Local market purchase/debit/INR|4|5780, 7733.42, 8246.3, 8766.09|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_119|groceries/Grocery delivery/debit/INR|5|8844.5, 8151.28, 7879.55, 8456.96, 7007.34|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_119|groceries/Bulk pantry shop/debit/INR|2|6568.87, 8789.96|repeated but not demonstrably recurrent|||
|user_119|transport/Parking and tolls/debit/INR|2|3651.67, 4098.69|repeated but not demonstrably recurrent|||
|user_119|transport/Ride-hailing trip/debit/INR|2|4119.02, 3963.75|repeated but not demonstrably recurrent|||
|user_119|transport/Fuel refill/debit/INR|4|3213.77, 4040.91, 3091.57, 3587.85|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_119|transport/Metro and bus fares/debit/INR|2|3862.98, 2791.82|repeated but not demonstrably recurrent|||
|user_119|dining/Quick-service meal/debit/INR|2|4081.17, 4968.73|repeated but not demonstrably recurrent|||
|user_119|dining/Takeaway order/debit/INR|3|5249.46, 4170, 6067.04|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_119|dining/Coffee shop/debit/INR|2|4628.52, 4603.17|repeated but not demonstrably recurrent|||
|user_120|salary/Payroll credit/credit/IDR|5|23750000, 23750000, 23750000, 23750000, 23750000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_120|rent/Shared housing rent/debit/IDR|6|7961000, 7961000, 7961000, 7961000, 7961000, 7961000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_120|utilities/Municipal utilities/debit/IDR|6|1506728.29, 1311221.33, 1401847.66, 1378821.68, 1279384.2, 1252224.53|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_120|cloud_storage/Cloud storage plan/debit/IDR|5|197600, 197600, 197600, 197600, 197600|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_120|streaming/Video streaming plan/debit/IDR|5|630800, 630800, 630800, 630800, 630800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_120|shopping/Online retail purchases/debit/IDR|5|615027.14, 747715.81, 689405.84, 607692.8, 646179.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_120|groceries/Supermarket basket/debit/IDR|4|1069027.96, 1136750.01, 1328013.89, 1125921.62|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_120|groceries/Grocery delivery/debit/IDR|3|793336.16, 980817.7, 1038683.1|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_120|groceries/Bulk pantry shop/debit/IDR|4|953827.18, 1113436.89, 1264380.1, 1229885.33|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_120|groceries/Local market purchase/debit/IDR|4|1175015.35, 1094303.42, 988379.76, 1154695.22|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_120|groceries/Fresh food shop/debit/IDR|2|1181682.16, 973506.61|repeated but not demonstrably recurrent|||
|user_120|transport/Local taxi/debit/IDR|3|548510.86, 389737.59, 432618.16|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_120|transport/Vehicle charging/debit/IDR|2|549433.24, 436593.19|repeated but not demonstrably recurrent|||
|user_120|transport/Metro and bus fares/debit/IDR|2|617567.67, 391893.64|repeated but not demonstrably recurrent|||
|user_120|dining/Family dinner/debit/IDR|5|988286.58, 911711.76, 1098369.54, 1069879.31, 738628.69|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_120|dining/Neighbourhood restaurant/debit/IDR|2|752226.03, 801061.04|repeated but not demonstrably recurrent|||
|user_121|salary/Payroll credit/credit/USD|5|1056, 1056, 1056, 1056, 1056|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_121|rent/Landlord standing order/debit/USD|6|351.6, 351.6, 351.6, 351.6, 351.6, 351.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_121|utilities/Electricity and water bill/debit/USD|5|55.75, 59.63, 56.7, 62.38, 56.8|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_121|music_subscription/Music service subscription/debit/USD|5|13, 13, 13, 13, 13|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_121|delivery_membership/Food delivery membership/debit/USD|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_121|gym/Gym membership/debit/USD|5|19, 19, 19, 19, 19|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_121|entertainment/Games and recreation/debit/USD|5|14.61, 16.63, 16.69, 14.79, 14.48|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_121|groceries/Weekly produce market/debit/USD|3|40.86, 47.77, 57.03|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_121|groceries/Fresh food shop/debit/USD|9|42.56, 56.38, 52.79, 54.63, 42.69, 43.72, 39.64, 52.46, 46.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_121|groceries/Household groceries/debit/USD|5|35.71, 51.82, 40.94, 46.71, 39.52|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_121|groceries/Neighbourhood grocer/debit/USD|4|46.73, 52.89, 47.1, 43.5|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_121|groceries/Local market purchase/debit/USD|2|37.23, 53.31|repeated but not demonstrably recurrent|||
|user_121|groceries/Grocery delivery/debit/USD|2|49.06, 44.76|repeated but not demonstrably recurrent|||
|user_121|transport/Ride-hailing trip/debit/USD|6|22.26, 29.7, 22.31, 30.7, 18.97, 25.56|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_121|transport/Metro and bus fares/debit/USD|3|24.53, 18.21, 18.91|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_121|transport/Fuel refill/debit/USD|4|27.84, 31.8, 19.08, 19.41|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_121|transport/Rail pass/debit/USD|2|30.03, 25.57|repeated but not demonstrably recurrent|||
|user_121|transport/Commuter pass/debit/USD|2|20.61, 20.69|repeated but not demonstrably recurrent|||
|user_121|transport/Vehicle charging/debit/USD|5|24.52, 26.16, 28.46, 22.25, 22.62|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_121|transport/Parking and tolls/debit/USD|3|23.19, 29.17, 31.78|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_121|dining/Takeaway order/debit/USD|2|30.41, 46.88|repeated but not demonstrably recurrent|||
|user_121|dining/Coffee shop/debit/USD|4|36.08, 41.31, 47.99, 47.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_121|dining/Lunch with colleagues/debit/USD|2|30.26, 32.53|repeated but not demonstrably recurrent|||
|user_122|salary/Design contract payment/credit/IDR|2|5328451.23, 9955318.68|repeated but not demonstrably recurrent|||
|user_122|salary/Content contract payment/credit/IDR|3|8020400.94, 9859324.94, 9980227.62|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_122|rent/Monthly rent/debit/IDR|6|3724000, 3724000, 3724000, 3724000, 3724000, 3724000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_122|utilities/Energy provider bill/debit/IDR|5|712176.04, 739267.08, 852115.92, 706344.94, 810788.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_122|cloud_storage/Shared storage plan/debit/IDR|5|53200, 53200, 53200, 53200, 53200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_122|streaming/Video streaming plan/debit/IDR|5|298300, 298300, 298300, 298300, 298300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_122|shopping/Household shopping/debit/IDR|5|737932.35, 647226.12, 699655.05, 748017.53, 663092.97|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_122|salary/Consulting invoice payment/credit/IDR|3|8392562.51, 4926194.02, 7785299.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_122|groceries/Supermarket basket/debit/IDR|4|645746.63, 618768.69, 540722.72, 635960.26|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_122|groceries/Household groceries/debit/IDR|2|778429.27, 620216.67|repeated but not demonstrably recurrent|||
|user_122|groceries/Weekly produce market/debit/IDR|5|693585.58, 666764.59, 483859.75, 475259.3, 469910.61|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_122|groceries/Bulk pantry shop/debit/IDR|2|585007.1, 610407.9|repeated but not demonstrably recurrent|||
|user_122|groceries/Grocery delivery/debit/IDR|2|439681.4, 463687.54|repeated but not demonstrably recurrent|||
|user_122|groceries/Neighbourhood grocer/debit/IDR|2|688442, 568026.94|repeated but not demonstrably recurrent|||
|user_122|transport/Fuel refill/debit/IDR|3|536700.53, 406344.47, 488746.59|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_122|transport/Ride-hailing trip/debit/IDR|2|454293.41, 442455.18|repeated but not demonstrably recurrent|||
|user_122|transport/Rail pass/debit/IDR|2|521857.33, 337695.73|repeated but not demonstrably recurrent|||
|user_122|dining/Family dinner/debit/IDR|2|446176.16, 499841.37|repeated but not demonstrably recurrent|||
|user_122|dining/Takeaway order/debit/IDR|2|622850.6, 465075.26|repeated but not demonstrably recurrent|||
|user_122|dining/Neighbourhood restaurant/debit/IDR|2|415157.32, 633375.85|repeated but not demonstrably recurrent|||
|user_123|salary/Weekly app earnings/credit/IDR|3|5688210.4, 4952204.46, 4946045.19|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_123|salary/Driver platform payout/credit/IDR|8|6050519.01, 5904437.63, 5904424.46, 4760936.54, 4079736.03, 5412029.86, 3965264.64, 4021909.61|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_123|salary/Task marketplace payout/credit/IDR|4|3874315.24, 5299320.9, 5811835.13, 4562125.73|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_123|rent/Landlord standing order/debit/IDR|6|6004000, 6004000, 6004000, 6004000, 6004000, 6004000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_123|utilities/Energy provider bill/debit/IDR|5|1069541.14, 909444.74, 1004365.34, 1045539.46, 1081312.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_123|music_subscription/Music subscription/debit/IDR|5|171950, 171950, 171950, 171950, 171950|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_123|delivery_membership/Grocery delivery membership/debit/IDR|5|217550, 217550, 217550, 217550, 217550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_123|gym/Community fitness plan/debit/IDR|5|543400, 543400, 543400, 543400, 543400|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_123|entertainment/Monthly entertainment spend/debit/IDR|5|597196.02, 595621.28, 713881.96, 630308.24, 576578.09|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_123|salary/Delivery platform payout/credit/IDR|6|3716275.23, 6192797.43, 5353613, 5380135.72, 3991183.46, 6112349.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_123|groceries/Neighbourhood grocer/debit/IDR|5|656196.94, 601344.08, 902230.49, 892695.25, 676402.26|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_123|groceries/Supermarket basket/debit/IDR|4|748629.63, 651590.58, 746923.84, 679324|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_123|groceries/Grocery delivery/debit/IDR|6|817458.18, 844864.09, 958844.38, 553748.36, 924862.81, 858703.91|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_123|groceries/Bulk pantry shop/debit/IDR|4|914694.91, 912443.59, 874966.46, 803625.5|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_123|groceries/Local market purchase/debit/IDR|3|819470.24, 670851.27, 740285.68|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_123|transport/Vehicle charging/debit/IDR|2|443810.31, 528634.66|repeated but not demonstrably recurrent|||
|user_123|transport/Fuel refill/debit/IDR|3|545741.38, 518469.47, 437428.33|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_123|transport/Rail pass/debit/IDR|5|408761.51, 409349.73, 462714.15, 390246.16, 427372.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_123|transport/Ride-hailing trip/debit/IDR|3|584635.92, 411918.79, 338205.7|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_123|transport/Parking and tolls/debit/IDR|3|348840.67, 393228.73, 496739.26|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_123|transport/Local taxi/debit/IDR|3|463574.92, 587766.58, 451309.38|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_123|transport/Metro and bus fares/debit/IDR|5|526409.19, 353801.85, 506830.23, 498860.16, 566124.71|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_123|dining/Bakery and snacks/debit/IDR|4|755913.35, 468583.34, 614140.24, 477341.99|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_123|dining/Coffee shop/debit/IDR|3|641980.07, 692640.81, 604212.62|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_123|dining/Takeaway order/debit/IDR|2|471625.39, 610970.65|repeated but not demonstrably recurrent|||
|user_124|salary/Previous employer payroll/credit/EUR|4|2629, 2629, 2629, 2629|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_124|rent/Apartment rent transfer/debit/EUR|6|779.9, 779.9, 779.9, 779.9, 779.9, 779.9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_124|utilities/Electricity and water bill/debit/EUR|5|139.64, 171.64, 151.47, 167.73, 150.16|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_124|debt_repayment/Education loan instalment/debit/EUR|5|367, 367, 367, 367, 367|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_124|music_subscription/Music service subscription/debit/EUR|5|34, 34, 34, 34, 34|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_124|groceries/Neighbourhood grocer/debit/EUR|2|124.95, 128.08|repeated but not demonstrably recurrent|||
|user_124|groceries/Household groceries/debit/EUR|3|95.08, 95.33, 91.91|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_124|groceries/Weekly produce market/debit/EUR|3|82.08, 105.99, 94.62|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_124|groceries/Fresh food shop/debit/EUR|2|79.92, 105.72|repeated but not demonstrably recurrent|||
|user_124|transport/Local taxi/debit/EUR|3|74.49, 67.78, 75.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_124|dining/Lunch with colleagues/debit/EUR|2|56.4, 88.88|repeated but not demonstrably recurrent|||
|user_124|dining/Bakery and snacks/debit/EUR|2|67.49, 73.54|repeated but not demonstrably recurrent|||
|user_124|dining/Neighbourhood restaurant/debit/EUR|2|71.51, 84.16|repeated but not demonstrably recurrent|||
|user_124|dining/Family dinner/debit/EUR|2|97.03, 76.35|repeated but not demonstrably recurrent|||
|user_125|salary/International employer payroll/credit/EUR|5|14960, 14960, 14960, 14960, 14960|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_125|rent/Landlord standing order/debit/ZAR|6|3520, 3520, 3520, 3520, 3520, 3520|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_125|utilities/Electricity and water bill/debit/ZAR|5|1110.39, 1096.2, 1007.54, 923.31, 1053.79|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_125|insurance/Insurance policy payment/debit/ZAR|5|613.8, 613.8, 613.8, 613.8, 613.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_125|cloud_storage/Cloud storage plan/debit/ZAR|5|117.7, 117.7, 117.7, 117.7, 117.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_125|streaming/Video streaming plan/debit/ZAR|5|341, 341, 341, 341, 341|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_125|shopping/Online retail purchases/debit/ZAR|5|401.17, 443.32, 400.22, 497.8, 466.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_125|entertainment/Monthly entertainment spend/debit/ZAR|5|481.46, 498.3, 417.72, 475.58, 489.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_125|groceries/Neighbourhood grocer/debit/ZAR|2|422.66, 603.13|repeated but not demonstrably recurrent|||
|user_125|groceries/Household groceries/debit/ZAR|4|664.43, 504.4, 681.64, 405.06|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_125|groceries/Fresh food shop/debit/ZAR|4|653.54, 426.56, 682.68, 711.41|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_125|groceries/Local market purchase/debit/ZAR|4|433.55, 672.41, 488.73, 616.13|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_125|groceries/Grocery delivery/debit/ZAR|2|599.62, 605.27|repeated but not demonstrably recurrent|||
|user_125|transport/Fuel refill/debit/ZAR|4|325.41, 362.36, 401.32, 357.75|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Commuter pass/debit/ZAR|12|431.01, 399.8, 259.26, 388.61, 413.95, 394.1, 433.39, 313.01, 317.69, 447.68, 386.63, 401.93|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Metro and bus fares/debit/ZAR|3|286.89, 415.11, 447.63|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Parking and tolls/debit/ZAR|4|394.7, 306.44, 415.05, 349.21|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Local taxi/debit/ZAR|3|443.52, 434.41, 301.08|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Ride-hailing trip/debit/ZAR|4|345.81, 344.02, 440.5, 380.65|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Vehicle charging/debit/ZAR|4|375.13, 375.98, 309.13, 328.91|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_125|transport/Rail pass/debit/ZAR|2|413.12, 334|repeated but not demonstrably recurrent|||
|user_125|dining/Family dinner/debit/ZAR|5|445.29, 448.26, 382.81, 512.62, 568.52|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_125|dining/Quick-service meal/debit/ZAR|3|564.41, 498.41, 515.3|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_125|dining/Weekend food delivery/debit/ZAR|4|479.39, 413.81, 496.6, 487.63|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_125|dining/Takeaway order/debit/ZAR|2|353.43, 375.45|repeated but not demonstrably recurrent|||
|user_125|dining/Lunch with colleagues/debit/ZAR|3|349.21, 507.4, 477.4|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_125|dining/Neighbourhood restaurant/debit/ZAR|4|406.41, 548.02, 436.47, 376.39|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_125|dining/Coffee shop/debit/ZAR|3|553.43, 515.66, 412.67|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_126|salary/Website project payment/credit/INR|4|49536.45, 65350.69, 93175.93, 48833.69|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_126|salary/Application project payment/credit/INR|2|93209.6, 85084.4|repeated but not demonstrably recurrent|||
|user_126|rent/Residential rent payment/debit/INR|5|43000, 43000, 43000, 43000, 43000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_126|utilities/Energy provider bill/debit/INR|5|7975.53, 7973.39, 8692.79, 8361.91, 8926.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_126|cloud_storage/Online backup subscription/debit/INR|5|935, 935, 935, 935, 935|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_126|streaming/Family streaming plan/debit/INR|5|3310, 3310, 3310, 3310, 3310|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_126|shopping/Monthly shopping spend/debit/INR|5|4193.01, 4985.97, 4292.43, 4243.01, 4141.76|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_126|salary/Client retainer payment/credit/INR|2|93878.4, 69807.95|repeated but not demonstrably recurrent|||
|user_126|groceries/Household groceries/debit/INR|2|6189.46, 6863.71|repeated but not demonstrably recurrent|||
|user_126|groceries/Bulk pantry shop/debit/INR|2|5282.77, 6864.13|repeated but not demonstrably recurrent|||
|user_126|groceries/Grocery delivery/debit/INR|5|5644.91, 5657.12, 4938.76, 5666.15, 6063.85|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_126|groceries/Fresh food shop/debit/INR|3|6947.75, 4874.4, 5552.07|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_126|groceries/Supermarket basket/debit/INR|2|6201.07, 5804.11|repeated but not demonstrably recurrent|||
|user_126|groceries/Neighbourhood grocer/debit/INR|2|5403.49, 4561.7|repeated but not demonstrably recurrent|||
|user_126|transport/Commuter pass/debit/INR|4|2367.61, 2974.22, 2518.88, 2570.25|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_126|transport/Fuel refill/debit/INR|2|3368.18, 2887.41|repeated but not demonstrably recurrent|||
|user_126|dining/Takeaway order/debit/INR|2|4360.78, 3716.48|repeated but not demonstrably recurrent|||
|user_126|dining/Coffee shop/debit/INR|2|4211.45, 5255.02|repeated but not demonstrably recurrent|||
|user_126|dining/Family dinner/debit/INR|2|3924.28, 3322.26|repeated but not demonstrably recurrent|||
|user_127|salary/Payroll before leave/credit/ZAR|2|50160, 50160|repeated but not demonstrably recurrent|||
|user_127|rent/Apartment rent transfer/debit/ZAR|6|14652, 14652, 14652, 14652, 14652, 14652|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_127|utilities/Municipal utilities/debit/ZAR|5|3350.79, 3348.28, 3092.37, 3379.34, 3400.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_127|debt_repayment/Loan repayment/debit/ZAR|5|3003, 3003, 3003, 3003, 3003|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_127|streaming/Video streaming plan/debit/ZAR|5|1117.6, 1117.6, 1117.6, 1117.6, 1117.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_127|cloud_storage/Cloud storage plan/debit/ZAR|5|255.2, 255.2, 255.2, 255.2, 255.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_127|shopping/Clothing and household items/debit/ZAR|5|1688.3, 1846.73, 1728.32, 1675.18, 1913.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_127|groceries/Bulk pantry shop/debit/ZAR|2|1874.16, 1910.56|repeated but not demonstrably recurrent|||
|user_127|groceries/Fresh food shop/debit/ZAR|3|1721.17, 2155.74, 2246.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|groceries/Weekly produce market/debit/ZAR|4|1448.74, 1513.09, 1814.63, 1430.53|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_127|groceries/Household groceries/debit/ZAR|4|2188.13, 2087.76, 1964.19, 2282.19|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_127|groceries/Supermarket basket/debit/ZAR|5|1815.86, 2269.93, 2422.71, 1397.93, 1469.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|groceries/Grocery delivery/debit/ZAR|4|2111.71, 1405.86, 1588.27, 2051.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|groceries/Neighbourhood grocer/debit/ZAR|2|2015.66, 2022.44|repeated but not demonstrably recurrent|||
|user_127|transport/Ride-hailing trip/debit/ZAR|3|1154.06, 1372.53, 1585.48|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|transport/Fuel refill/debit/ZAR|2|1739.41, 1517.97|repeated but not demonstrably recurrent|||
|user_127|transport/Local taxi/debit/ZAR|3|1119.49, 1212.71, 1687.17|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_127|transport/Metro and bus fares/debit/ZAR|5|1130.46, 1202.4, 1253.41, 1688.8, 1339.27|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|transport/Rail pass/debit/ZAR|4|1580.24, 1552.07, 1578.16, 1425.71|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_127|transport/Parking and tolls/debit/ZAR|4|1356.49, 1356.32, 1506.57, 1746.47|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|transport/Commuter pass/debit/ZAR|3|1242.75, 1077.39, 1702.45|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_127|dining/Bakery and snacks/debit/ZAR|3|1885.16, 1659.89, 1731.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_127|dining/Lunch with colleagues/debit/ZAR|2|1129.27, 1722.49|repeated but not demonstrably recurrent|||
|user_127|dining/Coffee shop/debit/ZAR|2|1442.73, 1493.09|repeated but not demonstrably recurrent|||
|user_127|dining/Neighbourhood restaurant/debit/ZAR|3|1551.55, 1905.64, 1898.19|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_128|salary/Payroll credit/credit/ZAR|5|55220, 55220, 55220, 55220, 55220|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_128|housing/Home association fee/debit/ZAR|6|5368, 5368, 5368, 5368, 5368, 5368|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_128|utilities/Electricity and water bill/debit/ZAR|6|3242.32, 3741.77, 3778.07, 3172.93, 3097.05, 3087.56|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_128|insurance/Vehicle insurance premium/debit/ZAR|6|2149.4, 2149.4, 2149.4, 2149.4, 2149.4, 2149.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_128|education/Course tuition/debit/ZAR|5|2908.4, 2908.4, 2908.4, 2908.4, 2908.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_128|healthcare/Therapy appointment/debit/ZAR|5|3123.14, 2827.33, 3015.15, 2972.92, 3423.06|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_128|entertainment/Cinema and events/debit/ZAR|5|2225.88, 2289.12, 2282.9, 2015.19, 2091.93|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_128|cloud_storage/Cloud storage plan/debit/ZAR|5|445.5, 445.5, 445.5, 445.5, 445.5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_128|groceries/Supermarket basket/debit/ZAR|3|1538.64, 1824.92, 1576.88|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_128|groceries/Household groceries/debit/ZAR|5|1716.59, 2512.64, 1678.15, 1649.72, 2122.76|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_128|groceries/Weekly produce market/debit/ZAR|2|1557.83, 1691.42|repeated but not demonstrably recurrent|||
|user_128|groceries/Fresh food shop/debit/ZAR|2|1778.4, 1775.34|repeated but not demonstrably recurrent|||
|user_128|groceries/Neighbourhood grocer/debit/ZAR|2|2237.88, 1710.7|repeated but not demonstrably recurrent|||
|user_128|groceries/Local market purchase/debit/ZAR|2|2573.06, 2394.73|repeated but not demonstrably recurrent|||
|user_128|transport/Fuel refill/debit/ZAR|2|1209.64, 992.96|repeated but not demonstrably recurrent|||
|user_128|transport/Vehicle charging/debit/ZAR|2|798.02, 1012.63|repeated but not demonstrably recurrent|||
|user_128|transport/Parking and tolls/debit/ZAR|4|1171.04, 1237.04, 1032.42, 1076.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_128|transport/Rail pass/debit/ZAR|2|1006.73, 858.2|repeated but not demonstrably recurrent|||
|user_128|transport/Metro and bus fares/debit/ZAR|2|961.2, 1341.18|repeated but not demonstrably recurrent|||
|user_128|dining/Family dinner/debit/ZAR|3|1607.21, 2049.08, 2295.53|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_128|dining/Coffee shop/debit/ZAR|2|2091.3, 2152.13|repeated but not demonstrably recurrent|||
|user_129|salary/Payroll credit/credit/USD|5|1020, 1020, 1020, 1020, 1020|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_129|rent/Apartment rent transfer/debit/USD|6|300, 300, 300, 300, 300, 300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_129|utilities/Energy provider bill/debit/USD|5|57.43, 52.75, 52.01, 52.05, 60.76|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_129|cloud_storage/Cloud storage plan/debit/USD|5|3, 3, 3, 3, 3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_129|streaming/Family streaming plan/debit/USD|5|27, 27, 27, 27, 27|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_129|shopping/Personal shopping/debit/USD|5|45.43, 46.24, 50.68, 47.59, 42.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_129|groceries/Bulk pantry shop/debit/USD|2|53.02, 37.69|repeated but not demonstrably recurrent|||
|user_129|groceries/Grocery delivery/debit/USD|3|37.71, 46, 36.96|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_129|groceries/Local market purchase/debit/USD|2|46.66, 50.13|repeated but not demonstrably recurrent|||
|user_129|groceries/Supermarket basket/debit/USD|2|50.58, 51.5|repeated but not demonstrably recurrent|||
|user_129|groceries/Household groceries/debit/USD|3|53.92, 47.72, 33.26|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_129|groceries/Fresh food shop/debit/USD|3|43.33, 42.31, 53.06|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_129|groceries/Neighbourhood grocer/debit/USD|2|37.81, 44.07|repeated but not demonstrably recurrent|||
|user_129|transport/Metro and bus fares/debit/USD|2|25.53, 25.2|repeated but not demonstrably recurrent|||
|user_129|transport/Commuter pass/debit/USD|2|22.75, 18.33|repeated but not demonstrably recurrent|||
|user_129|transport/Rail pass/debit/USD|2|20.03, 23.04|repeated but not demonstrably recurrent|||
|user_129|transport/Ride-hailing trip/debit/USD|2|27.14, 19.38|repeated but not demonstrably recurrent|||
|user_129|dining/Takeaway order/debit/USD|3|40.27, 31.86, 26.83|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_129|dining/Neighbourhood restaurant/debit/USD|2|37.88, 30.87|repeated but not demonstrably recurrent|||
|user_130|salary/Payroll credit/credit/USD|5|3024, 3024, 3024, 2177.28, 2177.28|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_130|rent/Residential rent payment/debit/USD|6|600, 600, 600, 600, 600, 600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_130|utilities/Municipal utilities/debit/USD|5|118.32, 118.26, 136.92, 134.82, 131.15|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_130|music_subscription/Music service subscription/debit/USD|5|27, 27, 27, 27, 27|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_130|delivery_membership/Food delivery membership/debit/USD|5|33, 33, 33, 33, 33|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_130|gym/Community fitness plan/debit/USD|5|63, 63, 63, 63, 63|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_130|entertainment/Games and recreation/debit/USD|5|76.82, 69.91, 67.32, 63.38, 67.24|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_130|groceries/Weekly produce market/debit/USD|4|95.21, 93.47, 79.12, 107.46|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_130|groceries/Local market purchase/debit/USD|4|72.16, 97.69, 78.59, 101.24|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_130|groceries/Supermarket basket/debit/USD|2|84.12, 103.34|repeated but not demonstrably recurrent|||
|user_130|groceries/Bulk pantry shop/debit/USD|3|85.43, 98.52, 69.12|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_130|groceries/Household groceries/debit/USD|2|73.21, 73.95|repeated but not demonstrably recurrent|||
|user_130|groceries/Neighbourhood grocer/debit/USD|3|86.27, 72.63, 92.57|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_130|groceries/Grocery delivery/debit/USD|6|97, 71.02, 99.33, 74.26, 68.78, 84.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_130|groceries/Fresh food shop/debit/USD|2|93.3, 73.94|repeated but not demonstrably recurrent|||
|user_130|transport/Ride-hailing trip/debit/USD|6|57.16, 63.64, 47.9, 73.38, 53.94, 65.99|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_130|transport/Parking and tolls/debit/USD|6|72.62, 49.89, 75.86, 58.13, 76.28, 71.82|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_130|transport/Fuel refill/debit/USD|4|66.45, 63.83, 70.25, 70.1|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_130|transport/Metro and bus fares/debit/USD|4|51.77, 73.8, 72.03, 50.27|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_130|transport/Local taxi/debit/USD|3|47.82, 64.12, 55.39|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_130|transport/Rail pass/debit/USD|2|65.63, 74.66|repeated but not demonstrably recurrent|||
|user_130|dining/Weekend food delivery/debit/USD|2|90.69, 100.56|repeated but not demonstrably recurrent|||
|user_130|dining/Takeaway order/debit/USD|3|61.72, 93.7, 60.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_130|dining/Lunch with colleagues/debit/USD|5|99.04, 94.19, 82.45, 71.02, 59.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_131|salary/Payroll credit/credit/USD|5|1632, 1632, 1632, 1632, 1632|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_131|rent/Residential rent payment/debit/USD|5|373.2, 373.2, 373.2, 373.2, 373.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_131|utilities/Energy provider bill/debit/USD|5|88.11, 90.29, 95.45, 93.07, 90.86|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_131|debt_repayment/Loan repayment/debit/USD|5|213, 213, 213, 213, 213|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_131|healthcare/Regular medicine purchase/debit/USD|5|55.05, 48.18, 52.96, 47.54, 51.94|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_131|family_support/Dependent care payment/debit/USD|5|166, 166, 166, 166, 166|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_131|cloud_storage/Shared storage plan/debit/USD|5|10, 10, 10, 10, 10|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_131|shopping/Clothing and household items/debit/USD|5|56.03, 51.69, 54.82, 54.49, 49.87|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_131|groceries/Neighbourhood grocer/debit/USD|3|46.89, 52.48, 52.06|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_131|groceries/Weekly produce market/debit/USD|5|49.93, 47.71, 47.23, 59.98, 57.21|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_131|groceries/Fresh food shop/debit/USD|3|48.77, 51.19, 59.72|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_131|groceries/Household groceries/debit/USD|3|57.88, 58.06, 52.13|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_131|groceries/Local market purchase/debit/USD|2|74.19, 58.22|repeated but not demonstrably recurrent|||
|user_131|groceries/Bulk pantry shop/debit/USD|5|46.46, 57.76, 64.13, 47.31, 57.56|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_131|groceries/Supermarket basket/debit/USD|3|50.53, 44.73, 55.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_131|transport/Metro and bus fares/debit/USD|2|37.22, 36.63|repeated but not demonstrably recurrent|||
|user_131|transport/Vehicle charging/debit/USD|2|27.75, 42.19|repeated but not demonstrably recurrent|||
|user_131|transport/Commuter pass/debit/USD|2|24.84, 26.73|repeated but not demonstrably recurrent|||
|user_131|transport/Parking and tolls/debit/USD|2|28.3, 31.85|repeated but not demonstrably recurrent|||
|user_131|transport/Rail pass/debit/USD|2|41.02, 27.4|repeated but not demonstrably recurrent|||
|user_132|salary/Payroll credit/credit/USD|5|1193.4, 1193.4, 1193.4, 1193.4, 656.37|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_132|rent/Landlord standing order/debit/USD|6|321.6, 321.6, 321.6, 321.6, 321.6, 321.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_132|utilities/Municipal utilities/debit/USD|5|50.93, 51.6, 52.92, 49.77, 60.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_132|insurance/Health insurance premium/debit/USD|5|35, 35, 35, 35, 35|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_132|cloud_storage/Online backup subscription/debit/USD|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_132|streaming/Video streaming plan/debit/USD|5|29, 29, 29, 29, 29|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_132|shopping/Online retail purchases/debit/USD|5|62.71, 68.82, 63.74, 62.04, 60.71|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_132|entertainment/Cinema and events/debit/USD|5|40.15, 40.71, 40.92, 37.77, 38.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_132|groceries/Fresh food shop/debit/USD|5|53.83, 50.95, 45.37, 48.88, 45.29|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_132|groceries/Local market purchase/debit/USD|4|43.55, 43.02, 39.44, 45.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_132|groceries/Weekly produce market/debit/USD|2|46.86, 52.29|repeated but not demonstrably recurrent|||
|user_132|groceries/Supermarket basket/debit/USD|3|53.67, 57.82, 42.01|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Commuter pass/debit/USD|7|31.63, 21.3, 28.31, 20.08, 22.63, 19.95, 30.35|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Rail pass/debit/USD|9|20.88, 25.92, 27.83, 21.73, 25.75, 33.93, 23.74, 25.28, 31.06|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Vehicle charging/debit/USD|4|31.94, 33.65, 29.7, 20.98|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Fuel refill/debit/USD|3|23.25, 27.51, 25|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Parking and tolls/debit/USD|4|29.39, 25.66, 28.34, 32.77|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Metro and bus fares/debit/USD|4|19.72, 27.58, 33.29, 26.66|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_132|transport/Local taxi/debit/USD|4|24.92, 21.79, 21.82, 19.83|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_132|dining/Takeaway order/debit/USD|7|45.56, 50.73, 54.18, 57.02, 52.23, 63.13, 63.97|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_132|dining/Bakery and snacks/debit/USD|5|40.99, 55.18, 47.81, 47.49, 44.43|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_132|dining/Coffee shop/debit/USD|3|42.22, 52.49, 42.65|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_132|dining/Quick-service meal/debit/USD|3|48.69, 58.88, 53.37|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_132|dining/Lunch with colleagues/debit/USD|4|55.37, 41.08, 62.92, 53.13|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_132|dining/Weekend food delivery/debit/USD|3|52.18, 55.84, 52.98|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_133|salary/Temporary assignment pay/credit/IDR|2|12840653.44, 16383851.46|repeated but not demonstrably recurrent|||
|user_133|rent/Residential rent payment/debit/IDR|6|3895000, 3895000, 3895000, 3895000, 3895000, 3895000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_133|utilities/Electricity and water bill/debit/IDR|6|1059614.05, 992864.29, 889670.31, 936562.59, 899242.8, 971702.14|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_133|debt_repayment/Loan repayment/debit/IDR|5|2441500, 2441500, 2441500, 2441500, 2441500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_133|music_subscription/Audio streaming plan/debit/IDR|5|151050, 151050, 151050, 151050, 151050|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_133|groceries/Neighbourhood grocer/debit/IDR|2|702560.66, 535880.63|repeated but not demonstrably recurrent|||
|user_133|groceries/Local market purchase/debit/IDR|5|709264.44, 719938.6, 550419.41, 458482.05, 596399.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_133|transport/Commuter pass/debit/IDR|4|273471.27, 423055.34, 299807.81, 440504.11|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_133|transport/Ride-hailing trip/debit/IDR|2|382685.58, 383603.78|repeated but not demonstrably recurrent|||
|user_133|dining/Coffee shop/debit/IDR|2|415975.02, 453431.58|repeated but not demonstrably recurrent|||
|user_133|dining/Neighbourhood restaurant/debit/IDR|3|442013.16, 558144.98, 630821.68|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_133|dining/Takeaway order/debit/IDR|2|625377.47, 493551.58|repeated but not demonstrably recurrent|||
|user_133|dining/Quick-service meal/debit/IDR|2|423976.95, 491109.53|repeated but not demonstrably recurrent|||
|user_134|salary/Payroll credit/credit/IDR|5|24510000, 24510000, 24510000, 24510000, 24510000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_134|rent/Apartment rent transfer/debit/IDR|6|7600000, 7600000, 7600000, 7600000, 7600000, 7600000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_134|utilities/Energy provider bill/debit/IDR|5|1080821.88, 1109953.17, 1070182.14, 1307689.62, 1173756.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_134|education/Professional training fee/debit/IDR|5|1738500, 1738500, 1738500, 1738500, 1738500|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_134|debt_repayment/Loan repayment/debit/IDR|5|1377500, 1377500, 1377500, 1377500, 1377500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_134|music_subscription/Music subscription/debit/IDR|5|265050, 265050, 265050, 265050, 265050|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_134|delivery_membership/Food delivery membership/debit/IDR|5|219450, 219450, 219450, 219450, 219450|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_134|groceries/Household groceries/debit/IDR|5|871968.66, 920772.13, 683333.41, 685170.7, 1003280.13|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_134|groceries/Grocery delivery/debit/IDR|3|795730.21, 1078595.32, 812333.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_134|groceries/Bulk pantry shop/debit/IDR|3|718534.13, 1096455.74, 879281.38|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_134|groceries/Neighbourhood grocer/debit/IDR|3|1040692.5, 689837, 917962.36|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_134|groceries/Local market purchase/debit/IDR|3|675966.02, 854742.39, 941184.09|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_134|groceries/Supermarket basket/debit/IDR|5|777263.44, 996488.93, 761677.45, 669832.54, 803428.79|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_134|groceries/Fresh food shop/debit/IDR|3|1126321.27, 1021578.02, 1014569.63|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_134|transport/Rail pass/debit/IDR|4|590025.07, 381799.54, 559257.43, 589678.89|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_134|transport/Local taxi/debit/IDR|5|383452.71, 559246.96, 584487.96, 418843.11, 518958.74|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_134|transport/Vehicle charging/debit/IDR|3|596956.59, 499585.66, 426989.11|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_134|transport/Metro and bus fares/debit/IDR|4|467480.95, 417010.63, 434974.7, 451335.39|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_134|transport/Commuter pass/debit/IDR|3|435170.17, 531527.94, 431477.81|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_134|transport/Fuel refill/debit/IDR|4|564369.58, 460883.95, 516781.2, 544952.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_134|dining/Weekend food delivery/debit/IDR|3|888325.64, 1100549.03, 1241658.57|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_134|dining/Neighbourhood restaurant/debit/IDR|3|1278907.79, 978622.94, 1168829.28|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_134|dining/Coffee shop/debit/IDR|3|1093248.6, 762860.26, 925587.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_134|dining/Bakery and snacks/debit/IDR|3|1198020.49, 1019303.31, 851726.26|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_135|salary/Payroll credit/credit/USD|5|645.84, 645.84, 645.84, 645.84, 645.84|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_135|housing/Home association fee/debit/USD|6|94, 94, 94, 94, 94, 94|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_135|utilities/Electricity and water bill/debit/USD|5|64.25, 55.47, 62.34, 56.54, 54.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_135|insurance/Health insurance premium/debit/USD|5|33, 33, 33, 33, 33|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_135|healthcare/Diagnostic test/debit/USD|5|53.84, 61.79, 63.33, 50.55, 57.9|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_135|streaming/Video streaming plan/debit/USD|5|23, 23, 23, 23, 23|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_135|groceries/Bulk pantry shop/debit/USD|3|26.3, 31.74, 41.9|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_135|groceries/Neighbourhood grocer/debit/USD|3|41.63, 31.4, 34.76|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_135|groceries/Local market purchase/debit/USD|3|42.9, 43.44, 34.99|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_135|groceries/Household groceries/debit/USD|3|42.8, 44, 40.09|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_135|groceries/Supermarket basket/debit/USD|3|32.5, 26, 38.64|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_135|groceries/Grocery delivery/debit/USD|2|29.94, 43.21|repeated but not demonstrably recurrent|||
|user_135|transport/Vehicle charging/debit/USD|2|19.93, 17.99|repeated but not demonstrably recurrent|||
|user_135|transport/Local taxi/debit/USD|2|14.3, 18.97|repeated but not demonstrably recurrent|||
|user_135|transport/Rail pass/debit/USD|2|12.93, 12.03|repeated but not demonstrably recurrent|||
|user_135|transport/Parking and tolls/debit/USD|3|11.96, 18.75, 16.16|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_135|transport/Metro and bus fares/debit/USD|2|14.35, 17.67|repeated but not demonstrably recurrent|||
|user_135|dining/Weekend food delivery/debit/USD|2|39.11, 35.79|repeated but not demonstrably recurrent|||
|user_135|dining/Coffee shop/debit/USD|3|30.83, 32.92, 29.32|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_135|dining/Neighbourhood restaurant/debit/USD|3|28.72, 32.93, 28.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_136|salary/Payroll credit/credit/USD|5|1548, 1548, 1548, 1548, 1548|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_136|rent/Monthly rent/debit/USD|6|357.6, 357.6, 357.6, 357.6, 357.6, 357.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_136|utilities/Energy provider bill/debit/USD|5|84.56, 83.21, 80.31, 75.06, 77.16|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_136|debt_repayment/Credit card repayment/debit/USD|5|111, 111, 111, 111, 111|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_136|healthcare/Therapy appointment/debit/USD|5|82.69, 100.9, 97.33, 83.39, 101.54|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_136|family_support/Dependent care payment/debit/USD|5|142, 142, 142, 142, 142|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_136|cloud_storage/Online backup subscription/debit/USD|5|9, 9, 9, 9, 9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_136|shopping/Household shopping/debit/USD|5|62.96, 63.71, 72.54, 70.6, 68.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Weekly produce market/debit/USD|3|50.62, 73.65, 47.92|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Bulk pantry shop/debit/USD|3|73.75, 69.02, 80.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Neighbourhood grocer/debit/USD|4|73.61, 65.03, 76.98, 80.06|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Supermarket basket/debit/USD|5|48.76, 77.2, 51.55, 60.5, 57.89|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Fresh food shop/debit/USD|4|58.24, 78.78, 61.64, 47.33|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Local market purchase/debit/USD|3|56.3, 70.84, 55.85|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_136|groceries/Grocery delivery/debit/USD|2|56.14, 53.43|repeated but not demonstrably recurrent|||
|user_136|groceries/Household groceries/debit/USD|2|59.66, 59.96|repeated but not demonstrably recurrent|||
|user_136|transport/Parking and tolls/debit/USD|2|37.14, 28.56|repeated but not demonstrably recurrent|||
|user_136|transport/Rail pass/debit/USD|3|37.17, 28.99, 29.55|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_136|transport/Local taxi/debit/USD|3|36.8, 33.02, 34.03|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_136|transport/Ride-hailing trip/debit/USD|2|37.55, 41.48|repeated but not demonstrably recurrent|||
|user_136|transport/Commuter pass/debit/USD|2|36.06, 32.93|repeated but not demonstrably recurrent|||
|user_137|salary/Payroll credit/credit/INR|5|114000, 114000, 114000, 114000, 114000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_137|rent/Monthly rent/debit/INR|6|37300, 37300, 37300, 37300, 37300, 37300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_137|utilities/Electricity bill/debit/INR|5|7433.4, 7208.14, 7220.64, 8816.7, 8038.04|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_137|debt_repayment/Personal loan payment/debit/INR|5|14350, 14350, 14350, 14350, 14350|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_137|streaming/Streaming subscription/debit/INR|5|3200, 3200, 3200, 3200, 3200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_137|cloud_storage/Cloud storage plan/debit/INR|5|475, 475, 475, 475, 475|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_137|shopping/Monthly shopping spend/debit/INR|5|5121.36, 5536.37, 4722.53, 4784.94, 5539.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Weekly produce market/debit/INR|3|5693.02, 4621.89, 5010.42|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Fresh food shop/debit/INR|3|5540.73, 5365.86, 3933.71|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Household groceries/debit/INR|4|4156.3, 5708.25, 4033.25, 5232.02|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Grocery delivery/debit/INR|6|5408.78, 5156.75, 4910.62, 4715.12, 5400.18, 4257.42|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Local market purchase/debit/INR|3|4991.82, 6420.34, 6282.81|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Supermarket basket/debit/INR|5|5063.81, 4650.44, 5312.36, 4953.32, 5251.45|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_137|groceries/Neighbourhood grocer/debit/INR|2|4899.6, 4986.88|repeated but not demonstrably recurrent|||
|user_137|transport/Ride-hailing trip/debit/INR|7|3000.28, 2398.57, 2399.34, 2655.48, 2618.4, 2565.36, 3342.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_137|transport/Fuel refill/debit/INR|2|3473.79, 2076.71|repeated but not demonstrably recurrent|||
|user_137|transport/Metro and bus fares/debit/INR|2|2548.15, 2894.14|repeated but not demonstrably recurrent|||
|user_137|transport/Rail pass/debit/INR|5|2249.65, 3235.32, 2270.05, 2257.82, 2751.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_137|transport/Commuter pass/debit/INR|4|2122.82, 3451.91, 3164.57, 2190.91|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_137|transport/Local taxi/debit/INR|5|2330.14, 2876.88, 2803.65, 2544.02, 2342.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_137|dining/Quick-service meal/debit/INR|6|2872.3, 3124.98, 2722.14, 4080.44, 3477.27, 4335.19|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_137|dining/Neighbourhood restaurant/debit/INR|4|4053.46, 2813.71, 4068.26, 4600.83|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_138|salary/Payroll credit/credit/EUR|5|2695, 2695, 2695, 2695, 2695|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_138|rent/Landlord standing order/debit/EUR|6|711.7, 711.7, 711.7, 711.7, 711.7, 711.7|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_138|utilities/Electricity and water bill/debit/EUR|5|146.13, 151.65, 149.41, 137.3, 162.37|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_138|cloud_storage/Shared storage plan/debit/EUR|5|23, 23, 23, 23, 23|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_138|streaming/Streaming subscription/debit/EUR|5|69, 69, 69, 69, 69|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_138|shopping/Clothing and household items/debit/EUR|5|100.32, 100, 120.01, 114.8, 103.86|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_138|groceries/Grocery delivery/debit/EUR|3|136.8, 80.16, 122.93|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_138|groceries/Fresh food shop/debit/EUR|2|108.43, 126.75|repeated but not demonstrably recurrent|||
|user_138|groceries/Supermarket basket/debit/EUR|2|86.11, 80.76|repeated but not demonstrably recurrent|||
|user_138|groceries/Neighbourhood grocer/debit/EUR|3|114.84, 100.74, 93.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_138|groceries/Household groceries/debit/EUR|2|104.14, 108.44|repeated but not demonstrably recurrent|||
|user_138|groceries/Weekly produce market/debit/EUR|3|124.65, 95.28, 114.61|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_138|groceries/Local market purchase/debit/EUR|2|130.14, 95.97|repeated but not demonstrably recurrent|||
|user_138|transport/Rail pass/debit/EUR|2|47.83, 57.78|repeated but not demonstrably recurrent|||
|user_138|transport/Local taxi/debit/EUR|3|56.37, 47.32, 45.32|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_138|transport/Parking and tolls/debit/EUR|2|61.79, 58.82|repeated but not demonstrably recurrent|||
|user_138|dining/Family dinner/debit/EUR|3|87.79, 78.61, 76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_138|dining/Takeaway order/debit/EUR|2|126.94, 110.12|repeated but not demonstrably recurrent|||
|user_138|dining/Lunch with colleagues/debit/EUR|2|89.58, 112.94|repeated but not demonstrably recurrent|||
|user_139|salary/Payroll credit/credit/USD|5|1824, 1824, 1824, 1824, 1824|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_139|rent/Monthly rent/debit/USD|5|480, 480, 480, 480, 480|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_139|utilities/Electricity bill/debit/USD|5|87.1, 80.61, 89.41, 73.15, 90.17|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_139|music_subscription/Music subscription/debit/USD|5|24, 24, 24, 24, 24|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_139|delivery_membership/Food delivery membership/debit/USD|5|21, 21, 21, 21, 21|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_139|gym/Community fitness plan/debit/USD|5|36, 36, 36, 36, 36|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_139|entertainment/Monthly entertainment spend/debit/USD|5|34.26, 29.51, 31.01, 31.13, 28.54|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Neighbourhood grocer/debit/USD|4|70.76, 73.05, 85.94, 52.89|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Weekly produce market/debit/USD|3|59.6, 87.98, 72.76|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Household groceries/debit/USD|3|69.74, 69.93, 83.07|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Fresh food shop/debit/USD|2|87.05, 73.03|repeated but not demonstrably recurrent|||
|user_139|groceries/Grocery delivery/debit/USD|4|66.04, 87.71, 75.29, 72.72|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Local market purchase/debit/USD|3|88.22, 50.72, 66.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Bulk pantry shop/debit/USD|4|78.5, 53.37, 84.66, 61.19|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_139|groceries/Supermarket basket/debit/USD|2|66.76, 76.72|repeated but not demonstrably recurrent|||
|user_139|transport/Vehicle charging/debit/USD|2|39.31, 33.96|repeated but not demonstrably recurrent|||
|user_139|transport/Ride-hailing trip/debit/USD|3|57.31, 45.95, 56.5|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_139|transport/Metro and bus fares/debit/USD|4|41.38, 46.91, 51.77, 45|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_139|transport/Commuter pass/debit/USD|3|34.8, 51.6, 42.94|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_139|transport/Rail pass/debit/USD|5|54.53, 37.01, 56.51, 50.5, 34.15|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_139|transport/Parking and tolls/debit/USD|4|40.11, 34.06, 33.16, 51.82|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_139|transport/Fuel refill/debit/USD|3|48.63, 56.93, 53.75|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_139|dining/Bakery and snacks/debit/USD|2|79.43, 94.52|repeated but not demonstrably recurrent|||
|user_139|dining/Weekend food delivery/debit/USD|4|72.98, 80.22, 66.19, 71.02|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_139|dining/Lunch with colleagues/debit/USD|2|86.85, 76.09|repeated but not demonstrably recurrent|||
|user_139|dining/Neighbourhood restaurant/debit/USD|2|84.48, 60.83|repeated but not demonstrably recurrent|||
|user_140|rent/Apartment rent transfer/debit/ZAR|6|9966, 9966, 9966, 9966, 9966, 9966|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_140|utilities/Electricity and water bill/debit/ZAR|6|1711.96, 1767.52, 1950.14, 1891.14, 2022.66, 2049.42|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_140|education/School fee payment/debit/ZAR|5|2758.8, 2758.8, 2758.8, 2758.8, 2758.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_140|debt_repayment/Personal loan payment/debit/ZAR|5|2948, 2948, 2948, 2948, 2948|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_140|music_subscription/Music subscription/debit/ZAR|5|337.7, 337.7, 337.7, 337.7, 337.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_140|delivery_membership/Food delivery membership/debit/ZAR|5|438.9, 438.9, 438.9, 438.9, 438.9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_140|salary/First-job payroll/credit/ZAR|2|31900, 31900|repeated but not demonstrably recurrent|||
|user_140|groceries/Supermarket basket/debit/ZAR|6|1097.1, 1523.52, 974.79, 1508.6, 1089.81, 1288.95|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_140|groceries/Grocery delivery/debit/ZAR|5|1445.02, 1406, 906.48, 1011.22, 1069.12|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_140|groceries/Fresh food shop/debit/ZAR|2|1571.82, 1207.96|repeated but not demonstrably recurrent|||
|user_140|groceries/Bulk pantry shop/debit/ZAR|3|1461.39, 1405.91, 1281.14|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_140|groceries/Weekly produce market/debit/ZAR|2|947.83, 1256.88|repeated but not demonstrably recurrent|||
|user_140|groceries/Local market purchase/debit/ZAR|4|1158.31, 1254.22, 1540.94, 1418.84|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_140|groceries/Neighbourhood grocer/debit/ZAR|3|1526.63, 1488.92, 1479.38|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_140|transport/Metro and bus fares/debit/ZAR|3|651.53, 782.76, 847.95|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_140|transport/Commuter pass/debit/ZAR|3|524.77, 644.31, 673.87|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_140|transport/Ride-hailing trip/debit/ZAR|7|820.22, 864.16, 556.62, 797.1, 719.47, 685.48, 728.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_140|transport/Parking and tolls/debit/ZAR|4|632.55, 792.09, 628.79, 624.89|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_140|transport/Local taxi/debit/ZAR|2|504.67, 853.27|repeated but not demonstrably recurrent|||
|user_140|transport/Rail pass/debit/ZAR|3|678.04, 811.85, 559.18|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_140|transport/Fuel refill/debit/ZAR|2|773.61, 677.89|repeated but not demonstrably recurrent|||
|user_140|transport/Vehicle charging/debit/ZAR|2|795.4, 654.93|repeated but not demonstrably recurrent|||
|user_140|dining/Lunch with colleagues/debit/ZAR|3|1272, 1285.19, 1168.53|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_140|dining/Takeaway order/debit/ZAR|3|1062.23, 1056.57, 919.15|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_140|dining/Bakery and snacks/debit/ZAR|3|1015.79, 1274.37, 1274.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_140|dining/Weekend food delivery/debit/ZAR|2|1279.29, 1350.9|repeated but not demonstrably recurrent|||
|user_141|salary/Payroll credit/credit/INR|5|97000, 97000, 97000, 97000, 97000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_141|rent/Apartment rent transfer/debit/INR|6|26800, 26800, 26800, 26800, 26800, 26800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_141|utilities/Household utility payment/debit/INR|5|4953.75, 5928.28, 4964, 4767.37, 4806.14|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_141|insurance/Vehicle insurance premium/debit/INR|5|3480, 3480, 3480, 3480, 3480|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_141|cloud_storage/Cloud storage plan/debit/INR|5|805, 805, 805, 805, 805|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_141|streaming/Streaming subscription/debit/INR|5|2900, 2900, 2900, 2900, 2900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_141|shopping/Monthly shopping spend/debit/INR|5|3360.12, 3576.68, 3746.82, 4154.16, 3724.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_141|entertainment/Monthly entertainment spend/debit/INR|5|2142.56, 2261.3, 2054.22, 1937.22, 1845.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_141|groceries/Neighbourhood grocer/debit/INR|2|2530.5, 2821.97|repeated but not demonstrably recurrent|||
|user_141|groceries/Bulk pantry shop/debit/INR|4|3998.06, 2961.4, 4058.62, 2807.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_141|groceries/Grocery delivery/debit/INR|3|4123.41, 2980.87, 2738.24|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_141|groceries/Fresh food shop/debit/INR|4|3545.1, 3819.93, 3360.34, 3490.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_141|groceries/Supermarket basket/debit/INR|3|2892.58, 3481.49, 2801.49|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Vehicle charging/debit/INR|3|1684.59, 1896.54, 1938.85|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Metro and bus fares/debit/INR|5|1665.84, 2667.89, 2369.48, 2167.62, 2740.98|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Ride-hailing trip/debit/INR|6|2225.98, 2201.5, 2355.63, 2249.79, 2201.14, 1895.75|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Parking and tolls/debit/INR|8|1986.1, 2480.78, 2027.71, 1758.1, 2698.35, 2671.14, 2774.94, 1754.25|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Fuel refill/debit/INR|4|1906.28, 2686.55, 2196.94, 2135.82|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Local taxi/debit/INR|2|2814.8, 2784.3|repeated but not demonstrably recurrent|||
|user_141|transport/Commuter pass/debit/INR|4|1611.51, 2727.45, 1686.06, 2780.17|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_141|transport/Rail pass/debit/INR|4|2146.02, 2826.88, 2348.66, 1816.18|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_141|dining/Lunch with colleagues/debit/INR|4|3112.38, 3435.89, 4237.34, 4068.39|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_141|dining/Neighbourhood restaurant/debit/INR|9|3314.31, 3173.08, 3148.07, 4466.92, 3631.01, 3257.48, 4270.6, 2862.92, 3574.57|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_141|dining/Bakery and snacks/debit/INR|3|4146.63, 4143.52, 4080.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_141|dining/Coffee shop/debit/INR|3|4552.49, 3443.26, 4169.07|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_141|dining/Family dinner/debit/INR|2|3829.27, 2949.28|repeated but not demonstrably recurrent|||
|user_141|dining/Takeaway order/debit/INR|2|3613.34, 3417.71|repeated but not demonstrably recurrent|||
|user_141|dining/Quick-service meal/debit/INR|2|4668.1, 2856.33|repeated but not demonstrably recurrent|||
|user_142|salary/Freelance milestone payment/credit/USD|3|701.64, 619.62, 1324.43|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_142|rent/Residential rent payment/debit/USD|6|564, 564, 564, 564, 564, 564|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_142|utilities/Energy provider bill/debit/USD|5|99.18, 115, 98.98, 101.28, 96.9|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_142|cloud_storage/Shared storage plan/debit/USD|5|12, 12, 12, 12, 12|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_142|streaming/Video streaming plan/debit/USD|5|54, 54, 54, 54, 54|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_142|shopping/Online retail purchases/debit/USD|5|70.87, 60.82, 73.91, 70.28, 77.09|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_142|salary/Client retainer payment/credit/USD|2|903.05, 798.63|repeated but not demonstrably recurrent|||
|user_142|salary/Application project payment/credit/USD|2|829.71, 1082.84|repeated but not demonstrably recurrent|||
|user_142|groceries/Supermarket basket/debit/USD|5|104.35, 98.29, 93.11, 76.01, 97.86|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_142|groceries/Local market purchase/debit/USD|2|96.9, 97.01|repeated but not demonstrably recurrent|||
|user_142|groceries/Weekly produce market/debit/USD|2|59.92, 71.07|repeated but not demonstrably recurrent|||
|user_142|groceries/Grocery delivery/debit/USD|2|103.68, 88.27|repeated but not demonstrably recurrent|||
|user_142|groceries/Bulk pantry shop/debit/USD|4|65.48, 87.21, 84.08, 66.19|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_142|transport/Fuel refill/debit/USD|2|61.07, 55.12|repeated but not demonstrably recurrent|||
|user_142|transport/Commuter pass/debit/USD|2|59.39, 60.36|repeated but not demonstrably recurrent|||
|user_142|transport/Ride-hailing trip/debit/USD|2|51.75, 49.92|repeated but not demonstrably recurrent|||
|user_142|dining/Coffee shop/debit/USD|2|56.3, 61.93|repeated but not demonstrably recurrent|||
|user_142|dining/Bakery and snacks/debit/USD|3|56.57, 38.16, 40.48|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_142|dining/Neighbourhood restaurant/debit/USD|2|46.8, 36.86|repeated but not demonstrably recurrent|||
|user_143|salary/Payroll credit/credit/ZAR|5|14960, 14960, 14960, 14960, 14960|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_143|rent/Landlord standing order/debit/ZAR|6|3784, 3784, 3784, 3784, 3784, 3784|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_143|utilities/Water and power payment/debit/ZAR|5|767.22, 750.55, 737.76, 756.2, 705.6|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_143|education/School fee payment/debit/ZAR|5|1234.2, 1234.2, 1234.2, 1234.2, 1234.2|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_143|debt_repayment/Loan repayment/debit/ZAR|5|1771, 1771, 1771, 1771, 1771|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_143|music_subscription/Music subscription/debit/ZAR|5|156.2, 156.2, 156.2, 156.2, 156.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_143|delivery_membership/Food delivery membership/debit/ZAR|5|203.5, 203.5, 203.5, 203.5, 203.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_143|groceries/Bulk pantry shop/debit/ZAR|8|594.37, 461.59, 576.67, 430.73, 561.14, 402.35, 648.23, 558.61|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_143|groceries/Local market purchase/debit/ZAR|3|647.74, 438.37, 410.28|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_143|groceries/Weekly produce market/debit/ZAR|2|625.76, 441|repeated but not demonstrably recurrent|||
|user_143|groceries/Household groceries/debit/ZAR|3|498.1, 410.39, 449.11|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_143|groceries/Fresh food shop/debit/ZAR|3|678.16, 629.32, 641.94|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_143|groceries/Neighbourhood grocer/debit/ZAR|3|477.12, 458.68, 569.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_143|groceries/Grocery delivery/debit/ZAR|2|470.69, 682.52|repeated but not demonstrably recurrent|||
|user_143|transport/Rail pass/debit/ZAR|4|279.08, 312.28, 388.8, 324.82|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_143|transport/Parking and tolls/debit/ZAR|2|282.17, 419.58|repeated but not demonstrably recurrent|||
|user_143|transport/Local taxi/debit/ZAR|5|271.88, 265.23, 391.22, 379.76, 320.69|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_143|transport/Vehicle charging/debit/ZAR|5|338.43, 299.1, 265.58, 350.58, 270.2|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_143|transport/Ride-hailing trip/debit/ZAR|3|254.97, 435.27, 400.46|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_143|transport/Metro and bus fares/debit/ZAR|3|314.15, 290.78, 347.71|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_143|transport/Commuter pass/debit/ZAR|3|283.61, 308.99, 363.02|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_143|dining/Family dinner/debit/ZAR|4|673.52, 607.15, 570.66, 589.56|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_143|dining/Neighbourhood restaurant/debit/ZAR|2|662.38, 538.35|repeated but not demonstrably recurrent|||
|user_143|dining/Lunch with colleagues/debit/ZAR|2|575.65, 454.94|repeated but not demonstrably recurrent|||
|user_143|dining/Bakery and snacks/debit/ZAR|2|679.59, 552.8|repeated but not demonstrably recurrent|||
|user_144|rent/Shared housing rent/debit/USD|6|220.8, 220.8, 220.8, 220.8, 220.8, 220.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_144|utilities/Water and power payment/debit/USD|5|50.59, 44.94, 46.29, 47.65, 53.68|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_144|education/Professional training fee/debit/USD|5|66, 66, 66, 66, 66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_144|debt_repayment/Education loan instalment/debit/USD|5|119, 119, 119, 119, 119|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_144|music_subscription/Audio streaming plan/debit/USD|5|6, 6, 6, 6, 6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_144|delivery_membership/Delivery service plan/debit/USD|5|12, 12, 12, 12, 12|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_144|salary/First-job payroll/credit/USD|2|864, 864|repeated but not demonstrably recurrent|||
|user_144|groceries/Fresh food shop/debit/USD|3|33.09, 35.53, 41.41|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_144|groceries/Neighbourhood grocer/debit/USD|3|49.82, 33.57, 44.81|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|groceries/Bulk pantry shop/debit/USD|5|42.14, 47.81, 46.24, 42, 41.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|groceries/Weekly produce market/debit/USD|4|34.78, 36.3, 32.87, 30.93|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_144|groceries/Local market purchase/debit/USD|5|34.35, 36.31, 49.59, 48.54, 32.26|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|groceries/Household groceries/debit/USD|3|29.9, 49.11, 29.8|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_144|groceries/Grocery delivery/debit/USD|3|32.12, 29.5, 36.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|transport/Local taxi/debit/USD|4|18.68, 17.37, 21.2, 21.42|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_144|transport/Vehicle charging/debit/USD|3|22.61, 16.16, 21.69|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|transport/Ride-hailing trip/debit/USD|7|17.48, 21.42, 16.54, 22, 18.29, 14.65, 25.4|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_144|transport/Rail pass/debit/USD|3|18.63, 17.47, 16.09|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_144|transport/Metro and bus fares/debit/USD|4|16.02, 20.48, 20.5, 25.32|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_144|transport/Commuter pass/debit/USD|4|25.01, 24.93, 21.59, 25.12|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_144|dining/Takeaway order/debit/USD|4|42.81, 29.96, 38.33, 36.53|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_144|dining/Family dinner/debit/USD|4|30.18, 39.76, 32.22, 43.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|dining/Neighbourhood restaurant/debit/USD|3|31.97, 42.45, 26.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_144|dining/Lunch with colleagues/debit/USD|2|39.81, 40.88|repeated but not demonstrably recurrent|||
|user_145|salary/Payroll credit/credit/INR|5|258000, 258000, 258000, 258000, 258000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_145|rent/Landlord standing order/debit/INR|6|63900, 63900, 63900, 63900, 63900, 63900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_145|utilities/Water and power payment/debit/INR|5|17305.06, 16555.36, 16754.81, 15463.11, 18915.23|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_145|debt_repayment/Vehicle loan payment/debit/INR|5|18500, 18500, 18500, 18500, 18500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_145|streaming/Video streaming plan/debit/INR|5|5840, 5840, 5840, 5840, 5840|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_145|cloud_storage/Cloud storage plan/debit/INR|5|835, 835, 835, 835, 835|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_145|shopping/Clothing and household items/debit/INR|5|14466.22, 13503.66, 14217.91, 12311.13, 12129.25|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_145|groceries/Grocery delivery/debit/INR|4|7509.18, 7599.76, 12102.7, 10064.79|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_145|groceries/Neighbourhood grocer/debit/INR|5|7907.92, 11419.64, 8712.85, 11021.81, 8142.56|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_145|groceries/Bulk pantry shop/debit/INR|6|9252.01, 11178.66, 11995.46, 8441.62, 8716.09, 7889.92|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_145|groceries/Household groceries/debit/INR|3|10005.95, 8672.39, 10518.27|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_145|groceries/Supermarket basket/debit/INR|3|10791.78, 9395.13, 10010.85|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_145|groceries/Fresh food shop/debit/INR|2|11128.2, 9557.02|repeated but not demonstrably recurrent|||
|user_145|groceries/Weekly produce market/debit/INR|2|7734.19, 12206.6|repeated but not demonstrably recurrent|||
|user_145|transport/Vehicle charging/debit/INR|5|7929.82, 7821.47, 6188.62, 6433, 5408.43|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_145|transport/Commuter pass/debit/INR|3|5972.54, 5729.01, 7695.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_145|transport/Parking and tolls/debit/INR|3|7509.31, 4813.77, 7637.73|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_145|transport/Metro and bus fares/debit/INR|5|5959.97, 4857.6, 5309.1, 8046.46, 6334.71|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_145|transport/Local taxi/debit/INR|2|6945.79, 6866.98|repeated but not demonstrably recurrent|||
|user_145|transport/Fuel refill/debit/INR|5|6191.94, 4691, 7836.02, 6132.53, 5448.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_145|transport/Rail pass/debit/INR|3|7023.5, 4720.4, 4673.62|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_145|dining/Family dinner/debit/INR|2|6218.85, 7214.4|repeated but not demonstrably recurrent|||
|user_145|dining/Takeaway order/debit/INR|2|5955.29, 8441.78|repeated but not demonstrably recurrent|||
|user_145|dining/Bakery and snacks/debit/INR|3|6053.01, 5022.4, 7401.77|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_145|dining/Neighbourhood restaurant/debit/INR|3|8080.8, 5680.84, 4928.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_146|salary/Payroll credit/credit/INR|5|168000, 168000, 168000, 168000, 168000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_146|housing/Home repair reserve/debit/INR|5|14450, 14450, 14450, 14450, 14450|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_146|utilities/Electricity bill/debit/INR|5|10295.07, 11874.23, 11664.01, 10083.67, 10560.82|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_146|insurance/Insurance policy payment/debit/INR|5|6110, 6110, 6110, 6110, 6110|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_146|education/Course tuition/debit/INR|5|11420, 11420, 11420, 11420, 11420|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_146|healthcare/Therapy appointment/debit/INR|5|10604.04, 9696.6, 11135.61, 9366.53, 10551.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_146|entertainment/Monthly entertainment spend/debit/INR|5|2815.02, 3021.17, 3089.31, 2677.55, 2774.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_146|cloud_storage/Cloud storage plan/debit/INR|5|525, 525, 525, 525, 525|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_146|groceries/Neighbourhood grocer/debit/INR|3|6805.12, 5214.57, 6415.63|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_146|groceries/Supermarket basket/debit/INR|4|7425.69, 6132.27, 7740.4, 6439.97|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_146|groceries/Local market purchase/debit/INR|2|5269.34, 9025.44|repeated but not demonstrably recurrent|||
|user_146|groceries/Bulk pantry shop/debit/INR|3|9062.58, 8692.14, 7312.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_146|groceries/Household groceries/debit/INR|2|7144.25, 5205.14|repeated but not demonstrably recurrent|||
|user_146|groceries/Weekly produce market/debit/INR|2|6999.98, 8454.15|repeated but not demonstrably recurrent|||
|user_146|transport/Commuter pass/debit/INR|2|4650.05, 5503.05|repeated but not demonstrably recurrent|||
|user_146|transport/Local taxi/debit/INR|2|3585.52, 4207.14|repeated but not demonstrably recurrent|||
|user_146|transport/Metro and bus fares/debit/INR|2|4189.07, 5338.21|repeated but not demonstrably recurrent|||
|user_146|transport/Fuel refill/debit/INR|2|3568.68, 5542.95|repeated but not demonstrably recurrent|||
|user_146|transport/Vehicle charging/debit/INR|2|4990.24, 5132.54|repeated but not demonstrably recurrent|||
|user_146|dining/Weekend food delivery/debit/INR|2|8189.44, 8266.04|repeated but not demonstrably recurrent|||
|user_146|dining/Family dinner/debit/INR|2|7166.24, 5540.24|repeated but not demonstrably recurrent|||
|user_146|dining/Bakery and snacks/debit/INR|2|6279.53, 7996.91|repeated but not demonstrably recurrent|||
|user_147|salary/Payroll before leave/credit/EUR|2|1529, 1529|repeated but not demonstrably recurrent|||
|user_147|rent/Apartment rent transfer/debit/EUR|6|464.2, 464.2, 464.2, 464.2, 464.2, 464.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_147|utilities/Electricity bill/debit/EUR|5|93.69, 77.74, 77.54, 90.14, 80.15|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_147|cloud_storage/Online backup subscription/debit/EUR|5|9, 9, 9, 9, 9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_147|streaming/Video streaming plan/debit/EUR|5|30, 30, 30, 30, 30|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_147|shopping/Clothing and household items/debit/EUR|5|65.42, 65.93, 75.96, 74.35, 73.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_147|groceries/Household groceries/debit/EUR|2|80.8, 66.81|repeated but not demonstrably recurrent|||
|user_147|groceries/Supermarket basket/debit/EUR|4|54.75, 80.1, 62.45, 86.42|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_147|groceries/Neighbourhood grocer/debit/EUR|2|76.95, 50.88|repeated but not demonstrably recurrent|||
|user_147|groceries/Bulk pantry shop/debit/EUR|4|66.77, 57.78, 82.48, 61.02|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_147|groceries/Fresh food shop/debit/EUR|3|73.91, 49.99, 80.07|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_147|groceries/Local market purchase/debit/EUR|2|85.37, 86.67|repeated but not demonstrably recurrent|||
|user_147|transport/Rail pass/debit/EUR|2|24.65, 34.48|repeated but not demonstrably recurrent|||
|user_147|transport/Fuel refill/debit/EUR|3|27.16, 23.09, 24.52|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_147|dining/Family dinner/debit/EUR|2|56.64, 62.27|repeated but not demonstrably recurrent|||
|user_147|dining/Neighbourhood restaurant/debit/EUR|3|57.7, 44.14, 73.31|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_147|dining/Weekend food delivery/debit/EUR|2|47.37, 56.83|repeated but not demonstrably recurrent|||
|user_148|salary/Payroll credit/credit/ZAR|5|35640, 35640, 35640, 35640, 35640|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_148|rent/Shared housing rent/debit/ZAR|6|11066, 11066, 11066, 11066, 11066, 11066|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_148|utilities/Electricity and water bill/debit/ZAR|6|2104.58, 2027.11, 2092.75, 1907.09, 1805.31, 2175.96|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_148|music_subscription/Audio streaming plan/debit/ZAR|5|328.9, 328.9, 328.9, 328.9, 328.9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_148|delivery_membership/Food delivery membership/debit/ZAR|5|575.3, 575.3, 575.3, 575.3, 575.3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_148|gym/Community fitness plan/debit/ZAR|5|651.2, 651.2, 651.2, 651.2, 651.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_148|entertainment/Games and recreation/debit/ZAR|5|1150.4, 1169.5, 1200.56, 1239.47, 1165.83|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_148|groceries/Local market purchase/debit/ZAR|3|1189.28, 1557.7, 1023.66|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_148|groceries/Neighbourhood grocer/debit/ZAR|2|1680.55, 1604.18|repeated but not demonstrably recurrent|||
|user_148|groceries/Supermarket basket/debit/ZAR|6|1253.56, 1412.06, 1313.84, 1625.21, 1501.7, 1347.14|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_148|groceries/Weekly produce market/debit/ZAR|4|1667.9, 1522.33, 1011.05, 1607.62|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_148|groceries/Grocery delivery/debit/ZAR|3|1635.88, 1425.66, 1090.04|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_148|groceries/Bulk pantry shop/debit/ZAR|4|1058.72, 1400.27, 1642.81, 1190.45|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_148|groceries/Household groceries/debit/ZAR|3|992.48, 1633.97, 1578.61|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_148|transport/Parking and tolls/debit/ZAR|4|1036.16, 906.06, 990.3, 919.55|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_148|transport/Commuter pass/debit/ZAR|2|1001.67, 673.57|repeated but not demonstrably recurrent|||
|user_148|transport/Metro and bus fares/debit/ZAR|3|773.83, 681.59, 834.49|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_148|transport/Vehicle charging/debit/ZAR|2|886.17, 842.44|repeated but not demonstrably recurrent|||
|user_148|transport/Ride-hailing trip/debit/ZAR|3|657.85, 854.1, 934.75|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_148|transport/Rail pass/debit/ZAR|4|731.52, 833.73, 1127.02, 805.32|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_148|transport/Local taxi/debit/ZAR|5|700.86, 904.15, 1000.83, 1123.26, 1148.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_148|transport/Fuel refill/debit/ZAR|3|909.61, 797.54, 808.1|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_148|dining/Weekend food delivery/debit/ZAR|3|1300.81, 1001.99, 1148.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_148|dining/Coffee shop/debit/ZAR|3|1260.82, 765.37, 1000.71|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_148|dining/Neighbourhood restaurant/debit/ZAR|3|1027.08, 788.69, 1193.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_148|dining/Family dinner/debit/ZAR|2|1187.15, 965.39|repeated but not demonstrably recurrent|||
|user_149|salary/Payroll credit/credit/ZAR|5|52360, 52360, 52360, 52360, 52360|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_149|rent/Monthly rent/debit/ZAR|6|16654, 16654, 16654, 16654, 16654, 16654|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_149|utilities/Energy provider bill/debit/ZAR|5|2936.36, 3140.97, 2692.64, 2720.7, 3185.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_149|debt_repayment/Education loan instalment/debit/ZAR|5|5324, 5324, 5324, 5324, 5324|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_149|healthcare/Clinic payment/debit/ZAR|5|1862.45, 1821.29, 2131.77, 1948.21, 1867.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_149|family_support/Childcare contribution/debit/ZAR|5|3671.8, 3671.8, 3671.8, 3671.8, 3671.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_149|cloud_storage/Cloud storage plan/debit/ZAR|5|366.3, 366.3, 366.3, 366.3, 366.3|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_149|shopping/Monthly shopping spend/debit/ZAR|5|2617.68, 2742.61, 2267.3, 2401.88, 2506.71|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_149|groceries/Supermarket basket/debit/ZAR|6|1393.19, 1633.49, 1706.81, 2052.23, 1691.74, 1978.04|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_149|groceries/Bulk pantry shop/debit/ZAR|4|2337.05, 1639.64, 2094.39, 1921.58|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_149|groceries/Local market purchase/debit/ZAR|2|1703.82, 1787.6|repeated but not demonstrably recurrent|||
|user_149|groceries/Grocery delivery/debit/ZAR|4|1647.87, 1703.68, 2100.93, 1700.87|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_149|groceries/Household groceries/debit/ZAR|3|1449.79, 1501.58, 1872.96|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_149|groceries/Fresh food shop/debit/ZAR|2|2306.75, 2042.92|repeated but not demonstrably recurrent|||
|user_149|groceries/Weekly produce market/debit/ZAR|2|2042.75, 2248.85|repeated but not demonstrably recurrent|||
|user_149|groceries/Neighbourhood grocer/debit/ZAR|3|1438.56, 1933.75, 1463.73|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_149|transport/Metro and bus fares/debit/ZAR|2|1358.31, 1258.65|repeated but not demonstrably recurrent|||
|user_149|transport/Local taxi/debit/ZAR|2|1070.78, 1300.94|repeated but not demonstrably recurrent|||
|user_149|transport/Fuel refill/debit/ZAR|3|1336.42, 1633.09, 1160.18|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_149|transport/Vehicle charging/debit/ZAR|3|1197.23, 1784.68, 1048.03|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_150|salary/Payroll credit/credit/EUR|5|893.75, 893.75, 893.75, 893.75, 491.56|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_150|rent/Residential rent payment/debit/EUR|6|268.4, 268.4, 268.4, 268.4, 268.4, 268.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_150|utilities/Household utility payment/debit/EUR|5|62.18, 53.02, 62.91, 57.92, 55.28|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_150|insurance/Health insurance premium/debit/EUR|5|25, 25, 25, 25, 25|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_150|cloud_storage/Online backup subscription/debit/EUR|5|6, 6, 6, 6, 6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_150|streaming/Family streaming plan/debit/EUR|5|25, 25, 25, 25, 25|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_150|shopping/Online retail purchases/debit/EUR|5|35.89, 36.73, 40.79, 35.93, 39.62|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_150|entertainment/Local event tickets/debit/EUR|5|27.91, 24.09, 26.52, 29.29, 25.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_150|groceries/Local market purchase/debit/EUR|2|40.91, 33.25|repeated but not demonstrably recurrent|||
|user_150|groceries/Bulk pantry shop/debit/EUR|5|43.78, 39.64, 35.82, 35.57, 40.4|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_150|groceries/Supermarket basket/debit/EUR|6|45.78, 31.55, 29.65, 45.18, 43.49, 49.42|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_150|groceries/Fresh food shop/debit/EUR|2|33.31, 42.65|repeated but not demonstrably recurrent|||
|user_150|transport/Commuter pass/debit/EUR|7|23.14, 18.91, 14.94, 14, 23.03, 23.57, 15.07|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Metro and bus fares/debit/EUR|5|16.58, 16.43, 24.17, 18.46, 22.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Vehicle charging/debit/EUR|3|19.25, 14.16, 15.69|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Fuel refill/debit/EUR|3|13.83, 22.69, 23.77|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Ride-hailing trip/debit/EUR|7|16.53, 21.07, 22.5, 18.32, 22.88, 20.96, 18.02|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Rail pass/debit/EUR|3|19.73, 15.15, 20.08|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Local taxi/debit/EUR|4|19.74, 15.44, 24.29, 16.19|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_150|transport/Parking and tolls/debit/EUR|3|15.96, 19.14, 14.83|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_150|dining/Bakery and snacks/debit/EUR|5|42.87, 33.57, 38, 41.36, 42.88|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_150|dining/Neighbourhood restaurant/debit/EUR|4|36.6, 43.98, 32.44, 40.82|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_150|dining/Family dinner/debit/EUR|6|27.71, 36.39, 45.77, 35.38, 37.56, 36.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_150|dining/Lunch with colleagues/debit/EUR|2|35.06, 28.28|repeated but not demonstrably recurrent|||
|user_150|dining/Coffee shop/debit/EUR|2|30.01, 33.22|repeated but not demonstrably recurrent|||
|user_150|dining/Quick-service meal/debit/EUR|2|43.93, 43.12|repeated but not demonstrably recurrent|||
|user_150|dining/Weekend food delivery/debit/EUR|3|27.45, 34, 35.03|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_151|salary/Previous employer payroll/credit/IDR|4|46170000, 46170000, 46170000, 46170000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_151|rent/Landlord standing order/debit/IDR|5|12236000, 12236000, 12236000, 12236000, 12236000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_151|utilities/Energy provider bill/debit/IDR|5|2651930.79, 3013296.95, 2750647.49, 2829095.55, 2713434.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_151|debt_repayment/Vehicle loan payment/debit/IDR|5|6203500, 6203500, 6203500, 6203500, 6203500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_151|music_subscription/Audio streaming plan/debit/IDR|5|382850, 382850, 382850, 382850, 382850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_151|groceries/Local market purchase/debit/IDR|3|2340934.72, 1411848.73, 1996302.75|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_151|groceries/Supermarket basket/debit/IDR|2|2045496.64, 1665441.51|repeated but not demonstrably recurrent|||
|user_151|groceries/Weekly produce market/debit/IDR|3|1869480.54, 1623671.08, 1707429.32|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_151|transport/Metro and bus fares/debit/IDR|3|1101605.93, 1111684.57, 1170262.26|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_151|transport/Fuel refill/debit/IDR|3|770110.99, 667062.91, 702720.06|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_151|dining/Takeaway order/debit/IDR|4|1190411.04, 965578.13, 964972.48, 1448991.76|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_152|salary/Payroll credit/credit/ZAR|5|13640, 13640, 13640, 13640, 13640|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_152|rent/Apartment rent transfer/debit/ZAR|6|3894, 3894, 3894, 3894, 3894, 3894|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_152|utilities/Household utility payment/debit/ZAR|5|757.76, 768.53, 876.5, 761.11, 821.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_152|education/Professional training fee/debit/ZAR|5|1124.2, 1124.2, 1124.2, 1124.2, 1124.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_152|debt_repayment/Vehicle loan payment/debit/ZAR|5|1881, 1881, 1881, 1881, 1881|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_152|music_subscription/Music subscription/debit/ZAR|5|122.1, 122.1, 122.1, 122.1, 122.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_152|delivery_membership/Food delivery membership/debit/ZAR|5|156.2, 156.2, 156.2, 156.2, 156.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_152|groceries/Supermarket basket/debit/ZAR|7|414.79, 619.79, 455.2, 421.22, 621.83, 496.66, 590.62|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|groceries/Local market purchase/debit/ZAR|4|523.62, 430.4, 417.79, 515.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|groceries/Bulk pantry shop/debit/ZAR|3|577.7, 466.05, 521.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|groceries/Household groceries/debit/ZAR|3|359.77, 468.36, 445.53|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|groceries/Fresh food shop/debit/ZAR|4|472.12, 424.25, 475.09, 353.31|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|groceries/Grocery delivery/debit/ZAR|4|624.51, 502.72, 613.79, 571.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|transport/Parking and tolls/debit/ZAR|5|315.12, 278.44, 258.7, 380.64, 366.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|transport/Metro and bus fares/debit/ZAR|3|356.94, 385.42, 390.61|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_152|transport/Commuter pass/debit/ZAR|3|394.43, 373.25, 381.2|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_152|transport/Ride-hailing trip/debit/ZAR|5|364.18, 256.4, 350.65, 303.35, 276.68|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_152|transport/Fuel refill/debit/ZAR|4|280.36, 353.02, 265.37, 428.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_152|transport/Vehicle charging/debit/ZAR|2|308.03, 409.92|repeated but not demonstrably recurrent|||
|user_152|transport/Rail pass/debit/ZAR|4|382.12, 389.08, 406.89, 414.9|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_152|dining/Family dinner/debit/ZAR|2|430.86, 481.32|repeated but not demonstrably recurrent|||
|user_152|dining/Bakery and snacks/debit/ZAR|3|525.04, 350.2, 486.2|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_152|dining/Takeaway order/debit/ZAR|2|572.65, 556.2|repeated but not demonstrably recurrent|||
|user_152|dining/Lunch with colleagues/debit/ZAR|2|463.27, 411.34|repeated but not demonstrably recurrent|||
|user_152|dining/Weekend food delivery/debit/ZAR|2|575.93, 383.24|repeated but not demonstrably recurrent|||
|user_153|salary/Payroll credit/credit/EUR|5|1630.64, 1630.64, 1630.64, 1630.64, 1630.64|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_153|rent/Residential rent payment/debit/USD|6|528, 528, 528, 528, 528, 528|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_153|utilities/Electricity bill/debit/USD|6|93.27, 90.99, 80.64, 85.8, 89.97, 87.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_153|insurance/Health insurance premium/debit/USD|5|49, 49, 49, 49, 49|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_153|cloud_storage/Cloud storage plan/debit/USD|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_153|streaming/Video streaming plan/debit/USD|5|34, 34, 34, 34, 34|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_153|shopping/Monthly shopping spend/debit/USD|5|81.18, 82.12, 87.66, 84.39, 72.25|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_153|entertainment/Games and recreation/debit/USD|5|60.34, 49.43, 48.93, 51.84, 56.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_153|groceries/Bulk pantry shop/debit/USD|3|68.41, 89.67, 91.86|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_153|groceries/Neighbourhood grocer/debit/USD|6|54.18, 73.3, 88.36, 57.41, 84.45, 81.77|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_153|groceries/Fresh food shop/debit/USD|5|56.98, 82.43, 60.76, 72.84, 87.69|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_153|groceries/Local market purchase/debit/USD|2|62.85, 91.29|repeated but not demonstrably recurrent|||
|user_153|transport/Commuter pass/debit/USD|3|42.22, 38.27, 44.13|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_153|transport/Vehicle charging/debit/USD|4|52.34, 50.88, 52.89, 32.35|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_153|transport/Ride-hailing trip/debit/USD|8|38.25, 31.62, 35.73, 47.14, 52.61, 35.85, 39.35, 42.24|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_153|transport/Metro and bus fares/debit/USD|5|50.64, 37.77, 48.62, 43.99, 37.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_153|transport/Rail pass/debit/USD|3|33.84, 32.69, 34.5|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_153|transport/Local taxi/debit/USD|5|47.21, 39.06, 36.43, 34.2, 37.35|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_153|transport/Parking and tolls/debit/USD|8|51.82, 34.95, 44.9, 48.46, 36.3, 36.36, 32.53, 49.77|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_153|dining/Takeaway order/debit/USD|4|56.83, 74.74, 65.25, 53.81|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_153|dining/Coffee shop/debit/USD|2|75.14, 79.83|repeated but not demonstrably recurrent|||
|user_153|dining/Family dinner/debit/USD|4|56.51, 82.17, 73.93, 80.7|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_153|dining/Neighbourhood restaurant/debit/USD|6|82.84, 81.82, 82.56, 51.33, 77.33, 60.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_153|dining/Bakery and snacks/debit/USD|4|55.31, 68.81, 74.21, 71.52|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_153|dining/Weekend food delivery/debit/USD|3|67.78, 69.35, 83.03|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_154|salary/Primary household salary/credit/EUR|5|1009.36, 1009.36, 1009.36, 1009.36, 1009.36|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_154|salary/Second household income/credit/EUR|4|655.97, 571.18, 601.56, 597.91|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_154|rent/Shared housing rent/debit/EUR|6|507.1, 507.1, 507.1, 507.1, 507.1, 507.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_154|utilities/Electricity bill/debit/EUR|5|100.46, 111.9, 102.22, 108.14, 112.63|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_154|debt_repayment/Credit card repayment/debit/EUR|5|212, 212, 212, 212, 212|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_154|streaming/Streaming subscription/debit/EUR|5|30, 30, 30, 30, 30|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_154|cloud_storage/Cloud storage plan/debit/EUR|5|8, 8, 8, 8, 8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_154|shopping/Personal shopping/debit/EUR|5|74.51, 72.3, 64.36, 63.57, 64.32|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_154|groceries/Supermarket basket/debit/EUR|3|58.33, 63.83, 90.82|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_154|groceries/Local market purchase/debit/EUR|3|84, 80.76, 92.88|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_154|groceries/Fresh food shop/debit/EUR|3|84.17, 67.5, 69.17|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_154|groceries/Household groceries/debit/EUR|4|76.5, 91.28, 63.01, 72.59|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_154|groceries/Weekly produce market/debit/EUR|2|93.22, 57.46|repeated but not demonstrably recurrent|||
|user_154|groceries/Bulk pantry shop/debit/EUR|5|84.72, 92.66, 83.4, 77.03, 69.53|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_154|groceries/Neighbourhood grocer/debit/EUR|5|79.31, 59.67, 61.06, 86.18, 93.4|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_154|transport/Vehicle charging/debit/EUR|4|42.24, 40.4, 27.27, 39.08|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_154|transport/Metro and bus fares/debit/EUR|4|31.32, 31.64, 39.11, 44.22|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_154|transport/Fuel refill/debit/EUR|2|25.93, 44.51|repeated but not demonstrably recurrent|||
|user_154|transport/Rail pass/debit/EUR|2|43.55, 25.64|repeated but not demonstrably recurrent|||
|user_154|transport/Parking and tolls/debit/EUR|7|43.21, 30.54, 41.55, 43.33, 38.97, 39.87, 32.21|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_154|transport/Local taxi/debit/EUR|3|32.57, 42.93, 30.24|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_154|transport/Ride-hailing trip/debit/EUR|3|38.01, 42.37, 44.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_154|dining/Quick-service meal/debit/EUR|3|52.1, 47.41, 65.64|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_154|dining/Takeaway order/debit/EUR|2|59.45, 64.36|repeated but not demonstrably recurrent|||
|user_154|dining/Weekend food delivery/debit/EUR|3|51.14, 65.24, 72.61|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_154|dining/Lunch with colleagues/debit/EUR|2|43.79, 58.59|repeated but not demonstrably recurrent|||
|user_154|dining/Neighbourhood restaurant/debit/EUR|2|63.17, 46.51|repeated but not demonstrably recurrent|||
|user_155|salary/Payroll before leave/credit/INR|2|84000, 84000|repeated but not demonstrably recurrent|||
|user_155|housing/Building maintenance payment/debit/INR|6|7800, 7800, 7800, 7800, 7800, 7800|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_155|utilities/Household utility payment/debit/INR|5|5359.65, 5480.76, 4699.41, 5241.63, 4697.91|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_155|insurance/Insurance policy payment/debit/INR|5|3130, 3130, 3130, 3130, 3130|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_155|education/Course tuition/debit/INR|5|8190, 8190, 8190, 8190, 8190|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_155|healthcare/Family healthcare expense/debit/INR|5|7047.74, 6377.57, 6280.42, 7398.25, 7316.32|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_155|entertainment/Monthly entertainment spend/debit/INR|5|2058.88, 1684.63, 1898.98, 1930.21, 1984.64|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_155|cloud_storage/Online backup subscription/debit/INR|5|295, 295, 295, 295, 295|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_155|groceries/Supermarket basket/debit/INR|5|3793.53, 3798.03, 3603.98, 3152, 2748.56|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_155|groceries/Weekly produce market/debit/INR|2|4106.51, 2989.27|repeated but not demonstrably recurrent|||
|user_155|groceries/Neighbourhood grocer/debit/INR|3|3853.94, 3307.39, 2502.33|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_155|groceries/Household groceries/debit/INR|3|3960.46, 3891.9, 2824.37|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_155|groceries/Bulk pantry shop/debit/INR|2|4256.06, 3905.93|repeated but not demonstrably recurrent|||
|user_155|groceries/Local market purchase/debit/INR|2|3997.54, 3660.59|repeated but not demonstrably recurrent|||
|user_155|transport/Commuter pass/debit/INR|2|1624.21, 1737.25|repeated but not demonstrably recurrent|||
|user_155|transport/Fuel refill/debit/INR|3|1467.57, 1917.93, 1828.33|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_155|transport/Rail pass/debit/INR|3|2110.24, 2091.21, 1535.51|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_155|transport/Metro and bus fares/debit/INR|2|2240.9, 1472.28|repeated but not demonstrably recurrent|||
|user_155|dining/Lunch with colleagues/debit/INR|3|3523.76, 3788.98, 3273.17|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_155|dining/Bakery and snacks/debit/INR|2|3130.23, 3535.41|repeated but not demonstrably recurrent|||
|user_156|salary/Payroll credit/credit/ZAR|5|32340, 32340, 32340, 32340, 32340|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_156|rent/Apartment rent transfer/debit/ZAR|6|7568, 7568, 7568, 7568, 7568, 7568|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_156|utilities/Household utility payment/debit/ZAR|5|1769.72, 1904.78, 1723.15, 1782.29, 1716.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_156|cloud_storage/Shared storage plan/debit/ZAR|5|225.5, 225.5, 225.5, 225.5, 225.5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_156|streaming/Streaming subscription/debit/ZAR|5|805.2, 805.2, 805.2, 805.2, 805.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_156|shopping/Online retail purchases/debit/ZAR|5|1087.55, 1058.91, 912.11, 957.02, 952.32|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_156|groceries/Fresh food shop/debit/ZAR|3|1422.6, 1241.42, 1242.49|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_156|groceries/Neighbourhood grocer/debit/ZAR|2|1008.28, 1227.16|repeated but not demonstrably recurrent|||
|user_156|groceries/Local market purchase/debit/ZAR|3|1303.55, 1438.79, 1237.45|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_156|groceries/Bulk pantry shop/debit/ZAR|2|1307.6, 1416.07|repeated but not demonstrably recurrent|||
|user_156|groceries/Weekly produce market/debit/ZAR|2|1516.55, 1449.28|repeated but not demonstrably recurrent|||
|user_156|groceries/Household groceries/debit/ZAR|3|1490.89, 1365.22, 978.95|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_156|groceries/Supermarket basket/debit/ZAR|2|1023.14, 1506.34|repeated but not demonstrably recurrent|||
|user_156|transport/Rail pass/debit/ZAR|2|1030.16, 676.32|repeated but not demonstrably recurrent|||
|user_156|transport/Commuter pass/debit/ZAR|3|1069.34, 1108.42, 985.51|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_156|dining/Takeaway order/debit/ZAR|2|1124.27, 1513.76|repeated but not demonstrably recurrent|||
|user_156|dining/Bakery and snacks/debit/ZAR|4|1273.83, 1067.62, 1532.97, 1030.87|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_157|salary/Payroll credit/credit/IDR|5|33250000, 33250000, 33250000, 23940000, 23940000|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_157|rent/Monthly rent/debit/IDR|6|6612000, 6612000, 6612000, 6612000, 6612000, 6612000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_157|utilities/Electricity bill/debit/IDR|5|1436807.15, 1441264.5, 1382702.09, 1277123.16, 1477172.83|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_157|music_subscription/Audio streaming plan/debit/IDR|5|226100, 226100, 226100, 226100, 226100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_157|delivery_membership/Food delivery membership/debit/IDR|5|240350, 240350, 240350, 240350, 240350|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_157|gym/Fitness club membership/debit/IDR|5|737200, 737200, 737200, 737200, 737200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_157|entertainment/Weekend entertainment/debit/IDR|5|400023.75, 377533.51, 383271.92, 392460.02, 442121.35|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_157|groceries/Local market purchase/debit/IDR|4|1300870.28, 784856.58, 1016213.87, 1188678.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_157|groceries/Supermarket basket/debit/IDR|2|1146211.38, 1112622.58|repeated but not demonstrably recurrent|||
|user_157|groceries/Weekly produce market/debit/IDR|5|796344.67, 1156107.59, 1265771.55, 963543.54, 1307246.22|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_157|groceries/Bulk pantry shop/debit/IDR|4|1199784.27, 1159696.94, 966988.38, 872038.09|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_157|groceries/Grocery delivery/debit/IDR|4|774881.66, 1093219.67, 1210619.42, 1093935.31|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_157|groceries/Fresh food shop/debit/IDR|3|892588.47, 1237308.4, 1193438.95|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_157|groceries/Household groceries/debit/IDR|4|927076.07, 858124.98, 1290234.67, 928967.22|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_157|transport/Vehicle charging/debit/IDR|6|458678.02, 659041.36, 444463.78, 741173.24, 720338.21, 473929.11|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_157|transport/Commuter pass/debit/IDR|3|718611.81, 731295.56, 590798.33|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_157|transport/Fuel refill/debit/IDR|5|661068.67, 599277.67, 552598.17, 752036.69, 756799.12|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_157|transport/Local taxi/debit/IDR|2|711393.64, 471832.26|repeated but not demonstrably recurrent|||
|user_157|transport/Parking and tolls/debit/IDR|3|560113.6, 672198.08, 482339.48|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_157|transport/Rail pass/debit/IDR|2|748572.46, 517570.19|repeated but not demonstrably recurrent|||
|user_157|transport/Ride-hailing trip/debit/IDR|4|627998.54, 627003.73, 590871.52, 540723.79|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_157|dining/Lunch with colleagues/debit/IDR|2|804641.2, 541699.04|repeated but not demonstrably recurrent|||
|user_157|dining/Family dinner/debit/IDR|3|549704.24, 745324.19, 545976.75|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_157|dining/Bakery and snacks/debit/IDR|4|514456.31, 574707.53, 557252.83, 632205.28|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_157|dining/Takeaway order/debit/IDR|2|664790.08, 768325.05|repeated but not demonstrably recurrent|||
|user_158|salary/Freelance milestone payment/credit/INR|2|124208.36, 141896.91|repeated but not demonstrably recurrent|||
|user_158|salary/Independent work payment/credit/INR|2|73104.02, 61095.14|repeated but not demonstrably recurrent|||
|user_158|rent/Shared housing rent/debit/INR|6|67600, 67600, 67600, 67600, 67600, 67600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_158|utilities/Municipal utilities/debit/INR|5|12666.5, 13624.18, 12553.89, 12501.31, 13873.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_158|cloud_storage/Shared storage plan/debit/INR|5|935, 935, 935, 935, 935|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_158|streaming/Streaming subscription/debit/INR|5|6560, 6560, 6560, 6560, 6560|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_158|shopping/Online retail purchases/debit/INR|5|10111.97, 9769.31, 11530.92, 11331.6, 10472.21|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_158|salary/Application project payment/credit/INR|2|82971.1, 134850.67|repeated but not demonstrably recurrent|||
|user_158|groceries/Neighbourhood grocer/debit/INR|2|9672.6, 8936.57|repeated but not demonstrably recurrent|||
|user_158|groceries/Household groceries/debit/INR|2|6298.97, 5907.4|repeated but not demonstrably recurrent|||
|user_158|groceries/Supermarket basket/debit/INR|4|9177.94, 8685.42, 6032.74, 9965.33|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_158|groceries/Local market purchase/debit/INR|3|8258.56, 6046.91, 6965.18|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_158|groceries/Weekly produce market/debit/INR|2|9317.84, 9036.35|repeated but not demonstrably recurrent|||
|user_158|groceries/Grocery delivery/debit/INR|2|9543.84, 5948.67|repeated but not demonstrably recurrent|||
|user_158|groceries/Bulk pantry shop/debit/INR|2|7086.43, 6917.8|repeated but not demonstrably recurrent|||
|user_158|transport/Vehicle charging/debit/INR|4|5814.09, 3599.51, 3716.58, 5801.94|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_158|dining/Neighbourhood restaurant/debit/INR|2|7403.95, 8181.2|repeated but not demonstrably recurrent|||
|user_158|dining/Coffee shop/debit/INR|2|6870.33, 6215.07|repeated but not demonstrably recurrent|||
|user_158|dining/Quick-service meal/debit/INR|2|4775.34, 7092.1|repeated but not demonstrably recurrent|||
|user_159|salary/Driver platform payout/credit/ZAR|5|2921.37, 2640.53, 3821.23, 3138.32, 3734.56|variable but recurrent|24|RECURRING_AMOUNT_UNRESOLVED|
|user_159|salary/Delivery platform payout/credit/ZAR|6|3759.01, 2834.74, 2653.51, 2299.52, 3358.43, 3721.37|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_159|salary/Weekly app earnings/credit/ZAR|5|4004.21, 2633.83, 2862.93, 3226.4, 2653.67|variable but recurrent|9|RECURRING_AMOUNT_UNRESOLVED|
|user_159|rent/Apartment rent transfer/debit/ZAR|5|4114, 4114, 4114, 4114, 4114|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_159|utilities/Energy provider bill/debit/ZAR|5|591.01, 621.74, 632.51, 751.4, 725.74|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_159|music_subscription/Music subscription/debit/ZAR|5|79.2, 79.2, 79.2, 79.2, 79.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_159|delivery_membership/Grocery delivery membership/debit/ZAR|5|156.2, 156.2, 156.2, 156.2, 156.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_159|gym/Community fitness plan/debit/ZAR|5|261.8, 261.8, 261.8, 261.8, 261.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_159|entertainment/Cinema and events/debit/ZAR|5|403.45, 416.14, 468.72, 467.06, 468.42|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_159|salary/Task marketplace payout/credit/ZAR|4|2678.41, 3033.7, 3536.6, 2560.16|variable but recurrent|23|RECURRING_AMOUNT_UNRESOLVED|
|user_159|groceries/Fresh food shop/debit/ZAR|3|445.05, 396.71, 606.42|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_159|groceries/Weekly produce market/debit/ZAR|3|612.4, 476.7, 402.26|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_159|groceries/Local market purchase/debit/ZAR|4|685.17, 603.19, 551.06, 605.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_159|groceries/Bulk pantry shop/debit/ZAR|4|482.88, 520.59, 565.21, 619.17|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_159|groceries/Supermarket basket/debit/ZAR|2|639.66, 641.38|repeated but not demonstrably recurrent|||
|user_159|groceries/Neighbourhood grocer/debit/ZAR|2|555.61, 681.28|repeated but not demonstrably recurrent|||
|user_159|groceries/Household groceries/debit/ZAR|6|640.85, 474.56, 599.01, 398.74, 672.42, 552.35|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_159|transport/Rail pass/debit/ZAR|6|212.7, 230.55, 320.38, 213.76, 290.61, 341.15|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_159|transport/Fuel refill/debit/ZAR|3|289.48, 351.23, 227.49|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_159|transport/Parking and tolls/debit/ZAR|3|356.56, 238.87, 372.55|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_159|transport/Ride-hailing trip/debit/ZAR|5|257.2, 348.87, 267.05, 295.58, 334.99|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_159|transport/Commuter pass/debit/ZAR|2|251.54, 297.88|repeated but not demonstrably recurrent|||
|user_159|transport/Vehicle charging/debit/ZAR|2|293.37, 288.42|repeated but not demonstrably recurrent|||
|user_159|transport/Local taxi/debit/ZAR|3|336.72, 356.96, 300.08|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_159|dining/Coffee shop/debit/ZAR|3|419.86, 367.22, 548.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_159|dining/Bakery and snacks/debit/ZAR|3|431.11, 346.33, 390.93|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_159|dining/Neighbourhood restaurant/debit/ZAR|2|429.42, 499.67|repeated but not demonstrably recurrent|||
|user_159|dining/Family dinner/debit/ZAR|2|473.41, 404.1|repeated but not demonstrably recurrent|||
|user_160|salary/Previous employer payroll/credit/EUR|4|1672, 1672, 1672, 1672|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_160|rent/Monthly rent/debit/EUR|6|534.6, 534.6, 534.6, 534.6, 534.6, 534.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_160|utilities/Energy provider bill/debit/EUR|6|101.12, 101.89, 102.01, 98.52, 107.6, 105.68|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_160|debt_repayment/Vehicle loan payment/debit/EUR|5|199, 199, 199, 199, 199|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_160|music_subscription/Music service subscription/debit/EUR|5|15, 15, 15, 15, 15|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_160|groceries/Local market purchase/debit/EUR|4|64.68, 81.27, 59.82, 69.14|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_160|groceries/Weekly produce market/debit/EUR|3|93.12, 61.48, 63.75|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_160|groceries/Grocery delivery/debit/EUR|2|84.72, 73.32|repeated but not demonstrably recurrent|||
|user_160|groceries/Household groceries/debit/EUR|2|81.43, 83.3|repeated but not demonstrably recurrent|||
|user_160|transport/Metro and bus fares/debit/EUR|2|37.25, 39.27|repeated but not demonstrably recurrent|||
|user_160|transport/Rail pass/debit/EUR|2|48.67, 40.22|repeated but not demonstrably recurrent|||
|user_160|dining/Quick-service meal/debit/EUR|2|71.57, 61.15|repeated but not demonstrably recurrent|||
|user_160|dining/Takeaway order/debit/EUR|3|69.33, 56.38, 43.63|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_161|rent/Landlord standing order/debit/IDR|6|8265000, 8265000, 8265000, 8265000, 8265000, 8265000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_161|utilities/Water and power payment/debit/IDR|5|1945034.11, 1643688.13, 1826725.75, 1631523.7, 1971928.05|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_161|education/Professional training fee/debit/IDR|5|2329400, 2329400, 2329400, 2329400, 2329400|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_161|debt_repayment/Education loan instalment/debit/IDR|5|2802500, 2802500, 2802500, 2802500, 2802500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_161|music_subscription/Music service subscription/debit/IDR|5|319200, 319200, 319200, 319200, 319200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_161|delivery_membership/Food delivery membership/debit/IDR|5|280250, 280250, 280250, 280250, 280250|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_161|groceries/Grocery delivery/debit/IDR|3|1207186.92, 1161658.5, 1296045.06|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_161|groceries/Household groceries/debit/IDR|3|1389625.71, 1192643.35, 1374369.29|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_161|groceries/Local market purchase/debit/IDR|5|1121931.37, 1122319.64, 978665.76, 819525.67, 1267144.03|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_161|groceries/Weekly produce market/debit/IDR|3|1170363.44, 874140.99, 1400429.61|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_161|groceries/Neighbourhood grocer/debit/IDR|2|1375591.62, 1296784.93|repeated but not demonstrably recurrent|||
|user_161|groceries/Supermarket basket/debit/IDR|4|1115280.59, 796615.95, 1360459.37, 936046.2|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_161|groceries/Fresh food shop/debit/IDR|4|1223841.58, 1252960.33, 1129712.71, 1046626.74|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_161|groceries/Bulk pantry shop/debit/IDR|2|1257668.49, 1096506.54|repeated but not demonstrably recurrent|||
|user_161|transport/Parking and tolls/debit/IDR|6|370459.55, 522920.91, 463907.18, 463897.53, 623998.03, 615180.3|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_161|transport/Fuel refill/debit/IDR|4|395688.79, 429801.67, 459091.26, 449977.89|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_161|transport/Commuter pass/debit/IDR|6|564491.08, 546860.64, 567493.1, 544534.47, 413722.12, 442384.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_161|transport/Metro and bus fares/debit/IDR|2|453016.01, 591964.09|repeated but not demonstrably recurrent|||
|user_161|transport/Local taxi/debit/IDR|3|397176.01, 428391.55, 621025.1|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_161|transport/Ride-hailing trip/debit/IDR|2|497888.67, 584785.84|repeated but not demonstrably recurrent|||
|user_161|transport/Vehicle charging/debit/IDR|2|632854.62, 512323.96|repeated but not demonstrably recurrent|||
|user_161|dining/Weekend food delivery/debit/IDR|2|1314945.18, 1338808.75|repeated but not demonstrably recurrent|||
|user_161|dining/Bakery and snacks/debit/IDR|2|1221812, 822732.91|repeated but not demonstrably recurrent|||
|user_161|dining/Quick-service meal/debit/IDR|2|1208494.3, 829596.42|repeated but not demonstrably recurrent|||
|user_161|dining/Neighbourhood restaurant/debit/IDR|2|1062496.76, 957822.5|repeated but not demonstrably recurrent|||
|user_161|dining/Takeaway order/debit/IDR|2|1175447.45, 1244197.58|repeated but not demonstrably recurrent|||
|user_161|dining/Coffee shop/debit/IDR|2|1239486.86, 1066369.58|repeated but not demonstrably recurrent|||
|user_162|salary/Payroll credit/credit/IDR|5|22674600, 22674600, 22674600, 22674600, 22674600|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_162|housing/Home repair reserve/debit/IDR|6|2242000, 2242000, 2242000, 2242000, 2242000, 2242000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_162|utilities/Energy provider bill/debit/IDR|5|1367991.94, 1496668.17, 1366853.8, 1479954.78, 1448393|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_162|insurance/Health insurance premium/debit/IDR|5|860700, 860700, 860700, 860700, 860700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_162|healthcare/Therapy appointment/debit/IDR|5|1061891.73, 1064786.32, 1023325.49, 1072993.99, 906152.79|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_162|streaming/Streaming subscription/debit/IDR|5|782800, 782800, 782800, 782800, 782800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_162|groceries/Grocery delivery/debit/IDR|2|1469258.26, 1409318.49|repeated but not demonstrably recurrent|||
|user_162|groceries/Bulk pantry shop/debit/IDR|3|1174858.32, 1354961.05, 1131397.06|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_162|groceries/Fresh food shop/debit/IDR|4|1350056.32, 1407347.08, 1170228.16, 1438438.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_162|groceries/Neighbourhood grocer/debit/IDR|2|1340648.21, 1133180.91|repeated but not demonstrably recurrent|||
|user_162|groceries/Weekly produce market/debit/IDR|2|1268096.64, 1072203.93|repeated but not demonstrably recurrent|||
|user_162|groceries/Local market purchase/debit/IDR|3|1408320.35, 1404605.58, 976350.21|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_162|transport/Vehicle charging/debit/IDR|3|890772.77, 600660.37, 619521.48|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_162|transport/Rail pass/debit/IDR|2|909935.59, 618801.71|repeated but not demonstrably recurrent|||
|user_162|transport/Ride-hailing trip/debit/IDR|2|872151.59, 952742.57|repeated but not demonstrably recurrent|||
|user_162|transport/Fuel refill/debit/IDR|2|770455, 605074.43|repeated but not demonstrably recurrent|||
|user_162|dining/Lunch with colleagues/debit/IDR|2|1135032.37, 1418814.22|repeated but not demonstrably recurrent|||
|user_162|dining/Bakery and snacks/debit/IDR|2|1328162.69, 1515099.71|repeated but not demonstrably recurrent|||
|user_162|dining/Family dinner/debit/IDR|3|1313370.77, 1131674.09, 907118.01|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_162|dining/Neighbourhood restaurant/debit/IDR|2|1479709.32, 1072939.71|repeated but not demonstrably recurrent|||
|user_162|dining/Coffee shop/debit/IDR|3|1256530.44, 1249009.08, 895628.58|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_163|salary/Payroll credit/credit/IDR|5|30400000, 30400000, 30400000, 30400000, 30400000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_163|rent/Residential rent payment/debit/IDR|6|6802000, 6802000, 6802000, 6802000, 6802000, 6802000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_163|utilities/Electricity and water bill/debit/IDR|5|1370049.81, 1469087.14, 1545810.55, 1318290.39, 1589775.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_163|debt_repayment/Credit card repayment/debit/IDR|5|4636000, 4636000, 4636000, 4636000, 4636000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_163|streaming/Family streaming plan/debit/IDR|5|720100, 720100, 720100, 720100, 720100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_163|cloud_storage/Online backup subscription/debit/IDR|5|209000, 209000, 209000, 209000, 209000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_163|shopping/Clothing and household items/debit/IDR|5|805211.81, 722194.59, 799625.15, 755575.12, 729502.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_163|groceries/Grocery delivery/debit/IDR|8|1294835.75, 907929.8, 840604.04, 832313.31, 1164272.23, 1095188.51, 852236.24, 1314117.44|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_163|groceries/Neighbourhood grocer/debit/IDR|2|997499.74, 890239.21|repeated but not demonstrably recurrent|||
|user_163|groceries/Local market purchase/debit/IDR|2|1397270.82, 1095715.77|repeated but not demonstrably recurrent|||
|user_163|groceries/Fresh food shop/debit/IDR|3|1270899.1, 1439988.44, 1356075.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_163|groceries/Supermarket basket/debit/IDR|6|1219442.13, 908287, 1436347.11, 1068337.29, 1439431.98, 1416906.45|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_163|groceries/Bulk pantry shop/debit/IDR|2|1176673.98, 1204026.75|repeated but not demonstrably recurrent|||
|user_163|transport/Ride-hailing trip/debit/IDR|7|849524.24, 759840.43, 804718.75, 862269.07, 865848.94, 718095.07, 879279.6|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_163|transport/Vehicle charging/debit/IDR|2|772436.18, 877615.15|repeated but not demonstrably recurrent|||
|user_163|transport/Commuter pass/debit/IDR|2|621279.77, 680476.87|repeated but not demonstrably recurrent|||
|user_163|transport/Fuel refill/debit/IDR|5|587564.12, 672571.27, 683328.91, 589492.13, 611382.87|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_163|transport/Rail pass/debit/IDR|2|845859.76, 714496.14|repeated but not demonstrably recurrent|||
|user_163|transport/Local taxi/debit/IDR|3|856704.69, 890049.46, 742180.4|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_163|transport/Parking and tolls/debit/IDR|3|569317.97, 543682.93, 802046.56|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_163|dining/Lunch with colleagues/debit/IDR|2|1029586.9, 1637705.56|repeated but not demonstrably recurrent|||
|user_163|dining/Bakery and snacks/debit/IDR|2|1691452.64, 1075864.64|repeated but not demonstrably recurrent|||
|user_163|dining/Neighbourhood restaurant/debit/IDR|4|1419545.42, 1453808.97, 1684338.95, 1319476.55|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_164|salary/Base salary/credit/IDR|5|26562000, 26562000, 26562000, 26562000, 26562000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_164|housing/Home association fee/debit/IDR|6|4474500, 4474500, 4474500, 4474500, 4474500, 4474500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_164|utilities/Energy provider bill/debit/IDR|5|3020527.72, 2888381.44, 2658261.05, 2775803.27, 2917512.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_164|insurance/Insurance policy payment/debit/IDR|5|1727100, 1727100, 1727100, 1727100, 1727100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_164|education/Child education fee/debit/IDR|5|2943100, 2943100, 2943100, 2943100, 2943100|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_164|healthcare/Diagnostic test/debit/IDR|5|3467909.66, 3246831.7, 3185180.6, 3070385.76, 3202739.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_164|entertainment/Games and recreation/debit/IDR|5|820925.83, 735053.97, 866244.86, 812587.41, 777359.15|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_164|cloud_storage/Online backup subscription/debit/IDR|5|310650, 310650, 310650, 310650, 310650|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_164|salary/Account commission payment/credit/IDR|3|22919323.42, 10979499.55, 25515681.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_164|groceries/Local market purchase/debit/IDR|3|1836849.28, 2386312.74, 1755155.38|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_164|groceries/Weekly produce market/debit/IDR|4|2063544.01, 2095422.17, 2199901.04, 2443066.27|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_164|groceries/Supermarket basket/debit/IDR|2|1857111.22, 2036615.05|repeated but not demonstrably recurrent|||
|user_164|groceries/Household groceries/debit/IDR|2|2227988.31, 1510640.32|repeated but not demonstrably recurrent|||
|user_164|groceries/Neighbourhood grocer/debit/IDR|2|1459556.09, 2067519.29|repeated but not demonstrably recurrent|||
|user_164|groceries/Fresh food shop/debit/IDR|3|2024258.08, 1553244.64, 1536572.7|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_164|groceries/Bulk pantry shop/debit/IDR|2|1958369.1, 1558674.13|repeated but not demonstrably recurrent|||
|user_164|transport/Ride-hailing trip/debit/IDR|2|1231535.38, 1175747.45|repeated but not demonstrably recurrent|||
|user_164|transport/Local taxi/debit/IDR|5|1333415.09, 1320790.53, 947726.4, 1160711.64, 1374057.71|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_164|transport/Rail pass/debit/IDR|3|958202.51, 1399560.09, 1061694.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_164|dining/Neighbourhood restaurant/debit/IDR|2|1360178.94, 1496035.8|repeated but not demonstrably recurrent|||
|user_164|dining/Takeaway order/debit/IDR|2|1436506.36, 1348932.72|repeated but not demonstrably recurrent|||
|user_165|salary/Payroll credit/credit/INR|4|121000, 121000, 121000, 121000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_165|rent/Monthly rent/debit/INR|6|30900, 30900, 30900, 30900, 30900, 30900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_165|utilities/Energy provider bill/debit/INR|5|7108.92, 8216.5, 8422.84, 7136.16, 7589.04|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_165|cloud_storage/Cloud storage plan/debit/INR|5|425, 425, 425, 425, 425|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_165|streaming/Video streaming plan/debit/INR|5|3330, 3330, 3330, 3330, 3330|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_165|shopping/Online retail purchases/debit/INR|5|2881.34, 2933.32, 2518.39, 2337, 2861.42|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_165|groceries/Fresh food shop/debit/INR|2|5782.52, 4065.87|repeated but not demonstrably recurrent|||
|user_165|groceries/Local market purchase/debit/INR|3|3718.47, 5455.74, 5840.42|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_165|groceries/Weekly produce market/debit/INR|2|5224.07, 3587.47|repeated but not demonstrably recurrent|||
|user_165|groceries/Bulk pantry shop/debit/INR|6|4427.26, 5146.69, 3844.4, 5454.32, 5350.73, 5370.63|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_165|groceries/Supermarket basket/debit/INR|2|5619.06, 3324.04|repeated but not demonstrably recurrent|||
|user_165|transport/Rail pass/debit/INR|2|2274.81, 2630.23|repeated but not demonstrably recurrent|||
|user_165|transport/Fuel refill/debit/INR|2|2393.95, 3385.56|repeated but not demonstrably recurrent|||
|user_165|dining/Coffee shop/debit/INR|2|3468.19, 3781.82|repeated but not demonstrably recurrent|||
|user_165|dining/Bakery and snacks/debit/INR|2|2917.17, 3032.9|repeated but not demonstrably recurrent|||
|user_165|dining/Weekend food delivery/debit/INR|2|3378.72, 3415.55|repeated but not demonstrably recurrent|||
|user_166|salary/Freelance milestone payment/credit/USD|3|1018.96, 1271.72, 1125.03|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_166|salary/Content contract payment/credit/USD|2|645.11, 1368.95|repeated but not demonstrably recurrent|||
|user_166|rent/Residential rent payment/debit/USD|5|520.8, 520.8, 520.8, 520.8, 520.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_166|utilities/Water and power payment/debit/USD|5|151.39, 156.38, 145.89, 172.98, 167.36|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_166|cloud_storage/Shared storage plan/debit/USD|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_166|streaming/Family streaming plan/debit/USD|5|59, 59, 59, 59, 59|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_166|shopping/Clothing and household items/debit/USD|5|119.66, 101.26, 118.46, 109.77, 122.89|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_166|salary/Application project payment/credit/USD|2|617.15, 1209.77|repeated but not demonstrably recurrent|||
|user_166|salary/Design contract payment/credit/USD|2|1039.9, 1356.16|repeated but not demonstrably recurrent|||
|user_166|groceries/Bulk pantry shop/debit/USD|3|104.87, 114.03, 77.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_166|groceries/Neighbourhood grocer/debit/USD|4|89.4, 120.42, 117.02, 79.77|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_166|groceries/Grocery delivery/debit/USD|3|90.25, 111.21, 92.45|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_166|groceries/Local market purchase/debit/USD|3|88.58, 109.65, 101.65|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_166|groceries/Fresh food shop/debit/USD|4|122.94, 115.31, 88.1, 116.41|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_166|transport/Vehicle charging/debit/USD|3|54.55, 36.26, 39.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_166|transport/Local taxi/debit/USD|3|36.81, 36, 34.91|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_166|transport/Parking and tolls/debit/USD|2|38.09, 34.59|repeated but not demonstrably recurrent|||
|user_166|dining/Takeaway order/debit/USD|3|77.25, 83.27, 79.08|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_166|dining/Neighbourhood restaurant/debit/USD|3|116.38, 97.81, 115.73|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_167|salary/Payroll credit/credit/ZAR|5|47740, 47740, 47740, 47740, 47740|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_167|rent/Residential rent payment/debit/ZAR|6|15994, 15994, 15994, 15994, 15994, 15994|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_167|utilities/Electricity and water bill/debit/ZAR|5|2211.77, 2481.11, 2022.55, 2268.02, 2002.22|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_167|debt_repayment/Personal loan payment/debit/ZAR|5|6721, 6721, 6721, 6721, 6721|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_167|healthcare/Therapy appointment/debit/ZAR|5|2547.63, 2325.38, 2266.38, 2111.34, 2284.08|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_167|family_support/Parent support transfer/debit/ZAR|5|5011.6, 5011.6, 5011.6, 5011.6, 5011.6|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_167|cloud_storage/Cloud storage plan/debit/ZAR|5|354.2, 354.2, 354.2, 354.2, 354.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_167|shopping/Clothing and household items/debit/ZAR|5|2223.36, 2246.61, 2246.53, 2079.47, 2122.34|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_167|groceries/Grocery delivery/debit/ZAR|2|1248.24, 1939.92|repeated but not demonstrably recurrent|||
|user_167|groceries/Bulk pantry shop/debit/ZAR|6|2036.05, 1942.03, 1430.58, 1295.81, 2151.25, 1511.52|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_167|groceries/Fresh food shop/debit/ZAR|4|2094.32, 2092.56, 1800.87, 1723.22|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_167|groceries/Supermarket basket/debit/ZAR|5|1355.44, 1800.86, 1248.53, 1675.89, 1844.02|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_167|groceries/Household groceries/debit/ZAR|3|1525.87, 1655.41, 1635.93|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_167|groceries/Local market purchase/debit/ZAR|4|1600.28, 1488.83, 2052.6, 1479.58|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_167|transport/Rail pass/debit/ZAR|3|1139.82, 950.41, 1350.48|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_167|transport/Fuel refill/debit/ZAR|2|1399.4, 1025.74|repeated but not demonstrably recurrent|||
|user_167|transport/Commuter pass/debit/ZAR|4|1208.65, 1275.09, 853.26, 886.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_167|transport/Ride-hailing trip/debit/ZAR|3|1022.52, 1398.34, 968.03|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_168|salary/Payroll credit/credit/INR|5|137150, 137150, 137150, 137150, 75432.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|rent/Landlord standing order/debit/INR|6|38100, 38100, 38100, 38100, 38100, 38100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_168|utilities/Municipal utilities/debit/INR|6|9828.47, 8828.01, 9909.83, 9412.56, 9836.04, 9282.04|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_168|insurance/Vehicle insurance premium/debit/INR|6|3810, 3810, 3810, 3810, 3810, 3810|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_168|cloud_storage/Online backup subscription/debit/INR|5|540, 540, 540, 540, 540|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_168|streaming/Video streaming plan/debit/INR|5|3630, 3630, 3630, 3630, 3630|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_168|shopping/Household shopping/debit/INR|5|6941.77, 6925.03, 6254.09, 6394.82, 7505.87|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|entertainment/Monthly entertainment spend/debit/INR|5|5532.4, 4847.4, 4893.34, 4654.74, 5304.83|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|groceries/Grocery delivery/debit/INR|4|4276.82, 5537.87, 6762.17, 5138.15|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|groceries/Local market purchase/debit/INR|3|4334.01, 4872.3, 4860.33|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_168|groceries/Bulk pantry shop/debit/INR|3|6207.76, 4135.04, 7152.79|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|groceries/Fresh food shop/debit/INR|2|6338.54, 5449.81|repeated but not demonstrably recurrent|||
|user_168|groceries/Household groceries/debit/INR|3|4854.71, 5975.27, 5626.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Local taxi/debit/INR|6|2911.3, 3413.28, 2619.03, 3848.27, 2976.95, 3155.32|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Vehicle charging/debit/INR|3|3976.96, 2952.02, 3084.74|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Ride-hailing trip/debit/INR|6|3853.11, 2385.24, 3612.12, 4136.02, 2436.52, 3487.94|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Commuter pass/debit/INR|3|3465.55, 2612.54, 2479.69|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Rail pass/debit/INR|7|3749.37, 2884.14, 3761.91, 3910.57, 2577.13, 3277.97, 4168.14|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Metro and bus fares/debit/INR|4|2887.81, 3006.69, 2722.13, 3081.48|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Parking and tolls/debit/INR|4|3883.75, 2501.7, 3047.74, 3060.65|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_168|transport/Fuel refill/debit/INR|3|2891.31, 2930.44, 3753.67|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_168|dining/Bakery and snacks/debit/INR|6|5029.38, 3890.17, 5520.32, 5526.95, 5386.91, 4473.69|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_168|dining/Coffee shop/debit/INR|4|4816.05, 3953.61, 3939.83, 3907.95|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_168|dining/Family dinner/debit/INR|5|4827.53, 3835.18, 3604.6, 3759.57, 5053.5|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_168|dining/Lunch with colleagues/debit/INR|4|5601.62, 3608.59, 4160.11, 3366.75|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_168|dining/Quick-service meal/debit/INR|3|5536.73, 3998.91, 4136.34|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_168|dining/Takeaway order/debit/INR|2|4357.05, 4045.21|repeated but not demonstrably recurrent|||
|user_169|salary/Payroll credit/credit/EUR|5|33000, 33000, 33000, 33000, 33000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_169|rent/Monthly rent/debit/ZAR|6|8932, 8932, 8932, 8932, 8932, 8932|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_169|utilities/Household utility payment/debit/ZAR|5|1555.4, 1606.32, 1562.89, 1755.25, 1679.76|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_169|insurance/Household insurance/debit/ZAR|5|1647.8, 1647.8, 1647.8, 1647.8, 1647.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_169|cloud_storage/Cloud storage plan/debit/ZAR|5|258.5, 258.5, 258.5, 258.5, 258.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_169|streaming/Video streaming plan/debit/ZAR|5|864.6, 864.6, 864.6, 864.6, 864.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_169|shopping/Monthly shopping spend/debit/ZAR|5|1243.35, 1345.81, 1282.82, 1421.72, 1467.3|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_169|entertainment/Local event tickets/debit/ZAR|5|851.94, 995.32, 966.73, 938.94, 958.95|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_169|groceries/Household groceries/debit/ZAR|4|1152.28, 1366.28, 1036.1, 1434.41|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_169|groceries/Neighbourhood grocer/debit/ZAR|4|1539.02, 1060.37, 1021.75, 1704.13|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_169|groceries/Weekly produce market/debit/ZAR|3|1345.42, 1532.82, 1669.14|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_169|groceries/Bulk pantry shop/debit/ZAR|4|1742.57, 1334.85, 1614.22, 1120.63|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_169|transport/Rail pass/debit/ZAR|9|751.47, 717.15, 630.15, 830.23, 696.95, 698.89, 639.27, 665.41, 934.46|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_169|transport/Vehicle charging/debit/ZAR|5|564.49, 874.39, 633.41, 910.82, 745.32|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_169|transport/Local taxi/debit/ZAR|5|746.9, 678.31, 781.3, 658.36, 648.69|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_169|transport/Metro and bus fares/debit/ZAR|2|926.04, 632.14|repeated but not demonstrably recurrent|||
|user_169|transport/Ride-hailing trip/debit/ZAR|6|856.83, 549.92, 579.57, 779.27, 857.94, 680.41|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_169|transport/Parking and tolls/debit/ZAR|3|876.78, 848.8, 558.43|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_169|transport/Fuel refill/debit/ZAR|5|742.42, 814.37, 758.44, 902.8, 578.95|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_169|dining/Neighbourhood restaurant/debit/ZAR|7|1070.26, 1196.92, 962.42, 1067.99, 1292.7, 1337.68, 937.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_169|dining/Bakery and snacks/debit/ZAR|2|1165.83, 1319.37|repeated but not demonstrably recurrent|||
|user_169|dining/Takeaway order/debit/ZAR|3|961.02, 1159.47, 859.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_169|dining/Quick-service meal/debit/ZAR|5|835.96, 1100.26, 1058.02, 1002.21, 1086.15|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_169|dining/Lunch with colleagues/debit/ZAR|2|1017.62, 1255.63|repeated but not demonstrably recurrent|||
|user_169|dining/Coffee shop/debit/ZAR|4|1189.11, 1394.37, 1190.63, 817.61|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_170|salary/Payroll credit/credit/IDR|5|38760000, 38760000, 38760000, 38760000, 38760000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_170|rent/Landlord standing order/debit/IDR|6|10507000, 10507000, 10507000, 10507000, 10507000, 10507000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_170|utilities/Water and power payment/debit/IDR|5|1844266.09, 1579111.28, 1977476.83, 1831321.31, 1619905.76|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_170|education/School fee payment/debit/IDR|5|1989300, 1989300, 1989300, 1989300, 1989300|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_170|debt_repayment/Personal loan payment/debit/IDR|5|5605000, 5605000, 5605000, 5605000, 5605000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_170|music_subscription/Audio streaming plan/debit/IDR|5|306850, 306850, 306850, 306850, 306850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_170|delivery_membership/Grocery delivery membership/debit/IDR|5|576650, 576650, 576650, 576650, 576650|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_170|groceries/Neighbourhood grocer/debit/IDR|8|1587242.68, 1928614.33, 1396085.16, 1861745.26, 1400725.74, 1630668.94, 1819948.05, 1981734.22|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_170|groceries/Fresh food shop/debit/IDR|6|1268958.86, 1870479, 1192609.8, 1499371.49, 1541462.02, 1787719.16|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_170|groceries/Grocery delivery/debit/IDR|2|1541240.57, 1684868.32|repeated but not demonstrably recurrent|||
|user_170|groceries/Bulk pantry shop/debit/IDR|3|1963780.86, 1538716.3, 1870392.65|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_170|groceries/Weekly produce market/debit/IDR|2|1488132.56, 1274294.27|repeated but not demonstrably recurrent|||
|user_170|groceries/Local market purchase/debit/IDR|3|1325708.45, 1422770.59, 1945718.78|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_170|transport/Rail pass/debit/IDR|3|866956.44, 644744.19, 892359.95|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_170|transport/Local taxi/debit/IDR|4|575950.12, 980578.1, 857074.55, 594899.75|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_170|transport/Ride-hailing trip/debit/IDR|5|815891.35, 641896.05, 681125.97, 967314.81, 658407.98|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_170|transport/Commuter pass/debit/IDR|6|778616.73, 855572.68, 595654.11, 654042.49, 612483.06, 660623.63|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_170|transport/Vehicle charging/debit/IDR|3|673780.55, 788031.76, 983422.22|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_170|transport/Parking and tolls/debit/IDR|3|560976.73, 720848.16, 868887.54|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_170|dining/Neighbourhood restaurant/debit/IDR|2|1422067.86, 1976180.26|repeated but not demonstrably recurrent|||
|user_170|dining/Quick-service meal/debit/IDR|3|1554770.59, 1814790.94, 1994050.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_170|dining/Family dinner/debit/IDR|2|1745928.45, 1519448.02|repeated but not demonstrably recurrent|||
|user_170|dining/Lunch with colleagues/debit/IDR|2|1376116.13, 1343401.58|repeated but not demonstrably recurrent|||
|user_170|dining/Weekend food delivery/debit/IDR|2|1336698.9, 1219776.17|repeated but not demonstrably recurrent|||
|user_171|salary/Payroll credit/credit/EUR|5|693, 693, 693, 693, 693|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_171|housing/Building maintenance payment/debit/EUR|5|81, 81, 81, 81, 81|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_171|utilities/Energy provider bill/debit/EUR|5|44.84, 41.43, 44.92, 37.61, 40.46|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_171|insurance/Household insurance/debit/EUR|5|22, 22, 22, 22, 22|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_171|healthcare/Diagnostic test/debit/EUR|5|38.27, 38.36, 33.95, 39.62, 36.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_171|streaming/Streaming subscription/debit/EUR|5|17, 17, 17, 17, 17|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_171|groceries/Bulk pantry shop/debit/EUR|2|26.23, 28.08|repeated but not demonstrably recurrent|||
|user_171|groceries/Weekly produce market/debit/EUR|3|36.03, 27.12, 39.01|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_171|groceries/Neighbourhood grocer/debit/EUR|3|30.56, 24.86, 32.46|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_171|groceries/Grocery delivery/debit/EUR|2|37.63, 34.45|repeated but not demonstrably recurrent|||
|user_171|groceries/Supermarket basket/debit/EUR|2|34.78, 36.73|repeated but not demonstrably recurrent|||
|user_171|groceries/Fresh food shop/debit/EUR|5|38.92, 38.77, 34.82, 30.02, 29.64|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_171|transport/Vehicle charging/debit/EUR|3|18.85, 14.69, 11.73|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_171|transport/Local taxi/debit/EUR|2|15.71, 15.56|repeated but not demonstrably recurrent|||
|user_171|transport/Ride-hailing trip/debit/EUR|4|20.39, 18.93, 17.46, 15.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_171|transport/Parking and tolls/debit/EUR|3|15.76, 15, 19.54|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_171|dining/Quick-service meal/debit/EUR|2|38.04, 28.05|repeated but not demonstrably recurrent|||
|user_171|dining/Bakery and snacks/debit/EUR|4|33.3, 27.91, 22.01, 24.96|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_171|dining/Family dinner/debit/EUR|2|29.44, 26.1|repeated but not demonstrably recurrent|||
|user_171|dining/Neighbourhood restaurant/debit/EUR|2|27.11, 34.33|repeated but not demonstrably recurrent|||
|user_171|dining/Lunch with colleagues/debit/EUR|2|22.64, 36.84|repeated but not demonstrably recurrent|||
|user_172|salary/Payroll credit/credit/ZAR|5|34540, 34540, 34540, 34540, 34540|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_172|rent/Landlord standing order/debit/ZAR|6|10340, 10340, 10340, 10340, 10340, 10340|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_172|utilities/Household utility payment/debit/ZAR|5|1883.56, 1759.83, 1617.26, 1888.13, 1626.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_172|debt_repayment/Loan repayment/debit/ZAR|5|5148, 5148, 5148, 5148, 5148|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_172|healthcare/Diagnostic test/debit/ZAR|5|1340.66, 1461.96, 1409.37, 1411.86, 1543.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_172|family_support/Dependent care payment/debit/ZAR|5|3058, 3058, 3058, 3058, 3058|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_172|cloud_storage/Online backup subscription/debit/ZAR|5|290.4, 290.4, 290.4, 290.4, 290.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_172|shopping/Monthly shopping spend/debit/ZAR|5|854.6, 874.64, 738.33, 835.57, 720.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_172|groceries/Neighbourhood grocer/debit/ZAR|8|1281.73, 1191.4, 1476.51, 1498.63, 1519.46, 1714.32, 1448.04, 1084.85|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_172|groceries/Local market purchase/debit/ZAR|4|1832.22, 1082.8, 1698.28, 1310.46|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_172|groceries/Grocery delivery/debit/ZAR|3|1361.19, 1791.53, 1470.94|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_172|groceries/Weekly produce market/debit/ZAR|3|1837.95, 1304.29, 1868.29|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_172|groceries/Fresh food shop/debit/ZAR|2|1427.35, 1236.93|repeated but not demonstrably recurrent|||
|user_172|groceries/Bulk pantry shop/debit/ZAR|4|1368.39, 1418.4, 1141.77, 1873.5|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_172|groceries/Household groceries/debit/ZAR|2|1908.52, 1723.13|repeated but not demonstrably recurrent|||
|user_172|transport/Metro and bus fares/debit/ZAR|2|902.72, 609.75|repeated but not demonstrably recurrent|||
|user_172|transport/Commuter pass/debit/ZAR|2|564.78, 671.71|repeated but not demonstrably recurrent|||
|user_172|transport/Parking and tolls/debit/ZAR|3|818.17, 541.13, 914.71|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_172|transport/Ride-hailing trip/debit/ZAR|3|561.48, 648.88, 596.96|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_173|salary/International employer payroll/credit/USD|5|106995.72, 106995.72, 106995.72, 106995.72, 106995.72|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_173|rent/Apartment rent transfer/debit/INR|6|34000, 34000, 34000, 34000, 34000, 34000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_173|utilities/Household utility payment/debit/INR|6|6073.32, 5090.45, 5369.53, 5797.26, 5342.75, 5201.34|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_173|insurance/Vehicle insurance premium/debit/INR|5|4480, 4480, 4480, 4480, 4480|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_173|cloud_storage/Cloud storage plan/debit/INR|5|420, 420, 420, 420, 420|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_173|streaming/Video streaming plan/debit/INR|5|3140, 3140, 3140, 3140, 3140|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_173|shopping/Household shopping/debit/INR|5|3420.26, 3551.22, 3058.81, 3531.58, 3365.59|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_173|entertainment/Weekend entertainment/debit/INR|5|1866.94, 1800.11, 1798.9, 1789.32, 1779|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_173|groceries/Household groceries/debit/INR|3|3344.67, 4211.18, 5468.08|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_173|groceries/Weekly produce market/debit/INR|3|4624.65, 4970.12, 3236.74|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_173|groceries/Fresh food shop/debit/INR|4|4978.39, 3744.75, 4179.21, 5089.75|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_173|groceries/Grocery delivery/debit/INR|3|4929.92, 5386.52, 3712.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_173|groceries/Local market purchase/debit/INR|2|5304.21, 3582.48|repeated but not demonstrably recurrent|||
|user_173|groceries/Supermarket basket/debit/INR|2|4981.31, 4750.06|repeated but not demonstrably recurrent|||
|user_173|transport/Fuel refill/debit/INR|6|1875.38, 2442.4, 2237.07, 1583.54, 1845.45, 2507.55|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_173|transport/Ride-hailing trip/debit/INR|5|1571.77, 1528.53, 2148.56, 2256.76, 2406.88|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_173|transport/Vehicle charging/debit/INR|5|1421.4, 2254.54, 1757.09, 1654.09, 2149.92|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_173|transport/Local taxi/debit/INR|5|2051.57, 1630.88, 1857.93, 1932.23, 2140.97|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_173|transport/Metro and bus fares/debit/INR|5|1447.51, 2515.4, 2458, 2144.89, 2421.96|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_173|transport/Rail pass/debit/INR|6|1816.02, 1692.83, 1816.88, 1975.23, 1867.22, 2438.75|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_173|transport/Commuter pass/debit/INR|3|1441.9, 1720.89, 2365.62|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_173|dining/Family dinner/debit/INR|6|3259.27, 3096.42, 4146.05, 4433.63, 4667.87, 4779.32|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_173|dining/Lunch with colleagues/debit/INR|2|3953.34, 4550.99|repeated but not demonstrably recurrent|||
|user_173|dining/Coffee shop/debit/INR|3|3473.22, 5090.62, 5271.1|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_173|dining/Weekend food delivery/debit/INR|3|3710.77, 4115.89, 3989.2|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_173|dining/Neighbourhood restaurant/debit/INR|2|3065.12, 5237.03|repeated but not demonstrably recurrent|||
|user_173|dining/Quick-service meal/debit/INR|4|5286.8, 3492.4, 3163.77, 3248.03|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_173|dining/Bakery and snacks/debit/INR|2|4500.42, 3641.57|repeated but not demonstrably recurrent|||
|user_173|dining/Takeaway order/debit/INR|3|3569.46, 4382.17, 3723.83|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_174|salary/Payroll credit/credit/EUR|4|880, 880, 880, 880|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_174|rent/Shared housing rent/debit/EUR|6|204.6, 204.6, 204.6, 204.6, 204.6, 204.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_174|utilities/Municipal utilities/debit/EUR|5|54.5, 61.88, 65.48, 63.51, 58.03|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_174|cloud_storage/Online backup subscription/debit/EUR|5|8, 8, 8, 8, 8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_174|streaming/Video streaming plan/debit/EUR|5|17, 17, 17, 17, 17|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_174|shopping/Household shopping/debit/EUR|5|41.73, 39.6, 42.93, 44.6, 43.52|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_174|groceries/Fresh food shop/debit/EUR|5|30.07, 29.67, 40.48, 30.11, 32.49|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_174|groceries/Local market purchase/debit/EUR|2|28.53, 27.94|repeated but not demonstrably recurrent|||
|user_174|groceries/Grocery delivery/debit/EUR|4|38.58, 29, 31.22, 42.12|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_174|groceries/Neighbourhood grocer/debit/EUR|2|36.67, 30.57|repeated but not demonstrably recurrent|||
|user_174|groceries/Weekly produce market/debit/EUR|3|36.52, 38.53, 28.02|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_174|transport/Ride-hailing trip/debit/EUR|2|23.52, 24.54|repeated but not demonstrably recurrent|||
|user_174|transport/Fuel refill/debit/EUR|2|28, 21.66|repeated but not demonstrably recurrent|||
|user_174|transport/Metro and bus fares/debit/EUR|3|17.69, 23.46, 17.28|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_174|dining/Quick-service meal/debit/EUR|2|28.93, 30.21|repeated but not demonstrably recurrent|||
|user_174|dining/Family dinner/debit/EUR|2|31.95, 27.47|repeated but not demonstrably recurrent|||
|user_174|dining/Lunch with colleagues/debit/EUR|2|24.56, 21.37|repeated but not demonstrably recurrent|||
|user_175|salary/Payroll credit/credit/EUR|5|2673, 2673, 2673, 1924.56, 1924.56|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_175|rent/Monthly rent/debit/EUR|6|496.1, 496.1, 496.1, 496.1, 496.1, 496.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_175|utilities/Energy provider bill/debit/EUR|5|102.56, 112.04, 111.77, 110.09, 96.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_175|music_subscription/Music service subscription/debit/EUR|5|12, 12, 12, 12, 12|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_175|delivery_membership/Delivery service plan/debit/EUR|5|19, 19, 19, 19, 19|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_175|gym/Gym membership/debit/EUR|5|43, 43, 43, 43, 43|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_175|entertainment/Weekend entertainment/debit/EUR|5|29.36, 27.71, 32.23, 28.01, 32.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_175|groceries/Weekly produce market/debit/EUR|4|112.13, 89.31, 70.47, 84.87|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_175|groceries/Fresh food shop/debit/EUR|4|109.65, 94.11, 88.94, 104.99|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_175|groceries/Bulk pantry shop/debit/EUR|5|111.16, 70.78, 110.3, 71.1, 68.87|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_175|groceries/Local market purchase/debit/EUR|4|112.58, 108.67, 92.05, 106.58|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_175|groceries/Household groceries/debit/EUR|5|74.44, 103.44, 87.94, 113.96, 114.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_175|groceries/Neighbourhood grocer/debit/EUR|2|102.59, 94.59|repeated but not demonstrably recurrent|||
|user_175|transport/Rail pass/debit/EUR|4|50.15, 29.29, 35.47, 36|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_175|transport/Commuter pass/debit/EUR|5|30.49, 34.45, 35.73, 46.41, 37.46|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_175|transport/Metro and bus fares/debit/EUR|4|36.09, 34.66, 45.72, 31.87|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_175|transport/Vehicle charging/debit/EUR|3|34.26, 40.69, 50.06|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_175|transport/Fuel refill/debit/EUR|3|31.15, 50.67, 34.39|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_175|transport/Ride-hailing trip/debit/EUR|2|38.09, 43.28|repeated but not demonstrably recurrent|||
|user_175|transport/Parking and tolls/debit/EUR|2|37.98, 41.92|repeated but not demonstrably recurrent|||
|user_175|transport/Local taxi/debit/EUR|2|33.86, 39.83|repeated but not demonstrably recurrent|||
|user_175|dining/Neighbourhood restaurant/debit/EUR|2|80.5, 63.85|repeated but not demonstrably recurrent|||
|user_175|dining/Bakery and snacks/debit/EUR|2|76.95, 76.11|repeated but not demonstrably recurrent|||
|user_175|dining/Weekend food delivery/debit/EUR|4|85.39, 91.09, 89.74, 78.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_175|dining/Family dinner/debit/EUR|2|79.75, 54.09|repeated but not demonstrably recurrent|||
|user_176|salary/Base salary/credit/EUR|5|508.2, 508.2, 508.2, 508.2, 508.2|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_176|salary/Account commission payment/credit/EUR|2|116.71, 379.12|repeated but not demonstrably recurrent|||
|user_176|rent/Residential rent payment/debit/EUR|6|258.5, 258.5, 258.5, 258.5, 258.5, 258.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_176|utilities/Municipal utilities/debit/EUR|5|56.02, 63.12, 53.42, 54.09, 63.28|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_176|debt_repayment/Loan repayment/debit/EUR|5|45, 45, 45, 45, 45|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_176|healthcare/Clinic payment/debit/EUR|5|24.52, 27.47, 27.83, 24.68, 22.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_176|family_support/Parent support transfer/debit/EUR|5|57, 57, 57, 57, 57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_176|cloud_storage/Shared storage plan/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_176|shopping/Personal shopping/debit/EUR|5|27.76, 26.8, 30.88, 29.92, 31.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_176|salary/Monthly sales commission/credit/EUR|2|364.31, 326.91|repeated but not demonstrably recurrent|||
|user_176|groceries/Weekly produce market/debit/EUR|5|29.3, 47.73, 32.9, 28.17, 36.39|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_176|groceries/Neighbourhood grocer/debit/EUR|3|38.37, 29.5, 47.37|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_176|groceries/Grocery delivery/debit/EUR|5|42.77, 34.09, 32.37, 31.52, 45.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_176|groceries/Supermarket basket/debit/EUR|3|44.95, 44.45, 36.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_176|groceries/Household groceries/debit/EUR|2|46.19, 43.68|repeated but not demonstrably recurrent|||
|user_176|groceries/Fresh food shop/debit/EUR|3|33.2, 33.49, 47.06|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_176|groceries/Local market purchase/debit/EUR|4|40.94, 44.9, 38.68, 37.55|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_176|transport/Rail pass/debit/EUR|2|22.78, 17.08|repeated but not demonstrably recurrent|||
|user_176|transport/Fuel refill/debit/EUR|2|23.39, 17.75|repeated but not demonstrably recurrent|||
|user_176|transport/Vehicle charging/debit/EUR|2|25.85, 25.13|repeated but not demonstrably recurrent|||
|user_176|transport/Local taxi/debit/EUR|3|16.84, 24.94, 26.34|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_176|transport/Metro and bus fares/debit/EUR|2|25.64, 22.95|repeated but not demonstrably recurrent|||
|user_177|salary/Payroll credit/credit/USD|5|1731.6, 1731.6, 1731.6, 1731.6, 952.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_177|rent/Apartment rent transfer/debit/USD|6|490.8, 490.8, 490.8, 490.8, 490.8, 490.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_177|utilities/Electricity and water bill/debit/USD|5|71.4, 87.45, 72.64, 84.68, 78.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_177|insurance/Household insurance/debit/USD|5|51, 51, 51, 51, 51|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_177|cloud_storage/Cloud storage plan/debit/USD|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_177|streaming/Video streaming plan/debit/USD|5|51, 51, 51, 51, 51|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_177|shopping/Monthly shopping spend/debit/USD|5|87.2, 89.41, 77.97, 83.67, 76.28|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_177|entertainment/Games and recreation/debit/USD|5|34.57, 34, 28.8, 34.51, 32.77|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_177|groceries/Supermarket basket/debit/USD|3|50.4, 66.35, 77.04|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_177|groceries/Fresh food shop/debit/USD|2|46.12, 67.17|repeated but not demonstrably recurrent|||
|user_177|groceries/Grocery delivery/debit/USD|4|51.17, 68.3, 50.64, 76.36|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_177|groceries/Household groceries/debit/USD|4|60.71, 73.98, 53.8, 57.28|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_177|groceries/Local market purchase/debit/USD|2|65.64, 79.97|repeated but not demonstrably recurrent|||
|user_177|transport/Metro and bus fares/debit/USD|8|40.86, 29.17, 38.19, 31.24, 35.68, 31.65, 37.37, 42.89|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_177|transport/Parking and tolls/debit/USD|4|41.83, 39.27, 41.11, 45.1|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_177|transport/Commuter pass/debit/USD|6|38.87, 31.05, 38.53, 44.96, 35.09, 42.42|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_177|transport/Ride-hailing trip/debit/USD|6|50.11, 35.63, 45.89, 36.38, 35.77, 50.33|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_177|transport/Vehicle charging/debit/USD|4|32.07, 43.46, 42.27, 50.82|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_177|transport/Local taxi/debit/USD|4|44.13, 48.73, 49.29, 42.75|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_177|transport/Rail pass/debit/USD|3|34.32, 50.21, 43.48|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_177|dining/Coffee shop/debit/USD|4|78.18, 72.39, 53.42, 48.97|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_177|dining/Family dinner/debit/USD|6|58.11, 70.77, 50.78, 72.59, 67.36, 68.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_177|dining/Lunch with colleagues/debit/USD|3|53.73, 62.66, 68.57|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_177|dining/Bakery and snacks/debit/USD|2|53.3, 71.52|repeated but not demonstrably recurrent|||
|user_177|dining/Neighbourhood restaurant/debit/USD|4|72.61, 56.28, 81.84, 71.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_177|dining/Takeaway order/debit/USD|4|58.09, 66.31, 64.8, 69.22|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_178|salary/Client retainer payment/credit/EUR|2|953.43, 916.52|repeated but not demonstrably recurrent|||
|user_178|rent/Apartment rent transfer/debit/EUR|6|540.1, 540.1, 540.1, 540.1, 540.1, 540.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_178|utilities/Energy provider bill/debit/EUR|5|152.07, 154.73, 138.83, 131.64, 145.42|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_178|cloud_storage/Online backup subscription/debit/EUR|5|8, 8, 8, 8, 8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_178|streaming/Video streaming plan/debit/EUR|5|49, 49, 49, 49, 49|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_178|shopping/Household shopping/debit/EUR|5|114.8, 119.58, 121.79, 114.02, 123.9|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_178|salary/Freelance milestone payment/credit/EUR|2|1054.76, 1423.4|repeated but not demonstrably recurrent|||
|user_178|salary/Content contract payment/credit/EUR|2|1124.05, 805.91|repeated but not demonstrably recurrent|||
|user_178|salary/Website project payment/credit/EUR|2|1164.55, 1029.8|repeated but not demonstrably recurrent|||
|user_178|groceries/Neighbourhood grocer/debit/EUR|3|96.23, 77.83, 73.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_178|groceries/Local market purchase/debit/EUR|4|69.15, 80.83, 78.59, 79.78|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_178|groceries/Fresh food shop/debit/EUR|3|113.5, 85.27, 107.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_178|groceries/Supermarket basket/debit/EUR|3|78.7, 65.5, 81.43|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_178|groceries/Household groceries/debit/EUR|3|110.27, 99.57, 111.36|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_178|transport/Metro and bus fares/debit/EUR|2|74.06, 75.93|repeated but not demonstrably recurrent|||
|user_178|transport/Commuter pass/debit/EUR|2|55.43, 57.48|repeated but not demonstrably recurrent|||
|user_178|transport/Rail pass/debit/EUR|2|61.64, 56.59|repeated but not demonstrably recurrent|||
|user_178|dining/Takeaway order/debit/EUR|2|72.76, 49.69|repeated but not demonstrably recurrent|||
|user_178|dining/Lunch with colleagues/debit/EUR|2|77.72, 47.96|repeated but not demonstrably recurrent|||
|user_179|salary/Payroll credit/credit/IDR|5|48830000, 48830000, 48830000, 48830000, 48830000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_179|rent/Apartment rent transfer/debit/IDR|5|13623000, 13623000, 13623000, 13623000, 13623000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_179|utilities/Energy provider bill/debit/IDR|5|2997806.63, 3364701.8, 3183278, 3423052.97, 3319630.16|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_179|education/Course tuition/debit/IDR|5|2698000, 2698000, 2698000, 2698000, 2698000|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_179|debt_repayment/Vehicle loan payment/debit/IDR|5|3401000, 3401000, 3401000, 3401000, 3401000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_179|music_subscription/Music subscription/debit/IDR|5|426550, 426550, 426550, 426550, 426550|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_179|delivery_membership/Delivery service plan/debit/IDR|5|794200, 794200, 794200, 794200, 794200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_179|groceries/Supermarket basket/debit/IDR|6|2116301.4, 1669738.67, 1486396.47, 2087467.93, 1911727.42, 2251577.66|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_179|groceries/Fresh food shop/debit/IDR|3|1918356.91, 1680998.04, 1558846.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_179|groceries/Bulk pantry shop/debit/IDR|7|1813928.64, 1654148.9, 2256075.12, 2242791.65, 2042891.95, 2224273.52, 1593183.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_179|groceries/Household groceries/debit/IDR|3|2152938.84, 2092352.8, 1466138.85|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_179|groceries/Weekly produce market/debit/IDR|2|2395730.8, 1752698.3|repeated but not demonstrably recurrent|||
|user_179|groceries/Local market purchase/debit/IDR|3|1858322.24, 2532455.46, 1654754.24|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_179|transport/Vehicle charging/debit/IDR|3|1412962.21, 1197287.61, 1023589.59|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_179|transport/Rail pass/debit/IDR|3|1208457.55, 1372502.45, 1320827.22|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_179|transport/Local taxi/debit/IDR|3|1399241.18, 1278450.4, 1008494.29|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_179|transport/Parking and tolls/debit/IDR|4|1392262.5, 1252535.57, 1533989.13, 1110108.36|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_179|transport/Ride-hailing trip/debit/IDR|6|1454116.62, 1078879.67, 1057514.65, 1454851.45, 1242284.22, 1504343.89|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_179|transport/Metro and bus fares/debit/IDR|2|1299942.33, 1097199.14|repeated but not demonstrably recurrent|||
|user_179|transport/Commuter pass/debit/IDR|3|1376590.41, 1147119.38, 1282304|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_179|dining/Weekend food delivery/debit/IDR|2|1926324.03, 1516742.13|repeated but not demonstrably recurrent|||
|user_179|dining/Quick-service meal/debit/IDR|3|1200463.23, 1725075.15, 1262604.46|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_179|dining/Takeaway order/debit/IDR|2|1640822.61, 1599811.45|repeated but not demonstrably recurrent|||
|user_179|dining/Bakery and snacks/debit/IDR|3|1543915.49, 1589321.13, 1228478.93|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_179|dining/Lunch with colleagues/debit/IDR|2|1823585.87, 1721690.95|repeated but not demonstrably recurrent|||
|user_180|rent/Monthly rent/debit/INR|6|17400, 17400, 17400, 17400, 17400, 17400|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_180|utilities/Electricity and water bill/debit/INR|6|3365.76, 3540.6, 3407.54, 3686.27, 3184.69, 3442.75|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_180|education/School fee payment/debit/INR|5|4600, 4600, 4600, 4600, 4600|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_180|debt_repayment/Education loan instalment/debit/INR|5|7250, 7250, 7250, 7250, 7250|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_180|music_subscription/Music service subscription/debit/INR|5|660, 660, 660, 660, 660|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_180|delivery_membership/Food delivery membership/debit/INR|5|955, 955, 955, 955, 955|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_180|salary/First-job payroll/credit/INR|2|59000, 59000|repeated but not demonstrably recurrent|||
|user_180|groceries/Fresh food shop/debit/INR|2|3109.33, 2563.11|repeated but not demonstrably recurrent|||
|user_180|groceries/Bulk pantry shop/debit/INR|4|2327.99, 2222.82, 2345.02, 2986.64|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_180|groceries/Supermarket basket/debit/INR|4|2360.7, 2063.24, 3030.22, 1888.77|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_180|groceries/Grocery delivery/debit/INR|5|2732.82, 2017.45, 1991.61, 2727.3, 2445.36|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_180|groceries/Weekly produce market/debit/INR|4|3164.22, 2310.51, 2003.51, 2780.39|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_180|groceries/Neighbourhood grocer/debit/INR|2|2111.69, 2767.17|repeated but not demonstrably recurrent|||
|user_180|groceries/Household groceries/debit/INR|4|3025.37, 2468.14, 1912.97, 2626.14|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_180|transport/Commuter pass/debit/INR|5|1366.12, 1369.23, 1369.06, 1295.86, 969.02|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_180|transport/Vehicle charging/debit/INR|5|962.34, 1065.98, 1237.96, 1544.55, 1104.65|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_180|transport/Ride-hailing trip/debit/INR|4|1209.68, 1518.74, 1368.94, 984.42|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_180|transport/Rail pass/debit/INR|3|942.63, 1238.8, 1126.53|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_180|transport/Fuel refill/debit/INR|2|1126.44, 1071.88|repeated but not demonstrably recurrent|||
|user_180|transport/Local taxi/debit/INR|3|1307.72, 1049.93, 973.93|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_180|transport/Metro and bus fares/debit/INR|3|952.66, 1078.1, 995.59|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_180|dining/Neighbourhood restaurant/debit/INR|2|1243.97, 1699.97|repeated but not demonstrably recurrent|||
|user_180|dining/Coffee shop/debit/INR|3|1999.91, 1754.25, 1627.1|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_180|dining/Bakery and snacks/debit/INR|4|1983.57, 1247.38, 1310.38, 1864.91|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_180|dining/Takeaway order/debit/INR|2|1222.47, 1632.11|repeated but not demonstrably recurrent|||
|user_181|salary/Payroll credit/credit/USD|5|2580, 2580, 2580, 2580, 2580|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_181|rent/Landlord standing order/debit/USD|6|877.2, 877.2, 877.2, 877.2, 877.2, 877.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_181|utilities/Water and power payment/debit/USD|5|129.15, 140.66, 115.1, 116.79, 116.35|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_181|debt_repayment/Education loan instalment/debit/USD|5|232, 232, 232, 232, 232|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_181|streaming/Video streaming plan/debit/USD|5|54, 54, 54, 54, 54|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_181|cloud_storage/Cloud storage plan/debit/USD|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_181|shopping/Monthly shopping spend/debit/USD|5|143.96, 147.81, 127.88, 141.31, 148.08|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_181|groceries/Supermarket basket/debit/USD|4|81.68, 124.69, 75.24, 88.7|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_181|groceries/Fresh food shop/debit/USD|2|86.39, 102.1|repeated but not demonstrably recurrent|||
|user_181|groceries/Weekly produce market/debit/USD|3|120.25, 98.9, 89.11|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_181|groceries/Household groceries/debit/USD|2|90.19, 124.13|repeated but not demonstrably recurrent|||
|user_181|groceries/Neighbourhood grocer/debit/USD|4|126.23, 113.45, 80.02, 88.81|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_181|groceries/Grocery delivery/debit/USD|5|104.14, 109.02, 93.82, 91.63, 116.26|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_181|groceries/Local market purchase/debit/USD|5|113.83, 112.6, 98.9, 115.26, 92.45|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_181|transport/Fuel refill/debit/USD|3|81.26, 78.45, 74.73|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_181|transport/Commuter pass/debit/USD|6|54.77, 82.58, 69.96, 75.62, 72.76, 56.27|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_181|transport/Rail pass/debit/USD|2|64.9, 82.65|repeated but not demonstrably recurrent|||
|user_181|transport/Local taxi/debit/USD|5|71.08, 76.88, 52.91, 59.82, 75.37|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_181|transport/Ride-hailing trip/debit/USD|4|51.7, 66.06, 59.98, 52.48|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_181|transport/Parking and tolls/debit/USD|4|68.69, 53.01, 67.04, 72.26|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_181|dining/Family dinner/debit/USD|4|129.78, 113.56, 125.86, 128.62|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_181|dining/Lunch with colleagues/debit/USD|3|138.57, 120.69, 113.8|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_181|dining/Neighbourhood restaurant/debit/USD|3|106.1, 89.59, 147.69|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_182|salary/Payroll credit/credit/ZAR|5|52800, 52800, 52800, 52800, 52800|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_182|housing/Home repair reserve/debit/ZAR|6|5522, 5522, 5522, 5522, 5522, 5522|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_182|utilities/Electricity and water bill/debit/ZAR|5|2958.34, 3020.79, 3181.31, 3497.36, 3188.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_182|insurance/Household insurance/debit/ZAR|5|2171.4, 2171.4, 2171.4, 2171.4, 2171.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_182|education/Professional training fee/debit/ZAR|5|3979.8, 3979.8, 3979.8, 3979.8, 3979.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_182|healthcare/Family healthcare expense/debit/ZAR|5|2347.5, 2231.36, 2153.76, 2384.76, 2446.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_182|entertainment/Cinema and events/debit/ZAR|5|2001.06, 2233.17, 2259.19, 1830.99, 2153.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_182|cloud_storage/Online backup subscription/debit/ZAR|5|261.8, 261.8, 261.8, 261.8, 261.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_182|groceries/Weekly produce market/debit/ZAR|5|1840.96, 2518.89, 2391.86, 2366.14, 2202.56|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_182|groceries/Household groceries/debit/ZAR|2|2361.51, 2473.88|repeated but not demonstrably recurrent|||
|user_182|groceries/Neighbourhood grocer/debit/ZAR|6|2416.34, 1956.7, 1485.65, 1793.53, 1716.4, 2284.79|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_182|groceries/Bulk pantry shop/debit/ZAR|3|1735.41, 1711.08, 2219.08|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_182|transport/Fuel refill/debit/ZAR|2|1311.4, 1325.69|repeated but not demonstrably recurrent|||
|user_182|transport/Commuter pass/debit/ZAR|2|953.09, 1394.71|repeated but not demonstrably recurrent|||
|user_182|transport/Parking and tolls/debit/ZAR|2|1612.12, 1218.06|repeated but not demonstrably recurrent|||
|user_182|transport/Rail pass/debit/ZAR|2|1341.71, 1376.13|repeated but not demonstrably recurrent|||
|user_182|transport/Local taxi/debit/ZAR|2|1448.53, 1107.21|repeated but not demonstrably recurrent|||
|user_182|dining/Quick-service meal/debit/ZAR|2|1895.9, 1397.36|repeated but not demonstrably recurrent|||
|user_182|dining/Family dinner/debit/ZAR|2|1464.49, 1524.83|repeated but not demonstrably recurrent|||
|user_182|dining/Lunch with colleagues/debit/ZAR|2|1513.88, 1999.6|repeated but not demonstrably recurrent|||
|user_183|salary/Payroll credit/credit/USD|5|20899995.60, 20899995.60, 20899995.60, 20899995.60, 20899995.60|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_183|rent/Shared housing rent/debit/IDR|6|5776000, 5776000, 5776000, 5776000, 5776000, 5776000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_183|utilities/Electricity and water bill/debit/IDR|5|1076415.3, 1003788.34, 998528.45, 1214067.39, 1170077.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_183|insurance/Vehicle insurance premium/debit/IDR|5|646000, 646000, 646000, 646000, 646000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_183|cloud_storage/Shared storage plan/debit/IDR|5|157700, 157700, 157700, 157700, 157700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_183|streaming/Streaming subscription/debit/IDR|5|511100, 511100, 511100, 511100, 511100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_183|shopping/Household shopping/debit/IDR|5|965808.79, 919619.02, 930711.79, 914698.03, 833984.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_183|entertainment/Cinema and events/debit/IDR|5|723787.79, 764665.23, 636529.93, 757176.28, 607320.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_183|groceries/Neighbourhood grocer/debit/IDR|3|1099371.01, 1010776.32, 1158028.93|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_183|groceries/Local market purchase/debit/IDR|3|1208007.58, 1105968.99, 983467.98|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_183|groceries/Supermarket basket/debit/IDR|2|716072.01, 1133406.74|repeated but not demonstrably recurrent|||
|user_183|groceries/Fresh food shop/debit/IDR|3|1003284.91, 1146459.1, 1200515.62|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_183|groceries/Household groceries/debit/IDR|2|960141.87, 987838.53|repeated but not demonstrably recurrent|||
|user_183|groceries/Bulk pantry shop/debit/IDR|2|1086662.8, 1126565.57|repeated but not demonstrably recurrent|||
|user_183|groceries/Grocery delivery/debit/IDR|2|973590.56, 890425.51|repeated but not demonstrably recurrent|||
|user_183|transport/Local taxi/debit/IDR|6|491022.99, 474774.85, 369434.17, 540041.08, 477675.94, 423315.05|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_183|transport/Ride-hailing trip/debit/IDR|10|580369.54, 605825.6, 463088.59, 408972.61, 582563.26, 565829.35, 526102.07, 648277.84, 379838.56, 516573.53|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_183|transport/Rail pass/debit/IDR|4|452718.3, 506637.22, 377568.14, 652711.36|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_183|transport/Metro and bus fares/debit/IDR|3|618452.61, 624735.64, 513238.53|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_183|transport/Fuel refill/debit/IDR|3|484061.72, 599343.34, 390752.19|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_183|transport/Vehicle charging/debit/IDR|4|522923.28, 539085.94, 527364.15, 468418.54|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_183|transport/Parking and tolls/debit/IDR|4|454505.71, 616658.18, 649671.84, 647475.96|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Quick-service meal/debit/IDR|3|553528.77, 479441.78, 531198.58|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Family dinner/debit/IDR|5|615037.96, 542517.73, 722372.86, 702893.13, 601341.66|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Coffee shop/debit/IDR|3|679672.42, 495760.92, 576310.49|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Neighbourhood restaurant/debit/IDR|3|446012.68, 706706.77, 536754.84|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Lunch with colleagues/debit/IDR|5|491668.68, 495630.56, 563189.3, 429631.83, 505234.31|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Bakery and snacks/debit/IDR|4|443742.41, 607908.97, 478757.22, 635815.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_183|dining/Weekend food delivery/debit/IDR|2|520363.98, 570433.42|repeated but not demonstrably recurrent|||
|user_184|salary/Payroll credit/credit/USD|5|131994.72, 131994.72, 131994.72, 131994.72, 131994.72|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_184|rent/Monthly rent/debit/INR|6|42300, 42300, 42300, 42300, 42300, 42300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_184|utilities/Household utility payment/debit/INR|5|8059.15, 9383.2, 8631.76, 7883.6, 8461.03|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_184|insurance/Insurance policy payment/debit/INR|5|5490, 5490, 5490, 5490, 5490|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_184|cloud_storage/Online backup subscription/debit/INR|5|1070, 1070, 1070, 1070, 1070|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_184|streaming/Streaming subscription/debit/INR|5|3020, 3020, 3020, 3020, 3020|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_184|shopping/Personal shopping/debit/INR|5|3309.69, 3059.89, 3002.18, 2773.86, 2881.56|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_184|entertainment/Monthly entertainment spend/debit/INR|5|3919.02, 3865.52, 3854.79, 3637.02, 3843.44|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_184|groceries/Household groceries/debit/INR|2|5357.95, 6298.49|repeated but not demonstrably recurrent|||
|user_184|groceries/Grocery delivery/debit/INR|2|4577.47, 4538.45|repeated but not demonstrably recurrent|||
|user_184|groceries/Neighbourhood grocer/debit/INR|2|5021.63, 6490.28|repeated but not demonstrably recurrent|||
|user_184|groceries/Supermarket basket/debit/INR|2|5113.48, 5745.27|repeated but not demonstrably recurrent|||
|user_184|groceries/Weekly produce market/debit/INR|3|3776.88, 4924.87, 5763.26|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_184|groceries/Fresh food shop/debit/INR|3|4386.82, 4342.1, 5615.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_184|groceries/Bulk pantry shop/debit/INR|2|5907.51, 4576.74|repeated but not demonstrably recurrent|||
|user_184|groceries/Local market purchase/debit/INR|2|5227.68, 3775.54|repeated but not demonstrably recurrent|||
|user_184|transport/Metro and bus fares/debit/INR|4|2262.01, 2160.76, 2214.04, 2380.67|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_184|transport/Fuel refill/debit/INR|6|3091.77, 2451.68, 2704.31, 3176.35, 3262.8, 3323.01|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_184|transport/Rail pass/debit/INR|4|1933.3, 2350.1, 2420.67, 2100.08|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_184|transport/Parking and tolls/debit/INR|6|2663.54, 3368.16, 2455.62, 3199.5, 3282.36, 2251.44|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_184|transport/Commuter pass/debit/INR|2|2530.03, 2315.65|repeated but not demonstrably recurrent|||
|user_184|transport/Ride-hailing trip/debit/INR|5|2398, 2487.19, 2628.6, 2778.08, 2978.19|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_184|transport/Vehicle charging/debit/INR|5|2515.22, 3136.72, 2575.55, 2587.09, 2072.71|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_184|transport/Local taxi/debit/INR|4|2265.41, 1996.17, 2228.65, 2627.49|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_184|dining/Weekend food delivery/debit/INR|5|5559.13, 6483.71, 4617.09, 4325.86, 4347.13|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_184|dining/Family dinner/debit/INR|2|6840.14, 4532.94|repeated but not demonstrably recurrent|||
|user_184|dining/Coffee shop/debit/INR|5|6397.39, 4529.27, 6792.41, 4787.05, 4139.41|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_184|dining/Neighbourhood restaurant/debit/INR|3|3972.68, 4621.95, 5395.06|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_184|dining/Quick-service meal/debit/INR|5|4354.28, 6101.37, 4039.27, 5449.82, 5051.03|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_184|dining/Lunch with colleagues/debit/INR|2|5094.57, 6191.57|repeated but not demonstrably recurrent|||
|user_184|dining/Takeaway order/debit/INR|2|4237.63, 6603.28|repeated but not demonstrably recurrent|||
|user_184|dining/Bakery and snacks/debit/INR|2|6459.5, 5743.62|repeated but not demonstrably recurrent|||
|user_185|salary/Payroll credit/credit/EUR|5|1562, 1562, 1562, 1562, 1562|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_185|rent/Apartment rent transfer/debit/EUR|6|451, 451, 451, 451, 451, 451|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_185|utilities/Municipal utilities/debit/EUR|5|104.62, 89.45, 100.65, 91.46, 90.09|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_185|debt_repayment/Education loan instalment/debit/EUR|5|102, 102, 102, 102, 102|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_185|streaming/Video streaming plan/debit/EUR|5|31, 31, 31, 31, 31|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_185|cloud_storage/Cloud storage plan/debit/EUR|5|6, 6, 6, 6, 6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_185|shopping/Monthly shopping spend/debit/EUR|5|61.17, 50.56, 61.38, 53.4, 61.28|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Bulk pantry shop/debit/EUR|3|69.57, 89.88, 69.34|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Fresh food shop/debit/EUR|3|66.07, 79.63, 86.18|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Weekly produce market/debit/EUR|4|68.01, 55.19, 87.55, 75.76|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Local market purchase/debit/EUR|2|60.8, 55.37|repeated but not demonstrably recurrent|||
|user_185|groceries/Supermarket basket/debit/EUR|3|81.28, 86.95, 67.7|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Grocery delivery/debit/EUR|4|84.59, 68.27, 69.78, 75.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Household groceries/debit/EUR|3|69.81, 52.78, 58.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_185|groceries/Neighbourhood grocer/debit/EUR|4|90.92, 83.48, 63.92, 60.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_185|transport/Vehicle charging/debit/EUR|4|41.46, 36.41, 40.05, 43.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_185|transport/Metro and bus fares/debit/EUR|2|41.21, 37.02|repeated but not demonstrably recurrent|||
|user_185|transport/Parking and tolls/debit/EUR|3|48.64, 49.52, 48.39|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_185|transport/Commuter pass/debit/EUR|4|45.69, 33.56, 41.19, 30.77|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_185|transport/Fuel refill/debit/EUR|3|45.44, 46.25, 47.26|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_185|transport/Local taxi/debit/EUR|7|35.92, 35.34, 35.56, 36.42, 48.01, 35.31, 37.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_185|transport/Rail pass/debit/EUR|3|36.94, 36.19, 33.96|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_185|dining/Weekend food delivery/debit/EUR|3|72.97, 51.26, 74.47|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_185|dining/Quick-service meal/debit/EUR|3|73.16, 83.51, 70.75|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_185|dining/Family dinner/debit/EUR|2|76.35, 79.33|repeated but not demonstrably recurrent|||
|user_185|dining/Takeaway order/debit/EUR|2|65.36, 51.51|repeated but not demonstrably recurrent|||
|user_186|salary/Payroll credit/credit/ZAR|5|31889, 31889, 31889, 31889, 17538.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_186|rent/Apartment rent transfer/debit/ZAR|5|7348, 7348, 7348, 7348, 7348|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_186|utilities/Household utility payment/debit/ZAR|5|1978.12, 1872.23, 1915.86, 1863.95, 2009.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_186|insurance/Household insurance/debit/ZAR|5|807.4, 807.4, 807.4, 807.4, 807.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_186|cloud_storage/Shared storage plan/debit/ZAR|5|128.7, 128.7, 128.7, 128.7, 128.7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_186|streaming/Video streaming plan/debit/ZAR|5|750.2, 750.2, 750.2, 750.2, 750.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_186|shopping/Household shopping/debit/ZAR|5|1813.21, 1698.39, 1584.11, 1581.76, 1692.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_186|entertainment/Weekend entertainment/debit/ZAR|5|1125.55, 950.07, 1025.86, 1129.83, 1023|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_186|groceries/Household groceries/debit/ZAR|2|1165.83, 1442.74|repeated but not demonstrably recurrent|||
|user_186|groceries/Grocery delivery/debit/ZAR|7|1411.36, 1475.26, 1168.88, 1384.7, 1389.68, 1473.86, 1286.19|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_186|groceries/Supermarket basket/debit/ZAR|2|1050.28, 1043.38|repeated but not demonstrably recurrent|||
|user_186|groceries/Local market purchase/debit/ZAR|3|1433.99, 1004.89, 1264.17|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_186|groceries/Fresh food shop/debit/ZAR|2|1128.96, 1302.35|repeated but not demonstrably recurrent|||
|user_186|transport/Parking and tolls/debit/ZAR|4|638.74, 536.51, 602.6, 522.38|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_186|transport/Metro and bus fares/debit/ZAR|7|820.08, 668.03, 855.16, 790.16, 605.72, 828.82, 881.18|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_186|transport/Ride-hailing trip/debit/ZAR|6|711.59, 880.67, 548.64, 697.92, 902.36, 744.97|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_186|transport/Vehicle charging/debit/ZAR|4|572.21, 855.93, 700.04, 758.91|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_186|transport/Local taxi/debit/ZAR|3|553.82, 777.6, 768.44|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_186|transport/Commuter pass/debit/ZAR|8|860.69, 827.56, 606.35, 584.36, 540.43, 666.77, 759, 785.84|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_186|transport/Fuel refill/debit/ZAR|2|543.99, 883.13|repeated but not demonstrably recurrent|||
|user_186|dining/Family dinner/debit/ZAR|3|1043.69, 1545.6, 1051.46|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_186|dining/Coffee shop/debit/ZAR|5|1319.3, 1401.64, 970.7, 1334.07, 1520.58|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_186|dining/Quick-service meal/debit/ZAR|6|1464.18, 1244.79, 1354.15, 1307.39, 1011.35, 1480.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_186|dining/Weekend food delivery/debit/ZAR|3|1274.11, 1339.31, 1522.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_186|dining/Takeaway order/debit/ZAR|4|1480.35, 1171.36, 1563.44, 1438.84|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_186|dining/Lunch with colleagues/debit/ZAR|3|1366.65, 1353.85, 1517.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_187|salary/Previous employer payroll/credit/INR|4|145000, 145000, 145000, 145000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_187|rent/Residential rent payment/debit/INR|6|34600, 34600, 34600, 34600, 34600, 34600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_187|utilities/Household utility payment/debit/INR|5|6717.13, 6576.5, 6618.99, 5980.75, 6013.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_187|debt_repayment/Loan repayment/debit/INR|5|13900, 13900, 13900, 13900, 13900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_187|music_subscription/Music service subscription/debit/INR|5|1945, 1945, 1945, 1945, 1945|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_187|groceries/Grocery delivery/debit/INR|2|7096.89, 7192.51|repeated but not demonstrably recurrent|||
|user_187|groceries/Local market purchase/debit/INR|2|4785.38, 7262.57|repeated but not demonstrably recurrent|||
|user_187|groceries/Weekly produce market/debit/INR|3|7968.83, 8344.27, 8143.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_187|groceries/Supermarket basket/debit/INR|2|8196.15, 7066.3|repeated but not demonstrably recurrent|||
|user_187|transport/Rail pass/debit/INR|2|2996.7, 2654.49|repeated but not demonstrably recurrent|||
|user_187|transport/Fuel refill/debit/INR|2|2390.65, 2174.27|repeated but not demonstrably recurrent|||
|user_187|transport/Metro and bus fares/debit/INR|2|3385.21, 2330.28|repeated but not demonstrably recurrent|||
|user_187|dining/Bakery and snacks/debit/INR|3|6516.01, 7919.36, 6615.21|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_187|dining/Takeaway order/debit/INR|2|7751.75, 5601.12|repeated but not demonstrably recurrent|||
|user_187|dining/Weekend food delivery/debit/INR|2|7576.38, 5840.39|repeated but not demonstrably recurrent|||
|user_188|salary/Payroll credit/credit/EUR|5|1386, 1386, 1386, 1386, 1386|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_188|rent/Monthly rent/debit/EUR|6|451, 451, 451, 451, 451, 451|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_188|utilities/Water and power payment/debit/EUR|6|66.24, 67.84, 79, 78.12, 80.61, 82.96|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_188|education/Course tuition/debit/EUR|5|80, 80, 80, 80, 80|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_188|debt_repayment/Loan repayment/debit/EUR|5|231, 231, 231, 231, 231|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_188|music_subscription/Music service subscription/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_188|delivery_membership/Food delivery membership/debit/EUR|5|20, 20, 20, 20, 20|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_188|groceries/Grocery delivery/debit/EUR|6|46.16, 75.78, 76.1, 73.42, 81.76, 73.87|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_188|groceries/Fresh food shop/debit/EUR|4|77.62, 52.85, 55.03, 48.05|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_188|groceries/Weekly produce market/debit/EUR|3|46.55, 56.83, 72.14|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_188|groceries/Household groceries/debit/EUR|2|49.94, 51.91|repeated but not demonstrably recurrent|||
|user_188|groceries/Supermarket basket/debit/EUR|2|72.46, 61.97|repeated but not demonstrably recurrent|||
|user_188|groceries/Neighbourhood grocer/debit/EUR|2|65.02, 52.31|repeated but not demonstrably recurrent|||
|user_188|groceries/Bulk pantry shop/debit/EUR|4|79.52, 50.55, 51.51, 59.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_188|groceries/Local market purchase/debit/EUR|3|47.76, 72.77, 78.48|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_188|transport/Metro and bus fares/debit/EUR|5|27.78, 27.69, 38.03, 42.67, 28.64|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_188|transport/Parking and tolls/debit/EUR|8|37.97, 33.62, 37.66, 41.44, 37.71, 34.51, 34.94, 35.17|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_188|transport/Local taxi/debit/EUR|2|28.1, 35.52|repeated but not demonstrably recurrent|||
|user_188|transport/Rail pass/debit/EUR|4|34.68, 46.52, 32.79, 40.6|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_188|transport/Fuel refill/debit/EUR|2|30.26, 38.9|repeated but not demonstrably recurrent|||
|user_188|transport/Commuter pass/debit/EUR|3|28.77, 40.61, 42.7|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_188|dining/Takeaway order/debit/EUR|2|32.11, 46.61|repeated but not demonstrably recurrent|||
|user_188|dining/Family dinner/debit/EUR|2|41.08, 34.28|repeated but not demonstrably recurrent|||
|user_188|dining/Coffee shop/debit/EUR|2|31.81, 38.37|repeated but not demonstrably recurrent|||
|user_188|dining/Neighbourhood restaurant/debit/EUR|2|32.94, 37.95|repeated but not demonstrably recurrent|||
|user_188|dining/Lunch with colleagues/debit/EUR|2|34.61, 32.34|repeated but not demonstrably recurrent|||
|user_188|dining/Weekend food delivery/debit/EUR|2|32.25, 46.28|repeated but not demonstrably recurrent|||
|user_189|salary/Payroll credit/credit/EUR|5|489.06, 489.06, 489.06, 489.06, 489.06|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_189|housing/Home association fee/debit/EUR|6|48, 48, 48, 48, 48, 48|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_189|utilities/Water and power payment/debit/EUR|5|43.77, 40.6, 37.78, 37.39, 38.57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_189|insurance/Vehicle insurance premium/debit/EUR|5|31, 31, 31, 31, 31|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_189|healthcare/Diagnostic test/debit/EUR|5|38.56, 32.03, 34.32, 38.05, 37.49|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_189|streaming/Streaming subscription/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_189|groceries/Fresh food shop/debit/EUR|5|32.35, 33.13, 25.43, 27.71, 27.59|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_189|groceries/Supermarket basket/debit/EUR|4|33.78, 21.13, 31.54, 35.28|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_189|groceries/Household groceries/debit/EUR|2|35.39, 22.01|repeated but not demonstrably recurrent|||
|user_189|groceries/Neighbourhood grocer/debit/EUR|3|32.94, 26.58, 25.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_189|groceries/Weekly produce market/debit/EUR|2|24.51, 31.37|repeated but not demonstrably recurrent|||
|user_189|transport/Vehicle charging/debit/EUR|3|11.37, 11.35, 11.88|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_189|transport/Ride-hailing trip/debit/EUR|2|15.91, 9.89|repeated but not demonstrably recurrent|||
|user_189|transport/Local taxi/debit/EUR|2|16.05, 10.46|repeated but not demonstrably recurrent|||
|user_189|transport/Metro and bus fares/debit/EUR|3|10.09, 9.87, 14.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_189|dining/Weekend food delivery/debit/EUR|3|15.44, 24.75, 25.69|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_189|dining/Bakery and snacks/debit/EUR|2|18.48, 15.37|repeated but not demonstrably recurrent|||
|user_189|dining/Lunch with colleagues/debit/EUR|3|18.58, 22.7, 17.6|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_189|dining/Coffee shop/debit/EUR|2|20.92, 20.51|repeated but not demonstrably recurrent|||
|user_190|salary/Payroll credit/credit/EUR|5|2849, 2849, 2849, 2849, 2849|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_190|rent/Residential rent payment/debit/EUR|6|728.2, 728.2, 728.2, 728.2, 728.2, 728.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_190|utilities/Electricity and water bill/debit/EUR|5|191.91, 177.26, 189.56, 195.37, 165.13|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_190|debt_repayment/Credit card repayment/debit/EUR|5|397, 397, 397, 397, 397|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_190|streaming/Video streaming plan/debit/EUR|5|65, 65, 65, 65, 65|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_190|cloud_storage/Cloud storage plan/debit/EUR|5|18, 18, 18, 18, 18|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_190|shopping/Online retail purchases/debit/EUR|5|78.13, 72.45, 66.16, 78.93, 83.93|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_190|groceries/Fresh food shop/debit/EUR|2|130.13, 117.94|repeated but not demonstrably recurrent|||
|user_190|groceries/Neighbourhood grocer/debit/EUR|3|104.41, 85.9, 84.44|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_190|groceries/Bulk pantry shop/debit/EUR|6|92.1, 95.72, 103.01, 101.55, 86.2, 129.55|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_190|groceries/Household groceries/debit/EUR|4|87.24, 100.15, 129.98, 126.27|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_190|groceries/Local market purchase/debit/EUR|4|125.13, 112.59, 84.34, 94.45|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_190|groceries/Supermarket basket/debit/EUR|3|89.02, 121.39, 123.71|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_190|groceries/Grocery delivery/debit/EUR|3|100.78, 103.55, 120.68|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_190|transport/Fuel refill/debit/EUR|4|85.99, 64.3, 68.84, 70.2|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_190|transport/Ride-hailing trip/debit/EUR|3|70.23, 73.43, 71.97|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_190|transport/Parking and tolls/debit/EUR|4|64.15, 81.93, 66.27, 85.66|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_190|transport/Vehicle charging/debit/EUR|4|56.78, 88.23, 88.18, 64.4|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_190|transport/Metro and bus fares/debit/EUR|4|85.37, 76.23, 89.3, 82.36|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_190|transport/Rail pass/debit/EUR|2|84.39, 81.94|repeated but not demonstrably recurrent|||
|user_190|transport/Local taxi/debit/EUR|3|54.37, 72.86, 63.62|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_190|dining/Family dinner/debit/EUR|2|58.41, 94|repeated but not demonstrably recurrent|||
|user_190|dining/Bakery and snacks/debit/EUR|5|71.4, 90.26, 93.84, 94.91, 77.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_190|dining/Coffee shop/debit/EUR|2|55.91, 73.57|repeated but not demonstrably recurrent|||
|user_190|dining/Weekend food delivery/debit/EUR|3|55.2, 95.35, 91.65|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_191|salary/Payroll credit/credit/EUR|5|814, 814, 814, 814, 814|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_191|housing/Home association fee/debit/EUR|5|74, 74, 74, 74, 74|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_191|utilities/Municipal utilities/debit/EUR|5|51.21, 48.32, 43.85, 49.81, 51.1|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_191|insurance/Insurance policy payment/debit/EUR|5|38, 38, 38, 38, 38|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_191|education/School fee payment/debit/EUR|5|47, 47, 47, 47, 47|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_191|healthcare/Family healthcare expense/debit/EUR|5|37.8, 37.24, 42.83, 38.66, 36.83|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_191|entertainment/Monthly entertainment spend/debit/EUR|5|13.23, 13.68, 13.84, 11.85, 12.93|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_191|cloud_storage/Online backup subscription/debit/EUR|5|4, 4, 4, 4, 4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_191|groceries/Supermarket basket/debit/EUR|2|43.61, 42.25|repeated but not demonstrably recurrent|||
|user_191|groceries/Fresh food shop/debit/EUR|2|40.02, 35.92|repeated but not demonstrably recurrent|||
|user_191|groceries/Bulk pantry shop/debit/EUR|3|30.2, 32, 27.55|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_191|groceries/Local market purchase/debit/EUR|4|33.31, 34.4, 46.04, 37.39|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_191|groceries/Household groceries/debit/EUR|3|34.99, 42.35, 32.36|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_191|groceries/Neighbourhood grocer/debit/EUR|2|31.05, 32.72|repeated but not demonstrably recurrent|||
|user_191|transport/Commuter pass/debit/EUR|3|21.65, 20.55, 18.11|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_191|transport/Metro and bus fares/debit/EUR|4|21.15, 15.4, 22.96, 15.09|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_191|transport/Fuel refill/debit/EUR|2|14.91, 14.46|repeated but not demonstrably recurrent|||
|user_191|dining/Weekend food delivery/debit/EUR|3|17.86, 26.61, 19.77|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_191|dining/Takeaway order/debit/EUR|2|17.7, 19.23|repeated but not demonstrably recurrent|||
|user_191|dining/Lunch with colleagues/debit/EUR|2|15.13, 16.4|repeated but not demonstrably recurrent|||
|user_192|salary/Base salary/credit/USD|5|813.6, 813.6, 813.6, 813.6, 813.6|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_192|salary/Performance commission/credit/USD|4|685.86, 636.75, 432.15, 393.53|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_192|rent/Monthly rent/debit/USD|6|375.6, 375.6, 375.6, 375.6, 375.6, 375.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_192|utilities/Energy provider bill/debit/USD|5|82.21, 72.57, 71.25, 75.49, 76.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_192|cloud_storage/Cloud storage plan/debit/USD|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_192|streaming/Streaming subscription/debit/USD|5|36, 36, 36, 36, 36|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_192|shopping/Monthly shopping spend/debit/USD|5|42.13, 42.46, 35.34, 38.47, 41.54|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_192|groceries/Grocery delivery/debit/USD|5|66.36, 59.22, 64.96, 52.31, 49.81|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_192|groceries/Household groceries/debit/USD|4|70.27, 69.34, 68.6, 65.62|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_192|groceries/Local market purchase/debit/USD|6|63.84, 52.27, 48.24, 49, 54.22, 71.83|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_192|groceries/Neighbourhood grocer/debit/USD|2|64.22, 51.56|repeated but not demonstrably recurrent|||
|user_192|transport/Parking and tolls/debit/USD|3|36.59, 41.07, 42.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_192|transport/Fuel refill/debit/USD|2|31.87, 33.04|repeated but not demonstrably recurrent|||
|user_192|transport/Commuter pass/debit/USD|2|29.27, 35.6|repeated but not demonstrably recurrent|||
|user_192|transport/Vehicle charging/debit/USD|2|34.7, 42.55|repeated but not demonstrably recurrent|||
|user_192|dining/Quick-service meal/debit/USD|2|45.58, 44.38|repeated but not demonstrably recurrent|||
|user_192|dining/Coffee shop/debit/USD|3|31.44, 44.17, 47.43|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_192|dining/Family dinner/debit/USD|2|34.82, 36.79|repeated but not demonstrably recurrent|||
|user_193|salary/Payroll credit/credit/EUR|5|2431, 2431, 2431, 1750.32, 1750.32|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_193|rent/Landlord standing order/debit/EUR|6|429, 429, 429, 429, 429, 429|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_193|utilities/Energy provider bill/debit/EUR|6|103.21, 96.77, 88.34, 83.44, 99.04, 92.4|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_193|music_subscription/Music service subscription/debit/EUR|5|13, 13, 13, 13, 13|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_193|delivery_membership/Grocery delivery membership/debit/EUR|5|18, 18, 18, 18, 18|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_193|gym/Community fitness plan/debit/EUR|5|36, 36, 36, 36, 36|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_193|entertainment/Monthly entertainment spend/debit/EUR|5|32.78, 29.92, 32.48, 33.65, 32.23|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_193|groceries/Bulk pantry shop/debit/EUR|2|52.99, 52.14|repeated but not demonstrably recurrent|||
|user_193|groceries/Fresh food shop/debit/EUR|5|76.06, 54.01, 62, 61.32, 46.77|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_193|groceries/Weekly produce market/debit/EUR|2|48.93, 75.28|repeated but not demonstrably recurrent|||
|user_193|groceries/Grocery delivery/debit/EUR|7|44.84, 60.1, 65.42, 72.44, 46.25, 63.88, 44.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_193|groceries/Local market purchase/debit/EUR|3|77.42, 72.89, 72.69|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_193|groceries/Supermarket basket/debit/EUR|5|61.42, 63.59, 60.63, 64.06, 71.13|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Commuter pass/debit/EUR|3|53.46, 58.42, 35.76|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Rail pass/debit/EUR|5|49.32, 50.76, 45.39, 55.64, 55.04|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Metro and bus fares/debit/EUR|3|47.95, 39.73, 48.25|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Local taxi/debit/EUR|3|47.13, 34.66, 46.75|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Parking and tolls/debit/EUR|2|45, 39.19|repeated but not demonstrably recurrent|||
|user_193|transport/Fuel refill/debit/EUR|3|45.36, 39.05, 40.19|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Ride-hailing trip/debit/EUR|4|55.94, 47.55, 54.52, 55.04|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_193|transport/Vehicle charging/debit/EUR|3|49.82, 50.06, 46.59|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_193|dining/Takeaway order/debit/EUR|3|72.09, 75.02, 83.72|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_193|dining/Lunch with colleagues/debit/EUR|2|56.5, 72.41|repeated but not demonstrably recurrent|||
|user_193|dining/Weekend food delivery/debit/EUR|4|53.8, 67.53, 51.23, 87.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_194|salary/Payroll credit/credit/INR|5|137000, 137000, 137000, 137000, 137000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_194|rent/Monthly rent/debit/INR|6|40200, 40200, 40200, 40200, 40200, 40200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_194|utilities/Municipal utilities/debit/INR|5|8575.51, 8969.59, 9212.33, 9899.38, 8158.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_194|debt_repayment/Vehicle loan payment/debit/INR|5|21200, 21200, 21200, 21200, 21200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_194|healthcare/Family healthcare expense/debit/INR|5|4221.84, 4405.16, 4320.07, 4783.08, 4873.1|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_194|family_support/Family support payment/debit/INR|5|7220, 7220, 7220, 7220, 7220|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_194|cloud_storage/Shared storage plan/debit/INR|5|1230, 1230, 1230, 1230, 1230|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_194|shopping/Clothing and household items/debit/INR|5|4294.62, 4420.91, 4825.71, 4705.33, 4575.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Local market purchase/debit/INR|3|5067.33, 6075.73, 7200.07|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Grocery delivery/debit/INR|4|5715.09, 5909, 5035.23, 5401.92|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Household groceries/debit/INR|4|5366.2, 5775.81, 7205.09, 7309.1|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Neighbourhood grocer/debit/INR|3|6945.08, 4310.38, 4832.3|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Bulk pantry shop/debit/INR|4|5086.81, 6606.13, 4647.21, 7263.79|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Fresh food shop/debit/INR|5|5446.8, 7359.4, 5617.63, 7177.14, 4850.37|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_194|groceries/Supermarket basket/debit/INR|2|6780.57, 5599.05|repeated but not demonstrably recurrent|||
|user_194|transport/Rail pass/debit/INR|3|1975.33, 2156.94, 1870.52|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_194|transport/Vehicle charging/debit/INR|2|2766.16, 1837.89|repeated but not demonstrably recurrent|||
|user_194|transport/Fuel refill/debit/INR|2|2661.33, 2851.51|repeated but not demonstrably recurrent|||
|user_194|transport/Metro and bus fares/debit/INR|2|2145.19, 2889.6|repeated but not demonstrably recurrent|||
|user_194|transport/Commuter pass/debit/INR|2|2932.83, 2601.15|repeated but not demonstrably recurrent|||
|user_195|salary/Payroll credit/credit/EUR|5|1222.65, 1222.65, 1222.65, 1222.65, 672.46|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_195|rent/Residential rent payment/debit/EUR|6|400.4, 400.4, 400.4, 400.4, 400.4, 400.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_195|utilities/Electricity bill/debit/EUR|5|60.61, 57.05, 53.85, 56.57, 54.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_195|insurance/Vehicle insurance premium/debit/EUR|5|50, 50, 50, 50, 50|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_195|cloud_storage/Cloud storage plan/debit/EUR|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_195|streaming/Streaming subscription/debit/EUR|5|24, 24, 24, 24, 24|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_195|shopping/Online retail purchases/debit/EUR|5|69.01, 65, 72.23, 66.38, 70.16|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_195|entertainment/Games and recreation/debit/EUR|5|26.17, 23.37, 23.77, 25.45, 27.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_195|groceries/Neighbourhood grocer/debit/EUR|3|61.19, 46.51, 51.86|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_195|groceries/Weekly produce market/debit/EUR|4|48.47, 45.08, 59.46, 60.44|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_195|groceries/Supermarket basket/debit/EUR|2|34.77, 40.39|repeated but not demonstrably recurrent|||
|user_195|groceries/Bulk pantry shop/debit/EUR|2|61.24, 56.17|repeated but not demonstrably recurrent|||
|user_195|groceries/Grocery delivery/debit/EUR|2|54.22, 35.23|repeated but not demonstrably recurrent|||
|user_195|groceries/Local market purchase/debit/EUR|5|37.6, 59.29, 56.65, 54.56, 50.13|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Local taxi/debit/EUR|5|28.57, 22.63, 28.53, 21.76, 31.71|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Commuter pass/debit/EUR|6|25.33, 28.43, 19.48, 30.03, 19.88, 25.45|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Parking and tolls/debit/EUR|7|25.87, 20.78, 19.51, 18.46, 29.9, 24.67, 30.49|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Rail pass/debit/EUR|5|28.26, 22.99, 29.37, 19.77, 26.04|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Vehicle charging/debit/EUR|3|21.25, 31.11, 22.1|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Metro and bus fares/debit/EUR|3|22.2, 18.22, 25.05|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Fuel refill/debit/EUR|3|24.35, 21.69, 19.4|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_195|transport/Ride-hailing trip/debit/EUR|3|18.69, 21.75, 27.36|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_195|dining/Neighbourhood restaurant/debit/EUR|4|35.49, 32.36, 29.53, 41.38|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_195|dining/Coffee shop/debit/EUR|2|38.48, 45.17|repeated but not demonstrably recurrent|||
|user_195|dining/Quick-service meal/debit/EUR|2|31.32, 44.4|repeated but not demonstrably recurrent|||
|user_195|dining/Family dinner/debit/EUR|6|39.87, 45.85, 43.56, 26.37, 38.79, 37.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_195|dining/Takeaway order/debit/EUR|4|39.48, 28.08, 38.06, 34.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_195|dining/Weekend food delivery/debit/EUR|5|44.94, 32.89, 32.63, 36.64, 31.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_195|dining/Bakery and snacks/debit/EUR|2|30.39, 36.08|repeated but not demonstrably recurrent|||
|user_196|salary/Previous employer payroll/credit/EUR|4|814, 814, 814, 814|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_196|rent/Residential rent payment/debit/EUR|6|248.6, 248.6, 248.6, 248.6, 248.6, 248.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_196|utilities/Water and power payment/debit/EUR|5|48.54, 57.87, 56.49, 52.38, 54.01|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_196|debt_repayment/Vehicle loan payment/debit/EUR|5|55, 55, 55, 55, 55|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_196|music_subscription/Audio streaming plan/debit/EUR|5|8, 8, 8, 8, 8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_196|groceries/Household groceries/debit/EUR|2|27.19, 37.58|repeated but not demonstrably recurrent|||
|user_196|groceries/Grocery delivery/debit/EUR|4|29.94, 25.93, 25.24, 35.06|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_196|groceries/Bulk pantry shop/debit/EUR|2|39.09, 37.24|repeated but not demonstrably recurrent|||
|user_196|transport/Vehicle charging/debit/EUR|2|17.93, 15.91|repeated but not demonstrably recurrent|||
|user_196|transport/Rail pass/debit/EUR|2|16.22, 12.83|repeated but not demonstrably recurrent|||
|user_196|transport/Commuter pass/debit/EUR|2|15.05, 13.71|repeated but not demonstrably recurrent|||
|user_196|dining/Neighbourhood restaurant/debit/EUR|2|31.73, 28.62|repeated but not demonstrably recurrent|||
|user_196|dining/Quick-service meal/debit/EUR|2|25.83, 38.17|repeated but not demonstrably recurrent|||
|user_196|dining/Bakery and snacks/debit/EUR|2|38.07, 41.8|repeated but not demonstrably recurrent|||
|user_196|dining/Family dinner/debit/EUR|3|33.64, 30.63, 42.09|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_197|rent/Landlord standing order/debit/IDR|6|11191000, 11191000, 11191000, 11191000, 11191000, 11191000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_197|utilities/Municipal utilities/debit/IDR|5|1738935.05, 2156129.36, 1851890.99, 1890191.34, 2121608.05|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_197|education/Professional training fee/debit/IDR|5|3131200, 3131200, 3131200, 3131200, 3131200|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_197|debt_repayment/Vehicle loan payment/debit/IDR|5|6422000, 6422000, 6422000, 6422000, 6422000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_197|music_subscription/Audio streaming plan/debit/IDR|5|262200, 262200, 262200, 262200, 262200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_197|delivery_membership/Grocery delivery membership/debit/IDR|5|314450, 314450, 314450, 314450, 314450|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_197|groceries/Supermarket basket/debit/IDR|2|1587929.58, 1891098.63|repeated but not demonstrably recurrent|||
|user_197|groceries/Fresh food shop/debit/IDR|5|1339134.94, 1352734.99, 1484732.1, 1478876.06, 2183333.58|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_197|groceries/Bulk pantry shop/debit/IDR|5|1818543.9, 1764196.6, 2254569.71, 1673446.62, 2057309.56|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_197|groceries/Grocery delivery/debit/IDR|4|1940584.72, 2014854.86, 2085231.2, 1852360.71|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_197|groceries/Local market purchase/debit/IDR|4|1672839.41, 1995328.86, 1718353.3, 1366366.03|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_197|groceries/Household groceries/debit/IDR|2|1325257.84, 1642353.8|repeated but not demonstrably recurrent|||
|user_197|groceries/Neighbourhood grocer/debit/IDR|3|1501339.41, 1961635.97, 2005368.29|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_197|transport/Rail pass/debit/IDR|3|613004.61, 981719.34, 945151.26|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_197|transport/Commuter pass/debit/IDR|5|600593.81, 937262.62, 710534.3, 973328.44, 851880.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_197|transport/Parking and tolls/debit/IDR|4|794264.25, 1001432.23, 803896.99, 568759.83|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_197|transport/Metro and bus fares/debit/IDR|2|591648.64, 618574.2|repeated but not demonstrably recurrent|||
|user_197|transport/Vehicle charging/debit/IDR|3|646808.12, 676470.73, 572211.47|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_197|transport/Ride-hailing trip/debit/IDR|5|1003339.38, 795582.87, 908886.67, 647311.84, 718694.9|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_197|transport/Local taxi/debit/IDR|2|993042.53, 993564.02|repeated but not demonstrably recurrent|||
|user_197|transport/Fuel refill/debit/IDR|2|732934.89, 769971.32|repeated but not demonstrably recurrent|||
|user_197|dining/Lunch with colleagues/debit/IDR|3|1456476.05, 1253785.72, 1421362.53|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_197|dining/Neighbourhood restaurant/debit/IDR|3|1882323.63, 1724493.92, 1317871.79|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_197|dining/Family dinner/debit/IDR|3|1121156.75, 1766894.3, 1400358.39|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_198|salary/Payroll credit/credit/INR|5|176000, 176000, 176000, 176000, 176000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_198|housing/Home association fee/debit/INR|6|17550, 17550, 17550, 17550, 17550, 17550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_198|utilities/Energy provider bill/debit/INR|5|11486.76, 12239, 12399.94, 11852.2, 10684.7|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_198|insurance/Vehicle insurance premium/debit/INR|5|7070, 7070, 7070, 7070, 7070|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_198|healthcare/Family healthcare expense/debit/INR|5|9113.39, 10096.56, 8755.62, 9550.65, 8529.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_198|streaming/Streaming subscription/debit/INR|5|4460, 4460, 4460, 4460, 4460|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_198|groceries/Bulk pantry shop/debit/INR|4|6450.67, 5649, 8237.44, 7411.98|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_198|groceries/Local market purchase/debit/INR|4|8104.41, 5907.51, 6702.39, 8220.21|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_198|groceries/Household groceries/debit/INR|3|6348.72, 6857.78, 5501.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_198|groceries/Fresh food shop/debit/INR|2|5589.69, 8034.3|repeated but not demonstrably recurrent|||
|user_198|groceries/Weekly produce market/debit/INR|2|6161.14, 7003.36|repeated but not demonstrably recurrent|||
|user_198|transport/Vehicle charging/debit/INR|3|3301.81, 3534.72, 3334.15|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_198|transport/Commuter pass/debit/INR|5|5309.31, 3356.41, 5149.37, 4249.5, 4247.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_198|transport/Parking and tolls/debit/INR|2|3206.23, 3635.8|repeated but not demonstrably recurrent|||
|user_198|transport/Local taxi/debit/INR|2|4551.74, 4248.25|repeated but not demonstrably recurrent|||
|user_198|dining/Bakery and snacks/debit/INR|2|6412.38, 4235.77|repeated but not demonstrably recurrent|||
|user_198|dining/Takeaway order/debit/INR|4|5142.7, 5597.05, 4475.41, 4302.53|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_198|dining/Family dinner/debit/INR|2|6342.78, 3844.14|repeated but not demonstrably recurrent|||
|user_198|dining/Coffee shop/debit/INR|2|4925.12, 5854.7|repeated but not demonstrably recurrent|||
|user_199|salary/Delivery platform payout/credit/IDR|6|8704221.31, 13214625.14, 12256728.4, 11398805.88, 12473475.74, 6776223.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_199|salary/Driver platform payout/credit/IDR|10|11788795.03, 10873759.02, 11349532.46, 6734099.12, 6874552.86, 7299396.24, 12809907.17, 7325461.82, 10255285.17, 8857664.58|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_199|rent/Shared housing rent/debit/IDR|5|10070000, 10070000, 10070000, 10070000, 10070000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_199|utilities/Municipal utilities/debit/IDR|5|2236640.73, 2178990.8, 1862069.39, 2240484.42, 2213714.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_199|music_subscription/Music subscription/debit/IDR|5|380950, 380950, 380950, 380950, 380950|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_199|delivery_membership/Delivery service plan/debit/IDR|5|605150, 605150, 605150, 605150, 605150|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_199|gym/Gym membership/debit/IDR|5|720100, 720100, 720100, 720100, 720100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_199|entertainment/Cinema and events/debit/IDR|5|1661245.42, 1508391.25, 1446905.85, 1364905.98, 1410663.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_199|salary/Task marketplace payout/credit/IDR|3|11876854.67, 8997763.7, 9592353.01|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_199|groceries/Local market purchase/debit/IDR|4|2053670.85, 1887145.24, 2025063.74, 2000701.06|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_199|groceries/Grocery delivery/debit/IDR|4|1729138.89, 1879931.13, 1784261.15, 1573157.7|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_199|groceries/Household groceries/debit/IDR|4|1494519.74, 1545362.81, 1205522.13, 1962277.13|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_199|groceries/Neighbourhood grocer/debit/IDR|2|1307131.11, 2022399.4|repeated but not demonstrably recurrent|||
|user_199|groceries/Bulk pantry shop/debit/IDR|2|1868081.72, 1572007.95|repeated but not demonstrably recurrent|||
|user_199|groceries/Supermarket basket/debit/IDR|2|1939832.57, 1199376.46|repeated but not demonstrably recurrent|||
|user_199|groceries/Fresh food shop/debit/IDR|3|1419322.16, 1865470.45, 1201544.03|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_199|groceries/Weekly produce market/debit/IDR|4|1561086.47, 1573956.25, 1295232.04, 1432463.13|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_199|transport/Parking and tolls/debit/IDR|4|804894.11, 671803.99, 653050.36, 818970.31|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_199|transport/Rail pass/debit/IDR|4|845873.32, 581495.05, 720207.22, 734937.49|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_199|transport/Commuter pass/debit/IDR|5|675190.1, 726971.49, 920376.7, 600320.75, 608606.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_199|transport/Ride-hailing trip/debit/IDR|4|706855.71, 847921.17, 574379.89, 634517.05|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_199|transport/Metro and bus fares/debit/IDR|3|936078.48, 675511.63, 711557.16|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_199|transport/Local taxi/debit/IDR|3|581849.45, 886374.81, 733363.26|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_199|dining/Coffee shop/debit/IDR|4|1141847.9, 1645974.77, 1029161.57, 1149380.63|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_199|dining/Quick-service meal/debit/IDR|3|945334.13, 972086.08, 1047289.31|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_199|dining/Bakery and snacks/debit/IDR|3|1004960.64, 1322950.15, 1386249.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_199|dining/Lunch with colleagues/debit/IDR|2|1522196.97, 1203335.23|repeated but not demonstrably recurrent|||
|user_200|salary/Payroll credit/credit/IDR|5|22610000, 22610000, 22610000, 22610000, 22610000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_200|housing/Building maintenance payment/debit/IDR|6|2346500, 2346500, 2346500, 2346500, 2346500, 2346500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_200|utilities/Electricity and water bill/debit/IDR|6|1210408.65, 1265623.99, 1339678.36, 1432361.49, 1257929.56, 1398221.49|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_200|insurance/Vehicle insurance premium/debit/IDR|5|982300, 982300, 982300, 982300, 982300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_200|education/Course tuition/debit/IDR|5|1791700, 1791700, 1791700, 1791700, 1791700|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_200|healthcare/Diagnostic test/debit/IDR|5|1687701.85, 1734104.66, 1690331.99, 1622655.54, 1993059.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_200|entertainment/Games and recreation/debit/IDR|5|878294.09, 834819.12, 839886.22, 817686.01, 758865.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_200|cloud_storage/Shared storage plan/debit/IDR|5|100700, 100700, 100700, 100700, 100700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_200|groceries/Supermarket basket/debit/IDR|5|945844.34, 760467.81, 931099.64, 775931.58, 798090.34|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_200|groceries/Fresh food shop/debit/IDR|3|692832.06, 1049633.09, 993994.56|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_200|groceries/Grocery delivery/debit/IDR|2|656121.16, 671255.46|repeated but not demonstrably recurrent|||
|user_200|groceries/Local market purchase/debit/IDR|2|1008046.95, 622994.1|repeated but not demonstrably recurrent|||
|user_200|groceries/Neighbourhood grocer/debit/IDR|3|930641.24, 1006461.56, 1002627.71|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_200|transport/Metro and bus fares/debit/IDR|3|422323.53, 631798.09, 644935.23|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_200|transport/Ride-hailing trip/debit/IDR|3|382845.56, 391821.74, 405199.76|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_200|transport/Commuter pass/debit/IDR|3|405506.43, 612452.45, 613991.21|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_200|transport/Fuel refill/debit/IDR|2|414963.5, 511451.93|repeated but not demonstrably recurrent|||
|user_200|dining/Coffee shop/debit/IDR|2|771740.58, 1064626.18|repeated but not demonstrably recurrent|||
|user_200|dining/Family dinner/debit/IDR|3|1039955.66, 851173.67, 1188877.35|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_200|dining/Takeaway order/debit/IDR|2|1155108.29, 1104017.89|repeated but not demonstrably recurrent|||
|user_201|salary/Peak-season wages/credit/IDR|3|17875798.85, 17041566.39, 16257294.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_201|rent/Apartment rent transfer/debit/IDR|6|6251000, 6251000, 6251000, 6251000, 6251000, 6251000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_201|utilities/Electricity and water bill/debit/IDR|5|1039278.81, 938896.83, 966401.6, 1092838.41, 1091467.32|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_201|cloud_storage/Cloud storage plan/debit/IDR|5|73150, 73150, 73150, 73150, 73150|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_201|streaming/Streaming subscription/debit/IDR|5|400900, 400900, 400900, 400900, 400900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_201|shopping/Household shopping/debit/IDR|5|800504.47, 916621.11, 807470.05, 825187.97, 849494.79|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_201|groceries/Household groceries/debit/IDR|5|624369.47, 745886.25, 862128.4, 616156.55, 619181.52|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_201|groceries/Bulk pantry shop/debit/IDR|3|783530.1, 813880.12, 636328.07|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_201|groceries/Fresh food shop/debit/IDR|3|747639.48, 633532.4, 842142.48|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_201|groceries/Local market purchase/debit/IDR|4|853645.79, 640785.32, 817954.16, 760642.14|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_201|groceries/Grocery delivery/debit/IDR|2|833637.77, 580383.49|repeated but not demonstrably recurrent|||
|user_201|transport/Vehicle charging/debit/IDR|3|432597.91, 488657.7, 438560.24|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_201|transport/Local taxi/debit/IDR|3|525601.3, 573030.83, 574028.45|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_201|dining/Quick-service meal/debit/IDR|2|595678.75, 640658.93|repeated but not demonstrably recurrent|||
|user_201|dining/Lunch with colleagues/debit/IDR|3|713501.25, 594794.91, 670438.5|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_201|dining/Takeaway order/debit/IDR|2|672086.66, 551889.8|repeated but not demonstrably recurrent|||
|user_202|salary/Payroll credit/credit/INR|5|180000, 180000, 180000, 180000, 180000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_202|rent/Residential rent payment/debit/INR|6|58300, 58300, 58300, 58300, 58300, 58300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_202|utilities/Energy provider bill/debit/INR|5|8373.83, 8824.18, 8260.48, 7898.18, 7350.98|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_202|debt_repayment/Loan repayment/debit/INR|5|17000, 17000, 17000, 17000, 17000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_202|healthcare/Family healthcare expense/debit/INR|5|7102.81, 7498.45, 7328.69, 7153.07, 6754.48|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_202|family_support/Childcare contribution/debit/INR|5|15000, 15000, 15000, 15000, 15000|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_202|cloud_storage/Online backup subscription/debit/INR|5|1300, 1300, 1300, 1300, 1300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_202|shopping/Household shopping/debit/INR|5|4017.32, 4687.26, 3755.14, 4349.46, 4061.97|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_202|groceries/Grocery delivery/debit/INR|4|7833.59, 6032.4, 8064.26, 7576.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_202|groceries/Local market purchase/debit/INR|3|9608.22, 7676.31, 9682.72|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_202|groceries/Fresh food shop/debit/INR|7|6575.01, 7241.77, 7919.26, 6182.15, 7883.34, 9526.51, 9957.36|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_202|groceries/Household groceries/debit/INR|5|7322, 8483.11, 10079.87, 8587.46, 9832.74|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_202|groceries/Bulk pantry shop/debit/INR|5|7235.91, 5725.69, 7036.82, 7526.98, 9147.87|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_202|transport/Vehicle charging/debit/INR|2|5852.26, 5680.13|repeated but not demonstrably recurrent|||
|user_202|transport/Local taxi/debit/INR|2|4989.04, 3746.87|repeated but not demonstrably recurrent|||
|user_202|transport/Fuel refill/debit/INR|2|4153.06, 4412.61|repeated but not demonstrably recurrent|||
|user_202|transport/Metro and bus fares/debit/INR|5|5939.49, 4625.47, 4501.44, 4264.94, 4406.24|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_203|salary/Task marketplace payout/credit/EUR|6|628.35, 490.56, 759.87, 802.07, 612.58, 763.61|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_203|salary/Weekly app earnings/credit/EUR|7|743.91, 825.68, 454.81, 606.81, 583.18, 693.93, 680.02|variable but recurrent|17|RECURRING_AMOUNT_UNRESOLVED|
|user_203|salary/Driver platform payout/credit/EUR|4|498.91, 722.07, 517.12, 730|variable but recurrent|17|RECURRING_AMOUNT_UNRESOLVED|
|user_203|salary/Delivery platform payout/credit/EUR|4|786.79, 565.92, 473.19, 580.63|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_203|rent/Shared housing rent/debit/EUR|6|800.8, 800.8, 800.8, 800.8, 800.8, 800.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_203|utilities/Water and power payment/debit/EUR|5|135.6, 142.51, 145.16, 158.29, 150.33|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_203|music_subscription/Audio streaming plan/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_203|delivery_membership/Delivery service plan/debit/EUR|5|30, 30, 30, 30, 30|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_203|gym/Fitness club membership/debit/EUR|5|61, 61, 61, 61, 61|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_203|entertainment/Weekend entertainment/debit/EUR|5|62.6, 70.64, 70.99, 63.48, 68.35|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_203|groceries/Neighbourhood grocer/debit/EUR|5|144.36, 129.55, 88.03, 137.54, 143.39|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_203|groceries/Local market purchase/debit/EUR|3|139.67, 99.82, 92.92|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_203|groceries/Fresh food shop/debit/EUR|5|129.09, 102.59, 132.83, 125.16, 92.25|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_203|groceries/Household groceries/debit/EUR|4|96.13, 126.22, 102.56, 95.32|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_203|groceries/Bulk pantry shop/debit/EUR|4|91.2, 114.43, 94.78, 107.5|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_203|groceries/Weekly produce market/debit/EUR|2|93.83, 86.28|repeated but not demonstrably recurrent|||
|user_203|transport/Commuter pass/debit/EUR|4|52.08, 60.56, 56.31, 67.74|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_203|transport/Metro and bus fares/debit/EUR|4|58.52, 41.92, 62.4, 43.23|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_203|transport/Local taxi/debit/EUR|4|58.55, 65.2, 41.05, 60.94|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_203|transport/Vehicle charging/debit/EUR|2|48.45, 54.64|repeated but not demonstrably recurrent|||
|user_203|transport/Rail pass/debit/EUR|5|64.26, 40.98, 53.37, 45.34, 48.57|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_203|transport/Fuel refill/debit/EUR|2|60.11, 42.88|repeated but not demonstrably recurrent|||
|user_203|transport/Ride-hailing trip/debit/EUR|3|41.92, 66.87, 41.32|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_203|dining/Takeaway order/debit/EUR|3|60.5, 55.98, 54.96|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_203|dining/Weekend food delivery/debit/EUR|3|62.73, 79.38, 69.98|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_203|dining/Bakery and snacks/debit/EUR|3|57.83, 68.69, 71.22|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_203|dining/Quick-service meal/debit/EUR|2|63.73, 58.76|repeated but not demonstrably recurrent|||
|user_204|rent/Residential rent payment/debit/EUR|6|628.1, 628.1, 628.1, 628.1, 628.1, 628.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_204|utilities/Electricity bill/debit/EUR|5|123.34, 138.24, 130.09, 123.01, 121.93|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_204|education/Child education fee/debit/EUR|5|213, 213, 213, 213, 213|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_204|debt_repayment/Credit card repayment/debit/EUR|5|102, 102, 102, 102, 102|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_204|music_subscription/Audio streaming plan/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_204|delivery_membership/Delivery service plan/debit/EUR|5|25, 25, 25, 25, 25|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_204|salary/First-job payroll/credit/EUR|2|2024, 2024|repeated but not demonstrably recurrent|||
|user_204|groceries/Neighbourhood grocer/debit/EUR|3|91, 93.64, 59.95|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_204|groceries/Weekly produce market/debit/EUR|3|93.5, 92.9, 88.51|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_204|groceries/Household groceries/debit/EUR|6|97.2, 100.39, 63.57, 72.43, 66.14, 67.73|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_204|groceries/Grocery delivery/debit/EUR|3|93.46, 76.09, 97.6|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_204|groceries/Local market purchase/debit/EUR|2|89.94, 62.4|repeated but not demonstrably recurrent|||
|user_204|groceries/Bulk pantry shop/debit/EUR|3|88.52, 80.73, 66.93|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_204|groceries/Supermarket basket/debit/EUR|5|61.09, 96.47, 83.33, 93.8, 76.32|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_204|transport/Parking and tolls/debit/EUR|4|50.84, 34.7, 33.67, 42.25|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_204|transport/Ride-hailing trip/debit/EUR|3|51.94, 45.19, 57.34|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_204|transport/Commuter pass/debit/EUR|5|52.1, 48.49, 51.4, 37.15, 35.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_204|transport/Fuel refill/debit/EUR|7|49.76, 47.85, 54.59, 50.29, 52.46, 54.53, 48.97|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_204|transport/Vehicle charging/debit/EUR|3|47.4, 57.76, 49.08|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_204|transport/Local taxi/debit/EUR|2|42.07, 53.17|repeated but not demonstrably recurrent|||
|user_204|dining/Quick-service meal/debit/EUR|2|64.61, 58.12|repeated but not demonstrably recurrent|||
|user_204|dining/Coffee shop/debit/EUR|4|54.09, 72.56, 51.83, 79.96|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_204|dining/Weekend food delivery/debit/EUR|3|84.44, 52.95, 68.12|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_204|dining/Neighbourhood restaurant/debit/EUR|3|66.87, 69.82, 56.83|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_205|salary/Payroll credit/credit/IDR|5|18240000, 18240000, 18240000, 18240000, 18240000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_205|rent/Apartment rent transfer/debit/IDR|6|5871000, 5871000, 5871000, 5871000, 5871000, 5871000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_205|utilities/Energy provider bill/debit/IDR|5|904186.9, 993830.6, 985882.81, 933863.63, 900242.29|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_205|debt_repayment/Vehicle loan payment/debit/IDR|5|1292000, 1292000, 1292000, 1292000, 1292000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_205|streaming/Video streaming plan/debit/IDR|5|435100, 435100, 435100, 435100, 435100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_205|cloud_storage/Shared storage plan/debit/IDR|5|141550, 141550, 141550, 141550, 141550|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_205|shopping/Household shopping/debit/IDR|5|555143.33, 612972.29, 639835.88, 634125.99, 560751.23|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_205|groceries/Grocery delivery/debit/IDR|4|820739.36, 946414.13, 889559.93, 735348.43|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_205|groceries/Supermarket basket/debit/IDR|2|1030670.92, 975762.63|repeated but not demonstrably recurrent|||
|user_205|groceries/Weekly produce market/debit/IDR|2|747972.86, 614746.69|repeated but not demonstrably recurrent|||
|user_205|groceries/Fresh food shop/debit/IDR|3|725467.97, 1051503.96, 681814.11|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_205|groceries/Bulk pantry shop/debit/IDR|5|650861.42, 888629.95, 687782.94, 1060818.64, 927563.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_205|groceries/Household groceries/debit/IDR|4|653839.68, 844654.44, 949682.36, 769206.97|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_205|groceries/Neighbourhood grocer/debit/IDR|4|895675.05, 647714.55, 700298.46, 833791.61|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_205|groceries/Local market purchase/debit/IDR|2|640036.35, 959002.77|repeated but not demonstrably recurrent|||
|user_205|transport/Fuel refill/debit/IDR|6|539010.1, 496432.86, 321245.85, 362068.9, 465465.03, 413583.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_205|transport/Metro and bus fares/debit/IDR|3|533671.47, 526461.03, 399324.4|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_205|transport/Rail pass/debit/IDR|3|457944.04, 406042.25, 459566.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_205|transport/Commuter pass/debit/IDR|2|378655.47, 539794.48|repeated but not demonstrably recurrent|||
|user_205|transport/Ride-hailing trip/debit/IDR|5|407902.1, 465691.17, 510350.12, 380754.97, 450073.19|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_205|transport/Vehicle charging/debit/IDR|3|518687.28, 386858.33, 332676.44|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_205|transport/Local taxi/debit/IDR|3|492710.3, 329521.75, 399149.01|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_205|dining/Takeaway order/debit/IDR|2|794714.92, 761331.77|repeated but not demonstrably recurrent|||
|user_205|dining/Quick-service meal/debit/IDR|2|730162.01, 500363.82|repeated but not demonstrably recurrent|||
|user_205|dining/Family dinner/debit/IDR|3|748610.47, 594895.89, 671267.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_205|dining/Neighbourhood restaurant/debit/IDR|3|690353.87, 568536.31, 612376.78|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_206|salary/Freelance milestone payment/credit/EUR|3|862.6, 436.62, 556.85|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_206|salary/Independent work payment/credit/EUR|2|717.4, 508.42|repeated but not demonstrably recurrent|||
|user_206|rent/Apartment rent transfer/debit/EUR|5|452.1, 452.1, 452.1, 452.1, 452.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_206|utilities/Water and power payment/debit/EUR|5|94.47, 102.86, 86.71, 101.75, 92.53|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_206|cloud_storage/Cloud storage plan/debit/EUR|5|5, 5, 5, 5, 5|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_206|streaming/Video streaming plan/debit/EUR|5|39, 39, 39, 39, 39|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_206|shopping/Online retail purchases/debit/EUR|5|61.94, 64.38, 54.4, 64.74, 54.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_206|groceries/Weekly produce market/debit/EUR|2|48.15, 49.46|repeated but not demonstrably recurrent|||
|user_206|groceries/Local market purchase/debit/EUR|5|56.83, 41.36, 44.86, 40.09, 53.95|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_206|groceries/Grocery delivery/debit/EUR|5|42.01, 67.68, 52.66, 63.79, 43.03|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_206|groceries/Bulk pantry shop/debit/EUR|5|59.24, 43.65, 46.12, 53.1, 65.99|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_206|transport/Fuel refill/debit/EUR|2|38.43, 30.57|repeated but not demonstrably recurrent|||
|user_206|transport/Rail pass/debit/EUR|2|32.81, 37.16|repeated but not demonstrably recurrent|||
|user_206|dining/Lunch with colleagues/debit/EUR|4|47.83, 46.87, 56.33, 37.12|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_206|dining/Neighbourhood restaurant/debit/EUR|2|36.61, 58.49|repeated but not demonstrably recurrent|||
|user_207|salary/Payroll credit/credit/ZAR|5|21120, 21120, 21120, 21120, 21120|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_207|housing/Property maintenance contribution/debit/ZAR|5|2453, 2453, 2453, 2453, 2453|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_207|utilities/Water and power payment/debit/ZAR|5|978.78, 1031.34, 983.2, 1084.71, 1116.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_207|insurance/Health insurance premium/debit/ZAR|5|897.6, 897.6, 897.6, 897.6, 897.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_207|healthcare/Regular medicine purchase/debit/ZAR|5|1260.61, 1184.3, 1403.4, 1149.93, 1403.86|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_207|streaming/Video streaming plan/debit/ZAR|5|521.4, 521.4, 521.4, 521.4, 521.4|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_207|groceries/Grocery delivery/debit/ZAR|3|1044.9, 729.79, 1026.11|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_207|groceries/Neighbourhood grocer/debit/ZAR|3|1078.92, 824.74, 817.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_207|groceries/Local market purchase/debit/ZAR|2|919.67, 990.59|repeated but not demonstrably recurrent|||
|user_207|groceries/Fresh food shop/debit/ZAR|4|1149.71, 1063.37, 703.16, 974.68|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_207|groceries/Supermarket basket/debit/ZAR|3|872.96, 1204.08, 745.52|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_207|groceries/Household groceries/debit/ZAR|2|1207, 869.68|repeated but not demonstrably recurrent|||
|user_207|transport/Ride-hailing trip/debit/ZAR|2|607.43, 461.17|repeated but not demonstrably recurrent|||
|user_207|transport/Commuter pass/debit/ZAR|2|648.53, 512.72|repeated but not demonstrably recurrent|||
|user_207|transport/Local taxi/debit/ZAR|2|586.84, 604.84|repeated but not demonstrably recurrent|||
|user_207|transport/Vehicle charging/debit/ZAR|2|591.08, 674.82|repeated but not demonstrably recurrent|||
|user_207|transport/Rail pass/debit/ZAR|2|516.13, 621.95|repeated but not demonstrably recurrent|||
|user_207|dining/Quick-service meal/debit/ZAR|5|990.06, 960.26, 601.87, 876.43, 672.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_207|dining/Family dinner/debit/ZAR|3|1034.5, 675.94, 651.44|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_207|dining/Lunch with colleagues/debit/ZAR|2|985.74, 935.17|repeated but not demonstrably recurrent|||
|user_207|dining/Neighbourhood restaurant/debit/ZAR|2|1004.89, 963.07|repeated but not demonstrably recurrent|||
|user_208|salary/Payroll credit/credit/IDR|5|13870000, 13870000, 13870000, 13870000, 13870000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_208|rent/Monthly rent/debit/IDR|6|3097000, 3097000, 3097000, 3097000, 3097000, 3097000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_208|utilities/Household utility payment/debit/IDR|6|948667.13, 874408.25, 942966.96, 782127.92, 851760.83, 882056.02|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_208|debt_repayment/Personal loan payment/debit/IDR|5|883500, 883500, 883500, 883500, 883500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_208|streaming/Family streaming plan/debit/IDR|5|355300, 355300, 355300, 355300, 355300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_208|cloud_storage/Cloud storage plan/debit/IDR|5|70300, 70300, 70300, 70300, 70300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_208|shopping/Monthly shopping spend/debit/IDR|5|591380.76, 581735.89, 643735.6, 680553.59, 665651.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_208|groceries/Household groceries/debit/IDR|4|583984.57, 730945.12, 679373.99, 542305.38|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_208|groceries/Bulk pantry shop/debit/IDR|2|642457.58, 769632.92|repeated but not demonstrably recurrent|||
|user_208|groceries/Neighbourhood grocer/debit/IDR|6|599228.17, 691589.52, 587841.5, 768217.43, 738749.86, 514230.3|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_208|groceries/Fresh food shop/debit/IDR|5|630004.38, 661073.09, 786373.79, 633924.84, 593212.34|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_208|groceries/Supermarket basket/debit/IDR|2|623194.53, 456204.58|repeated but not demonstrably recurrent|||
|user_208|groceries/Local market purchase/debit/IDR|3|629191.53, 729316.51, 452155.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_208|groceries/Grocery delivery/debit/IDR|3|648832.61, 671017.56, 548523.48|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_208|transport/Rail pass/debit/IDR|4|287283.63, 279377.3, 273375.57, 336791.18|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_208|transport/Commuter pass/debit/IDR|7|282838.67, 225168.88, 324929.91, 237459.12, 271120.62, 284929.66, 253837.45|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_208|transport/Ride-hailing trip/debit/IDR|2|303865.81, 322714.11|repeated but not demonstrably recurrent|||
|user_208|transport/Metro and bus fares/debit/IDR|2|339753.28, 281548.74|repeated but not demonstrably recurrent|||
|user_208|transport/Fuel refill/debit/IDR|5|322732.68, 212911.36, 242885.25, 264020.77, 222128.47|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_208|transport/Parking and tolls/debit/IDR|2|209065.27, 278591.77|repeated but not demonstrably recurrent|||
|user_208|transport/Local taxi/debit/IDR|2|215392.24, 260399.51|repeated but not demonstrably recurrent|||
|user_208|transport/Vehicle charging/debit/IDR|2|270006.72, 269003.09|repeated but not demonstrably recurrent|||
|user_208|dining/Lunch with colleagues/debit/IDR|2|674826.52, 665239.87|repeated but not demonstrably recurrent|||
|user_208|dining/Coffee shop/debit/IDR|3|636492.08, 574972.13, 425145.42|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_208|dining/Quick-service meal/debit/IDR|3|579138.37, 510160.96, 427390.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_208|dining/Neighbourhood restaurant/debit/IDR|2|410842.12, 561642.37|repeated but not demonstrably recurrent|||
|user_209|salary/Payroll credit/credit/ZAR|5|21120, 21120, 21120, 21120, 21120|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_209|housing/Property maintenance contribution/debit/ZAR|6|2409, 2409, 2409, 2409, 2409, 2409|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_209|utilities/Electricity bill/debit/ZAR|5|1174.7, 1297.09, 1276.19, 1388.06, 1242.22|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_209|insurance/Household insurance/debit/ZAR|5|1018.6, 1018.6, 1018.6, 1018.6, 1018.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_209|education/Child education fee/debit/ZAR|5|1467.4, 1467.4, 1467.4, 1467.4, 1467.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_209|healthcare/Family healthcare expense/debit/ZAR|5|1240.18, 1080.04, 1303.38, 1103.65, 1285.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_209|entertainment/Games and recreation/debit/ZAR|5|514.97, 447.16, 426.6, 482.47, 498.67|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_209|cloud_storage/Online backup subscription/debit/ZAR|5|78.1, 78.1, 78.1, 78.1, 78.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_209|groceries/Weekly produce market/debit/ZAR|2|1069.22, 683.86|repeated but not demonstrably recurrent|||
|user_209|groceries/Neighbourhood grocer/debit/ZAR|4|756.71, 997.02, 816.47, 977.37|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_209|groceries/Bulk pantry shop/debit/ZAR|2|1051.42, 919.33|repeated but not demonstrably recurrent|||
|user_209|groceries/Supermarket basket/debit/ZAR|2|887.17, 914.89|repeated but not demonstrably recurrent|||
|user_209|groceries/Grocery delivery/debit/ZAR|3|1040.18, 908.39, 626.19|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_209|groceries/Fresh food shop/debit/ZAR|5|1077.73, 1093.41, 1020.14, 888.91, 684.19|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_209|transport/Commuter pass/debit/ZAR|3|495.56, 605.7, 634.74|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_209|transport/Fuel refill/debit/ZAR|2|574.05, 440.21|repeated but not demonstrably recurrent|||
|user_209|transport/Vehicle charging/debit/ZAR|3|424.32, 666.36, 647.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_209|transport/Rail pass/debit/ZAR|2|423.83, 541.6|repeated but not demonstrably recurrent|||
|user_209|dining/Weekend food delivery/debit/ZAR|2|699.18, 816.71|repeated but not demonstrably recurrent|||
|user_209|dining/Quick-service meal/debit/ZAR|4|688.75, 793.98, 570.82, 587.73|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_210|salary/Payroll credit/credit/USD|5|2916, 2916, 2916, 2916, 2916|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_210|rent/Shared housing rent/debit/USD|6|673.2, 673.2, 673.2, 673.2, 673.2, 673.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_210|utilities/Electricity and water bill/debit/USD|5|154.69, 168.6, 161.72, 145.67, 159.38|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_210|cloud_storage/Online backup subscription/debit/USD|5|18, 18, 18, 18, 18|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_210|streaming/Video streaming plan/debit/USD|5|87, 87, 87, 87, 87|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_210|shopping/Monthly shopping spend/debit/USD|5|174.56, 173.29, 154.43, 149.83, 160.26|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_210|groceries/Local market purchase/debit/USD|3|95.35, 162.54, 149.73|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_210|groceries/Weekly produce market/debit/USD|7|106.43, 118.35, 134.78, 153.13, 115.24, 107.6, 104.43|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_210|groceries/Neighbourhood grocer/debit/USD|2|103.33, 110.76|repeated but not demonstrably recurrent|||
|user_210|groceries/Grocery delivery/debit/USD|2|131.38, 129.67|repeated but not demonstrably recurrent|||
|user_210|groceries/Fresh food shop/debit/USD|2|161.78, 101.57|repeated but not demonstrably recurrent|||
|user_210|transport/Commuter pass/debit/USD|3|88.1, 75.03, 76.35|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_210|transport/Vehicle charging/debit/USD|2|65.51, 80.59|repeated but not demonstrably recurrent|||
|user_210|dining/Quick-service meal/debit/USD|2|135.72, 139.35|repeated but not demonstrably recurrent|||
|user_210|dining/Lunch with colleagues/debit/USD|2|113.36, 118.08|repeated but not demonstrably recurrent|||
|user_210|dining/Bakery and snacks/debit/USD|2|91.08, 128.93|repeated but not demonstrably recurrent|||
|user_211|salary/Payroll credit/credit/EUR|5|2618, 2618, 2618, 1884.96, 1884.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_211|rent/Apartment rent transfer/debit/EUR|5|460.9, 460.9, 460.9, 460.9, 460.9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_211|utilities/Electricity and water bill/debit/EUR|5|114.66, 129.94, 108.46, 134.29, 106.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_211|music_subscription/Music service subscription/debit/EUR|5|12, 12, 12, 12, 12|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_211|delivery_membership/Grocery delivery membership/debit/EUR|5|17, 17, 17, 17, 17|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_211|gym/Gym membership/debit/EUR|5|57, 57, 57, 57, 57|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_211|entertainment/Local event tickets/debit/EUR|5|50.89, 55.28, 48.68, 56.9, 56.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_211|groceries/Bulk pantry shop/debit/EUR|4|88.66, 59.81, 76.08, 75.42|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_211|groceries/Local market purchase/debit/EUR|3|75.69, 88.64, 71.54|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_211|groceries/Grocery delivery/debit/EUR|7|92.06, 101.87, 92.29, 67.82, 67.71, 74.78, 65.35|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_211|groceries/Neighbourhood grocer/debit/EUR|4|86.95, 91.43, 70.05, 100.06|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_211|groceries/Fresh food shop/debit/EUR|4|83.34, 89.26, 69.08, 72.98|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_211|groceries/Household groceries/debit/EUR|2|74.26, 97.75|repeated but not demonstrably recurrent|||
|user_211|transport/Commuter pass/debit/EUR|3|34.49, 49.28, 38.03|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_211|transport/Vehicle charging/debit/EUR|3|41.95, 47.6, 48.2|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_211|transport/Metro and bus fares/debit/EUR|4|44.98, 50.05, 52.29, 57.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_211|transport/Rail pass/debit/EUR|7|49.22, 40.78, 47.24, 39.68, 37.59, 47.27, 46.29|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_211|transport/Parking and tolls/debit/EUR|4|58.03, 42.1, 48.79, 38.26|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_211|transport/Ride-hailing trip/debit/EUR|2|44.77, 42.07|repeated but not demonstrably recurrent|||
|user_211|transport/Local taxi/debit/EUR|2|45.97, 56.12|repeated but not demonstrably recurrent|||
|user_211|dining/Quick-service meal/debit/EUR|2|89.98, 67.54|repeated but not demonstrably recurrent|||
|user_211|dining/Family dinner/debit/EUR|4|71.55, 80.32, 82.11, 75.72|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_211|dining/Coffee shop/debit/EUR|2|76.99, 55.13|repeated but not demonstrably recurrent|||
|user_211|dining/Takeaway order/debit/EUR|2|69.58, 70.84|repeated but not demonstrably recurrent|||
|user_212|salary/Payroll credit/credit/IDR|5|33440000, 33440000, 33440000, 33440000, 33440000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_212|rent/Apartment rent transfer/debit/IDR|6|7600000, 7600000, 7600000, 7600000, 7600000, 7600000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_212|utilities/Water and power payment/debit/IDR|5|2017035.98, 2407985.7, 2535417.01, 2284809.09, 2279277.87|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_212|debt_repayment/Vehicle loan payment/debit/IDR|5|4740500, 4740500, 4740500, 4740500, 4740500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_212|healthcare/Regular medicine purchase/debit/IDR|5|2477091.03, 2415001.8, 2167007.53, 2378913.4, 2480255.06|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_212|family_support/Dependent care payment/debit/IDR|5|3363000, 3363000, 3363000, 3363000, 3363000|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_212|cloud_storage/Online backup subscription/debit/IDR|5|133000, 133000, 133000, 133000, 133000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_212|shopping/Personal shopping/debit/IDR|5|1522637.52, 1642776.2, 1679726.08, 1404824.98, 1591451.15|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_212|groceries/Fresh food shop/debit/IDR|4|1171677.6, 1259198.16, 1225363.25, 1787409.06|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_212|groceries/Supermarket basket/debit/IDR|6|1241214.81, 1776775.83, 1290563.41, 1252823.32, 1418399.12, 1231250.58|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_212|groceries/Neighbourhood grocer/debit/IDR|3|1882986.9, 1643735.98, 1193656.16|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_212|groceries/Weekly produce market/debit/IDR|4|1705161.08, 1304091.04, 1907596.59, 1319157.73|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_212|groceries/Bulk pantry shop/debit/IDR|2|1387096.96, 1281288.6|repeated but not demonstrably recurrent|||
|user_212|groceries/Grocery delivery/debit/IDR|3|1382150.61, 1544937.85, 1619206.17|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_212|groceries/Local market purchase/debit/IDR|3|1458915.06, 1155468.15, 1825846.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_212|transport/Ride-hailing trip/debit/IDR|4|919275.51, 836604.04, 804206.66, 706068.67|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_212|transport/Rail pass/debit/IDR|4|832371.19, 1003245, 871652.06, 754680.04|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_212|transport/Fuel refill/debit/IDR|3|724283.06, 757673.93, 893547.15|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_213|salary/Seasonal contract payment/credit/USD|2|2445.14, 2394.14|repeated but not demonstrably recurrent|||
|user_213|rent/Residential rent payment/debit/USD|6|842.4, 842.4, 842.4, 842.4, 842.4, 842.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_213|utilities/Electricity and water bill/debit/USD|6|119.62, 118.5, 132.89, 136.5, 120.11, 138.16|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_213|insurance/Vehicle insurance premium/debit/USD|5|121, 121, 121, 121, 121|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_213|cloud_storage/Cloud storage plan/debit/USD|5|22, 22, 22, 22, 22|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_213|streaming/Streaming subscription/debit/USD|5|52, 52, 52, 52, 52|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_213|shopping/Household shopping/debit/USD|5|88.14, 88.94, 83.98, 82.16, 97.32|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_213|entertainment/Local event tickets/debit/USD|5|60.56, 63.95, 73.49, 68.85, 71|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_213|groceries/Supermarket basket/debit/USD|3|141.62, 145.35, 140.6|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_213|groceries/Weekly produce market/debit/USD|4|108.05, 150.18, 121.52, 140.79|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_213|groceries/Fresh food shop/debit/USD|3|142.55, 118.42, 148.93|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_213|groceries/Neighbourhood grocer/debit/USD|5|127.49, 151.65, 150.47, 98.91, 121.41|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Metro and bus fares/debit/USD|6|67.57, 60.58, 85.38, 82.58, 63.88, 72.48|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Fuel refill/debit/USD|3|78.54, 54.27, 77.55|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Vehicle charging/debit/USD|5|68.07, 51.69, 81.44, 72.19, 63.55|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Local taxi/debit/USD|8|58.33, 57.42, 58.88, 52.96, 85.02, 76.83, 62.16, 74.67|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Ride-hailing trip/debit/USD|6|81.36, 77.28, 48.51, 75.74, 77.61, 69.15|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Rail pass/debit/USD|3|79.96, 51.55, 72.81|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_213|transport/Parking and tolls/debit/USD|2|84.78, 73.76|repeated but not demonstrably recurrent|||
|user_213|transport/Commuter pass/debit/USD|3|66.69, 61.8, 81.03|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Bakery and snacks/debit/USD|5|61.09, 98.76, 68.33, 75.48, 84.12|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Takeaway order/debit/USD|3|105.89, 100.42, 94.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Lunch with colleagues/debit/USD|3|85.39, 80.87, 92.11|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Quick-service meal/debit/USD|4|91.31, 95, 62.62, 88.1|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Neighbourhood restaurant/debit/USD|4|94.45, 68.88, 90.59, 87.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Family dinner/debit/USD|3|89.89, 62.82, 60.1|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_213|dining/Weekend food delivery/debit/USD|3|77.26, 83.4, 76.73|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_214|salary/Payroll credit/credit/USD|5|241990.32, 241990.32, 241990.32, 241990.32, 241990.32|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_214|rent/Apartment rent transfer/debit/INR|6|69100, 69100, 69100, 69100, 69100, 69100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_214|utilities/Electricity and water bill/debit/INR|5|10803.07, 12713.22, 10941, 12335.19, 12669.86|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_214|insurance/Vehicle insurance premium/debit/INR|5|6510, 6510, 6510, 6510, 6510|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_214|cloud_storage/Online backup subscription/debit/INR|5|930, 930, 930, 930, 930|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_214|streaming/Streaming subscription/debit/INR|5|5670, 5670, 5670, 5670, 5670|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_214|shopping/Online retail purchases/debit/INR|5|10330.82, 10538.66, 11054.39, 9652.11, 11622.98|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_214|entertainment/Cinema and events/debit/INR|5|7594.25, 6306.91, 6918.91, 7621.44, 6398.15|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_214|groceries/Neighbourhood grocer/debit/INR|3|8191.45, 11011.5, 11884.24|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_214|groceries/Weekly produce market/debit/INR|4|8494.22, 11054.53, 10935.53, 8352.59|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_214|groceries/Bulk pantry shop/debit/INR|4|9821.37, 11800.05, 8214.74, 11032.44|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_214|groceries/Household groceries/debit/INR|2|8575.26, 6924.57|repeated but not demonstrably recurrent|||
|user_214|groceries/Local market purchase/debit/INR|2|7686.3, 7046.43|repeated but not demonstrably recurrent|||
|user_214|transport/Local taxi/debit/INR|3|4254.46, 4397.11, 6184.83|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Rail pass/debit/INR|9|3830.3, 5095.62, 4313.8, 5941.54, 5261.84, 3936.94, 6434.37, 3635.66, 5273.26|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Metro and bus fares/debit/INR|6|5274.35, 5606.84, 5846.22, 4840.3, 4125.83, 3647.78|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Parking and tolls/debit/INR|3|3866.16, 5147.2, 4545.68|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Fuel refill/debit/INR|5|6135.6, 6246.64, 5829.27, 5018.41, 3659.43|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Commuter pass/debit/INR|3|5000.45, 5513.05, 6373.92|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Ride-hailing trip/debit/INR|3|4520.11, 6146.37, 4216.28|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_214|transport/Vehicle charging/debit/INR|3|3960.31, 4240.12, 4803.89|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_214|dining/Quick-service meal/debit/INR|3|9570.97, 8077.29, 7098.37|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_214|dining/Weekend food delivery/debit/INR|2|9719.56, 6942.87|repeated but not demonstrably recurrent|||
|user_214|dining/Neighbourhood restaurant/debit/INR|3|7938.57, 10145.3, 7893.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_214|dining/Bakery and snacks/debit/INR|5|7941.37, 6801.07, 6629.64, 8416.33, 8876.03|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_214|dining/Coffee shop/debit/INR|4|7942.23, 6485.75, 8714.53, 10127.98|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_214|dining/Takeaway order/debit/INR|3|9187.37, 6499.64, 8418.67|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_214|dining/Lunch with colleagues/debit/INR|2|10024.12, 6688.92|repeated but not demonstrably recurrent|||
|user_214|dining/Family dinner/debit/INR|3|11082.79, 7842.38, 6524.42|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_215|salary/Driver platform payout/credit/ZAR|10|6998.77, 6850.55, 6701.86, 7005.19, 4949.51, 4420.57, 4904.96, 7487.67, 6583.22, 5351.57|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_215|salary/Delivery platform payout/credit/ZAR|3|3917.87, 4557.01, 5040.15|variable but recurrent|38|RECURRING_AMOUNT_UNRESOLVED|
|user_215|rent/Monthly rent/debit/ZAR|6|6270, 6270, 6270, 6270, 6270, 6270|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_215|utilities/Household utility payment/debit/ZAR|5|1496.71, 1506.45, 1574.85, 1400.02, 1616.39|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_215|music_subscription/Music service subscription/debit/ZAR|5|170.5, 170.5, 170.5, 170.5, 170.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_215|delivery_membership/Delivery service plan/debit/ZAR|5|387.2, 387.2, 387.2, 387.2, 387.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_215|gym/Community fitness plan/debit/ZAR|5|543.4, 543.4, 543.4, 543.4, 543.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_215|entertainment/Monthly entertainment spend/debit/ZAR|5|740.11, 822.23, 769.53, 732.14, 740.76|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_215|salary/Task marketplace payout/credit/ZAR|5|7920.56, 5490.82, 7915.72, 5376.45, 4006.75|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_215|salary/Weekly app earnings/credit/ZAR|3|4628.34, 4062.93, 7740.39|variable but recurrent|17|RECURRING_AMOUNT_UNRESOLVED|
|user_215|groceries/Local market purchase/debit/ZAR|6|658.63, 866.28, 630.89, 902.23, 992.57, 849.49|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_215|groceries/Grocery delivery/debit/ZAR|4|631.13, 734.56, 937.87, 686.63|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_215|groceries/Weekly produce market/debit/ZAR|3|1037.9, 629.74, 674.81|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_215|groceries/Bulk pantry shop/debit/ZAR|4|661.3, 973.98, 643.63, 949.33|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_215|groceries/Fresh food shop/debit/ZAR|3|1086.44, 1081.65, 688.76|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_215|groceries/Household groceries/debit/ZAR|3|672.34, 726.96, 624.91|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_215|transport/Commuter pass/debit/ZAR|5|478.18, 488.45, 582.38, 435.44, 400.29|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_215|transport/Fuel refill/debit/ZAR|7|506.33, 545.16, 385.59, 567.73, 365.18, 431.67, 520.36|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_215|transport/Local taxi/debit/ZAR|2|569.19, 463.35|repeated but not demonstrably recurrent|||
|user_215|transport/Vehicle charging/debit/ZAR|5|465.14, 608.98, 428.24, 597.98, 465.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_215|transport/Parking and tolls/debit/ZAR|4|453.36, 557.61, 477.21, 573.22|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_215|dining/Bakery and snacks/debit/ZAR|4|948.42, 829.77, 711.92, 1004.21|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_215|dining/Neighbourhood restaurant/debit/ZAR|3|895.92, 913.02, 642.35|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_215|dining/Family dinner/debit/ZAR|2|747.57, 683.96|repeated but not demonstrably recurrent|||
|user_216|salary/Payroll credit/credit/USD|5|1890.72, 1890.72, 1890.72, 1890.72, 1890.72|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_216|housing/Home repair reserve/debit/USD|6|194, 194, 194, 194, 194, 194|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_216|utilities/Water and power payment/debit/USD|5|182.83, 159.21, 149.64, 176.34, 171.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_216|insurance/Health insurance premium/debit/USD|5|119, 119, 119, 119, 119|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_216|healthcare/Regular medicine purchase/debit/USD|5|102.43, 105.83, 100.93, 93.95, 112.68|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_216|streaming/Video streaming plan/debit/USD|5|53, 53, 53, 53, 53|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_216|groceries/Bulk pantry shop/debit/USD|5|89.45, 89.21, 74.04, 92.44, 78.36|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_216|groceries/Local market purchase/debit/USD|3|84.67, 102.53, 78.54|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_216|groceries/Fresh food shop/debit/USD|2|86.5, 110.77|repeated but not demonstrably recurrent|||
|user_216|groceries/Grocery delivery/debit/USD|2|97.22, 97.2|repeated but not demonstrably recurrent|||
|user_216|groceries/Household groceries/debit/USD|3|99.95, 87.06, 95.42|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_216|transport/Fuel refill/debit/USD|4|67.01, 46.13, 61.02, 55.26|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_216|transport/Parking and tolls/debit/USD|2|41.8, 56.33|repeated but not demonstrably recurrent|||
|user_216|transport/Rail pass/debit/USD|2|52.4, 60.01|repeated but not demonstrably recurrent|||
|user_216|transport/Local taxi/debit/USD|3|67.34, 63.84, 46.88|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_216|dining/Weekend food delivery/debit/USD|2|106.18, 105.4|repeated but not demonstrably recurrent|||
|user_216|dining/Quick-service meal/debit/USD|3|106.86, 80.84, 111.67|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_216|dining/Takeaway order/debit/USD|2|63.78, 93.96|repeated but not demonstrably recurrent|||
|user_216|dining/Neighbourhood restaurant/debit/USD|3|92.74, 84.33, 112.58|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_217|salary/Payroll credit/credit/ZAR|5|35420, 35420, 35420, 35420, 35420|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_217|rent/Landlord standing order/debit/ZAR|6|10472, 10472, 10472, 10472, 10472, 10472|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_217|utilities/Household utility payment/debit/ZAR|5|2450.45, 2432.34, 2215.44, 2256.28, 2631.22|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_217|debt_repayment/Education loan instalment/debit/ZAR|5|3619, 3619, 3619, 3619, 3619|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_217|streaming/Video streaming plan/debit/ZAR|5|734.8, 734.8, 734.8, 734.8, 734.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_217|cloud_storage/Shared storage plan/debit/ZAR|5|192.5, 192.5, 192.5, 192.5, 192.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_217|shopping/Online retail purchases/debit/ZAR|5|1278.99, 1474.71, 1322.24, 1549.93, 1395.91|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_217|groceries/Local market purchase/debit/ZAR|2|1181.12, 1584.59|repeated but not demonstrably recurrent|||
|user_217|groceries/Weekly produce market/debit/ZAR|3|1249.33, 1840.72, 1478.93|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_217|groceries/Supermarket basket/debit/ZAR|6|1188.17, 1632.04, 1435.05, 1340.04, 1327.17, 1934.4|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_217|groceries/Bulk pantry shop/debit/ZAR|3|1510.31, 1870.04, 1761.38|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_217|groceries/Household groceries/debit/ZAR|6|1643.51, 1685.75, 1721.5, 1365.57, 1920.47, 1469.95|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_217|groceries/Neighbourhood grocer/debit/ZAR|3|1671.94, 1634.51, 1815.05|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_217|groceries/Grocery delivery/debit/ZAR|2|1212.99, 1911.3|repeated but not demonstrably recurrent|||
|user_217|transport/Parking and tolls/debit/ZAR|3|712.29, 897.77, 770.74|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_217|transport/Metro and bus fares/debit/ZAR|5|944.81, 797.2, 625.84, 734.12, 758.69|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_217|transport/Ride-hailing trip/debit/ZAR|3|658.09, 590.81, 550.8|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_217|transport/Vehicle charging/debit/ZAR|3|857.6, 766.33, 670.35|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_217|transport/Commuter pass/debit/ZAR|7|971.66, 926.33, 664.99, 600.27, 750.45, 962.27, 656.47|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_217|transport/Rail pass/debit/ZAR|2|795.5, 960.65|repeated but not demonstrably recurrent|||
|user_217|transport/Fuel refill/debit/ZAR|2|711.28, 558.27|repeated but not demonstrably recurrent|||
|user_217|dining/Bakery and snacks/debit/ZAR|2|1358.78, 1286.51|repeated but not demonstrably recurrent|||
|user_217|dining/Takeaway order/debit/ZAR|3|1413.56, 985.03, 1331.35|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_217|dining/Quick-service meal/debit/ZAR|2|1609.1, 1631.32|repeated but not demonstrably recurrent|||
|user_217|dining/Neighbourhood restaurant/debit/ZAR|3|1556.68, 1493.41, 1206.69|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_218|salary/Payroll credit/credit/IDR|5|48640000, 48640000, 48640000, 48640000, 48640000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_218|housing/Building maintenance payment/debit/IDR|6|3800000, 3800000, 3800000, 3800000, 3800000, 3800000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_218|utilities/Water and power payment/debit/IDR|5|2718318.65, 2492990.7, 2687703.28, 2801292.78, 2562015.09|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_218|insurance/Insurance policy payment/debit/IDR|5|1991200, 1991200, 1991200, 1991200, 1991200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_218|education/Child education fee/debit/IDR|5|3760100, 3760100, 3760100, 3760100, 3760100|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_218|healthcare/Diagnostic test/debit/IDR|5|1814562.94, 1903321.36, 1611929.77, 1673179.72, 1887029.58|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_218|entertainment/Monthly entertainment spend/debit/IDR|5|1286535.51, 1344821.99, 1302116.74, 1293090.12, 1133260.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_218|cloud_storage/Cloud storage plan/debit/IDR|5|189050, 189050, 189050, 189050, 189050|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_218|groceries/Grocery delivery/debit/IDR|3|1337125.59, 1348460.18, 1942680.99|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_218|groceries/Local market purchase/debit/IDR|4|1904559.47, 1309387.6, 2098711.41, 1994218.56|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_218|groceries/Weekly produce market/debit/IDR|2|2083442, 2109187.11|repeated but not demonstrably recurrent|||
|user_218|groceries/Supermarket basket/debit/IDR|4|1687590.29, 2176841.36, 1446723.47, 2167715.85|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_218|groceries/Fresh food shop/debit/IDR|2|1522116.1, 1852060.42|repeated but not demonstrably recurrent|||
|user_218|transport/Ride-hailing trip/debit/IDR|3|1039227.43, 1160630.37, 995037.32|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_218|transport/Local taxi/debit/IDR|2|1369886.77, 1148824.37|repeated but not demonstrably recurrent|||
|user_218|transport/Vehicle charging/debit/IDR|3|947359.91, 1441945.02, 928006.09|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_218|transport/Commuter pass/debit/IDR|3|1322394.74, 1280366.97, 1333149.07|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_218|dining/Takeaway order/debit/IDR|2|1852711.73, 1839130.67|repeated but not demonstrably recurrent|||
|user_218|dining/Coffee shop/debit/IDR|3|1469078.23, 1939020.45, 1935454.71|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_218|dining/Quick-service meal/debit/IDR|2|1753072.91, 1808827.65|repeated but not demonstrably recurrent|||
|user_219|salary/Payroll before leave/credit/EUR|2|1914, 1914|repeated but not demonstrably recurrent|||
|user_219|rent/Residential rent payment/debit/EUR|5|650.1, 650.1, 650.1, 650.1, 650.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_219|utilities/Water and power payment/debit/EUR|5|119.56, 115.45, 97.85, 115.12, 117.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_219|cloud_storage/Cloud storage plan/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_219|streaming/Video streaming plan/debit/EUR|5|53, 53, 53, 53, 53|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_219|shopping/Clothing and household items/debit/EUR|5|82.14, 83.32, 88.04, 78.57, 86.68|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_219|groceries/Grocery delivery/debit/EUR|4|75.18, 104.52, 85.51, 100.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_219|groceries/Supermarket basket/debit/EUR|4|97.05, 102.62, 105.82, 106.65|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_219|groceries/Neighbourhood grocer/debit/EUR|2|106.04, 66.33|repeated but not demonstrably recurrent|||
|user_219|groceries/Bulk pantry shop/debit/EUR|3|63.51, 62.23, 88.18|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_219|groceries/Local market purchase/debit/EUR|2|107.81, 78.24|repeated but not demonstrably recurrent|||
|user_219|transport/Rail pass/debit/EUR|3|39.32, 60.98, 36.79|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_219|transport/Parking and tolls/debit/EUR|2|62.3, 37.4|repeated but not demonstrably recurrent|||
|user_219|transport/Fuel refill/debit/EUR|2|38.31, 57.46|repeated but not demonstrably recurrent|||
|user_219|dining/Family dinner/debit/EUR|2|47.91, 58.4|repeated but not demonstrably recurrent|||
|user_219|dining/Bakery and snacks/debit/EUR|3|44.8, 47.66, 42.55|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_220|salary/Payroll credit/credit/EUR|5|1870, 1870, 1870, 1346.4, 1346.4|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_220|rent/Shared housing rent/debit/EUR|6|309.1, 309.1, 309.1, 309.1, 309.1, 309.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_220|utilities/Water and power payment/debit/EUR|6|77.99, 72.6, 72.85, 64.73, 73.89, 70.45|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_220|music_subscription/Music subscription/debit/EUR|5|9, 9, 9, 9, 9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_220|delivery_membership/Delivery service plan/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_220|gym/Community fitness plan/debit/EUR|5|35, 35, 35, 35, 35|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_220|entertainment/Games and recreation/debit/EUR|5|32.76, 33.34, 33.53, 41.24, 39.48|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_220|groceries/Neighbourhood grocer/debit/EUR|3|62.64, 58.52, 46.52|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_220|groceries/Local market purchase/debit/EUR|4|60.17, 64.47, 59.71, 50.26|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_220|groceries/Grocery delivery/debit/EUR|3|69.16, 74.97, 69.1|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_220|groceries/Bulk pantry shop/debit/EUR|6|62.53, 55.63, 60.43, 49.72, 73.57, 62.64|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_220|groceries/Household groceries/debit/EUR|2|66.46, 74.19|repeated but not demonstrably recurrent|||
|user_220|groceries/Supermarket basket/debit/EUR|2|52.02, 68.97|repeated but not demonstrably recurrent|||
|user_220|groceries/Fresh food shop/debit/EUR|2|75.44, 67.9|repeated but not demonstrably recurrent|||
|user_220|groceries/Weekly produce market/debit/EUR|4|44.84, 56.39, 53.97, 49.78|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_220|transport/Ride-hailing trip/debit/EUR|4|30.86, 26.5, 21.05, 26.19|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_220|transport/Metro and bus fares/debit/EUR|2|22.26, 31.08|repeated but not demonstrably recurrent|||
|user_220|transport/Parking and tolls/debit/EUR|4|21.73, 21.58, 29.08, 21.66|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_220|transport/Commuter pass/debit/EUR|2|19.32, 22.29|repeated but not demonstrably recurrent|||
|user_220|transport/Local taxi/debit/EUR|4|29.62, 23.52, 18.97, 19.46|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_220|transport/Vehicle charging/debit/EUR|2|28.08, 24.89|repeated but not demonstrably recurrent|||
|user_220|transport/Fuel refill/debit/EUR|4|24.81, 19.97, 27.26, 32.84|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_220|transport/Rail pass/debit/EUR|4|21.42, 26.79, 20.16, 29.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_220|dining/Weekend food delivery/debit/EUR|2|55.21, 52.23|repeated but not demonstrably recurrent|||
|user_220|dining/Family dinner/debit/EUR|5|68.49, 61.25, 42.93, 47.44, 45.38|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_220|dining/Takeaway order/debit/EUR|3|57.06, 53.54, 60.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_220|dining/Neighbourhood restaurant/debit/EUR|2|44.55, 64.87|repeated but not demonstrably recurrent|||
|user_221|salary/Payroll credit/credit/INR|5|118000, 118000, 118000, 118000, 118000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_221|rent/Landlord standing order/debit/INR|6|29300, 29300, 29300, 29300, 29300, 29300|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_221|utilities/Electricity bill/debit/INR|5|5070.09, 5409.75, 5879.61, 4818.47, 5751.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_221|debt_repayment/Personal loan payment/debit/INR|5|18900, 18900, 18900, 18900, 18900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_221|healthcare/Diagnostic test/debit/INR|5|4319.78, 4187.79, 4608.15, 4234.8, 4181.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_221|family_support/Childcare contribution/debit/INR|5|12530, 12530, 12530, 12530, 12530|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_221|cloud_storage/Cloud storage plan/debit/INR|5|375, 375, 375, 375, 375|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_221|shopping/Monthly shopping spend/debit/INR|5|3881.43, 3926.68, 4276.93, 4302.13, 3978.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_221|groceries/Household groceries/debit/INR|4|5381.59, 4002.41, 4371.7, 4895.73|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_221|groceries/Supermarket basket/debit/INR|3|4474.89, 4730.18, 5984.09|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_221|groceries/Bulk pantry shop/debit/INR|4|4637.01, 6166.95, 6176.13, 5078.78|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_221|groceries/Neighbourhood grocer/debit/INR|6|4055.71, 3618.02, 4136.89, 4614.95, 3931.28, 6130.6|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_221|groceries/Grocery delivery/debit/INR|2|4345.74, 3678.49|repeated but not demonstrably recurrent|||
|user_221|groceries/Weekly produce market/debit/INR|5|5413, 5197.15, 4834.99, 4151.12, 4285.21|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_221|groceries/Local market purchase/debit/INR|2|5310.06, 3799.12|repeated but not demonstrably recurrent|||
|user_221|transport/Local taxi/debit/INR|2|2569.73, 1828.5|repeated but not demonstrably recurrent|||
|user_221|transport/Rail pass/debit/INR|5|2332.27, 2181.8, 2465.33, 2010.54, 2959.97|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_221|transport/Parking and tolls/debit/INR|2|2981.99, 2037.08|repeated but not demonstrably recurrent|||
|user_221|transport/Metro and bus fares/debit/INR|2|2736.29, 2348.05|repeated but not demonstrably recurrent|||
|user_222|salary/Content contract payment/credit/ZAR|2|16274.89, 10196.54|repeated but not demonstrably recurrent|||
|user_222|rent/Shared housing rent/debit/ZAR|6|8404, 8404, 8404, 8404, 8404, 8404|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_222|utilities/Municipal utilities/debit/ZAR|5|1877.15, 2146.23, 2190.38, 2255.45, 1983.9|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_222|cloud_storage/Cloud storage plan/debit/ZAR|5|184.8, 184.8, 184.8, 184.8, 184.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_222|streaming/Family streaming plan/debit/ZAR|5|723.8, 723.8, 723.8, 723.8, 723.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_222|shopping/Personal shopping/debit/ZAR|5|1279.68, 1251.56, 1414.98, 1329.57, 1292.74|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_222|salary/Freelance milestone payment/credit/ZAR|2|12177.38, 10930.42|repeated but not demonstrably recurrent|||
|user_222|salary/Independent work payment/credit/ZAR|2|11653.9, 17131.21|repeated but not demonstrably recurrent|||
|user_222|salary/Design contract payment/credit/ZAR|2|18637.75, 13936.93|repeated but not demonstrably recurrent|||
|user_222|groceries/Fresh food shop/debit/ZAR|2|1636.22, 1313.92|repeated but not demonstrably recurrent|||
|user_222|groceries/Bulk pantry shop/debit/ZAR|3|1215.28, 1788.38, 1081.03|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_222|groceries/Grocery delivery/debit/ZAR|4|1213.51, 1752.1, 1292.24, 1735.04|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_222|groceries/Neighbourhood grocer/debit/ZAR|3|1752.89, 1750.95, 1429.2|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_222|groceries/Household groceries/debit/ZAR|3|1573.99, 1165.57, 1402.32|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_222|transport/Fuel refill/debit/ZAR|3|760.82, 751.19, 769.77|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_222|transport/Metro and bus fares/debit/ZAR|2|707.76, 466.93|repeated but not demonstrably recurrent|||
|user_222|transport/Local taxi/debit/ZAR|2|740.91, 504.12|repeated but not demonstrably recurrent|||
|user_222|dining/Neighbourhood restaurant/debit/ZAR|3|985.07, 1140.51, 1022.51|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_222|dining/Takeaway order/debit/ZAR|3|938.12, 1105.57, 765.85|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_222|dining/Coffee shop/debit/ZAR|2|917.93, 700.31|repeated but not demonstrably recurrent|||
|user_223|salary/Previous employer payroll/credit/EUR|4|1309, 1309, 1309, 1309|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_223|rent/Monthly rent/debit/EUR|6|342.1, 342.1, 342.1, 342.1, 342.1, 342.1|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_223|utilities/Household utility payment/debit/EUR|5|63.09, 57.45, 62.99, 57.65, 65.86|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_223|debt_repayment/Personal loan payment/debit/EUR|5|165, 165, 165, 165, 165|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_223|music_subscription/Music service subscription/debit/EUR|5|12, 12, 12, 12, 12|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_223|groceries/Fresh food shop/debit/EUR|2|43.61, 63.66|repeated but not demonstrably recurrent|||
|user_223|groceries/Bulk pantry shop/debit/EUR|3|68.58, 69.63, 53.26|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_223|groceries/Weekly produce market/debit/EUR|2|48.36, 63.17|repeated but not demonstrably recurrent|||
|user_223|groceries/Neighbourhood grocer/debit/EUR|2|43, 59.05|repeated but not demonstrably recurrent|||
|user_223|groceries/Local market purchase/debit/EUR|2|47.54, 61.58|repeated but not demonstrably recurrent|||
|user_223|transport/Ride-hailing trip/debit/EUR|2|17.46, 19.6|repeated but not demonstrably recurrent|||
|user_223|transport/Vehicle charging/debit/EUR|2|24.22, 20.83|repeated but not demonstrably recurrent|||
|user_223|transport/Metro and bus fares/debit/EUR|3|18.33, 25.87, 29.61|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_223|dining/Weekend food delivery/debit/EUR|2|45.66, 41.23|repeated but not demonstrably recurrent|||
|user_223|dining/Family dinner/debit/EUR|2|33.08, 28.69|repeated but not demonstrably recurrent|||
|user_223|dining/Takeaway order/debit/EUR|3|31.94, 35.56, 34.13|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_224|salary/Payroll credit/credit/IDR|5|36100000, 36100000, 36100000, 36100000, 36100000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_224|rent/Landlord standing order/debit/IDR|6|9310000, 9310000, 9310000, 9310000, 9310000, 9310000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_224|utilities/Water and power payment/debit/IDR|5|2336966.27, 2485406.99, 2312367.65, 2678229.73, 2677836.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_224|education/Child education fee/debit/IDR|5|3959600, 3959600, 3959600, 3959600, 3959600|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_224|debt_repayment/Loan repayment/debit/IDR|5|5548000, 5548000, 5548000, 5548000, 5548000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_224|music_subscription/Music subscription/debit/IDR|5|412300, 412300, 412300, 412300, 412300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_224|delivery_membership/Grocery delivery membership/debit/IDR|5|530100, 530100, 530100, 530100, 530100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_224|groceries/Grocery delivery/debit/IDR|6|1599812.82, 1115571.32, 1638463.11, 1126242.09, 1567636.31, 1123098.74|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_224|groceries/Household groceries/debit/IDR|2|1288264.24, 989812.71|repeated but not demonstrably recurrent|||
|user_224|groceries/Fresh food shop/debit/IDR|3|1115025.74, 1685786.52, 1355949.53|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_224|groceries/Local market purchase/debit/IDR|6|1179537.35, 1223175.67, 1570145.59, 989815.19, 1480771.83, 1474753.11|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_224|groceries/Neighbourhood grocer/debit/IDR|3|1600185.59, 1267045.6, 1095805.27|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_224|groceries/Supermarket basket/debit/IDR|2|1274676.3, 1126434.37|repeated but not demonstrably recurrent|||
|user_224|groceries/Bulk pantry shop/debit/IDR|4|1283772.45, 1448336.3, 1119327.67, 1061275.73|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_224|transport/Parking and tolls/debit/IDR|2|524892.56, 849959.8|repeated but not demonstrably recurrent|||
|user_224|transport/Vehicle charging/debit/IDR|6|595181.52, 708166.89, 756050.14, 548610.83, 812746.29, 713440.4|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_224|transport/Metro and bus fares/debit/IDR|4|703608.23, 728240.49, 785395.73, 833335.17|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_224|transport/Local taxi/debit/IDR|4|742465.18, 736581.99, 502526.35, 837060.88|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_224|transport/Ride-hailing trip/debit/IDR|4|832574.51, 529075.87, 500978.19, 815186.27|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_224|transport/Fuel refill/debit/IDR|4|528660.53, 693712.23, 762497.62, 763390.6|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_224|transport/Commuter pass/debit/IDR|2|822074.97, 725611.5|repeated but not demonstrably recurrent|||
|user_224|dining/Neighbourhood restaurant/debit/IDR|2|1198512.79, 1070982.82|repeated but not demonstrably recurrent|||
|user_224|dining/Takeaway order/debit/IDR|2|864335.89, 1108875.75|repeated but not demonstrably recurrent|||
|user_224|dining/Weekend food delivery/debit/IDR|2|904014.81, 1143822.23|repeated but not demonstrably recurrent|||
|user_224|dining/Coffee shop/debit/IDR|3|878029.47, 983602.92, 781658.3|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_224|dining/Bakery and snacks/debit/IDR|2|958922.16, 826708.02|repeated but not demonstrably recurrent|||
|user_225|salary/Payroll credit/credit/IDR|5|24890000, 24890000, 24890000, 24890000, 24890000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_225|rent/Residential rent payment/debit/IDR|6|6346000, 6346000, 6346000, 6346000, 6346000, 6346000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_225|utilities/Energy provider bill/debit/IDR|5|1325530.94, 1232311.06, 1142505.24, 1401153.94, 1369196.3|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_225|debt_repayment/Personal loan payment/debit/IDR|5|2650500, 2650500, 2650500, 2650500, 2650500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_225|streaming/Streaming subscription/debit/IDR|5|628900, 628900, 628900, 628900, 628900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_225|cloud_storage/Online backup subscription/debit/IDR|5|101650, 101650, 101650, 101650, 101650|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_225|shopping/Monthly shopping spend/debit/IDR|5|1204172.14, 1279452.84, 1158063.8, 1213773.87, 1316605.3|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_225|groceries/Bulk pantry shop/debit/IDR|4|773217.02, 998883.39, 821437.84, 886058.75|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_225|groceries/Household groceries/debit/IDR|5|1219257.78, 1140352.84, 762388.3, 761063.97, 1244037.99|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_225|groceries/Supermarket basket/debit/IDR|2|1053913.05, 750156.8|repeated but not demonstrably recurrent|||
|user_225|groceries/Fresh food shop/debit/IDR|4|857677.54, 771072.56, 1130328.94, 752699.42|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_225|groceries/Weekly produce market/debit/IDR|5|1135909.59, 889170.38, 794761.69, 899107.39, 812083.53|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_225|groceries/Local market purchase/debit/IDR|4|1119980.61, 936810.6, 993361.63, 882047.95|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_225|transport/Parking and tolls/debit/IDR|5|614361.85, 599629.03, 793240.61, 664326.98, 501036.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_225|transport/Commuter pass/debit/IDR|2|871867.55, 571893.14|repeated but not demonstrably recurrent|||
|user_225|transport/Ride-hailing trip/debit/IDR|9|580029.09, 883414.1, 871623.92, 586264.06, 724519.23, 761711.92, 828654.3, 794570.65, 846421.59|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_225|transport/Rail pass/debit/IDR|4|702984.23, 727398.49, 758797.78, 654263.76|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_225|transport/Vehicle charging/debit/IDR|2|631531.69, 533636.52|repeated but not demonstrably recurrent|||
|user_225|transport/Fuel refill/debit/IDR|2|695738.27, 628002.32|repeated but not demonstrably recurrent|||
|user_225|transport/Metro and bus fares/debit/IDR|2|869593.87, 623471.85|repeated but not demonstrably recurrent|||
|user_225|dining/Neighbourhood restaurant/debit/IDR|2|722583.99, 1018200.48|repeated but not demonstrably recurrent|||
|user_225|dining/Lunch with colleagues/debit/IDR|5|1205792.94, 757369.07, 976755.63, 1011041.51, 944756.05|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_225|dining/Weekend food delivery/debit/IDR|3|1179846.43, 1175711.56, 897505.86|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_226|salary/Payroll credit/credit/INR|5|260000, 260000, 260000, 260000, 260000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_226|rent/Shared housing rent/debit/INR|5|82200, 82200, 82200, 82200, 82200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_226|utilities/Electricity and water bill/debit/INR|5|14879.63, 13836.09, 12067.21, 13290.15, 13435.49|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_226|debt_repayment/Personal loan payment/debit/INR|5|38450, 38450, 38450, 38450, 38450|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_226|streaming/Family streaming plan/debit/INR|5|7400, 7400, 7400, 7400, 7400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_226|cloud_storage/Cloud storage plan/debit/INR|5|1000, 1000, 1000, 1000, 1000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_226|shopping/Personal shopping/debit/INR|5|8728.76, 7976.82, 9688.97, 9561.86, 8088.46|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_226|groceries/Grocery delivery/debit/INR|6|10145.99, 11886.27, 14151.83, 11689.04, 8859.02, 12127.11|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_226|groceries/Weekly produce market/debit/INR|7|9000.75, 8913.54, 11057.39, 11066.87, 10279.1, 13594.5, 12888.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_226|groceries/Supermarket basket/debit/INR|3|11820.28, 8813.11, 10277.23|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_226|groceries/Fresh food shop/debit/INR|2|10758.64, 13133.65|repeated but not demonstrably recurrent|||
|user_226|groceries/Neighbourhood grocer/debit/INR|3|13012, 14521.62, 14459.04|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_226|groceries/Local market purchase/debit/INR|3|13777.24, 12813.8, 11830.72|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_226|groceries/Household groceries/debit/INR|2|11872.55, 8490.66|repeated but not demonstrably recurrent|||
|user_226|transport/Commuter pass/debit/INR|6|6140.3, 5428.07, 6835.54, 6808.17, 4939.33, 5973.26|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_226|transport/Metro and bus fares/debit/INR|3|6727.96, 5237.54, 4040.16|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_226|transport/Parking and tolls/debit/INR|3|7071.02, 6783.91, 6972.67|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_226|transport/Ride-hailing trip/debit/INR|6|6559.95, 6422.65, 4826.3, 5424.96, 6347.43, 5911.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_226|transport/Local taxi/debit/INR|4|6312.12, 6538.72, 5246.6, 5327.31|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_226|dining/Neighbourhood restaurant/debit/INR|2|8042.23, 13054.3|repeated but not demonstrably recurrent|||
|user_226|dining/Coffee shop/debit/INR|2|9469.19, 13186.42|repeated but not demonstrably recurrent|||
|user_226|dining/Family dinner/debit/INR|4|13536.87, 10562.03, 13265.85, 8221.37|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_226|dining/Takeaway order/debit/INR|3|12521.81, 9541.36, 11986.43|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_227|salary/Payroll credit/credit/INR|5|94000, 94000, 94000, 94000, 94000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_227|housing/Property maintenance contribution/debit/INR|5|10250, 10250, 10250, 10250, 10250|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_227|utilities/Household utility payment/debit/INR|5|4838.78, 4926.37, 4804.09, 5024.41, 4758.92|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_227|insurance/Vehicle insurance premium/debit/INR|5|3470, 3470, 3470, 3470, 3470|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_227|education/Child education fee/debit/INR|5|7130, 7130, 7130, 7130, 7130|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_227|healthcare/Diagnostic test/debit/INR|5|2772.79, 3432.19, 3459.21, 2773.43, 3489.74|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_227|entertainment/Weekend entertainment/debit/INR|5|3967.79, 3720.5, 3735.04, 3839.77, 3789.53|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_227|cloud_storage/Cloud storage plan/debit/INR|5|795, 795, 795, 795, 795|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_227|groceries/Weekly produce market/debit/INR|3|4068.81, 3861.86, 2811.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_227|groceries/Neighbourhood grocer/debit/INR|2|3894.48, 2779.41|repeated but not demonstrably recurrent|||
|user_227|groceries/Grocery delivery/debit/INR|3|2902.97, 3010.19, 3534.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_227|groceries/Fresh food shop/debit/INR|4|4048.85, 3498.07, 4049.75, 4106.04|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_227|groceries/Supermarket basket/debit/INR|2|4449.05, 3951.72|repeated but not demonstrably recurrent|||
|user_227|groceries/Bulk pantry shop/debit/INR|2|4244.83, 4340.82|repeated but not demonstrably recurrent|||
|user_227|transport/Ride-hailing trip/debit/INR|2|1799.21, 2321.68|repeated but not demonstrably recurrent|||
|user_227|transport/Vehicle charging/debit/INR|2|1766.36, 2379.56|repeated but not demonstrably recurrent|||
|user_227|transport/Metro and bus fares/debit/INR|2|2171.47, 1533.44|repeated but not demonstrably recurrent|||
|user_227|transport/Local taxi/debit/INR|2|1641.41, 1839.62|repeated but not demonstrably recurrent|||
|user_227|transport/Commuter pass/debit/INR|2|1607.22, 1388.7|repeated but not demonstrably recurrent|||
|user_227|dining/Bakery and snacks/debit/INR|2|1910.13, 1799.3|repeated but not demonstrably recurrent|||
|user_227|dining/Quick-service meal/debit/INR|2|2695.02, 2241.81|repeated but not demonstrably recurrent|||
|user_227|dining/Neighbourhood restaurant/debit/INR|2|2084.9, 2261.09|repeated but not demonstrably recurrent|||
|user_228|rent/Shared housing rent/debit/IDR|6|7049000, 7049000, 7049000, 7049000, 7049000, 7049000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_228|utilities/Water and power payment/debit/IDR|6|1583551.33, 1543604.98, 1573017.31, 1772590.87, 1750497.45, 1650326.73|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_228|education/Professional training fee/debit/IDR|5|2986800, 2986800, 2986800, 2986800, 2986800|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_228|debt_repayment/Personal loan payment/debit/IDR|5|2460500, 2460500, 2460500, 2460500, 2460500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_228|music_subscription/Audio streaming plan/debit/IDR|5|190950, 190950, 190950, 190950, 190950|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_228|delivery_membership/Delivery service plan/debit/IDR|5|262200, 262200, 262200, 262200, 262200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_228|salary/First-job payroll/credit/IDR|2|30400000, 30400000|repeated but not demonstrably recurrent|||
|user_228|groceries/Grocery delivery/debit/IDR|5|1032069.48, 1395425.45, 1321360.29, 952328.65, 1035706.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_228|groceries/Fresh food shop/debit/IDR|6|1267979.23, 827126.29, 1090019.6, 1068959.2, 1435529.84, 854546.32|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_228|groceries/Household groceries/debit/IDR|3|1224759.05, 1124306.86, 1182601.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_228|groceries/Weekly produce market/debit/IDR|3|1173521.54, 1285648.32, 988400.28|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_228|groceries/Bulk pantry shop/debit/IDR|2|1351927.87, 989521.52|repeated but not demonstrably recurrent|||
|user_228|groceries/Supermarket basket/debit/IDR|3|1231200.05, 1232359.56, 1012633.46|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_228|groceries/Neighbourhood grocer/debit/IDR|2|1018384.92, 1343412.51|repeated but not demonstrably recurrent|||
|user_228|groceries/Local market purchase/debit/IDR|2|1338557.57, 1449370.17|repeated but not demonstrably recurrent|||
|user_228|transport/Metro and bus fares/debit/IDR|4|952611.98, 994901.47, 999487.45, 969204.91|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_228|transport/Fuel refill/debit/IDR|8|775248.97, 931457.19, 1043230.94, 665173.66, 832024.85, 771464, 787793.34, 906592.61|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_228|transport/Commuter pass/debit/IDR|4|876727.86, 976621.78, 679805.9, 646714.77|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_228|transport/Rail pass/debit/IDR|2|762275.53, 730508.06|repeated but not demonstrably recurrent|||
|user_228|transport/Parking and tolls/debit/IDR|2|896214.38, 626080.31|repeated but not demonstrably recurrent|||
|user_228|transport/Vehicle charging/debit/IDR|3|761216.8, 1069737.92, 779935.01|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_228|transport/Ride-hailing trip/debit/IDR|2|772563.18, 977452.37|repeated but not demonstrably recurrent|||
|user_228|dining/Quick-service meal/debit/IDR|4|1136626.41, 847172.43, 966535.12, 1371615.52|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_228|dining/Coffee shop/debit/IDR|2|913260.36, 963526.18|repeated but not demonstrably recurrent|||
|user_228|dining/Neighbourhood restaurant/debit/IDR|2|903646.5, 1068401.91|repeated but not demonstrably recurrent|||
|user_228|dining/Weekend food delivery/debit/IDR|2|1012128.37, 1094112.95|repeated but not demonstrably recurrent|||
|user_228|dining/Lunch with colleagues/debit/IDR|2|909996.98, 1169134.25|repeated but not demonstrably recurrent|||
|user_229|salary/Payroll credit/credit/EUR|5|1298, 1298, 1298, 1298, 1298|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_229|rent/Apartment rent transfer/debit/EUR|6|366.3, 366.3, 366.3, 366.3, 366.3, 366.3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_229|utilities/Household utility payment/debit/EUR|5|69.05, 64.64, 79.33, 68.97, 79.43|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_229|music_subscription/Music subscription/debit/EUR|5|10, 10, 10, 10, 10|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_229|delivery_membership/Food delivery membership/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_229|gym/Fitness club membership/debit/EUR|5|29, 29, 29, 29, 29|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_229|entertainment/Monthly entertainment spend/debit/EUR|5|45.95, 38.07, 38.45, 38.78, 42.33|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_229|groceries/Local market purchase/debit/EUR|6|33.69, 41.65, 51.62, 51.83, 39.82, 43.66|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_229|groceries/Weekly produce market/debit/EUR|6|54.98, 58.14, 37.67, 53.14, 36.9, 41.33|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_229|groceries/Grocery delivery/debit/EUR|2|58.63, 39.63|repeated but not demonstrably recurrent|||
|user_229|groceries/Neighbourhood grocer/debit/EUR|2|53.44, 48.82|repeated but not demonstrably recurrent|||
|user_229|groceries/Bulk pantry shop/debit/EUR|2|35.71, 45.8|repeated but not demonstrably recurrent|||
|user_229|groceries/Household groceries/debit/EUR|3|54.64, 34.94, 52.77|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_229|groceries/Fresh food shop/debit/EUR|4|55.27, 55.23, 36.04, 43.26|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Parking and tolls/debit/EUR|3|26.78, 32.64, 25.11|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Ride-hailing trip/debit/EUR|6|25.91, 32.96, 29.37, 34.38, 22.85, 30.64|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Fuel refill/debit/EUR|2|23.5, 25.87|repeated but not demonstrably recurrent|||
|user_229|transport/Metro and bus fares/debit/EUR|3|30.7, 21.89, 29.26|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Vehicle charging/debit/EUR|3|25.87, 21.83, 28.56|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Rail pass/debit/EUR|3|26.76, 33.55, 23.77|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Local taxi/debit/EUR|3|27.08, 26.94, 21.83|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_229|transport/Commuter pass/debit/EUR|3|22, 27.44, 32.2|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_229|dining/Quick-service meal/debit/EUR|2|61.49, 60.22|repeated but not demonstrably recurrent|||
|user_229|dining/Family dinner/debit/EUR|3|62.56, 48.6, 38.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_229|dining/Takeaway order/debit/EUR|2|57.42, 51.64|repeated but not demonstrably recurrent|||
|user_229|dining/Lunch with colleagues/debit/EUR|3|50.08, 43.15, 47.91|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_230|salary/Primary household salary/credit/EUR|5|1752.74, 1752.74, 1752.74, 1752.74, 1752.74|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_230|salary/Second household income/credit/EUR|4|1393.84, 1300.25, 1225.91, 1250.57|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_230|rent/Apartment rent transfer/debit/EUR|6|891, 891, 891, 891, 891, 891|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_230|utilities/Municipal utilities/debit/EUR|5|133.73, 129.18, 156.45, 153.26, 145.18|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_230|debt_repayment/Credit card repayment/debit/EUR|5|381, 381, 381, 381, 381|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_230|healthcare/Family healthcare expense/debit/EUR|5|120.58, 120.77, 110.97, 107.15, 121.48|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_230|family_support/Dependent care payment/debit/EUR|5|259, 259, 259, 259, 259|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_230|cloud_storage/Online backup subscription/debit/EUR|5|25, 25, 25, 25, 25|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_230|shopping/Household shopping/debit/EUR|5|87.74, 87.09, 87.63, 81.05, 71.12|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_230|groceries/Neighbourhood grocer/debit/EUR|5|85.54, 130.52, 124.4, 95.54, 112.99|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_230|groceries/Weekly produce market/debit/EUR|2|74.73, 124.77|repeated but not demonstrably recurrent|||
|user_230|groceries/Bulk pantry shop/debit/EUR|3|85.38, 89.23, 88.39|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_230|groceries/Local market purchase/debit/EUR|4|125.73, 91.62, 119.35, 87.86|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_230|groceries/Household groceries/debit/EUR|3|96.17, 84.37, 110.44|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_230|groceries/Grocery delivery/debit/EUR|6|92.9, 79.65, 79.7, 95.43, 93.7, 120.57|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_230|groceries/Fresh food shop/debit/EUR|2|90.87, 95.09|repeated but not demonstrably recurrent|||
|user_230|transport/Fuel refill/debit/EUR|2|77.25, 69.9|repeated but not demonstrably recurrent|||
|user_230|transport/Parking and tolls/debit/EUR|3|62.96, 79.7, 47.77|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_230|transport/Local taxi/debit/EUR|2|58.4, 46.68|repeated but not demonstrably recurrent|||
|user_230|transport/Rail pass/debit/EUR|2|73.21, 71.67|repeated but not demonstrably recurrent|||
|user_231|salary/Payroll credit/credit/ZAR|5|44000, 44000, 44000, 44000, 44000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_231|rent/Residential rent payment/debit/ZAR|5|14168, 14168, 14168, 14168, 14168|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_231|utilities/Water and power payment/debit/ZAR|5|3021.7, 3377.55, 3256.81, 2972.83, 3027.81|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_231|insurance/Health insurance premium/debit/ZAR|5|1449.8, 1449.8, 1449.8, 1449.8, 1449.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_231|cloud_storage/Shared storage plan/debit/ZAR|5|221.1, 221.1, 221.1, 221.1, 221.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_231|streaming/Streaming subscription/debit/ZAR|5|904.2, 904.2, 904.2, 904.2, 904.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_231|shopping/Personal shopping/debit/ZAR|5|847.86, 964.23, 822.1, 991.3, 790.54|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_231|entertainment/Local event tickets/debit/ZAR|5|1283.05, 1315.79, 1157.98, 1198.17, 1279.51|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_231|groceries/Local market purchase/debit/ZAR|6|2113.27, 2235.38, 1740.05, 1677.99, 2023.09, 2280.18|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_231|groceries/Supermarket basket/debit/ZAR|4|1940.02, 2292.64, 1585.25, 2226.18|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_231|groceries/Neighbourhood grocer/debit/ZAR|3|1794.57, 1789.59, 1934.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_231|groceries/Fresh food shop/debit/ZAR|2|1932.39, 2182.96|repeated but not demonstrably recurrent|||
|user_231|transport/Commuter pass/debit/ZAR|5|1189.38, 1382.46, 969.76, 1379.09, 1119.33|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Parking and tolls/debit/ZAR|3|1153.04, 1477.69, 1543.95|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Fuel refill/debit/ZAR|3|938.05, 1469.38, 1005.63|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Metro and bus fares/debit/ZAR|6|907.67, 1513.12, 1331.04, 1247.12, 1429.28, 980.77|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Rail pass/debit/ZAR|6|1060.2, 1080.46, 1068.42, 1173.73, 900.17, 1484.11|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Vehicle charging/debit/ZAR|5|972.91, 1325.55, 1464.56, 1096.29, 1502.67|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Ride-hailing trip/debit/ZAR|4|1120.65, 1131.32, 967.02, 1288.7|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_231|transport/Local taxi/debit/ZAR|3|1000.37, 1296.92, 917.91|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_231|dining/Coffee shop/debit/ZAR|2|1360.62, 1917.06|repeated but not demonstrably recurrent|||
|user_231|dining/Lunch with colleagues/debit/ZAR|5|1759.45, 1537.52, 1834.34, 1477.3, 1815.67|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_231|dining/Neighbourhood restaurant/debit/ZAR|4|1945.81, 1970.65, 1253.56, 1709.72|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_231|dining/Quick-service meal/debit/ZAR|5|1427.07, 1711.95, 1683.09, 2078.55, 1515.99|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_231|dining/Family dinner/debit/ZAR|3|1844.49, 1224.12, 1592.18|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_231|dining/Weekend food delivery/debit/ZAR|3|1458.11, 1806.4, 1898.11|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_231|dining/Bakery and snacks/debit/ZAR|3|1738.95, 1395.32, 1672.73|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_232|rent/Landlord standing order/debit/EUR|6|873.4, 873.4, 873.4, 873.4, 873.4, 873.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_232|utilities/Water and power payment/debit/EUR|5|182.83, 202.65, 165.6, 171, 189.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_232|education/Professional training fee/debit/EUR|5|245, 245, 245, 245, 245|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_232|debt_repayment/Credit card repayment/debit/EUR|5|463, 463, 463, 463, 463|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_232|music_subscription/Audio streaming plan/debit/EUR|5|20, 20, 20, 20, 20|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_232|delivery_membership/Food delivery membership/debit/EUR|5|23, 23, 23, 23, 23|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_232|salary/First-job payroll/credit/EUR|2|2772, 2772|repeated but not demonstrably recurrent|||
|user_232|groceries/Weekly produce market/debit/EUR|3|100.74, 125.62, 131.74|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_232|groceries/Supermarket basket/debit/EUR|2|89.56, 94.31|repeated but not demonstrably recurrent|||
|user_232|groceries/Bulk pantry shop/debit/EUR|5|101.52, 119.46, 90.69, 128.43, 125.97|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_232|groceries/Household groceries/debit/EUR|4|107.11, 132.91, 94.43, 130.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_232|groceries/Local market purchase/debit/EUR|2|119.61, 98.61|repeated but not demonstrably recurrent|||
|user_232|groceries/Neighbourhood grocer/debit/EUR|4|113.35, 138.41, 130.53, 125.74|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_232|groceries/Grocery delivery/debit/EUR|3|119.42, 83.27, 143.87|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_232|groceries/Fresh food shop/debit/EUR|3|120.42, 110.41, 126.72|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_232|transport/Commuter pass/debit/EUR|3|67.38, 44.56, 68.87|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_232|transport/Ride-hailing trip/debit/EUR|4|67.03, 53.8, 62.5, 63.27|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_232|transport/Parking and tolls/debit/EUR|6|65.41, 72.39, 57.53, 42.83, 47.47, 55.43|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_232|transport/Local taxi/debit/EUR|2|42.45, 66.56|repeated but not demonstrably recurrent|||
|user_232|transport/Rail pass/debit/EUR|2|44.56, 58.33|repeated but not demonstrably recurrent|||
|user_232|transport/Metro and bus fares/debit/EUR|3|43.35, 58.71, 44.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_232|transport/Fuel refill/debit/EUR|3|66.68, 48.26, 58.76|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_232|transport/Vehicle charging/debit/EUR|3|60.23, 60.9, 41.64|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_232|dining/Weekend food delivery/debit/EUR|2|96.57, 92.02|repeated but not demonstrably recurrent|||
|user_232|dining/Quick-service meal/debit/EUR|3|92.19, 90.1, 112.54|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_232|dining/Takeaway order/debit/EUR|3|107.39, 104.45, 83.68|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_232|dining/Neighbourhood restaurant/debit/EUR|2|83.9, 104.22|repeated but not demonstrably recurrent|||
|user_233|rent/Shared housing rent/debit/IDR|6|3895000, 3895000, 3895000, 3895000, 3895000, 3895000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_233|utilities/Electricity and water bill/debit/IDR|6|1140535.55, 1158999.75, 1038485.01, 1012817.3, 1065181.69, 1076322.99|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_233|education/School fee payment/debit/IDR|5|1027900, 1027900, 1027900, 1027900, 1027900|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_233|debt_repayment/Loan repayment/debit/IDR|5|2099500, 2099500, 2099500, 2099500, 2099500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_233|music_subscription/Music subscription/debit/IDR|5|102600, 102600, 102600, 102600, 102600|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_233|delivery_membership/Delivery service plan/debit/IDR|5|277400, 277400, 277400, 277400, 277400|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_233|groceries/Weekly produce market/debit/IDR|7|752109.76, 556588.1, 557096.21, 636712.22, 960452.83, 817730.19, 716049.63|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_233|groceries/Bulk pantry shop/debit/IDR|5|935952.57, 594510.73, 883029.07, 806100.16, 767939.73|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_233|groceries/Neighbourhood grocer/debit/IDR|3|584455.38, 947127.8, 759505.41|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_233|groceries/Supermarket basket/debit/IDR|3|669975.95, 894815.34, 957685.8|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_233|groceries/Household groceries/debit/IDR|2|790492.1, 653618.99|repeated but not demonstrably recurrent|||
|user_233|groceries/Grocery delivery/debit/IDR|2|552844.41, 842623.88|repeated but not demonstrably recurrent|||
|user_233|groceries/Local market purchase/debit/IDR|3|766911.38, 696349.56, 597889.53|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_233|transport/Fuel refill/debit/IDR|5|339484.26, 311066.66, 508987.03, 420927.6, 488072.14|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_233|transport/Vehicle charging/debit/IDR|5|476166.2, 414442.71, 477456.37, 366939.5, 353399.8|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_233|transport/Commuter pass/debit/IDR|3|422922.8, 420915.45, 455715.39|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_233|transport/Local taxi/debit/IDR|4|510240.27, 357004.55, 522923.47, 335705.3|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_233|transport/Metro and bus fares/debit/IDR|7|452262.74, 520982.34, 432157, 315439.45, 485509.42, 302358.08, 387127.05|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_233|dining/Takeaway order/debit/IDR|2|716482.5, 606022.06|repeated but not demonstrably recurrent|||
|user_233|dining/Coffee shop/debit/IDR|4|674294.13, 421236.33, 460927.84, 529143.13|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_233|dining/Quick-service meal/debit/IDR|4|435519.29, 646189.78, 533786.45, 494220.86|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_233|dining/Bakery and snacks/debit/IDR|2|693449.03, 518947.14|repeated but not demonstrably recurrent|||
|user_234|salary/Payroll credit/credit/EUR|5|913, 913, 913, 913, 913|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_234|housing/Home association fee/debit/EUR|5|86, 86, 86, 86, 86|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_234|utilities/Energy provider bill/debit/EUR|5|62.37, 64.13, 60.59, 57.03, 64.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_234|insurance/Health insurance premium/debit/EUR|5|45, 45, 45, 45, 45|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_234|healthcare/Therapy appointment/debit/EUR|5|37.62, 41.46, 36.28, 41.26, 37.25|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_234|streaming/Family streaming plan/debit/EUR|5|19, 19, 19, 19, 19|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_234|groceries/Supermarket basket/debit/EUR|4|32.5, 49.69, 41.88, 33.69|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_234|groceries/Fresh food shop/debit/EUR|2|37.67, 43.4|repeated but not demonstrably recurrent|||
|user_234|groceries/Weekly produce market/debit/EUR|2|43.8, 28.41|repeated but not demonstrably recurrent|||
|user_234|groceries/Bulk pantry shop/debit/EUR|2|45.55, 32.88|repeated but not demonstrably recurrent|||
|user_234|groceries/Grocery delivery/debit/EUR|2|31.55, 41.14|repeated but not demonstrably recurrent|||
|user_234|groceries/Local market purchase/debit/EUR|5|29.09, 44.14, 47.62, 36.43, 42.75|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_234|transport/Local taxi/debit/EUR|2|25.85, 23.46|repeated but not demonstrably recurrent|||
|user_234|transport/Ride-hailing trip/debit/EUR|2|21.21, 19.24|repeated but not demonstrably recurrent|||
|user_234|transport/Commuter pass/debit/EUR|2|26.35, 25.95|repeated but not demonstrably recurrent|||
|user_234|transport/Parking and tolls/debit/EUR|2|22.5, 20.13|repeated but not demonstrably recurrent|||
|user_234|transport/Rail pass/debit/EUR|2|21.51, 19.51|repeated but not demonstrably recurrent|||
|user_234|dining/Takeaway order/debit/EUR|4|28.72, 34.13, 35.87, 38.01|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_234|dining/Lunch with colleagues/debit/EUR|4|28.12, 40.08, 29.28, 35.92|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_234|dining/Bakery and snacks/debit/EUR|2|26.86, 38.12|repeated but not demonstrably recurrent|||
|user_234|dining/Quick-service meal/debit/EUR|2|35.57, 25.44|repeated but not demonstrably recurrent|||
|user_235|salary/Payroll credit/credit/EUR|5|1019.15, 1019.15, 1019.15, 1019.15, 1019.15|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_235|rent/Residential rent payment/debit/USD|6|224.4, 224.4, 224.4, 224.4, 224.4, 224.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_235|utilities/Municipal utilities/debit/USD|5|50.12, 53.02, 47.35, 50.86, 54.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_235|insurance/Household insurance/debit/USD|5|41, 41, 41, 41, 41|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_235|cloud_storage/Cloud storage plan/debit/USD|5|6, 6, 6, 6, 6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_235|streaming/Family streaming plan/debit/USD|5|27, 27, 27, 27, 27|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_235|shopping/Online retail purchases/debit/USD|5|40.07, 39.94, 43.49, 37.1, 40.78|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_235|entertainment/Games and recreation/debit/USD|5|16.5, 19.28, 16.32, 17.56, 20|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_235|groceries/Household groceries/debit/USD|2|49.32, 57.75|repeated but not demonstrably recurrent|||
|user_235|groceries/Weekly produce market/debit/USD|4|40.86, 56.25, 45.43, 47.32|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_235|groceries/Fresh food shop/debit/USD|3|51.8, 44.55, 49.69|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_235|groceries/Neighbourhood grocer/debit/USD|2|36.2, 52.26|repeated but not demonstrably recurrent|||
|user_235|groceries/Bulk pantry shop/debit/USD|2|43.64, 39.85|repeated but not demonstrably recurrent|||
|user_235|groceries/Supermarket basket/debit/USD|2|57.86, 36.81|repeated but not demonstrably recurrent|||
|user_235|groceries/Local market purchase/debit/USD|2|41.09, 36.24|repeated but not demonstrably recurrent|||
|user_235|transport/Vehicle charging/debit/USD|5|17.98, 17.56, 26.11, 18.83, 29.51|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_235|transport/Metro and bus fares/debit/USD|4|29.22, 25.52, 29.08, 19.85|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_235|transport/Local taxi/debit/USD|10|27.44, 24.15, 22.21, 27.16, 23.85, 27.04, 26.57, 23.92, 29.54, 17.93|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_235|transport/Parking and tolls/debit/USD|3|27.02, 23.48, 25.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_235|transport/Fuel refill/debit/USD|4|23.43, 19.46, 20.91, 30.23|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_235|transport/Rail pass/debit/USD|4|29.78, 17.94, 22.38, 29.77|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_235|transport/Ride-hailing trip/debit/USD|2|19.85, 23.58|repeated but not demonstrably recurrent|||
|user_235|transport/Commuter pass/debit/USD|3|24.71, 27.43, 28.93|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_235|dining/Family dinner/debit/USD|5|35.4, 31.44, 35.95, 31.66, 45.13|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_235|dining/Lunch with colleagues/debit/USD|3|36.94, 34.07, 40.62|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_235|dining/Coffee shop/debit/USD|4|37.42, 37.23, 46.38, 34.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_235|dining/Weekend food delivery/debit/USD|3|31.09, 29.51, 38.36|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_235|dining/Quick-service meal/debit/USD|2|48.56, 38.64|repeated but not demonstrably recurrent|||
|user_235|dining/Bakery and snacks/debit/USD|4|36.93, 38.13, 41.9, 41.52|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_235|dining/Takeaway order/debit/USD|5|36.65, 28.69, 31.16, 47.31, 42.53|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_236|salary/Payroll credit/credit/IDR|5|22420000, 22420000, 22420000, 22420000, 22420000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_236|housing/Home repair reserve/debit/IDR|6|2584000, 2584000, 2584000, 2584000, 2584000, 2584000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_236|utilities/Energy provider bill/debit/IDR|5|1344396.44, 1657888.36, 1400471.91, 1600000.63, 1427489.97|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_236|insurance/Health insurance premium/debit/IDR|5|1117200, 1117200, 1117200, 1117200, 1117200|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_236|education/School fee payment/debit/IDR|5|2356000, 2356000, 2356000, 2356000, 2356000|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_236|healthcare/Family healthcare expense/debit/IDR|5|1704371.09, 1739809, 1581179.34, 1840765.68, 1493958.89|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_236|entertainment/Games and recreation/debit/IDR|5|460814.95, 451352.09, 430511.34, 494914.12, 470533.13|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_236|cloud_storage/Cloud storage plan/debit/IDR|5|95950, 95950, 95950, 95950, 95950|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_236|groceries/Supermarket basket/debit/IDR|2|707817.31, 1039082.35|repeated but not demonstrably recurrent|||
|user_236|groceries/Weekly produce market/debit/IDR|4|656842.27, 826741.55, 863857.62, 738743.14|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_236|groceries/Grocery delivery/debit/IDR|4|657320.98, 938836.44, 1078087.24, 648593.65|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_236|groceries/Household groceries/debit/IDR|2|859052.45, 767968.33|repeated but not demonstrably recurrent|||
|user_236|groceries/Local market purchase/debit/IDR|4|870376.51, 979797.91, 976968.58, 1023080|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_236|transport/Commuter pass/debit/IDR|3|485290.15, 658293.75, 623634.19|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_236|transport/Metro and bus fares/debit/IDR|3|407198.85, 399503, 618676.6|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_236|transport/Ride-hailing trip/debit/IDR|2|663284.87, 629742.96|repeated but not demonstrably recurrent|||
|user_236|transport/Parking and tolls/debit/IDR|2|403117.88, 448761.83|repeated but not demonstrably recurrent|||
|user_236|dining/Weekend food delivery/debit/IDR|2|877967.75, 666837.52|repeated but not demonstrably recurrent|||
|user_237|rent/Shared housing rent/debit/IDR|6|7695000, 7695000, 7695000, 7695000, 7695000, 7695000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_237|utilities/Energy provider bill/debit/IDR|5|1855483.37, 2061230.01, 1978462.16, 2150724.21, 1833100.55|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_237|cloud_storage/Shared storage plan/debit/IDR|5|268850, 268850, 268850, 268850, 268850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_237|streaming/Family streaming plan/debit/IDR|5|765700, 765700, 765700, 765700, 765700|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_237|shopping/Clothing and household items/debit/IDR|5|1499088.01, 1387939.06, 1249197.04, 1253636.18, 1509740.57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_237|salary/Peak-season wages/credit/IDR|2|25730389.06, 28612583.81|repeated but not demonstrably recurrent|||
|user_237|groceries/Neighbourhood grocer/debit/IDR|4|1067537.03, 1071977.28, 1130278.27, 1641362.65|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_237|groceries/Grocery delivery/debit/IDR|4|990089.35, 1153275.99, 1198118.49, 1544507.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_237|groceries/Bulk pantry shop/debit/IDR|4|1412621.2, 1283382.46, 1133815.7, 1110467.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_237|groceries/Weekly produce market/debit/IDR|3|1409535.04, 1250058.37, 1560955.54|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_237|transport/Ride-hailing trip/debit/IDR|3|972054.62, 820437.91, 765642.68|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_237|dining/Bakery and snacks/debit/IDR|2|1658256.62, 1067792.12|repeated but not demonstrably recurrent|||
|user_237|dining/Neighbourhood restaurant/debit/IDR|3|1000129.26, 1445644.82, 1596135.54|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_238|salary/Primary household salary/credit/USD|5|565.44, 565.44, 565.44, 565.44, 565.44|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_238|salary/Second household income/credit/USD|4|425.96, 430.19, 391.73, 431.51|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_238|rent/Monthly rent/debit/USD|6|205.2, 205.2, 205.2, 205.2, 205.2, 205.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_238|utilities/Energy provider bill/debit/USD|5|45.06, 53.75, 48.81, 53.35, 52.61|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_238|music_subscription/Music service subscription/debit/USD|5|9, 9, 9, 9, 9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_238|delivery_membership/Delivery service plan/debit/USD|5|9, 9, 9, 9, 9|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_238|gym/Gym membership/debit/USD|5|28, 28, 28, 28, 28|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_238|entertainment/Games and recreation/debit/USD|5|25.18, 28.31, 30.94, 30.18, 27.1|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Supermarket basket/debit/USD|4|54.21, 54.27, 42.13, 53.21|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Local market purchase/debit/USD|4|35.8, 32.05, 36.54, 41.24|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Fresh food shop/debit/USD|5|36.96, 39.6, 36.28, 49.58, 36.49|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Household groceries/debit/USD|4|45.38, 31.39, 49.46, 33.4|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Grocery delivery/debit/USD|3|46.97, 37.75, 51.45|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Weekly produce market/debit/USD|3|53.05, 39.09, 45.84|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_238|groceries/Bulk pantry shop/debit/USD|2|53.01, 49.09|repeated but not demonstrably recurrent|||
|user_238|transport/Rail pass/debit/USD|2|17.96, 22.84|repeated but not demonstrably recurrent|||
|user_238|transport/Metro and bus fares/debit/USD|2|23.91, 20.07|repeated but not demonstrably recurrent|||
|user_238|transport/Local taxi/debit/USD|4|25.05, 17.83, 19.5, 23.35|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_238|transport/Fuel refill/debit/USD|4|19.74, 29.08, 20.98, 25.54|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_238|transport/Parking and tolls/debit/USD|5|17.58, 26.97, 21.78, 21.67, 26.96|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_238|transport/Ride-hailing trip/debit/USD|5|27.53, 22.01, 29.11, 27.55, 23.65|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_238|transport/Commuter pass/debit/USD|2|23.6, 29.23|repeated but not demonstrably recurrent|||
|user_238|dining/Family dinner/debit/USD|3|37.21, 37.3, 33.93|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_238|dining/Coffee shop/debit/USD|2|39.47, 38.07|repeated but not demonstrably recurrent|||
|user_238|dining/Bakery and snacks/debit/USD|2|39.35, 31.55|repeated but not demonstrably recurrent|||
|user_238|dining/Quick-service meal/debit/USD|3|45.62, 29.61, 29.51|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_238|dining/Weekend food delivery/debit/USD|2|29.72, 46.21|repeated but not demonstrably recurrent|||
|user_239|salary/Payroll before leave/credit/USD|2|1020, 1020|repeated but not demonstrably recurrent|||
|user_239|rent/Landlord standing order/debit/USD|5|321.6, 321.6, 321.6, 321.6, 321.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_239|utilities/Municipal utilities/debit/USD|5|63.58, 67.81, 72.9, 72.93, 66.72|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_239|debt_repayment/Personal loan payment/debit/USD|5|82, 82, 82, 82, 82|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_239|healthcare/Clinic payment/debit/USD|5|67.85, 74.88, 70.02, 77.67, 72.57|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_239|family_support/Family support payment/debit/USD|5|91, 91, 91, 91, 91|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_239|cloud_storage/Online backup subscription/debit/USD|5|7, 7, 7, 7, 7|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_239|shopping/Monthly shopping spend/debit/USD|5|25.32, 23.54, 20.8, 25.12, 21.93|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_239|groceries/Fresh food shop/debit/USD|5|55.39, 46.73, 44.94, 57.27, 39.89|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_239|groceries/Bulk pantry shop/debit/USD|2|45.29, 59.67|repeated but not demonstrably recurrent|||
|user_239|groceries/Local market purchase/debit/USD|3|56.56, 44.04, 37.9|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_239|groceries/Supermarket basket/debit/USD|5|47.01, 51.73, 56.67, 43.68, 48.4|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_239|groceries/Household groceries/debit/USD|2|36.25, 45.19|repeated but not demonstrably recurrent|||
|user_239|groceries/Grocery delivery/debit/USD|6|48.74, 38.93, 33.98, 34.81, 58.52, 54.06|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_239|transport/Rail pass/debit/USD|2|24.41, 20.55|repeated but not demonstrably recurrent|||
|user_239|transport/Commuter pass/debit/USD|3|25.15, 26.09, 28.13|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_239|transport/Parking and tolls/debit/USD|2|23.82, 25.7|repeated but not demonstrably recurrent|||
|user_239|transport/Vehicle charging/debit/USD|2|16.74, 22.41|repeated but not demonstrably recurrent|||
|user_240|rent/Residential rent payment/debit/INR|6|16100, 16100, 16100, 16100, 16100, 16100|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_240|utilities/Municipal utilities/debit/INR|6|3233.67, 3665.78, 3220.24, 3951.14, 3859.06, 3313.38|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_240|education/School fee payment/debit/INR|5|6740, 6740, 6740, 6740, 6740|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_240|debt_repayment/Education loan instalment/debit/INR|5|9350, 9350, 9350, 9350, 9350|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_240|music_subscription/Audio streaming plan/debit/INR|5|570, 570, 570, 570, 570|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_240|delivery_membership/Delivery service plan/debit/INR|5|720, 720, 720, 720, 720|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_240|salary/First-job payroll/credit/INR|2|62000, 62000|repeated but not demonstrably recurrent|||
|user_240|groceries/Neighbourhood grocer/debit/INR|6|2960.45, 2198.11, 2626.02, 2601.48, 2767.67, 1959.27|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_240|groceries/Household groceries/debit/INR|4|3464.84, 2040.53, 3229.29, 2866.41|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_240|groceries/Weekly produce market/debit/INR|3|2000.84, 3235.99, 2334.3|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_240|groceries/Bulk pantry shop/debit/INR|2|2034.95, 2371.1|repeated but not demonstrably recurrent|||
|user_240|groceries/Local market purchase/debit/INR|2|2299.68, 3154.91|repeated but not demonstrably recurrent|||
|user_240|groceries/Grocery delivery/debit/INR|6|3201.59, 3210.19, 2269.36, 2460.72, 3175, 2327.04|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_240|groceries/Fresh food shop/debit/INR|3|2956.67, 2917.39, 2000.04|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Ride-hailing trip/debit/INR|3|1202.78, 1328.73, 1085.73|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Fuel refill/debit/INR|5|929.68, 1283.23, 1374.09, 869.16, 1441.24|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Local taxi/debit/INR|3|1249.65, 1301.23, 968.71|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Parking and tolls/debit/INR|4|854.26, 849.24, 1055.24, 1158.86|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Metro and bus fares/debit/INR|4|1348.78, 1354.62, 1140.03, 1432.29|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Commuter pass/debit/INR|5|1131.15, 1030.74, 962.9, 939.89, 1294.58|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_240|transport/Rail pass/debit/INR|2|1034.8, 1003.95|repeated but not demonstrably recurrent|||
|user_240|dining/Quick-service meal/debit/INR|3|2321.57, 2282.83, 2311.98|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_240|dining/Bakery and snacks/debit/INR|3|2081.63, 3073.61, 2601.56|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_240|dining/Neighbourhood restaurant/debit/INR|3|2152.37, 2251.93, 2769.02|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_241|rent/Residential rent payment/debit/IDR|6|7182000, 7182000, 7182000, 7182000, 7182000, 7182000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_241|utilities/Electricity bill/debit/IDR|5|1575646.28, 1595763.92, 1339647.9, 1286458.46, 1383559.12|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_241|debt_repayment/Credit card repayment/debit/IDR|5|4066000, 4066000, 4066000, 4066000, 4066000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_241|music_subscription/Audio streaming plan/debit/IDR|5|262200, 262200, 262200, 262200, 262200|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_241|salary/Temporary assignment pay/credit/IDR|2|29546144.66, 22898788.56|repeated but not demonstrably recurrent|||
|user_241|groceries/Neighbourhood grocer/debit/IDR|2|992400.91, 924123.77|repeated but not demonstrably recurrent|||
|user_241|groceries/Supermarket basket/debit/IDR|2|1015380.99, 976661.16|repeated but not demonstrably recurrent|||
|user_241|groceries/Weekly produce market/debit/IDR|2|1195238.21, 1111684.92|repeated but not demonstrably recurrent|||
|user_241|groceries/Household groceries/debit/IDR|2|1154077.72, 1069591.52|repeated but not demonstrably recurrent|||
|user_241|groceries/Local market purchase/debit/IDR|2|1122459.59, 1331166.36|repeated but not demonstrably recurrent|||
|user_241|transport/Fuel refill/debit/IDR|4|653801.95, 585974.1, 588978.85, 584214.93|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_241|transport/Commuter pass/debit/IDR|2|539034.87, 388016.04|repeated but not demonstrably recurrent|||
|user_241|dining/Bakery and snacks/debit/IDR|2|1270816.22, 1223345.04|repeated but not demonstrably recurrent|||
|user_241|dining/Takeaway order/debit/IDR|2|830129.34, 1082664.91|repeated but not demonstrably recurrent|||
|user_241|dining/Lunch with colleagues/debit/IDR|2|1176539.79, 1104540.73|repeated but not demonstrably recurrent|||
|user_242|rent/Shared housing rent/debit/EUR|6|270.6, 270.6, 270.6, 270.6, 270.6, 270.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_242|utilities/Household utility payment/debit/EUR|5|67.09, 70.58, 68.85, 62, 72.01|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_242|education/Child education fee/debit/EUR|5|60, 60, 60, 60, 60|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_242|debt_repayment/Personal loan payment/debit/EUR|5|75, 75, 75, 75, 75|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_242|music_subscription/Music service subscription/debit/EUR|5|10, 10, 10, 10, 10|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_242|delivery_membership/Delivery service plan/debit/EUR|5|13, 13, 13, 13, 13|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_242|groceries/Neighbourhood grocer/debit/EUR|3|50.03, 45.79, 48.6|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_242|groceries/Bulk pantry shop/debit/EUR|8|44.41, 49.92, 52.09, 35.34, 46.77, 47.47, 38.97, 43.16|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_242|groceries/Household groceries/debit/EUR|6|46.47, 38.39, 40.25, 40.77, 49.34, 34.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_242|groceries/Grocery delivery/debit/EUR|3|53.99, 32.5, 48.54|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_242|groceries/Supermarket basket/debit/EUR|3|35.41, 41.6, 47.73|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_242|transport/Rail pass/debit/EUR|7|24.08, 16.41, 23.96, 17.76, 22.53, 15.18, 14.22|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_242|transport/Fuel refill/debit/EUR|5|16.37, 16.02, 15.21, 19.15, 14.46|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_242|transport/Metro and bus fares/debit/EUR|3|13.9, 23.03, 22.69|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_242|transport/Ride-hailing trip/debit/EUR|5|20.81, 22, 22.21, 16.45, 19.1|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_242|transport/Parking and tolls/debit/EUR|3|17.12, 20.11, 18.27|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_242|dining/Weekend food delivery/debit/EUR|3|42.36, 25.79, 38.67|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_242|dining/Neighbourhood restaurant/debit/EUR|3|36.86, 43.03, 41.48|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_242|dining/Family dinner/debit/EUR|3|32.13, 27.45, 35.84|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_242|dining/Coffee shop/debit/EUR|2|34.35, 34.73|repeated but not demonstrably recurrent|||
|user_243|salary/Payroll credit/credit/ZAR|5|23980, 23980, 23980, 23980, 23980|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_243|housing/Property maintenance contribution/debit/ZAR|6|2343, 2343, 2343, 2343, 2343, 2343|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_243|utilities/Municipal utilities/debit/ZAR|5|1353.06, 1664.29, 1457.64, 1372.82, 1547.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_243|insurance/Household insurance/debit/ZAR|5|688.6, 688.6, 688.6, 688.6, 688.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_243|healthcare/Therapy appointment/debit/ZAR|5|1410.41, 1185.91, 1319.34, 1375.7, 1413.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_243|streaming/Streaming subscription/debit/ZAR|5|682, 682, 682, 682, 682|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_243|groceries/Fresh food shop/debit/ZAR|2|708.23, 884.86|repeated but not demonstrably recurrent|||
|user_243|groceries/Household groceries/debit/ZAR|3|991.1, 1117.22, 800.37|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_243|groceries/Weekly produce market/debit/ZAR|3|784.37, 1160.88, 931.08|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_243|groceries/Local market purchase/debit/ZAR|4|1004.14, 980.29, 908.21, 1017.96|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_243|groceries/Grocery delivery/debit/ZAR|3|1191.83, 966.97, 834.42|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_243|transport/Local taxi/debit/ZAR|5|558.84, 553.53, 399.97, 445.99, 494.71|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_243|transport/Metro and bus fares/debit/ZAR|2|560.82, 573.19|repeated but not demonstrably recurrent|||
|user_243|transport/Commuter pass/debit/ZAR|3|552.64, 497.69, 422.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_243|transport/Fuel refill/debit/ZAR|2|573.62, 570.59|repeated but not demonstrably recurrent|||
|user_243|dining/Coffee shop/debit/ZAR|3|775.07, 961.48, 853.77|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_243|dining/Takeaway order/debit/ZAR|3|615.77, 670.89, 739.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_243|dining/Family dinner/debit/ZAR|2|906.18, 888.1|repeated but not demonstrably recurrent|||
|user_243|dining/Bakery and snacks/debit/ZAR|2|794.27, 825.73|repeated but not demonstrably recurrent|||
|user_244|rent/Residential rent payment/debit/ZAR|6|18106, 18106, 18106, 18106, 18106, 18106|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_244|utilities/Household utility payment/debit/ZAR|5|2732.19, 2540.59, 3181.44, 3133.95, 2970.41|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_244|education/Course tuition/debit/ZAR|5|2945.8, 2945.8, 2945.8, 2945.8, 2945.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_244|debt_repayment/Vehicle loan payment/debit/ZAR|5|3289, 3289, 3289, 3289, 3289|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_244|music_subscription/Music subscription/debit/ZAR|5|441.1, 441.1, 441.1, 441.1, 441.1|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_244|delivery_membership/Delivery service plan/debit/ZAR|5|534.6, 534.6, 534.6, 534.6, 534.6|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_244|salary/First-job payroll/credit/ZAR|2|56760, 56760|repeated but not demonstrably recurrent|||
|user_244|groceries/Supermarket basket/debit/ZAR|4|1995.5, 2499.67, 2018.48, 2570.79|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_244|groceries/Neighbourhood grocer/debit/ZAR|4|1923.94, 1698.02, 1924.55, 2129.83|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_244|groceries/Local market purchase/debit/ZAR|6|2342.84, 2533.21, 2188.58, 1767.91, 2715.67, 1655.41|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_244|groceries/Grocery delivery/debit/ZAR|2|1768.02, 2498.12|repeated but not demonstrably recurrent|||
|user_244|groceries/Bulk pantry shop/debit/ZAR|4|1815.51, 2632.73, 2264.92, 1565.85|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_244|groceries/Household groceries/debit/ZAR|4|2099.91, 2206.97, 2739.85, 2303.02|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_244|transport/Local taxi/debit/ZAR|2|1653.45, 986.09|repeated but not demonstrably recurrent|||
|user_244|transport/Metro and bus fares/debit/ZAR|6|1708.31, 1705.17, 1612.16, 1333.68, 1470.91, 1427.7|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_244|transport/Parking and tolls/debit/ZAR|3|987.6, 1444.8, 993.68|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_244|transport/Commuter pass/debit/ZAR|4|1116.54, 1237.08, 1706.49, 1627.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_244|transport/Fuel refill/debit/ZAR|3|1338.43, 1127.39, 1538.2|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_244|transport/Vehicle charging/debit/ZAR|3|1497.55, 1044.43, 1403.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_244|transport/Rail pass/debit/ZAR|4|1073.13, 1151.71, 1183.26, 1538.99|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_244|dining/Weekend food delivery/debit/ZAR|2|2165.8, 3004.87|repeated but not demonstrably recurrent|||
|user_244|dining/Lunch with colleagues/debit/ZAR|3|1998.4, 2518.84, 2131.86|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_244|dining/Takeaway order/debit/ZAR|3|2931.99, 2664.82, 1803.69|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_244|dining/Neighbourhood restaurant/debit/ZAR|2|2365.28, 1735.73|repeated but not demonstrably recurrent|||
|user_245|salary/International employer payroll/credit/USD|5|139994.40, 139994.40, 139994.40, 139994.40, 139994.40|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_245|rent/Monthly rent/debit/INR|6|35400, 35400, 35400, 35400, 35400, 35400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_245|utilities/Household utility payment/debit/INR|5|7232.52, 7167.85, 6494.28, 7623.45, 6520.35|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_245|insurance/Household insurance/debit/INR|5|4010, 4010, 4010, 4010, 4010|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_245|cloud_storage/Online backup subscription/debit/INR|5|1120, 1120, 1120, 1120, 1120|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_245|streaming/Family streaming plan/debit/INR|5|3490, 3490, 3490, 3490, 3490|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_245|shopping/Household shopping/debit/INR|5|5799.63, 6613.91, 6594.52, 6174.58, 5539.09|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_245|entertainment/Cinema and events/debit/INR|5|3171.07, 3567.03, 3320.72, 3597.07, 3216.95|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_245|groceries/Local market purchase/debit/INR|6|6252.89, 3853.97, 6085.3, 5495.99, 6195.7, 5404.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_245|groceries/Grocery delivery/debit/INR|3|4219.54, 5263.49, 3785.08|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_245|groceries/Supermarket basket/debit/INR|2|4216.59, 6462.93|repeated but not demonstrably recurrent|||
|user_245|groceries/Fresh food shop/debit/INR|3|5241.28, 4211.02, 5681.23|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_245|transport/Metro and bus fares/debit/INR|7|2678.96, 3290.59, 3009.76, 3676.42, 3681.43, 3803.26, 3828.05|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_245|transport/Vehicle charging/debit/INR|8|2601.66, 3586.41, 3310.43, 3410.44, 3370.33, 2436.3, 2589.17, 3051.69|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_245|transport/Commuter pass/debit/INR|6|3846.68, 3424.78, 3514.14, 2339.22, 3692.1, 3310.67|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_245|transport/Local taxi/debit/INR|5|3798.97, 3247.7, 2643.5, 2261.55, 3168.86|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_245|transport/Rail pass/debit/INR|3|3240.09, 2536.01, 3099|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_245|transport/Ride-hailing trip/debit/INR|5|3160.03, 3882.06, 2933.19, 3231.96, 3074.73|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_245|dining/Quick-service meal/debit/INR|5|4045.38, 3460.88, 4560.81, 2998.27, 3744.09|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_245|dining/Coffee shop/debit/INR|3|4719.66, 3483.32, 4505.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_245|dining/Lunch with colleagues/debit/INR|5|4909.85, 3595.37, 4086.31, 3734.29, 3436.18|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_245|dining/Bakery and snacks/debit/INR|4|4668.68, 5011.96, 4980.96, 4678.38|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_245|dining/Neighbourhood restaurant/debit/INR|2|3335.99, 4049.86|repeated but not demonstrably recurrent|||
|user_245|dining/Weekend food delivery/debit/INR|2|4904.5, 3400.78|repeated but not demonstrably recurrent|||
|user_245|dining/Takeaway order/debit/INR|4|3351.31, 5023.99, 3202.58, 4357.08|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_246|salary/Payroll credit/credit/ZAR|4|50160, 50160, 50160, 50160|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_246|rent/Residential rent payment/debit/ZAR|5|14234, 14234, 14234, 14234, 14234|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_246|utilities/Electricity bill/debit/ZAR|5|3454.05, 3113.72, 3118.21, 3201.07, 3700.91|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_246|cloud_storage/Shared storage plan/debit/ZAR|5|218.9, 218.9, 218.9, 218.9, 218.9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_246|streaming/Video streaming plan/debit/ZAR|5|1218.8, 1218.8, 1218.8, 1218.8, 1218.8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_246|shopping/Clothing and household items/debit/ZAR|5|2570.28, 2444.69, 2153.22, 2205.73, 2486.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_246|groceries/Bulk pantry shop/debit/ZAR|2|1808.79, 1532.64|repeated but not demonstrably recurrent|||
|user_246|groceries/Neighbourhood grocer/debit/ZAR|3|2175.22, 2474.93, 1731.86|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_246|groceries/Supermarket basket/debit/ZAR|7|1505.24, 2560.38, 1832.94, 2403.02, 2101.15, 2042.85, 2544.53|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_246|groceries/Grocery delivery/debit/ZAR|2|2484.9, 2370.69|repeated but not demonstrably recurrent|||
|user_246|groceries/Local market purchase/debit/ZAR|2|2331.67, 2454.43|repeated but not demonstrably recurrent|||
|user_246|groceries/Fresh food shop/debit/ZAR|2|2375.18, 2409.04|repeated but not demonstrably recurrent|||
|user_246|transport/Vehicle charging/debit/ZAR|3|659.01, 721.94, 777.13|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_246|transport/Fuel refill/debit/ZAR|2|1124.14, 1122.46|repeated but not demonstrably recurrent|||
|user_246|dining/Takeaway order/debit/ZAR|3|1338.36, 1382.2, 1068.87|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_246|dining/Bakery and snacks/debit/ZAR|3|1521.07, 1829.72, 1757.91|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_247|salary/Payroll credit/credit/EUR|5|2123, 2123, 2123, 1528.56, 1528.56|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_247|rent/Landlord standing order/debit/EUR|6|434.5, 434.5, 434.5, 434.5, 434.5, 434.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_247|utilities/Water and power payment/debit/EUR|5|106.51, 105.99, 100.2, 89.84, 100.29|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_247|music_subscription/Music service subscription/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_247|delivery_membership/Food delivery membership/debit/EUR|5|12, 12, 12, 12, 12|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_247|gym/Fitness club membership/debit/EUR|5|43, 43, 43, 43, 43|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_247|entertainment/Local event tickets/debit/EUR|5|32.77, 33.71, 31.69, 31.94, 36.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_247|groceries/Household groceries/debit/EUR|4|83.6, 60.17, 73.23, 52.92|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_247|groceries/Fresh food shop/debit/EUR|3|78.37, 69.03, 69.88|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_247|groceries/Local market purchase/debit/EUR|3|78.66, 68.35, 66.99|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_247|groceries/Neighbourhood grocer/debit/EUR|4|73.69, 58.36, 75.56, 49.29|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_247|groceries/Grocery delivery/debit/EUR|4|75.62, 73.92, 61.53, 50.34|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_247|groceries/Weekly produce market/debit/EUR|2|79.41, 82.81|repeated but not demonstrably recurrent|||
|user_247|groceries/Bulk pantry shop/debit/EUR|4|60.15, 80.01, 69.32, 61.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_247|transport/Vehicle charging/debit/EUR|6|50.56, 43.91, 47.29, 49.2, 35.66, 49.76|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_247|transport/Commuter pass/debit/EUR|4|39.18, 33.44, 42.31, 48.3|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_247|transport/Fuel refill/debit/EUR|5|40.74, 41.9, 34.24, 33.78, 31.27|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_247|transport/Local taxi/debit/EUR|4|45.18, 30.34, 37.19, 33.66|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_247|transport/Rail pass/debit/EUR|4|48.34, 38.58, 37.88, 34.83|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_247|dining/Weekend food delivery/debit/EUR|2|37.19, 34.94|repeated but not demonstrably recurrent|||
|user_247|dining/Quick-service meal/debit/EUR|3|31.61, 30.8, 38.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_247|dining/Takeaway order/debit/EUR|3|50.06, 33.55, 46.7|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_247|dining/Bakery and snacks/debit/EUR|3|38.63, 30.45, 36.01|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_248|salary/Base salary/credit/USD|5|928.8, 928.8, 928.8, 928.8, 928.8|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_248|salary/Account commission payment/credit/USD|4|912.36, 233.22, 486.97, 563.01|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_248|rent/Apartment rent transfer/debit/USD|6|343.2, 343.2, 343.2, 343.2, 343.2, 343.2|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_248|utilities/Energy provider bill/debit/USD|6|85.75, 98.84, 89.08, 90.14, 90.24, 91.08|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_248|debt_repayment/Personal loan payment/debit/USD|5|236, 236, 236, 236, 236|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_248|healthcare/Therapy appointment/debit/USD|5|84.64, 80.61, 81.61, 92.43, 87.33|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_248|family_support/Parent support transfer/debit/USD|5|106, 106, 106, 106, 106|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_248|cloud_storage/Cloud storage plan/debit/USD|5|13, 13, 13, 13, 13|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_248|shopping/Monthly shopping spend/debit/USD|5|39.4, 38.52, 39.1, 40.5, 38.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Household groceries/debit/USD|4|59.75, 61.54, 66.53, 66|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Local market purchase/debit/USD|3|47.62, 59.62, 41.13|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Fresh food shop/debit/USD|6|60.23, 49.48, 69.95, 54.47, 47.84, 40.44|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Grocery delivery/debit/USD|3|63.73, 50.54, 60.09|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Supermarket basket/debit/USD|3|51.81, 70.83, 45.49|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Neighbourhood grocer/debit/USD|3|67.78, 41.23, 49.18|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_248|groceries/Weekly produce market/debit/USD|2|45.19, 67.02|repeated but not demonstrably recurrent|||
|user_248|groceries/Bulk pantry shop/debit/USD|2|45.2, 63.01|repeated but not demonstrably recurrent|||
|user_248|transport/Ride-hailing trip/debit/USD|2|24.62, 28.63|repeated but not demonstrably recurrent|||
|user_248|transport/Rail pass/debit/USD|3|40.91, 25.75, 36.94|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_248|transport/Commuter pass/debit/USD|2|38.17, 37.69|repeated but not demonstrably recurrent|||
|user_248|transport/Parking and tolls/debit/USD|2|38.56, 34.17|repeated but not demonstrably recurrent|||
|user_248|transport/Local taxi/debit/USD|2|30.57, 36.44|repeated but not demonstrably recurrent|||
|user_249|salary/Payroll credit/credit/USD|5|702, 702, 702, 702, 386.1|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_249|rent/Monthly rent/debit/USD|6|210, 210, 210, 210, 210, 210|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_249|utilities/Water and power payment/debit/USD|5|37.15, 35.73, 40.56, 40.3, 38.85|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_249|insurance/Vehicle insurance premium/debit/USD|5|34, 34, 34, 34, 34|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_249|cloud_storage/Shared storage plan/debit/USD|5|2, 2, 2, 2, 2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_249|streaming/Streaming subscription/debit/USD|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_249|shopping/Personal shopping/debit/USD|5|25.74, 26.22, 25.56, 30.99, 26.6|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_249|entertainment/Monthly entertainment spend/debit/USD|5|13.3, 13.97, 12.46, 12.02, 12.93|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_249|groceries/Fresh food shop/debit/USD|4|25.42, 20.77, 31.87, 25.11|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_249|groceries/Household groceries/debit/USD|3|30.53, 26.58, 19.05|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_249|groceries/Weekly produce market/debit/USD|2|25.31, 19|repeated but not demonstrably recurrent|||
|user_249|groceries/Bulk pantry shop/debit/USD|4|24.83, 21.8, 20.85, 20.51|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_249|groceries/Local market purchase/debit/USD|3|18.32, 23.06, 23.01|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_249|transport/Parking and tolls/debit/USD|8|16.31, 11.02, 17.25, 13.44, 13.02, 16.25, 16.3, 15.51|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_249|transport/Ride-hailing trip/debit/USD|2|11.67, 11.55|repeated but not demonstrably recurrent|||
|user_249|transport/Metro and bus fares/debit/USD|7|15.5, 14.2, 13.93, 13.91, 12.88, 17.2, 14.42|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_249|transport/Fuel refill/debit/USD|5|16.33, 11.98, 16.55, 11.18, 17.35|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_249|transport/Vehicle charging/debit/USD|5|17.51, 16.45, 13.76, 10.24, 17.22|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_249|transport/Rail pass/debit/USD|6|15.15, 17.83, 14.97, 16.86, 12.22, 17.89|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_249|transport/Local taxi/debit/USD|2|12, 12.74|repeated but not demonstrably recurrent|||
|user_249|dining/Coffee shop/debit/USD|4|18.47, 22.15, 13.96, 15.25|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_249|dining/Takeaway order/debit/USD|3|19.98, 15.67, 20.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_249|dining/Quick-service meal/debit/USD|2|17.38, 13.95|repeated but not demonstrably recurrent|||
|user_249|dining/Lunch with colleagues/debit/USD|5|14.22, 22.57, 23.4, 15.19, 14.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_249|dining/Neighbourhood restaurant/debit/USD|4|18.61, 14.12, 15.06, 15.16|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_249|dining/Bakery and snacks/debit/USD|4|18.71, 17.93, 22.61, 19.58|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_249|dining/Weekend food delivery/debit/USD|2|13.85, 13.7|repeated but not demonstrably recurrent|||
|user_250|salary/Previous employer payroll/credit/ZAR|4|53680, 53680, 53680, 53680|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_250|rent/Landlord standing order/debit/ZAR|6|15158, 15158, 15158, 15158, 15158, 15158|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_250|utilities/Household utility payment/debit/ZAR|5|3448.43, 2849.96, 3475.3, 2981.68, 3117.92|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_250|debt_repayment/Personal loan payment/debit/ZAR|5|7579, 7579, 7579, 7579, 7579|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_250|music_subscription/Music service subscription/debit/ZAR|5|360.8, 360.8, 360.8, 360.8, 360.8|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_250|groceries/Fresh food shop/debit/ZAR|3|2065.15, 1839.89, 1984.65|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_250|groceries/Bulk pantry shop/debit/ZAR|3|1741.72, 1737.24, 2397.09|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_250|groceries/Household groceries/debit/ZAR|2|2281.76, 2620.39|repeated but not demonstrably recurrent|||
|user_250|groceries/Neighbourhood grocer/debit/ZAR|2|2918.84, 1705.57|repeated but not demonstrably recurrent|||
|user_250|transport/Parking and tolls/debit/ZAR|3|1431.23, 1613.8, 1179.51|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_250|transport/Vehicle charging/debit/ZAR|3|1793.01, 1568.65, 1244.81|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_250|dining/Bakery and snacks/debit/ZAR|4|2074.38, 1561.1, 1726.18, 1997.65|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_250|dining/Weekend food delivery/debit/ZAR|2|2404.19, 2264.27|repeated but not demonstrably recurrent|||
|user_250|dining/Family dinner/debit/ZAR|2|2416.75, 2437.53|repeated but not demonstrably recurrent|||
|user_251|salary/Delivery platform payout/credit/EUR|4|447.45, 403.32, 423.28, 487.62|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_251|salary/Driver platform payout/credit/EUR|9|489.79, 284.5, 408.65, 263.49, 383.35, 362.56, 392.79, 373.23, 238.52|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_251|rent/Apartment rent transfer/debit/EUR|5|401.5, 401.5, 401.5, 401.5, 401.5|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_251|utilities/Electricity bill/debit/EUR|5|106.73, 107.91, 89.58, 102.52, 103.74|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_251|music_subscription/Music subscription/debit/EUR|5|18, 18, 18, 18, 18|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_251|delivery_membership/Food delivery membership/debit/EUR|5|23, 23, 23, 23, 23|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_251|gym/Fitness club membership/debit/EUR|5|32, 32, 32, 32, 32|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_251|entertainment/Monthly entertainment spend/debit/EUR|5|42.53, 45.99, 45.68, 48.66, 47.64|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_251|salary/Weekly app earnings/credit/EUR|2|385.56, 468.97|repeated but not demonstrably recurrent|||
|user_251|salary/Task marketplace payout/credit/EUR|5|295.7, 407.01, 233.9, 412.26, 245.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_251|groceries/Local market purchase/debit/EUR|9|43.38, 55.92, 39.46, 61.27, 46.89, 61.79, 64.22, 62.13, 56.46|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_251|groceries/Weekly produce market/debit/EUR|3|58.14, 52.89, 39.95|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_251|groceries/Grocery delivery/debit/EUR|3|51.36, 49.58, 55.1|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_251|groceries/Fresh food shop/debit/EUR|3|53.35, 53.99, 50.35|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_251|groceries/Supermarket basket/debit/EUR|4|38.52, 60.76, 59.14, 50.03|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_251|groceries/Household groceries/debit/EUR|2|38.78, 53.16|repeated but not demonstrably recurrent|||
|user_251|transport/Metro and bus fares/debit/EUR|2|22.7, 31.37|repeated but not demonstrably recurrent|||
|user_251|transport/Ride-hailing trip/debit/EUR|5|33.44, 26.66, 27.34, 31.13, 30.17|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_251|transport/Local taxi/debit/EUR|2|28.38, 23.8|repeated but not demonstrably recurrent|||
|user_251|transport/Vehicle charging/debit/EUR|3|34.35, 28.65, 31.67|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_251|transport/Commuter pass/debit/EUR|3|25.26, 31.54, 23.06|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_251|transport/Parking and tolls/debit/EUR|5|20.5, 21.66, 22.43, 33.59, 27.94|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_251|transport/Rail pass/debit/EUR|3|27.76, 22.96, 29.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_251|transport/Fuel refill/debit/EUR|2|21.24, 31.64|repeated but not demonstrably recurrent|||
|user_251|dining/Neighbourhood restaurant/debit/EUR|2|53.46, 63.8|repeated but not demonstrably recurrent|||
|user_251|dining/Family dinner/debit/EUR|2|39.66, 40.9|repeated but not demonstrably recurrent|||
|user_251|dining/Weekend food delivery/debit/EUR|3|67.51, 65.63, 43.82|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_251|dining/Quick-service meal/debit/EUR|4|44.81, 51.52, 44.05, 38.63|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_251|dining/Coffee shop/debit/EUR|2|67.55, 41.1|repeated but not demonstrably recurrent|||
|user_252|salary/Payroll credit/credit/IDR|5|19760000, 19760000, 19760000, 19760000, 19760000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_252|housing/Property maintenance contribution/debit/IDR|6|1453500, 1453500, 1453500, 1453500, 1453500, 1453500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_252|utilities/Household utility payment/debit/IDR|5|865272.87, 897363.38, 901530.66, 1001208.64, 937150.9|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_252|insurance/Health insurance premium/debit/IDR|5|685900, 685900, 685900, 685900, 685900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_252|healthcare/Therapy appointment/debit/IDR|5|1218822.21, 1176631.52, 1217794.69, 1164150.18, 1395289.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_252|streaming/Video streaming plan/debit/IDR|5|372400, 372400, 372400, 372400, 372400|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_252|groceries/Weekly produce market/debit/IDR|2|853990.45, 904717.64|repeated but not demonstrably recurrent|||
|user_252|groceries/Neighbourhood grocer/debit/IDR|4|721672.08, 748421.8, 706284.36, 856819.07|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_252|groceries/Grocery delivery/debit/IDR|4|565504.88, 879234.03, 900759.15, 738165.06|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_252|groceries/Supermarket basket/debit/IDR|4|749176.87, 717402.15, 721610.86, 653155.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_252|groceries/Local market purchase/debit/IDR|2|726004.31, 674194.81|repeated but not demonstrably recurrent|||
|user_252|transport/Metro and bus fares/debit/IDR|2|314820.68, 525346.53|repeated but not demonstrably recurrent|||
|user_252|transport/Local taxi/debit/IDR|4|314184.82, 448959.87, 321798.87, 308746.92|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_252|transport/Fuel refill/debit/IDR|2|459858.68, 466321.18|repeated but not demonstrably recurrent|||
|user_252|transport/Vehicle charging/debit/IDR|2|306021.3, 519462.42|repeated but not demonstrably recurrent|||
|user_252|dining/Lunch with colleagues/debit/IDR|2|597407.32, 898283.63|repeated but not demonstrably recurrent|||
|user_252|dining/Coffee shop/debit/IDR|3|536945.69, 850141, 768917.38|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_252|dining/Neighbourhood restaurant/debit/IDR|3|701354.02, 761038.18, 844791|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_253|salary/Payroll credit/credit/EUR|5|2860, 2860, 2860, 2860, 2860|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_253|rent/Monthly rent/debit/EUR|6|883.3, 883.3, 883.3, 883.3, 883.3, 883.3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_253|utilities/Electricity bill/debit/EUR|6|185.42, 206.5, 213.78, 188.44, 175.52, 186.2|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_253|debt_repayment/Loan repayment/debit/EUR|5|324, 324, 324, 324, 324|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_253|streaming/Streaming subscription/debit/EUR|5|86, 86, 86, 86, 86|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_253|cloud_storage/Cloud storage plan/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_253|shopping/Household shopping/debit/EUR|5|79.11, 90.41, 81.88, 82.07, 80.61|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Local market purchase/debit/EUR|4|115.01, 116.38, 111.33, 111.05|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Grocery delivery/debit/EUR|4|109.45, 125.89, 105.26, 99.71|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Fresh food shop/debit/EUR|5|91.31, 128.14, 131.16, 84.69, 102.24|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Bulk pantry shop/debit/EUR|3|119.41, 110.48, 125.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Neighbourhood grocer/debit/EUR|4|138.84, 93.17, 96.22, 107.59|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Weekly produce market/debit/EUR|3|118.73, 130.07, 133.95|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_253|groceries/Household groceries/debit/EUR|2|106.71, 112.74|repeated but not demonstrably recurrent|||
|user_253|transport/Parking and tolls/debit/EUR|7|40.63, 47.36, 57.9, 47.62, 46.28, 68.61, 62.35|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_253|transport/Ride-hailing trip/debit/EUR|2|43.52, 53.72|repeated but not demonstrably recurrent|||
|user_253|transport/Fuel refill/debit/EUR|7|53.57, 52.7, 48.45, 59.36, 45.56, 47.76, 65.3|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_253|transport/Rail pass/debit/EUR|2|52.97, 46.86|repeated but not demonstrably recurrent|||
|user_253|transport/Metro and bus fares/debit/EUR|3|70.21, 52.58, 42.46|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_253|transport/Commuter pass/debit/EUR|3|42.67, 53.76, 70.19|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_253|dining/Bakery and snacks/debit/EUR|3|84.9, 114.2, 80.94|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_253|dining/Quick-service meal/debit/EUR|4|111.8, 108.29, 92.92, 101.57|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_253|dining/Takeaway order/debit/EUR|3|79.97, 105.87, 104.73|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_253|dining/Neighbourhood restaurant/debit/EUR|2|94.27, 115.44|repeated but not demonstrably recurrent|||
|user_254|salary/Payroll credit/credit/USD|5|2808, 2808, 2808, 2808, 2808|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_254|housing/Property maintenance contribution/debit/USD|5|244, 244, 244, 244, 244|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_254|utilities/Electricity bill/debit/USD|5|188.74, 167.3, 170.23, 182.34, 175.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_254|insurance/Insurance policy payment/debit/USD|5|118, 118, 118, 118, 118|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_254|education/School fee payment/debit/USD|5|236, 236, 236, 236, 236|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_254|healthcare/Diagnostic test/debit/USD|5|140.44, 139.01, 144.61, 132.82, 140.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_254|entertainment/Local event tickets/debit/USD|5|106.67, 94.34, 95.55, 108.48, 110.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_254|cloud_storage/Cloud storage plan/debit/USD|5|21, 21, 21, 21, 21|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_254|groceries/Neighbourhood grocer/debit/USD|4|102.03, 146.71, 152.41, 95.16|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_254|groceries/Weekly produce market/debit/USD|2|129.74, 118.94|repeated but not demonstrably recurrent|||
|user_254|groceries/Bulk pantry shop/debit/USD|4|89.37, 144.5, 100.64, 121.28|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_254|groceries/Household groceries/debit/USD|2|110.91, 149.01|repeated but not demonstrably recurrent|||
|user_254|groceries/Fresh food shop/debit/USD|3|88.52, 147.5, 134.3|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_254|transport/Metro and bus fares/debit/USD|2|68.25, 83.02|repeated but not demonstrably recurrent|||
|user_254|transport/Fuel refill/debit/USD|2|54.58, 50.09|repeated but not demonstrably recurrent|||
|user_254|transport/Parking and tolls/debit/USD|3|49.29, 52.32, 69.04|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_254|transport/Commuter pass/debit/USD|2|78.85, 73.25|repeated but not demonstrably recurrent|||
|user_254|transport/Local taxi/debit/USD|2|53.36, 62.48|repeated but not demonstrably recurrent|||
|user_254|dining/Weekend food delivery/debit/USD|2|65.05, 65.07|repeated but not demonstrably recurrent|||
|user_254|dining/Coffee shop/debit/USD|2|81.52, 64.39|repeated but not demonstrably recurrent|||
|user_254|dining/Quick-service meal/debit/USD|3|86.41, 77.23, 81.54|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_255|salary/Payroll credit/credit/IDR|4|16530000, 16530000, 16530000, 16530000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_255|rent/Residential rent payment/debit/IDR|6|3838000, 3838000, 3838000, 3838000, 3838000, 3838000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_255|utilities/Municipal utilities/debit/IDR|5|1012249.59, 1172920.97, 1179687.44, 958054.21, 967473.02|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_255|cloud_storage/Online backup subscription/debit/IDR|5|122550, 122550, 122550, 122550, 122550|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_255|streaming/Streaming subscription/debit/IDR|5|406600, 406600, 406600, 406600, 406600|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_255|shopping/Online retail purchases/debit/IDR|5|349586.56, 333581.77, 347834.83, 328485.06, 334004.68|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_255|groceries/Household groceries/debit/IDR|5|867740.47, 678657.18, 760350.87, 604019.39, 611662.54|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_255|groceries/Supermarket basket/debit/IDR|2|841420.67, 785447.69|repeated but not demonstrably recurrent|||
|user_255|groceries/Local market purchase/debit/IDR|3|693907.25, 735298.07, 742704.01|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_255|groceries/Grocery delivery/debit/IDR|2|760959.58, 654376.72|repeated but not demonstrably recurrent|||
|user_255|groceries/Bulk pantry shop/debit/IDR|2|752796.55, 607093.41|repeated but not demonstrably recurrent|||
|user_255|groceries/Fresh food shop/debit/IDR|2|810705.23, 748602.21|repeated but not demonstrably recurrent|||
|user_255|transport/Fuel refill/debit/IDR|4|282862.76, 373032.25, 455543.6, 495948.9|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_255|transport/Commuter pass/debit/IDR|3|302537.56, 411281.43, 481115.36|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_255|dining/Takeaway order/debit/IDR|4|521819.83, 508323.48, 644455.53, 857439.86|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_255|dining/Quick-service meal/debit/IDR|2|686948.39, 516996.33|repeated but not demonstrably recurrent|||
|user_255|dining/Lunch with colleagues/debit/IDR|2|623860.02, 640348.6|repeated but not demonstrably recurrent|||
|user_256|rent/Monthly rent/debit/INR|6|56600, 56600, 56600, 56600, 56600, 56600|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_256|utilities/Electricity bill/debit/INR|5|12532.23, 10122.12, 11848.67, 10020.25, 12467.76|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_256|education/Course tuition/debit/INR|5|12160, 12160, 12160, 12160, 12160|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_256|debt_repayment/Loan repayment/debit/INR|5|15600, 15600, 15600, 15600, 15600|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_256|music_subscription/Audio streaming plan/debit/INR|5|2415, 2415, 2415, 2415, 2415|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_256|delivery_membership/Delivery service plan/debit/INR|5|3525, 3525, 3525, 3525, 3525|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_256|salary/First-job payroll/credit/INR|2|214000, 214000|repeated but not demonstrably recurrent|||
|user_256|groceries/Bulk pantry shop/debit/INR|5|11199.93, 8273.86, 6907.77, 9454.87, 7268.62|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_256|groceries/Fresh food shop/debit/INR|5|10482.76, 11226.94, 6495.04, 10761.05, 9892.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_256|groceries/Neighbourhood grocer/debit/INR|3|9240.8, 7527.83, 7137.74|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_256|groceries/Supermarket basket/debit/INR|3|9596.4, 7035.31, 11015.27|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_256|groceries/Grocery delivery/debit/INR|5|9081.63, 6689.69, 7279.62, 6513.64, 6729.06|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_256|groceries/Household groceries/debit/INR|3|8508.11, 11112.22, 8740.4|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_256|transport/Ride-hailing trip/debit/INR|2|4301.97, 4604.18|repeated but not demonstrably recurrent|||
|user_256|transport/Parking and tolls/debit/INR|5|3839.92, 3300.02, 3114.77, 4307.38, 3956.53|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_256|transport/Vehicle charging/debit/INR|4|4393.98, 3275.35, 4059.96, 3676.24|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_256|transport/Rail pass/debit/INR|2|3611.06, 2847.48|repeated but not demonstrably recurrent|||
|user_256|transport/Commuter pass/debit/INR|5|3377.22, 3405.97, 3197.21, 4857.65, 3364.43|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_256|transport/Fuel refill/debit/INR|2|4903.35, 4747.38|repeated but not demonstrably recurrent|||
|user_256|transport/Metro and bus fares/debit/INR|4|4862.89, 3633.08, 3193.76, 4042.75|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_256|transport/Local taxi/debit/INR|2|3411.86, 2839.35|repeated but not demonstrably recurrent|||
|user_256|dining/Lunch with colleagues/debit/INR|3|8401.33, 8041.28, 8240.48|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_256|dining/Family dinner/debit/INR|2|7768.93, 8747.63|repeated but not demonstrably recurrent|||
|user_256|dining/Weekend food delivery/debit/INR|3|6050.1, 5591.67, 8456.74|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_256|dining/Coffee shop/debit/INR|2|5146.86, 5357.14|repeated but not demonstrably recurrent|||
|user_257|salary/International employer payroll/credit/EUR|5|1954.37, 1954.37, 1954.37, 1954.37, 1954.37|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_257|rent/Apartment rent transfer/debit/USD|6|540, 540, 540, 540, 540, 540|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_257|utilities/Water and power payment/debit/USD|5|128.13, 138.06, 119.37, 129, 128.07|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_257|insurance/Health insurance premium/debit/USD|5|82, 82, 82, 82, 82|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_257|cloud_storage/Cloud storage plan/debit/USD|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_257|streaming/Video streaming plan/debit/USD|5|48, 48, 48, 48, 48|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_257|shopping/Household shopping/debit/USD|5|76.65, 70.59, 80.09, 71.56, 84.46|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_257|entertainment/Games and recreation/debit/USD|5|74.51, 72.26, 75.78, 73.11, 84.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_257|groceries/Bulk pantry shop/debit/USD|3|88.71, 98.27, 63.08|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_257|groceries/Local market purchase/debit/USD|2|73.92, 98.32|repeated but not demonstrably recurrent|||
|user_257|groceries/Weekly produce market/debit/USD|2|96.78, 81.55|repeated but not demonstrably recurrent|||
|user_257|groceries/Fresh food shop/debit/USD|5|92.69, 83.43, 65.57, 67.03, 97.37|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_257|groceries/Neighbourhood grocer/debit/USD|2|82.56, 65.26|repeated but not demonstrably recurrent|||
|user_257|groceries/Grocery delivery/debit/USD|2|80.47, 81.2|repeated but not demonstrably recurrent|||
|user_257|transport/Local taxi/debit/USD|4|47.59, 46.93, 60.41, 56.07|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Commuter pass/debit/USD|5|55.25, 46, 49.01, 37.03, 50.12|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Metro and bus fares/debit/USD|8|44.24, 48.06, 45.12, 35.91, 45.36, 43.07, 42.54, 38.55|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Rail pass/debit/USD|5|40.06, 39.13, 38.29, 35.8, 43.08|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Vehicle charging/debit/USD|3|60.76, 62.5, 50.87|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Fuel refill/debit/USD|4|49.01, 47.94, 56.44, 38.98|variable but recurrent|55|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Ride-hailing trip/debit/USD|4|38.76, 44.51, 62.12, 35.49|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_257|transport/Parking and tolls/debit/USD|3|49.01, 42.7, 35.31|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_257|dining/Coffee shop/debit/USD|5|74.85, 64.78, 103.33, 90.57, 109.87|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_257|dining/Weekend food delivery/debit/USD|6|87.56, 99.85, 88.12, 66.72, 93.79, 90.8|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_257|dining/Bakery and snacks/debit/USD|7|75.96, 90.14, 97.42, 89.76, 105.67, 63.02, 63.03|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_257|dining/Family dinner/debit/USD|3|84.13, 82.22, 64.64|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_257|dining/Neighbourhood restaurant/debit/USD|2|82.64, 62.85|repeated but not demonstrably recurrent|||
|user_258|salary/Primary household salary/credit/USD|5|572.88, 572.88, 572.88, 572.88, 572.88|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_258|salary/Second household income/credit/USD|4|414.52, 369.04, 404.79, 367.09|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_258|rent/Apartment rent transfer/debit/USD|6|242.4, 242.4, 242.4, 242.4, 242.4, 242.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_258|utilities/Water and power payment/debit/USD|5|66.5, 61.65, 59.11, 62.12, 55.73|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_258|insurance/Health insurance premium/debit/USD|5|42, 42, 42, 42, 42|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_258|cloud_storage/Cloud storage plan/debit/USD|5|8, 8, 8, 8, 8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_258|streaming/Family streaming plan/debit/USD|5|22, 22, 22, 22, 22|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_258|shopping/Online retail purchases/debit/USD|5|30.2, 27.04, 29.73, 25.62, 26.87|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_258|entertainment/Monthly entertainment spend/debit/USD|5|32.24, 31.71, 31.23, 29.28, 28.98|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_258|groceries/Household groceries/debit/USD|3|34.57, 50.87, 38.75|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_258|groceries/Bulk pantry shop/debit/USD|3|40.36, 35.01, 35.42|variable but recurrent|60|RECURRING_AMOUNT_UNRESOLVED|
|user_258|groceries/Weekly produce market/debit/USD|4|45.75, 42.74, 40.52, 32.45|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_258|groceries/Neighbourhood grocer/debit/USD|4|33.13, 51.12, 51.27, 38.8|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_258|groceries/Local market purchase/debit/USD|2|35.92, 40.97|repeated but not demonstrably recurrent|||
|user_258|transport/Commuter pass/debit/USD|3|16.52, 18.52, 20.03|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_258|transport/Rail pass/debit/USD|8|26.5, 21.75, 26.84, 18.78, 21.73, 24.55, 20.01, 20.35|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_258|transport/Vehicle charging/debit/USD|5|15.83, 23.3, 16.06, 20.87, 24.64|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_258|transport/Metro and bus fares/debit/USD|6|20.58, 18.8, 18.96, 23.88, 19.37, 24.3|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_258|transport/Parking and tolls/debit/USD|6|17.32, 22.2, 22.4, 25.45, 15.17, 25.19|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_258|transport/Ride-hailing trip/debit/USD|2|20.36, 22.3|repeated but not demonstrably recurrent|||
|user_258|transport/Fuel refill/debit/USD|3|17.27, 16.92, 20.37|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_258|transport/Local taxi/debit/USD|2|21.06, 21.04|repeated but not demonstrably recurrent|||
|user_258|dining/Weekend food delivery/debit/USD|5|43.7, 31.23, 30.14, 48.36, 36.52|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_258|dining/Quick-service meal/debit/USD|3|48.03, 38.28, 48.51|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_258|dining/Neighbourhood restaurant/debit/USD|3|42.52, 37.78, 44.3|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_258|dining/Family dinner/debit/USD|3|34.26, 32.34, 41.5|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_258|dining/Takeaway order/debit/USD|2|45.31, 39.52|repeated but not demonstrably recurrent|||
|user_258|dining/Coffee shop/debit/USD|2|49.65, 40.05|repeated but not demonstrably recurrent|||
|user_258|dining/Bakery and snacks/debit/USD|5|46.61, 40.93, 35.4, 36.65, 30.4|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_258|dining/Lunch with colleagues/debit/USD|2|36.64, 31.4|repeated but not demonstrably recurrent|||
|user_259|salary/Payroll credit/credit/EUR|5|792, 792, 792, 792, 792|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_259|rent/Monthly rent/debit/EUR|5|240.9, 240.9, 240.9, 240.9, 240.9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_259|utilities/Municipal utilities/debit/EUR|5|41.94, 39.93, 37.95, 46.4, 39.44|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_259|debt_repayment/Personal loan payment/debit/EUR|5|91, 91, 91, 91, 91|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_259|music_subscription/Audio streaming plan/debit/EUR|5|7, 7, 7, 7, 7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_259|groceries/Household groceries/debit/EUR|4|28.58, 32.1, 31.11, 42.39|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_259|groceries/Bulk pantry shop/debit/EUR|2|30.04, 29.31|repeated but not demonstrably recurrent|||
|user_259|groceries/Weekly produce market/debit/EUR|4|39.16, 34.49, 33.19, 41.98|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_259|groceries/Neighbourhood grocer/debit/EUR|2|42.96, 36.86|repeated but not demonstrably recurrent|||
|user_259|transport/Parking and tolls/debit/EUR|2|23.83, 21.93|repeated but not demonstrably recurrent|||
|user_259|transport/Local taxi/debit/EUR|2|22.96, 22.39|repeated but not demonstrably recurrent|||
|user_259|transport/Fuel refill/debit/EUR|2|18.98, 22.66|repeated but not demonstrably recurrent|||
|user_259|dining/Takeaway order/debit/EUR|3|34.6, 43.49, 40.48|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_259|dining/Family dinner/debit/EUR|2|25.65, 41.15|repeated but not demonstrably recurrent|||
|user_259|dining/Lunch with colleagues/debit/EUR|2|28.41, 31.82|repeated but not demonstrably recurrent|||
|user_260|salary/International employer payroll/credit/USD|5|29259993.84, 29259993.84, 29259993.84, 29259993.84, 29259993.84|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_260|rent/Landlord standing order/debit/IDR|6|8436000, 8436000, 8436000, 8436000, 8436000, 8436000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_260|utilities/Electricity and water bill/debit/IDR|6|1513544.02, 1361516.99, 1335669.78, 1360722.74, 1401346.97, 1387636.09|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_260|insurance/Vehicle insurance premium/debit/IDR|5|834100, 834100, 834100, 834100, 834100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_260|cloud_storage/Online backup subscription/debit/IDR|5|248900, 248900, 248900, 248900, 248900|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_260|streaming/Video streaming plan/debit/IDR|5|627000, 627000, 627000, 627000, 627000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_260|shopping/Online retail purchases/debit/IDR|5|1158203.42, 1091724.51, 1155009.38, 1217772.81, 1330372.23|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_260|entertainment/Cinema and events/debit/IDR|5|714235.64, 578152.38, 724281.68, 699204.83, 685291.53|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_260|groceries/Household groceries/debit/IDR|2|865077.88, 1022209.96|repeated but not demonstrably recurrent|||
|user_260|groceries/Neighbourhood grocer/debit/IDR|4|1332582.42, 871805.8, 1104509.54, 1228170.8|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_260|groceries/Grocery delivery/debit/IDR|2|822816.41, 1097684.39|repeated but not demonstrably recurrent|||
|user_260|groceries/Bulk pantry shop/debit/IDR|2|1117310.96, 1224801.56|repeated but not demonstrably recurrent|||
|user_260|groceries/Fresh food shop/debit/IDR|3|832841.78, 907440.73, 1241677.18|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_260|groceries/Weekly produce market/debit/IDR|2|926316.49, 977514.52|repeated but not demonstrably recurrent|||
|user_260|groceries/Local market purchase/debit/IDR|2|817553.43, 1247124.71|repeated but not demonstrably recurrent|||
|user_260|transport/Fuel refill/debit/IDR|7|582360.34, 650007.8, 714068.9, 638311.63, 614346.06, 668670.58, 556523.53|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_260|transport/Vehicle charging/debit/IDR|2|494416.39, 698109.99|repeated but not demonstrably recurrent|||
|user_260|transport/Commuter pass/debit/IDR|4|733549.73, 679642.43, 648060.44, 587871.85|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_260|transport/Ride-hailing trip/debit/IDR|8|692607.71, 564722.17, 670306.48, 699166.35, 730285.4, 680868.39, 612668.58, 682856.53|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_260|transport/Metro and bus fares/debit/IDR|6|830414.89, 597618.35, 531178.87, 753716.25, 493772.22, 562113.29|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_260|transport/Parking and tolls/debit/IDR|6|483132.05, 568084.71, 752813.43, 766539.46, 710795, 770358.48|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_260|transport/Local taxi/debit/IDR|2|552176.35, 734471.33|repeated but not demonstrably recurrent|||
|user_260|dining/Neighbourhood restaurant/debit/IDR|4|1475443.71, 1106402.94, 921226.93, 1274236.25|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_260|dining/Takeaway order/debit/IDR|4|957034.08, 956366.83, 1319861.24, 1237493.08|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_260|dining/Quick-service meal/debit/IDR|5|1480391.11, 1423558.21, 1434565.96, 1446204.89, 1447652.11|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_260|dining/Weekend food delivery/debit/IDR|4|1492572.69, 1246344.88, 1149212.86, 1218343.4|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_260|dining/Bakery and snacks/debit/IDR|3|1083835.61, 1237374.03, 1406574.66|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_260|dining/Lunch with colleagues/debit/IDR|2|1054313.35, 1108539.81|repeated but not demonstrably recurrent|||
|user_260|dining/Coffee shop/debit/IDR|2|877809.17, 1251147.88|repeated but not demonstrably recurrent|||
|user_260|dining/Family dinner/debit/IDR|2|1129688.97, 1111877.06|repeated but not demonstrably recurrent|||
|user_261|salary/Payroll credit/credit/EUR|5|2684, 2684, 2684, 2684, 2684|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_261|housing/Home repair reserve/debit/EUR|5|301, 301, 301, 301, 301|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_261|utilities/Electricity bill/debit/EUR|5|153.67, 183.63, 166.2, 164.7, 148.94|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_261|insurance/Health insurance premium/debit/EUR|5|88, 88, 88, 88, 88|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_261|healthcare/Family healthcare expense/debit/EUR|5|142.83, 167.33, 168.33, 147.05, 154.78|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_261|streaming/Family streaming plan/debit/EUR|5|51, 51, 51, 51, 51|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_261|groceries/Supermarket basket/debit/EUR|3|102.12, 90.44, 103.87|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_261|groceries/Household groceries/debit/EUR|6|106.04, 89.01, 123.73, 78.47, 96.69, 82.66|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_261|groceries/Grocery delivery/debit/EUR|4|126.47, 86.08, 123.98, 89.76|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_261|groceries/Weekly produce market/debit/EUR|2|112.53, 110|repeated but not demonstrably recurrent|||
|user_261|transport/Local taxi/debit/EUR|2|58.47, 53.57|repeated but not demonstrably recurrent|||
|user_261|transport/Parking and tolls/debit/EUR|2|78.22, 77.05|repeated but not demonstrably recurrent|||
|user_261|transport/Fuel refill/debit/EUR|2|77.43, 52.42|repeated but not demonstrably recurrent|||
|user_261|transport/Metro and bus fares/debit/EUR|2|47.37, 66.07|repeated but not demonstrably recurrent|||
|user_261|transport/Rail pass/debit/EUR|2|66.02, 69.05|repeated but not demonstrably recurrent|||
|user_261|dining/Neighbourhood restaurant/debit/EUR|2|82.55, 120.37|repeated but not demonstrably recurrent|||
|user_261|dining/Family dinner/debit/EUR|3|81.57, 113.13, 92.5|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_261|dining/Weekend food delivery/debit/EUR|2|77.51, 101.32|repeated but not demonstrably recurrent|||
|user_261|dining/Bakery and snacks/debit/EUR|4|81.65, 120.38, 94.99, 91.14|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_262|salary/Primary household salary/credit/IDR|5|29921200, 29921200, 29921200, 29921200, 29921200|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_262|salary/Second household income/credit/IDR|4|22714908.49, 18377907.14, 21064928.29, 20526620.46|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_262|rent/Landlord standing order/debit/IDR|6|13452000, 13452000, 13452000, 13452000, 13452000, 13452000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_262|utilities/Household utility payment/debit/IDR|5|2471314.05, 2662460.23, 2461506.79, 2647513.06, 2475234.6|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_262|debt_repayment/Loan repayment/debit/IDR|5|7951500, 7951500, 7951500, 7951500, 7951500|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_262|streaming/Video streaming plan/debit/IDR|5|1083000, 1083000, 1083000, 1083000, 1083000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_262|cloud_storage/Shared storage plan/debit/IDR|5|343900, 343900, 343900, 343900, 343900|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_262|shopping/Household shopping/debit/IDR|5|1405454.44, 1469924.66, 1240936.11, 1492159.53, 1310015.03|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_262|groceries/Bulk pantry shop/debit/IDR|3|1954462.56, 1679212.62, 2012688.71|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_262|groceries/Weekly produce market/debit/IDR|7|1988486.01, 2065641.65, 1704914.5, 2143092.09, 2028917.62, 1326574.95, 1422703.23|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_262|groceries/Grocery delivery/debit/IDR|3|2090205.91, 1717384.53, 2086113.98|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_262|groceries/Local market purchase/debit/IDR|4|1282180.34, 1761463.63, 1665010.51, 1465361.51|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_262|groceries/Supermarket basket/debit/IDR|2|1522200.89, 2014319.22|repeated but not demonstrably recurrent|||
|user_262|groceries/Household groceries/debit/IDR|3|1826715.05, 2097173.16, 2225313|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_262|groceries/Fresh food shop/debit/IDR|3|1467279.21, 1820422.76, 2159759.07|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_262|transport/Fuel refill/debit/IDR|4|1147389.62, 814517.01, 1127348.53, 845521.63|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_262|transport/Parking and tolls/debit/IDR|6|1287363.47, 1025859.92, 1169610.06, 880460.77, 867068.29, 1063419.17|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_262|transport/Local taxi/debit/IDR|2|1313785.17, 1017512.59|repeated but not demonstrably recurrent|||
|user_262|transport/Rail pass/debit/IDR|3|896271.85, 895871.38, 1400584.49|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_262|transport/Metro and bus fares/debit/IDR|4|1243926.34, 1030786.66, 1289197.99, 1352026.88|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_262|transport/Commuter pass/debit/IDR|2|939446.85, 1191380.75|repeated but not demonstrably recurrent|||
|user_262|transport/Ride-hailing trip/debit/IDR|4|988697.29, 1289155.32, 972537.65, 965332.34|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_262|dining/Neighbourhood restaurant/debit/IDR|4|1884774.87, 1755808.89, 1729305.77, 1238012.34|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_262|dining/Quick-service meal/debit/IDR|2|1439870.4, 1287249.7|repeated but not demonstrably recurrent|||
|user_262|dining/Lunch with colleagues/debit/IDR|3|1426748.83, 1484566.13, 1248579.32|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_262|dining/Bakery and snacks/debit/IDR|2|1592357.9, 1638396.17|repeated but not demonstrably recurrent|||
|user_263|salary/International employer payroll/credit/EUR|5|29700, 29700, 29700, 29700, 29700|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_263|rent/Apartment rent transfer/debit/ZAR|6|9174, 9174, 9174, 9174, 9174, 9174|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_263|utilities/Household utility payment/debit/ZAR|5|1263.45, 1382.56, 1528.66, 1256.95, 1472.99|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_263|insurance/Vehicle insurance premium/debit/ZAR|5|781, 781, 781, 781, 781|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_263|cloud_storage/Online backup subscription/debit/ZAR|5|92.4, 92.4, 92.4, 92.4, 92.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_263|streaming/Family streaming plan/debit/ZAR|5|798.6, 798.6, 798.6, 798.6, 798.6|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_263|shopping/Clothing and household items/debit/ZAR|5|1216.17, 1395.41, 1381.8, 1173.14, 1281.05|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_263|entertainment/Monthly entertainment spend/debit/ZAR|5|896.3, 947.45, 792.85, 855.18, 855.98|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_263|groceries/Bulk pantry shop/debit/ZAR|3|1079.97, 1071.95, 1115.66|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_263|groceries/Supermarket basket/debit/ZAR|5|1372.51, 931.35, 1600.07, 1594.95, 1597.45|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_263|groceries/Household groceries/debit/ZAR|2|1326.52, 1298.11|repeated but not demonstrably recurrent|||
|user_263|groceries/Fresh food shop/debit/ZAR|3|1004.62, 1389.09, 1601.61|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_263|groceries/Local market purchase/debit/ZAR|3|1235.38, 1101.96, 1178.6|variable but recurrent|40|RECURRING_AMOUNT_UNRESOLVED|
|user_263|transport/Fuel refill/debit/ZAR|4|519.84, 813.27, 649.07, 502.13|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_263|transport/Metro and bus fares/debit/ZAR|6|767.06, 701.96, 741.36, 654.61, 811.62, 562.54|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_263|transport/Commuter pass/debit/ZAR|6|730.67, 545.64, 798.15, 688.74, 746.07, 594.57|variable but recurrent|25|RECURRING_AMOUNT_UNRESOLVED|
|user_263|transport/Vehicle charging/debit/ZAR|6|493.43, 862.78, 551.32, 777.45, 668.18, 760.6|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_263|transport/Local taxi/debit/ZAR|4|710.6, 811.79, 855.13, 505.56|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_263|transport/Rail pass/debit/ZAR|2|848.9, 853.14|repeated but not demonstrably recurrent|||
|user_263|transport/Parking and tolls/debit/ZAR|2|748.63, 802.34|repeated but not demonstrably recurrent|||
|user_263|transport/Ride-hailing trip/debit/ZAR|5|721.72, 599.82, 868.23, 753.08, 872.41|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_263|dining/Lunch with colleagues/debit/ZAR|6|1030.77, 720.76, 899.69, 1153.32, 1039.55, 782.83|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_263|dining/Quick-service meal/debit/ZAR|3|939.17, 879.73, 900.02|variable but recurrent|77|RECURRING_AMOUNT_UNRESOLVED|
|user_263|dining/Neighbourhood restaurant/debit/ZAR|2|683.92, 839.69|repeated but not demonstrably recurrent|||
|user_263|dining/Takeaway order/debit/ZAR|6|1099.93, 1004.75, 1098.89, 1163.48, 731.98, 772.09|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_263|dining/Weekend food delivery/debit/ZAR|5|891.77, 1080.16, 870.67, 1081.64, 864.14|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_263|dining/Coffee shop/debit/ZAR|2|937.46, 725.1|repeated but not demonstrably recurrent|||
|user_264|salary/Payroll credit/credit/INR|5|88000, 88000, 88000, 88000, 88000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_264|rent/Apartment rent transfer/debit/INR|6|20400, 20400, 20400, 20400, 20400, 20400|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_264|utilities/Water and power payment/debit/INR|5|5147.14, 5311.42, 5558.94, 5747.51, 5986.66|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_264|cloud_storage/Shared storage plan/debit/INR|5|475, 475, 475, 475, 475|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_264|streaming/Streaming subscription/debit/INR|5|2410, 2410, 2410, 2410, 2410|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_264|shopping/Clothing and household items/debit/INR|5|3914.35, 3943.18, 4120.5, 4125.12, 4059.6|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_264|groceries/Supermarket basket/debit/INR|5|2893.63, 3626.2, 4815.25, 3585.31, 3142.32|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_264|groceries/Fresh food shop/debit/INR|3|2742.75, 3964.51, 4674.37|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_264|groceries/Weekly produce market/debit/INR|4|3496.34, 4495.04, 3310.44, 4081.25|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_264|groceries/Grocery delivery/debit/INR|2|3077.89, 4745.12|repeated but not demonstrably recurrent|||
|user_264|transport/Commuter pass/debit/INR|2|1506.95, 1986.78|repeated but not demonstrably recurrent|||
|user_264|transport/Metro and bus fares/debit/INR|2|2009.69, 1968.9|repeated but not demonstrably recurrent|||
|user_264|transport/Ride-hailing trip/debit/INR|2|1663.46, 2152.67|repeated but not demonstrably recurrent|||
|user_264|dining/Bakery and snacks/debit/INR|4|2966.75, 4807.26, 4764.48, 3030.36|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_264|dining/Lunch with colleagues/debit/INR|2|4693.11, 4086.27|repeated but not demonstrably recurrent|||
|user_265|rent/Monthly rent/debit/INR|6|83700, 83700, 83700, 83700, 83700, 83700|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_265|utilities/Household utility payment/debit/INR|5|12603.67, 13568.46, 15363.94, 13319.23, 12926.87|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_265|music_subscription/Music subscription/debit/INR|5|1585, 1585, 1585, 1585, 1585|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_265|delivery_membership/Grocery delivery membership/debit/INR|5|3540, 3540, 3540, 3540, 3540|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_265|gym/Community fitness plan/debit/INR|5|6630, 6630, 6630, 6630, 6630|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_265|entertainment/Local event tickets/debit/INR|5|5172.92, 5763.36, 5365.8, 4874.91, 4949.6|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_265|salary/Peak-season wages/credit/INR|2|246832.35, 292002.89|repeated but not demonstrably recurrent|||
|user_265|groceries/Fresh food shop/debit/INR|5|8162.22, 13228.91, 12744.57, 8028.8, 13559.37|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_265|groceries/Local market purchase/debit/INR|3|12496.19, 12680.1, 10178.8|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_265|groceries/Supermarket basket/debit/INR|6|12858.57, 10128.49, 8478.2, 12373.44, 13322.17, 11357.09|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_265|groceries/Grocery delivery/debit/INR|5|13507.29, 11872.87, 10689.91, 12861.12, 11451.5|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_265|groceries/Neighbourhood grocer/debit/INR|2|9499.44, 9495.1|repeated but not demonstrably recurrent|||
|user_265|groceries/Weekly produce market/debit/INR|3|7792.78, 10921.92, 8181.43|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_265|transport/Ride-hailing trip/debit/INR|4|6222.59, 4439.92, 6286.53, 5768.3|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_265|transport/Vehicle charging/debit/INR|11|6155.48, 5539.42, 5124.04, 4066.23, 6289.3, 4769.84, 6416.37, 5420.33, 6420.51, 6354.24, 4211.94|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_265|transport/Parking and tolls/debit/INR|4|5376.03, 5173.66, 3908.11, 3786.81|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_265|transport/Commuter pass/debit/INR|2|4861.84, 4973.83|repeated but not demonstrably recurrent|||
|user_265|transport/Fuel refill/debit/INR|2|4548.53, 5847.07|repeated but not demonstrably recurrent|||
|user_265|transport/Local taxi/debit/INR|2|4183.18, 6006.03|repeated but not demonstrably recurrent|||
|user_265|dining/Neighbourhood restaurant/debit/INR|2|8627.06, 12836.78|repeated but not demonstrably recurrent|||
|user_265|dining/Quick-service meal/debit/INR|2|8852.09, 8002.47|repeated but not demonstrably recurrent|||
|user_265|dining/Weekend food delivery/debit/INR|3|7885.41, 9232.33, 12629.24|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_265|dining/Takeaway order/debit/INR|3|10574.72, 9329.15, 12439.13|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_266|salary/Payroll credit/credit/EUR|5|968, 968, 968, 968, 968|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_266|rent/Apartment rent transfer/debit/EUR|5|266.2, 266.2, 266.2, 266.2, 266.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_266|utilities/Electricity bill/debit/EUR|5|67.59, 66.34, 64.4, 73.15, 68.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_266|debt_repayment/Personal loan payment/debit/EUR|5|147, 147, 147, 147, 147|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_266|healthcare/Family healthcare expense/debit/EUR|5|45.5, 48.47, 47.34, 41.32, 39.27|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_266|family_support/Dependent care payment/debit/EUR|5|62, 62, 62, 62, 62|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_266|cloud_storage/Online backup subscription/debit/EUR|5|7, 7, 7, 7, 7|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_266|shopping/Monthly shopping spend/debit/EUR|5|24.29, 24.22, 29.15, 30.06, 25.87|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_266|groceries/Weekly produce market/debit/EUR|5|37.57, 49.75, 49.75, 35.86, 38.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_266|groceries/Supermarket basket/debit/EUR|4|46.17, 49.75, 44.56, 53.5|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_266|groceries/Fresh food shop/debit/EUR|4|42.92, 34.41, 39.26, 50.6|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_266|groceries/Local market purchase/debit/EUR|4|35.64, 50.1, 37.09, 38.89|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_266|groceries/Household groceries/debit/EUR|2|32.23, 38.59|repeated but not demonstrably recurrent|||
|user_266|groceries/Bulk pantry shop/debit/EUR|4|46.12, 34.39, 48.98, 34.36|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_266|groceries/Grocery delivery/debit/EUR|2|52.08, 38.8|repeated but not demonstrably recurrent|||
|user_266|transport/Ride-hailing trip/debit/EUR|3|28.16, 18.68, 17.11|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_266|transport/Vehicle charging/debit/EUR|2|20.68, 22.79|repeated but not demonstrably recurrent|||
|user_266|transport/Metro and bus fares/debit/EUR|3|23.69, 20.11, 18.6|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_266|transport/Local taxi/debit/EUR|3|19.17, 24.24, 20.86|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_267|salary/Payroll credit/credit/USD|5|1821.60, 1821.60, 1821.60, 1821.60, 1821.60|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_267|rent/Landlord standing order/debit/EUR|6|575.3, 575.3, 575.3, 575.3, 575.3, 575.3|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_267|utilities/Electricity and water bill/debit/EUR|5|112.99, 102.15, 112.68, 114.87, 100.36|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_267|insurance/Household insurance/debit/EUR|5|81, 81, 81, 81, 81|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_267|cloud_storage/Online backup subscription/debit/EUR|5|8, 8, 8, 8, 8|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_267|streaming/Family streaming plan/debit/EUR|5|52, 52, 52, 52, 52|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_267|shopping/Personal shopping/debit/EUR|5|40.71, 40.66, 47.53, 48.33, 49.07|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_267|entertainment/Cinema and events/debit/EUR|5|72.29, 68.03, 66.15, 71.47, 70.47|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_267|groceries/Supermarket basket/debit/EUR|4|80.57, 67.39, 54.77, 57.34|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_267|groceries/Fresh food shop/debit/EUR|3|81.88, 90.26, 88.85|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_267|groceries/Local market purchase/debit/EUR|2|61.3, 86.97|repeated but not demonstrably recurrent|||
|user_267|groceries/Bulk pantry shop/debit/EUR|3|65.67, 68.06, 62.48|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_267|groceries/Neighbourhood grocer/debit/EUR|3|83.05, 68.38, 71.02|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_267|groceries/Grocery delivery/debit/EUR|2|66.6, 89.5|repeated but not demonstrably recurrent|||
|user_267|transport/Commuter pass/debit/EUR|5|45.12, 53.13, 34.5, 52.48, 42.84|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Rail pass/debit/EUR|6|44.63, 49.02, 46.83, 53.68, 43.2, 55.93|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Parking and tolls/debit/EUR|3|37.76, 42.92, 37.09|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Fuel refill/debit/EUR|3|39.19, 48.41, 41.57|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Metro and bus fares/debit/EUR|4|41.29, 38.73, 41.3, 52.41|variable but recurrent|45|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Ride-hailing trip/debit/EUR|4|47.89, 46.73, 43.48, 43.2|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Local taxi/debit/EUR|7|52.25, 43.37, 36.71, 42.47, 53.46, 52.1, 47.74|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_267|transport/Vehicle charging/debit/EUR|3|47.09, 35.01, 55.02|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_267|dining/Quick-service meal/debit/EUR|5|36.12, 40.18, 58.42, 45.03, 36.59|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_267|dining/Takeaway order/debit/EUR|4|47.96, 54.66, 45.17, 40.49|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_267|dining/Family dinner/debit/EUR|4|57.08, 57.69, 42.68, 51.77|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_267|dining/Coffee shop/debit/EUR|2|54.36, 41.68|repeated but not demonstrably recurrent|||
|user_267|dining/Bakery and snacks/debit/EUR|7|38.96, 44.08, 44.95, 60.85, 49.92, 56.95, 58.55|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_267|dining/Lunch with colleagues/debit/EUR|2|55.74, 50.76|repeated but not demonstrably recurrent|||
|user_268|salary/Payroll credit/credit/EUR|5|2288, 2288, 2288, 2288, 2288|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_268|rent/Monthly rent/debit/EUR|6|557.7, 557.7, 557.7, 557.7, 557.7, 557.7|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_268|utilities/Household utility payment/debit/EUR|6|147.64, 149.94, 149.45, 158.96, 151.5, 158.89|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_268|debt_repayment/Loan repayment/debit/EUR|5|364, 364, 364, 364, 364|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_268|music_subscription/Audio streaming plan/debit/EUR|5|14, 14, 14, 14, 14|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_268|groceries/Supermarket basket/debit/EUR|5|87.61, 100.83, 81.84, 117.32, 102.34|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_268|groceries/Bulk pantry shop/debit/EUR|2|100.23, 80.53|repeated but not demonstrably recurrent|||
|user_268|groceries/Household groceries/debit/EUR|2|120.08, 95.1|repeated but not demonstrably recurrent|||
|user_268|transport/Fuel refill/debit/EUR|2|53.33, 60.94|repeated but not demonstrably recurrent|||
|user_268|transport/Local taxi/debit/EUR|2|42.58, 49.8|repeated but not demonstrably recurrent|||
|user_268|transport/Ride-hailing trip/debit/EUR|2|41.03, 53.03|repeated but not demonstrably recurrent|||
|user_268|dining/Takeaway order/debit/EUR|2|63.94, 78.74|repeated but not demonstrably recurrent|||
|user_268|dining/Family dinner/debit/EUR|2|70.87, 80.22|repeated but not demonstrably recurrent|||
|user_268|dining/Bakery and snacks/debit/EUR|2|70.98, 83.28|repeated but not demonstrably recurrent|||
|user_269|rent/Shared housing rent/debit/ZAR|6|11484, 11484, 11484, 11484, 11484, 11484|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_269|utilities/Municipal utilities/debit/ZAR|5|1657.15, 1983, 1646.88, 1938.61, 1630.24|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_269|education/Course tuition/debit/ZAR|5|1960.2, 1960.2, 1960.2, 1960.2, 1960.2|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_269|debt_repayment/Education loan instalment/debit/ZAR|5|4499, 4499, 4499, 4499, 4499|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_269|music_subscription/Music service subscription/debit/ZAR|5|376.2, 376.2, 376.2, 376.2, 376.2|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_269|delivery_membership/Delivery service plan/debit/ZAR|5|317.9, 317.9, 317.9, 317.9, 317.9|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_269|groceries/Bulk pantry shop/debit/ZAR|5|1425.74, 1277.23, 1049.54, 1693.13, 1352.04|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_269|groceries/Grocery delivery/debit/ZAR|3|1540.95, 1490.49, 1285.7|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_269|groceries/Weekly produce market/debit/ZAR|3|1258.09, 1140.3, 1747.52|variable but recurrent|70|RECURRING_AMOUNT_UNRESOLVED|
|user_269|groceries/Local market purchase/debit/ZAR|2|1336.22, 1604.42|repeated but not demonstrably recurrent|||
|user_269|groceries/Supermarket basket/debit/ZAR|4|1628.9, 1218.06, 1325.62, 1242.58|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_269|groceries/Fresh food shop/debit/ZAR|2|1020.58, 1562.36|repeated but not demonstrably recurrent|||
|user_269|groceries/Household groceries/debit/ZAR|5|1080.31, 1311.17, 1463.64, 1124.36, 1060.52|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_269|groceries/Neighbourhood grocer/debit/ZAR|2|1433.24, 1738.21|repeated but not demonstrably recurrent|||
|user_269|transport/Commuter pass/debit/ZAR|2|795.46, 743.01|repeated but not demonstrably recurrent|||
|user_269|transport/Parking and tolls/debit/ZAR|4|703.59, 821.72, 817.55, 1179.48|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_269|transport/Local taxi/debit/ZAR|6|890.74, 869.48, 1012.16, 1219.16, 724.1, 740.09|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_269|transport/Metro and bus fares/debit/ZAR|6|1165.91, 1143.11, 894.42, 792.85, 853.73, 1092.41|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_269|transport/Rail pass/debit/ZAR|3|918.83, 1042.28, 920.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_269|transport/Vehicle charging/debit/ZAR|2|1197.09, 1136.8|repeated but not demonstrably recurrent|||
|user_269|transport/Fuel refill/debit/ZAR|2|836.19, 949.37|repeated but not demonstrably recurrent|||
|user_269|dining/Neighbourhood restaurant/debit/ZAR|2|1156.77, 1080.8|repeated but not demonstrably recurrent|||
|user_269|dining/Family dinner/debit/ZAR|3|1058.39, 1202.41, 1299.69|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_269|dining/Quick-service meal/debit/ZAR|3|1016.79, 1255.4, 1020.95|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_269|dining/Lunch with colleagues/debit/ZAR|2|1098.59, 1004.68|repeated but not demonstrably recurrent|||
|user_270|salary/Primary household salary/credit/USD|5|1071.36, 1071.36, 1071.36, 1071.36, 1071.36|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_270|salary/Second household income/credit/USD|4|615.83, 641.84, 665.03, 846.63|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_270|housing/Home association fee/debit/USD|6|183, 183, 183, 183, 183, 183|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_270|utilities/Energy provider bill/debit/USD|5|86.51, 102.44, 93.46, 101.07, 83.72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_270|insurance/Insurance policy payment/debit/USD|5|78, 78, 78, 78, 78|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_270|healthcare/Diagnostic test/debit/USD|5|75.81, 75.17, 84.03, 72.02, 72|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_270|streaming/Streaming subscription/debit/USD|5|46, 46, 46, 46, 46|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_270|groceries/Grocery delivery/debit/USD|3|52.55, 63.17, 50|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_270|groceries/Weekly produce market/debit/USD|7|55.38, 71.99, 53.29, 84.4, 62.51, 78.26, 48.98|variable but recurrent|20|RECURRING_AMOUNT_UNRESOLVED|
|user_270|groceries/Household groceries/debit/USD|3|55.37, 73.74, 72.65|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_270|groceries/Neighbourhood grocer/debit/USD|2|77.64, 82.32|repeated but not demonstrably recurrent|||
|user_270|transport/Ride-hailing trip/debit/USD|4|36.2, 44.64, 39.27, 38.83|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_270|transport/Parking and tolls/debit/USD|2|40.53, 36.12|repeated but not demonstrably recurrent|||
|user_270|transport/Commuter pass/debit/USD|4|37.2, 37.6, 41.17, 42.01|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_270|dining/Weekend food delivery/debit/USD|3|42.59, 50.32, 38.72|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_270|dining/Family dinner/debit/USD|2|33.76, 44.01|repeated but not demonstrably recurrent|||
|user_270|dining/Takeaway order/debit/USD|2|39.67, 33.82|repeated but not demonstrably recurrent|||
|user_270|dining/Neighbourhood restaurant/debit/USD|2|56.3, 36.12|repeated but not demonstrably recurrent|||
|user_271|salary/Payroll credit/credit/INR|5|103000, 103000, 103000, 103000, 103000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_271|rent/Shared housing rent/debit/INR|5|27800, 27800, 27800, 27800, 27800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_271|utilities/Municipal utilities/debit/INR|5|6438.75, 5991.15, 6358.46, 6068.51, 5774.5|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_271|debt_repayment/Vehicle loan payment/debit/INR|5|14850, 14850, 14850, 14850, 14850|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_271|streaming/Family streaming plan/debit/INR|5|2000, 2000, 2000, 2000, 2000|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_271|cloud_storage/Shared storage plan/debit/INR|5|530, 530, 530, 530, 530|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_271|shopping/Personal shopping/debit/INR|5|4310.66, 4439.51, 4217.15, 3760.08, 4085.6|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Neighbourhood grocer/debit/INR|3|3620.23, 3913.62, 4393.35|variable but recurrent|63|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Supermarket basket/debit/INR|4|3617.39, 3740.49, 3734.02, 4726.55|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Bulk pantry shop/debit/INR|4|4535.05, 3542.38, 3970.55, 4298.36|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Grocery delivery/debit/INR|2|3862.61, 4181.62|repeated but not demonstrably recurrent|||
|user_271|groceries/Local market purchase/debit/INR|3|4022.37, 4573.94, 3477.33|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Household groceries/debit/INR|4|3653.63, 2709.67, 3235.58, 3060.56|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Weekly produce market/debit/INR|3|3418.51, 4261.77, 4477.15|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_271|groceries/Fresh food shop/debit/INR|2|2930.29, 4318.35|repeated but not demonstrably recurrent|||
|user_271|transport/Local taxi/debit/INR|5|2378.22, 3043.36, 1765.76, 2601.38, 2827.44|variable but recurrent|49|RECURRING_AMOUNT_UNRESOLVED|
|user_271|transport/Commuter pass/debit/INR|5|2969.9, 2489.35, 2851.47, 2908.65, 2772.68|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_271|transport/Rail pass/debit/INR|3|1861.33, 2977.05, 2908.56|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_271|transport/Vehicle charging/debit/INR|4|2430.77, 1756.34, 1971.99, 2296.57|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_271|transport/Metro and bus fares/debit/INR|4|3031.63, 2915.27, 2639.45, 2228.29|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_271|transport/Fuel refill/debit/INR|2|1984.04, 2545.37|repeated but not demonstrably recurrent|||
|user_271|transport/Parking and tolls/debit/INR|2|2871.92, 1923.78|repeated but not demonstrably recurrent|||
|user_271|dining/Quick-service meal/debit/INR|2|2941.58, 2454.78|repeated but not demonstrably recurrent|||
|user_271|dining/Neighbourhood restaurant/debit/INR|3|3374.98, 2742.36, 2698.01|variable but recurrent|56|RECURRING_AMOUNT_UNRESOLVED|
|user_271|dining/Family dinner/debit/INR|2|2753.61, 2843.76|repeated but not demonstrably recurrent|||
|user_271|dining/Coffee shop/debit/INR|3|2323.24, 2880.69, 2773.96|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_272|salary/Payroll credit/credit/IDR|5|11780000, 11780000, 11780000, 11780000, 11780000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_272|housing/Home repair reserve/debit/IDR|6|836000, 836000, 836000, 836000, 836000, 836000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_272|utilities/Municipal utilities/debit/IDR|5|598242.36, 577872.22, 523883.25, 580909.48, 592465.88|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_272|insurance/Health insurance premium/debit/IDR|5|402800, 402800, 402800, 402800, 402800|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_272|education/Child education fee/debit/IDR|5|807500, 807500, 807500, 807500, 807500|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_272|healthcare/Diagnostic test/debit/IDR|5|421470.15, 386827.61, 427100.48, 407908.96, 420536.92|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_272|entertainment/Local event tickets/debit/IDR|5|457665.38, 397257.49, 427461.39, 444045.69, 389866.57|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_272|cloud_storage/Online backup subscription/debit/IDR|5|74100, 74100, 74100, 74100, 74100|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_272|groceries/Weekly produce market/debit/IDR|5|370159.67, 573031.08, 432552.07, 539683.25, 479451.75|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_272|groceries/Bulk pantry shop/debit/IDR|5|413353.38, 559114.5, 372672.4, 365590.11, 386665.56|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_272|groceries/Supermarket basket/debit/IDR|2|600177.9, 418844.86|repeated but not demonstrably recurrent|||
|user_272|groceries/Fresh food shop/debit/IDR|2|561679.87, 509692.76|repeated but not demonstrably recurrent|||
|user_272|groceries/Neighbourhood grocer/debit/IDR|2|533247.85, 428177.03|repeated but not demonstrably recurrent|||
|user_272|transport/Vehicle charging/debit/IDR|4|287759.37, 179454.09, 213260.03, 194635.76|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_272|transport/Rail pass/debit/IDR|2|281694.01, 267787.12|repeated but not demonstrably recurrent|||
|user_272|transport/Local taxi/debit/IDR|2|203354.91, 280116.11|repeated but not demonstrably recurrent|||
|user_272|transport/Metro and bus fares/debit/IDR|2|231581.46, 238043.1|repeated but not demonstrably recurrent|||
|user_272|dining/Lunch with colleagues/debit/IDR|2|305411.6, 431358.06|repeated but not demonstrably recurrent|||
|user_272|dining/Weekend food delivery/debit/IDR|2|283037.64, 368323.46|repeated but not demonstrably recurrent|||
|user_272|dining/Takeaway order/debit/IDR|2|344218.99, 338737.28|repeated but not demonstrably recurrent|||
|user_273|salary/Payroll credit/credit/IDR|5|34010000, 34010000, 34010000, 34010000, 34010000|variable but recurrent|30|UNSUPPORTED_HISTORICAL_INCOME|
|user_273|rent/Apartment rent transfer/debit/IDR|6|10374000, 10374000, 10374000, 10374000, 10374000, 10374000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_273|utilities/Water and power payment/debit/IDR|6|1637119.6, 1401906.12, 1426020.51, 1466820.28, 1585648.66, 1639730.47|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_273|cloud_storage/Cloud storage plan/debit/IDR|5|199500, 199500, 199500, 199500, 199500|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_273|streaming/Streaming subscription/debit/IDR|5|944300, 944300, 944300, 944300, 944300|stable fixed|30|SUPPORTED_FIXED_AMOUNT|
|user_273|shopping/Household shopping/debit/IDR|5|1484654.11, 1280519.82, 1248771.48, 1464139.04, 1471885.22|variable but recurrent|30|RECURRING_AMOUNT_UNRESOLVED|
|user_273|groceries/Local market purchase/debit/IDR|3|1040057.58, 1510669.93, 1279643.69|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_273|groceries/Neighbourhood grocer/debit/IDR|4|1202587.81, 1269777.04, 936585.2, 1564167.7|variable but recurrent|50|RECURRING_AMOUNT_UNRESOLVED|
|user_273|groceries/Fresh food shop/debit/IDR|2|1459577.21, 931325.07|repeated but not demonstrably recurrent|||
|user_273|groceries/Grocery delivery/debit/IDR|2|940880.76, 1530538.9|repeated but not demonstrably recurrent|||
|user_273|groceries/Household groceries/debit/IDR|2|1436958.13, 992881.71|repeated but not demonstrably recurrent|||
|user_273|groceries/Weekly produce market/debit/IDR|2|1219379.63, 1161828.47|repeated but not demonstrably recurrent|||
|user_273|groceries/Bulk pantry shop/debit/IDR|2|897272.32, 1060156.6|repeated but not demonstrably recurrent|||
|user_273|transport/Metro and bus fares/debit/IDR|2|1048157.97, 879600.7|repeated but not demonstrably recurrent|||
|user_273|transport/Parking and tolls/debit/IDR|2|954809.89, 757625.24|repeated but not demonstrably recurrent|||
|user_273|dining/Weekend food delivery/debit/IDR|2|1281801.1, 1136150.23|repeated but not demonstrably recurrent|||
|user_273|dining/Quick-service meal/debit/IDR|4|1569401.74, 1169419.57, 1395318.38, 980572.71|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_274|salary/Payroll credit/credit/USD|5|2484.00, 2484.00, 2484.00, 2484.00, 2484.00|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_274|rent/Apartment rent transfer/debit/EUR|6|576.4, 576.4, 576.4, 576.4, 576.4, 576.4|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_274|utilities/Water and power payment/debit/EUR|5|179.22, 166.8, 182.27, 182.11, 154.55|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_274|insurance/Health insurance premium/debit/EUR|5|96, 96, 96, 96, 96|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_274|cloud_storage/Online backup subscription/debit/EUR|5|16, 16, 16, 16, 16|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_274|streaming/Video streaming plan/debit/EUR|5|50, 50, 50, 50, 50|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_274|shopping/Clothing and household items/debit/EUR|5|124.41, 132.11, 113.57, 135.64, 114.14|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_274|entertainment/Games and recreation/debit/EUR|5|78.68, 80.97, 72.57, 69.71, 69.91|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_274|groceries/Weekly produce market/debit/EUR|3|140.33, 138.94, 84.38|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_274|groceries/Fresh food shop/debit/EUR|2|143.53, 108.56|repeated but not demonstrably recurrent|||
|user_274|groceries/Household groceries/debit/EUR|3|120.14, 144.8, 121.1|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_274|groceries/Neighbourhood grocer/debit/EUR|4|138.61, 129.31, 120.71, 131.7|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_274|groceries/Bulk pantry shop/debit/EUR|2|140.68, 136.02|repeated but not demonstrably recurrent|||
|user_274|groceries/Grocery delivery/debit/EUR|2|115.86, 120.73|repeated but not demonstrably recurrent|||
|user_274|transport/Commuter pass/debit/EUR|7|45.46, 54.44, 58.7, 59.94, 52.97, 55.85, 39.68|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Ride-hailing trip/debit/EUR|6|56.08, 57.75, 58.45, 42.29, 42.38, 61.72|variable but recurrent|15|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Vehicle charging/debit/EUR|5|65.62, 56.72, 43.45, 62.85, 45.73|variable but recurrent|5|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Local taxi/debit/EUR|3|51.5, 40.04, 56.95|variable but recurrent|65|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Rail pass/debit/EUR|3|67.48, 55.6, 64.44|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Parking and tolls/debit/EUR|6|54.63, 54.93, 63.73, 51.81, 41.12, 68.26|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Fuel refill/debit/EUR|3|52.1, 53.42, 62.35|variable but recurrent|10|RECURRING_AMOUNT_UNRESOLVED|
|user_274|transport/Metro and bus fares/debit/EUR|2|61.75, 47.58|repeated but not demonstrably recurrent|||
|user_274|dining/Lunch with colleagues/debit/EUR|4|101.13, 66.12, 64.91, 85.16|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_274|dining/Bakery and snacks/debit/EUR|4|70.39, 63.76, 62.82, 100.22|variable but recurrent|28|RECURRING_AMOUNT_UNRESOLVED|
|user_274|dining/Quick-service meal/debit/EUR|4|89.48, 86.78, 87.69, 103.83|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_274|dining/Coffee shop/debit/EUR|6|77.43, 103.89, 69.46, 96.58, 66.07, 106.42|variable but recurrent|21|RECURRING_AMOUNT_UNRESOLVED|
|user_274|dining/Weekend food delivery/debit/EUR|2|94.88, 78.09|repeated but not demonstrably recurrent|||
|user_274|dining/Takeaway order/debit/EUR|3|90.36, 101.89, 74.28|variable but recurrent|7|RECURRING_AMOUNT_UNRESOLVED|
|user_275|salary/Payroll credit/credit/IDR|5|18050000, 18050000, 18050000, 18050000, 18050000|variable but recurrent|31|UNSUPPORTED_HISTORICAL_INCOME|
|user_275|rent/Shared housing rent/debit/IDR|6|5225000, 5225000, 5225000, 5225000, 5225000, 5225000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_275|utilities/Electricity bill/debit/IDR|5|1397870.05, 1173094.13, 1258904.05, 1246455.24, 1259413.52|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_275|debt_repayment/Personal loan payment/debit/IDR|5|1539000, 1539000, 1539000, 1539000, 1539000|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_275|healthcare/Regular medicine purchase/debit/IDR|5|1226962.68, 1128337.74, 1285827.89, 1325567.69, 1206981.09|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_275|family_support/Parent support transfer/debit/IDR|5|1149500, 1149500, 1149500, 1149500, 1149500|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_275|cloud_storage/Cloud storage plan/debit/IDR|5|71250, 71250, 71250, 71250, 71250|stable fixed|31|SUPPORTED_FIXED_AMOUNT|
|user_275|shopping/Clothing and household items/debit/IDR|5|949902.46, 1038116, 853022.13, 955567.05, 827731.99|variable but recurrent|31|RECURRING_AMOUNT_UNRESOLVED|
|user_275|groceries/Household groceries/debit/IDR|3|870520.77, 721376.22, 683659.7|variable but recurrent|42|RECURRING_AMOUNT_UNRESOLVED|
|user_275|groceries/Neighbourhood grocer/debit/IDR|7|820531.51, 646736.14, 811061, 916411.91, 935483.85, 630901.21, 897272.28|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_275|groceries/Weekly produce market/debit/IDR|5|751783.39, 789793.3, 797149, 974763.43, 636370.42|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_275|groceries/Supermarket basket/debit/IDR|4|730690.71, 600493.39, 781222.58, 571991.19|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_275|groceries/Fresh food shop/debit/IDR|3|918869.14, 634736.56, 686518.46|variable but recurrent|35|RECURRING_AMOUNT_UNRESOLVED|
|user_275|groceries/Grocery delivery/debit/IDR|2|593308.87, 828323.33|repeated but not demonstrably recurrent|||
|user_275|transport/Local taxi/debit/IDR|5|356891.47, 414484.4, 282022.99, 270553.72, 451837.75|variable but recurrent|14|RECURRING_AMOUNT_UNRESOLVED|
|user_275|transport/Fuel refill/debit/IDR|2|303809, 387671.23|repeated but not demonstrably recurrent|||
|user_275|transport/Ride-hailing trip/debit/IDR|2|418415.26, 477812.2|repeated but not demonstrably recurrent|||
|user_275|transport/Vehicle charging/debit/IDR|2|420021.42, 378457.9|repeated but not demonstrably recurrent|||

## Evidence classification

- **SUPPORTED:** equal amounts, stable source identity, and recurrence evidence support a fixed projection.
- **STRONGLY_INFERRED:** repeated source identity suggests a series but the specification does not define amount estimation.
- **UNRESOLVED:** varying amounts, missing cycles, month-end behavior, or ambiguous lifecycle.
- **UNSUPPORTED:** inventing a future amount from category frequency alone.
