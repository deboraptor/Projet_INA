from bs4 import BeautifulSoup as bs
import csv 

with open("../M1/11870482.001.eaf", "r") as file:
    soup = bs(file, features="xml")

    # Je récupère les id des participants dans tier
    tier = soup.find_all('TIER')
    participant_liste = []
    for balise in tier:
        participant = balise.get('TIER_ID')
        if participant == "*PRE":
            participant_liste.append('Présentateur')        
        else:
            if participant == None:
                participant_liste.append('Inconnu')
            else:
                participant_liste.append(participant)
    print(participant_liste)
    alignable_annotation = soup.find_all('ALIGNABLE_ANNOTATION')
    annotation_value_liste = []
    for balise in alignable_annotation:
        time_slot_ref1 = balise.get('TIME_SLOT_REF1')
        annotation_value = balise.find('ANNOTATION_VALUE')

        # Je récupère dans la balise annotation_value la valeur de time_slot_ref1
        # Je la met dans un dictionnaire dans l'ordre d'apparition
        if time_slot_ref1 and annotation_value:
            annotation_value_liste.append((time_slot_ref1, annotation_value.text.strip()))

# Et là je trie les balises des annotations par ordre croissant par rapport au time_slot_ref1
sorted_annotation_values = sorted(annotation_value_liste, key=lambda x: x[0])


file = open("resultats.csv", 'w')

# Je fais une liste de compréhension pour que chaque élément soit une colonne pour le format csv
data = [(participant, annotation_value) for time_slot, annotation_value in sorted_annotation_values]

# Il faut maintenant mettre ligne par ligne chaque élément de la liste
objet = csv.writer(file)
for element in data:
    objet.writerow(element)

file.close()