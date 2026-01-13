"""
Skill extraction using spaCy and skills database.
"""

from typing import List
import spacy
import config
from utils.file_loader import load_skills_db


# -------------------------------
# Load spaCy model safely
# -------------------------------
def load_spacy_model():
    """
    Load spaCy NLP model safely for both local and Streamlit Cloud environments.
    """
    try:
        return spacy.load(config.NLP_MODEL)
    except OSError as e:
        raise RuntimeError(
            f"spaCy model '{config.NLP_MODEL}' not found. "
            f"Ensure it is installed via requirements.txt.\n{e}"
        )


nlp = load_spacy_model()


# -------------------------------
# Skill Extraction Function
# -------------------------------
def extract_skills(text: str) -> List[str]:
    """
    Extract skills from the given text using spaCy and a skills database.

    Args:
        text (str): Input resume or job description text.

    Returns:
        List[str]: Sorted list of extracted skills.
    """
    if not text:
        return []

    # Load skills database
    skills_db = load_skills_db(config.SKILLS_DB_PATH)
    skills_db_set = set(skill.lower() for skill in skills_db)

    doc = nlp(text.lower())
    extracted_skills = set()

    # Extract single-word skills
    for token in doc:
        if token.pos_ in ("NOUN", "PROPN"):
            lemma = token.lemma_.lower()
            if lemma in skills_db_set:
                extracted_skills.add(lemma)

    # Extract multi-word skills
    text_lower = text.lower()
    for skill in skills_db_set:
        if skill in text_lower:
            extracted_skills.add(skill)

    return sorted(extracted_skills)
