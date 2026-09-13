 # Token Usage Report

Final deterministic full-dataset run (250 requests):

| Provider/model | Calls | Input tokens | Output tokens | Estimated cost |
|---|---:|---:|---:|---:|
| None (deterministic pipeline) | 0 | 0 | 0 | $0.00 |

Total calls: 0  
Total tokens: 0  
Average tokens per request: 0  
Estimated total cost: $0.00  
Estimated cost per request: $0.00

The solver keeps event arithmetic, forecasting, candidate generation, validation,
ranking, and CSV generation deterministic. Evidence values are read from the
provided evidence cache generated during repository audit. No LLM-generated
decision is accepted by the validator.
