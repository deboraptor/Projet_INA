# Projet de fin d'année en enrichissement de corpus 
## Analyse des données sur le Grand Paris
### Données :
Transcriptions automatiques corrigées des émissions radio et télé portant sur le
Grand Paris (xml ou txt)

- Objectif :
Tester les outils de détection automatique de la subjectivité sur les données
Outil : détection de modalité, d’émotions, de sentiments (lexiques
existants, python, etc.)
Analyser manuellement les résultats (observer à l’œil si les résultats sont
pertinents) et proposer les meilleurs outils

## Recherche de modules
camemBERT, distilBERT (transformers)

__Module__ : TextBlob

## Analyse
### A faire absolument 
* analyser la polarité
* faire des graphiques "avant" sur des données brutes
* faire les analyses "après"

### A regarder plus tard
* Regarder quel locuteur est triste ?

## TO-DO's
- [ ] rajouter les locuteurs dans le fichier csv
	- le module `speach` fait ça !! la commande c'est `python -m speach eaf2csv path/to/my_transcript.eaf -o path/to/my_transcript.csv`
	- il faut séparer avec espace et ce caractère →
- [ ] traiter le fichier csv pour qu'il soit en fichier txt

## eaf2csv.sh
Ce script Bash permet de convertir les fichiers .eaf en fichiers .csv en utilisant la librairie *speach*. 
En parcourant tous les fichiers .eaf présents dans le répertoire spécifié, le script exécute la commande 
`python3 -m speech eaf2csv` pour chacun d'entre eux. Les fichiers CSV générés sont délimités par des tabulations 
et des flèches, et ils sont enregistrés dans le même répertoire que les fichiers .eaf d'origine, avec le même 
nom de base mais une extension .csv.
