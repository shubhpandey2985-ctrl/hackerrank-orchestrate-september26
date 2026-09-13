"""Candidate generation and deterministic ranking boundary."""
def generate(request, data):
    from main import candidate
    return candidate(request, data)
