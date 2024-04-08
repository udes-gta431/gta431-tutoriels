import random
import csv


# Function to generate random missing values
def generate_missing_values():
    return random.random() < 0.15


# Lists of possible values for each column
prenoms = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
noms = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Lee", "Jones", "Clark", "Hall", "Moore"]
villes = ['Quebec', 'Montreal', 'Sherbrooke', 'Trois-Rivieres']

# Create and write to the CSV file
with open('donnees_pratique.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Prenom', 'Nom', 'Ville', 'Age', 'Locataire']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(20):
        prenom = random.choice(prenoms)
        nom = random.choice(noms)
        ville = random.choice(villes)
        age = random.randint(18, 100)
        locataire = random.choice([True, False])

        # Generate missing values
        if generate_missing_values():
            prenom = ""
        if generate_missing_values():
            nom = ""
        if generate_missing_values():
            ville = ""
        if generate_missing_values():
            age = ""
        if generate_missing_values():
            locataire = ""

        writer.writerow(
            {'Prenom': prenom, 'Nom': nom, 'Ville': ville, 'Age': age, 'Locataire': locataire})

print("CSV dataset created successfully.")