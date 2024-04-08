# Nom du fichier : Demo0_Exemple
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Exemple d'introduction démontrant comment convertir une liste de noms en liste de courriels.


## Sans la compréhension de liste
if __name__ == "__main__":
    # Liste des noms
    noms = ["Pierre Dufort", "Marie Tremblay", "Pierre Jalbert", "Marianne Lefebvre"]

    # Liste des adresses courriel
    courriels = []

    # Créer les adresses courriel à l'aide d'une boucle
    for nom in noms:
        # Mettre les noms complètement en minuscules
        nom_minuscules = nom.lower()
        # Remplacer les espaces par des points
        nom_point = nom_minuscules.replace(" ", ".")
        # Ajouter le domaine "@usherbrooke.ca" à la fin
        courriel = nom_point + "@usherbrooke.ca"
        # Ajouter l'adresse courriel à la liste
        courriels.append(courriel)

    print(courriels)

# Résultat: ['pierre.dufort@usherbrooke.ca', 'marie.tremblay@usherbrooke.ca', 'pierre.jalbert@usherbrooke.ca', 'marianne.lefebvre@usherbrooke.ca']


## Avec la compréhension de liste:
if __name__ == "__main__":
    # Liste des noms
    noms = ["Pierre Dufort", "Marie Tremblay", "Pierre Jalbert", "Marianne Lefebvre"]

    # Utilisation de la compréhension de liste pour créer une liste d'adresses courriel
    courriels = [nom.lower().replace(" ", ".") + "@usherbrooke.ca" for nom in noms]

    print(courriels)

# Résultat: ['pierre.dufort@usherbrooke.ca', 'marie.tremblay@usherbrooke.ca', 'pierre.jalbert@usherbrooke.ca', 'marianne.lefebvre@usherbrooke.ca']

