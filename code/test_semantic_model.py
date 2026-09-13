"""Focused regression tests for the reconstructed semantic model."""
from datetime import date
from decimal import Decimal
import main

def ev(i, typ="expense", cat="shopping", direction="debit", amount="10",
       day=date(2026, 1, 1), status="settled", flex="fixed", settle=None,
       link="", description="same"):
    value = None if amount is None else Decimal(amount)
    return main.Event(i, "u", typ, description, cat, direction, value, "USD",
                      day, settle or day, status, link, flex, Decimal("0"), value)

def profile(balance="100", minimum="50"):
    return {"user_id":"u", "home_currency":"USD",
            "current_available_balance":balance,
            "minimum_balance_to_keep":minimum,
            "expense_categories_to_protect":"",
            "expense_categories_user_is_willing_to_reduce":"dining",
            "expense_categories_user_is_willing_to_stop":"streaming",
            "payment_methods_user_will_consider":"full_payment",
            "max_installment_months":""}

def test_variable_recurrence_is_evidence_without_invented_amount():
    xs = [ev("g1", cat="groceries", amount="20", day=date(2025,12,1)),
          ev("g2", cat="groceries", amount="25", day=date(2025,12,8)),
          ev("g3", cat="groceries", amount="30", day=date(2025,12,15))]
    groups = main.recurring(xs)
    assert len(groups) == 1
    assert groups[0].amount_policy == "RECURRING_AMOUNT_UNRESOLVED"
    assert groups[0].amount_estimate is None
    data = main.Data({"u": profile()}, [], {}, {"u": xs}, [], [], {})
    ok, balances = main.forecast("u", date(2026,1,1), data)
    assert ok and balances[date(2026,1,20)] == Decimal("100")

def test_historical_salary_does_not_create_future_credit():
    xs = [ev("s1", typ="income", cat="salary", direction="credit", amount="100", day=date(2025,10,15)),
          ev("s2", typ="income", cat="salary", direction="credit", amount="100", day=date(2025,11,15)),
          ev("s3", typ="income", cat="salary", direction="credit", amount="100", day=date(2025,12,15))]
    data = main.Data({"u": profile(balance="50", minimum="50")}, [], {}, {"u": xs}, [], [], {})
    ok, balances = main.forecast("u", date(2026,1,1), data)
    assert ok and balances[date(2026,1,20)] == Decimal("50")

def test_pending_settled_lifecycle_prefers_settled_row():
    pending = ev("pending", amount="40", day=date(2026,1,2), status="pending", settle=date(2026,1,3), link="txn")
    settled = ev("settled", amount="40", day=date(2026,1,2), status="settled", settle=date(2026,1,3), link="txn")
    data = main.Data({"u": profile(balance="100", minimum="50")}, [], {}, {"u": [pending, settled]}, [], [], {})
    live = main.semantic_events(data, "u")
    assert [e.event_id for e in live] == ["settled"]

def test_classification_requires_flexible_recurring_evidence_for_modification():
    p = profile()
    fixed = ev("x", cat="dining", flex="fixed")
    flexible = ev("y", cat="dining", flex="stoppable")
    assert main.classify_event(fixed, p)["modifiable"] is False
    assert main.classify_event(flexible, p)["modifiable"] is False
    recurrence = main.RecurrenceEvidence([flexible], 7, ("dining",), "RECURRING_AMOUNT_UNRESOLVED", None, ("y",), "unresolved")
    assert main.classify_event(flexible, p, recurrence)["modifiable"] is True

def test_forecast_trace_records_movements_and_policy():
    e = ev("d", amount="20", day=date(2026,1,2))
    data = main.Data({"u": profile()}, [], {}, {"u": [e]}, [], [], {})
    trace = main.forecast_trace("u", date(2026,1,1), data)
    assert trace["safe"] is True
    assert trace["policy"]["same_day_order"]
    assert trace["movements"][0]["event_id"] == "d"
    assert trace["movements"][0]["balance_after"] == "80"

def test_fixed_recurring_expense_requires_stable_amount():
    xs=[ev("r1",typ="subscription",cat="cloud_storage",amount="10",day=date(2025,10,1)),
        ev("r2",typ="subscription",cat="cloud_storage",amount="10",day=date(2025,11,1)),
        ev("r3",typ="subscription",cat="cloud_storage",amount="10",day=date(2025,12,1))]
    g=main.recurring(xs)[0]
    assert g.amount_policy == "SUPPORTED_FIXED_AMOUNT" and g.amount_estimate == Decimal("10")

def test_same_category_unrelated_descriptions_do_not_merge():
    xs=[ev("a",cat="groceries",description="Market",day=date(2025,10,1)),
        ev("b",cat="groceries",description="Supermarket",day=date(2025,10,8)),
        ev("c",cat="groceries",description="Market",day=date(2025,11,1))]
    assert not any(len(g.events) == 3 for g in main.recurring(xs))

def test_missed_salary_cycle_does_not_create_new_credit():
    xs=[ev("s1",typ="income",cat="salary",direction="credit",amount="100",day=date(2025,10,1)),
        ev("s2",typ="income",cat="salary",direction="credit",amount="100",day=date(2025,12,1))]
    data=main.Data({"u":profile(balance="50",minimum="50")},[],{}, {"u":xs},[],[],{})
    assert main.forecast("u",date(2026,1,1),data)[1][date(2026,1,20)] == Decimal("50")

def test_generic_scheduled_credit_is_not_available_capacity():
    e=ev("grant",typ="transfer",cat="other",direction="credit",amount="100",day=date(2026,1,5),status="scheduled")
    data=main.Data({"u":profile(balance="50",minimum="50")},[],{}, {"u":[e]},[],[],{})
    assert main.semantic_events(data,"u") == []

def test_explicit_replacement_is_used_without_inference():
    old=ev("old",amount="40",day=date(2026,1,2),status="failed")
    new=ev("new",amount="30",day=date(2026,1,4),status="settled",link="old")
    data=main.Data({"u":profile()},[],{}, {"u":[old,new]},[],[],{})
    live=main.semantic_events(data,"u")
    assert [e.event_id for e in live] == ["new"]

def test_90_day_boundary_excludes_day_90():
    e=ev("d90",amount="20",day=date(2026,4,1))
    data=main.Data({"u":profile()},[],{}, {"u":[e]},[],[],{})
    tr=main.forecast_trace("u",date(2026,1,1),data)
    assert all(x["date"] != "2026-04-01" for x in tr["movements"])
