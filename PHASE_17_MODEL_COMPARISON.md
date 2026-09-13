# Phase 17 Model Comparison

| Model | Safe | Earliest | Status | Method | Plan | Changes | Safety | Classification | Promoted |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
|MODEL_A|2|8|10|12|11|22|0|SPECIFICATION-SUPPORTED + STRONGLY-EXAMPLE-SUPPORTED|True|
|MODEL_B|3|9|12|14|13|22|0|SPECIFICATION-SUPPORTED; conservative counterfactual|False|
|MODEL_C|2|8|10|12|11|22|0|STRONGLY-EXAMPLE-SUPPORTED; current contract|True|
|MODEL_D|n/a|n/a|n/a|n/a|n/a|n/a|0|UNSUPPORTED-ASSUMPTION; analysis only|False|

MODEL_D remains analysis-only because it invents varying future amounts. Higher score cannot override the specification/evidence hierarchy.
