import nlu
print(nlu.load("fr.classify.sentiment.bert").predict("""Mignolet vraiment dommage de ne jamais le voir comme titulaire"""))
