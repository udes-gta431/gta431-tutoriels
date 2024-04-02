import requests
    
def fetch_data(source_url):
    response = requests.get(source_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des données : {response.status_code}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    data_url = "https://www.data.gouv.fr/"
    data = fetch_data(data_url)
    print(data[:5])  # Imprime les 5 premiers éléments pour vérifier
