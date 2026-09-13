# Phase 16 Deadline Policy

The solver keeps capacity date, deadline feasibility, and plan feasibility
separate. A post-deadline capacity date cannot be emitted as an in-deadline wait
plan. Safe-today and safe-on-deadline are feasible when all other constraints
pass; safe-after-deadline and never-safe cases remain governed by the explicit
late-deadline policy because the specification does not fully define status
mapping. No production change was made.
