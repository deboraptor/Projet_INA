import pandas as pd
import glob
import os


fichiers = glob.glob("./fichiers_extraits/*.csv") 

for fichier in fichiers:
    pd_fichier = pd.read_csv(fichier)
    colonnes = [1, 2, 3, 4]
    pd_fichier.drop(columns=colonnes, inplace=True)
    base = os.path.splitext(fichier)[0]
    pd_fichier.to_csv(f"{base}.csv", index=False, header=False)
