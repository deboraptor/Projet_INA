from sklearn.metrics import precision_score, recall_score, f1_score

# Exemple d'étiquettes réelles et de prédictions
y_true = [5, 2, 4, 3, 2, 3, 1, 1, 1, 3, 3, 2]
y_pred = [3, 5, 3, 3, 3, 4, 1, 1, 1, 4, 3, 2]

precision = precision_score(y_true, y_pred, average='macro')  # 'macro' pour ne pas tenir compte du déséquilibre de classe
print("Précision: {:.2f}".format(precision))

recall = recall_score(y_true, y_pred, average='macro')
print("Rappel: {:.2f}".format(recall))

f1 = f1_score(y_true, y_pred, average='macro')
print("Score F1: {:.2f}".format(f1))