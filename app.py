from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfReader
import spacy
import google.generativeai as palm
from googleapiclient.discovery import build

app = Flask(__name__)

# Configure generative AI model
palm.configure(api_key='AIzaSyC83Yrs5-IcKklvTCd3FEonXeOxRPUjM34')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Configure YouTube API
API_KEY = 'AIzaSyAxcZzWGyjLT8wKeEZZ-beEAHZ40SkvddY'

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def extract_keywords(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return keywords

def generate_analysis(job, resume_text):
    keywords = extract_keywords(resume_text)
    keywords_str = ', '.join(keywords)
    
    prompt = f"My job is {job} and my skills are {keywords_str}. give a score of resume out of 10. suggest required skills which are not present in the resume"

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )

    return completion.result

def search_youtube_videos(query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        title = search_result['snippet']['title']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append({'title': title, 'video_id': video_id, 'video_url': video_url})

    return videos

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job = request.form['job']
        resume_file = request.files['resume']

        if resume_file:
            # Save the uploaded resume
            resume_filename = secure_filename(resume_file.filename)
            resume_path = os.path.join('uploads', resume_filename)
            resume_file.save(resume_path)

            # Extract text from the resume
            resume_text = extract_text_from_pdf(resume_path)

            # Generate analysis
            analysis_result = generate_analysis(job, resume_text)

            # Search YouTube videos
            search_query = f"{job} skills in one video"
            youtube_results = search_youtube_videos(search_query)

            return render_template('result.html', job=job, analysis=analysis_result, videos=youtube_results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)