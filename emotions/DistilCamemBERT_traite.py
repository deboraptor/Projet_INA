import csv
import glob
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from transformers import pipeline

# Télécharger les données nécessaires pour NLTK
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def traiter_texte(texte):
    """ Effectue la lemmatization et enlève les stop words du texte. """
    mots = word_tokenize(texte)
    lemmatizer = WordNetLemmatizer()
    mots_lemmatises = [lemmatizer.lemmatize(mot) for mot in mots]
    stop_words = set(stopwords.words('french'))
    mots_filtres = [mot for mot in mots_lemmatises if mot.lower() not in stop_words]
    texte_traite = ' '.join(mots_filtres)
    return texte_traite

def traiter_fichier(fichier, analyzer, dossier_output):
    """ Traite un fichier CSV et écrit le résultat dans un fichier de sortie. """
    try:
        with open(fichier, 'r') as fichier_entree:
            lecteur_csv = csv.reader(fichier_entree)
            dialect = csv.Sniffer().sniff(fichier_entree.readline())
            fichier_entree.seek(0)
            lecteur_csv = csv.reader(fichier_entree, dialect)
            if csv.Sniffer().has_header(fichier_entree.readline()):
                next(lecteur_csv)
            fichier_output_traite = os.path.basename(fichier).replace('.csv', '_output_traite.csv')
            with open(os.path.join(dossier_output, fichier_output_traite), 'w', newline='') as fichier_sortie:
                ecrivain_csv = csv.writer(fichier_sortie)
                ecrivain_csv.writerow(["speaker", "text", "label"])
                for ligne in lecteur_csv:
                    texte_brut = ligne[1]
                    texte_traite = traiter_texte(texte_brut)
                    result = analyzer(texte_traite)
                    label = result[0]['label']
                    ecrivain_csv.writerow([ligne[0], texte_traite, label])
            print("Fichier bien créé :", fichier_output_traite)
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
