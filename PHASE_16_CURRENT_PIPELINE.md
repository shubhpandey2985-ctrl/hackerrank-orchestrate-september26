# Phase 16 Current Pipeline

## Actual call/data flow

`main.main(root)` → `load_data` (`code/main.py`) reads profiles, requests,
options, events, messages, images and direct FX rates into `Data` →
`normalize_events` parses Decimal amounts, image evidence and home-currency
conversion → each request calls `candidate` → `semantic_events` applies
lifecycle/deduplication/pending/message evidence → `recurring` builds
source-identity recurrence evidence → `safe_amount` calls `forecast` with a
Decimal monotone search → `earliest` scans each date through the same forecast
→ `candidate` creates full, supplied-installment, partial, wait and bounded
flexible-change candidates → `forecast` validates every plan against the
minimum balance and 90-day horizon → deterministic ranking selects a candidate
→ `validate_output` checks grammar, preferences, options, actions and reruns
forecast → `main` serializes the exact eight-column CSV.

`evidence.py` and `explanations.py` are adapters only; they do not authorize
arithmetic or decisions. `semantic_lab.py` and Phase 15/16 scripts are
analysis-only and are not imported by production `main.py`.

## Semantic decision locations

| Decision | Source |
|---|---|
| schema/input loading | `code/main.py:load_data` |
| lifecycle/cash state/FX | `normalize_events`, `semantic_events` |
| deduplication | `semantic_events` precedence/signature logic |
| recurrence identity/date/amount | `recurring`, `estimate_future_amount` |
| scheduled/pending treatment | `normalize_events`, `semantic_events` |
| optional baseline | `baseline_include_optional`, `policy.py` |
| daily movement order | `forecast`, `policy.py:same_day_order` |
| safe amount | `safe_amount` |
| earliest safe date | `earliest` |
| candidates/ranking | `candidate` |
| hard validation | `validate_output` |
| serialization | `main` CSV writer and `fmt` |
