from transformers import pipeline

analyzer = pipeline(
    task='text-classification',
    model='botdevringring/fr-naxai-ai-emotion-classification-081808122023',
    tokenizer='botdevringring/fr-naxai-ai-emotion-classification-081808122023'
)
result = analyzer(
    "Le film traine un peu en longueur, mais l'ensemble j'ai bien aimé."
)

print(result)
