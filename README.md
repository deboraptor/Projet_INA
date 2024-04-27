# Exploration de la perception dans les transcriptions d’émissions de télé et radio (INA)
## Analyse des données sur le Grand Paris
### Données :
Transcriptions automatiques corrigées des émissions radio et télé portant sur le
Grand Paris (xml ou txt).

### Objectif :
* Tester les outils de détection automatique de la subjectivité sur les données.
* Outil : détection de modalité, d’émotions, de sentiments (lexiques
existants, python, etc.).
* Analyser manuellement les résultats (observer à l’œil si les résultats sont
pertinents) et proposer les meilleurs outils.

## Recherche de modules
camemBERT, distilBERT (transformers)
__Module__ : TextBlob

## Analyse
### A faire absolument 
* analyser la polarité
* faire des graphiques "avant" sur des données brutes
* faire les analyses "après"
* Regarder quel locuteur est triste pour faire un lien avec l'objectivité du journalite/présentateur ?

## TO-DO's
- [X] rajouter les locuteurs dans le fichier csv
	- le module `speach` fait ça !!
	- il faut séparer avec espace et ce caractère →
- [X] traiter le fichier csv pour qu'il soit en fichier txt
- [ ] corriger les erreurs des fichiers CSV qui se terminent par .eaf.csv

### Problèmes
Le fichier 4169456.001.006.eaf n'a qu'une seule ligne de dialogue et pose problème lors de la conversion en CSV, le fichier ressort vide. A voir plus tard si c'est possible de le gérer.

## eaf2csv.sh
Ce script Bash permet de convertir les fichiers .eaf en fichiers .csv en utilisant la librairie *speach*. En parcourant tous les fichiers .eaf présents dans le répertoire spécifié, le script exécute la commande `python3 -m speech eaf2csv` pour chacun d'entre eux. Les fichiers CSV générés sont délimités par des tabulations et des flèches, et ils sont enregistrés dans le même répertoire que les fichiers .eaf d'origine, avec le même nom de base mais une extension .csv.

## modifier_csv.py
Après avoir lancé le script bash `eaf2csv.sh`, on lance celui-ci immdiatement pour supprimer les colonnes dont on a pas besoin. Le script parcours dans le dossier `fichiers_csv` et cherche tous les fichiers dont l'extension est .eaf. Ensuite, il supprime les colonnes inutes à savoir les colonnes 2, 3, 4 et 5. Le séparateur des fichiers CSV est maintenant la virgule.

- [ ] à essayer de l'inclure directement dans le fichier bash, quand je l'ai fait j'avais pas géré les erreurs et ça ne fonctionnait pas.

## csv2txt
Ce script permet d'extraire et de nettoyer le contenu textuel présent dans les fichiers CSV, en supprimant les parties indésirables situées à gauche de la virgule ainsi que la virgule elle-même. Le script traite chaque fichier CSV dans un répertoire donné, puis écrit le texte nettoyé dans un fichier texte correspondant. L'objectif principal de ce script est de préparer les données textuelles pour l'annotation automatique ultérieure, en facilitant le processus et en améliorant la qualité des données d'entrée.