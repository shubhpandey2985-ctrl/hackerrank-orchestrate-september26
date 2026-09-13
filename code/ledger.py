"""Canonical event/lifecycle and currency-normalization boundary."""
from pathlib import Path

def normalize(data, root: Path):
    from main import normalize_events
    normalize_events(data, Path(root))
    return data

def cash_events(data, user_id):
    from main import semantic_events
    return semantic_events(data, user_id)
