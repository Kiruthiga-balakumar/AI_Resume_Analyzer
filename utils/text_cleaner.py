"""
Text cleaning utilities for resume and job description processing.
"""

import re

def clean_text(text: str) -> str:
    """
    Clean the input text by normalizing whitespace and removing unwanted characters.

    Args:
        text (str): The raw text to clean.

    Returns:
        str: The cleaned text.
    """
    if not text:
        return ""

    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text.strip())

    # Remove non-printable characters
    text = re.sub(r'[^\x20-\x7E\n]', '', text)

    return text