import glob
import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


fichiers = glob.glob("../emotions/output/*_brut.csv")
dossier_sauvegarde = "./output/graphes/zipf"

df_total = pd.concat([pd.read_csv(fichier) for fichier in fichiers])
word_counts_total = df_total['text'].str.split(expand=True).stack().value_counts()

for fichier in fichiers:
    df = pd.read_csv(fichier)
    word_counts = df['text'].str.split(expand=True).stack().value_counts()

    sns.set()
    plt.figure(figsize=(10, 6))
    plt.loglog(word_counts.index, word_counts.values, alpha=.8, color="darkmagenta")
    plt.title('Loi de Zipf')
    plt.xlabel('Rang du mot')
    plt.ylabel('Fréquence du mot')
    # plt.show()

    nom_fichier = os.path.basename(fichier).replace("_output_brut.csv", "_brut_zipf.png")
    chemin_fichier = os.path.join(dossier_sauvegarde, nom_fichier)
    plt.savefig(chemin_fichier)

print("Tous les graphiques ont été enregistrés dans", dossier_sauvegarde)

sns.set()
plt.figure(figsize=(10, 6))
plt.loglog(word_counts_total.index, word_counts_total.values, alpha=.8, color="darkmagenta")
plt.title('Loi de Zipf (total)')
plt.xlabel('Rang du mot')
plt.ylabel('Fréquence du mot')

dossier_sauvegarde_total = "./output/graphes"
nom_fichier_total = "total_brut_zipf.png"
chemin_fichier_total = os.path.join(dossier_sauvegarde_total, nom_fichier_total)
plt.savefig(chemin_fichier_total)

print("Un graphique pour tout les fichiers enregistré dans", dossier_sauvegarde_total)
