from pattern.fr import sentiment

text = "j'aime boen cette pomme"
polarity, subjectivity = sentiment(text)

print (f"Polarité:{polarity}, Subjectivité :{subjectivity}")