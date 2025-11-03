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
        
    def generate_study_plan(self, subject, hours_per_day, days):
        plan = []
        topics = {
            'Math': ['Algebra', 'Geometry', 'Calculus', 'Statistics'],
            'Science': ['Physics', 'Chemistry', 'Biology', 'Earth Science'],
            'History': ['Ancient History', 'Modern History', 'World Wars', 'Civilizations'],
            'English': ['Grammar', 'Literature', 'Writing', 'Reading Comprehension'],
            'Computer Science': ['Programming', 'Data Structures', 'Algorithms', 'Databases']
        }
        
        subject_topics = topics.get(subject, ['Topic 1', 'Topic 2', 'Topic 3', 'Topic 4'])
        
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
            ]
        }
        return quizzes.get(subject, [{'question': 'Sample question?', 'options': ['A', 'B', 'C', 'D'], 'answer': 0}])
    
    def generate_feedback(self, score):
        if score >= 80:
            return "Excellent work! Keep up the great effort!"
        elif score >= 60:
            return "Good job! You're making progress!"
        else:
            return "Keep practicing! You'll improve with time!"

study_pal = StudyPal()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    data = request.json
    subject = data.get('subject')
    hours = int(data.get('hours', 2))
    days = int(data.get('days', 7))
    
    plan = study_pal.generate_study_plan(subject, hours, days)
    return jsonify({'plan': plan})

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.json
    subject = data.get('subject')    
    quiz = study_pal.generate_quiz(subject)
    return jsonify({'quiz': quiz})

@app.route('/get_feedback', methods=['POST'])
def get_feedback():
    data = request.json
    score = int(data.get('score', 0))
    feedback = study_pal.generate_feedback(score)
    return jsonify({'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)  