# Tutoriel : les API RESTful et leur utilisation (exemple de yfinance)

En contexte d'analyse de données d'affaires, on cherche habituellement à travailler avec la plus grande quantité possible de données afin d'obtenir des résultats de meilleure qualité. Par exemple, imaginons que l'on veut représenter l'évolution du cours d'une action sur les 20 dernières années : aucun problème, on n'a qu'à visiter un site comme Yahoo Finance, sélectionner la période et télécharger les prix pour plus de 5000 jours en un seul clic. Mais qu'arrive-t-il quand on s'intéresse à des dizaines, voire des centaines d'entreprises différentes? C'est ici que les API prennent tout leur sens, car ce qui serait cent fois plus long à faire manuellement représente une différence de temps négligeable à réaliser quand on utilise une API. 

Dans ce tutoriel, nous allons explorer : 
- ce qu'est une API RESTful
- pourquoi elles sont importantes
- comment les utiliser (en prenant l'exemple de yfinance).

## Qu'est-ce qu'une API RESTful ?

Une API RESTful suit la convention REST (Representational State Transfer). C'est un style d'architecture logicielle qui définit un ensemble de contraintes et de conventions pour la création de services web. Elle utilise les méthodes standard HTTP (Hypertext Transfer Protocol) telles que GET, POST, PUT et DELETE pour effectuer des opérations sur les ressources. Dans notre cas, c'est le GET qui sera principalement utilisé puisque nous voulons récupérer des données. 

Les principaux principes d'une API RESTful incluent :
- **Stateless (sans état)** : Chaque requête du client au serveur doit contenir toutes les informations nécessaires pour comprendre et traiter la demande. Le serveur ne conserve aucune information sur l'état du client entre les requêtes.
- **Resources (ressources)** : Les données sont considérées comme des ressources qui peuvent être manipulées à travers des requêtes. Chaque ressource est identifiée de manière unique par une URI (Uniform Resource Identifier).
- **HTTP Methods (méthodes HTTP)** : Les opérations CRUD (Create, Read, Update, Delete) sont effectuées à l'aide des méthodes HTTP appropriées (GET, POST, PUT, DELETE) sur les ressources.

## Pourquoi utiliser une API RESTful ?

Les API RESTful offrent plusieurs avantages, notamment :

- **Simplicité**: Elles utilisent des standards largement adoptés tels que HTTP, ce qui les rend faciles à comprendre et à utiliser.
- **Adaptabilité**: Elles permettent de construire des systèmes évolutifs en utilisant des ressources distribuées sur le web.
- **Flexibilité**: Les clients peuvent accéder aux ressources de manière indépendante, ce qui permet une évolution plus souple et des mises à jour plus faciles.
- **Interopérabilité**: Elles permettent l'intégration de différents systèmes et langages de programmation.

Maintenant, explorons comment utiliser une API RESTful en utilisant yfinance comme exemple.

## Exemple d'utilisation d'une API RESTful : yfinance

[yfinance](https://pypi.org/project/yfinance/) est une bibliothèque Python qui permet de récupérer des données financières directement depuis Yahoo Finance. Elle offre une interface simple et intuitive pour accéder aux données boursières telles que les prix des actions, les informations sur les sociétés, les données historiques, etc.

Pour commencer, assurez-vous d'avoir installé yfinance en utilisant pip :

```bash
pip install yfinance
```

Une fois yfinance installé, nous pouvons l'utiliser pour récupérer les données financières à partir de Yahoo Finance.

### Exemple d'utilisation de yfinance pour récupérer les données d'une action

Avant tout, il faut importer la bibliothèque `yfinance` et identifier les actions qui nous intéressent :

```python
# Importation des modules
import yfinance as yf

# Actions qui nous intéressent
tickers = (
    "AAPL",  # Apple
    "MSFT",  # Microsoft
)
```

Ensuite, nous utiliserons la fonction `Ticker` pour identifier les titres boursiers qui nous intéressent grâce à leur symbole (ticker). 
La boucle `for` nous permettra de récupérer les données pour chaque action :

```python
#Récupération des données
for ticker in tickers:
    action = yf.Ticker(ticker)
    # Attention! Ne pas oublier l'indentation des prochains éléments pour qu'ils soient dans la boucle for
```

Nous pouvons à présent utiliser les différentes fonctions de yfinance pour obtenir les données souhaitées. Voici quelques exemples :

```python
    # Informations générales
    print(action.info["longBusinessSummary"])  # Description de l'entreprise
    print(action.info["marketCap"])  # Capitalisation boursière
    print(action.recommendations)  # Recommandations des analystes
```
Remarquez la syntaxe ici : vous constaterez que `info` est un dictionnaire duquel on ne tire que certaines informations à l'aide de leur clé. Pour obtenir la liste des clés disponibles, vous pouvez utiliser `print(action.info.keys())` et constater qu'il y en a une quantité impressionnante!



Il est aussi possible d'utiliser `history()` pour récupérer des données historiques en spécifiant les paramètres souhaités :

```python
    # Données historiques
    period = "2y"  # Période en jours (d), semaines (wk), mois (mo), années (y) ou autre (YTD, max)
    value = ("Close")  # Valeurs acceptées : "Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"

    print(action.history(period=period)[value])
```

Quelques points à noter :
- Le paramètre `period` peut être remplacé par les paramètre `start` et `end` au format `"aaaa-mm-jj"` pour une période spécifique, ce qui peut être préférable dans certains cas : cela permet notamment d'obtenir les mêmes résultats si le programme est exécuté à des moments différents.
- Nous pouvons spécifier le paramètre `interval` pour modifier la fréquence des données (hebdomadaire, mensuelle ou trimestrielle). Dans la majorité des cas, cependant, les données quotidiennes (option par défaut) sont préférables et il n'est donc pas nécessaire de le préciser.
- Le paramètre `value` spécifie la donnée à récupérer. En supprimant `[value]` dans la dernière ligne, on obtient toutes les données.


## Conclusion

Une API RESTful est un outil puissant et polyvalent qui permet d'interagir avec des services web. Elle est essentielle pour de nombreux projets logiciels et offre de nombreux avantages aux personnes qui savent les utiliser (ou même les créer!). 

Dans le contexte de l'analyse des données financières, les API RESTful telles que yfinance offrent une manière simple et efficace de récupérer rapidement une grande quantité de données. Évidemment, pour en tirer le maximum, il faut les employer en combinaison avec d'autres outils et techniques. On pourra par exemple utiliser des bibliothèques de visualisation de données telles que Matplotlib ou Seaborn pour représenter graphiquement les données récupérées, ou encore des bibliothèques de traitement de données telles que CSV, JSON ou Pandas pour les manipuler et les analyser.
