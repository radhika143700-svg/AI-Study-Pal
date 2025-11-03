import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import numpy as np

class QuizGenerator:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.classifier = LogisticRegression()
        self.questions = [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4", "difficulty": "easy"},
            {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Madrid"], "answer": "Paris", "difficulty": "easy"},
            {"question": "What is the square root of 16?", "options": ["2", "4", "8", "16"], "answer": "4", "difficulty": "medium"},
            {"question": "Who wrote Romeo and Juliet?", "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"], "answer": "Shakespeare", "difficulty": "medium"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "O2", "N2"], "answer": "H2O", "difficulty": "easy"},
            {"question": "What is photosynthesis?", "options": ["Respiration", "Energy production in plants", "Cell division", "Water cycle"], "answer": "Energy production in plants", "difficulty": "medium"},
            {"question": "What year did World War II end?", "options": ["1945", "1939", "1950", "1960"], "answer": "1945", "difficulty": "medium"},
            {"question": "What is the largest planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter", "difficulty": "easy"},
            {"question": "What is the Pythagorean theorem?", "options": ["a^2 + b^2 = c^2", "E=mc^2", "F=ma", "PV=nRT"], "answer": "a^2 + b^2 = c^2", "difficulty": "medium"},
            {"question": "What is the main function of the heart?", "options": ["Thinking", "Pumping blood", "Digestion", "Breathing"], "answer": "Pumping blood", "difficulty": "easy"}
        ]
        self.train_model()

    def train_model(self):
        # Prepare training data
        texts = [q["question"] for q in self.questions]
        difficulties = [1 if q["difficulty"] == "easy" else 0 for q in self.questions]  # 1 for easy, 0 for medium

        X = self.vectorizer.fit_transform(texts)
        X_train, X_test, y_train, y_test = train_test_split(X, difficulties, test_size=0.2, random_state=42)

        self.classifier.fit(X_train, y_train)

        # Evaluate
        y_pred = self.classifier.predict(X_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        print(f"F1 Score: {f1_score(y_test, y_pred)}")

    def generate_quiz(self, subject, num_questions=5):
        # Filter questions by subject (simplified)
        relevant_questions = [q for q in self.questions if subject.lower() in q["question"].lower() or True]  # For now, use all
        selected_questions = np.random.choice(relevant_questions, min(num_questions, len(relevant_questions)), replace=False)
        return selected_questions.tolist()

class ResourceSuggester:
    def __init__(self):
        self.resources = {
            "math": ["https://www.khanacademy.org/math", "https://www.mathway.com/"],
            "science": ["https://www.nasa.gov/stem", "https://www.sciencemag.org/"],
            "history": ["https://www.history.com/", "https://www.bbc.co.uk/history"],
            "english": ["https://www.pbs.org/wnet/poetry/", "https://www.grammarly.com/"]
        }

    def suggest_resources(self, subject):
        return self.resources.get(subject.lower(), ["https://www.google.com/search?q=" + subject])

if __name__ == "__main__":
    quiz_gen = QuizGenerator()
    quiz = quiz_gen.generate_quiz("Math", 3)
    print("Generated Quiz:", quiz)

    suggester = ResourceSuggester()
    resources = suggester.suggest_resources("Math")
    print("Suggested Resources:", resources)
