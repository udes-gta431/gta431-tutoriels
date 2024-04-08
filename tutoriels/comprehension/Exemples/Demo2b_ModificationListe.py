# Nom du fichier : Demo2_ModificationListe
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Modifier une liste de clients afin d'ajouter les taxes à une liste de prix.

## Sans la compréhension de liste
if __name__ == "__main__":
    prix_finaux = []
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15

    for prix in liste_prix:
        prix_final = prix * (1 + taxes)
        prix_finaux.append(prix_final)
    print(prix_finaux)

    # Résultat: [3.4385, 22.988499999999995, 64.3885, 5.1635, 91.98849999999999]



## Avec la compréhension de liste
if __name__ == "__main__":
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15

    prix_finaux = [prix * (1 + taxes) for prix in liste_prix]
    print(prix_finaux)


