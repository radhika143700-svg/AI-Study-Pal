from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import os
from models.ml_models import QuizGenerator, ResourceSuggester
from models.nlp_processor import NLPProcessor
from models.dl_models import TextSummarizer, FeedbackGenerator

app = Flask(__name__)

# Initialize components
quiz_gen = QuizGenerator()
resource_suggester = ResourceSuggester()
nlp_processor = NLPProcessor()
summarizer = TextSummarizer()
feedback_gen = FeedbackGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    data = request.json
    subject = data.get('subject')
    hours = int(data.get('hours'))

    # Simple study plan generation
    plan = f"Study Plan for {subject}:\n"
    plan += f"Total Hours: {hours}\n"
    plan += f"Daily: {hours//7} hours per day for 7 days\n"
    plan += "Focus on key topics and practice problems."

    # Generate quiz
    quiz = quiz_gen.generate_quiz(subject, 5)

    # Get resources
    resources = resource_suggester.suggest_resources(subject)

    # Summarize text (using sample text)
    sample_text = "Mathematics is the study of numbers, shapes, and patterns."
    summary = summarizer.summarize(sample_text)

    # Generate tips
    keywords = nlp_processor.extract_keywords(sample_text)
    tips = nlp_processor.generate_study_tips(keywords)

    # Generate feedback
    feedback = feedback_gen.generate_feedback(subject)

    # Create CSV schedule
    schedule_data = {
        'Day': [f'Day {i+1}' for i in range(7)],
        'Hours': [hours//7] * 7,
        'Topic': [f'{subject} Topic {i+1}' for i in range(7)]
    }
    df_schedule = pd.DataFrame(schedule_data)
    schedule_path = f'static/schedule_{subject}.csv'
    df_schedule.to_csv(schedule_path, index=False)

    return jsonify({
        'plan': plan,
        'quiz': quiz,
        'resources': resources,
        'summary': summary,
        'tips': tips,
        'feedback': feedback,
        'schedule_url': f'/download/{subject}'
    })

@app.route('/download/<subject>')
def download_schedule(subject):
    path = f'static/schedule_{subject}.csv'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
