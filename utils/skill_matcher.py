"""
Skill matching utilities.
"""

from typing import List, Set

def find_matched_skills(resume_skills: List[str], job_skills: List[str]) -> List[str]:
    """
    Find skills that are present in both resume and job description.

    Args:
        resume_skills (List[str]): Skills extracted from resume.
        job_skills (List[str]): Skills required in job description.

    Returns:
        List[str]: List of matched skills.
    """
    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)
    matched = resume_set.intersection(job_set)
    return sorted(list(matched))

def find_missing_skills(resume_skills: List[str], job_skills: List[str]) -> List[str]:
    """
    Find skills that are required in job but missing in resume.

    Args:
        resume_skills (List[str]): Skills extracted from resume.
        job_skills (List[str]): Skills required in job description.

    Returns:
        List[str]: List of missing skills.
    """
    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)
    missing = job_set - resume_set
    return sorted(list(missing))