import pandas as pd

data = pd.read_csv("C:\\Users\\emman\\OneDrive\\Bureau\\donnees_customers.csv")

print(data)


print(data.shape)
print(data["CustFirstName"])
nom_filtre = 'Luke'  # Remplacez "John" par le nom que vous souhaitez filtrer
resultats_filtres = data[data['CustFirstName'] == nom_filtre]
print(resultats_filtres)


# Supposons que vous souhaitez modifier le nom "Jim" en "Jima"

# Utilisez l'indexation booléenne pour sélectionner les lignes où le nom est "John"
indices_a_modifier = data['CustFirstName'] == "Jim"

# Attribuez une nouvelle valeur au nom pour les lignes sélectionnées
data.loc[indices_a_modifier, 'CustFirstName'] = "Jima"

# Affichez le DataFrame pour vérifier les modifications
print(data)

# Supposons que vous souhaitiez modifier le numéro de téléphone pour le client avec l'index 0
index_client = 25

# Nouveau numéro de téléphone
nouveau_numero = "210 555-2312"

# Modifier le numéro de téléphone pour le client spécifique
data.loc[index_client, '210 555-2312'] = nouveau_numero

# Supprimer toutes les lignes où le nom est "Estella"
data = data.drop(data[data['CustFirstName'] == 'Estella'].index)

# Afficher le DataFrame après la suppression
print(data)
