from pathlib import Path
import importlib.util
import sys
sys.path.insert(0, str(Path(__file__).parent))
from policy import DEFAULT_POLICY
_spec=importlib.util.spec_from_file_location("app_io", Path(__file__).parent/"io.py")
io_module=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(io_module)
import ledger, forecast, plans, validator, evidence, explanations

ROOT=Path(__file__).resolve().parents[1]

def test_explicit_undefined_semantics_are_configured():
    p=DEFAULT_POLICY
    assert p.same_day_order
    assert p.recurrence_min_observations >= 2
    assert p.scheduled_credit_mode == "confirmed_salary_only"
    assert p.failed_replacement_mode == "never_invent"
    assert p.late_deadline_mode == "capacity_only_no_recommendation"
    assert p.flexible_tie_break == "sorted_event_id_then_action"

def test_module_boundaries_and_llm_guardrails():
    d=io_module.load(ROOT)
    ledger.normalize(d,ROOT)
    assert len(d.requests)==250
    req=d.requests[0]
    row=plans.generate(req,d)
    validator.validate(row,req,d)
    assert evidence.llm_can_authorize_plan() is False
    assert explanations.llm_can_change_financial_facts() is False
    ok,_=forecast.simulate(req["user_id"],__import__('main').dt(req["request_date"]),d)
    assert isinstance(ok,bool)
