from bs4 import BeautifulSoup as bs
import csv
import glob
import os

dossier_fichiers = glob.glob("../M1/*.eaf")
for fichier in dossier_fichiers:
    with open(fichier, "r") as file:
        soup = bs(file, features="xml")

    nom_fichier_csv = os.path.basename(fichier).replace(".eaf", ".csv")

    ## Je récupère les id des participants dans tier
    tier = soup.find_all('TIER')
    participant_liste = []
    participant_dict = {}
    for balise in tier:
        participant = balise.get('TIER_ID')
        time_slot = balise.find('TIME_SLOT')
        if time_slot:
            time_slot_num = int(time_slot.get('TIME_SLOT_ID').split('ts')[-1])
            participant_dict[time_slot_num] = participant
        if participant == "*PRE":
            participant_liste.append('Présentateur')

    ## Les annotations
    alignable_annotation = soup.find_all('ALIGNABLE_ANNOTATION')
    annotation_value_liste = []
    for balise in alignable_annotation:
        time_slot_ref1 = balise.get('TIME_SLOT_REF1')
        annotation_value = balise.find('ANNOTATION_VALUE')

        # Je récupère dans la balise annotation_value la valeur de time_slot_ref1
        # Je la met dans un dictionnaire dans l'ordre d'apparition
        if time_slot_ref1 and annotation_value:
            time_slot_num = int(time_slot_ref1.split('ts')[-1])
            participant = participant_dict.get(time_slot_num, 'Inconnu')
            annotation_value_liste.append((participant, time_slot_ref1, annotation_value.text.strip()))

    # Et là je trie les balises des annotations par ordre croissant par rapport au time_slot_ref1
    sorted_annotation_values = sorted(annotation_value_liste, key=lambda x: int(x[1].split('ts')[-1]))

    # Écrit les annotations avec les noms des locuteurs dans le fichier CSV
    with open(os.path.join('fichiers_csv', nom_fichier_csv), 'w', newline='') as csvfile:
        objet = csv.writer(csvfile)
        for participant, _, annotation_value in sorted_annotation_values:
            objet.writerow([participant, annotation_value])
