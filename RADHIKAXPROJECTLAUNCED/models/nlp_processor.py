import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_keywords(self, text, num_keywords=5):
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word not in self.stop_words and word not in string.punctuation]
        word_freq = nltk.FreqDist(tokens)
        keywords = [word for word, freq in word_freq.most_common(num_keywords)]
        return keywords

    def generate_study_tips(self, keywords):
        tips = []
        for keyword in keywords:
            tips.append(f"Review key terms like '{keyword}' daily.")
        return tips

if __name__ == "__main__":
    processor = NLPProcessor()
    text = "Mathematics is the study of numbers, shapes, and patterns."
    keywords = processor.extract_keywords(text)
    tips = processor.generate_study_tips(keywords)
    print("Keywords:", keywords)
    print("Study Tips:", tips)
