"""Analysis-only counterfactual scoring for specification reconstruction.

This does not alter production files or datasets. It temporarily substitutes
recurrence interpretations in memory, runs the unchanged solver, and reports
field-level sample matches.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import main

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["amount_safe_to_pay", "earliest_date_for_full_payment",
          "affordability_status", "recommended_payment_method",
          "payment_plan", "spending_changes_needed"]
VARIABLE = {"groceries","transport","dining","entertainment","shopping",
            "healthcare","education","family_support"}

def score(samples, data):
    counts = {f: 0 for f in FIELDS}
    for req in samples:
        got = main.candidate(req, data)
        for f in FIELDS:
            counts[f] += int(str(got.get(f, "")) == str(req.get(f, "")))
    return counts

def variant_filter(base, keep):
    def wrapped(events):
        return [g for g in base(events) if keep(g[0])]
    return wrapped

def group_is_variable(g):
    return bool(g) and g[0].category in VARIABLE

def group_is_income(g):
    return bool(g) and g[0].direction == "credit"

def group_is_fixed(g):
    return bool(g) and (not group_is_variable(g))

def main_run():
    data = main.load_data(ROOT)
    main.normalize_events(data, ROOT)
    samples = main.read_csv(ROOT / "dataset" / "sample_requests.csv")
    base = main.recurring
    variants = {
        "current implementation": base,
        "remove variable-category recurrence": variant_filter(base, group_is_fixed),
        "explicit events only (remove all inferred recurrence)": lambda events: [],
        "no historical income extrapolation": variant_filter(base, lambda g: not group_is_income(g)),
        "fixed obligations only (same as removing variable and income recurrence)": variant_filter(base, lambda g: group_is_fixed(g) and not group_is_income(g)),
    }
    out = {}
    try:
        for name, fn in variants.items():
            main.recurring = fn
            out[name] = score(samples, data)
    finally:
        main.recurring = base
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main_run()
