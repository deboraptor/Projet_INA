# Exploration de la perception dans les transcriptions d’émissions de télé et radio (INA)
## Analyse des données sur le Grand Paris
### Données :
Transcriptions automatiques corrigées des émissions radio et télé portant sur le
Grand Paris (xml ou txt).

### Objectif :
* Tester les outils de détection automatique de la subjectivité sur les données.
* Outil : détection de modalité, d’émotions, de sentiments (lexiques
existants, python, etc.).
* Analyser manuellement les résultats (observer à l’œil si les résultats sont
pertinents) et proposer les meilleurs outils.

## Recherche de modules
camemBERT, distilBERT (transformers)

__Module__ : TextBlob

## TO-DO's
- [X] rajouter les locuteurs dans le fichier csv
- [X] traiter le fichier csv pour qu'il soit en fichier txt
- [X] corriger les erreurs des fichiers csv qui se terminent par .eaf.csv
- [ ] faire l'annotation automatique des .txt
- [ ] faire le gold standard
- [ ] faire les mesures de fiabilité du modèle
- [ ] faire l'accord inter-annotateur
- [ ] faire des graphiques "avant/après" 

### Problèmes
Le fichier 4169456.001.006.eaf n'a qu'une seule ligne de dialogue et pose problème lors de la conversion en CSV, le fichier ressort vide. A voir plus tard si c'est possible de le gérer.

## main.sh
Ce script Bash permet de convertir les fichiers .eaf en fichiers .csv en utilisant la librairie *speach*. En parcourant tous les fichiers .eaf présents dans le répertoire spécifié, le script exécute la commande `python3 -m speech eaf2csv` pour chacun d'entre eux. Les fichiers CSV générés sont délimités par des tabulations et des flèches, et ils sont enregistrés dans le même répertoire que les fichiers .eaf d'origine, avec le même nom de base mais une extension .csv.

- [X] inclure les autres scripts dedans pour tout lancer d'un coup

## modifier_csv.py
Ce script permet de supprimer les colonnes dont on a pas besoin. Le script parcours dans le dossier `fichiers_csv` et cherche tous les fichiers dont l'extension est .eaf. Ensuite, il supprime les colonnes inutes à savoir les colonnes 2, 3, 4 et 5. Le séparateur des fichiers CSV est maintenant la virgule.

- [X] à essayer de l'inclure directement dans le fichier bash, quand je l'ai fait je n'avais pas géré les erreurs et ça ne fonctionnait pas.

## csv2txt.py
Ce script permet d'extraire et de nettoyer le contenu textuel présent dans les fichiers CSV, en supprimant les parties indésirables situées à gauche de la virgule ainsi que la virgule elle-même. Le script traite chaque fichier CSV dans un répertoire donné, puis écrit le texte nettoyé dans un fichier texte correspondant. L'objectif principal de ce script est de préparer les données textuelles pour l'annotation automatique ultérieure, en facilitant le processus et en améliorant la qualité des données d'entrée.
## 29/03

J'ai pu trouver deux midèles qui fonctionnent bien, un pour la polarité et un pour les émotions. Mais j'ai également du tester plein de modèles qui be fonctionnaient pas ou qui demandaient des librairies que je n'i pas su utilisée.

##  05/04
pattern.py : ça permet d'obtenir la polarité et la subectivité d'une string. Facile à utiliser ais je n'arrive pas à installer le module pattern.