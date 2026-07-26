# Resume Parser Project

## Overview
This project is a simple resume parser built with Flask and SpaCy.  
It extracts key information such as Name, Education, Skills, and Experience from a resume PDF.

## Requirements
- Python 3.x
- Flask
- pdfplumber
- spacy

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/tamanna206/Resume_Parser_Project2.git
pip install -r requirements.txt
python app.py
Test with Postman:

Method: POST

URL: http://127.0.0.1:5000/parse_resume (127.0.0.1 in Bing)

Body: form‑data → Key = resume, Type = File, Value = resume.pdf

## Features
- Upload resume in PDF format
- Extract Name, Education, Skills, Experience
- JSON output for easy integration

## Future Improvements
- Add web UI for resume upload
- Store parsed data in database
- Support for multiple languages
