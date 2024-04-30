from transformers import pipeline, AutoTokenizer
import os

tokenizer = AutoTokenizer.from_pretrained("cmarkea/distilcamembert-base-sentiment")

analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer=tokenizer
)


def division_analyse (text):
    tokens = tokenizer(text, add_special_tokens=False, return_tensors="pt")['input_ids'][0]
    
    # Split tokens into chunks respecting the max_length
    parts = [tokens[i:i + 510 - 2] for i in range(0, len(tokens), 510 - 2)]
    
    results = []
    for part in parts:
        # Add special tokens
        input_ids = tokenizer.build_inputs_with_special_tokens(part.tolist())
        
        # Convert back to text (for demonstration; not necessarily needed for processing)
        part_text = tokenizer.decode(input_ids)
        
        # Analyze the text part
        result = analyzer(part_text, return_all_scores=True)
        results.append(result)
    
    return results


chemin = "data/fichiers_lemmes/"
for file in os.listdir(chemin):
    fichier = os.path.join(chemin,file)
    with open (fichier, "r", encoding="utf-8") as f :
        r = f.read()
        print (r)
        if not r:
            result = "Empty file"
        else :
            result = division_analyse(r)
        
        print (file, result)