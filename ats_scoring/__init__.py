# ats_scoring/__init__.py

# Import key functions so they can be accessed directly from ats_scoring
from .extract_text import extract_text
from .ats_scoring import analyze_ats_compliance

__all__ = ["extract_text", "analyze_ats_compliance"]
