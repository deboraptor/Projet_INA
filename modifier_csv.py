import pandas as pd
import glob
import os


fichiers = glob.glob("./data/fichiers_extraits_/*.csv") 

for fichier in fichiers:
    df = pd.read_csv(fichier, sep="\t")
    # print("DEBUT", df.columns.values)
    df = df.drop(df.columns[[1, 2, 3, 4]], axis=1)
    # print("RESULTAT", df.columns.values)
    base = os.path.splitext(fichier)[0]
    df.to_csv(f"{base}.csv", index=False, header=False)
