"""
File loading utilities.
"""

import json
import os
from typing import List

def load_skills_db(skills_db_path: str) -> List[str]:
    """
    Load the skills database from a JSON file.

    Args:
        skills_db_path (str): Path to the skills JSON file.

    Returns:
        List[str]: List of skills.
    """
    if not os.path.exists(skills_db_path):
        raise FileNotFoundError(f"Skills database not found at {skills_db_path}")

    with open(skills_db_path, 'r', encoding='utf-8') as f:
        skills = json.load(f)

    return [skill.lower() for skill in skills]