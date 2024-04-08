# Nom du fichier : Demo3_FiltrerListe
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Filtrer une liste de prix pour avoir seulement les prix plus élevés que 5$.


## Sans la compréhension de liste
if __name__ == "__main__":
    # Listes originales
    prix_finaux = []
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15
    # Création de la nouvelle liste à l'aide d'une boucle
    for prix in liste_prix:
        prix_final = prix * (1 + taxes)
        if prix > 5:
            prix_finaux.append(prix_final)
    # Afficher la nouvelle liste
    print(prix_finaux)

    # Résultat: [22.988499999999995, 64.3885, 91.98849999999999]

## Avec la compréhension de liste :
if __name__ == "__main__":
    # Listes originales
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15
    # Créer la nouvelle liste à l'aide de la syntaxe de compréhension de liste
    prix_finaux = [prix * (1 + taxes) for prix in liste_prix if prix > 5]
    # Afficher la nouvelle liste
    print(prix_finaux)

    # Résultat: [22.988499999999995, 64.3885, 91.98849999999999]

