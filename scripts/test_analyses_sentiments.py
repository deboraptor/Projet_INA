import spacy 

from extraire_eaf import annotation_value_liste


nlp = spacy.load("fr_core_news_sm")

doc = nlp(annotation_value_liste)
print(doc)