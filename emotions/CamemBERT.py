import csv
import glob
import os
from transformers import pipeline

fichiers = glob.glob("../data/fichiers_csv/*.csv")
dossier_output = "../emotions/output"

nombre_fichiers = 0

analyzer = pipeline(
    task='text-classification',
    model='botdevringring/fr-naxai-ai-emotion-classification-081808122023',
    tokenizer='botdevringring/fr-naxai-ai-emotion-classification-081808122023'
)

for fichier in fichiers:
    with open(fichier, 'r') as fichier_entree:
        # Compter le nombre de lignes dans le fichier
        nombre_lignes = sum(1 for ligne in fichier_entree)

        # Ignorer les fichiers qui ont moins de 3 lignes
        if nombre_lignes < 3:
            
            print("Le fichier", fichier, "a moins de 3 lignes. On l'ignore.", flush=True)
            continue

        # Réinitialiser le pointeur du fichier pour le lire à nouveau
        fichier_entree.seek(0)

        lecteur_csv = csv.reader(fichier_entree)
        dialect = csv.Sniffer().sniff(fichier_entree.readline())
        fichier_entree.seek(0)
        lecteur_csv = csv.reader(fichier_entree, dialect)

        # Pour gérer l'erreur Stop Iteration, on vérifie s'il y a un en-tête
        if csv.Sniffer().has_header(fichier_entree.readline()):
            next(lecteur_csv)

        fichier_output_brut = os.path.basename(fichier).replace('.csv', '_output_brut.csv')
        with open(os.path.join(dossier_output, fichier_output_brut), 'w', newline='') as fichier_sortie:
            ecrivain_csv = csv.writer(fichier_sortie)
            ecrivain_csv.writerow(["speaker", "text", "label"])
            for ligne in lecteur_csv:
                texte_brut = ligne[1]
                result = analyzer(texte_brut)
                label = result[0]['label']
                ecrivain_csv.writerow([ligne[0], ligne[1], label])
        nombre_fichiers += 1
        print("Fichier bien créé :", fichier_output_brut)

print("Au total", nombre_fichiers, "fichiers correctement créés.")
