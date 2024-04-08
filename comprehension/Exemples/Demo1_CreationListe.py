# Nom du fichier : Demo1_CreationListe
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Céer une liste simple de carrés.


## Sans la compréhension de liste
if __name__ == "__main__":
    # Liste de carrés
    squares = []
    # Créer la liste à l'aide d'une boucle
    for nombre in range(10):
        squares.append(nombre * nombre)
    # Afficher la liste
    print(squares)

# Résultat: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## Avec la compréhension de liste:
if __name__ == "__main__":
    # Créer la liste à l'aide de la syntaxe de compréhension de liste
    squares = [nombre * nombre for nombre in range(10)]
    # Afficher la liste
    print(squares)

# Résultat: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
