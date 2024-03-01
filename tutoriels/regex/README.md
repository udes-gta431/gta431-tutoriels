# Tutoriel_Regex101_GTA431_PICS2704
Tutoriel de comment fonctionne Regex dans Python

Introduction :
Dans le monde de la programmation, un des facteurs le plus importants est le traitement de données brutes. Ces données nous permettent de faire des analyses stratégiques. 
Pour ce faire, il est important de faire un nettoyage de données. Par contre, dans des bases de données volumineuses, 
il peut être demandant de faire des recherches complexes afin de trouver des résultats qui répondent à un critère particulier. 
Les boucles If, Do, for peuvent faire ce traitement, mais nécessite beaucoup de pouvoir machine. C’est dans cette situation que Regex peut nous venir en aide.
Regex vient du terme Regular Expression et permet de faire une manipulation, filtrer ou même extraire des données à partir d’une chaîne de caractères qui représente une condition à respecter. 
Prenons comme exemple que nous voulons trouver tous les numéros de téléphone dans un texte. Normalement, nous utiliserons une boucle for afin de trouver la valeur :
```python
texte = "Contactez-moi au 123-456-7890 ou au 987.654.3210 pour plus d'informations."

numeros_telephone = []
numero_temp = ""
for char in texte:
    if char.isdigit() or char in "-.":
        numero_temp += char
    elif numero_temp:
        numeros_telephone.append(numero_temp)
        numero_temp = ""
print(numeros_telephone)
```
resultat: ['-', '123-456-7890', '987.654.3210']

Avec Regex, nous pouvons faire la même recherche plus facilement :
```python
import re

texte = "Contactez-moi au 123-456-7890 ou au 987.654.3210 pour plus d'informations."

numeros_telephone = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', texte)

print(numeros_telephone)
```
resultat: ['123-456-7890', '987.654.3210']

Comme nous pouvons voir, Regex permet d’extraire l’information plus précisément avec une seule ligne de code. Bien que le code ne soit pas simple à comprendre à première vue, Nous allons découvrir ensemble comment Regex fonctionne et l’explication détailler de celui-ci.

# Concepts clés
- [Les métacaractères et les quantificateurs](demo/caractere.md)
- [Les fonctions de regex](demo/Fonctions.md)
- [Contexte](demo/Contexte.md)


Références:<br>
- https://regexr.com/
- https://www.datacamp.com/cheat-sheet/regular-expresso
- https://www.w3schools.com/python/python_regex.asp
- https://www.geeksforgeeks.org/regular-expression-python-examples/
