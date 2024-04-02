import matplotlib.pyplot as plt
import pandas as pd

def visualize_sales_data(data_frame):
    """
    Visualise les données de ventes en créant un graphique linéaire des ventes au fil du temps.
    
    Args:
        data_frame (pd.DataFrame): Le DataFrame contenant les colonnes 'Date' et 'Sales'.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data_frame['Date'], data_frame['Sales'], marker='o', linestyle='-', color='b')
    plt.title('Évolution des Ventes au Fil du Temps')
    plt.xlabel('Date')
    plt.ylabel('Ventes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    # Supposons que 'clean_sales_data.csv' est le fichier contenant nos données nettoyées
    clean_df = pd.read_csv('clean_sales_data.csv')
    clean_df['Date'] = pd.to_datetime(clean_df['Date'])
    visualize_sales_data(clean_df)
