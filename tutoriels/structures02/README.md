# Tutoriel: Quelles sont les différences entre une liste et un tuple : pourquoi et comment les utiliser ?

## Le contexte de la problématique d'affaires
Au 21e siècle, bien savoir utiliser la technologie dans le monde des affaires peut être un avantage considérable par rapport à la compétition, mais peut aussi amener plusieurs enjeux. Par exemple, choisir la structure de données appropriée pour stocker et manipuler les données d'affaires est très important pour le bon fonctionnement de n'importe quelle entreprise. Deux de ces structures en Python sont les listes et les tulpes et savoir les différencier permet de choisir la structure la plus appropriée et rendre l'accès et la manipulation aux données d'affaires beaucoup plus simple pour le futur.

Pour ce tutoriel, les conaissances préalables nécessaires sont:
- Une connaissance de base en Python.
- Une compréhension des concepts de variables, de types de données et de structures de contrôle serait également bénéfique.
  
## Un exemple pour introduire le contenu du tutoriel en contexte de manipulation des données
Si nous prenons comme exemple une compagnie d'investissement. Cette compagnie doit stocker différentes informations comme leur liste de clients, leur liste d'employés et les différents titres et produits que la compagnie gère. Pour stocker ces informations, la compagnie peut utiliser des listes et des tuples pour ensuite facilement y avoir accès. Par exemple, la compagnie peut elle-même créer une liste ou un tuple pour stocker sa liste de client:

``` Python 
#Création du tuple
Tuple = ("Client1","Client2","Client3","Client4")

#Création de la liste
Liste = ["Client1","Client2","Client3","Client4"]
```
Les données sont maintenant stockées en liste et en tuple, ce qui permet à la compagnie de manipuler ces données quand elle en a besoin. 

## Présentation et illustration du contenu du tutoriel
Il y a plusieurs différences entre une liste et un tuple et plusieurs façons pour les utiliser. Premièrement, en regardant l'exemple plus haut de création d'une liste et d'un tuple, la première différence est la syntaxe. Les listes sont définies avec des crochets [ ] alors que les tuples sont définis avec des parenthèses ( ). 

Deuxièmement, la différence qui vient déterminer quelle structure est la plus appropriée est leur mutabilité. Les listes peuvent être modifiées, ce qui veut dire qu'on peut supprimer, ajouter et modifier les éléments dans des listes après leur création. Au contraire, les tuples sont immuables, ce qui veut dire qu'on ne peut pas les modifier après leur création (Docstring, Les tuples en Python). Voici un exemple pour représenter cette deuxième différence:

``` Python
#Modification d'un élément de la liste
Liste[0]="Client5"
#Afficher le résultat du changement
print(Liste)  #Affichera: ['Client5', 'Client2', 'Client3', 'Client4']

#Tentative de modification d'un élément du tuple
#Tuple[0]="Client5" #Cela va créer une erreur; TypeError: 'tuple' object
#does not support item assignment

#Ajout d'un élément dans la liste
Liste.append("Client6")
#Afficher le résultat de l'ajout
print(Liste)    #Affichera: ['Client5', 'Client2', 'Client3', 'Client4', 'Client6']

#Tentative d'ajout d'un élément dans le tuple
#Tuple.append("Client6") #Cela va encore créer une erreur; AttributeError: 'tuple' object
                            # has no attribute 'append'
``` 
Comme on peut voir dans cet exemple, on peut facilement modifier un élément de la liste (Client1) par un nouveau (Client5). Cependant, on ne peut pas dire la même chose pour le tuple, car lorsqu'on essaie de modifier un élément dans le tuple, cela crée une erreur dans le code. C'est la même chose pour l'ajout d'un élément. Dans la liste, on peut facilement le faire avec l'attribut .append qui va ajouter "Client6" à la fin, alors que ça crée une erreur pour le tuple. 

La troisième différence, qui découle de la deuxième, est l'utilisation des listes et des tuples. Il est mieux d'utiliser une liste lorsque ce sont des données que nous allons vouloir modifier dans le futur et utiliser un tuple quand ce sont des données qui ne doivent pas être modifiées. Pour notre exemple de compagnie d'investissement, si la liste de client doit être modifiée fréquemment pour ajouter et retirer des clients, alors il est mieux de la stocker dans une liste. Si c'est une liste très importante qui ne doit pas être modifiée, alors on utilise un tuple (Docstring, Les tuples en Python).

La dernière différence est la performance d'un tuple comparé à une liste. En général, les tuples sont plus rapides que les listes à cause de leur immuabilité (Docstring, Les tuples en Python).

Une fois la liste et le tuple créé, la compagnie peut accéder à ces données de la même façon avec la fonction "print":

``` Python
# Accéder aux éléments dans la liste et le tuple
print("Éléments de la liste :", Liste[0])    # Affichera :Client5
print("Éléments du tuple :", Tuple[1])      # Affichera : Client2
```

Maintenant que la différence entre les listes et les tuples et leur utilisation sont expliquées, voici des bonnes pratiques et astuces pour la manipulation efficace des données:
- Utiliser des noms de variables significatifs pour se retrouver plus facilement dans son code. S'il y a plusieurs listes ou tuples dans un code, les identifier selon ce que contient la liste ou le tuple peut rendre la manipulation des données plus simple par la suite (Daniel Chamberland-Tremblay, Bonnes pratiques de base de programmation en Python).
- Utiliser des listes pour des données qui doivent être facilement et régulièrement modifiées.
- Utiliser des tuples pour des données qui ne doivent pas être accidentellement modifiées.
  
## Transfère des connaissances à d'autres contextes 
Une façon d'utiliser les tuples est de les utiliser comme clés d'un dictionnaire. Un dictionnaire est une autre structure de données qui ne sera pas abordée en profondeur dans ce tutoriel. Voici un exemple où l'on veut avoir accès aux notes de différents étudiants dans différentes matières. 

``` Python
#Exemple 1
# Création d'un dictionnaire qui contient les notes des étudiants
Notes = { ('Joany', 'Finance'):90,
          ('Eve', 'RH'):85,
          ('Jade', 'Marketing'):80}

# Avoir accès aux notes des étudiants
print("Note de Joany en Finance:", Notes[('Joany', 'Finance')])
#Affichera: 90

#Ajouter une nouvelle note
Notes[('Joany', 'RH')]=85
print("Note de Joany en RH:", Notes[('Joany', 'RH')])
#Affichera: 85
```
Premièrement, il faut créer un dictionnaire en utilisant des accolades { } et en prenant des tuples comme clés du dictionnaire. Ici un exemple de tuple est ('Joany', 'Finance') et sa valeur est de 90. Les tuples offrent l'avantage de pouvoir représenter des paires de données uniques, ce qui les rend utiles dans ce cas. Ensuite, pour avoir accès aux notes, on utilise les tuples pour afficher la note. Finalement, on peut ajouter de nouvelles notes lorsque les examens sont corrigés en ajoutant un nouveau tuple avec sa valeur au dictionnaire. 

Un autre exemple pour appliquer le contenu du tutoriel à un autre contexte serait dans ce cas-ci un magasin qui vend des articles scolaires. Ce magasin stocke les données des commandes des clients sous forme de tuples qui contiennent le nom du client, les effets scolaires commandés et le coût de la commande. Pour que ça soit plus simple pour le magasin d'ajouter, supprimer ou modifier les éléments de la commande, on peut modifier des tuples en listes comme dans cet exemple:

``` Python
#Exemple 2
#Données sur les commandes des clients sous forme de tuple
#(Nom de client, Commande, Coût)
Commandes_des_clients = (("Joany", ["Stylo", "Cartable"],10),
             ('Eve',["Agenda", "Stylo"],15),
             ('Jade',["Agenda", "Surligneur", "Calculatrice"],20 ))

#Convertir les tuples en listes
Commandes_liste = [list(commande) for commande in Commandes_des_clients]

#Ajouter un nouvel article à la commande de Joany
Index_Joany = [i for i, (nom, _, _) in enumerate(Commandes_liste) if nom == "Joany"][0]
Commandes_liste[Index_Joany][1].append("Agenda")

# Afficher les commandes modifiées sous forme de listes
print("Commandes des clients sous forme de listes :")
for commande in Commandes_liste:
    print(commande)
# Affichera: 
# ['Joany', ['Stylo', 'Cartable', 'Agenda'], 10]
# ['Eve', ['Agenda', 'Stylo'], 15]
# ['Jade', ['Agenda', 'Surligneur', 'Calculatrice'], 20]
```
Dans cet exemple, nous commençons avec nos données de commandes stockées dans des tuples dans la variable "Commandes_des_clients" et nous les transformons en listes avec la fonction "list". Par la suite, les commandes sont modifiables puisqu'elles sont maintenant stockées dans des listes qui elles peuvent être modifiées comme présenté dans l'exemple.

Ces deux exemples sont facilement applicables et répétables dans n'importe quel contexte.

## Limites du tutoriel et les prochaines étapes d'apprentissage
Voici quelques limites du tutoriel:
- Les exemples fournis sont assez simples pour qu'ils puissent être compris facilement et appliqués à plusieurs situations. Cependant, certaines situations vont demander des connaissances plus poussées pour pouvoir bien manipuler les données.
- Il y a d'autres structures de données importantes en Python comme les ensembles et les dictionnaires qui ne sont pas expliquées en détail dans ce tutoriel, mais qui sont très utiles pour la manipulation de données.

Les prochaines étapes d'apprentissage:
- Explorer d'autres structures de données comme les ensembles et les dictionnaires et leur utilisation dans différents contextes vont aider à avoir une meilleure compréhension de la manipulation de données.
- Explorer des techniques plus avancées de manipulation de données comme des fonctions et différentes bibliothèques vont permettre de pouvoir accomplir des manipulations de données plus compliquées.
- Explorer comment importer des données en listes ou tuples d'un document json, csv ou même d'un Excel.
- Prendre ces connaissances et les appliquer à des projets réels est la meilleure façon de les développer et d'apprendre davantage. 

## Synthèse
En conclusion, il est de plus en plus important avec l'avancement technologique de choisir les bonnes structures de données pour stocker les informations dans le monde des affaires. Dans ce tutoriel, les différences entre les listes et les tuples ont été abordées à l'aide d'explications et d'exemples. Les concepts clés qui ont été abordés sont leur mutabilité, leur syntaxte et leurs utilisation appropriée. Ce tutoriel permet au lecteur de savoir quand utiliser des listes ou des tuples et lui permet d'approfondir ses connaissances et de créer des codes plus robustes. Les prochaines notions intéressantes pour le lecteur seraient de découvrir les autres structures de données, les différentes bibliothèques et les fonctions plus avancées en python pour pouvoir effectuer des codes dans n'importe quel contexte. 

## Sources:
Docstring, Les tuples en Python, 18 mars 2024, https://www.docstring.fr/glossaire/tuple/#:~:text=La%20diff%C3%A9rence%20fondamentale%20entre%20les,pouvez%20pas%20modifier%20leurs%20%C3%A9l%C3%A9ments.

Daniel Chamberland-Tremblay, Bonnes pratiques de base de programmation en Python, gta431s02-variables-controle-et-logique-carj1826/bonnes_pratiques.md
