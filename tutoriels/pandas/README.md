# Projet-tutoriel
Introduction au problème d’affaire en lien avec la bibliothèque Panda

  

La bibliothèque logicielle Panda est un outil d’analyse et de manipulation de données open-source qui est spécifiquement conçu pour la manipulation de donnée du langage python. Panda est un outil performant, flexible et simple d’utilisation qui permet de charger, aligner, manipuler et fusionner des données issues du langage python. La bibliothèque peut aussi être utilisée pour traiter les données structurées sous forme de tableaux, matrice ou de série temporelle composée de nombres ou de caractères.   

Cet outil est actuellement utilisé dans plusieurs domaines soit les commerces, l’immobilier le domaine de la santé et le domaine des finances. Par exemple, dans le cadre d’une entreprise qui doit analyser des données qui sont reliées entre elles telles que des données sur les clients et leurs transactions ce qui peut représenter la réalité de n’importe quelle entreprise qui offre un service ou un produit. Ainsi l’entreprise est en mesure de prendre une base de données des ventes puis de l’associer à une base de données clients et d’analyser les tendances de consommations de sa clientèle. Par la suite, cela est pratique pour adapter son offre en conséquence et améliorer ses performances de ventes ou prédire certains comportements.   

Pour manipuler la bibliothèque, des connaissances de base du langage Python sont requises au préalable. Il n’est pas nécessaire d’avoir d’autres connaissances avancées dans le domaine puisque Panda a été élaboré pour une utilisation intuitive et simple.    

Pandas fonctionne à partir de « tables » et donc de données disposées sous forme de lignes et de colonnes. Les informations sont présentées sous forme de « dataframes » soit des lignes et des colonnes, à la façon des tableaux. Il peut opérer à partir de format de fichiers fort populaires, tels qu’Excel, ou encore le .CSV, mais aussi sur des bases de données de haut niveau comme celles gérées avec SQL. De fait, la polyvalence de Pandas est un de ses atouts majeurs. Une fois ces documents absorbés par Pandas et transformés en « dataframes », il devient possible de leur appliquer des opérations statistiques et des transformations.    

   

Exemples d’un contexte d’utilisation  

  

Voici un exemple de codage en utilisant la bibliothèque Pandas en Python. Supposons que nous avons des données sur des étudiants, telles que leurs noms, âges et notes, et que vous souhaitez les stocker dans un dataFrame Pandas.   

  

Dans un premier temps, la bibliothèque Pandas doit être installée en utilisant la commande suivante si :   

bashCopy code   

pip install pandas   

Ensuite, vous pouvez utiliser le code suivant :   

#Pd signifie bibliothèque Panda dans le code   

pythonCopy code   

import pandas as pd   
   
 # Création d'un dictionnaire avec des données d'étudiants   
 donnees_etudiants = {   
     'Nom': ['Alice', 'Charle', 'Aby', 'Félix'],   
     'Age': [20, 22, 21, 23],   
     'Note': [85, 90, 78, 95]}   
   
 # Création d'un dataFrame à partir du dictionnaire   
 dataframe_etudiants = pd.DataFrame(donnees_etudiants)   
   
 # Affichage du DataFrame   
 print("DataFrame des étudiants :")   
 print(dataframe_etudiants)   
   
 # Calcul de la moyenne des notes   
 moyenne_notes = dataframe_etudiants['Note'].mean()   
 print("\nMoyenne des notes : {:.2f}".format(moyenne_notes))   
   
 # Filtrage des étudiants ayant obtenu une note supérieure à la moyenne   
 etudiants_superieurs_moyenne = dataframe_etudiants[dataframe_etudiants['Note'] > moyenne_notes]   
 print("\nÉtudiants ayant obtenu une note supérieure à la moyenne :")   
 print(etudiants_superieurs_moyenne)   

   

Ce code crée un dataFrame Pandas à partir d'un dictionnaire de données sur les étudiants, affiche le dataFrame, calcule la moyenne des notes, puis filtre et affiche les étudiants ayant obtenu une note supérieure à la moyenne.   

   

Pour mieux comprendre les capacités de la bibliothèque Panda, supposons un exemple dans un autre contexte. Par exemple que nous avons un fichier nommé "immobilier" contenant des données sur les prix des immeubles dans différentes régions. Voici comment vous pourriez charger et analyser ces données à l'aide de Pandas :   

pythonCopy code   

import pandas as pd   
   
 # Charger les données depuis le fichier   
 df_immobilier = pd.read_csv("immobilier")   
   
 # Afficher les premières lignes du dataframe   
 print("Premières lignes du dataframe :")   
 print(df_immobilier.head())   
   
 # Afficher des informations sur les colonnes et les types de données   
 print("\nInformations sur les colonnes :")   
 print(df_immobilier.info())   
   
 # Résumé statistique des données numériques   
 print("\nRésumé statistique des données numériques :")   
 print(df_immobilier.describe())   
   
 # Filtrer les maisons avec un prix supérieur à 500 000 $   
 maisons_cheres = df_immobilier[df_immobilier['Prix'] > 500000]   
   
 # Afficher les maisons avec un prix supérieur à 500 000 $   
 print("\nMaisons avec un prix supérieur à 500 000 $ :")   
 print(maisons_cheres)   
   
 # Trouver la moyenne du prix des immeubles par région   
 moyenne_par_region = df_immobilier.groupby('Région')['Prix'].mean()   
   
 # Afficher la moyenne du prix des immeubles par région   
 print("\nMoyenne du prix des immeubles par région :")   
 print(moyenne_par_region)   

Assurez-vous de modifier le nom du fichier et d'ajuster le code en fonction de la structure réelle de vos données sur l'immobilier.   

   

   

  

Tutoriel   

Installation de Pandas :   

Ouvrez votre terminal ou votre invite de commande   

Tapez pip install pandas et appuyez sur Entrée   

Attendez que l'installation soit terminée   

Importer la bibliothèque Pandas :   

Ouvrez votre éditeur Python préféré (ex: PyCharm,Jupyter, etc.)   

Ajoutez cette ligne de code en haut de votre script pour importer Pandas :   

 

import pandas as pd   
    

Lecture de données :   

Pandas offre de nombreuses fonctions pour lire différents types de fichiers de données (CSV, Excel, SQL, etc.)   

Par exemple, pour lire un fichier CSV, utilisez la fonction pd.read_csv("nom_du_fichier.csv")   

Vous pouvez spécifier différentes options de lecture (ex: séparateur, colonnes à lire, etc.)   

Manipulation de données :   

Pandas offre de nombreuses fonctions pour manipuler les données   

Vous pouvez filtrer des données, trier des données, grouper des données, effectuer des calculs et plus encore. 

Utilisez les fonctions intégrées de Pandas pour réaliser ces opérations   

Affichage des données :   

Pandas offre des méthodes pour afficher les données à l'écran   

Par exemple, utilisez, print(df) pour afficher un DataFrame (tableau de données) ou utilisez df.head() pour afficher les premières lignes   

Ce tutoriel couvre les bases de la bibliothèque Pandas en Python. Il existe de nombreux autres concepts avancés que vous pouvez explorer tels que la fusion de données et la visualisation des données. 

Pour mieux comprendre les capacités de la bibliothèque Panda, supposons un exemple dans un autre contexte. Par exemple que nous avons un fichier nommé "immobilier" contenant des données sur les prix des immeubles dans différentes régions. Voici comment vous pourriez charger et analyser ces données à l'aide de Pandas :   

pythonCopy code   

import pandas as pd     
   
 # Charger les données depuis le fichier   
 df_immobilier = pd.read_csv("immobilier")   
   
 # Afficher les premières lignes du dataframe   
 print("Premières lignes du dataframe :")   
 print(df_immobilier.head())   
   
 # Afficher des informations sur les colonnes et les types de données   
 print("\nInformations sur les colonnes :")   
 print(df_immobilier.info())   
   
 # Résumé statistique des données numériques   
 print("\nRésumé statistique des données numériques :")   
 print(df_immobilier.describe())   
   
 # Filtrer les maisons avec un prix supérieur à 500 000 $   
 maisons_cheres = df_immobilier[df_immobilier['Prix'] > 500000]   
   
 # Afficher les maisons avec un prix supérieur à 500 000 $   
 print("\nMaisons avec un prix supérieur à 500 000 $ :")   
 print(maisons_cheres)   
   
 # Trouver la moyenne du prix des immeubles par région   
 moyenne_par_region = df_immobilier.groupby('Région')['Prix'].mean()   
   
 # Afficher la moyenne du prix des immeubles par région   
 print("\nMoyenne du prix des immeubles par région :")   
 print(moyenne_par_region)   

Assurez-vous de modifier le nom du fichier et d'ajuster le code en fonction de la structure réelle de vos données sur l'immobilier.   

   

   

Autres apprentissages  

Le tutoriel présente qu’une infirme partie des capacités de la bibliothèque Panda. De nombreuses autres fonctionnalisées plus avancées sont possibles tel qu'obtenir un résumé rapide de votre dataFrame (moyenne, écart type, minimum, maximum et d’autres informations pour chacune des colonnes du dataFrame). Les méthode comme ci-dessous peuvent être appliquées.   

describe() :   

dataFrame.describe()   

Un dataFrame offre également un certain nombre de fonctions statistiques telles que:   

abs() – valeurs absolues   

mean() – Valeurs moyennes. On a aussi median() et mode()   

min() – valeur minimale (et max())   

count(), std() – écart type, prod() – pour calculer le produit des valeurs et cumsum() pour calculer les sommes cumulées, etc.   

   

Les dataFrames offrent des options pour tracer des graphiques. Nous pouvons tracer des courbes, des boîtes à moustaches, des surfaces, des nuages de points, des graphiques empilés, des diagrammes à barres, des histogrammes, etc…   

dataFrame.plot.bar() # retourne un diagramme à barres   

dataFrame.diff.hist(bins=10) # retourne un histogramme   

dataFrame.plot.scatter() # retourne un graphique de nuage de points   

   

Les limites  

  

La bibliothèque quoi que très performantes et simple d’utilisation celle-ci a certaines limites.  

  

Fonction de base: Le tutoriel présenté est utilisé pour démontrer les fonctionnalités de base de cet outil et ne permet pas de résoudre tout type problème. Il est nécessaire de suivre d’autres tutoriel et de continuier à développer ses compétences.    

  

Structure de travail: un problème peut vite devenir complexe et l’utilisation de la plateforme difficile sans une structure de travail adéquate.   

  

Gestion de grandes quantités de données : bien que panda permette de manipuler et analyser de grandes quantités de données, son utilisation peut être limitée pour des ensembles de données extrêmement volumineux. Dans de tels cas, il est préférable d'utiliser d'autres bibliothèques spécialement conçues pour les fichiers volumineux.   

Temps de traitement : bien que pandas soit relativement rapide, le temps de traitement peut augmenter significativement avec des opérations complexes ou l'application de fonctions personnalisées.   

  

Compatibilité avec d'autres outils : pandas est principalement conçu pour être utilisé avec Python et n'a pas une compatibilité totale avec d'autres langages de programmation.   

 

Bref résumé  

En bref, a bibliothèque Panda est un outil pratique pour l’analyse et le traitement des données à l’aide du langage python. Les principaux avantages de la structure des données qu’offre Panda sont les séries soit en étiquetant sous forme de tableaux à une dimension, des dataFrames soit une structure bidimensionnelle (des données alignées de façon tabulaire) et des Panels soit une structure de données tridimensionnelles. Panda est un outil polyvalent accessible pour tous les niveaux et à disposition de tous.  

 


Bibliographie 

Datasciente (janvier 2024) Panda: la bibliothèque Python dédiée à la Data science, Pandas : la bibliothèque Python dédiée à la Data Science (datascientest.com) 

D. Starnes,(2024) Explore your Dataset with Pandas, Explore Your Dataset With pandas – Real Python 

Jehda (2023), L’essentiel à savoir sur Pandas : la bibliothèque Python, L'essentiel à savoir sur Pandas : la bibliothèque Python (jedha.co) 

(Janvier 2024) User guide, pandas documentation — pandas 2.2.0 documentation (pydata.org) 
