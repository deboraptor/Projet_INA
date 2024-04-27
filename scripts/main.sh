#!/bin/bash

chemin="../data/fichiers_csv"

for eaf in ../../M1/*.eaf;
do
  base="$(basename "$eaf" .eaf)"
  python3 -m speach eaf2csv "$eaf" -o "${chemin}/${base}.csv"
done

python3 modifier_csv.py
python3 csv2txt.py