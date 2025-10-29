from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
import numpy as np

class QuizGenerator:
    def __init__(self):
        self.vectorizer = CountVectorizer(max_features=100)
        self.classifier = LogisticRegression()
        self.clusterer = KMeans(n_clusters=3)
        
    def train_difficulty_classifier(self, texts, difficulties):
        X = self.vectorizer.fit_transform(texts)
        X_train, X_test, y_train, y_test = train_test_split(X, difficulties, test_size=0.2)
        
        self.classifier.fit(X_train, y_train)
        
        y_pred = self.classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        return {'accuracy': accuracy, 'f1_score': f1}
    
    def predict_difficulty(self, text):
        X = self.vectorizer.transform([text])
        return self.classifier.predict(X)[0]
    
    def cluster_topics(self, texts):
        X = self.vectorizer.fit_transform(texts)
        clusters = self.clusterer.fit_predict(X)
        return clusters

class ResourceSuggester:
    def __init__(self):
        self.resources = {
            'Math': ['Khan Academy Math', 'Wolfram Alpha', 'MIT OpenCourseWare'],
            'Science': ['NASA Education', 'National Geographic', 'Coursera Science'],
            'History': ['History.com', 'BBC History', 'Smithsonian'],
            'English': ['Grammarly', 'Purdue OWL', 'Literature Online']
        }
    
    def get_resources(self, subject):
        return self.resources.get(subject, ['General Study Resources'])
