# Importation des librairies
import pandas as pd
from bs4 import BeautifulSoup as Bs
import urllib.request
import time
import csv

# Définir la variable url qui va contenir l'url de la page à scrapper
url = "https://www.amazon.ca/-/fr/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers"

# Ajout d'en-têtes pour simuler une requête venant d'un navigateur web afin d'éviter d'être bloqué
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

req = urllib.request.Request(url, headers=headers)

# Tentative de récupération de la page sans surcharger le serveur
max_attempts = 5
for attempt in range(max_attempts):
    try:
        page = urllib.request.urlopen(req).read()
        break  # Si la requête réussit, sortir de la boucle
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"Erreur HTTP 429: Trop de requêtes. Tentative {attempt+1}/{max_attempts}.")
            time.sleep(10)  # Attendre 10 secondes avant de réessayer
        else:
            raise  # Renvoyer l'exception si ce n'est pas une erreur 429

# Charger le code de la page avec BeautifulSoup
soup = Bs(page, 'html.parser')

# Extraction des noms de produits à partir des balises div avec la classe spécifiée
products_divs = soup.find_all('div', {'class': 'p13n-sc-truncate-desktop-type2'})
price_divs = soup.find_all('span', {'class': '_cDEzb_p13n-sc-price_3mJ9Z'})

# Initialisation de la liste pour stocker les noms de produits
products = []
prices = []

# Boucle pour traiter chaque balise div contenant un nom de produit
for div in products_divs:
    # Extraire le texte du produit et nettoyer les espaces
    product_name = div.text.strip()
    # Ajouter le nom du produit à la liste
    products.append(product_name)

# Boucle pour traiter chaque balise div contenant un prix de produit
for div in price_divs:
    # Extraire le texte du prix et nettoyer les espaces
    price_name = div.text.strip()
    # Ajouter le prix à la liste
    prices.append(price_name)

# Écrire les données dans un fichier CSV
with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for product, price in zip(products, prices):
        writer.writerow({'Product': product, 'Price': price})

print("Les données ont été stockées dans amazon_products.csv avec succès.")