# Nom du fichier : Demo5_ListeImbriquee
# Auteur : daphne.lauziere@usherbrooke.ca
# Date de création : 20240211
# Description : Démonstration de compréhension de listes imbriquées en calculant le nombre d'employés dans chaque département.


## Sans la compréhension de liste
if __name__ == "__main__":
    # Liste des départements
    departements = ["Finances", "Marketing", "IT"]

    # Liste des employés et leur département
    employes = [
        ("Pierre Dupont", "Finances"),
        ("Marie Lajoie", "IT"),
        ("Jaccques Tremblay", "Finances"),
        ("Sophie Lemieux", "Marketing"),
        ("Philippe Charbonneau", "Marketing"),
        ("Julie Dubois", "IT"),
        ("Stéphanie Bergeron", "Marketing"),
        ("Patrick Gagnon", "Marketing"),
        ("Nadine Roy", "Finances")
    ]

    # Initialiser la liste
    nombre_employes_departement = []

    # Parcourir chaque département
    for departement in departements:
    # Initialiser le compteur d'employés
        count = 0
        # Parcourir chaque employé
        for employe in employes:
            # Vérifier si l'employé travaille dans le département
            if employe[1] == departement:
                # Incrémenter le compteur d'employés
                count += 1
        # Ajouter le nombre d'employés pour ce département à la nouvelle liste
        nombre_employes_departement.append((departement, count))

    # Afficher le nombre d'employés par département
    for departement, count in nombre_employes_departement:
        print(f"Il y a {count} employé(s) dans le département de {departement}.")

        # Résultat: Il y a 3 employé(s) dans le département de Finances.
        #           Il y a 4 employé(s) dans le département de Marketing.
        #           Il y a 2 employé(s) dans le département de IT.


## Avec la compréhension de liste
    if __name__ == "__main__":
        departements = ["Finances", "Marketing", "IT"]

        # Liste des employés et leur département
        employes = [
            ("Pierre Dupont", "Finances"),
            ("Marie Lajoie", "IT"),
            ("Jaccques Tremblay", "Finances"),
            ("Sophie Lemieux", "Marketing"),
            ("Philippe Charbonneau", "Marketing"),
            ("Julie Dubois", "IT"),
            ("Stéphanie Bergeron", "Marketing"),
            ("Patrick Gagnon", "Marketing"),
            ("Nadine Roy", "Finances")
        ]

        # Création d'une nouvelle liste contenant le nombre d'employés par département, à l'aide d'une liste de compréhension imbriquée
        nombre_employes_departement = [(departement, sum(1 for employe in employes if employe[1] == departement)) for departement in
                                     departements]

        # Afficher la liste nombre_employes_departement
        print(nombre_employes_departement)

        # Résultat: [('Finances', 3), ('Marketing', 4), ('IT', 2)]
        # Ce résultat peut être mélangeant, il est donc mieux de l'afficher d'une façon différente

        # Afficher le nombre d'employés par département
        for departement, count in nombre_employes_departement:
            print(f"Il y a {count} employé(s) dans le département de {departement}.")

        # Résultat: Il y a 3 employé(s) dans le département de Finances.
        #           Il y a 4 employé(s) dans le département de Marketing.
        #           Il y a 2 employé(s) dans le département de IT.