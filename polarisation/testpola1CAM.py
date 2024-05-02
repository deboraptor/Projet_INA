import tensorflow as tf
assert tf.__version__ >= "2.0"
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
import os

# Chargement du modèle
tokenizer = AutoTokenizer.from_pretrained("tblard/tf-allocine", use_fast=True)
model = TFAutoModelForSequenceClassification.from_pretrained("tblard/tf-allocine")

# Initialisation du pipeline NLP
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

def division_analyse (text):
    #tokenisation du texte 
    tokens = tokenizer(text, add_special_tokens=False, return_tensors="pt")['input_ids'][0]
    #on fait une liste de strings de 508 tokens 
    parts = [tokens[i:i + 510 - 2] for i in range(0, len(tokens), 510 - 2)]
    results = []
    for part in parts:
        input_ids = tokenizer.build_inputs_with_special_tokens(part.tolist())
        part_text = tokenizer.decode(input_ids)
        result = nlp(part_text, return_all_scores=True)
        results.append(result)   
    return results

def main() : 
    # Chemin du dossier contenant les fichiers à traiter, 
    chemin = "../data/fichiers_lemmes" ##__CHEMIN À MODIFIER__##
    for fichier in os.listdir(chemin):  
        fichier = os.path.join(chemin, fichier) 
        if os.path.getsize(fichier) == 0: ##verification si un fichier est vide afin de le passer
            print(f"Fichier vide : {fichier}. Pas de label.")
            continue
        with open(fichier, "r") as file : 
            r = file.read()
            result = division_analyse(r)
        print(f"Fichier : {fichier}, Label : {result}")

main()