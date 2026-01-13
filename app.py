"""
Main Streamlit application for AI Resume Analyzer & Job Match Dashboard.
"""

import streamlit as st
import tempfile
import os
from resume_parser.resume_reader import read_resume
from utils.text_cleaner import clean_text
from nlp_engine.matcher import match_resume_to_job
from dashboard.layout import display_results

def main():
    st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

    st.title("📄 AI Resume Analyzer & Job Match Dashboard")
    st.markdown("Upload your resume and paste a job description to get an AI-powered match analysis.")

    # Input section
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Upload Resume")
        uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])

    with col2:
        st.subheader("Job Description")
        job_description = st.text_area("Paste the job description here", height=200)

    # Analyze button
    if st.button("Analyze Resume", type="primary"):
        if not uploaded_file:
            st.error("Please upload a resume file.")
            return
        if not job_description.strip():
            st.error("Please enter a job description.")
            return

        with st.spinner("Analyzing..."):
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name

            try:
                # Read resume
                resume_text = read_resume(tmp_file_path)
                if not resume_text:
                    st.error("Failed to extract text from the resume. Please check the file format.")
                    return

                # Clean texts
                resume_text = clean_text(resume_text)
                job_text = clean_text(job_description)

                # Match
                results = match_resume_to_job(resume_text, job_text)

                # Display results
                display_results(results)

            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")
            finally:
                # Clean up temp file
                os.unlink(tmp_file_path)

if __name__ == "__main__":
    main()