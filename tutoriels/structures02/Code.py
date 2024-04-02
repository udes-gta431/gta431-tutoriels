#Création du tuple
Tuple = ("Client1","Client2","Client3","Client4")

#Création de la liste
Liste = ["Client1","Client2","Client3","Client4"]

#Modification d'un élément de la liste
Liste[0]="Client5"
#Afficher le résultat du changement
print(Liste)    #Affichera: ['Client5', 'Client2', 'Client3', 'Client4']

#Tentative de modification d'un élément du tuple
#Tuple[0]="Client5" #Cela va créer une erreur; TypeError: 'tuple' object
                        # does not support item assignment

#Ajout d'un élément dans la liste
Liste.append("Client6")
#Afficher le résultat de l'ajout
print(Liste)    #Affichera: ['Client5', 'Client2', 'Client3', 'Client4', 'Client6']

#Tentative d'ajout d'un élément dans le tuple
#Tuple.append("Client6") #Cela va encore créer une erreur; AttributeError: 'tuple' object
                            # has no attribute 'append'

# Accéder aux éléments dans la liste et le tuple
print("Éléments de la liste :", Liste[0])    # Affichera :Client5
print("Éléments du tuple :", Tuple[1])      # Affichera : Client2

#Exemple 1
# Création d'un dictionnaire qui contient les notes des étudiants
Notes = { ('Joany', 'Finance'):90,
          ('Eve', 'RH'):85,
          ('Jade', 'Marketing'):80}

# Avoir accès aux notes des étudiants
print("Note de Joany en Finance:", Notes[('Joany', 'Finance')])
#Affichera: 90

#Ajouter une nouvelle note
Notes[('Joany', 'RH')]=85
print("Note de Joany en RH:", Notes[('Joany', 'RH')])
#Affichera: 85

#Exemple 2
#Données sur les commandes des clients sous forme de tuple
#(Nom de client, Commande, Coût)
Commandes_des_clients = (("Joany", ["Stylo", "Cartable"],10),
             ('Eve',["Agenda", "Stylo"],15),
             ('Jade',["Agenda", "Surligneur", "Calculatrice"],20 ))

#Convertir les tuples en listes
Commandes_liste = [list(commande) for commande in Commandes_des_clients]

#Ajouter un nouvel article à la commande de Joany
Index_Joany = [i for i, (nom, _, _) in enumerate(Commandes_liste) if nom == "Joany"][0]
Commandes_liste[Index_Joany][1].append("Agenda")

# Afficher les commandes modifiées sous forme de listes
print("Commandes des clients sous forme de listes :")
for commande in Commandes_liste:
    print(commande)
# Affichera:
# ['Joany', ['Stylo', 'Cartable', 'Agenda'], 10]
# ['Eve', ['Agenda', 'Stylo'], 15]
# ['Jade', ['Agenda', 'Surligneur', 'Calculatrice'], 20]