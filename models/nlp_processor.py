import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import re

class NLPProcessor:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
            
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
    
    def extract_keywords(self, text, top_n=5):
        # Tokenize and clean
        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        
        # Get most common words
        word_freq = Counter(tokens)
        return [word for word, freq in word_freq.most_common(top_n)]
    
    def generate_study_tips(self, keywords):
        tips = []
        for keyword in keywords:
            tips.append(f"Review {keyword} concepts daily")
            tips.append(f"Practice {keyword} problems regularly")
        return tips[:3]  # Return top 3 tips
    
    def summarize_text(self, text, max_sentences=2):
        sentences = sent_tokenize(text)
        if len(sentences) <= max_sentences:
            return text
        
        # Simple extractive summarization - return first few sentences
        return ' '.join(sentences[:max_sentences])
    
    def clean_text(self, text):
        # Remove special characters and extra whitespace
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = ' '.join(text.split())
        return text.lower()
