import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

ROOT = Path(__file__).resolve().parents[1]

def test_full_generation_and_invariants(tmp_path):
    rows = main.main(ROOT)
    requests = {r["request_id"]: r for r in main.read_csv(ROOT/"dataset"/"requests.csv")}
    assert len(rows) == len(requests) == 250
    assert [r for r in rows if r["request_id"] not in requests] == []
    for row in rows:
        main.validate_output(row, requests[row["request_id"]])
    with open(ROOT/"output.csv", newline="", encoding="utf-8") as f:
        out=list(csv.DictReader(f))
    assert len(out)==250
    assert set(out[0].keys()) == set(main.OUT_COLS)

def test_safe_amount_bounds_for_first_requests():
    d=main.load_data(ROOT); main.normalize_events(d,ROOT)
    for req in main.read_csv(ROOT/"dataset"/"requests.csv")[:10]:
        safe=main.safe_amount(req["user_id"],req,d)
        assert main.ZERO <= safe <= main.D(req["requested_amount"])

