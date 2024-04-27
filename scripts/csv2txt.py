import glob

fichiers = glob.glob("../data/fichiers_csv/*.csv")

succes = 0
erreur = 0

for fichier in fichiers:
    try:
        csv2txt = fichier.replace("../data/fichiers_csv/", "../data/fichiers_txt/").replace(".csv", ".txt")
        with open(fichier, 'r') as csv:
            lignes = csv.readlines()
            with open(csv2txt, "w") as txt:
                for ligne in lignes:
                    if ',' in ligne:
                        partie_droite = ligne.split(',', 1)[1].strip()
                        txt.write(partie_droite + '\n')
        succes += 1
    except Exception as e:
        erreur += 1
        print(f"Erreur lors de la conversion '{fichier}': {str(e)}")

print(f"\n{succes} fichiers convertis avec succès.")
if erreur > 0:
    print(f"{erreur} fichiers n'ont pas été convertis à cause d'une erreur.")
