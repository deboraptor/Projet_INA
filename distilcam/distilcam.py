from transformers import pipeline, AutoTokenizer
import os

tokenizer = AutoTokenizer.from_pretrained("cmarkea/distilcamembert-base-sentiment")

analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer=tokenizer
)


def division_analyse (text):
    #tokenisation du texte 
    tokens = tokenizer(text, add_special_tokens=False, return_tensors="pt")['input_ids'][0]
    
    #on fait une liste de strings de 508 tokens 
    parts = [tokens[i:i + 510 - 2] for i in range(0, len(tokens), 510 - 2)]
    
    results = []
    for part in parts:
        input_ids = tokenizer.build_inputs_with_special_tokens(part.tolist())
        
        part_text = tokenizer.decode(input_ids)
        
        #on fait une liste des outputs de l'analyseur
        result = analyzer(part_text, return_all_scores=True)
        results.append(result)
    
    return results

def main ():
    chemin = "data/fichiers_lemmes/"
    for file in os.listdir(chemin):
        fichier = os.path.join(chemin,file)
        with open (fichier, "r", encoding="utf-8") as f :
            r = f.read()
            #print (r)
            if not r:
                result = "Empty file"
            else :
                result = division_analyse(r)
        
            print (file, result)

main()