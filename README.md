# AI Resume Analyzer & Job Match Dashboard

A real-time AI-powered tool to analyze resumes and match them against job descriptions using Streamlit.

## Features

- Upload PDF or DOCX resumes
- Input or paste job descriptions
- Extract skills, experience, and education from resumes
- Match resume vs job description using TF-IDF Vectorizer and Cosine Similarity
- Display match score, matched skills, missing skills, and improvement suggestions
- Interactive dashboard with gauge, bar charts, and lists

## Setup Instructions

1. Ensure you have Python 3.9+ installed.

2. Clone or download this repository to your local machine.

3. Navigate to the project directory:

   ```bash
   cd AI_Resume_Analyzer
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Download the spaCy English model:

   ```bash
   python -m spacy download en_core_web_sm
   ```

6. Verify installations by running the test script:

   ```bash
   python test_imports.py
   ```

   If all imports are successful, you're ready to run the app.

## Running the Application

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload a resume (PDF or DOCX), enter a job description, and click "Analyze Resume" to see the results.

## Project Structure

```
AI_Resume_Analyzer/
├── app.py                    # Main Streamlit application
├── config.py                 # Configuration constants
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── test_imports.py           # Import verification script
├── utils/
│   ├── text_cleaner.py       # Text cleaning utilities
│   ├── file_loader.py        # File loading helpers
│   └── skill_matcher.py      # Skill matching logic
├── resume_parser/
│   ├── pdf_parser.py         # PDF text extraction
│   ├── docx_parser.py        # DOCX text extraction
│   └── resume_reader.py      # Unified resume reading interface
├── nlp_engine/
│   ├── preprocessing.py      # Text preprocessing
│   ├── skill_extractor.py    # Skill extraction using spaCy
│   ├── experience_extractor.py # Experience extraction
│   ├── education_extractor.py  # Education extraction
│   └── matcher.py            # Resume-job matching using TF-IDF
├── dashboard/
│   ├── charts.py             # Chart generation
│   └── layout.py             # Dashboard layout components
└── data/
    └── skills_db/skills_list.json  # Skills database
```

## Technical Details

- **Frontend**: Streamlit
- **PDF Parsing**: pdfplumber
- **DOCX Parsing**: python-docx
- **NLP**: spaCy with en_core_web_sm
- **Matching**: scikit-learn TF-IDF Vectorizer and Cosine Similarity
- **Python Version**: 3.9+

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is open-source. Use at your own risk.