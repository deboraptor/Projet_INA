from compter_sentiments import machine, gold

import pandas as pd
import tabulate
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



if len(machine) == len(gold):
    report = classification_report(gold, machine, zero_division=1, output_dict=True)

    precision = report['weighted avg']['precision']
    recall = report['weighted avg']['recall']
    f1_score = report['weighted avg']['f1-score']

    # print("Les listes sont de même taille.")
    # print('Précision :', precision)
    # print('Rappel :', recall)
    # print('F-mesure :', f1_score)

    metrique = [['Précision', str(precision)], ['Rappel', str(recall)], ['F-mesure', str(f1_score)]]
    table = tabulate.tabulate(metrique, headers=['Métrique', 'Valeur'], tablefmt="rounded_outline")
    print(table)

    conf_matrix = confusion_matrix(gold, machine)
    classes = np.unique(np.concatenate((gold, machine)))
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g', xticklabels=classes, yticklabels=classes)

    plt.xlabel('Classe Prédite')
    plt.ylabel('Classe Réelle')
    plt.title('Matrice de Confusion')
    plt.savefig("./output/graphes/matrice_confusion.png")

else:
    print("Les listes ne sont pas de même taille.")

