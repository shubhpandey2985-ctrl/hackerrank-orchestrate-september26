# Policy Decisions

This file separates challenge requirements from evidence-supported behavior and
explicit policies that remain unresolved. It is not a substitute for the
authoritative problem statement.

| Area | Decision | Classification | Rationale |
|---|---|---|---|
| Minimum balance / 90-day safety | Never fall below profile minimum after every movement and plan payment | SPECIFICATION-EXPLICIT | Direct safety contract |
| FX | Dated direct supplied rate only; Decimal arithmetic | SPECIFICATION-EXPLICIT | Direct input/output contract |
| Pending credit | Exclude from available capacity | SPECIFICATION-EXPLICIT | 90-day rule explicitly ignores pending credits |
| Pending debit | Reserve on supplied settlement date | STRONGLY-EXAMPLE-SUPPORTED | Conservative use of supplied pending settlement fact |
| Failed/cancelled/unrealized | No cash movement | SPECIFICATION-EXPLICIT | Explicit forecast exclusion |
| Lifecycle duplicate | Prefer settled/scheduled/pending over lower-precedence duplicate; retain provenance | STRONGLY-EXAMPLE-SUPPORTED | Prevents double counting while preserving evidence |
| Confirmed future salary | Use only with explicit amount and date | SPECIFICATION-EXPLICIT | Confirmed future payments are forecast inputs |
| Historical salary | Do not extrapolate from history alone | STRONGLY-EXAMPLE-SUPPORTED | Prevents invented income; terminal examples support this |
| Message salary | Use when message explicitly gives amount and date | STRONGLY-EXAMPLE-SUPPORTED | Samples 14/15 confirm this pattern |
| Generic scheduled credit | Exclude unless explicit confirmation makes it usable | UNRESOLVED-POLICY | Specification distinguishes confirmed future payments but does not define every scheduled label |
| Recurrence identity | Use category, description/merchant, direction and currency; never category alone | STRONGLY-EXAMPLE-SUPPORTED | Avoids merging unrelated purchases |
| Fixed recurrence amount | Project only when all observed home amounts are equal | STRONGLY-EXAMPLE-SUPPORTED | “Supported fixed recurrence” baseline; no estimator invented |
| Variable recurrence amount | `RECURRING_AMOUNT_UNRESOLVED`; do not project | SPECIFICATION-EXPLICIT | No mean/median/latest rule is supplied; do not invent amount |
| Recurrence threshold/gap/month-end | Current configured values remain explicit policy | UNRESOLVED-POLICY | Numeric rules absent from specification |
| Terminal recurrence | Final/last/ended/terminated/cancelled/failed stops projection | STRONGLY-EXAMPLE-SUPPORTED | Lifecycle evidence must prevent invented future movements |
| Replacement event | Use only its supplied date/amount; never infer replacement | SPECIFICATION-EXPLICIT | No unsupported financial information |
| Protected events | Include always; never modify | SPECIFICATION-EXPLICIT | Essential/protected expense contract |
| Flexible events | Modify only recurring, flexible, non-protected events | SPECIFICATION-EXPLICIT | Exact spending-change contract |
| Optional baseline | Keep separate from protected baseline; do not use changes unless candidate includes them | STRONGLY-EXAMPLE-SUPPORTED | Prevents safe amount depending on candidate ranking |
| Same-day order | Credits before required debits before plan payment | UNRESOLVED-POLICY | Existing explicit policy; no sample isolates the order |
| Deadline | Valid plan must complete by desired date | SPECIFICATION-EXPLICIT | Hard candidate constraint |
| Late capacity status | Capacity date and deadline compliance are separate; conservative mapping retained | UNRESOLVED-POLICY | Status boundary not fully specified |
| Ranking | Use published six-key ranking unchanged | SPECIFICATION-EXPLICIT | Do not repair forecast errors downstream |
| Flexible-action ties | Stable event/action ordering after published keys tie | UNRESOLVED-POLICY | No tie fixture establishes official rule |

## Phase 14 semantic-resolution gate

The formal movement contract marks every raw event as `INCLUDED_BECAUSE` or
`EXCLUDED_BECAUSE` and preserves recurrence, lifecycle and provenance metadata.
Phase 14 did not identify a single evidence-supported repair for the 23
safe-amount first divergences. Variable estimators, calendar thresholds,
generic scheduled-credit inclusion, same-day changes and invented replacements
remain prohibited. The production forecast is unchanged.

## Phase 15 fixture-driven semantic discovery

Added an independent Decimal semantic laboratory with 66 synthetic fixtures.
Resolved lab rules cover lifecycle exclusions, pending-credit treatment, direct
FX failure, Decimal arithmetic, confirmed-income boundaries and explicit
replacement evidence. Variable amounts, recurrence calendars, optional
baseline, same-day ordering and late-deadline mapping remain unresolved by
available challenge evidence. The lab is analysis-only; production behavior is
unchanged.
| Decimal serialization | Exact Decimal internally; deterministic output scale remains explicit | UNRESOLVED-POLICY | Trailing-zero rule absent |

## Phase 13 evidence-to-behavior reconstruction

The Phase 13 matrix and causal traces confirm that safe amount is the first
observable divergence for 23/25 solved examples, while two rows are
serialization-only. This is an upstream forecast-contract signal, not evidence
that candidate ranking is wrong. The strongest general model remains explicit
confirmed movements plus supported stable fixed recurrence. No variable-amount
estimator or sample-specific semantic change is authorized.

## Phase 16 evidence-weighted reconstruction

The actual call graph and canonical movement contract were reverified. Stable
fixed recurrence remains the strongest defensible model. Latest, median, mean,
maximum and recurrence-conditioned variable estimators are unsupported
assumptions; calendar, optional-baseline, same-day and late-deadline boundaries
remain configurable. No production change passed the evidence gate.

## Phase 17 forecast contract implementation

Formalized the three-level inference contract: `EXPLICIT_CONFIRMED` and
`SUPPORTED_FIXED_RECURRENCE` are production-eligible; `UNRESOLVED_INFERENCE`
remains visible but contributes no cash. The model lab is analysis-only and no
counterfactual estimator or calendar model was promoted.

## Phase 18 authoritative evidence gate

Repository-wide search found no authoritative rule resolving variable amounts,
calendar recurrence, optional baseline, generic scheduled credits, same-day
order, replacement timing or late-deadline mapping. Decision:
`AUTHORITATIVE_EVIDENCE_MISSING`; production behavior remains unchanged.

## Phase 19 production policy boundary

Unresolved semantics are centralized, explicit and fail-closed. Fixed-only
variable spending, observed-interval recurrence, confirmed-salary-only credits,
never-invent replacements, configurable same-day ordering and conservative
deadline mapping are documented policies. The hidden-test hardening suite adds
invariant coverage without changing financial decision logic.
