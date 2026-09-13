"""Fact-bundle explanation boundary. Deterministic template is authoritative."""
def render(row):
    return row["decision_explanation"]

def llm_can_change_financial_facts():
    return False
