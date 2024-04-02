## Tutoriel : Qu'est-ce qu'un ORM (ex. SQLAlchemy) : pourquoi et comment l'utiliser ?
# Introduction

Quand on crée des logiciels, surtout pour des projets d'école, où il faut que le travail soit vite fait et bien fait, gérer les informations stockées (comme dans un tableau de données) peut être un vrai casse-tête. 
C'est là que des outils appelés "mappings objet-relationnel" (ORM) (comme SQLAlchemy) nous viennent en aide. 
Imaginez ces outils comme des assistants qui prennent les informations complexes et les rendent faciles à manipuler dans notre code, un peu comme si on jouait avec des blocs de construction au lieu d'écrire des instructions compliquées. 
Utiliser SQLAlchemy, c'est un peu comme avoir un traducteur entre nous et la base de données; cela rend non seulement notre travail de création plus simple et notre code plus propre, mais ça aide aussi à éviter des erreurs qui pourraient rendre nos programmes vulnérables à des attaques. 
Pour les étudiants et les professeurs, apprendre à utiliser SQLAlchemy, c'est gagner du temps sur les projets et rendre nos programmes plus sûrs et de meilleure qualité.

# Contexte

Dans le secteur de la finance, un ORM comme SQLAlchemy se révèle particulièrement utile pour la gestion de portefeuilles et l'analyse de risques, où encore pour manipuler d'énormes volumes de données sur les actifs financiers quotidien. 
Cela permet aux développeurs de focaliser leur attention sur la logique commerciale, rendant plus facile l'intégration de diverses données financières, l'amélioration des stratégies d'investissement et l'adhérence aux normes réglementaires. 
L'utilisation d'un ORM comme SQLAlchemy permet une interaction plus intuitive et sécurisée avec les bases de données, essentielle dans un domaine où la précision et la rapidité d'accès aux données peuvent significativement impacter les décisions financières.

Pour mieux comprendre l'ORM, prenons l'exemple concret d'une application destinée à la gestion de portefeuilles d'investissement. 
Cette application vise à assister les investisseurs dans le suivi et l'analyse de leurs actifs financiers, incluant actions, obligations et fonds mutuels. 
Utiliser un ORM tel que SQLAlchemy dans ce cadre peut considérablement faciliter à la fois le développement et la maintenance de l’application.

# Connaissance Préalables

Afin de suivre ce tutoriel, il est important d'avoir des connaissances de base en Python, notamment sur les concepts suivants:

- Les types de données de base (comme les chaînes de caractères, les nombres, les listes, les dictionnaires, etc.)
- La définition et l'utilisation de fonctions
- La programmation orientée objet (création de classes, héritage)
- La gestion des exceptions
- Les opérations d'entrées/sorties de base, particulièrement en ce qui concerne la lecture et l'écriture de fichiers

# La programmation orientée objet
### Les utilisateurs de Python sont souvent moins familiarisés avec la POO; voici donc une brève explication de ce concept, qui est utilisé avec l'ORM :
La programmation orientée objet (POO) organise les programmes avec des "objets" qui combinent des données et des fonctions dans des "classes" faciles à utiliser et à modifier. 
Elle se base sur des idées comme regrouper les données, utiliser des modèles existants, et permettre aux différentes parties du code de s'interchanger facilement. 
C++ mise beaucoup sur la POO pour ses avantages, offrant plus d'outils orientés objet par rapport à Python, qui, tout en supportant la POO, est souvent vu comme plus simple et flexible pour différents types de programmation.

# Comment utiliser l'Object-Relational Mapping
Voici un guide étape par étape pour utiliser un ORM (Object-Relational Mapping) en Python, avec SQLAlchemy comme exemple. 
Ce guide vous aidera à démarrer avec l'intégration de bases de données dans vos applications Python d'une manière plus intuitive et orientée objet.

### Étape 1 : Installation de SQLAlchemy
Tout d'abord, vous devez installer SQLAlchemy. Ouvrez votre terminal ou invite de commande et exécutez la commande suivante :
```python
pip install SQLAlchemy
```
### Étape 2 : Configuration de la base de données
Ensuite, configurez votre base de données. Pour cet exemple, nous utiliserons SQLite, une base de données légère qui ne nécessite aucune configuration serveur.
```python
from sqlalchemy import create_engine

# Créez une connexion à une base de données SQLite en mémoire
engine = create_engine('sqlite:///:memory:', echo=True)
```
Le paramètre echo=True permet à SQLAlchemy de logger toutes les requêtes SQL générées, ce qui est utile pour le débogage.
### Étape 3 : Définitions des modèles
Les modèles en SQLAlchemy correspondent à des tables dans votre base de données. Ils sont définis comme des classes Python.
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
```
Ici, nous avons défini un modèle User avec trois champs : id, name, et age.
### Étape 4 : Création des tables
Après avoir défini vos modèles, créez les tables correspondantes dans votre base de données.
```python
Base.metadata.create_all(engine)
```
### Étape 5 : Création d'une session
La session en SQLAlchemy agit comme un tampon entre vos objets Python et la base de données.
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```
### Étape 6 : Ajout de nouveaux objets
Vous pouvez maintenant créer des instances de vos modèles et les ajouter à votre session pour les insérer dans la base de données.
```python
new_user = User(name='André Côté', age=47)
session.add(new_user)
session.commit()
```
### Étape 7 : Requêtes 
Utilisez la session pour faire des requêtes. Par exemple, pour récupérer tous les utilisateurs :
```python
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
```
### Étape 8 : Mise à jour et supression
Pour mettre à jour ou supprimer des objets, vous les modifiez ou les marquez pour suppression dans la session, puis vous validez ces changements.
```python
# Mise à jour
user_to_update = session.query(User).filter_by(name='André Côté').first()
user_to_update.age = 50
session.commit()

# Suppression
user_to_delete = session.query(User).filter_by(name='André Côté').first()
session.delete(user_to_delete)
session.commit()
```
### Conclusion du guide d'utilisation
Maintenant que vous êtes équipé des connaissances fondamentales nécessaires à l'utilisation d'un ORM, vous êtes prêt à l'intégrer dans vos projets variés en suivant les directives fournies précédemment. 
Cette approche vous permettra d'exploiter pleinement les avantages de l'ORM pour simplifier la gestion des données dans vos applications, en assurant une transition fluide et efficace entre votre code Python et votre base de données.

# Exemple d'un ORM en finance
Après avoir abordé les bases de l'utilisation d'un ORM à travers notre guide pratique, il est temps de plonger dans une application concrète de cette technologie, en nous orientant vers le secteur financier. 
Nous allons explorer un exemple pertinent : l'implémentation d'un ORM au cœur d'une application dédiée à la gestion de portefeuilles d'investissement. 
Cet exemple illustrera comment les principes discutés précédemment peuvent être appliqués pour simplifier et optimiser le développement et la maintenance de solutions logicielles dans le domaine complexe et exigeant de la finance, comme nous l'avons introduit dans notre contexte initial.

### Étape 1 : Installation de SQLAlchemy
```python
pip install SQLAlchemy
```
### Étape 2 : Configuration de la base de données
```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Définition de la base
Base = declarative_base()

# Connexion à la base de données SQLite
engine = create_engine('sqlite:///portfolio.db', echo=True)
```
### Étape 3 : Définition des modèles
```python
class Asset(Base):
    __tablename__ = 'assets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)  # Par exemple, 'stock', 'bond', 'mutual fund'
    value = Column(Float)

Base.metadata.create_all(engine)
```
### Étape 4 : Création d'une session
```python
Session = sessionmaker(bind=engine)
session = Session()
```
### Étape 5 : Ajout d'Actifs
```python
new_asset = Asset(name="Google Inc.", type="stock", value=2800.00)
session.add(new_asset)
session.commit()
```
### Étape 6 : Requêter les données
```python
assets = session.query(Asset).all()
for asset in assets:
    print(f"{asset.name}, {asset.type}, ${asset.value}")
```

En somme, en suivant ces étapes, vous avez créé une application simple de gestion de portefeuilles d'investissement en utilisant SQLAlchemy comme ORM. 
Cet exemple montre comment SQLAlchemy peut simplifier le développement et la maintenance de votre application en facilitant la manipulation des données. 
Vous pouvez étendre cet exemple en ajoutant plus de fonctionnalités, comme la gestion des transactions ou l'analyse des performances des actifs.

# Transfert de connaissances
L'adoption d'un ORM (Object-Relational Mapping) peut transformer la manière dont nous interagissons avec les bases de données, en particulier dans des contextes nécessitant une gestion complexe des données, comme c'est le cas pour la création d'applications de gestion de portefeuilles d'investissement. 
Par exemple, dans le processus de synchronisation et de mise à jour des données financières, l'utilisation d'un ORM facilite grandement l'intégration et la manipulation des données. 

En utilisant SQLAlchemy, un ORM populaire en Python, on peut modéliser chaque actif financier (actions, obligations, fonds mutuels) comme un objet Python. 
Ce paradigme objet facilite l'organisation des données, leur récupération, et leur mise à jour de manière intuitive et sécurisée. 
Ainsi, lors de la génération de rapports d'investissement automatisés, on peut tirer parti de cette structuration pour créer des rapports dynamiques qui s'adaptent aux changements des données en temps réel.

Cette approche offre une flexibilité sans précédent pour le développement d'applications financières, permettant aux développeurs de se concentrer sur la logique métier plutôt que sur les détails techniques de la base de données. 
Le transfert de connaissances de l'ORM vers la création de rapports d'investissement automatisés illustre comment la modélisation orientée objet des données peut simplifier et enrichir la présentation et l'analyse des données financières.

# Limites et prochaines étapes
Bien que le tutoriel sur les ORM couvre les bases essentielles pour démarrer, il est important de noter certaines limites. 
Les ORM ne sont pas toujours les plus performants pour des requêtes très complexes ou pour des opérations massives sur les données. 
À mesure que vous vous familiariserez avec les ORM, vous pourrez explorer des fonctionnalités avancées, comme l'optimisation des performances et la personnalisation des requêtes, pour mieux répondre aux besoins spécifiques de vos projets.

# Synthèse sur L'ORM
Notre exploration des ORM, en particulier SQLAlchemy, offre une légèrte introduction à l'intégration efficace des bases de données dans vos applications Python. 
En abordant les sujets fondamentaux, de la configuration initiale à la manipulation avancée des données, ce tutoriel vise à équiper les étudiants et les professeurs avec les outils nécessaires pour simplifier et optimiser l'accès aux données. 
Bien qu'il existe des limites, notamment pour les requêtes complexes ou les manipulations de données à grande échelle, la maîtrise des ORM ouvre la porte à des développements plus agiles et sécurisés. 
À mesure que vous gagnez en expérience, vous découvrirez des stratégies pour surmonter ces défis, enrichissant ainsi vos compétences en développement logiciel.

### Bibliographie
https://tahe.developpez.com/tutoriels-cours/python-flask-2020/?page=utilisation-de-l-orm-sqlalchem 

https://builtin.com/data-science/object-relational-mapping# 

https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/ 

https://www.youtube.com/watch?v=B1zrBwjnsPM

https://www.youtube.com/watch?v=g0-7TrVCNtg

ChatGPT