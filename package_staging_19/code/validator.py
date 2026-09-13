"""Reject-only output and plan validation boundary."""
def validate(row, request, data=None):
    from main import validate_output
    return validate_output(row, request, data)
