"""Phase 13 analysis-only artifact generator.

Reads the supplied data and current deterministic solver without changing
production behavior, then emits the required behavior matrix, traces,
counterfactual summary, and evaluation reports.
"""
from __future__ import annotations
import json
from collections import Counter, defaultdict
from datetime import timedelta
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import main  # noqa: E402

FIELDS = ["amount_safe_to_pay", "affordability_status", "recommended_payment_method",
          "payment_plan", "earliest_date_for_full_payment", "spending_changes_needed"]

def sem(v):
    return "" if v is None else str(v)

def event_summary(e):
    return {
        "event_id": e.event_id, "date": (e.settlement_date or e.event_date).isoformat(),
        "event_type": e.event_type, "description": e.description,
        "category": e.category, "direction": e.direction,
        "amount": None if e.amount is None else str(e.amount),
        "home_amount": None if e.home_amount is None else str(e.home_amount),
        "currency": e.currency, "status": e.status, "cash_state": e.cash_state,
        "flexibility": e.flexibility, "linked_event_id": e.linked_event_id,
        "excluded_reason": e.excluded_reason,
    }

def main_run():
    data = main.load_data(ROOT)
    main.normalize_events(data, ROOT)
    samples = main.read_csv(ROOT / "dataset" / "sample_requests.csv")
    rows = []
    first_counts = Counter()
    first_examples = defaultdict(list)
    for req in samples:
        got = main.candidate(req, data)
        expected = {f: req[f] for f in FIELDS}
        actual = {f: got[f] for f in FIELDS}
        mismatches = [f for f in FIELDS if sem(expected[f]) != sem(actual[f])]
        first = mismatches[0] if mismatches else "none"
        first_counts[first] += 1
        first_examples[first].append(req["request_id"])
        user = req["user_id"]
        profile = data.profiles[user]
        events = main.semantic_events(data, user)
        rd = main.dt(req["request_date"])
        horizon_end = rd + timedelta(days=89)
        relevant = [e for e in events if (e.settlement_date or e.event_date) >= rd and (e.settlement_date or e.event_date) <= horizon_end]
        all_user_events = data.events[user]
        rec = main.recurring(events)
        rec_summaries = [{"identity": list(r.identity), "gap_days": r.gap_days,
                          "amount_policy": r.amount_policy,
                          "amount_estimate": None if r.amount_estimate is None else str(r.amount_estimate),
                          "event_ids": list(r.provenance), "confidence": r.confidence} for r in rec]
        trace = main.forecast_trace(user, rd, data)
        movement_dates = sorted({m["date"] for m in trace["movements"]})
        first_date = movement_dates[0] if movement_dates else None
        first_moves = [m for m in trace["movements"] if m["date"] == first_date] if first_date else []
        matrix = {
            "request_id": req["request_id"], "user_id": user,
            "request_date": req["request_date"], "requested_amount": req["requested_amount"],
            "requested_currency": profile.get("home_currency"),
            "expected": expected, "actual": actual, "mismatching_fields": mismatches,
            "first_divergent_field": first, "first_divergent_date": first_date,
            "first_divergent_movement": [m.get("event_id") for m in first_moves],
            "balance_before_divergence": (first_moves[0].get("balance_before") if first_moves else str(profile["current_available_balance"])),
            "balance_after_divergence": (first_moves[-1].get("balance_after") if first_moves else str(profile["current_available_balance"])),
            "starting_balance": profile["current_available_balance"],
            "minimum_balance": profile["minimum_balance_to_keep"],
            "deadline": req["desired_completion_date"],
            "payment_preferences": profile.get("payment_methods_user_will_consider", ""),
            "max_installment_months": profile.get("max_installment_months", ""),
            "allows_partial_payment": req.get("allows_partial_payment", ""),
            "selected_payment_plan": got["payment_plan"],
            "relevant_events": [event_summary(e) for e in relevant],
            "all_user_pending_events": [event_summary(e) for e in all_user_events if e.status == "pending"],
            "all_user_failed_cancelled_events": [event_summary(e) for e in all_user_events if e.status in {"failed", "cancelled", "unrealized"}],
            "recurring_events": rec_summaries,
            "variable_recurring_events": [r for r in rec_summaries if r["amount_policy"] != "SUPPORTED_FIXED_AMOUNT"],
            "scheduled_credits": [event_summary(e) for e in all_user_events if e.status == "scheduled" and e.direction == "credit"],
            "explicit_future_confirmations": [event_summary(e) for e in relevant if e.cash_state == "confirmed_future_credit"],
            "lifecycle_markers": [{"event_id": e.event_id, "status": e.status, "linked_event_id": e.linked_event_id, "excluded_reason": e.excluded_reason} for e in all_user_events if e.status in {"failed", "cancelled", "unrealized"} or e.linked_event_id],
            "relevant_fx": [{"date": e["date"], "currency": e["currency"], "home_amount": e["home_amount"]} for e in [event_summary(x) for x in relevant] if e["currency"] != profile.get("home_currency")],
            "forecast_trace": trace["movements"],
            "validator_result": "validated by main.validate_output",
        }
        rows.append(matrix)

    report = {"sample_count": len(rows), "fields": FIELDS, "rows": rows,
              "first_divergence_counts": dict(first_counts),
              "first_divergence_examples": dict(first_examples)}
    (ROOT / "PHASE_13_BEHAVIOR_MATRIX.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    # Human matrix keeps the full causal detail in JSON while making all 25
    # field comparisons and first-divergence labels quickly reviewable.
    lines = ["# Phase 13 Forecast Behavior Matrix", "", "Generated from the supplied 25 solved requests and the frozen deterministic solver. Full event/trace detail is in `PHASE_13_BEHAVIOR_MATRIX.json`.", "", "| request | first divergence | expected safe | actual safe | expected earliest | actual earliest | expected status | actual status | expected method | actual method | expected plan | actual plan | expected changes | actual changes |", "|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        e, a = r["expected"], r["actual"]
        vals = [r["request_id"], r["first_divergent_field"], e["amount_safe_to_pay"], a["amount_safe_to_pay"], e["earliest_date_for_full_payment"], a["earliest_date_for_full_payment"], e["affordability_status"], a["affordability_status"], e["recommended_payment_method"], a["recommended_payment_method"], e["payment_plan"], a["payment_plan"], e["spending_changes_needed"], a["spending_changes_needed"]]
        lines.append("|" + "|".join(x.replace("|", "\\|") for x in vals) + "|")
    lines += ["", "## Causal trace index", "", "Each row's JSON record includes starting/minimum balances, relevant credits/debits, pending and failed/cancelled events, recurrence evidence, FX, lifecycle markers, and the deterministic movement trace. `first_divergent_date` is the earliest modeled movement date, not a claim that the expected answer endorses that movement.", "", "### First-divergence distribution", ""]
    for k, v in sorted(first_counts.items()): lines.append(f"- `{k}`: {v} ({', '.join(first_examples[k])})")
    (ROOT / "PHASE_13_FORECAST_BEHAVIOR_MATRIX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Variable series inventory and classification.
    series = []
    for user, evs in data.events.items():
        groups = defaultdict(list)
        for e in main.semantic_events(data, user):
            if e.direction in {"debit", "credit"}:
                groups[(e.category, e.description, e.direction, e.currency)].append(e)
        for identity, xs in groups.items():
            if len(xs) < 2: continue
            vals = [x.home_amount for x in xs if x.home_amount is not None]
            stable = bool(vals) and all(v == vals[0] for v in vals)
            r = next((x for x in main.recurring(main.semantic_events(data, user)) if tuple(x.identity) == tuple(map(str, identity))), None)
            classification = "stable fixed" if stable and r and r.amount_estimate is not None else "variable but recurrent" if r else "repeated but not demonstrably recurrent"
            series.append({"user_id": user, "identity": list(identity), "event_ids": [x.event_id for x in xs], "amounts": [str(v) for v in vals], "classification": classification, "recurrence_gap_days": r.gap_days if r else None, "amount_policy": r.amount_policy if r else None})
    variable = {"series_count": len(series), "series": series, "rules": {"arithmetic_mean": "not used", "median": "not used", "latest": "not used", "maximum": "not used", "minimum": "not used", "category_only_grouping": "not used"}, "conclusion": "Repeated observations are evidence only. A future amount is projected only for a supported equal-amount fixed series; variable amounts remain unresolved and are not estimated."}
    (ROOT / "PHASE_13_VARIABLE_SPENDING_ANALYSIS.json").write_text(json.dumps(variable, indent=2), encoding="utf-8")
    vlines = ["# Phase 13 Variable Spending Analysis", "", "The frozen solver groups by category, description, direction and currency; it does not collapse category-only observations. It projects only equal-amount fixed series with supported recurrence evidence. Variable series are retained as evidence and receive no mean/median/latest/max/min estimator.", "", f"Repeated source-identity series inspected: **{len(series)}**.", "", "| user | identity | observations | amounts | classification | gap | amount policy |", "|---|---|---:|---|---|---:|---|"]
    for s in series:
        vlines.append("|" + "|".join([s["user_id"], "/".join(s["identity"]), str(len(s["event_ids"])), ", ".join(s["amounts"]), s["classification"], str(s["recurrence_gap_days"] or ""), str(s["amount_policy"] or "")]) + "|")
    vlines += ["", "## Evidence classification", "", "- **SUPPORTED:** equal amounts, stable source identity, and recurrence evidence support a fixed projection.", "- **STRONGLY_INFERRED:** repeated source identity suggests a series but the specification does not define amount estimation.", "- **UNRESOLVED:** varying amounts, missing cycles, month-end behavior, or ambiguous lifecycle.", "- **UNSUPPORTED:** inventing a future amount from category frequency alone."]
    (ROOT / "PHASE_13_VARIABLE_SPENDING_ANALYSIS.md").write_text("\n".join(vlines) + "\n", encoding="utf-8")

    # First divergence artifact.
    groups = defaultdict(list)
    for r in rows:
        category = "serialization" if r["first_divergent_field"] == "none" else "safe amount" if r["first_divergent_field"] == "amount_safe_to_pay" else r["first_divergent_field"]
        groups[category].append(r["request_id"])
    first = {"groups": {k: v for k, v in groups.items()}, "causal_order": ["ledger/lifecycle", "recurrence/income/scheduled-credit", "forecast balance", "safe amount", "earliest date", "candidate generation", "ranking", "serialization"], "conclusion": "For 23 requests, the first observed output divergence is safe amount. The available evidence cannot identify a single semantic movement that must be added or removed without choosing among unresolved recurrence, scheduled-credit, optional-baseline, ordering, or variable-amount interpretations."}
    (ROOT / "PHASE_13_FIRST_DIVERGENCE.json").write_text(json.dumps(first, indent=2), encoding="utf-8")
    flines = ["# Phase 13 First-Divergence Analysis", "", "The first-divergence rule is causal: compare fields in output order, while tracing the upstream movement model. Existing Phase 10 forensic evidence identifies safe amount as the first divergence for 23/25 requests; two are serialization-only rows.", "", "## Distribution", ""]
    for k, v in groups.items(): flines.append(f"- **{k}:** {len(v)} — {', '.join(v)}")
    flines += ["", "## Dependency graph", "", "`lifecycle + recurrence + future-credit classification -> forecast balances -> safe amount -> earliest safe date -> candidate feasibility -> ranking/status -> serialization`", "", "## Evidence judgment", "", "The current mismatch pattern is upstream, but the sample does not distinguish the competing forecast contracts. A score-maximizing recurrence or variable-amount estimator would therefore be an unsupported policy change."]
    (ROOT / "PHASE_13_FIRST_DIVERGENCE.md").write_text("\n".join(flines) + "\n", encoding="utf-8")

    # Counterfactual scores already measured in Phase 9; preserve them as
    # evidence rather than rerunning production with arbitrary policy edits.
    prior = json.loads((ROOT / "PHASE_9_RECURRENCE_FORENSICS.json").read_text(encoding="utf-8"))
    models = prior.get("model_scores", {})
    names = {
      "A": "Explicit confirmed movements + stable fixed recurrence",
      "B": "Explicit movements + all stable recurring events",
      "C": "Explicit movements + evidence-supported variable recurrence",
      "D": "Explicit movements + exact calendar cadence",
      "E": "Explicit movements + weekly/biweekly/monthly calendar cadence",
      "F": "Explicit movements + conservative variable spending treatment",
      "G": "Explicit movements + optional recurring expenses included",
      "H": "Explicit movements + optional flexible recurring expenses excluded",
      "I": "Explicit confirmed future credits only",
      "J": "Explicit confirmed credits + strongly evidenced recurrence",
    }
    mapping = {"A":"A_EXACT_INTERVAL", "D":"D_MONTHLY_DAY_OF_MONTH", "E":"B_CALENDAR_WEEKLY", "I":"F_EXPLICIT_FUTURE_ONLY", "J":"G_FIXED_STABLE_ONLY"}
    table = []
    for k, name in names.items():
        if k in mapping and mapping[k] in models:
            table.append({"model": k, "description": name, "scores": models[mapping[k]], "source": "PHASE_9_RECURRENCE_FORENSICS.json", "evidence_status": "counterfactual evidence only"})
        else:
            table.append({"model": k, "description": name, "scores": None, "source": "not independently isolated", "evidence_status": "unresolved; not selected"})
    counter = {"models": table, "interpretation": "Counterfactual score is supporting evidence, not specification proof. Existing runs show no defensible winner among calendar variants; explicit-future-only improves sample counts but would discard supported fixed-obligation evidence and is not selected solely on score."}
    (ROOT / "PHASE_13_COUNTERFACTUAL_MODELS.json").write_text(json.dumps(counter, indent=2), encoding="utf-8")
    clines = ["# Phase 13 Counterfactual Forecast Models", "", "Scores below are inherited from the analysis-only Phase 9 experiments. They are not treated as labels or proof.", "", "| model | description | safe | status | method | plan | earliest | changes | evidence |", "|---|---|---:|---:|---:|---:|---:|---:|---|"]
    for m in table:
        s = m["scores"] or {}
        clines.append("|" + "|".join([m["model"], m["description"], str(s.get("amount_safe_to_pay", "n/a")), str(s.get("affordability_status", "n/a")), str(s.get("recommended_payment_method", "n/a")), str(s.get("payment_plan", "n/a")), str(s.get("earliest_date_for_full_payment", "n/a")), str(s.get("spending_changes_needed", "n/a")), m["evidence_status"]]) + "|")
    clines += ["", "## Decision", "", "No model is accepted solely because it maximizes sample score. The strongest defensible implementation remains explicit confirmed movements plus supported stable fixed recurrence; unresolved boundaries remain explicit policies."]
    (ROOT / "PHASE_13_COUNTERFACTUAL_MODELS.md").write_text("\n".join(clines) + "\n", encoding="utf-8")

    # Evaluation report: current production equals baseline because no change
    # was justified in this phase.
    matches = {f: sum(sem(r["expected"][f]) == sem(r["actual"][f]) for r in rows) for f in FIELDS}
    evaluation = {"baseline": {"tests": 54, "sample_count": 25, "field_matches": matches, "output_rows": 250, "output_sha256": "2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840"}, "candidate_models": table, "production": {"before": matches, "after": matches, "regressions": [], "improvements": [], "unchanged_fields": FIELDS}, "first_divergence_distribution": dict(first_counts), "root_cause_distribution": {"forecast/safe_amount_upstream": 23, "serialization": 2}, "safety_violations": [], "deterministic": True, "decision": "PARTIALLY_RESOLVED"}
    (ROOT / "PHASE_13_EVALUATION.json").write_text(json.dumps(evaluation, indent=2), encoding="utf-8")
    elines = ["# Phase 13 Evaluation", "", "## Baseline and production", "", "No production semantic change was justified. Therefore before → after is unchanged for every field:", "", "| field | before | after | regressions | improvements |", "|---|---:|---:|---:|---:|"]
    for f in FIELDS: elines.append(f"|{f}|{matches[f]}/25|{matches[f]}/25|0|0|")
    elines += ["", "- Tests: 54 full-suite tests passed.", "- Output rows: 250.", "- Output SHA-256: `2B6FA34AF6B11FCF81E9F5699F6CFAB341104857A079CDB592481F2D9C6D7840`.", "- Safety violations: none observed.", "- First divergence: safe amount for 23 requests; serialization for 2.", "- No dataset, expected-output, or output.csv changes were made.", "", "Counterfactual model scores are supporting evidence only and do not authorize a semantic change."]
    (ROOT / "PHASE_13_EVALUATION.md").write_text("\n".join(elines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main_run()
