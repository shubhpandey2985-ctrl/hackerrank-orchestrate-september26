# Phase 13 Baseline

- HEAD: `d2416958be49f40ef9a15fefe3a6795d6d34a7e1`
- Phase 13 checkpoint requested: `phase13-analysis-only` (tag creation was attempted but the checkout denied creation of `.git/refs/tags/*.lock`; HEAD is unchanged).
- Full test suite: 54 passed
- Focused semantic/adversarial/hardening tests: 45 passed
- 25-example field matches: safe 2/25; status 10/25; method 12/25; plan 11/25; earliest 8/25; changes 22/25
- Output rows: 250
- Output SHA-256: `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`
- Dataset hashes are recorded in the Phase 13 transcript and were unchanged.
- Dataset SHA-256: `financial_events.csv` B6C3F43A8AD3A80CA11C72CCE6F2818EEA06621A3582D2851886FD9127B1229D;
  `financial_profiles.csv` FA173608F8EC99C8D9D633EACE762695AEAA2D276A509989F0EDD8E123C07964;
  `requests.csv` 13663D50B7098B28A8C087A02EB085041260999707ADADE5230D29F1C2E6595D;
  `sample_requests.csv` 117BF2AB9E5F0054BAE48AFE8506F5DAA35929559CB771F2C27DD4FE18DA62F6.
- Supplied datasets, solved examples, expected outputs and `output.csv` were not modified.

Prior conclusions carried forward: Phase 10 found safe amount as the first
divergence for 23 requests; Phase 12 found the strongest model to be explicit
confirmed movements plus supported stable fixed recurrence, with variable
amounts, calendar recurrence, optional baseline, generic scheduled credits,
same-day ordering, replacement timing, late-deadline mapping and decimal
presentation unresolved.
