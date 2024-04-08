# **Qu'est-ce qu'une fonction lambda : pourquoi et comment l'utiliser ?**


## **Introduction:**

Avec le langage Python, les programmeurs sont constamment à la recherche de façon de rendre leurs codes plus concis, 
simple et efficace. Une fonctionnalité très intéressante et souvent méconnues des utilisateurs débutants sur Python est 
la fonction lambda. Lambda est une fonction anonyme, ce qui veut dire qu’elle n’est pas définie avec un nom habituel à 
l’aide du mot-clé `def`. Elle est donc créer avec le mot-clé `lambda`. Cette fonctionnalité permet de définir des fonctions 
simplement et rapidement sans la nécessité de créer une fonction formelle. Nous allons tout d'abord décomposer la synthaxe
générale de la fonction lambda et par la suite démontrer des exemples de son utilisation.



## **Intermède :** 

Avant de commencer les explications, expliquons la différence entre le mot-clé `def` et `lambda` adin d'éviter toute 
confusion de leur utilisation. 

1. La nomination:
Avec `def`, notre fonction aura un nom spécifique alors qu'avec `lambda` la fonction n'a pas de nom (anonyme)

2. Corps de la fonction:
Le corps de la fonction `lambda` va être généralement plus simple puisqu'il est limité à une seule expression. Avec `def`
on va pourvoir utiliser plusieurs expressions (donner plusieurs instructions). La fonction pourra donc être plus complexe.

3. La clarté:
Comme mentionné précédemment, `lambda` va être utilisé pour les fonctions plus simple. `Def` va nous être utile pour des 
fonctions plus complètes et répétable dans le texte. Il va être plus facile de revenir par la suite et de comprendre ces 
fonctions. Un code plus gros et avec plus d'instructions sera plus lisible avec `Def`.



## **Synthaxe :**

### La synthaxe de la fonction lambda peut être définie comme suit :

_lambda arguments : expression_

* Le mot-clé `lambda` est utilisé pour indiquer que nous définissions une fonction lambda.
* Nous avons ensuite `arguments`, qui représente le/les paramètres de la fonction. Ils peuvent représenter une multitude 
de choses (ex: variable, liste, un mot-clé, paramètres conditionnels, etc).
* Pour finir, nous avons `expression` qui est le corps de la fonction lambda. C'est l'expression (l'instruction) qui est
exécutée lorsque la fonction est appelée. Cette expression est évaluée et le résultat est renvoyé. Par exemple, il
s'agir : d'une multiplication scalaire, une addition, un filtrage de liste, une vérification de parité, etc.



### Voici un exemple simple et concret de l'utilisation de la fonction lambda : 

`addition = lambda x, y: x + y`

Dans cet exemple, `lambda x, y`: définit une fonction lambda prenant deux arguments, `x` et `y`, et`x + y` est
l'expression qui sera évaluée et renvoyée lorsque la fonction est appelée avec des valeurs spécifiques pour `x et y`.
Donc en ayant des nombres spécifique pour `x` et `y`, la fonction nous ferait l'addition.



## **Contexte d'utilisation:**

La fonction lambda est souvent utilisée dans des situations où une petite fonction est nécessaire pour une opération 
ponctuelle. Voici quelques contextes courants où la fonction lambda est particulièrement utile :



#### **Exemple #1**

Les fonctions lambda sont souvent utilisées avec des fonctions intégrées telles que `map()`,`filter()`, et `sorted()`.
Par exemple, ici, nous allons appliquer une opération simple à chaque élément d'une liste. Nous allons utiliser la fonction 
`map()` avec une fonction lambda.

`nombres = [1, 2, 3, 4, 5]`

`nombre_pairs = map(lambda x: x**2, nombres)`

Dans l’exemple on utilise une fonction lambda avec `map()` pour appliquer rapidement une opération à chaque élément 
d'une liste et obtenir une nouvelle liste résultante. C'est un moyen efficace et concis d'effectuer des transformations
sur des données de manière itérative.



#### **Exemple #2**

Tri personnalisé: Lors du tri d'objets complexes, vous pouvez utiliser la fonction lambda pour spécifier une clé de tri 
personnalisée. Nous allons utilisé la fonction `sorted()` avec lambda.

`etudiants = [('Philippe', 27), ('Roger', 15), ('Anna', 33)]`

`tri_etudiants = sorted(etudiants, key=lambda x: x[1])`

Dans cet exemple-ci, on utilise la fonction lambda comme clé de tri personnalisée avec la fonction `sorted()` pour trier 
une liste d'objets complexes selon un critère spécifique (dans le cas présent l’âge). On peut donc voir la facilité et 
la simplicité de traitement de données grâce à la fonction.



#### **Exemple #3**

Filtrage de données: Vous pouvez utiliser la fonction lambda avec `filter()` pour filtrer des éléments d'une séquence 
en fonction d'un critère spécifique.

`nombre = [1, 2, 3, 4, 5]`

`nombre_pairs = filter(lambda x: x % 2 == 0, nombre)`

J'ai repris mon exemple avec une liste de nombre. Ici, on utilise la fonction lambda avec `filter()` pour filtrer 
rapidement les éléments d'une liste en fonction d'un critère spécifique, ce qui permet de créer une nouvelle liste 
contenant uniquement les éléments souhaités. La fonction de lambda dans l’exercice est de prendre un seul argument x 
(un nombre de la liste) et de retourner `True`si le nombre est pair (c'est-à-dire si le reste de la division par 2 est 
égal à zéro), sinon elle retourne `False` et le nombre sera exclu. 



#### **Exemple #4**

Expressions de listes et de dictionnaires: Les fonctions lambda sont souvent utilisées pour créer des expressions de 
listes ou de dictionnaires de manière concise.

`nombres = [1, 2, 3, 4, 5]`

`nombres_carre = [x**2 for x in nombres]`

Dans cet exemple, la fonction lambda est utilisée pour définir une opération à appliquer à chaque élément d'une liste. 
Plus précisément, la fonction lambda `x**2` est utilisée pour calculer le carré de chaque nombre`x` dans la liste 
`nombres`. Cette fonction est ensuite intégrée dans une expression de liste `[x**2 for x in nombres]`, où elle est 
évaluée pour chaque élément de la liste `nombre`. Ainsi, la fonction lambda permet de créer rapidement une nouvelle 
liste contenant les carrés des nombres de la liste initiale.



## **Mise en garde lors de l'utilisation :** 

Dans ces contextes, l'utilisation de la fonction lambda a permis d'écrire un code plus concis et lisible, en évitant de
la définition formelle de fonction à part entière. Cependant, il est important de noter que l'abus de fonctions lambda 
peut rendre le code moins lisible. En effet, en ayant trop de fonction lambda le lecteur pourrait avoir de la difficulté
à comprendre comment les résultats sont obtenus. Il est conseillé de les utiliser avec modération et de privilégier la 
clarté du code plutôt que d'essayer de le rendre trop concis. Cette fonction peut être très utile dans certains contextes,
mais elle n'est pas toujours nécéssaire. 



## **Conclusion :** 

La fonction lambda peut sembler compliqué au premier regard, par contre elle permet de créer des fonctions simples et 
rapides sans la nécessité de définir formellement une fonction avec le mot-clé `def`. Sa syntaxe est concise et elle 
permet d’être utilisé dans plusieurs contexte. Elle est très utile dans le filtrage de données, le tri personnalisé et 
les expressions de listes. Bien quel doit être utilisé avec modération, c’est un bel outil à avoir dans son coffre à 
outils de programmeur Python. C’est une belle alternative pour faire varier votre code des autres techniques appris dans 
ce cours. 



#### **Source :** 

* [https://www.w3schools.com/python/python_lambda.asp](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/fonctions-lambda-en-python/)
* https://realpython.com/python-lambda/
* https://chat.openai.com/
* https://www.ionos.fr/digitalguide/sites-internet/developpement-web/fonctions-lambda-en-python/