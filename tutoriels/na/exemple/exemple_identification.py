import csv
import pandas as pd
import numpy as np

chemin_cible ="../exemple/data_set/donnees_pratique.csv"

# Creation du DataFrame
with open(chemin_cible, 'r') as fh:
    df = pd.read_csv(fh)

    # Utiliser isna() pour identifier les données manquantes
    donnees_manquantes = df.isna()
    print(f"Tableau Output de la methode isna() :\n{donnees_manquantes}")

    # Utiliser isna().sum() pour identifier le nombre de données manquantes pour chaque colonne
    donnees_manquantes =df.isna().sum()
    print(f"\nOutput de la methode isna().sum() :\nLe nombre total de données manquantes par colonne est :\n{donnees_manquantes}")

    # Utiliser isna().sum().sum() pour identifier le nombre de données manquantes totales
    donnees_manquantes = df.isna().sum().sum()
    print(f"\nOutput de la methode isna().sum().sum() : \nLe nombre total de données manquantes est : {donnees_manquantes}")

    # Utiliser info() pour obtenir un résumé des données manquantes
    print(f"\nTableau Output de la methode info() :")
    print(df.info())

    # Utiliser describe() pour obtenir des statistiques récapitulatives par colonne
    donnees_manquantes = df['Prenom'].describe()
    print(f"\nTableau Output de la methode describe() pour Prenom:\n{donnees_manquantes}")
    donnees_manquantes = df['Nom'].describe()
    print(f"\nTableau Output de la methode describe() pour Nom:\n{donnees_manquantes}")
    donnees_manquantes = df['Ville'].describe()
    print(f"\nTableau Output de la methode describe() pour Ville:\n{donnees_manquantes}")
    donnees_manquantes = df['Age'].describe()
    print(f"\nTableau Output de la methode describe() pour Age:\n{donnees_manquantes}")
    donnees_manquantes = df['Locataire'].describe()
    print(f"\nTableau Output de la methode describe() pour Locataire:\n{donnees_manquantes}")