from bs4 import BeautifulSoup as bs

with open("../M1/11870482.001.eaf", "r") as f:
    soup = bs(f, features="xml")
    alignable_annotation = soup.find_all('ALIGNABLE_ANNOTATION')
    # print(annotation_value)
    text = ""
    for balise in alignable_annotation:
        annotation_value = balise.find('ANNOTATION_VALUE')
        if annotation_value:
            text += annotation_value.text + "\n"
            with open("resultats.csv", 'w') as file:
                file.write(text)


