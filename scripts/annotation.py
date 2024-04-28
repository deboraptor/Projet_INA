import spacy
import glob
import os

fichiers = glob.glob("../data/fichiers_txt/*.txt")
# print("Fichiers :\t", fichiers)

dossier_lemmes = "../data/fichiers_lemmes"
if not os.path.exists(dossier_lemmes):
    os.makedirs(dossier_lemmes)

nlp = spacy.load("fr_core_news_sm")

nombre_fichiers = 0

for fichier in fichiers:
    with open(fichier, "r") as f:
        corpus = f.read()
        doc = nlp(corpus)
        # print("Fichier :\t", fichier)
        # print("Doc:\t", doc)

    lignes = []
    for token in doc:
        lignes.append(token.lemma_)

    fichier_lemme = os.path.basename(fichier).replace('.txt', '_lemmes.txt')
    with open(os.path.join(dossier_lemmes, fichier_lemme), 'w') as lf:
        for lemme in lignes:
            lf.write(lemme + " ")
    nombre_fichiers += 1
    print("Fichier bien créé :", fichier_lemme)

print("Au total ", nombre_fichiers, " fichiers correctement créés.")
