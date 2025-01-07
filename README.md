
# Resume Review Flask App

## Description
A Flask-based web application for resume review, using the Google Bard/Gemini API to analyze user resumes against job titles. The app provides a rating out of 10 and suggests related videos using the YouTube Data API.

## Features
- Upload a PDF resume.
- Extracts text from the resume and analyzes it using Google Bard/Gemini API.
- Rates the resume out of 10 based on job title relevance.
- Suggests missing skills for the given job.
- Recommends related videos using the YouTube Data API.

## Technologies Used
- **Flask**: Web framework for Python.
- **PyPDF2**: For extracting text from PDF files.
- **spaCy**: For natural language processing and keyword extraction.
- **Google Bard/Gemini API**: For generative AI text analysis.
- **YouTube Data API**: For fetching related videos.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-review-app.git
   cd resume-review-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the API keys:
   - **Google Bard/Gemini API**: Replace the `api_key` in `palm.configure` with your Google Bard/Gemini API key.
   - **YouTube Data API**: Replace `API_KEY` with your YouTube Data API key.

5. Create an `uploads` directory in the project root to store uploaded resumes:
   ```bash
   mkdir uploads
   ```

## Usage
1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Upload a resume (PDF format) and enter the desired job title.
4. View the analysis, rating, and recommended videos.

## File Structure
```
resume-review-app/
├── app.py                # Main Flask application
├── templates/
│   ├── index.html        # Form for uploading resume and entering job title
│   └── result.html       # Displays analysis and recommended videos
├── uploads/              # Directory for uploaded resumes
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [spaCy Documentation](https://spacy.io/)
- [Google Bard/Gemini API](https://cloud.google.com/)
- [YouTube Data API](https://developers.google.com/youtube/v3)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
