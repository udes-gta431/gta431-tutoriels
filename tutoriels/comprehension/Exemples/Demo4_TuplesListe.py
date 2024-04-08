# Nom du fichier : Demo4_TuplesListe
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Effectuer des opérations sur une liste de tuples afin de connaître les produits ayant un prix plus élevé que 5$.


## Sans la compréhension de liste
if __name__ == "__main__":
    # Liste de tuples de produits
    produits = [
        ("Stylo", 2.99),
        ("Cahier", 19.99),
        ("Écouteurs Bluetooth", 55.99),
        ("Ciseaux", 4.99),
        ("Clavier Bluetooth", 79.99)
    ]
    # Nouvelle liste contenant les produits filtrés
    noms_produits = []
    # Création de la nouvelle liste à l'aide d'une boucle
    for produit in produits:
        if produit[1] > 5 :
            noms_produits.append(produit[0])
    # Afficher la liste
    print(noms_produits)

    # Résultat: ['Cahier', 'Écouteurs Bluetooth', 'Clavier Bluetooth']



    ## Avec la compréhension de liste
    if __name__ == "__main__":
        # Liste de tuples de produits
        produits = [
            ("Stylo", 2.99),
            ("Cahier", 19.99),
            ("Écouteurs Bluetooth", 55.99),
            ("Ciseaux", 4.99),
            ("Clavier Bluetooth", 79.99)
        ]
        # Créer la nouvelle liste à l'aide de la syntaxe de compréhension de liste
        noms_produits = [produit[0] for produit in produits if produit[1] > 5]
        # Afficher la liste
        print(noms_produits)

        # Résultat: ['Cahier', 'Écouteurs Bluetooth', 'Clavier Bluetooth']


