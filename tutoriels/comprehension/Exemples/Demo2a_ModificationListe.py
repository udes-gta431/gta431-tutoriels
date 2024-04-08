# Nom du fichier : Demo2_ModificationListe
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Modifier une liste de clients afin d'ajouter des majuscules à chaque première lettre.

## Sans la compréhension de liste
if __name__ == "__main__":
    # Liste des noms des clients tous en minuscules
    clients = ["natalie tremblay", "william bouchard", "elizabeth fortin", "lilianne gagnon", "thomas turcotte", "antoine savard"]
    # Nouvelle liste de clients
    client_liste = []
    # Création de la nouvelle liste à l'aide d'une boucle
    for client in clients:
        nom_majuscule = client.title()
        client_liste.append(nom_majuscule)
    # Afficher la liste
    print(client_liste)

    # Résultat: ['Natalie Tremblay', 'William Bouchard', 'Elizabeth Fortin', 'Lilianne Gagnon', 'Thomas Turcotte', 'Antoine Savard']



## Avec la compréhension de liste
if __name__ == "__main__":
    # Liste des noms des clients tous en minuscules
    clients = ["natalie tremblay", "william bouchard", "elizabeth fortin", "lilianne gagnon", "thomas turcotte",
               "antoine savard"]
    # Créer la liste à l'aide de la syntaxe de compréhension de liste
    client_liste = [client.title() for client in clients]
    # Afficher la liste
    print(client_liste)

    # Résultat: ['Natalie Tremblay', 'William Bouchard', 'Elizabeth Fortin', 'Lilianne Gagnon', 'Thomas Turcotte', 'Antoine Savard']


