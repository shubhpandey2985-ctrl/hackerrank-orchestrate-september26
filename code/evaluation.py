"""Development-only comparison against the 25 public solved examples."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

root=Path(__file__).resolve().parents[1]
d=main.load_data(root); main.normalize_events(d,root)
samples=main.read_csv(root/"dataset"/"sample_requests.csv")
fields=["amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed"]
matches={f:0 for f in fields}; rows=[]
for req in samples:
    got=main.candidate(req,d)
    for f in fields: matches[f]+=int(str(got.get(f,""))==str(req.get(f,"")))
    rows.append({"request_id":req["request_id"],"expected":{f:req[f] for f in fields},"actual":{f:got[f] for f in fields}})
report={"sample_count":len(samples),"field_matches":matches,"rows":rows}
(root/"evaluation_sample_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps({"sample_count":len(samples),"field_matches":matches},indent=2))
