"""I/O boundary. Parsing and relational validation are delegated through a lazy
adapter to retain compatibility with the existing command-line entry point."""
from pathlib import Path

def load(root: Path):
    from main import load_data
    return load_data(Path(root))

def required_output_columns():
    from main import OUT_COLS
    return tuple(OUT_COLS)
