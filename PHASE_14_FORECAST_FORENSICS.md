# Phase 14 Forecast Forensics

## First divergence

- Safe amount: 23 requests
- Serialization-only: 2 requests
- Candidate ranking is not established as the primary defect.

## Causal interpretation

The first future date at which the actual forecast can differ is controlled by lifecycle classification, recurrence projection, scheduled-credit treatment, optional baseline, same-day policy and direct FX. The available solved outputs do not uniquely identify which movement to add/remove. Any repair that chooses a variable estimator, calendar threshold, generic scheduled-credit inclusion or replacement date would be an unsupported inference.

## Safety review

The frozen 54-test suite remains passing; no production forecast was changed in this phase.
