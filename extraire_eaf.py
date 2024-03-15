from bs4 import BeautifulSoup as bs

with open("../M1/11870482.001.eaf", "r") as f:
    soup = bs(f, features="xml")
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

with open("resultats.csv", 'w') as file:
    for time_slot, annotation_value in sorted_annotation_values:
        file.write(annotation_value + "\n")
