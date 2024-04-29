import csv
import glob
import os

from transformers import pipeline


def traiter_fichier(fichier, analyzer, dossier_output):
    """ Traite un fichier CSV et écrit le résultat dans un fichier de sortie. """
    try:
        with open(fichier, 'r') as fichier_entree:
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
            print("Fichier bien créé :", fichier_output_brut)
    except FileNotFoundError:
        print("Erreur : le fichier n'existe pas.")
    except csv.Error as e:
        print(f"Erreur : {e}")

def compter_fichiers(fichiers, analyzer, dossier_output):
    """ Traite tous les fichiers CSV dans le répertoire spécifié. """
    nombre_fichiers = 0
    for fichier in fichiers:
        traiter_fichier(fichier, analyzer, dossier_output)
        nombre_fichiers += 1
    print("Succès !", nombre_fichiers, "ont été traités correctement.")

def main():
    fichiers = glob.glob("../data/fichiers_csv/*.csv")
    dossier_output = "../emotions/output"
    analyzer = pipeline(
        task='text-classification',
        model='botdevringring/fr-naxai-ai-emotion-classification-081808122023',
        tokenizer='botdevringring/fr-naxai-ai-emotion-classification-081808122023'
    )
    compter_fichiers(fichiers, analyzer, dossier_output)

if __name__ == "__main__":
    main()
