# Tutoriel: Qu'est-ce que le format datetime : pourquoi et comment l'utiliser?

## Introduction 
Comme tout langage en programmation, Python intègre le module datetime, indispensable dans de nombreux projets et structures organisationnelles pour la gestion précise des dates d'échéance et d'enregistrement. Contrairement à certains types de données intégrés, tels que les nombres, Python ne propose pas de structure native pour les dates, d'où l'importance du module datetime pour manipuler efficacement ces informations. Ce module fournit une classe de base abstraite qui offre une gamme de types de données pour les heures et les dates, permettant ainsi une flexibilité et une précision accrues dans la programmation. Dans des contextes de projets complexes, où la gestion du temps est cruciale, le module datetime devient un outil incontournable, facilitant la manipulation et le traitement des informations temporelles. Grâce à cette fonctionnalité, les développeurs peuvent structurer leurs applications de manière plus robuste et efficace, améliorant ainsi la qualité et la fiabilité de leurs logiciels. En somme, l'intégration du module datetime dans Python renforce sa polyvalence et sa pertinence dans une variété de contextes de développement logiciel.

## Contexte 

Dans le monde professionnel, la gestion précise des dates et heures est devenue indispensable. Que ce soit pour coordonner des réunions, respecter des échéances ou planifier des projets, la manipulation efficace des horaires est cruciale. Les calculs liés aux dates sont omniprésents dans divers secteurs, permettant de planifier les activités et d'évaluer les délais. Ainsi, une maîtrise adéquate des outils informatiques est essentielle, notamment des langages comme Python avec ses modules de gestion des dates comme datetime. Ces compétences permettent de rationaliser les processus de travail et d'optimiser la productivité. En outre, une compréhension approfondie des implications temporelles facilite la prise de décision et la gestion des ressources. En fin de compte, la gestion efficace du temps contribue à la réussite globale des projets et à la réalisation des objectifs organisationnels.

## Fonctionnement du module datetime
Il Permet de créer des objets qui vont représenter le temps avec les heures, les minutes, les secondes et les microsecondes. Il nous donne quatre classes principales pour travailler avec les heures et les dates qui sont : 
- Classe date : pour reprsenter des dates (année, mois, jour) 
- Classe time : représente des heures (heure, minutes, secondes, microsecondes) 
- Classe datetime : représente des dates et des heures combinées
- Classe timedelta : représente une différence entre deux dates ou heures.

  Avant toute manipulation, vous devez importer le module avant de le manipuler
```python
# Section d'importation des modules
import datetime
```

## Première manipulation avec datetime

Dans cet exemple, nous pouvoir voir comment obtenir la date, l'heure exacte ainsi que le fuseau horaire à l'instant ou nous exécutons le code.
```python
asd = datetime.datetime.today()
print(asd)
```
![00](https://github.com/pitalain/Tutoriel/assets/132237358/f7d4a838-fdd5-49a3-9828-21e521da243c)

Ceci est un autre exemple nous permettant de voir à travers un autre code pour avoir la date et l'heure exacte à l'instant ou nous exécutons le code 
```python
exple = datetime.datetime.now()
print(exple)
```
![01](https://github.com/pitalain/Tutoriel/assets/132237358/653d5a7f-45b8-45be-88c4-23f7b494fdc7)


Comme on peut le voir la seule différence est avec les méthodes now() et today(). En utilisant la même syntaxe, ceci nous permet d'avoir le même résultat.
En plus, la méthode today() récupère la date du jour à partir de l'horloge interne de l'ordinateur tandis que la méthode

Pour la classe datetime, nous pouvons également afficher uniquement la date, l'heure, les minutes et les secondes.
```python
# Affectation de la date, l'heure, les minutes et les secondes
aff = datetime.datetime(2019, 10, 7, 10, 9, 58)
print(aff)
```

Ce code retournera le résultat: 2019-10-07 10:09:58. Mais il est possible d'exécuter le code en affichant uniquement le mois, l'année, la date, l'heure, les minutes ou les secondes
```python
#Affichage des composantes individuels des dates, d'heures, minutes
print(aff.year)      # Année
print(aff.month)     # Mois
print(aff.day)       # Jour
print(aff.hour)      # Heure
print(aff.minute)    # Minute
print(aff.second)    # Seconde
```

## Formatage des dates 

Il est possible également de formater les résultats. L'affichage de la date par-défaut s'effectue au format AAAA-MM-JJ, mais vous pouvez formater des heures et des dates comme vous les souhaitez. 
Il existe une multitude de chaînes de format des dates et d'heures mais dans ce tutoriel, nous allons parcourir quelques unes d'entre elles. Vous pouvez consulter ce lien pour avoir la liste complète: 
[Liste des chânes de formatage de date et d'heures](http://www.python-simple.com/python-modules-autres/date-et-temps.php)
Nous pouvons se pratiquer avec ce lien sur les dates et les heures également.

Quand vous utilisez des chaînes de format, veillez à placer des espaces, des barres obliques et tout autre élément entre les directives à l'endroit ou vous souhaitez que ces signes apparaissent en sortie.

```python
#Affichage de la date en uttilisant le formatage
print(f"{aff:%A, %d %B, %Y}")
```

Quand le code ci-dessus est exécuté, ce résultat est affiché en sortie: Monday, 07 October, 2019

Pour afficher la date au format JJ/MM/AAAA, utilisez %d%m%Y, de la manière suivante: 
```python
#Affichage de la date au format JJ/MM/AAAA
exple = f"{aff:%d/%m/%Y}"
print(exple)
```

Après instruction, nous aurons ce résultat en sortie: 07/10/2019

Il est également possible d'afficher les dates dans un autre formatage de date. Dans le code ci-dessous, nous voyons que le module datetime offre des méthodes pour formater les objets datetime 
en chaînes de caractères :
```python
# Formater un objet datetime en chaîne de caractères
print(dt.strftime("%Y-%m-%d %H:%M:%S"))  # Format personnalisé
print(dt.isoformat())                     # Format avec la norme
```

## Affichage d'une date

Dans ce cas, nous voyons comment affecter une date pour qu'il nous retourne notre choix. Nous spécifions alors les composantes suivantes année, mois, jour. Il est idéal quand nous n'avons pas à gérer des heures. 
```python
#Demandons lui de nous afficher la date du 2024-2-11
t = datetime.date(2024, 2, 1)
print(t)
```
![02](https://github.com/pitalain/Tutoriel/assets/132237358/cf8345f9-7423-4bd8-9a37-ec0ed3d3784b)

![03](https://github.com/pitalain/Tutoriel/assets/132237358/89d76f8d-f468-4713-9bb3-0286ecf1a014)

Nous voyons ici qu'on a utilisé la classe date pour avoir une date spécifique.

Note: Pour le mois et le jour, assurons nous de ne pas marquer le chiffre 0 devant le deuxième chiffre.
- Par exemple, pour dire le mois de juillet: 7 et non 07.
- Pour le jour 7, mettre 7 au lieu de 07

 ## Manipulation des heures
 
  Comme c'est le cas pour la date, nous pouvons afficher l'heure entière avec les composantes suivantes (heure, minutes et secondes). Comme pour les dates, vous pouvez également faire le formatage
  en l'affichant dans le format que vous voulez. Parfois, on veut travailler avvec des dates ou des heures. 

  ```python
  # Affichage d'une heure spécifique avec tous ses détails
  h = datetime.time(11, 19, 52)
  print(h)
```

## Calcul avec les dates en durée 

Pour tout projet dans le monde des affaires, la date et les heures ne nous donne pas des informations pertinentes. Nous avons besoin de faire des calculs pour savoir un intervalle de temps ou une durée.
Pour les durées, le module Python datetime datetime comprend la classe datetime.timedelta.

Un objet timedelta est crée automatiquement lorsqu'on soustrait deux dates, deux heures afin de déterminer la durée entre les deux données. Par exemple, dans ce cas, stockons le jour de l'an et la date du jour.  On doit créer trois variables pour pouvoir stocker la différence qu'on obtient en soustrayant la date la plus ancienne à la date la plus récente.

Insertion de timedelta

 ```python
# Importation de la classe timedelta
from datetime import timedelta
```

  ```python
#Calcul de différence de date
jour_an = datetime.date(2024,1,1)
annif = datetime.date(2024,10,10)
intervalle  = annif - jour_an
print(intervalle)
```
En exécutant le code on obtient en sortie: 283 days.
Il y'a 283 jours entre ces deux dates et nous n'avons pas spécifié d'heures de jour dans ces date, elles sont simplement initialisés à 0. Le calcul de timedelta est généré automatiquement lorsqu'on soustrait une date 
à une autre pour obtenir la durée entre ces deux dates.

## Exercice récapitulatif 

Dans l'exemple ci-dessous un cas complet ou on calcule l'âge en années et en mois à partir d'un timedelta.

  ```python
#Calcul de l'âge en années et en mois
#c'est la date du jour que donne l'ordinateur
auj = datetime.date.today()
#date de naissance exprimée en année, mois, jour
date_naissance = datetime.date(2000,11,5)
#durée entr les deux dates sous la formne d'un objet timedelta'
age = auj - date_naissance
#durée entre les deux dates exprimé en jours
jours = age.days
#déterminons le nombre d'années
annees = jours // 365
#Le nombre de jours restant est le modulo de la division par 365
#En divisant le nombre par 30, on obtient un nombre de mois approximatif
mois = (jours % 365) // 30
#Affichage du résultat
print(f"Vous êtes agé de  {annees} ans et {mois} mois")
```
Comme sortie, elle nous retourne: Vous êtes agé de  23 ans et 3 mois

## Utilisation d'une fonction

  ```python
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_date = datetime.date(1990, 5, 17)
print("Age:", calculate_age(birth_date))
```
En sortie, nous avons comme résultat: Age: 33 ans 
 
La fonction calculate_age détermine l'âge d'une personne en fonction de sa date de naissance. Elle prend en argument la date de naissance au format date. En se basant sur la date actuelle obtenue avec datetime.date.today(), elle compare les années et les mois/jours de naissance pour savoir si l'anniversaire est déjà passé cette année. Puis, elle soustrait l'année de naissance de l'année actuelle, ajustant si nécessaire si l'anniversaire n'est pas encore survenu. Enfin, elle renvoie l'âge calculé en années.

## Conversion de chaînes de caractères en objets datetime

  ```python
# Conversion de chaînes de caractères en objets datetime
date_s = "2024-02-12"
pd = datetime.datetime.strptime(date_s, "%Y-%m-%d")
print(pd)
```
En sortie, on a le résultat: 2024-02-12 00:00:00

Ce code accomplit la conversion d'une chaîne de caractères représentant une date au format "YYYY-MM-DD" en un objet datetime. Initialement, une variable date_str est définie, contenant la date "2023-12-25". Ensuite, la méthode strptime() de la classe datetime.datetime est invoquée, permettant la transformation de cette chaîne en un objet datetime. Le format spécifié dans la méthode est "%Y-%m-%d", correspondant à l'année, au mois et au jour respectivement. Le résultat de cette opération est assigné à la variable parsed_date. Pour finir, la date convertie est affichée à l'aide de la fonction print(). Par conséquent, ce code offre la possibilité de convertir une chaîne de caractères dépeignant une date en un objet datetime, qui se prête ensuite à diverses manipulations ou utilisations dans des opérations de date et d'heure ultérieures.

## Fuseaux horaires 

Dans ce tutoriel, nous allons explorer le concpet des fuseaux horaires sans entrer en profondeur. 
Il existe deux tpes d'objets datetime. L'objet datetime naif qui est pour toute date et heure qui ne comporte pas d'informations la reliant à un fuseau horaire spécifique et l'objet datetime avisé qui pour toute date et heure comprend des informations sur le fuseau horaire. Lorsqu' on récupère l'heure à partir de l'horloge, elle correspond à celle de votre 
fuseau horaire, mais il n'y a aucune indication de quel fuseau horaire il s'agit. Vous pouvez cependant obtenir la différence entre votre fuseau et le temps UTC en comparant now(). 
Bien que le module datetime ne supporte pas nativement la gestion des fuseaux horaires, le module pytz offre cette fonctionnalité supplémentaire. Pour illustrer, voici un exemple qui démontre la création d'un objet datetime en spécifiant un fuseau horaire. En utilisant pytz, il devient possible d'instancier un objet datetime avec une référence à un fuseau horaire précis, permettant ainsi une manipulation précise des dates et heures dans différents contextes temporels. Ils utilisent une base de donnees appelles tz database [Base de données tz](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). C'est une base de données universelle qui permet de representer différents fuseaux horaire dans le monde. 

Ci-joint un exercice récapitulatif des fuseaux horaires

  ```python
#Cas récapitulatif des fuseaux horaires
#on réimporte le module pour une facilitation du code
from datetime import datetime
#création d'un objet datetime now
now = datetime.now()
#On peut afficher les informations du fuseau horaire avec l'attribut tzinfo qui est un raccourci pour le fuseau horaire'
now.tzinfo
#En affichant le now.tzinfo cela ne me retourne rien et pour avoir un résultat il faut l'afficher avec un print
print(now.tzinfo)
#Il nous retourne en sortie None ce qui veut dire qu'on n'a pas d('informations sur le fuseau horaire '
#Pour avoir des informations sur le fuseau horaire on peut importer la classe zoneinfo
from zoneinfo import ZoneInfo
#Affichons ici le fuseau horaire de New York
f_v = datetime.now(tz=ZoneInfo("America/New_York"))
print(("L'heure actuelle de New York: ", f_v))
#Affichage du fuseau horaire sous un format de chaine formatée
print(f"UTC offset de New York: {f_v.utcoffset()}")
#Vous pourriez rencontrer des problèmes d'exécution de Python inférieure à 3.9
# Obtention de la date et l'heure actuelles dans le fuseau horaire de Los Angeles
fus_losAnge = datetime.now(tz=ZoneInfo("America/Los_Angeles"))
print("Heure actuelle à Los Angeles:", fus_losAnge)
# Calcul de la différence entre les deux fuseaux horaires de New York et de Los Angeles
diff_result = f_v - fus_losAnge
print("La différence de temps entre New York et Los Angeles est de:", diff_result)
```
## Limites et prochaines étapes
Ce tutoriel aborde les principes fondamentaux de DateTime, mais n'explique pas les fonctionnalités avancées ou les cas d'utilisation complexes. Il pourrait manquer d'exemples pratiques où la manipulation de dates est essentielle, comme dans l'analyse financière ou météorologique. Les étapes suivantes impliquent une meilleure compréhension de la gestion des fuseaux horaires, la manipulation de formats de date personnalisés, et l'adoption de bonnes pratiques pour garantir la sécurité des applications traitant des données temporelles. Ces notions pourront être abordées et sont utiles pour des projets en gestion.

## Transfert des connaissances

Ce module datetime permet de concevoir une application permettant à l'utilisateur de planifier des événements dans un calendrier. Ce même module peut également être employé pour calculer des délais et des échéances dans divers contextes, tels que la gestion de projet ou la planification de tâches, incluant des fonctionnalités telles que le calcul du nombre de jours avant une date d'échéance donnée. En outre, le module datetime offre des capacités pour gérer les conversions entre différents fuseaux horaires. En démontrant ces fonctionnalités dans divers scénarios, vous pouvez aider à illustrer de manière efficace la polyvalence et l'application pratique du module datetime, facilitant ainsi une meilleure compréhension de son utilisation et de son fonctionnement.

## Conclusion  

Ce tutoriel a été une expérience extrêmement enrichissante pour moi, m'offrant une compréhension étendue du langage Python à travers une diversité de domaines. En mettant l'accent sur le module datetime, il a permis une exploration approfondie de cet outil crucial, essentiel dans l'analyse des données d'entreprise. Il a clairement mis en évidence l'importance vitale des dates dans ces analyses, soulignant la nécessité absolue de maîtriser les multiples facettes de leur manipulation pour exécuter diverses tâches avec exactitude. Ce tutoriel m'a permis d'acquérir des compétences pratiques et théoriques dans la gestion des dates, renforçant ainsi ma capacité à travailler efficacement dans des projets Python impliquant des aspects temporels. Bref, en comprenant les concepts de base et en explorant ses fonctionnalités avancées, nous pouvons gérer efficacement les aspects temporels de vos applications Python. 



## Références bibliographiques

- https://www.youtube.com/watch?v=GzhG26cvmNg&t=541s
- https://docs.python.org/fr/3.6/library/datetime.html#datetime-objects
- https://www.youtube.com/watch?v=r1Iv4d6CO2Q
- Utilisation de chatgpt
