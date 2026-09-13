# Phase 13 First-Divergence Analysis

The first-divergence rule is causal: compare fields in output order, while tracing the upstream movement model. Existing Phase 10 forensic evidence identifies safe amount as the first divergence for 23/25 requests; two are serialization-only rows.

## Distribution

- **serialization:** 2 — request_01, request_12
- **safe amount:** 23 — request_02, request_03, request_04, request_05, request_06, request_07, request_08, request_09, request_10, request_11, request_13, request_14, request_15, request_16, request_17, request_18, request_19, request_20, request_21, request_22, request_23, request_24, request_25

## Dependency graph

`lifecycle + recurrence + future-credit classification -> forecast balances -> safe amount -> earliest safe date -> candidate feasibility -> ranking/status -> serialization`

## Evidence judgment

The current mismatch pattern is upstream, but the sample does not distinguish the competing forecast contracts. A score-maximizing recurrence or variable-amount estimator would therefore be an unsupported policy change.
