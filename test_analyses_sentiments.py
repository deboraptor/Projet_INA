import spacy 

from extraire_eaf import annotation_values_liste


nlp = spacy.load("fr_core_news_sm")

doc = nlp(annotation_values_liste)
print(doc)