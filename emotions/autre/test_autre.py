import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import os


def load_data(fichier_chemin):
    """ Fonction pour charger et préparer les données à partir d'un fichier CSV donné """
    
    df = pd.read_csv(fichier_chemin)
    return df


def predict_emotions(df):
    """ Fonction pour entraîner le modèle XGBoost et prédire les émotions pour un DataFrame donné """
    
    X_train, X_test, y_train, y_test = train_test_split(df['1'], df['2'], test_size=0.2, random_state=42)
    vectorizer = CountVectorizer(max_features=5000, stop_words='french')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    xgb_model = xgb.XGBClassifier(objective='multi:softmax', num_class=6, random_state=42)
    xgb_model.fit(X_train_vec, y_train)
    y_pred = xgb_model.predict(X_test_vec)
    return y_pred


def dominant_emotion(predictions):
    """ Fonction pour calculer l'émotion dominante pour une liste de prédictions donnée """
    
    emotions = np.bincount(predictions)
    index_emotion_dominante = np.argmax(emotions)
    return index_emotion_dominante

dossier_csv = "../data/fichiers_csv"
dossier_output = "../emotions/output/"

for fichier in os.listdir(dossier_csv):
    if fichier.endswith('.csv'):
        fichier_chemin = os.path.join(dossier_csv, fichier)
        df = load_data(fichier_chemin)
        predictions = predict_emotions(df)
        index_emotion_dominante = dominant_emotion(predictions)
        base_fichiername, ext = os.path.splitext(fichier)
        output_fichiername = base_fichiername + '_output.csv'
        output_fichier = os.path.join(dossier_output, output_fichiername)
        with open(output_fichier, 'w') as out_f:
            out_f.write(f'{fichier},{index_emotion_dominante}\n')
