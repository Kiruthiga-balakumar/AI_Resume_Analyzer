"""
Text preprocessing for NLP tasks.
"""

import spacy
from typing import List
import config

# Load the spaCy model
nlp = spacy.load(config.NLP_MODEL)

def preprocess_text(text: str) -> str:
    """
    Preprocess text for NLP analysis.

    Args:
        text (str): Input text.

    Returns:
        str: Preprocessed text.
    """
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    return " ".join(tokens)

def tokenize_text(text: str) -> List[str]:
    """
    Tokenize text into words.

    Args:
        text (str): Input text.

    Returns:
        List[str]: List of tokens.
    """
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_space]