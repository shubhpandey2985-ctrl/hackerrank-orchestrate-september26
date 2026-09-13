# Phase 15 Property Tests

`code/test_semantic_lab.py` covers the synthetic lab properties: unavoidable
debits cannot increase capacity; confirmed income cannot decrease capacity;
failed/cancelled and pending credits do not create capacity; Decimal traces are
provenance-bearing; same-day orders are explicitly comparable; and reordered
input is deterministic. The production hardening suite continues to cover
minimum-balance, payment-plan, FX and output invariants.

