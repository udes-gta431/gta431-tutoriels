# Tutoriel sur la manipulation des données en Python : Tri, accès et manipulation de dictionnaires

## Introduction
Dans le domaine de l'analyse des données, la manipulation efficace des structures de données est essentielle. Les dictionnaires sont l'une des structures de données les plus utilisées en Python pour stocker et manipuler des données. Un dictionnaire est une collection non ordonnée, mutable et indexée d'éléments. Chaque élément est représenté par une paire clé-valeur, où chaque clé est unique et associée à une valeur spécifique. Cette structure de données flexible et puissante permet de représenter efficacement une grande variété d'informations, ce qui en fait un outil indispensable pour les professionnels des données et les analystes.

Dans ce tutoriel, nous explorerons différentes façons de trier un dictionnaire par valeur et par clé, ainsi que d'accéder à la liste des clés et des valeurs. Nous présenterons des exemples concrets issus du domaine des affaires pour illustrer chaque concept. Que vous soyez un analyste de données chevronné ou un étudiant en administration des affaires souhaitant perfectionner ses compétences en manipulation de données, ce tutoriel vous fournira les connaissances nécessaires pour tirer pleinement parti des dictionnaires en Python dans un contexte professionnel.

## Contexte
Imaginons que vous travaillez dans une entreprise de commerce électronique et que vous avez besoin d'analyser les données des ventes. Vous disposez d'un ensemble de données stocké dans un dictionnaire Python, mais vous devez le trier pour une analyse plus approfondie.

## Public cible
Le tutoriel s'adresse à un public varié, incluant les professionnels des données et les analystes des données, mais cible spécifiquement les étudiants en administration des affaires souhaitant améliorer ses compétences en manipulation de données pour les affaires.


### Dictionnaire
Considérons un exemple de dictionnaire représentant les ventes mensuelles de différents produits :
```python
    ventes = {'janvier': 1500,'février': 2200,'mars': 1800,'avril': 2500,'mai': 2000 }
```
Dans un dictionnaire, il y a des clés et des valeurs associés à celle ci, les clés peuvent être soit des mots ou des nombres.

Dans notre cas:
- clés = mois
- valeurs = ventes

 ### Trier par fonction sorted
Si on utlise seulement le fonction `sorted()`, python va seulement comprendre que nous voulons trier les clés sans les valeurs associer vu que les clés sont les élémentes par défaut du dictionnaire.
Donc, si nous prenons la formule suivante:

```python
        print(sorted(ventes))
 ```
 Nous allons avoir comme résultat seulement une liste des clés triés:

```python
    ['avril', 'février', 'janvier', 'mai', 'mars']
```
 ### Extraire les valeurs
Si nous voulons voir les valeurs en plus des clés dans notre résultat, nous devons les extraires en tant qu'items
Donc, si nous prenons la formule suivante:

```python
        print(ventes.items())
 ```
Nous allons avoir comme résultat notre dictionnaire en format tuple:

```python
    dict_items([('janvier', 1500), ('février', 2200), ('mars', 1800), ('avril', 2500), ('mai', 2000)])
```
Ceci est dû au fait que `ventes.items()` renvoie un objet de type `dict_items`, qui est essentiellement une vue sur les paires (clé, valeur) du dictionnaire. Il est important de noter que cette méthode renvoie un **itérable**, un objet capable de retourner ses éléments un par un. Cela signifie que vous pouvez parcourir les éléments de cet objet à l'aide d'une boucle et accéder à chaque élément séquentiellement..
### Tri par clé
Donc pour trier le dictionnaire par clé (c'est-à-dire par mois), nous n'avons même pas besoin de spécifier le paramètre key, car c'est le comportement par défaut de la fonction `sorted()` et nous avons juste à extraire les valeurs avec ce que nous venons de voir :

```python
    ventes_triées = sorted(ventes.items())
        print(ventes_triées)
 ```
Par contre si nous voulons avoir notre résultat nous devons le convertir en mettant un `dict` en avant de notre fonction:

```python
    ventes_triées = dict(sorted(ventes.items()))
        print(ventes_triées)
 ```    
Cela produira :
```python
    {'avril': 2500, 'février': 2200, 'janvier': 1500, 'mai': 2000, 'mars': 1800}
 ```
Note: Le système python va par défaut trier en ordre croissant et de A à Z, mais si non voulons changer l'ordre de croissant à décroissant et de Z à A nous pouvons seulement rajouter `reverse=True` à la fonction:
 ```  
ventes_triées_reverse = dict(sorted(ventes.items(), reverse=True))
print(ventes_triées_reverse)
 ```  
  ### Tri par valeur 
Pour trier ce dictionnaire par valeur (c'est-à-dire par montant de ventes), nous pouvons utiliser la fonction `sorted()` avec le paramètre `key` pour spécifier que nous voulons trier par valeur.

Nous allons prendre la fonction lambda pour simplifier les choses, le lambda est une fonction anonyme en Python. Il est souvent utilisé comme argument pour les fonctions qui attendent une fonction en paramètre, comme dans notre cas avec la fonction `sorted()` :

```python
    sorted(ventes.items(), key=lambda)
```
Il faudra rajouter la partie du code qui trie les éléments du dictionnaire ventes en utilisant la fonction `sorted()`. Le paramètre `key` spécifie une fonction de comparaison qui est utilisée pour extraire une clé de chaque élément de `ventes.items()` afin de les comparer et de les trier en conséquence. 

Donc nous rajoutons :

```python
    (sorted(ventes.items(), key=lambda item: item[1]))
```

 Le lambda est utilisé comme fonction de comparaison et définit une fonction qui prend un élément (ici, une paire clé-valeur) comme argument et retourne `item[1]`, c'est-à-dire la valeur associée à cette paire clé-valeur. 
 
 Ainsi, la fonction de comparaison va comparer les valeurs des paires clé-valeur du dictionnaire ventes et pour avoir notre dictionnaire nous devons seulement rajouter de nouveau:

```python
    ventes_triées = dict(sorted(ventes.items(), key=lambda item: item[1]))
        print(ventes_triées)
```

      
Cela produira :
```python
    {'janvier': 1500, 'mars': 1800, 'mai': 2000, 'février': 2200, 'avril': 2500}
```
 
### Accès à la liste des clés et des valeurs
Pour accéder à la liste des clés et des valeurs du dictionnaire, nous utilisons les méthodes `keys()` et `values()` respectivement :
```python
    clés = ventes.keys()
    valeurs = ventes.values()
        print("Clés :", clés)
        print("Valeurs :", valeurs)
```
     
Cela produira :
```python
    Clés : dict_keys(['janvier', 'février', 'mars', 'avril', 'mai'])
    Valeurs : dict_values([1500, 2200, 1800, 2500, 2000])
```

## Bonnes pratiques et astuces
-Utilisez la fonction `sorted(`) pour trier un dictionnaire par valeur ou par clé.
-Utilisez les méthodes `keys()` et `values()` pour accéder aux clés et aux valeurs d'un dictionnaire.

## Répétabilité du contenu
En suivant ce tutoriel, vous devriez être en mesure de comprendre comment trier un dictionnaire par valeur ou par clé, ainsi que d'accéder à la liste des clés et des valeurs. Ces compétences sont fondamentales dans le domaine de l'analyse des données et peuvent être appliquées à diverses situations commerciales.

## Transfert des connaissances
Les concepts présentés dans ce tutoriel peuvent être appliqués à de nombreuses autres situations commerciales impliquant la manipulation de données. Par exemple, vous pourriez utiliser ces techniques pour analyser les performances des produits, suivre les tendances de vente ou générer des rapports financiers.

## Limites du tutoriel et prochaines étapes
Ce tutoriel a couvert les bases du tri et de l'accès aux dictionnaires en Python, mais il existe de nombreuses autres fonctionnalités et techniques avancées à explorer. Pour aller plus loin, vous pourriez vous intéresser à la manipulation de dictionnaires imbriqués, à l'utilisation de fonctions de rappel pour le tri personnalisé, ou à l'optimisation des performances pour les grands ensembles de données.

## Conclusion
Dans ce tutoriel, nous avons exploré différentes façons de trier un dictionnaire par valeur et par clé, ainsi que d'accéder à la liste des clés et des valeurs. Nous avons présenté des exemples concrets issus du domaine des affaires pour illustrer chaque concept. En suivant ce tutoriel, vous avez acquis des compétences précieuses en manipulation de données en Python, qui vous seront utiles dans de nombreuses situations commerciales. Ces compétences sont indispensables pour analyser et interpréter les données, prendre des décisions éclairées et optimiser les performances de votre entreprise.

J'espère que ce tutoriel vous a été utile et vous souhaite beaucoup de succès dans votre parcours d'apprentissage de l'analyse des données en Python!



