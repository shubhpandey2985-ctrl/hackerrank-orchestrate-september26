"""Evidence adapter. It returns facts only; it cannot authorize decisions."""
from pathlib import Path

def image_amount(root: Path, event):
    from main import extract_image_amount
    return extract_image_amount(Path(root), event)

def llm_allowed_for_fact_extraction():
    return True

def llm_can_authorize_plan():
    return False
