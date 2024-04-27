import glob

fichiers = glob.glob("../data/fichiers_csv/*.csv")

for fichier in fichiers:
    csv2txt = fichier.replace("../data/fichiers_csv/", "../data/fichiers_txt/").replace(".csv", ".txt")
    with open(fichier, 'r') as csv:
        lignes = csv.readlines()
        with open(csv2txt, "w") as txt:
            for ligne in lignes:
                if ',' in ligne:
                    partie_droite = ligne.split(',', 1)[1].strip()
                    txt.write(partie_droite + '\n')
