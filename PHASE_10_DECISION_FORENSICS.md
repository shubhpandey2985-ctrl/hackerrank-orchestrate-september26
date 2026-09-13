# Phase 10 — Downstream Decision Forensics

Status: analysis-only. Forecast, ledger, recurrence, lifecycle, FX, Decimal arithmetic and production output were treated as immutable. No production code, dataset, expected output, output.csv or code.zip was modified.

## Dependency graph

```text
forecast → safe amount → earliest date → candidate generation → validation → deadline/status → ranking → output
```

## First-divergence aggregate

| Stage | Examples | Interpretation |
|---|---:|---|
| OUTPUT_SERIALIZATION | 2 | request_01, request_12 |
| SAFE_AMOUNT | 23 | request_02, request_03, request_04, request_05, request_06, request_07, request_08, request_09, request_10, request_11, request_13, request_14, request_15, request_16, request_17, request_18, request_19, request_20, request_21, request_22, request_23, request_24, request_25 |

The earliest mismatch wins: a wrong safe amount masks later candidate/status/method/plan symptoms. A wrong earliest date masks wait/partial/deadline symptoms.

## Candidate generation, validation and ranking

The JSON artifact contains every available candidate audit for each request, including generated/rejected counts, preference eligibility, deadline compliance, safety, payment plan, changes and published rank keys. This permits exact rejection and ranking inspection without changing the pipeline.

## Preferences and status truth table

For each request the JSON records accepted preferences, expected/actual status and method, deadline, plan and first divergence. Preference constraints remain hard; no method rejected by the profile should be considered eligible.

## Spending changes

The remaining spending-change mismatches are isolated in the machine-readable rows. The subsystem was not rewritten; each is classified by its earlier first divergence where applicable.

## Safe amount and earliest-date invariants

The frozen implementation must preserve: `0 <= safe_amount <= requested_amount`; pending credits, failed/cancelled events and unsupported salary/variable estimates cannot increase capacity; every movement and candidate payment must respect the minimum balance; earliest date is independent of payment preference and ranking.

## Decision category

Remaining failures are primarily **forecast-dependent** and **earliest-date dependent**, with downstream candidate/status/method/plan mismatches. Candidate generation and validation should not be changed until the upstream forecast contract is resolved. Ranking is not evidenced as the primary defect.

## Phase 11 recommendation

Recommend one smallest next change: **freeze the current decision pipeline and document unresolved forecast semantics**. Do not implement candidate-generation, validation, ranking, status, preference or serialization repairs while safe amount and earliest date remain mismatched upstream.

COUNTERFACTUAL SCORE != SPECIFICATION PROOF.
