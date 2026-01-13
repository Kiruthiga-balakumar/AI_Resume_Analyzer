"""
Skill extraction using spaCy and skills database.
"""

from typing import List
import spacy
from spacy.util import is_package
import config
from utils.file_loader import load_skills_db


# -------------------------------
# Load spaCy model safely
# -------------------------------
def load_spacy_model():
    """
    Load spaCy NLP model safely for local and cloud environments.
    """
    model_name = config.NLP_MODEL

    if is_package(model_name):
        return spacy.load(model_name)

    raise RuntimeError(
        f"spaCy model '{model_name}' is not installed. "
        "Make sure it is added to requirements.txt"
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

    # Extract single-word skills using POS tagging
    for token in doc:
        if token.pos_ in ("NOUN", "PROPN"):
            lemma = token.lemma_.lower()
            if lemma in skills_db_set:
                extracted_skills.add(lemma)

    # Extract multi-word skills (phrase matching)
    text_lower = text.lower()
    for skill in skills_db_set:
        if skill in text_lower:
            extracted_skills.add(skill)

    return sorted(extracted_skills)
