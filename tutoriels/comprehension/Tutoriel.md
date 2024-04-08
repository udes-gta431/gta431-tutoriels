# La compréhension de liste (_list comprehension_)

## Contexte
La création et la génération de rapports pour la prise de décision éclairée sont des activités clés dans le domaine de l’administration. Les notions de transformation, filtrage et validation des données sont utilisées afin de réaliser ces activités. Dans le but d’accomplir ces tâches, l’extraction de données peut être simplifiée grâce au concept de compréhension de liste. En effet, cela comporte plusieurs avantages, dont une écriture plus concise du code. Cette situation en milieu de travail est seulement un exemple parmi tant d’autres, car cette notion sur les listes peut être également utilisée dans plusieurs autres contextes.

Pour illustrer cela, voici un exemple dans lequel nous voulons transformer une liste de noms en liste de courriels. Toutefois, cela peut nécessiter un code long comme ceci:

````Python
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
````

Alors qu'il pourrait être raccourci de cette manière en utilisation la _list comprehension_:

````python
if __name__ == "__main__":
    # Liste des noms
    noms = ["Pierre Dufort", "Marie Tremblay", "Pierre Jalbert", "Marianne Lefebvre"]

    # Utilisation de la compréhension de liste pour créer une liste d'adresses courriel
    courriels = [nom.lower().replace(" ", ".") + "@usherbrooke.ca" for nom in noms]

    print(courriels)

# Résultat: ['pierre.dufort@usherbrooke.ca', 'marie.tremblay@usherbrooke.ca', 'pierre.jalbert@usherbrooke.ca', 'marianne.lefebvre@usherbrooke.ca']
````

Ces deux méthodes donnent le même résultat, mais une des deux est beaucoup plus concise et facile à lire, en étant traduite en une seule ligne de code.

L’__objectif__ de ce tutoriel est alors de définir l’utilisation des compréhensions de listes, à l'aide d'exemples et de cas d'utilisation progressant en difficulté, afin de comprendre comment s’en servir et de pouvoir éventuellement accomplir des tâches d'extraction de données de manière plus efficace.

Il est recommandé d’avoir des __connaissances préalables__ sur les opérateurs, les listes, les itérations et l’utilisation de conditions dans Python avant de procéder à la lecture de ce tutoriel. Ces concepts sont utilisés dans la syntaxe et dans l'élaboration des listes en compréhension.

__Ce tutoriel contient :__
-	Une définition du concept de compréhension de liste
-	Pourquoi l’utiliser?
-	Comment l’utiliser?
-	Les limites de cette technique
-	Les prochaines étapes d’apprentissage

## Définition
La compréhension de liste, ou _list comprehension_, est une manière d’élaborer ou de transformer une liste de façon très concise, en une seule ligne de code, dont les éléments résultent d’une opération s’appliquant à chaque valeur d’une autre séquence. Le résultat obtenu est une nouvelle liste contenant les éléments modifiés et satisfaisant les critères demandés.

## Pourquoi l’utiliser?
-	Optimiser le code
-	Augmenter la productivité du programmeur
-	Avoir une plus grande rapidité d’écriture et d’élaboration de scripts Python
-	Concevoir des scripts ayant une maintenance plus simple
-	Construire du code plus concis et lisible 

## Comment l’utiliser? 
### La syntaxe
La syntaxe est simple à maîtriser si les concepts de boucles et de structures de contôle ont déjà été assimilés antérieurement, car elle contient le vocabulaire _for_ et _in_ entouré de quelques éléments essentiels.

````python
nouvelle_liste = [<expression> for <item> in <iterable>]
````
Il faut donc placer entre crochets les éléments suivants :
-	__L’expression__ : L’opération voulant être appliquée sur les éléments de la liste
-	__L’item__ : Élément de la liste
-	__L’itérable__ : Dans ce cas-ci, c’est la liste dans laquelle on prend les items
-	Une condition (optionnel)

## Cas d'utilisation
### 1. Création de liste
Une fonctionnalité de base des listes en compréhension est la création d'une nouvelle liste. L'itérable peut être une liste déjà existante ou provenir d'une fonction, comme _range()_.

Un exemple simple pour représenter cela est la possibilité de créer une liste de carrés facilement.

__Sans__ la compréhension de liste :

````python
if __name__ == "__main__":
    # Liste de carrés
    squares = []
    # Créer la liste à l'aide d'une boucle
    for nombre in range(10):
        squares.append(nombre * nombre)
    # Afficher la liste
    print(squares)

# Résultat: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
````

__Avec__ la compréhension de liste:

````python
if __name__ == "__main__":
    # Créer la liste à l'aide de la syntaxe de compréhension de liste
    squares = [nombre * nombre for nombre in range(10)]
    # Afficher la liste
    print(squares)

# Résultat: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
````

### 2. Modification de liste
Parfois, certaines listes existantes ne sont pas dans le format désiré et nécessitent des modifications sur chaque élément.

Par exemple, si les noms de la liste des clients de la compagnie sont tous en minuscules, il est possible de modifier la liste efficacement pour mettre des majuscules.

__Sans__ la compréhension de liste :
````python
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
````


__Avec__ la compréhension de liste:
````python
if __name__ == "__main__":
    # Liste des noms des clients tous en minuscules
    clients = ["natalie tremblay", "william bouchard", "elizabeth fortin", "lilianne gagnon", "thomas turcotte",
               "antoine savard"]
    # Créer la liste à l'aide de la syntaxe de compréhension de liste
    client_liste = [client.title() for client in clients] 
    # Afficher la liste
    print(client_liste)

    # Résultat: ['Natalie Tremblay', 'William Bouchard', 'Elizabeth Fortin', 'Lilianne Gagnon', 'Thomas Turcotte', 'Antoine Savard']
````

La modification de liste peut se faire également avec des __valeurs numériques__. Par exemple, s’il faut ajouter les taxes à une liste de prix.

__Sans__ la compréhension de liste :
````python
if __name__ == "__main__":
    prix_finaux = []
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15

    for prix in liste_prix:
        prix_final = prix * (1 + taxes)
        prix_finaux.append(prix_final)
    print(prix_finaux)

    # Résultat: [3.4385, 22.988499999999995, 64.3885, 5.1635, 91.98849999999999]
````

__Avec__ la compréhension de liste :
````python
if __name__ == "__main__":
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15

    prix_finaux = [prix * (1 + taxes) for prix in liste_prix]
    print(prix_finaux)
````

### 3. Filtrer une liste
Il est également possible de filtrer une liste en ajoutant une opération conditionnelle après l’itérable. La fonction _if_ est ajoutée à la syntaxe.
````python
nouvelle_liste = [<expression> for <item> in <iterable> if <condition>]
````

En reprenant l’exemple appliquant les taxes sur une liste de prix, ajoutons une condition afin d’avoir les prix ayant un prix sans taxes plus élevé que 5$. 

__Sans__ la compréhension de liste :
````python
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
````

__Avec__ la compréhension de liste :
````python
if __name__ == "__main__":
    # Listes originales
    liste_prix = [2.99, 19.99, 55.99, 4.49, 79.99]
    taxes = .15
    # Créer la nouvelle liste à l'aide de la syntaxe de compréhension de liste
    prix_finaux = [prix * (1 + taxes) for prix in liste_prix if prix > 5]
    # Afficher la nouvelle liste
    print(prix_finaux)

    # Résultat: [22.988499999999995, 64.3885, 91.98849999999999]
````
### 4. Liste de tuples
Cette technique fonctionne également avec des listes de tuples dans lesquelles plusieurs informations sont stockées. Nous pouvons créer une nouvelle liste en utilisant une liste de tuples comme itérable.

Par exemple, dans le cas où nous aimerions connaître les produits ayant un prix plus élevé que 5$.

__Sans__ la compréhension de liste :
````python
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
````

__Avec__ la compréhension de liste :
````python
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
````

### 5. Listes de compréhension imbriquées

Plusieurs listes de compréhensions peuvent être utilisées en même temps pour créer une liste de compréhension imbriquée. Il s'agit donc d'imbriquer plusieurs listes de compréhensions ensembles sur la même ligne de code. 

Ci-dessous se trouve un exemple dans lequel nous voulons compter le nombre d'employés par départment à l'aide d'une liste de départements et d'une liste de tuples des employées avec leur département.


__Sans__ la compréhension de liste :
````python
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

````
__Avec__ la compréhension de liste :
````python
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
````

__Dans tous ces exemples, il est possible d’observer que le code est beaucoup plus concis. En effet, ce qui prend une seule ligne à l’aide de la compréhension de liste peut nécessiter plus de 3 lignes en utilisant une autre technique de programmation.__


## Limites
La compréhension de liste comprend beaucoup d’avantages, notamment la facilité de lecture du code. Cependant, elle n’est pas toujours le meilleur choix pour toutes les circonstances. En effet, cette fonctionnalité peut également avoir le résultat contraire, c’est-à-dire un code moins efficace et plus difficile à lire, car certains programmeurs l’utilisent trop et ont du mal à exploiter les fonctionnalités plus avancées. 

Aussi, il faut faire attention aux listes de compréhension imbriquées qui peuvent devenir mélangeantes si elles donnent un résultat de matrice aplatie. Si l'on reprend le résultat du dernier exercice sur le nombre d'employés par département, celui-ci pourrait devenir difficile à lire s'il retourne beaucoup de résultats dans la liste et qu'il reste sous cette forme: [('Finances', 3), ('Marketing', 4), ('IT', 2)].

La taille de l’échantillon peut également poser problème lorsque celui-ci est trop grand. Effectivement, lorsque la liste à créer consomme trop de mémoire, l’ordinateur peut devenir non réactif et ainsi ralentir ou planter. Dans ce contexte de structure de données volumineuses, il est mieux d’utiliser un générateur. 

Il est donc important de comprendre dans quel contexte utiliser la compréhension de liste et connaître ses limites. 

## Prochaines étapes d’apprentissage
Après avoir pratiqué et maîtrisé la compréhension de liste, voici certaines fonctionnalités plus avancées pouvant être étudiées : 
-	Les compréhensions de liste en allant chercher les données dans un fichier ou une base de données
-	Les dictionnaires de compréhension 
-	Les générateurs
-	Les décorateurs

## Conclusion
L'avantage principal de la compréhension de liste est l'élaboration de code efficace, ce qui est un atout à ne pas négliger lors de la résolution de problème ou l'extraction de données pour l'analyse et la création de tableaux de bord, par exemple. 
Effectivement, cela permet de mieux comprendre le code créé et de se retrouver plus facilement dans son projet. 
Il est possible de créer, modifier et filtrer des listes grâce à une syntaxe concise et facile à interpréter. 
De plus, la compréhension de liste peut s'étendre sur des cas d'utilisation plus complexes que ceux présentés dans ce tutoriel, notamment en allant chercher des données dans un autre fichier.


## Bibliographie
_Les compréhensions de liste python_, Python Doctor, [https: // python.doctor / page - comprehension - list - listes - python - cours - debutants](URL) (consulté le 11-02-2024).

_Listes en compréhension_, Python Software Foundation, [https://docs.python.org/fr/3.12/tutorial/datastructures.html#list-comprehensions](URL) (consulté le 11-02-2024).

Priya C, Bala. _Compréhension de liste en Python - avec des exemples_, Geekflare, [https://geekflare.com/fr/list-comprehension-in-python/](URL)  (consulté le 11-02-2024).

_Python – List Compréhension_, GeeksforGeeks, [https://www.geeksforgeeks.org/python-list-comprehension/](URL)  (consulté le 11-02-2024).

_Python - List Comprehension_, w3schools, [https://www.w3schools.com/python/python_lists_comprehension.asp](URL)  (consulté le 11-02-2024).

Timmins, James. _When to Use a List Comprehension in Python_, Real Python, [https://realpython.com/list-comprehension-python/](URL)  (consulté le 11-02-2024).

### Utilisation de l'IA
L'intelligence artificielle générative a été utilisée dans la conception de ce tutoriel afin de bâtir certains scripts python donnés en exemple. En utilisant ChatGPT, l'objectif était de bien concevoir le code avec et sans la compréhension de liste dans le but d'avoir la meilleur comparaison possible entre les deux techniques. Pour obtenir la réponse souhaitée, les informations suivantes ont été mentionnées: le type de cas d'utilisation voulu, les variables voulant être utilisées et le contexte de l'exemple. Cependant, le code généré n'était pas toujours ce qui était souhaité et nécessitait alors des modifications ou plus de précisions.