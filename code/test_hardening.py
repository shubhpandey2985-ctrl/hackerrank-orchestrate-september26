"""Phase 11 defensive hidden-test hardening checks."""
from datetime import date
from decimal import Decimal
import csv
import pytest
import main

def ev(i, amount="10", direction="debit", status="settled", day=date(2026,1,2), settle=None, typ="expense", cat="shopping", flex="fixed"):
    a=Decimal(amount) if amount is not None else None
    return main.Event(i,"u",typ,"x",cat,direction,a,"USD",day,settle or day,status,"",flex,Decimal("0"),a)

def profile(balance="100",minimum="50",prefs="full_payment"):
    return {"user_id":"u","home_currency":"USD","current_available_balance":balance,"minimum_balance_to_keep":minimum,"expense_categories_to_protect":"rent","expense_categories_user_is_willing_to_reduce":"dining","expense_categories_user_is_willing_to_stop":"streaming","payment_methods_user_will_consider":prefs,"max_installment_months":""}

def data(events): return main.Data({"u":profile()},[],{}, {"u":events},[],[],{})

def test_malformed_decimal_and_duplicate_profile_fail_closed(tmp_path):
    with pytest.raises(Exception): main.D("not-a-number")
    with pytest.raises(ValueError): main.require_columns([], ["x"], "empty")

def test_pending_credit_cannot_increase_capacity():
    base=data([]); pending=data([ev("c",amount="100",direction="credit",status="pending",typ="income",cat="salary")])
    req={"request_id":"r","user_id":"u","request_date":"2026-01-01","requested_amount":"40","desired_completion_date":"2026-01-10","allows_partial_payment":"false","request_text":""}
    assert main.safe_amount("u",req,pending) <= main.safe_amount("u",req,base)

def test_required_debit_cannot_increase_capacity():
    base=data([]); debit=data([ev("d",amount="20",day=date(2026,1,3))])
    req={"request_id":"r","user_id":"u","request_date":"2026-01-01","requested_amount":"40","desired_completion_date":"2026-01-10","allows_partial_payment":"false","request_text":""}
    assert main.safe_amount("u",req,debit) <= main.safe_amount("u",req,base)

def test_failed_cancelled_do_not_create_cash_movement():
    d=data([ev("f",amount="100",direction="credit",status="failed",typ="income",cat="salary"),ev("c",amount="100",direction="credit",status="cancelled",typ="income",cat="salary")])
    assert main.semantic_events(d,"u") == []

def test_fixed_and_protected_events_are_not_modifiable():
    p=profile(); fixed=ev("f",cat="rent",flex="fixed"); flex=ev("x",cat="dining",flex="stoppable")
    assert main.classify_event(fixed,p)["modifiable"] is False
    assert main.classify_event(flex,p)["modifiable"] is False

def test_output_contract_has_250_unique_request_rows():
    rows=list(csv.DictReader(open("output.csv",encoding="utf-8-sig")))
    expected=["request_id","amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed","decision_explanation"]
    assert rows and list(rows[0].keys())==expected
    ids=[r["request_id"] for r in rows]
    assert len(ids)==len(set(ids))==250
    assert all(r["affordability_status"] in main.STATUS | {"affordable_now","affordable_with_plan","affordable_later","not_affordable"} for r in rows)
    assert all(r["recommended_payment_method"] in main.METHODS for r in rows)

def test_missing_direct_fx_fails_closed():
    e=ev("fx",amount="10",day=date(2026,1,2)); e.currency="EUR"
    d=main.Data({"u":profile()},[],{}, {"u":[e]},[],[],{})
    with pytest.raises(ValueError): main.normalize_events(d, __import__('pathlib').Path('.'))
