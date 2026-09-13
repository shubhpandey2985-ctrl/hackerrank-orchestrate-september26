# Phase 19 Policy Boundary

All unresolved semantics are centralized in `code/policy.py` and are explicit
engineering policies, not claims about hidden specification rules.

| Policy | Selected value | Classification | Conservative interpretation | Main risk |
|---|---|---|---|---|
| `VARIABLE_SPENDING_POLICY` | `FIXED_ONLY_UNRESOLVED_VARIABLE` | UNSUPPORTED alternatives rejected | Preserve varying observations; project no invented amount | False negatives |
| `RECURRENCE_CALENDAR_POLICY` | `OBSERVED_INTERVAL` | UNRESOLVED policy | Use only supported fixed observed interval | Month-end/missed-cycle mismatch |
| `RECURRENCE_THRESHOLD_POLICY` | existing configured threshold | UNRESOLVED policy | Do not broaden recurrence identity | Missed valid recurrence |
| `OPTIONAL_BASELINE_POLICY` | `CURRENT_BEHAVIOR` | UNRESOLVED policy | Preserve existing safe/earliest split | Optional-capacity ambiguity |
| `SCHEDULED_CREDIT_POLICY` | `CONFIRMED_SALARY_ONLY` | SPECIFICATION/strong evidence | Generic scheduled credit contributes no cash | Conservative false negative |
| `SAME_DAY_ORDER_POLICY` | credits → required debits → plan payment | POLICY CHOICE | Deterministic and consistently applied | Unspecified settlement order |
| `REPLACEMENT_POLICY` | `NEVER_INVENT` | SPECIFICATION-EXPLICIT | Require supplied date and amount | False negatives |
| `DEADLINE_STATUS_POLICY` | `CAPACITY_ONLY_NO_RECOMMENDATION` | UNRESOLVED policy | Never treat post-deadline capacity as in-deadline plan | Status ambiguity |
| `DECIMAL_PRESENTATION_POLICY` | Decimal quantize at configured scale | UNRESOLVED presentation | Separate numeric value from serialized value | Trailing-zero mismatch |

Every policy is deterministic, testable, and visible in the audit trace.
