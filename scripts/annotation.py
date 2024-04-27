import spacy
import glob

fichiers = glob.glob("../data/fichiers_txt/*.txt")
print("Fichiers :\t", fichiers)

for fichier in fichiers:
    with open(fichier) as f:
        nlp = spacy.load("fr_core_news_sm")
        corpus = f.read()
        doc = nlp(corpus)
        print("Doc :\t", doc)

    lignes = []
    for token in doc:
        lignes.append([token.lemma_])
    print("Lignes :\t", lignes)