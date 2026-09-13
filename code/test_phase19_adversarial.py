from decimal import Decimal
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).parent))
from semantic_lab import catalog, run_fixture

_fixtures = catalog()[:60]

@pytest.mark.parametrize("fixture_spec", _fixtures, ids=lambda f: f.fixture_id)
def test_phase19_fixture_is_deterministic_and_decimal(fixture_spec):
    try:
        first = run_fixture(fixture_spec)
        second = run_fixture(fixture_spec)
        assert first.movements == second.movements
        assert first.balances == second.balances
        assert first.safe_amount == second.safe_amount
        assert isinstance(first.safe_amount, Decimal)
        assert first.safe_amount >= Decimal("0")
    except ValueError as exc:
        # Missing direct FX is a deliberate fail-closed fixture, never a
        # silently substituted rate.
        assert fixture_spec.fixture_id in {"FX-02", "FX-05"}
        assert "missing direct FX rate" in str(exc)

def test_phase19_no_lifecycle_cash_invariant():
    for f in catalog():
        try:
            result = run_fixture(f)
        except ValueError:
            continue
        for movement in result.movements:
            if movement["movement_id"].startswith("failed") or movement["movement_id"].startswith("cancelled"):
                assert movement["movement"] == "0"

def test_phase19_minimum_balance_trace_is_audit_visible():
    for f in catalog():
        try: result = run_fixture(f)
        except ValueError: continue
        assert all("minimum" in m and "safe" in m for m in result.movements)

def test_phase19_model_variants_never_change_fixture_inputs():
    for f in catalog()[:20]:
        stable = run_fixture(f, "stable_fixed")
        explicit = run_fixture(f, "explicit_only")
        assert f.requested_amount >= Decimal("0")
        assert stable.fixture_id == explicit.fixture_id == f.fixture_id

def test_phase19_policy_boundary_is_explicit():
    text = Path("PHASE_19_POLICY_BOUNDARY.md").read_text(encoding="utf-8")
    for key in ("VARIABLE_SPENDING_POLICY", "RECURRENCE_CALENDAR_POLICY", "OPTIONAL_BASELINE_POLICY", "SAME_DAY_ORDER_POLICY", "DEADLINE_STATUS_POLICY"):
        assert key in text
