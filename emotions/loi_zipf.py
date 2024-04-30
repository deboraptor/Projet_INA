import glob
import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def zipf(chemin_csv, sortie_fichier, sortie_total, type):
    """
    Génère les graphiques de la loi de Zipf pour chaque fichier CSV dans le chemin spécifié,
    ainsi que pour l'ensemble des fichiers.

    Args:
        chemin_csv (str): Le chemin vers les fichiers CSV à traiter.
        sortie_fichier (str): Le chemin vers le dossier où enregistrer les graphiques générés.
        type (str): On choisi fichier traite ou brute.
    """

    fichiers_csv = glob.glob(os.path.join(chemin_csv, "*.csv"))

    df_total = pd.concat([pd.read_csv(fichier) for fichier in fichiers_csv])
    total_mots = df_total['text'].str.split(expand=True).stack().value_counts()

    sns.set()
    plt.figure(figsize=(10, 6))
    plt.loglog(total_mots.index, total_mots.values, alpha=.8, color="darkmagenta")
    plt.title(f'Loi de Zipf {type} (total)')
    plt.xlabel('Rang du mot')
    plt.ylabel('Fréquence du mot')

    total_nom_fichier = f"total_{type}_zipf.png"
    total_nom_chemin = os.path.join(sortie_fichier, total_nom_fichier)
    plt.savefig(total_nom_chemin)
    plt.clf()

    # for fichier in fichiers_csv:
    #     df = pd.read_csv(fichier)
    #     word_counts = df['text'].str.split(expand=True).stack().value_counts()

    #     sns.set()
    #     plt.figure(figsize=(10, 6))
    #     plt.loglog(word_counts.index, word_counts.values, alpha=.8, color="darkmagenta")
    #     plt.title('Loi de Zipf')
    #     plt.xlabel('Rang du mot')
    #     plt.ylabel('Fréquence du mot')

    #     # Enregistrer le graphique de la loi  Zipf pour le fichier actuel
    #     nom_fichier = os.path.basename(fichier).replace(f"_output_{type}.csv", f"_{type}_zipf.png")
    #     nom_chemin = os.path.join(sortie_fichier, nom_fichier)
    #     plt.savefig(nom_chemin)

    # print("Tous les graphiques ont été enregistrés dans", sortie_fichier)
    print(f"Le fichier pour les fichiers {type} a été enregistré dans {sortie_total}.")

zipf("../emotions/output", "./output/graphes/", "./output/graphes", "traite")
zipf("../emotions/output", "./output/graphes/", "./output/graphes", "brut")

