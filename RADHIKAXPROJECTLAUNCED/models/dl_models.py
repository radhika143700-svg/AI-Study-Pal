class TextSummarizer:
    def __init__(self):
        pass

    def summarize(self, text):
        # Very basic summarization: just return first 50 words
        words = text.split()[:50]
        summary = ' '.join(words)
        return summary

class FeedbackGenerator:
    def __init__(self):
        self.feedbacks = [
            "Great job! Keep it up!",
            "You're doing well. Stay focused!",
            "Excellent progress. You're on the right track!",
            "Good work! Review the key concepts.",
            "Well done! Practice more for better results."
        ]

    def generate_feedback(self, subject):
        # Simple random feedback
        import random
        feedback = random.choice(self.feedbacks)
        return f"{feedback} on {subject}!"

if __name__ == "__main__":
    summarizer = TextSummarizer()
    text = "Mathematics is the study of numbers, shapes, and patterns. It includes topics like algebra, geometry, and calculus. Algebra deals with equations and variables. Geometry studies shapes and their properties. Calculus involves rates of change and accumulation."
    summary = summarizer.summarize(text)
    print("Summary:", summary)

    generator = FeedbackGenerator()
    feedback = generator.generate_feedback("Math")
    print("Feedback:", feedback)
