"""Explicit policies for semantics the challenge leaves undefined.

These are configuration choices, not claims about the official hidden-test rules.
Each policy is tested independently and surfaced in the audit trace.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Policy:
    forecast_days: int = 90
    same_day_order: str = "credits_before_required_debits_before_plan"
    recurrence_min_observations: int = 3
    recurrence_gap_tolerance_days: int = 3
    month_end_mode: str = "clamp_to_last_day"
    scheduled_credit_mode: str = "confirmed_salary_only"
    failed_replacement_mode: str = "never_invent"
    late_deadline_mode: str = "capacity_only_no_recommendation"
    decimal_scale: int = 2
    decimal_rounding: str = "ROUND_HALF_EVEN"
    flexible_tie_break: str = "sorted_event_id_then_action"

DEFAULT_POLICY = Policy()
