from transformers import pipeline

analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)
result = analyzer(
    "Ce produit ne me plait pas du tout.",
    return_all_scores=True
)
print (result)