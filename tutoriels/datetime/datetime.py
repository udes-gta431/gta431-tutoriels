# Nom du fichier : datetime
# Auteur : aiea2001@usherbrooke.ca
# Date de création : 20240214
# Description : Tutoriel sur le module datetime

# Section d'importation des modules
import datetime
from datetime import timedelta

# Variables globales

# Fonctions personnalisées

# Programme principal

# Obtenir la date et l'heure du jour premier exemple
# asd = datetime.datetime.today()
# print(asd)

# Obtenir la date et l'heure du jour premier exemple
# Ceci est un autre exemple nous permettant d'obtenir l'heure et la date actuelle du jour
exple = datetime.datetime.now()
print(exple)

# Affectation de la date, l'heure, les minutes et les secondes
aff = datetime.datetime(2019, 10, 7, 10, 9, 58)
print(aff)

#Affichage des composantes individuels des dates, d'heures, minutes
print(aff.year)      # Année
print(aff.month)     # Mois
print(aff.day)       # Jour
print(aff.hour)      # Heure
print(aff.minute)    # Minute
print(aff.second)    # Seconde

#Affichage de la date en uttilisant le formatage
print(f"{aff:%A, %d %B, %Y}")

#Affichage de la date au format JJ/MM/AAAA
exple = f"{aff:%d/%m/%Y}"
print(exple)


# Demandons lui de nous afficher la date du 2024-2-11
t = datetime.date(2024, 2, 1)
print(t)


# Affichage d'une heure spécifique avec tous ses détails
h = datetime.time(11, 19, 52)
print(h)



# Créer un objet datetime pour une date et une heure spécifiques
dt = datetime.datetime(2023, 5, 17, 12, 30, 15)
print(dt.year)

# Formater un objet datetime en chaîne de caractères
print(dt.strftime("%Y-%m-%d %H:%M:%S"))  # Format personnalisé
print(dt.isoformat())                     # Format avec la norme

#Calcul de différence de date
jour_an = datetime.date(2024,1,1)
annif = datetime.date(2024,10,10)
intervalle  = annif - jour_an
print(intervalle)

# Importation de la classe timedelta
from datetime import timedelta

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

#Utilisation d'une fonction pour le calcul
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Exemple d'utilisation
birth_date = datetime.date(1990, 5, 17)
print("Age:", calculate_age(birth_date))

# Conversion de chaînes de caractères en objets datetime
date_s = "2024-02-12"
pd = datetime.datetime.strptime(date_s, "%Y-%m-%d")
print(pd)

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

