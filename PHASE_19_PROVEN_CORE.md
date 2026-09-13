# Phase 19 Proven Core

The following behavior is frozen because it is specification-explicit or
strongly supported by schemas/fixtures:

- Decimal-only financial arithmetic and deterministic serialization.
- Direct supplied dated FX only; no inverse, triangulation or substitute rate.
- Failed, cancelled, unrealized and non-cash rows create no cash movement.
- Pending credits are excluded; pending debits reserve supplied settlement
  information.
- Explicit confirmed future movements and explicitly confirmed salary only.
- Historical salary does not create unsupported future income; terminal payroll
  stops extrapolation.
- Replacements require their own supplied amount/date/currency evidence.
- Minimum balance is checked after every movement and payment over the 90-day
  horizon.
- User payment preferences, supplied installment options, protected categories,
  flexible-action legality, payment grammar, deterministic validation/ranking,
  and the exact eight-column output contract.

These rules are not changed to improve solved-example scores.
