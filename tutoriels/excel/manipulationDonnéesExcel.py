import pandas as pd

# Lire les données du fichier Excel
listeClientsExcel = pd.read_excel("../clients.xlsx")
# Afficher les données
print(f"Données contenues dans le fichier Excel : \n {listeClientsExcel}\n")

# Créer une liste de femmes uniquement, ordonnée par leur âges
listeFemmesordonnée = listeClientsExcel[listeClientsExcel['Sexe'] == "femme"].sort_values("Âge")
# Afficher la liste de femmes ordonnée
print(f"Liste des femmes ordonnée par leur âge : \n{listeFemmesordonnée}\n")

# Créer une liste d'homme uniquement, ordonnée par leur âges
listeHommesordonnée = listeClientsExcel[listeClientsExcel['Sexe'] == "homme"].sort_values("Âge")
# Afficher la liste d'homme ordonnée
print(f"Liste des hommes ordonnée par leur âge : \n {listeHommesordonnée}\n")

# créer un objet avec les salaires moyen
data = {
    "Sexe": ["Femme", "Homme"],
    "Salaire moyen": [round(listeFemmesordonnée["Salaire"].mean(), 2), round(listeHommesordonnée["Salaire"].mean(), 2)]
}
# Transformer l'objet  de salaires moyen en tableau
salairesMoyen = pd.DataFrame(data)
# Afficher le tableau des salaires moyen
print(f"Tableau des salaires moyen : \n {salairesMoyen}")

# Écrire les résultats dans de nouvelles feuilles de calculs
with pd.ExcelWriter('../clients.xlsx', engine='openpyxl', mode='a') as writer:
    listeFemmesordonnée.to_excel(writer, sheet_name='Femmes', index=False)
    listeHommesordonnée.to_excel(writer, sheet_name='Hommes', index=False)
    salairesMoyen.to_excel(writer, sheet_name='Salaires moyen', index=False)


