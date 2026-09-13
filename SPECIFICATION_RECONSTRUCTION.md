# Specification Reconstruction

Status: analysis-only. This document records a read-only reconstruction of the
challenge semantics. No production code, supplied dataset, or expected output
was modified. The current solver was evaluated as-is; the counterfactuals were
in-memory substitutions only.

## Executive conclusion

The specification is explicit about the safety invariant, the 90-day horizon,
pending/failed/cancelled exclusions, minimum balance, hard payment-method
eligibility, exact partial-payment contract, and plan ranking. It is not
explicit about the statistic or threshold used to turn repeated variable
spending into a future amount, same-day settlement order, generic scheduled
credits, recurrence tolerances/month-end behavior, failed-obligation
replacement timing, late-deadline status mapping, decimal presentation, or
ties between equally valid flexible changes.

The current Decimal arithmetic mean for repeated variable spending is not
authorized by the specification or any repeated sample behavior. It must not
be treated as the canonical rule. Historical salary recurrence is likewise
unsafe unless a future credit is explicitly confirmed; a final/ended payroll
must not be extrapolated. These are upstream ledger questions, not ranking
questions.

## Evidence hierarchy

1. Exact problem-statement text is binding.
2. An explicit solved-example fact is evidence for that fixture and, where
   repeated consistently, strong evidence for a general rule.
3. Repeated sample behavior may resolve an otherwise underspecified boundary,
   but is not permission to invent a numerical policy.
4. Remaining gaps are explicit policy choices and must be documented and tested.

## Semantic reconstruction

### Variable spending

The specification says to distinguish recurring expenses and to forecast
recurring expenses over 90 days. It does not define “recurring” numerically,
does not prescribe a mean/median/latest statistic, and does not say that every
repeated category is a future obligation. The current arithmetic mean is
therefore an unsupported assumption. Category/direction/currency is a useful
candidate identity for investigation, but the specification does not make it
the identity; merchant/description/source may be necessary to avoid combining
unrelated purchases. Only a validated recurring event marked flexible may be
changed. Protected categories from the profile and non-flexible events remain
protected. Optional variable spending is not automatically zero, nor is it
automatically a protected obligation: its baseline treatment is unresolved.

Strongest defensible rule: forecast only a repeated series when recurrence is
supported by the available history or explicit evidence; do not use an
arithmetic mean as an official rule. Preserve every source amount and
provenance. The amount estimator, observation threshold, category identity and
optional-baseline treatment remain explicit unresolved policy.

### Income / salary

Settled credits affect the ledger on their settlement/event date. A supplied
next confirmed salary is a confirmed future credit and may be used on its
settlement date. Messages can confirm a salary amount/date; the typed fact is
usable only when the message supplies both, and the message remains
provenance. Historical salary observations alone do not authorize inventing
future money. A final, last, ended, or employment-terminated payroll is a
terminal fact; no later salary recurrence may be extrapolated unless a later
explicit confirmation exists. A missed historical cycle is not evidence of a
new credit.

### Scheduled credits

The explicit 90-day rule allows confirmed future payments. An explicitly
confirmed scheduled salary is usable. A generic scheduled credit without a
confirmation/amendment is ambiguous; conservative policy is to exclude it
from available future capacity and retain it as excluded evidence. Never
invent a date, amount, inverse FX rate, or substitute credit.

### Pending events

Pending credits are ignored for the safety forecast. Pending debits are not
available cash and should be reserved using their supplied settlement date (or
the event date only under an explicitly documented fallback when no settlement
date exists). Pending status does not turn an amount into zero and cannot make a
plan safe. Their treatment is part of the canonical lifecycle and must be
identical for safe amount, earliest date, and candidate validation.

### Protected, optional and flexible obligations

| Evidence/event property | Essential/protected | Flexible/modifiable | Baseline treatment |
|---|---:|---:|---|
| Profile `expense_categories_to_protect` match | yes | no | always include; never change |
| Event `flexibility` non-flexible/fixed | yes for safety | no | include; reject any change |
| Recurring event explicitly marked flexible and not protected | no | yes | include unless a validated stop/reduction is selected |
| One-time debit | obligation if settled/confirmed | no | include only on its supplied date |
| Pending debit | reserved obligation | no | include on settlement date |
| Failed/cancelled/unrealized/non-cash row | no cash movement | no | exclude, retain provenance |
| Generic repeated category with no recurrence evidence | unresolved | unresolved | do not invent a movement |

Category names alone do not establish protection. Profile priorities,
per-event flexibility and explicit evidence must be consulted. A spending
change is valid only for a recurring flexible event, may stop or reduce it, is
limited to three actions, and may not stop and reduce the same event.

### Same-day ordering

The specification requires the balance never to fall below the minimum after
every movement but does not say whether a same-day credit settles before a
debit or plan payment. The current implementation uses credit-before-debit-
before-plan as an explicit policy. A conservative alternative is to test the
pre-credit balance and reject a payment that requires unsettled same-day
income. No supplied example proves either order, so this remains unresolved
and must be measured in focused tests.

### Recurrence and lifecycle

Recurrence identity, minimum observations, gap tolerance, month-end rollover,
missed cycles, and terminal behavior are not numerically specified. The
specification does require distinguishing recurring expenses from one-time or
unusual events and says explicit cancellation/settlement/amendment wins when
records conflict. A failed/cancelled row is excluded. A linked live replacement
may be used only when its own date and amount are supplied; replacement timing
must never be invented.

### Deadlines and statuses

Payment is safe only when every payment completes by the desired completion
date and the 90-day minimum never fails. `affordable_now` requires a safe full
payment today and user acceptance of `full_payment`. `affordable_with_plan`
requires an eligible, validated plan completing by the deadline. `affordable_later`
means full payment is expected to become safe later; the exact mapping when
capacity first appears after the deadline is not stated. `not_affordable` is
the fallback when no safe eligible completion exists within the forecast.
Capacity date and recommendation eligibility must remain separate.

### Payment methods

User payment preferences are hard eligibility constraints for full, partial and
installment methods. Wait is eligible only when full payment later is safe and
the user accepts full payment. Supplied installment options must be reproduced
exactly. Among eligible safe plans, the specification gives the exact ranking:
complete by deadline, no spending changes, minimize total paid, start earlier,
fewer payments, then lowest `payment_option_id`.

### Currency and output

Amounts are in home currency. Conversion uses the supplied dated direct rate
matching the event settlement/event date and currency pair. No inverse,
triangulated, substitute-date or invented rate is permitted. Decimal arithmetic
must be exact. The eight output columns and payment-plan grammar are explicit;
trailing-zero and final decimal scale behavior are not, so serialization must
be deterministic and documented separately from arithmetic.

## Evidence matrix

| RULE-ID | Rule | Specification evidence | Example evidence | Affected examples | Alternative interpretations / impact | Confidence | Classification |
|---|---|---|---|---|---|---|---|
| VAR-01 | Do not use a Decimal arithmetic mean as an authoritative forecast for variable spending | No mean/statistic is defined; do not invent expenses | Low safe/date matches after mean policy; no sample states mean | 01,02,03,04,06,07,08,11,13,17,18,19,21,22,23,24,25 | Explicit recurring-only vs conservative statistic changes amount/date and downstream plans | High | UNSUPPORTED ASSUMPTION |
| VAR-02 | A repeated series must be supported as recurring before projection | Recurring expenses must be distinguished from one-time/unusual events | Subscription and repeated obligations behave consistently | recurring users, especially 01,04,14,15,22 | Broad category grouping over-forecasts unrelated purchases | High | SPECIFICATION-EXPLICIT |
| VAR-03 | Category/direction/currency alone define recurrence identity | Not stated | Some category series appear related, but descriptions vary | 01,06,11,21 | Description/source identity would reduce false recurrence | Low | WEAKLY EXAMPLE-SUPPORTED |
| VAR-04 | Statistic for repeated variable amount | Not stated | No example proves mean, median, latest, max, or fixed amount | variable-spend users | Each statistic changes safe amount; score cannot decide authority | High | UNRESOLVED |
| INC-01 | Settled/confirmed salary is usable on supplied settlement date | Confirmed future payments are forecast inputs | Scheduled/confirmed salary examples 14,15,25 | 14,15,25 | Using historical cadence alone invents cash | High | SPECIFICATION-EXPLICIT |
| INC-02 | Message-confirmed salary with explicit amount and date becomes typed evidence | Messages may clarify/confirm facts; do not invent | 14 and 15 explicitly confirm salary/date | 14,15 | Parsing incomplete message is unsafe | High | STRONGLY EXAMPLE-SUPPORTED |
| INC-03 | Final/ended payroll terminates extrapolation | Do not invent unsupported income | 05 final payroll; no later confirmed salary | 05 and salary-series users | Continuing recurrence creates false capacity | High | STRONGLY EXAMPLE-SUPPORTED |
| SCH-01 | Explicit confirmed scheduled salary counts at settlement | Confirmed future payments are allowed | 25 next confirmed salary | 25 | Generic scheduled credit differs | High | SPECIFICATION-EXPLICIT |
| SCH-02 | Generic scheduled credit without confirmation | “Confirmed future payments” is narrower than scheduled | Mixed scheduled rows do not establish guarantee | 01,13,17,21,25 | Include vs exclude materially changes capacity | Medium | UNRESOLVED |
| PEN-01 | Pending credit is excluded | 90-day rule explicitly says ignore pending credits | Pending-credit users | 02,03,20,22,23 | Counting it creates invented capacity | High | SPECIFICATION-EXPLICIT |
| PEN-02 | Pending debit is reserved at settlement | Pending payments must be considered; settlement date supplied | Pending-debit traces | 02,03,20,22,23 | Event-date fallback is policy when settlement missing | Medium | STRONGLY EXAMPLE-SUPPORTED |
| LIFE-01 | Failed/cancelled/unrealized/non-cash rows have no cash movement | Explicitly ignored by 90-day rule | Lifecycle rows and linked amendments | multiple | Linked live replacement only on supplied facts | High | SPECIFICATION-EXPLICIT |
| LIFE-02 | Replacement obligation timing/amount | No replacement rule | No example proves inferred replacement | lifecycle users | Inventing replacement is unsafe | High | UNRESOLVED |
| PROT-01 | Profile-protected categories are hard obligations | Cover essential/protected expenses | Expected changes preserve protected expenses | 04,06,11,19,21 | Category-only inference can misclassify | High | SPECIFICATION-EXPLICIT |
| PROT-02 | Only recurring flexible events may be stopped/reduced | Exact spending-change contract | Stop/reduce examples 06,11,21 | 06,11,19,21 | One-time/non-flexible actions must reject | High | SPECIFICATION-EXPLICIT |
| PROT-03 | Whether optional variable spending belongs in baseline | “Before optional spending changes” and recurring forecast both appear | Samples do not isolate this boundary | 01,04,06,11,19,21 | Exclude vs include changes safe amount and date | Medium | UNRESOLVED |
| SAME-01 | Same-day settlement ordering | Not stated | No sample isolates same-day credit/debit/payment | any same-day case | Credit-first vs conservative pre-credit affects feasibility | High | UNRESOLVED |
| REC-01 | Threshold/gap/month-end/missed-cycle policy | Not stated | Monthly examples show cadence but not tolerance | 01,04,14,15,22 | Different calendars shift future flows | High | UNRESOLVED |
| REC-02 | Cancellation/failure/terminal facts stop recurrence | Conflict precedence and ignored failures are explicit | Final payroll 05 | 05 and lifecycle cases | Continue recurrence invents cash/expense | High | STRONGLY EXAMPLE-SUPPORTED |
| DEAD-01 | Deadline is a hard plan constraint | Plan must complete by desired date | Installment/partial examples | 02,03,04,19 | Post-deadline capacity cannot make an in-deadline plan valid | High | SPECIFICATION-EXPLICIT |
| DEAD-02 | Mapping of safe-after-deadline capacity | Status definitions do not resolve late boundary | Mixed late cases 03,04,08,10,13,20,24,25 | affordable_later vs not_affordable remains ambiguous | Medium | UNRESOLVED |
| METHOD-01 | User preference is hard eligibility | Immediate methods and wait acceptance rules | Preference mismatches appear when upstream dates change | all | Ignoring preference invalidates plan | High | SPECIFICATION-EXPLICIT |
| METHOD-02 | Ranking order as published | Six ordered ranking rules | Sample plans reflect order | 02,06,11,19,21 | No alternate rank is justified | High | SPECIFICATION-EXPLICIT |
| FX-01 | Use only dated direct supplied FX | Rates matched by date/pair; no live rates | Foreign-currency samples | 01,02,03,04,11,21 | Missing direct rate must fail/omit, never invent | High | SPECIFICATION-EXPLICIT |
| SER-01 | Eight columns/order/plan grammar | Required-output section | All 25 rows conform | all | Trailing zeros remain unspecified | High | SPECIFICATION-EXPLICIT |
| SER-02 | Decimal trailing-zero policy | Not stated | 603.3/603.30-style observations | 06,09,21 | Preserve meaningful supplied precision vs normalized Decimal | Medium | UNRESOLVED |
| FLEX-01 | Tie between equally valid flexible action sets | No tie rule | No fixture uniquely proves a tie | 06,11,21 | Stable event/action key is a policy choice | High | UNRESOLVED |

## Counterfactual scoring

The analysis-only script `code/spec_counterfactual.py` temporarily replaced the
in-memory recurrence function and ran the unchanged candidate pipeline over all
25 solved rows. Counts below are field matches, not proof of correctness.

| Interpretation | Safe amount | Earliest date | Status | Method | Plan | Changes |
|---|---:|---:|---:|---:|---:|---:|
| Current implementation (category recurrence, variable mean, income recurrence) | 2 | 9 | 15 | 17 | 14 | 22 |
| Remove variable-category recurrence | 3 | 4 | 17 | 19 | 15 | 22 |
| Explicit events only (remove all inferred recurrence) | 3 | 9 | 12 | 14 | 13 | 22 |
| No historical income extrapolation | 1 | 8 | 8 | 8 | 8 | 22 |
| Fixed obligations only (remove variable and income recurrence) | 2 | 8 | 10 | 11 | 10 | 22 |

The score table demonstrates blast radius: recurrence semantics affect every
downstream field. It does not justify selecting “remove variable recurrence”
solely because it scores better on this fixture; that interpretation must still
be reconciled with the specification's recurring-expense requirement. Likewise,
removing all income recurrence scores poorly because it also removes explicit
recurring fixed income that may be supported. The defensible repair direction
is to distinguish explicit confirmed credits from unsupported historical
extrapolation and to resolve variable recurrence evidence, not to maximize a
single table.

## RECOMMENDED_SEMANTIC_MODEL

1. Load and validate every schema with Decimal values, preserve source IDs and
   evidence provenance, and fail closed on missing amounts or missing direct FX.
2. Build an immutable canonical ledger. Exclude failed, cancelled, unrealized,
   non-cash rows and duplicate lifecycle records. Exclude pending credits;
   reserve pending debits using supplied settlement dates. Use only explicit
   settled/confirmed future credits, including message-confirmed salary facts
   with both amount and date. Do not extrapolate a historical salary after a
   terminal payroll or without explicit future confirmation.
3. Detect recurrence as evidence, not as permission to invent amounts. Keep
   recurrence identity, cadence, source rows, amount observations and terminal
   markers. Do not use a Decimal arithmetic mean as an authoritative variable-
   spending rule. Until resolved, expose the amount estimator and optional-
   baseline treatment as named policy configuration with trace output.
4. Normalize every usable movement to home currency using only the dated direct
   supplied rate. Keep exact Decimal arithmetic; no intermediate rounding.
5. Forecast day-by-day over the inclusive 90-day contract used by the solver,
   applying the documented same-day policy consistently to all queries. Check
   the minimum after every movement and after each candidate payment.
6. Compute safe amount as a monotone deterministic capacity query before
   optional changes, capped to the request. Compute earliest full-payment date
   independently of payment-method preference and separately record whether it
   meets the deadline.
7. Generate only deterministic candidates: full payment, exact two-payment
   partial plan, supplied installments reproduced exactly, wait, and up to
   three permitted flexible actions. Never invent options or silently repair an
   invalid plan.
8. Validate every candidate against ledger flows, minimum balance, horizon,
   deadline, preference, payment sums, protected categories and action rules.
   Rank valid candidates only with the published six-key ordering, followed by
   an explicit stable action-set tie policy if all published keys tie.
9. Generate explanations only from the validated fact bundle. An LLM may
   extract unstructured evidence or phrase the explanation, but cannot alter
   arithmetic, affordability, ranking or validation.
10. Emit the exact eight columns, deterministic Decimal strings and payment-plan
    grammar; run schema, invariant, determinism, sample-comparison and
    adversarial regression checks.

## UNRESOLVED_SEMANTICS

Only the following decisions remain genuinely unsupported by the supplied
specification and examples:

- the numeric statistic and evidence threshold for repeated variable spending;
- whether optional flexible variable spending is included in baseline safe
  capacity or treated as optional capacity throughout;
- recurrence gap tolerance, minimum observations, month-end rollover, missed
  cycles and terminal recurrence details;
- same-day credit/debit/payment ordering;
- generic scheduled-credit usability without explicit confirmation;
- timing and amount of a replacement obligation when the source row fails or
  is cancelled;
- status mapping when capacity first appears after the requested deadline;
- deterministic ties between equally valid flexible action sets;
- final decimal scale/trailing-zero serialization.

These must be documented as policy, tested with focused fixtures, and surfaced
in audit traces. They must not be disguised as specification-mandated rules.
