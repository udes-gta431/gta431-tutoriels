# Tutoriel

# Problématique : Comment améliorer la gestion financière pour augmenter les bénéfices.

## Introduction

La gestion financière joue un rôle crucial dans le domaine des affaires, et elle implique souvent l'utilisation d'outils puissants comme Python pour analyser et interpréter les données financières.
La gestion financière dans le domaine des affaires requiert une approche complexe, impliquant la collecte et l'analyse de données financières.
Avec ses fonctions, Python propose des solutions robustes pour le traitement efficace de ces données.
Ce tutoriel nous permettra d’explorer l'utilisation de Python pour la gestion et l'analyse de données financières, en mettant l'accent sur des stratégies importantes telles que la concaténation de dictionnaires et de listes.


## Thématique utilisée dans cette analyse :

Comment concaténer des listes, comment concaténer des dictionnaires?
Avant d’appliquer l’analyse de la problématique sur mon exemple de données, je vais d’abord expliquer les définitions importantes relatives à la thématique et certaines stratégies et opérateurs du langage Python.


## Concaténation de listes en Python :

La concaténation de listes en Python consiste à fusionner deux ou plusieurs listes pour former une nouvelle liste résultante. 
On peut employer l'opérateur "+" pour fusionner des listes. Par exemple, en prenant deux listes, liste 1 et liste 2, la concaténation s'effectue avec l'expression nouvelle liste égale à **liste 1 + liste 2**, créant ainsi une nouvelle liste englobant tous les éléments des deux listes initiales.

Exemple de cette définition :
```python
 Liste1 = [1,2,3]
 Liste2 = [4,5,6]
 Nouvelle_liste =liste1+liste2
 Print( nouvelle_liste )
 Résultat : [1,2,3,4,5,6]
```

## Concaténation de dictionnaires en Python :

Contrairement aux listes, les dictionnaires n’emploient pas l’opérateur "+" pour la concaténation, étant donné qu’ils sont des structures non-séquentielles.
Il s'agit de fusionner deux dictionnaires distincts pour former un nouveau dictionnaire contenant toutes les paires clé-valeur des dictionnaires d'origine.
Cela se fait en utilisant l’opérateur d’union “| “, qui prend en argument un autre dictionnaire et ajoute ses paires clés-valeurs au dictionnaire d’origine. Si une clé existe déjà dans le dictionnaire d’origine, la valeur associée à cette clé est mise à jour avec la nouvelle valeur du dictionnaire ajoutée.

Exemple de cette définition :
```python
 Dict1 = {1,2,3}
 Dict2 = {3,4,5}
 Nouveau_Dict = Dict1 | Dict2
 Print( Nouveau_Dict)
 Résultat : {1,2,3,4,5}
```
La concaténation de dictionnaires est utile lorsqu’on veut combiner des ensembles de données clé-valeur distincts et créer un dictionnaire global contenant toutes les informations nécessaires. Elle est réalisée de manière efficace avec l’opérateur mentionné dans l’exemple.


##  Le tri en Python :

Le tri en Python se réfère au processus de réorganisation d’une séquence d’éléments, comme une liste ou un dictionnaire. En combinaison avec la concaténation de listes ou de dictionnaire, le tri peut être particulièrement utile pour organiser les données d’une liste ou un dictionnaire combiné résultant de manière spécifique.
Le tri peut être effectué sur une liste à l’aide de la méthode _sort_ ou en utilisant la fonction _sorted_.

Exemple de cette définition :
```python
 Liste = [7,2,1,5,9]
 Liste.sort()
 Print(list)
 Resultat : [1,2,5,7,9]
```

## L’itération dans Python :

L’itération combinée avec la concaténation de listes et de dictionnaires est souvent utilisée pour parcourir des éléments d’une séquence (exemple de liste) ou d’une structure de données (exemple de dictionnaire) tout en construisant une nouvelle séquence ou structure résultante.
Une fonction plus courante qui est ‘’ FOR’’. On peut choisir cette structure de boucle en fonction  du contexte de la problématique et des conditions spécifiques qu’on doit satisfaire.
Exemple de cette définition :

```python
Liste = [A,B,C]
For element in Liste :
Print(element)
```
Dans cet exemple, la boucle __for__ parcourt de la liste et affiche le nom de l’élément et affiche le nom de cet élément à chaque itération.
Grâce à l’itération, le code devient plus élégant et plus concret.


## Le découpage dans Python :

Le slicing ou le découpage en Python se réfère à la technique permettant d’extraire une portion spécifique d’une séquence, comme une liste.
La notation [début : fin] indique la portion de la séquence que vous souhaitez extraire. Le point de départ (début) est inclus, et le point de fin (fin) est exclu. Si on définit le début, cela signifie que le découpage commence depuis le début de la séquence. Si on définit la fin, cela signifie que le découpage va jusqu’à la fin de la séquence.
En résumé, le découpage est une manière pratique d’extraire des parties spécifiques de la liste ou une séquence en Python, facilitant ainsi la manipulation et l’analyse des données.

Exemple de cette définition :

```python
Liste = [10, 15, 7, 20, 100, 58, 27, 44, 77, 99]
Liste_decoupee = [4:6]
Resultat : [100, 58]
```

## Mon exemple de données

Dans cette problématique nous allons utiliser des données qui ne sont pas réelles pour faire l’analyse de la gestion financière.
Voici les données pour les revenus réparties selon le mois et l’année en dollars :

Année 2021
Janvier:150000, Février: 175000, Mars:200000, Avril:225000, Mai: 250000, Juin:275000, Juillet: 300000, Aout:325000, Septembre: 350000, Octobre: 375000, Novembre: 400000, Décemebre: 4250000

Année 2022
Janvier:160000, Février: 185000, Mars:210000, Avril:235000, Mai: 260000, Juin:285000, Juillet: 310000, Aout:335000, Septembre: 360000, Octobre: 385000, Novembre: 410000, Décemebre: 4350000

Année 2023
Janvier:170000, Février: 195000, Mars:220000, Avril:2245000, Mai: 270000, Juin:295000, Juillet: 320000, Aout:345000, Septembre: 370000, Octobre: 395000, Novembre: 420000, Décemebre: 4450000

Année 2024
Janvier:180000, Février: 205000, Mars:230000, Avril:255000, Mai: 280000, Juin:305000, Juillet: 330000, Aout:355000, Septembre: 380000, Octobre: 405000, Novembre: 430000, Décemebre: 4550000

Voici les données des dépenses pour l’année 2023 :

Année 2023
Janvier:55000, Février:100000, Mars:70000, Avril:60000,	Mai:75000, Juin:80000, Juillet:70000, Aout:75000, Septembre:80000, Octobre:85000, Novembre:90000, Décembre:60000



## Analyse

Nous allons maintenant utiliser ces données sous forme de listes pour les années 2021, 2022, 2023 :

```python
# Liste de ventes de 2021
monthly_sales_2021 = [150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 375000, 400000, 425000]
# Liste de vente de 2022
monthly_sales_2022 = [160000, 185000, 210000, 235000, 260000, 285000, 310000, 335000, 360000, 385000, 410000, 435000]
# Liste de vente de 2023
monthly_sales_2023 = [170000, 195000, 220000, 245000, 270000, 295000, 320000, 345000, 370000, 395000, 420000, 445000]
```
 
Maintenant nous allons afficher une liste qui démontre la concaténation de liste (année 2021,2022,2023) :
```python
last_3_years_monthly_sales = monthly_sales_2021 + monthly_sales_2022 + monthly_sales_2023;
print("les ventes des trois dernières années concaténées sont :", (last_3_years_monthly_sales))
Résultat: [150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 375000, 400000, 425000, 160000, 185000, 210000, 235000, 260000, 285000, 310000, 335000, 360000, 385000, 410000, 435000, 170000, 195000, 220000, 245000, 270000, 295000, 320000, 345000, 370000, 395000, 420000, 445000]
```

Pour avoir une idée sur le montant total de ventes de ces trois dernières années, je vais additionner ces données :
```python
totale_des_ventes = sum(last_3_years_monthly_sales)
# On obtient un résultat de : 10710000 $
```

Maintenant on va aborder la technique de découpage pour analyser et avoir une idée sur les ventes pour chaque quatre mois de l’année 2023 :
```python
quarter1_2023 = monthly_sales_2023[0:3]
quarter2_2023 = monthly_sales_2023[3:6]
quarter3_2023 = monthly_sales_2023[6:9]
quarter4_2023 = monthly_sales_2023[9:12]
```

Et ensuite je vais faire la somme totale de chaque quart :
```python
print("La somme du premier quart  est :", sum(quarter1_2023))
print("La somme du deuxième quart est :", sum(quarter2_2023))
print("La somme du troisième quart est :", sum(quarter3_2023))
print("La somme du quatrième quart est :", sum(quarter4_2023))
#Résultat :
#La somme du premier quart est : 585000 $
#La somme du deuxième quart est : 810000 $
#La somme du troisième quart est : 1035000 $
#La somme du quatrième quart est : 1260000 $
```

Cette fois-ci je vais mettre les dépenses de l’année 2023 sous forme de liste :
```python
monthly_costs_2023 = [55000, 100000, 70000, 60000, 75000, 80000, 70000, 75000, 80000, 85000, 90000, 60000]
```

Maintenant on va calculer les profits de chaque mois de l’année 2023 en utilisant la boucle ( For) :
```python
monthly_profits_2023 = [];
for i in range(12):
    profit = monthly_sales_2023[i] - monthly_costs_2023[i]
    monthly_profits_2023 += [profit]
#Résultat: [115000, 95000, 150000, 185000, 195000, 215000, 250000, 270000, 290000, 310000, 330000, 385000]
```

Dans la gestion financière, il est parfois important de savoir le mois où le profit était très bas.
En effet, on va calculer cela comme ceci :

```python
min_profit = min(monthly_profits_2023)
#Résultat : 95000 $
```

Aussi, il est vraiment important dans une analyse financière de préciser le mois où il y a eu lieu le bas profit.
Donc, on peut faire cela comme ça :

```python
index_min_profit = monthly_profits_2023.index(min_profit)
#Résultat : 1. Cet index représente le mois de février.
#NB : janvier est représenté par l’index 0.
```

Une autre méthode pour afficher le minimum profit est la technique de triage.

```python
monthly_profits_2023.sort();
#Résultat : les profits 2023 en ordre croissant [95000, 115000, 150000, 185000, 195000, 215000, 250000, 270000, 290000, 310000, 330000, 385000]
```
Et on rajoute cette technique pour afficher la valeur du bas profit :

```python
monthly_profits_2023[0])
#Résultat : 95000 $
```

Concernant les données sous formes de dictionnaires, ces dernières seront affichées de cette façon :

```python
monthly_sales_2021_dict = {'January': 150000, 'February': 175000, 'March': 200000, 'April': 225000, 'May': 250000, 'June': 275000, 'July': 300000, 'August': 325000, 'September': 350000, 'October': 375000, 'November': 400000, 'December': 425000}
monthly_sales_2022_dict = {'January': 160000, 'February': 185000, 'March': 210000, 'April': 235000, 'May': 260000, 'June': 285000, 'July': 310000, 'August': 335000, 'September': 360000, 'October': 385000, 'November': 410000, 'December': 435000}
monthly_sales_2023_dict = {'January': 170000, 'February': 195000, 'March': 220000, 'April': 245000, 'May': 270000, 'June': 295000, 'July': 320000, 'August': 345000, 'September': 370000, 'October': 395000, 'November': 420000, 'December': 445000}

#La concaténation se fait de cette façon :
last_3_years_sales_dict = {
    2021: monthly_sales_2021_dict,
    2022: monthly_sales_2022_dict,
    2023: monthly_sales_2023_dict
}
#résultat: 
{2021: {'January': 150000, 'February': 175000, 'March': 200000, 'April': 225000, 'May': 250000, 'June': 275000, 'July': 300000, 'August': 325000, 'September': 350000, 'October': 375000, 'November': 400000, 'December': 425000}, 2022: {'January': 160000, 'February': 185000, 'March': 210000, 'April': 235000, 'May': 260000, 'June': 285000, 'July': 310000, 'August': 335000, 'September': 360000, 'October': 385000, 'November': 410000, 'December': 435000}, 2023: {'January': 170000, 'February': 195000, 'March': 220000, 'April': 245000, 'May': 270000, 'June': 295000, 'July': 320000, 'August': 345000, 'September': 370000, 'October': 395000, 'November': 420000, 'December': 445000}}
```

Pour bien comprendre le principe de concaténation, je vais ajouter un dictionnaire 2024 au dictionnaire des trois dernières années :

```python
#Maintenant on va l'ajouter aux autres années pour afficher les quatre:
last_4_years_sales_dict = last_3_years_sales_dict | { 2024 : monthly_sales_2024_dict }

#On obtient un résultat de dictionnaire englobant les quatre années :
{2021: {'January': 150000, 'February': 175000, 'March': 200000, 'April': 225000, 'May': 250000, 'June': 275000, 'July': 300000, 'August': 325000, 'September': 350000, 'October': 375000, 'November': 400000, 'December': 425000}, 2022: {'January': 160000, 'February': 185000, 'March': 210000, 'April': 235000, 'May': 260000, 'June': 285000, 'July': 310000, 'August': 335000, 'September': 360000, 'October': 385000, 'November': 410000, 'December': 435000}, 2023: {'January': 170000, 'February': 195000, 'March': 220000, 'April': 245000, 'May': 270000, 'June': 295000, 'July': 320000, 'August': 345000, 'September': 370000, 'October': 395000, 'November': 420000, 'December': 445000}, 2024: {'January': 180000, 'February': 205000, 'March': 230000, 'April': 255000, 'May': 280000, 'June': 305000, 'July': 330000, 'August': 355000, 'September': 380000, 'October': 405000, 'November': 430000, 'December': 455000}}
```

## Conclusion

Je termine ce tutoriel pour dire que le langage Python aide énormément dans l’analyse de données des entreprises à l’aide des listes et des dictionnaires. En effet, avec le code utilisé pour cette problématique, on arrive à bien visualisé des nouvelles données qui seront utiles dans une bonne stratégie d’analyse afin de maximiser les gains.
 Cependant, il y a des avantages et des désavantages concernant les dictionnaires par rapport aux listes. Par exemple, on remarque que les dictionnaires sont plus faciles à visualiser car ils disposent de clés qui permettent la clarté dans la lecture des données. D’autre part les listes sont plus rapides pour faire des calculs par rapport aux dictionnaires.

