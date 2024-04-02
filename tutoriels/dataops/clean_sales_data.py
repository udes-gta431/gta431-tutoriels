import pandas as pd

def clean_sales_data(data_frame):
    """
    Nettoie un DataFrame de données de ventes en supprimant les lignes avec des valeurs manquantes
    et en convertissant les valeurs de ventes de chaînes de caractères en nombres flottants.
    
    Args:
        data_frame (pd.DataFrame): Le DataFrame contenant les données de ventes brutes.

    Returns:
        pd.DataFrame: Le DataFrame nettoyé.
    """
    cleaned_df = data_frame.dropna()
    cleaned_df['Sales'] = cleaned_df['Sales'].str.replace('$', '').astype(float)
    return cleaned_df

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger les données depuis un fichier CSV (exemple fictif)
    df = pd.read_csv('sales_data.csv')
    clean_df = clean_sales_data(df)
    print(clean_df)
