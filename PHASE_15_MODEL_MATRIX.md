# Phase 15 Differential Model Matrix

| Model | Safety | Spec support | Example support | Hidden-test risk | Complexity | Recommendation |
|---|---|---|---|---|---|---|
| A explicit only | safe in lab | high | partial | medium false negatives | low | analysis baseline |
| B explicit + stable fixed | safe in lab | strongest current | current baseline | medium | medium | retain production |
| C explicit + calendar | safe when dates defined | unresolved | indistinguishable | high month-end risk | medium | analysis only |
| D explicit + variable estimator | can be safe but amount invented | unsupported | score evidence only | high | high | reject |
| E optional excluded | safe | unresolved boundary | counterfactual only | medium | low | configurable |
| F optional included | safe | unresolved boundary | counterfactual only | medium | low | configurable |
| G conservative same-day | safe | policy | no isolating sample | medium | low | configurable |
| H credit-first same-day | safe | policy | current policy | medium | low | current explicit policy |

No model is promoted solely by sample score.

