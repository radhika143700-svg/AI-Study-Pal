from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

class StudyPal:
    def __init__(self):
        self.subjects = ['Math', 'Science', 'History', 'English', 'Computer Science']
        
    def generate_study_plan(self, subject, hours_per_day, days):
        plan = []
        topics = {
            'Math': ['Algebra', 'Geometry', 'Calculus', 'Statistics', 'Trigonometry'],
            'Science': ['Physics', 'Chemistry', 'Biology', 'Earth Science', 'Astronomy'],
            'History': ['Ancient History', 'Modern History', 'World Wars', 'Civilizations', 'Renaissance'],
            'English': ['Grammar', 'Literature', 'Writing', 'Reading Comprehension', 'Poetry'],
            'Computer Science': ['Programming', 'Data Structures', 'Algorithms', 'Databases', 'Web Development']
        }
        
        subject_topics = topics.get(subject, ['Topic 1', 'Topic 2', 'Topic 3', 'Topic 4'])
        
        for day in range(days):
            topic = subject_topics[day % len(subject_topics)]
            plan.append({
                'day': day + 1,
                'topic': topic,
                'hours': hours_per_day,
                'tasks': f'Study {topic} for {hours_per_day} hours',
                'date': (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
            })
        
        return plan
    
    def generate_quiz(self, subject):
        quizzes = {
            'Math': [
                {'question': 'What is 2 + 2?', 'options': ['3', '4', '5', '6'], 'answer': 1},
                {'question': 'What is the square root of 16?', 'options': ['2', '3', '4', '5'], 'answer': 2},
                {'question': 'What is 5 × 7?', 'options': ['30', '35', '40', '45'], 'answer': 1}
            ],
            'Science': [
                {'question': 'What is H2O?', 'options': ['Oxygen', 'Water', 'Hydrogen', 'Carbon'], 'answer': 1},
                {'question': 'How many planets are in our solar system?', 'options': ['7', '8', '9', '10'], 'answer': 1},
                {'question': 'What gas do plants absorb from the atmosphere?', 'options': ['Oxygen', 'Nitrogen', 'Carbon Dioxide', 'Hydrogen'], 'answer': 2}
            ],
            'History': [
                {'question': 'When did World War II end?', 'options': ['1944', '1945', '1946', '1947'], 'answer': 1},
                {'question': 'Who was the first President of the United States?', 'options': ['John Adams', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'], 'answer': 2}
            ],
            'English': [
                {'question': 'What is a noun?', 'options': ['Action word', 'Describing word', 'Person, place, or thing', 'Connecting word'], 'answer': 2},
                {'question': 'Who wrote Romeo and Juliet?', 'options': ['Charles Dickens', 'William Shakespeare', 'Jane Austen', 'Mark Twain'], 'answer': 1}
            ]
        }
        return quizzes.get(subject, [{'question': 'Sample question?', 'options': ['A', 'B', 'C', 'D'], 'answer': 0}])
    
    def generate_feedback(self, score):
        if score >= 80:
            messages = ["Excellent work! Keep up the great effort!", "Outstanding performance! You're doing amazing!", "Fantastic job! Your hard work is paying off!"]
        elif score >= 60:
            messages = ["Good job! You're making progress!", "Nice work! Keep practicing!", "Well done! You're on the right track!"]
        else:
            messages = ["Keep practicing! You'll improve with time!", "Don't give up! Every expert was once a beginner!", "Great effort! Practice makes perfect!"]
        
        return random.choice(messages)
    
    def get_study_tips(self, subject):
        tips = {
            'Math': ['Practice problems daily', 'Review formulas regularly', 'Work through examples step by step'],
            'Science': ['Conduct experiments when possible', 'Create concept maps', 'Read scientific articles'],
            'History': ['Create timelines', 'Use mnemonics for dates', 'Connect events to causes and effects'],
            'English': ['Read diverse literature', 'Practice writing daily', 'Expand your vocabulary'],
            'Computer Science': ['Code every day', 'Build projects', 'Debug systematically']
        }
        return tips.get(subject, ['Study regularly', 'Take breaks', 'Ask questions'])

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
    tips = study_pal.get_study_tips(subject)
    
    return jsonify({'plan': plan, 'tips': tips})

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

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text', '')
    
    # Simple summarization - take first 2 sentences
    sentences = text.split('.')
    summary = '. '.join(sentences[:2]) + '.' if len(sentences) > 2 else text
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    print("🎓 AI Study Pal is starting...")
    print("📚 Access the application at: http://localhost:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)
