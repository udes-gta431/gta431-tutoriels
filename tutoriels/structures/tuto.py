# Nom du fichier : tuto.py
# Auteur : Sara Blekadi, cip: BELS2569, courriel:bels2569@usherbrooke.ca
# Date de création : 2024-02-07
# Description : tutoriel sur comment concaténer les liste, les dictionnaires.

#Section d'importation des modules

# Variables globales

# Liste de ventes de 2021
monthly_sales_2021 = [150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 375000, 400000, 425000]
# Liste de vente de 2022
monthly_sales_2022 = [160000, 185000, 210000, 235000, 260000, 285000, 310000, 335000, 360000, 385000, 410000, 435000]
# Liste de vente de 2023
monthly_sales_2023 = [170000, 195000, 220000, 245000, 270000, 295000, 320000, 345000, 370000, 395000, 420000, 445000]

# Fonctions personnalisées

# Programme principal
if __name__ == "__main__":
 # Liste des trois années de ventes
 last_3_years_monthly_sales = monthly_sales_2021 + monthly_sales_2022 + monthly_sales_2023;
 print("les ventes des trois dernières années concaténées sont :", (last_3_years_monthly_sales))
 totale_des_ventes = sum(last_3_years_monthly_sales)
print("les ventes des trois dernières années sont :", (totale_des_ventes))


#Découpage de l'année 2023 en quatre parties
quarter1_2023 = monthly_sales_2023[0:3]
quarter2_2023 = monthly_sales_2023[3:6]
quarter3_2023 = monthly_sales_2023[6:9]
quarter4_2023 = monthly_sales_2023[9:12]

# la somme de vente pour chaque quatre mois:
print("La somme du premier quart  est :", sum(quarter1_2023))
print("La somme du deuxième quart est :", sum(quarter2_2023))
print("La somme du troisième quart est :", sum(quarter3_2023))
print("La somme du quatrième quart est :", sum(quarter4_2023))

# Les dépenses de l'année 2023
monthly_costs_2023 = [55000, 100000, 70000, 60000, 75000, 80000, 70000, 75000, 80000, 85000, 90000, 60000]

# profit de chaque mois

monthly_profits_2023 = [];
for i in range(12):
    profit = monthly_sales_2023[i] - monthly_costs_2023[i]
    monthly_profits_2023 += [profit]
print("les profits de chaque mois sont ",monthly_profits_2023)
# le mois où il y a le plus bas profit
min_profit = min(monthly_profits_2023)
print("le plus bas profit est : ",min_profit)
# Resultat est 1 ==> Fevrier
index_min_profit = monthly_profits_2023.index(min_profit)
print("index de mois est :",index_min_profit)
print("Il s'agit du mois de fevrier")




#Autre methode pour avoir le minimum :on va trier et afficher le minimum
monthly_profits_2023.sort();
print("les profits 2023 en ordre croissant",monthly_profits_2023)
# Smallest profit fevrier
print("le plus bas profit",monthly_profits_2023[0])

# Dictionnaire de l'année 2021 des ventes
monthly_sales_2021_dict = {'January': 150000, 'February': 175000, 'March': 200000, 'April': 225000, 'May': 250000, 'June': 275000, 'July': 300000, 'August': 325000, 'September': 350000, 'October': 375000, 'November': 400000, 'December': 425000}
print("les ventes de 2021",monthly_sales_2021_dict)
# Dictionnaire de l'année 2022 des ventes
monthly_sales_2022_dict = {'January': 160000, 'February': 185000, 'March': 210000, 'April': 235000, 'May': 260000, 'June': 285000, 'July': 310000, 'August': 335000, 'September': 360000, 'October': 385000, 'November': 410000, 'December': 435000}
print("les ventes de 2022",monthly_sales_2022_dict)
# Dictionnaire de l'année 2023 des ventes
monthly_sales_2023_dict = {'January': 170000, 'February': 195000, 'March': 220000, 'April': 245000, 'May': 270000, 'June': 295000, 'July': 320000, 'August': 345000, 'September': 370000, 'October': 395000, 'November': 420000, 'December': 445000}
print("les ventes de 2023",monthly_sales_2023_dict)

# Dictionnaire des trois années des ventes
last_3_years_sales_dict = {
    2021: monthly_sales_2021_dict,
    2022: monthly_sales_2022_dict,
    2023: monthly_sales_2023_dict
}

print("les ventes des 3 dernieres années",last_3_years_sales_dict)

# exemple de nouvelle année 2024
monthly_sales_2024_dict = {'January': 180000, 'February': 205000, 'March': 230000, 'April': 255000, 'May': 280000, 'June': 305000, 'July': 330000, 'August': 355000, 'September': 380000, 'October': 405000, 'November': 430000, 'December': 455000}

# Maintenant on va l'ajouter aux autres années pour afficher les quatre:
last_4_years_sales_dict = last_3_years_sales_dict | { 2024 : monthly_sales_2024_dict }

print("les ventes des 4 dernieres années",last_4_years_sales_dict)


