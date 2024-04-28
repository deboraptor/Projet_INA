from textblob import TextBlob

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob("J'aime bien cette pomme", analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)
