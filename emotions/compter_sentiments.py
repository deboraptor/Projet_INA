from tabulate import tabulate

import pandas as pd
import matplotlib.pyplot as plt

import glob
import collections
import os


fichiers = glob.glob("./output/*traite.csv")
fichiers_gold = glob.glob("./output/gold_standard/*.csv")

sortie_fichier = "./output/graphes/"
sortie_fichier_total = "./output"

tableau = []
fichier_numero = 0

gold = []
machine = []

sentiment_couleurs = {
    "sadness": "skyblue",
    "love": "gold",
    "anger": "lightcoral",
    "joy": "plum",
    "surprise": "mediumaquamarine",
    "fear": "wheat"
}

for fichier in fichiers:
    fichier_numero += 1
    df = pd.read_csv(fichier)
    labels = df["label"].tolist()
    # print(fichier, labels)

    sentiment_counts = collections.Counter(labels)
    # print(sentiment_counts)

    nom_fichier_diagramme = os.path.basename(fichier).replace(f"_output_traite.csv", f"_repartition.png")
    nom_chemin_diagramme = os.path.join(sortie_fichier, nom_fichier_diagramme)
    # nom = os.path.basename(fichier).replace("output_*_repartition.*", "")

    sentiments = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())

    couleurs = [sentiment_couleurs[sentiment] for sentiment in sentiments]

    ########################
    # Diagramme circulaire #
    ########################

    plt.pie(counts, labels=sentiments, colors=couleurs, autopct='%1.1f%%')
    # plt.title(f"Répartition des sentiments : {nom}")
    plt.title(f"Répartition des sentiments :")
    # plt.show()

    plt.savefig(nom_chemin_diagramme)
    plt.clf()

    ######################
    # Diagramme à barres #
    ######################

    bars = plt.bar(sentiments, counts)
    for i, bar in enumerate(bars):
        bar.set_color(couleurs[i])
    plt.title('Nombre d\'occurrences des sentiments')
    plt.xlabel('Sentiments')
    plt.ylabel('Nombre d\'occurrences')
    # plt.show()

    nom_fichier_barre = os.path.basename(fichier).replace(f"_output_traite.csv", f"_barre.png")
    nom_chemin_barre = os.path.join(sortie_fichier, nom_fichier_barre)

    plt.savefig(nom_chemin_barre)
    plt.clf()

    ########################################
    # Données gold pour chaque fichier #
    ########################################

    sentiment_dominant = sentiment_counts.most_common(1)
    # print(f"Sentiment dominant du fichier {fichier} : {sentiment_dominant[0][0]} ({sentiment_dominant[0][1]} occurrences)")

    for sentiment in sentiment_dominant:
        gold.append(sentiment[0])
    

    tableau.append([f"Fichier {fichier_numero} : {os.path.basename(fichier).replace('_output_traite.csv', '')}", sentiment_dominant[0][0], sentiment_dominant[0][1]])

tableau.insert(0, ["Fichier", "Sentiment dominant", "Nombre d'occurrences"])
print(tabulate(tableau, headers="firstrow", tablefmt="rounded_outline"))

####################################
# Données gold pour chaque fichier #
####################################

for fichier in fichiers_gold:
    read = pd.read_csv(fichier)
    df = pd.DataFrame(read)
    label_liste = df['label'].tolist()
    case1 = label_liste[0]
    case1_liste = [case1]
    machine.append(case1)

