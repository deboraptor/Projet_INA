import pandas as pd
import glob
import os

fichiers = glob.glob("./data/fichiers_csv_/*.csv")

succes = 0
erreur = 0

for fichier in fichiers:
    try:
        df = pd.read_csv(fichier, sep="\t")
        df = df.drop(df.columns[[1, 2, 3, 4]], axis=1)
        base = os.path.splitext(fichier)[0]
        df.to_csv(f"{base}.csv", index=False, header=False)
        succes += 1
    except Exception as e:
        erreur += 1
        print(f"Erreur lors de l'actualisation du fichier CSV '{fichier}': {str(e)}")

print(f"\n{succes} fichiers actualisés avec succès.")
if erreur > 0:
    print(f"{erreur} fichiers n'ont pas été actualisés à cause d'une erreur.")
