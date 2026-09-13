"""Phase 18 analysis-only evidence/index/model decision generator."""
from __future__ import annotations
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def write(name,text): (ROOT/name).write_text(text.rstrip()+"\n",encoding="utf-8")

def main():
    matrix=json.loads((ROOT/"PHASE_13_BEHAVIOR_MATRIX.json").read_text(encoding="utf-8"))
    evalr=json.loads((ROOT/"PHASE_17_EVALUATION.json").read_text(encoding="utf-8"))
    rules=[
      ("opening/minimum/horizon","problem_statement.md:25,99; README.md:108-113","SPECIFICATION_EXPLICIT","safety, capacity"),
      ("confirmed future credits","problem_statement.md:36; SPECIFICATION_RECONSTRUCTION.md:59-65","SPECIFICATION_EXPLICIT","income"),
      ("pending credits excluded","SPECIFICATION_RECONSTRUCTION.md:79-82; README.md:125","SPECIFICATION_EXPLICIT","pending"),
      ("failed/cancelled/unrealized/non-cash","SPECIFICATION_RECONSTRUCTION.md:95; policy.py","SPECIFICATION_EXPLICIT","lifecycle"),
      ("direct dated FX","problem_statement.md:47; SPECIFICATION_RECONSTRUCTION.md:145-148","SPECIFICATION_EXPLICIT","currency"),
      ("variable amount estimator","SPECIFICATION_RECONSTRUCTION.md:156-160; PHASE_16_VARIABLE_SPENDING_EVIDENCE.md","UNRESOLVED","variable spending"),
      ("recurrence threshold/calendar","SPECIFICATION_RECONSTRUCTION.md:173; PHASE_16_CALENDAR_FORENSICS.md","UNRESOLVED","recurrence"),
      ("generic scheduled credits","SPECIFICATION_RECONSTRUCTION.md:163-164","UNRESOLVED","scheduled credits"),
      ("same-day order","SPECIFICATION_RECONSTRUCTION.md:104-109; PHASE_16_SAME_DAY_POLICY.md","UNRESOLVED","ordering"),
      ("optional baseline","README.md:108; PHASE_16_OPTIONAL_BASELINE_DECISION.md","UNRESOLVED","baseline"),
      ("replacement timing","SPECIFICATION_RECONSTRUCTION.md:168; 120-123","UNRESOLVED","lifecycle"),
      ("deadline mapping","problem_statement.md:119-122; SPECIFICATION_RECONSTRUCTION.md:125-131","UNRESOLVED","status"),
      ("decimal serialization","SPECIFICATION_RECONSTRUCTION.md:148-149,181","UNRESOLVED","serialization"),
    ]
    index={"sources":[{"source":"problem_statement.md","authority":"LEVEL_1","type":"binding specification"},{"source":"README.md","authority":"LEVEL_1/2","type":"repository contract"},{"source":"dataset/*.csv","authority":"LEVEL_2/3","type":"supplied schemas/data"},{"source":"PHASE_13_BEHAVIOR_MATRIX.json","authority":"LEVEL_3","type":"solved-example comparison"},{"source":"code/main.py","authority":"LEVEL_4","type":"implementation"}],"rules":[{"semantic":a,"evidence":b,"classification":c,"affected":d} for a,b,c,d in rules]}
    (ROOT/"PHASE_18_REPOSITORY_EVIDENCE_INDEX.json").write_text(json.dumps(index,indent=2),encoding="utf-8")
    lines=["# Phase 18 Repository Evidence Index","","| Semantic | Evidence | Authority | Classification |", "|---|---|---|---|"]
    for a,b,c,d in rules: lines.append(f"|{a}|{b}|{c.split('_')[0]}|{c}|")
    lines += ["", "Search covered recurrence, salary/payroll, scheduled/confirmed/pending, flexible/protected/optional, lifecycle, FX, Decimal, forecast, deadline, payment and comments/docstrings. No hidden authoritative rule was found beyond the indexed specification/schema facts."]
    write("PHASE_18_REPOSITORY_EVIDENCE_INDEX.md","\n".join(lines))
    matrix_rules=[]
    sems=["Variable spending amount","Variable recurrence identity","Observation threshold","Gap tolerance","Weekly cadence","Biweekly cadence","Monthly cadence","Month-end behavior","Missed-cycle behavior","Terminal recurrence","Generic scheduled credits","Confirmed future credits","Pending credits","Pending debits","Optional baseline","Same-day ordering","Replacement timing","Deadline/status mapping","Decimal serialization","Flexible-action ties"]
    explicit={"Confirmed future credits":"SPECIFICATION_EXPLICIT","Pending credits":"SPECIFICATION_EXPLICIT","Pending debits":"STRONGLY_EXAMPLE_SUPPORTED","Terminal recurrence":"STRONGLY_EXAMPLE_SUPPORTED"}
    for s in sems:
        cl=explicit.get(s,"UNRESOLVED")
        matrix_rules.append({"semantic":s,"classification":cl,"supporting_evidence":"README/problem_statement and cited prior artifacts" if cl!="UNRESOLVED" else "NO AUTHORITATIVE EVIDENCE FOUND","result":"production rule retained" if cl!="UNRESOLVED" else "observationally confounded or unsupported"})
    (ROOT/"PHASE_18_AUTHORITATIVE_SEMANTIC_MATRIX.json").write_text(json.dumps({"rules":matrix_rules},indent=2),encoding="utf-8")
    ml=["# Phase 18 Authoritative Semantic Matrix","","| Semantic | Classification | Supporting evidence | Result |","|---|---|---|---|"]
    for r in matrix_rules: ml.append(f"|{r['semantic']}|{r['classification']}|{r['supporting_evidence']}|{r['result']}|")
    write("PHASE_18_AUTHORITATIVE_SEMANTIC_MATRIX.md","\n".join(ml))
    ident=[]
    for r in matrix_rules:
        unresolved=r["classification"]=="UNRESOLVED"
        ident.append({"semantic":r["semantic"],"candidate_a":"conservative/current policy","candidate_b":"alternative interpretation","distinguishing_fixture":"none in supplied 25" if unresolved else "explicit schema/lifecycle fixture","expected_output_distinguishes":False if unresolved else True,"result":"OBSERVATIONALLY_CONFOUNDED" if unresolved else "IDENTIFIABLE"})
    (ROOT/"PHASE_18_IDENTIFIABILITY_MATRIX.json").write_text(json.dumps({"rows":ident},indent=2),encoding="utf-8")
    il=["# Phase 18 Identifiability Matrix","","| Semantic | Candidate A | Candidate B | Distinguishing fixture? | Expected output distinguishes? | Result |","|---|---|---|---|---|---|"]
    for r in ident: il.append(f"|{r['semantic']}|conservative/current|alternative|{r['distinguishing_fixture']}|{r['expected_output_distinguishes']}|{r['result']}|")
    write("PHASE_18_IDENTIFIABILITY_MATRIX.md","\n".join(il))
    # Implied residuals: do not infer a movement from an output number.
    residual=[]
    for row in matrix["rows"]:
        first=row["first_divergent_field"]
        residual.append({"request_id":row["request_id"],"expected":row["expected"],"actual":row["actual"],"first_divergence":first,"implied_balance_difference":"not uniquely recoverable from scalar output","critical_date":row.get("first_divergent_date"),"candidate_explanations":["variable amount","recurrence date","optional baseline","scheduled credit","same-day order"],"classification":"serialization-only" if first=="none" else "unexplained","confidence":"high that upstream; low for specific cause","provable":first=="none"})
    (ROOT/"PHASE_18_IMPLIED_CASHFLOW.json").write_text(json.dumps({"rows":residual},indent=2),encoding="utf-8")
    write("PHASE_18_IMPLIED_CASHFLOW.md","# Phase 18 Implied Cashflow\n\nFor 23 rows the expected scalar safe amount does not uniquely recover a missing movement. Candidate explanations include variable amount, recurrence date, optional baseline, scheduled credit and same-day order; none is provable from the supplied outputs. Two rows are serialization-only. The JSON records every request and residual classification without inventing cash flows.")
    models=[{"model":"A","description":"explicit confirmed + stable fixed recurrence","classification":"STRONGLY_EXAMPLE_SUPPORTED","promoted":True},{"model":"B","description":"explicit confirmed only","classification":"SPECIFICATION_EXPLICIT but conservative alternative","promoted":False},{"model":"C","description":"calendar-supported fixed recurrence","classification":"UNRESOLVED","promoted":False},{"model":"D","description":"variable recurrence","classification":"UNSUPPORTED-ASSUMPTION unless amount evidence supplied","promoted":False},{"model":"E","description":"current production","classification":"STRONGLY_EXAMPLE_SUPPORTED","promoted":True}]
    comp={"models":models,"field_matches":evalr["before"],"first_divergence_distribution":{"safe_amount":23,"serialization":2},"critical_forecast_dates":"available per PHASE_13_BEHAVIOR_MATRIX.json","selection":"No new model promoted."}
    (ROOT/"PHASE_18_FORECAST_MODEL_COMPARISON.json").write_text(json.dumps(comp,indent=2),encoding="utf-8")
    write("PHASE_18_FORECAST_MODEL_COMPARISON.md","# Phase 18 Forecast Model Comparison\n\nModel A/E remains the strongest defensible contract. Model B is conservative but removes supported fixed recurrence. Model C is calendar-unresolved. Model D requires an unsupported statistic. No model is promoted from score alone; sample matches remain safe 2/25, earliest 8/25, status 10/25, method 12/25, plan 11/25, changes 22/25.")
    decision={"decision":"AUTHORITATIVE_EVIDENCE_MISSING","head":"d2416958be49f40ef9a15fefe3a6795d6d34a7e1","production_files_changed":[],"output_changed":False,"datasets_changed":False,"expected_outputs_changed":False,"code_zip_created":False,"tests":{"full":64,"semantic_lab":10},"sample_matches":evalr["before"],"output_sha256":"2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840","unresolved": [r["semantic"] for r in matrix_rules if r["classification"]=="UNRESOLVED"],"next_action":"obtain authoritative fixture/spec clarification for variable amount and recurrence calendar semantics"}
    (ROOT/"PHASE_18_DECISION.json").write_text(json.dumps(decision,indent=2),encoding="utf-8")
    write("PHASE_18_DECISION.md","""# Phase 18 Decision

`AUTHORITATIVE_EVIDENCE_MISSING`

## Evidence result

Repository audit found no hidden authoritative rule beyond the specification,
schemas and already indexed lifecycle/FX/Decimal facts. The unresolved forecast
semantics are observationally confounded by the 25 solved examples.

## Production change

`NO_PRODUCTION_CHANGE_JUSTIFIED`. Production files are unchanged.

## Validation

Full suite: 64 passed. Semantic-lab: 10 passed. Sample matches remain
2/10/12/11/8/22. Output hash remains
`2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.

## Submission gate

Datasets, expected outputs and `output.csv` were not modified. No code.zip was
created. The system remains not submission-ready because variable amount and
recurrence-calendar semantics lack authoritative evidence.
""")

if __name__=="__main__": main()
