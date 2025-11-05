from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import json
from datetime import datetime, timedelta
import csv
import io

app = Flask(__name__)

class StudyPal:
    def __init__(self):
        self.subjects = ['Math', 'Science', 'History', 'English', 'Computer Science']
        self.topics = {
            'Math': ['Algebra', 'Geometry', 'Calculus', 'Statistics'],
            'Science': ['Physics', 'Chemistry', 'Biology', 'Earth Science'],
            'History': ['Ancient History', 'Modern History', 'World Wars', 'Civilizations'],
            'English': ['Grammar', 'Literature', 'Writing', 'Reading Comprehension'],
            'Computer Science': ['Programming', 'Data Structures', 'Algorithms', 'Databases']
        }

    def generate_study_plan(self, subject, hours_per_day, days):
        subject_topics = self.topics.get(subject, ['Topic 1', 'Topic 2', 'Topic 3', 'Topic 4'])
        plan = []
        for day in range(days):
            topic = subject_topics[day % len(subject_topics)]
            plan.append({
                'day': day + 1,
                'topic': topic,
                'hours': hours_per_day,
                'tasks': f'Study {topic} for {hours_per_day} hours'
            })
        return plan

    def generate_quiz(self, subject):
        quizzes = {
            'Math': [
                {'question': 'What is 2 + 2?', 'options': ['3', '4', '5', '6'], 'answer': 1},
                {'question': 'What is the square root of 16?', 'options': ['2', '3', '4', '5'], 'answer': 2}
            ],
            'Science': [
                {'question': 'What is H2O?', 'options': ['Oxygen', 'Water', 'Hydrogen', 'Carbon'], 'answer': 1},
                {'question': 'How many planets are in our solar system?', 'options': ['7', '8', '9', '10'], 'answer': 1}
            ],
            'History': [
                {'question': 'In which year did World War II end?', 'options': ['1944', '1945', '1946', '1947'], 'answer': 1},
                {'question': 'Who was the first President of the United States?', 'options': ['Thomas Jefferson', 'George Washington', 'Abraham Lincoln', 'John Adams'], 'answer': 1}
            ],
            'English': [
                {'question': 'What is the past tense of "go"?', 'options': ['goed', 'went', 'gone', 'going'], 'answer': 1},
                {'question': 'Which word is a noun?', 'options': ['run', 'quickly', 'house', 'beautiful'], 'answer': 2}
            ],
            'Computer Science': [
                {'question': 'What does CPU stand for?', 'options': ['Central Processing Unit', 'Computer Personal Unit', 'Central Processor Unit', 'Computer Processing Unit'], 'answer': 0},
                {'question': 'Which of these is not a programming language?', 'options': ['Python', 'HTML', 'Java', 'C++'], 'answer': 1}
            ]
        }
        return quizzes.get(subject, [{'question': 'Sample question?', 'options': ['A', 'B', 'C', 'D'], 'answer': 0}])

    def generate_feedback(self, score):
        if score >= 8:
            return "Excellent work! Keep up the great effort!"
        elif score >= 5:
            return "Good job! You're making progress!"
        else:
            return "Keep practicing! You'll improve with time!"

study_pal = StudyPal()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    try:
        data = request.get_json(force=True)
        subject = data.get('subject')
        hours = int(data.get('hours', 2))
        days = int(data.get('days', 7))

        plan = study_pal.generate_study_plan(subject, hours, days)
        tips = [
            "Take short breaks between study sessions.",
            "Revise topics before sleeping for better memory.",
            "Start with difficult topics when your mind is fresh.",
            "Use diagrams or notes to summarize what you learned."
        ]
        return jsonify({'plan': plan, 'tips': tips})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    try:
        data = request.get_json(force=True)
        subject = data.get('subject')
        quiz = study_pal.generate_quiz(subject)
        return jsonify({'quiz': quiz})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_feedback', methods=['POST'])
def get_feedback():
    try:
        data = request.get_json(force=True)
        score = int(data.get('score', 0))
        feedback = study_pal.generate_feedback(score)
        return jsonify({'feedback': feedback})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text', '')

    if not text.strip():
        return jsonify({'summary': 'Please provide some text to summarize.'})

    # Simple summarization logic — extracts first 2 sentences
    sentences = text.split('. ')
    summary = '. '.join(sentences[:2]) + ('.' if not sentences[0].endswith('.') else '')

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)