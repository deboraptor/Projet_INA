#!bin/bash

chemin="../Projet_INA/fichiers_extraits"

for eaf in ../M1/*.eaf; 
do
  base="${eaf%.*}"
  base="${eaf##*/}"
  python3 -m speach eaf2csv "$eaf" -o "${chemin}/${base}.csv"
done