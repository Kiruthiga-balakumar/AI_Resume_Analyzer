"""
Resume-job matching using TF-IDF and cosine similarity.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Any
from .skill_extractor import extract_skills
from .experience_extractor import extract_experience_years
from .education_extractor import extract_education
from utils.skill_matcher import find_matched_skills, find_missing_skills

def match_resume_to_job(resume_text: str, job_text: str) -> Dict[str, Any]:
    """
    Match resume to job description and return analysis results.

    Args:
        resume_text (str): Resume text.
        job_text (str): Job description text.

    Returns:
        Dict[str, Any]: Matching results including score, skills, etc.
    """
    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    # Extract experience and education
    resume_experience = extract_experience_years(resume_text)
    resume_education = extract_education(resume_text)

    # Find matched and missing skills
    matched_skills = find_matched_skills(resume_skills, job_skills)
    missing_skills = find_missing_skills(resume_skills, job_skills)

    # Compute TF-IDF similarity
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_score = round(similarity * 100, 2)

    # Generate suggestions
    suggestions = generate_suggestions(matched_skills, missing_skills, resume_experience, resume_education)

    return {
        'match_score': match_score,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'resume_skills': resume_skills,
        'job_skills': job_skills,
        'resume_experience': resume_experience,
        'resume_education': resume_education,
        'suggestions': suggestions
    }

def generate_suggestions(matched_skills: list, missing_skills: list, experience: int, education: list) -> list:
    """
    Generate actionable improvement suggestions.

    Args:
        matched_skills: List of matched skills.
        missing_skills: List of missing skills.
        experience: Years of experience.
        education: List of education qualifications.

    Returns:
        List of suggestions.
    """
    suggestions = []

    if missing_skills:
        suggestions.append(f"Consider learning or gaining experience in: {', '.join(missing_skills[:5])}")

    if not experience or experience < 2:
        suggestions.append("Gain more professional experience to strengthen your resume.")

    if not education:
        suggestions.append("Highlight your educational qualifications more prominently.")

    if len(matched_skills) < 5:
        suggestions.append("Expand your skill set to match more job requirements.")

    suggestions.append("Tailor your resume keywords to better match the job description.")

    return suggestions