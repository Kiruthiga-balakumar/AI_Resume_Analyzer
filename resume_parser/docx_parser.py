"""
DOCX parser for extracting text from DOCX resumes.
"""

from docx import Document
from typing import Optional

def extract_text_from_docx(file_path: str) -> Optional[str]:
    """
    Extract text content from a DOCX file.

    Args:
        file_path (str): Path to the DOCX file.

    Returns:
        Optional[str]: Extracted text or None if extraction fails.
    """
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from DOCX: {e}")
        return None