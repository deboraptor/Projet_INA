from compter_sentiments import machine, gold

import pandas as pd
import tabulate

from sklearn.metrics import classification_report



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

else:
    print("Les listes ne sont pas de même taille.")

