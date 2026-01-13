"""
Dashboard layout components.
"""

import streamlit as st
from typing import Dict, Any
from .charts import create_match_gauge, create_skills_bar_chart

def display_results(results: Dict[str, Any]):
    """
    Display the analysis results in the dashboard.

    Args:
        results (Dict[str, Any]): Analysis results.
    """
    st.header("Analysis Results")

    # Match Score
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Match Score", f"{results['match_score']}%")
    with col2:
        st.plotly_chart(create_match_gauge(results['match_score']), use_container_width=True)

    # Skills
    st.subheader("Skills Analysis")
    col3, col4 = st.columns(2)
    with col3:
        st.write("**Matched Skills:**")
        if results['matched_skills']:
            for skill in results['matched_skills']:
                st.write(f"✅ {skill}")
        else:
            st.write("No matched skills found.")
    with col4:
        st.write("**Missing Skills:**")
        if results['missing_skills']:
            for skill in results['missing_skills']:
                st.write(f"❌ {skill}")
        else:
            st.write("No missing skills.")

    # Skills Chart
    st.plotly_chart(create_skills_bar_chart(results['matched_skills'], results['missing_skills']), use_container_width=True)

    # Experience and Education
    st.subheader("Resume Summary")
    col5, col6 = st.columns(2)
    with col5:
        exp = results.get('resume_experience')
        st.write(f"**Experience:** {exp} years" if exp else "**Experience:** Not detected")
    with col6:
        edu = results.get('resume_education', [])
        st.write(f"**Education:** {', '.join(edu)}" if edu else "**Education:** Not detected")

    # Suggestions
    st.subheader("Improvement Suggestions")
    for suggestion in results.get('suggestions', []):
        st.write(f"💡 {suggestion}")