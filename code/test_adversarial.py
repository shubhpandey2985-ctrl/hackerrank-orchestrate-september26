"""Adversarial hidden-test probes. These deliberately exercise rules beyond samples."""
from datetime import date, timedelta
from decimal import Decimal
import pytest
import main
from pathlib import Path

def ev(i, user="u", typ="expense", cat="shopping", direction="debit", amount="10", day=date(2026,1,1), status="settled", flex="fixed", settle=None, currency="USD", link=""):
    value = None if amount is None else Decimal(amount)
    return main.Event(i,user,typ,"x",cat,direction,value,currency,day,settle or day,status,link,flex,Decimal("0"),value)

def data(profile, events, options=None, rates=None):
    return main.Data({"u":profile}, [], options or {}, {"u":events}, [], [], rates or {})

def profile(balance="100", minimum="50", prefs="full_payment", max_months=""):
    return {"user_id":"u","home_currency":"USD","current_available_balance":balance,"minimum_balance_to_keep":minimum,"financial_priorities":"","expense_categories_to_protect":"","expense_categories_user_is_willing_to_reduce":"dining","expense_categories_user_is_willing_to_stop":"streaming","payment_methods_user_will_consider":prefs,"max_installment_months":max_months}

def req(amount="40", date_="2026-01-01", deadline="2026-01-10", partial="false"):
    return {"request_id":"r","user_id":"u","request_date":date_,"request_type":"purchase","requested_amount":amount,"desired_completion_date":deadline,"allows_partial_payment":partial,"request_text":""}

def test_pending_credit_is_not_spendable():
    d=data(profile(balance="0", minimum="50"), [ev("c",typ="income",cat="salary",direction="credit",amount="100",status="pending")])
    ok,_=main.forecast("u",date(2026,1,1),d,((date(2026,1,1),Decimal("40")),))
    assert not ok

def test_pending_debit_is_reserved():
    d=data(profile(balance="100", minimum="50"), [ev("d",amount="60",status="pending",settle=date(2026,1,2))])
    ok,_=main.forecast("u",date(2026,1,1),d,())
    assert not ok

def test_confirmed_income_only_arrives_on_settlement_date():
    e=ev("salary",typ="income",cat="salary",direction="credit",amount="100",day=date(2026,1,2),settle=date(2026,1,3),status="scheduled")
    d=data(profile(balance="50",minimum="50"), [e])
    before,_=main.forecast("u",date(2026,1,1),d,((date(2026,1,2),Decimal("1")),))
    onday,_=main.forecast("u",date(2026,1,1),d,((date(2026,1,3),Decimal("1")),))
    assert not before and onday

def test_duplicate_lifecycle_rows_are_counted_once():
    a=ev("a",amount="10"); b=ev("b",amount="10"); b.description=a.description
    d=data(profile(balance="20",minimum="10"), [a,b])
    assert len(main.semantic_events(d,"u")) == 1

def test_missing_image_amount_without_cache_fails_closed(tmp_path):
    e=ev("missing",amount=None)
    e.evidence=("image_missing",)
    d=data(profile(),[e])
    with pytest.raises(ValueError): main.normalize_events(d,tmp_path)

def test_image_amount_cache_is_used_as_evidence(tmp_path):
    (tmp_path/"code").mkdir(); (tmp_path/"code"/"evidence_cache.json").write_text('{"missing":"12.50"}')
    e=ev("missing",amount=None); e.evidence=("image_missing",)
    d=data(profile(),[e]); main.normalize_events(d,tmp_path)
    assert e.home_amount == Decimal("12.50")

def test_currency_uses_exact_settlement_date_rate():
    e=ev("fx",amount="10",currency="EUR",settle=date(2026,1,3))
    d=data(profile(),[e],rates={("2026-01-03","EUR","USD"):Decimal("1.25")})
    main.normalize_events(d,Path('.')); assert e.home_amount==Decimal("12.50")

def test_impossible_request_has_zero_safe_amount():
    d=data(profile(balance="0",minimum="50"), [])
    r=req(amount="100",deadline="2026-01-10")
    assert main.safe_amount("u",r,d)==Decimal("0")
    assert main.candidate(r,d)["recommended_payment_method"]=="not_recommended"

def test_wait_requires_full_payment_preference():
    d=data(profile(balance="0",minimum="0",prefs="installments"), [])
    r=req(amount="10",deadline="2026-01-10")
    got=main.candidate(r,d)
    assert got["recommended_payment_method"] != "wait"

def test_exact_minimum_boundary_is_safe():
    d=data(profile(balance="90",minimum="50"), [])
    r=req(amount="40")
    assert main.safe_amount("u",r,d)==Decimal("40")

def test_temporary_dip_rejects_plan_even_if_final_balance_recovers():
    d=data(profile(balance="100",minimum="50"), [ev("debit",amount="60",day=date(2026,1,2)) ,ev("credit",typ="income",cat="salary",direction="credit",amount="60",day=date(2026,1,3))])
    ok,_=main.forecast("u",date(2026,1,1),d,((date(2026,1,1),Decimal("40")),))
    assert not ok

def test_installment_schedule_mismatch_is_rejected():
    r=req(amount="30"); r["request_id"]="r"
    o={"payment_option_id":"p","request_id":"r","payment_method":"installments","payment_amount":"10","number_of_payments":"3","first_payment_date":"2026-01-01","payment_frequency_days":"3","financing_fee":"0","total_payable_amount":"30"}
    d=data(profile(prefs="installments",max_months="3"), [], {"r":[o]})
    bad={"request_id":"r","amount_safe_to_pay":"0","affordability_status":"affordable_with_plan","recommended_payment_method":"installments","payment_plan":"2026-01-01:10|2026-01-04:10|2026-01-08:10","earliest_date_for_full_payment":"","spending_changes_needed":"none","decision_explanation":"x"}
    with pytest.raises(AssertionError): main.validate_output(bad,r,d)

def test_partial_payment_requires_exact_two_payments_and_sum():
    r=req(amount="30",partial="true")
    bad={"request_id":"r","amount_safe_to_pay":"10","affordability_status":"affordable_with_plan","recommended_payment_method":"partial_payment","payment_plan":"2026-01-01:10|2026-01-05:19","earliest_date_for_full_payment":"2026-01-05","spending_changes_needed":"none","decision_explanation":"x"}
    with pytest.raises(AssertionError): main.validate_output(bad,r)

def test_horizon_boundary_is_inclusive_of_ninetieth_day_only_if_specified():
    d=data(profile(balance="100",minimum="50"), [])
    r=req(amount="50",deadline="2026-04-01")
    assert main.earliest("u",r,d)==date(2026,1,1)

def test_missing_direct_fx_rate_fails_closed():
    e=ev("fx",amount="10",currency="EUR")
    d=data(profile(), [e], rates={})
    with pytest.raises(ValueError): main.normalize_events(d, __import__('pathlib').Path('.'))

def test_nonflexible_event_cannot_be_stopped():
    d=data(profile(balance="0",minimum="0",prefs="full_payment"), [ev("fixed",amount="10",flex="fixed")])
    bad={"request_id":"r","amount_safe_to_pay":"0","affordability_status":"affordable_with_plan","recommended_payment_method":"full_payment","payment_plan":"2026-01-01:1","earliest_date_for_full_payment":"2026-01-01","spending_changes_needed":"stop:fixed","decision_explanation":"x"}
    with pytest.raises(AssertionError): main.validate_output(bad,req(amount="1"),d)

def test_multiple_installment_options_respect_installment_limit():
    r=req(amount="30"); r["request_id"]="r"
    opts=[{"payment_option_id":"p1","request_id":"r","payment_method":"installments","payment_amount":"10","number_of_payments":"3","first_payment_date":"2026-01-01","payment_frequency_days":"3","financing_fee":"0","total_payable_amount":"30"},{"payment_option_id":"p2","request_id":"r","payment_method":"installments","payment_amount":"5","number_of_payments":"6","first_payment_date":"2026-01-01","payment_frequency_days":"3","financing_fee":"0","total_payable_amount":"30"}]
    d=data(profile(balance="100",minimum="0",prefs="installments",max_months="3"), [], {"r":opts})
    got=main.candidate(r,d)
    assert got["payment_plan"].count("|")==2

def test_partial_plan_cannot_finish_after_deadline():
    r=req(amount="30",deadline="2026-01-02",partial="true")
    bad={"request_id":"r","amount_safe_to_pay":"10","affordability_status":"affordable_with_plan","recommended_payment_method":"partial_payment","payment_plan":"2026-01-01:10|2026-01-03:20","earliest_date_for_full_payment":"2026-01-03","spending_changes_needed":"none","decision_explanation":"x"}
    with pytest.raises(AssertionError): main.validate_output(bad,r)

def test_multiple_flexible_changes_can_be_combined():
    p=profile(balance="100",minimum="0",prefs="full_payment"); p["expense_categories_user_is_willing_to_stop"]="streaming|music"
    events=[ev("s1",cat="streaming",amount="60",day=date(2026,1,2),flex="stoppable"), ev("s2",cat="music",amount="60",day=date(2026,1,3),flex="stoppable")]
    d=data(p,events); r=req(amount="100",deadline="2026-01-04")
    got=main.candidate(r,d)
    assert got["recommended_payment_method"]=="full_payment"
    assert got["spending_changes_needed"]=="stop:s1|stop:s2"

def test_message_ending_employment_overrides_future_income():
    future=ev("salary",typ="income",cat="salary",direction="credit",amount="100",day=date(2026,1,10),settle=date(2026,1,10),status="scheduled")
    p=profile(balance="50",minimum="50")
    msg={"message_id":"m","user_id":"u","request_id":"","related_event_id":"","sent_at":"2026-01-02T00:00:00Z","source_type":"employer","message_text":"Your employment has ended. There are no regular salary payments scheduled after the final settlement."}
    d=main.Data({"u":p},[],{}, {"u":[future]},[msg],[],{})
    ok,_=main.forecast("u",date(2026,1,1),d,((date(2026,1,10),Decimal("1")),))
    assert not ok

def test_repeated_variable_essential_spending_is_forecast():
    events=[
        ev("g1",cat="groceries",amount="20",day=date(2025,12,1)),
        ev("g2",cat="groceries",amount="25",day=date(2025,12,8)),
        ev("g3",cat="groceries",amount="30",day=date(2025,12,15)),
    ]
    d=data(profile(balance="100",minimum="50"),events)
    groups=main.recurring(events)
    assert any(xs[0].category=="groceries" for xs,_ in groups)

def test_forecast_exposes_event_level_movements_and_floor():
    e=ev("d",amount="20",day=date(2026,1,2))
    d=data(profile(balance="100",minimum="50"),[e])
    ok,balances=main.forecast("u",date(2026,1,1),d,())
    assert balances[date(2026,1,2)] == Decimal("80")
    assert ok

def test_safe_amount_excludes_optional_flexible_spend_until_change_is_requested():
    p=profile(balance="100",minimum="50",prefs="full_payment")
    p["expense_categories_user_is_willing_to_stop"]="streaming"
    e=ev("stream",typ="subscription",cat="streaming",amount="20",day=date(2025,12,1),flex="stoppable")
    d=data(p,[e])
    r=req(amount="50")
    assert main.safe_amount("u",r,d) == Decimal("50")
    ok,_=main.forecast("u",date(2026,1,1),d,((date(2026,1,1),Decimal("50")),))
    assert ok

def test_final_payroll_does_not_generate_future_salary():
    events=[ev("s1",typ="income",cat="salary",direction="credit",amount="100",day=date(2025,10,15)), ev("s2",typ="income",cat="salary",direction="credit",amount="100",day=date(2025,11,15))]
    events[-1].description="Final employer payroll"
    assert not any(xs[0].event_type=="income" for xs,_ in main.recurring(events))

def test_message_confirmed_salary_becomes_typed_future_credit():
    msg={"message_id":"m-salary","user_id":"u","request_id":"","related_event_id":"","sent_at":"2026-01-03T00:00:00Z","source_type":"employer","message_text":"Your first salary will be EUR 1661. The confirmed credit date is 2026-01-15."}
    d=main.Data({"u":profile(balance="0",minimum="0")},[],{}, {"u":[]}, [msg], [], {})
    events=main.semantic_events(d,"u")
    assert len(events)==1 and events[0].home_amount==Decimal("1661") and events[0].settlement_date==date(2026,1,15)
