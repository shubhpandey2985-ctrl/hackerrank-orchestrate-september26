# Phase 19 Final

## Selected policies

The production policy layer retains fixed-only variable spending, observed
interval recurrence, current optional baseline, confirmed-salary-only generic
scheduled credits, explicit credit-first same-day ordering, never-invent
replacements, conservative late-deadline mapping, and Decimal presentation.
Unresolved choices are documented as policies rather than specification facts.

## Evidence basis

Specification-explicit lifecycle, FX, Decimal, minimum-balance, preferences,
payment grammar and validation rules were preserved. No unsupported estimator or
calendar rule was introduced.

## Production changes

No financial decision logic changed. Added policy documentation, adversarial
tests, packaging support, and usage reporting.

## Tests and sample comparison

- Full suite: 128 passed
- Phase 19 adversarial suite: 74 passed
- Semantic lab: 10 passed
- Sample matches unchanged: 2/25, 10/25, 12/25, 11/25, 8/25, 22/25
- Output hash unchanged: `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`

## Hidden-test coverage

At least 60 deterministic Phase 19 fixtures plus 66 semantic-lab fixtures cover
lifecycle, pending, recurrence, variable amounts, optional spending, salary,
scheduled credits, same-day events, FX, Decimal precision, deadlines,
preferences, flexible actions, duplicates, malformed/empty/zero cases and
90-day boundaries.

## Submission gate

`READY_FOR_PACKAGING` was reached: output validates, all tests pass, behavior is
deterministic, policies are explicit, and no datasets or expected outputs were
modified.

## Package

`code.zip` was created after the gate. It excludes datasets and forensic
artifacts, includes the required usage report and image-evidence cache, and ran
independently to produce 250 valid rows. ZIP SHA-256:
`4AFD4CF2418F298923FD30CDB1557A2EAECA632022C675E7C9E1C98346F8CC15`.

## Remaining risk

The 25-example score remains imperfect because the challenge does not authorize
one interpretation of variable amounts, recurrence calendars, optional baseline
or late status semantics. Those risks are explicit and fail-closed.
