from textblob import TextBlob

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob("J'aime bien cette ppomme", analyzer=NaiveBayesAnalyzer())

blob.sentiment