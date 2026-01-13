"""
Experience extraction from resume text.
"""

import re
from typing import Optional

def extract_experience_years(text: str) -> Optional[int]:
    """
    Extract total years of experience from the text.

    Args:
        text (str): Resume text.

    Returns:
        Optional[int]: Total years of experience or None if not found.
    """
    # Patterns to match years of experience
    patterns = [
        r'(\d+)\s*(?:\+?\s*)?years?\s*(?:of\s*)?experience',
        r'experience\s*(?:of\s*)?(\d+)\s*(?:\+?\s*)?years?',
        r'(\d+)\s*(?:\+?\s*)?years?\s*in\s*',
    ]

    max_years = 0
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            try:
                years = int(match)
                if years > max_years:
                    max_years = years
            except ValueError:
                continue

    return max_years if max_years > 0 else None