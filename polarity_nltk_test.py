"""
VADER is best suited for language used in social media, like short sentences with some slang and abbreviations. 
It’s less accurate when rating longer, structured sentences, but it’s often a good launching point.
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

exemple = "nul !"
sia = SentimentIntensityAnalyzer()

sentiment_score = sia.polarity_scores(exemple)
print(exemple)
print(sentiment_score)