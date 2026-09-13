from decimal import Decimal
from datetime import date, timedelta
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from semantic_lab import catalog, run_fixture, LabEvent, fixture

def test_fixture_catalog_covers_phase15_ids():
    ids = {f.fixture_id for f in catalog()}
    required = {f"VS-{i:02d}" for i in range(1,11)} | {f"RC-{i:02d}" for i in range(1,15)} | {f"INC-{i:02d}" for i in range(1,11)}
    required |= {f"PEN-{i:02d}" for i in range(1,6)} | {f"SD-{i:02d}" for i in range(1,5)} | {f"REP-{i:02d}" for i in range(1,6)}
    required |= {f"DL-{i:02d}" for i in range(1,6)} | {f"FX-{i:02d}" for i in range(1,6)} | {f"DEC-{i:02d}" for i in range(1,7)}
    assert required <= ids

def test_all_fixtures_are_decimal_and_traceable():
    for f in catalog():
        try:
            result = run_fixture(f)
        except ValueError as exc:
            assert f.fixture_id in {"FX-02", "FX-05"}
            assert "missing direct FX rate" in str(exc)
            continue
        assert isinstance(result.safe_amount, Decimal)
        assert result.safe_amount >= 0
        assert result.minimum_observed >= f.minimum_balance or any(not x["safe"] for x in result.movements)
        for p in result.provenance:
            assert p["reason"].startswith(("INCLUDED_BECAUSE", "EXCLUDED_BECAUSE"))

def test_lifecycle_and_pending_credit_properties():
    base = fixture("PROP", "lifecycle", events=(LabEvent("debit", date(2025,1,2), Decimal("100")),), requested_amount=Decimal("500"))
    failed = fixture("PROP-F", "failed", events=base.events + (LabEvent("failed", date(2025,1,3), Decimal("100"), status="failed"),), requested_amount=Decimal("500"))
    pending_credit = fixture("PROP-PC", "pending credit", events=base.events + (LabEvent("pc", date(2025,1,3), Decimal("1000"), direction="credit", status="pending"),), requested_amount=Decimal("500"))
    assert run_fixture(failed).safe_amount == run_fixture(base).safe_amount
    assert run_fixture(pending_credit).safe_amount == run_fixture(base).safe_amount

def test_unavoidable_debit_cannot_increase_capacity_and_income_can_help():
    base = fixture("PROP-M", "monotonic", opening_balance=Decimal("1000"), minimum_balance=Decimal("100"), requested_amount=Decimal("800"))
    debit = fixture("PROP-D", "debit", opening_balance=Decimal("1000"), minimum_balance=Decimal("100"), requested_amount=Decimal("800"), events=(LabEvent("d", date(2025,1,2), Decimal("200")),))
    income = fixture("PROP-I", "income", opening_balance=Decimal("1000"), minimum_balance=Decimal("100"), requested_amount=Decimal("800"), events=(LabEvent("i", date(2025,1,2), Decimal("200"), direction="credit"),))
    assert run_fixture(debit).safe_amount <= run_fixture(base).safe_amount
    assert run_fixture(income).safe_amount >= run_fixture(base).safe_amount

def test_protected_and_nonflexible_events_remain_provenance_only():
    f = fixture("PROP-P", "protected", requested_amount=Decimal("500"), events=(LabEvent("p", date(2025,1,2), Decimal("100"), flexibility="fixed", protected=True),))
    r = run_fixture(f)
    assert any(x["movement_id"] == "p" for x in r.movements)

def test_same_day_models_are_explicitly_comparable():
    d=date(2025,1,2)
    f=fixture("PROP-SD", "same day", opening_balance=Decimal("100"), minimum_balance=Decimal("50"), requested_amount=Decimal("50"), events=(LabEvent("c",d,Decimal("100"),direction="credit"),LabEvent("d",d,Decimal("100"),direction="debit")))
    credit_first=run_fixture(f,same_day="credit_first")
    debit_first=run_fixture(f,same_day="debit_first")
    assert credit_first.movements != debit_first.movements

def test_same_day_credit_and_debit_is_deterministic():
    d=date(2025,1,2)
    f=fixture("SD-C-D","credit debit",opening_balance=Decimal("100"),minimum_balance=Decimal("50"),events=(LabEvent("c",d,Decimal("25"),direction="credit"),LabEvent("d",d,Decimal("25"),direction="debit")),requested_amount=Decimal("10"))
    a=run_fixture(f,same_day="credit_first"); b=run_fixture(f,same_day="credit_first")
    assert a.movements == b.movements and a.safe_amount == b.safe_amount

def test_same_day_debit_and_payment_uses_same_forecast_engine():
    d=date(2025,1,2)
    f=fixture("SD-D-P","debit payment",opening_balance=Decimal("100"),minimum_balance=Decimal("50"),events=(LabEvent("d",d,Decimal("20")),),requested_amount=Decimal("50"))
    r=run_fixture(f,payment=(d,Decimal("30")))
    assert r.minimum_observed == Decimal("50")

def test_same_day_credit_debit_payment_order_is_explicit():
    d=date(2025,1,2)
    f=fixture("SD-C-D-P","credit debit payment",opening_balance=Decimal("100"),minimum_balance=Decimal("100"),events=(LabEvent("c",d,Decimal("20"),direction="credit"),LabEvent("d",d,Decimal("20"))),requested_amount=Decimal("20"))
    r=run_fixture(f,same_day="credit_first",payment=(d,Decimal("20")))
    assert r.minimum_observed == Decimal("80")

def test_reordering_fixture_input_is_deterministic():
    d=date(2025,1,2)
    events=(LabEvent("c",d,Decimal("100"),direction="credit"),LabEvent("d",d,Decimal("20")))
    a=fixture("ORDER-A","order",events=events,requested_amount=Decimal("50")); b=fixture("ORDER-B","order",events=tuple(reversed(events)),requested_amount=Decimal("50"))
    assert run_fixture(a).safe_amount == run_fixture(b).safe_amount
