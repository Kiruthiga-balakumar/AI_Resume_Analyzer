"""
Skill extraction using spaCy and skills database.
"""

import spacy
from typing import List
import config
from utils.file_loader import load_skills_db

# Load the spaCy model
nlp = spacy.load(config.NLP_MODEL)

def extract_skills(text: str) -> List[str]:
    """
    Extract skills from the given text.

    Args:
        text (str): Input text.

    Returns:
        List[str]: List of extracted skills.
    """
    skills_db = load_skills_db(config.SKILLS_DB_PATH)
    skills_db_set = set(skills_db)

    doc = nlp(text.lower())
    extracted_skills = set()

    # Extract nouns and proper nouns as potential skills
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN']:
            lemma = token.lemma_.lower()
            if lemma in skills_db_set:
                extracted_skills.add(lemma)

    # Also check for multi-word skills (simple approach)
    for skill in skills_db:
        if skill in text.lower():
            extracted_skills.add(skill)

    return sorted(list(extracted_skills))