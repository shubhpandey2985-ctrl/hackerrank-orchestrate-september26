# Phase 18 Identifiability Matrix

| Semantic | Candidate A | Candidate B | Distinguishing fixture? | Expected output distinguishes? | Result |
|---|---|---|---|---|---|
|Variable spending amount|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Variable recurrence identity|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Observation threshold|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Gap tolerance|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Weekly cadence|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Biweekly cadence|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Monthly cadence|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Month-end behavior|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Missed-cycle behavior|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Terminal recurrence|conservative/current|alternative|explicit schema/lifecycle fixture|True|IDENTIFIABLE|
|Generic scheduled credits|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Confirmed future credits|conservative/current|alternative|explicit schema/lifecycle fixture|True|IDENTIFIABLE|
|Pending credits|conservative/current|alternative|explicit schema/lifecycle fixture|True|IDENTIFIABLE|
|Pending debits|conservative/current|alternative|explicit schema/lifecycle fixture|True|IDENTIFIABLE|
|Optional baseline|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Same-day ordering|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Replacement timing|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Deadline/status mapping|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Decimal serialization|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
|Flexible-action ties|conservative/current|alternative|none in supplied 25|False|OBSERVATIONALLY_CONFOUNDED|
