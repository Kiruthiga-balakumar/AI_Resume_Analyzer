"""
PDF parser for extracting text from PDF resumes.
"""

import pdfplumber
from typing import Optional

def extract_text_from_pdf(file_path: str) -> Optional[str]:
    """
    Extract text content from a PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        Optional[str]: Extracted text or None if extraction fails.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None