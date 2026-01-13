"""
Education extraction from resume text.
"""

import re
from typing import List

def extract_education(text: str) -> List[str]:
    """
    Extract education qualifications from the text.

    Args:
        text (str): Resume text.

    Returns:
        List[str]: List of education qualifications.
    """
    # Common degree keywords
    degrees = [
        'bachelor', 'bachelors', 'bsc', 'ba', 'bs',
        'master', 'masters', 'msc', 'ma', 'ms', 'mba',
        'phd', 'doctorate', 'ph.d', 'doctor',
        'associate', 'diploma', 'certificate'
    ]

    found_degrees = set()
    text_lower = text.lower()

    for degree in degrees:
        if degree in text_lower:
            found_degrees.add(degree.capitalize())

    # Also check for full phrases
    patterns = [
        r'\b(bachelor|master|phd|doctorate)\b',
        r'\b(bsc|msc|ba|ma|bs|ms|mba)\b',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text_lower)
        for match in matches:
            found_degrees.add(match.capitalize())

    return sorted(list(found_degrees))