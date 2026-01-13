"""
Unified resume reader that handles PDF and DOCX files.
"""

import os
from typing import Optional
from .pdf_parser import extract_text_from_pdf
from .docx_parser import extract_text_from_docx

def read_resume(file_path: str) -> Optional[str]:
    """
    Read and extract text from a resume file (PDF or DOCX).

    Args:
        file_path (str): Path to the resume file.

    Returns:
        Optional[str]: Extracted text or None if reading fails.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_ext in ['.docx', '.doc']:
        return extract_text_from_docx(file_path)
    else:
        print(f"Unsupported file type: {file_ext}")
        return None