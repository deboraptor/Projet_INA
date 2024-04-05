"""
VADER is best suited for language used in social media, like short sentences with some slang and abbreviations. 
It’s less accurate when rating longer, structured sentences, but it’s often a good launching point.
"""

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores("Wow, NLTK is really powerful!")
{'neg': 0.0, 'neu': 0.295, 'pos': 0.705, 'compound': 0.8012}
