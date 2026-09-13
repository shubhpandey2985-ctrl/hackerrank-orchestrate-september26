import tempfile
from pathlib import Path
import main

ROOT = Path(__file__).resolve().parents[1]

def test_load_schema_and_links():
    d = main.load_data(ROOT)
    assert len(d.profiles) == 275
    assert len(d.requests) == 250
    assert len(d.events) == 275
    assert sum(len(v) for v in d.options.values()) == 790
    assert len(d.images) == 16
    assert all(e.event_id for xs in d.events.values() for e in xs)

def test_blank_amounts_have_evidence():
    d = main.load_data(ROOT)
    blanks = [e for xs in d.events.values() for e in xs if e.amount is None]
    assert len(blanks) == 16
    assert all(e.evidence for e in blanks)

def test_decimal_parser():
    assert main.D("1,234.50") == main.Decimal("1234.50")
    assert main.fmt(main.Decimal("12.00")) == "12"

def test_normalization_and_lifecycle():
    d = main.load_data(ROOT)
    main.normalize_events(d, ROOT)
    all_events = [e for xs in d.events.values() for e in xs]
    assert all(e.home_amount is not None for e in all_events)
    assert all(e.excluded_reason for e in all_events if e.status in {"cancelled","failed","unrealized"})
    assert all(e.home_amount >= 0 for e in all_events)

def test_direct_fx_only():
    d = main.load_data(ROOT)
    main.normalize_events(d, ROOT)
    foreign = [e for xs in d.events.values() for e in xs if e.currency != d.profiles[e.user_id]["home_currency"]]
    assert foreign
    assert all(e.home_amount is not None for e in foreign)
