#!/usr/bin/env python3
"""
Test script to verify all required imports and installations.
"""

import sys
import json

def test_imports():
    try:
        import streamlit as st
        print(f"Streamlit version: {st.__version__}")
    except ImportError as e:
        print(f"Failed to import streamlit: {e}")
        return False

    try:
        import pdfplumber
        print(f"pdfplumber version: {pdfplumber.__version__}")
    except ImportError as e:
        print(f"Failed to import pdfplumber: {e}")
        return False

    try:
        import docx
        print("python-docx imported successfully")
    except ImportError as e:
        print(f"Failed to import python-docx: {e}")
        return False

    try:
        import spacy
        print(f"spaCy version: {spacy.__version__}")
        try:
            nlp = spacy.load("en_core_web_sm")
            print("en_core_web_sm loaded successfully")
        except OSError:
            print("en_core_web_sm not installed. Run: python -m spacy download en_core_web_sm")
            return False
    except ImportError as e:
        print(f"Failed to import spacy: {e}")
        return False

    try:
        import sklearn
        print(f"scikit-learn version: {sklearn.__version__}")
    except ImportError as e:
        print(f"Failed to import scikit-learn: {e}")
        return False

    # Test config
    try:
        import config
        print("config imported successfully")
        print(f"SKILLS_DB_PATH: {config.SKILLS_DB_PATH}")
        print(f"NLP_MODEL: {config.NLP_MODEL}")
    except ImportError as e:
        print(f"Failed to import config: {e}")
        return False

    # Test skills db
    try:
        with open(config.SKILLS_DB_PATH, 'r') as f:
            skills = json.load(f)
        print(f"Skills database loaded with {len(skills)} skills")
    except Exception as e:
        print(f"Failed to load skills database: {e}")
        return False

    print("All imports successful!")
    return True

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)