"""
Skill extraction using spaCy and skills database.
"""

from typing import List
import spacy
import config
from utils.file_loader import load_skills_db


# Load spaCy model (Cloud + Local compatible)
nlp = spacy.load(config.NLP_MODEL)


def extract_skills(text: str) -> List[str]:
    """
    Extract skills from the given text using spaCy and a skills database.
    """
    if not text:
        return []

    skills_db = load_skills_db(config.SKILLS_DB_PATH)
    skills_db_set = set(skill.lower() for skill in skills_db)

    doc = nlp(text.lower())
    extracted_skills = set()

    for token in doc:
        if token.pos_ in ("NOUN", "PROPN"):
            lemma = token.lemma_.lower()
            if lemma in skills_db_set:
                extracted_skills.add(lemma)

    text_lower = text.lower()
    for skill in skills_db_set:
        if skill in text_lower:
            extracted_skills.add(skill)

    return sorted(extracted_skills)
