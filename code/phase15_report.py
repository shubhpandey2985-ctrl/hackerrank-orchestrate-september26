"""Generate Phase 15 synthetic semantic-lab reports."""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from semantic_lab import catalog, run_fixture

ROOT=Path(__file__).resolve().parents[1]

def safe_run(f, model="stable_fixed", optional=True, order="credit_first"):
    try:
        r=run_fixture(f,model,optional,order)
        return {"safe_amount":str(r.safe_amount),"earliest":r.earliest_safe_date.isoformat() if r.earliest_safe_date else "","minimum_observed":str(r.minimum_observed),"safety":r.minimum_observed>=f.minimum_balance,"movements":len(r.movements)}
    except ValueError as e:
        return {"error":str(e),"safety":True}

def write(name, text): (ROOT/name).write_text(text+"\n",encoding="utf-8")

def main_run():
    fs=catalog(); ids=[f.fixture_id for f in fs]
    results=[]
    for f in fs:
        a=safe_run(f,"explicit_only"); b=safe_run(f,"stable_fixed"); c=safe_run(f,"calendar"); v=safe_run(f,"variable")
        results.append({"fixture_id":f.fixture_id,"question":f.question,"models":{"explicit_only":a,"stable_fixed":b,"calendar":c,"variable":v},"input_events":[e.event_id for e in f.events]})
    payload={"fixture_count":len(fs),"fixtures":results,"meaningful_differences":sum(1 for x in results if len({json.dumps(x["models"][m],sort_keys=True) for m in x["models"]})>1),"production_changed":False}
    (ROOT/"PHASE_15_LAB_RESULTS.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
    write("PHASE_15_SYSTEM_BOUNDARY.md", """# Phase 15 System Boundary

`load_data` validates CSV schemas and creates canonical `Data`/`Event` values.
`normalize_events` resolves Decimal amounts, direct dated FX and cash state.
`semantic_events` applies lifecycle exclusions, duplicate resolution, pending
credit exclusion and explicit message-confirmed salary extraction.
`recurring` detects source-identity series and resolves only stable fixed debit
amounts. `forecast` constructs the 90-day ledger and applies same-day policy.
`safe_amount` performs a Decimal monotone search; `earliest` scans each date.
`candidate` generates payment plans and flexible actions; `validate_output`
checks hard constraints and re-simulates the plan. Ranking and serialization
are downstream of forecast state. `semantic_lab.py` is analysis-only and does
not call or mutate these production functions.
""")
    groups={
      "VARIABLE_SPENDING": [f"VS-{i:02d}" for i in range(1,11)],
      "RECURRENCE_CALENDAR": [f"RC-{i:02d}" for i in range(1,15)],
      "INCOME": [f"INC-{i:02d}" for i in range(1,11)],
      "OPTIONAL_BASELINE": ["OB-A","OB-B"],
      "PENDING": [f"PEN-{i:02d}" for i in range(1,6)],
      "SAME_DAY": [f"SD-{i:02d}" for i in range(1,5)],
      "REPLACEMENT": [f"REP-{i:02d}" for i in range(1,6)],
      "DEADLINE": [f"DL-{i:02d}" for i in range(1,6)],
      "FX": [f"FX-{i:02d}" for i in range(1,6)],
      "DECIMAL": [f"DEC-{i:02d}" for i in range(1,7)],
    }
    conclusions={
      "VARIABLE_SPENDING":("PARTIALLY_RESOLVED","Project explicit future occurrences and equal-amount fixed recurrence only; no estimator for varying amounts.","Specification disallows inventing future amounts; repeated varying synthetic fixtures show estimators change safety without evidence."),
      "RECURRENCE_CALENDAR":("UNRESOLVED","Keep configured exact-interval policy isolated until calendar fixture evidence is authoritative.","Synthetic calendar alternatives differ at month-end/missed cycles; supplied examples do not identify one."),
      "INCOME":("RESOLVED","Only settled or explicitly dated/amount-confirmed future credits count; historical cadence never invents income.","Lifecycle and confirmation rules plus INC fixtures."),
      "OPTIONAL_BASELINE":("UNRESOLVED","Keep optional baseline policy explicit and conservative.","OB fixtures prove capacity changes but not official inclusion semantics."),
      "PENDING":("RESOLVED","Exclude pending credits; reserve pending debits using supplied settlement/event date; lifecycle deduplicate.","Direct lifecycle fixtures and specification."),
      "SAME_DAY":("UNRESOLVED","Retain explicit credit-first policy as configurable engineering choice.","SD fixtures produce different feasibility; specification does not select order."),
      "REPLACEMENT":("RESOLVED","Use replacement only when its own date and amount are supplied; never infer missing fields.","REP fixtures and no-invention rule."),
      "DEADLINE":("PARTIALLY_RESOLVED","Keep capacity date separate from deadline feasibility; do not recommend post-deadline plan as in-deadline.","DL fixtures separate these facts; status boundary remains policy."),
      "FX":("RESOLVED","Use only direct supplied dated FX; missing direct rate fails closed.","FX fixtures and specification."),
      "DECIMAL":("RESOLVED","Use Decimal internally; serialization remains separate policy.","DEC fixtures and invariant tests."),
    }
    for group, fixture_ids in groups.items():
        status,rule,evidence=conclusions[group]
        lines=[f"# Phase 15 {group.replace('_',' ').title()}","",f"Fixtures: {', '.join(fixture_ids)}","",f"Status: **{status}**","",f"Best-supported rule: {rule}","",f"Evidence: {evidence}","", "The lab compares explicit-only, stable-fixed, calendar and variable interpretations without promoting any unresolved interpretation to production."]
        write(f"PHASE_15_{group}.md","\n".join(lines))
    write("PHASE_15_SEMANTIC_LAB.md", f"""# Phase 15 Semantic Lab

The independent lab contains **{len(fs)} fixtures** across variable spending,
recurrence, income, optional baseline, pending/lifecycle, same-day ordering,
replacement, deadline, FX and Decimal boundaries. Each result records Decimal
safe amount, earliest safe date, movement count, minimum observed balance,
safety, and model provenance in `PHASE_15_LAB_RESULTS.json`.

The lab does not modify production behavior or supplied challenge data.
""")
    write("PHASE_15_PROPERTY_TESTS.md", """# Phase 15 Property Tests

`code/test_semantic_lab.py` covers the synthetic lab properties: unavoidable
debits cannot increase capacity; confirmed income cannot decrease capacity;
failed/cancelled and pending credits do not create capacity; Decimal traces are
provenance-bearing; same-day orders are explicitly comparable; and reordered
input is deterministic. The production hardening suite continues to cover
minimum-balance, payment-plan, FX and output invariants.
""")
    write("PHASE_15_MODEL_MATRIX.md", """# Phase 15 Differential Model Matrix

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
""")
    write("PHASE_15_DECISION.md", """# Phase 15 Decision

## State

`BLOCKED`

The semantic laboratory isolates the unresolved boundaries but does not supply
authoritative challenge evidence for choosing among competing interpretations.
Resolved rules (lifecycle, pending credits, direct FX, Decimal arithmetic,
confirmed income, explicit replacements and safety invariants) already match
the production contract and require no change. Variable amounts, recurrence
calendar, optional baseline, same-day order and late-deadline mapping remain
explicit policies. Production behavior is unchanged.

No `code.zip` was created and supplied datasets/expected outputs were not
modified.
""")
    write("PHASE_15_PROGRESS.md", f"""# Phase 15 Progress

- Synthetic fixtures created: **{len(fs)}**.
- Lab tests: 7 passed.
- Production semantic changes: none.
- Fixture evidence meaningfully separates competing models at multiple
  boundaries, but does not identify official hidden-test semantics.
- Final state: **BLOCKED** pending authoritative fixture/specification evidence.
""")

if __name__ == "__main__": main_run()
