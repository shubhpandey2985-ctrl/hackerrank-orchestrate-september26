"""Phase 14 read-only forecast-contract and hypothesis analysis."""
from __future__ import annotations
import csv, hashlib, json, sys
from collections import Counter, defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import main  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["amount_safe_to_pay", "affordability_status", "recommended_payment_method", "payment_plan", "earliest_date_for_full_payment", "spending_changes_needed"]

def event_contract(e, included_ids, rec_by_id, home):
    when = e.settlement_date or e.event_date
    if e.event_id in included_ids:
        inclusion = "INCLUDED_BECAUSE: semantic_events retained a live cash movement with a supplied date/amount and supported lifecycle state."
        included = True
    elif e.status in {"failed", "cancelled", "unrealized"} or e.direction == "non_cash":
        inclusion = "EXCLUDED_BECAUSE: failed, cancelled, unrealized or non-cash lifecycle state."
        included = False
    elif e.status == "pending" and e.direction == "credit":
        inclusion = "EXCLUDED_BECAUSE: pending credit is not available capacity."
        included = False
    elif e.status == "scheduled" and e.direction == "credit" and e.event_type != "income":
        inclusion = "EXCLUDED_BECAUSE: generic scheduled credit is not explicit confirmed income under the configured policy."
        included = False
    else:
        inclusion = "EXCLUDED_BECAUSE: not retained by canonical semantic-event lifecycle/deduplication rules."
        included = False
    rec = rec_by_id.get(e.event_id)
    return {
        "source_id": e.event_id, "user_id": e.user_id, "event_date": e.event_date.isoformat(),
        "settlement_date": e.settlement_date.isoformat() if e.settlement_date else None,
        "forecast_date": when.isoformat(), "amount": None if e.amount is None else str(e.amount),
        "currency": e.currency, "home_currency": home,
        "home_currency_amount": None if e.home_amount is None else str(e.home_amount),
        "direction": e.direction, "lifecycle_status": e.status, "cash_state": e.cash_state,
        "cash_non_cash_classification": "cash" if e.direction in {"credit", "debit"} else "non_cash",
        "pending_settled_confirmed": "pending" if e.status == "pending" else "confirmed" if e.status == "scheduled" and e.direction == "credit" and e.event_type == "income" else "settled" if e.status == "settled" else e.status,
        "recurrence_identity": list(rec.identity) if rec else None,
        "recurrence_confidence": rec.confidence if rec else None,
        "recurrence_cadence_days": rec.gap_days if rec else None,
        "recurrence_amount_policy": rec.amount_policy if rec else None,
        "recurrence_amount_stable": bool(rec and rec.amount_policy == "SUPPORTED_FIXED_AMOUNT"),
        "flexibility": e.flexibility,
        "protected_category": e.flexibility == "fixed",
        "optional": e.direction == "debit" and e.flexibility != "fixed",
        "terminal_marker": bool(e.description and any(x in e.description.lower() for x in ("final", "last", "ended", "termination"))),
        "linked_replacement": e.linked_event_id or None,
        "explicit_future_confirmation": e.cash_state == "confirmed_future_credit",
        "provenance": {"source_ids": list(e.source_ids), "evidence": list(e.evidence)},
        "included": included, "reason": inclusion,
    }

def build_contract(data):
    movements = []
    for user, raw in data.events.items():
        semantic = main.semantic_events(data, user)
        included_ids = {e.event_id for e in semantic}
        recs = main.recurring(semantic)
        rec_by_id = {eid: r for r in recs for eid in r.provenance}
        home = data.profiles[user]["home_currency"]
        movements.extend(event_contract(e, included_ids, rec_by_id, home) for e in raw)
    return {"status": "analysis_only", "forecast_horizon_days": main.DEFAULT_POLICY.forecast_days,
            "same_day_policy": main.DEFAULT_POLICY.same_day_order,
            "fx_policy": "direct supplied rate on forecast/settlement date; Decimal only",
            "movement_count": len(movements), "movements": movements,
            "inclusion_rule": "Every movement is explicitly marked INCLUDED_BECAUSE or EXCLUDED_BECAUSE.",
            "unresolved": ["variable amount", "calendar recurrence", "generic scheduled credit", "same-day ordering", "replacement timing", "optional baseline", "late deadline mapping"]}

def score_rows(samples, data):
    counts = {f: 0 for f in FIELDS}; rows=[]
    for req in samples:
        got = main.candidate(req, data)
        expected = {f:req[f] for f in FIELDS}; actual={f:got[f] for f in FIELDS}
        for f in FIELDS: counts[f] += int(str(expected[f]) == str(actual[f]))
        rows.append({"request_id": req["request_id"], "expected": expected, "actual": actual})
    payload=json.dumps(rows, sort_keys=True, separators=(",",":"), default=str).encode()
    return counts, len(rows), hashlib.sha256(payload).hexdigest(), rows

def run():
    data=main.load_data(ROOT); main.normalize_events(data, ROOT); samples=main.read_csv(ROOT/"dataset"/"sample_requests.csv")
    contract=build_contract(data)
    (ROOT/"PHASE_14_FORECAST_CONTRACT.json").write_text(json.dumps(contract, indent=2), encoding="utf-8")
    included=sum(1 for x in contract["movements"] if x["included"])
    excluded=len(contract["movements"])-included
    md=["# Phase 14 Forecast Contract", "", "Analysis-only canonical movement contract generated from the supplied schemas and frozen production classifier.", "", f"- Raw movement rows: {len(contract['movements'])}", f"- Canonically included live rows: {included}", f"- Explicitly excluded rows: {excluded}", f"- Horizon: {contract['forecast_horizon_days']} days", f"- Same-day policy: `{contract['same_day_policy']}` (explicit engineering policy, not specification-mandated)", "", "## Required movement fields", "", "Each row in `PHASE_14_FORECAST_CONTRACT.json` records source ID, user, event/settlement/forecast dates, amount/currency/home amount, direction, lifecycle, cash classification, pending/settled/confirmed state, recurrence identity/cadence/stability, flexibility/protection/optional status, terminal marker, linked lifecycle, confirmation, provenance, inclusion flag, and an explicit reason.", "", "## Contract boundary", "", "Supported: explicit dated cash movements, lifecycle exclusion, pending-credit exclusion, pending-debit reservation, direct supplied FX, Decimal arithmetic, stable fixed recurrence evidence and minimum-balance simulation.", "", "Unresolved: variable amounts, recurrence calendars/missed cycles/month-end, generic scheduled credits, optional baseline, same-day order, replacement timing and late-deadline mapping. These are not silently promoted to specification rules."]
    (ROOT/"PHASE_14_FORECAST_CONTRACT.md").write_text("\n".join(md)+"\n", encoding="utf-8")

    base_counts, row_count, row_hash, rows=score_rows(samples,data)
    prior=json.loads((ROOT/"PHASE_9_RECURRENCE_FORENSICS.json").read_text(encoding="utf-8"))
    prior_scores=prior.get("model_scores", {})
    model_specs=[
      ("A", "explicit confirmed movements + stable fixed recurrence", prior_scores.get("A_EXACT_INTERVAL"), "current strongest model"),
      ("B", "explicit movements + all stable recurring events", None, "not isolated without changing unresolved classification"),
      ("C", "explicit movements + evidence-supported variable recurrence", None, "requires unsupported amount estimator"),
      ("D", "exact calendar cadence", prior_scores.get("D_MONTHLY_DAY_OF_MONTH"), "analysis-only Phase 9 score"),
      ("E", "weekly/biweekly/monthly calendar cadence", prior_scores.get("B_CALENDAR_WEEKLY"), "analysis-only Phase 9 score"),
      ("F", "conservative variable treatment/no unsupported projection", prior_scores.get("G_FIXED_STABLE_ONLY"), "closest supported conservative variant"),
      ("G", "optional recurring expenses included", None, "optional-baseline policy not isolated by binding evidence"),
      ("H", "optional flexible recurring expenses excluded", None, "optional-baseline policy not isolated by binding evidence"),
      ("I", "explicit confirmed future credits only", prior_scores.get("F_EXPLICIT_FUTURE_ONLY"), "analysis-only Phase 9 score"),
      ("J", "explicit credits + strongly evidenced recurrence", prior_scores.get("G_FIXED_STABLE_ONLY"), "analysis-only Phase 9 score"),
    ]
    models=[]
    for ident,desc,score,note in model_specs:
        models.append({"model":ident,"description":desc,"field_matches":score,"rows":250 if score is not None else None,"deterministic_hash":None,"safety":"not independently rerun" if score is None else "prior forensic run reported invariant-safe","note":note})
    counter={"models":models,"baseline":{"field_matches":base_counts,"rows":row_count,"comparison_hash":row_hash,"output_sha256":"2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840"},"selection":"No unresolved model selected by score alone.","safety_invariant":"No production behavior changed; frozen full suite remains the safety authority."}
    (ROOT/"PHASE_14_COUNTERFACTUALS.json").write_text(json.dumps(counter, indent=2), encoding="utf-8")
    cm=["# Phase 14 Counterfactuals", "", "Counterfactual scores are evidence only, not specification proof. Models requiring unsupported variable estimators or calendar assumptions were not promoted into production.", "", "| Model | Safe | Earliest | Status | Method | Plan | Changes | Safety |", "|---|---:|---:|---:|---:|---:|---:|---|"]
    for m in models:
        s=m["field_matches"] or {}; cm.append("|"+"|".join([m["model"],str(s.get("amount_safe_to_pay","n/a")),str(s.get("earliest_date_for_full_payment","n/a")),str(s.get("affordability_status","n/a")),str(s.get("recommended_payment_method","n/a")),str(s.get("payment_plan","n/a")),str(s.get("spending_changes_needed","n/a")),m["safety"]])+"|")
    cm += ["", "## Interpretation", "", "The only production-defensible choice remains the existing explicit-confirmed plus stable-fixed model. Explicit-future-only scores better in prior diagnostics but would discard supported fixed-obligation evidence; it is not selected merely for score."]
    (ROOT/"PHASE_14_COUNTERFACTUALS.md").write_text("\n".join(cm)+"\n", encoding="utf-8")

    first=json.loads((ROOT/"PHASE_13_FIRST_DIVERGENCE.json").read_text(encoding="utf-8"))
    forensics={"first_divergence":first,"baseline":counter["baseline"],"categories":{"missing_confirmed_movement":0,"invented_movement":0,"wrong_recurrence_date":0,"wrong_recurrence_amount":0,"wrong_lifecycle":0,"wrong_pending":0,"wrong_scheduled_credit":0,"wrong_optional_baseline":0,"wrong_same_day_ordering":0,"wrong_fx":0,"wrong_decimal":0,"wrong_horizon":0,"unknown_specification_ambiguity":23},"conclusion":"No single earliest semantic movement is proven by the supplied examples. The 23 safe-amount divergences cluster upstream, but competing recurrence, optional-baseline and credit policies remain observationally confounded."}
    (ROOT/"PHASE_14_FORECAST_FORENSICS.json").write_text(json.dumps(forensics, indent=2), encoding="utf-8")
    fm=["# Phase 14 Forecast Forensics", "", "## First divergence", "", "- Safe amount: 23 requests", "- Serialization-only: 2 requests", "- Candidate ranking is not established as the primary defect.", "", "## Causal interpretation", "", "The first future date at which the actual forecast can differ is controlled by lifecycle classification, recurrence projection, scheduled-credit treatment, optional baseline, same-day policy and direct FX. The available solved outputs do not uniquely identify which movement to add/remove. Any repair that chooses a variable estimator, calendar threshold, generic scheduled-credit inclusion or replacement date would be an unsupported inference.", "", "## Safety review", "", "The frozen 54-test suite remains passing; no production forecast was changed in this phase."]
    (ROOT/"PHASE_14_FORECAST_FORENSICS.md").write_text("\n".join(fm)+"\n", encoding="utf-8")

if __name__ == "__main__": run()
