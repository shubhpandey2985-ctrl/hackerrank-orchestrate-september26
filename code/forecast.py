"""Deterministic fixed-point forecast boundary."""
from datetime import date
from decimal import Decimal

def simulate(user_id, request_date: date, data, payments=(), changes=()):
    from main import forecast
    return forecast(user_id, request_date, data, payments, changes)

def trace(user_id, request_date: date, data, payments=(), changes=(), include_optional=True):
    from main import forecast_trace
    return forecast_trace(user_id, request_date, data, payments, changes, include_optional)

def safe_amount(user_id, request, data, changes=()):
    from main import safe_amount as _safe
    return _safe(user_id, request, data, changes)

def earliest_full_payment(user_id, request, data, changes=()):
    from main import earliest
    return earliest(user_id, request, data, changes)
