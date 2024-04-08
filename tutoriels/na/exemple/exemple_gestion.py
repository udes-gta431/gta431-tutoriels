import csv
import pandas as pd
import numpy as np

chemin_cible ="../exemple/data_set/donnees_pratique.csv"

# Creation du DataFrame
with open(chemin_cible, 'r') as fh:
    df = pd.read_csv(fh)
    print(f"DataFrame avant l'utilisation des méthode:\n{df}")

    # Suppression des lignes avec des valeurs manquantes - méthode dropna()
    df_modifier = df.dropna()
    print(f"\nDataFrame après l'utilisation de la méthode dropna():\n{df_modifier}")

    # Imputation - Méthode fillna
    ## Imputation par la median fillna(df.median())
    ### Seulement la colonne 'Age' peut être utiliser puisqu'elle est constituée de floats
    df_modifier = df
    df_modifier['Age'] = df_modifier['Age'].fillna(df_modifier['Age'].median())
    print(f"\nDataFrame après l'utilisation de la méthode fillna(df.median()): Median = {df_modifier['Age'].median()} \n{df_modifier}")

    ## Imputation par des valeurs personnalisées - méthode fillna()
    df_modifier['Ville'] = df_modifier['Ville'].fillna('Inconnue')
    print(f"\nDataFrame après l'utilisation de la méthode fillna() pour changer une donnee manquante par Inconnue:\n{df_modifier}")

    ## Imputation de Prenom par la valeur suivante - méthode bfill()
    df_modifier['Prenom'] =df_modifier['Prenom'].bfill()
    print(f"\nDataFrame après l'utilisation de la méthode bfill():\n{df_modifier}")

    ## Imputation Nom par la valeur precedante - méthode ffill()
    df_modifier['Nom'] = df_modifier['Nom'].ffill()
    print(f"\nDataFrame après l'utilisation de la méthode ffill():\n{df_modifier}")