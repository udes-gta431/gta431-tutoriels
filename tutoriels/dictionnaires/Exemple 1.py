
## Exemple sur la manipulation des données en Python : Tri, accès et manipulation de dictionnaires

ventes = {'janvier': 1500, 'février': 2200, 'mars': 1800, 'avril': 2500, 'mai': 2000}

if __name__ == "__main__":
    # Fonction sorted()
    print(sorted(ventes))

    # Extraire les valeurs
    print(ventes.items())

    # Tri par clé
    ventes_triées = dict(sorted(ventes.items()))
    print(ventes_triées)

    # Tri par valeur
    ventes_triées = dict(sorted(ventes.items(), key=lambda item: item[1]))
    print(ventes_triées)

    # Accès à la liste des clés et des valeurs
    clés = ventes.keys()
    valeurs = ventes.values()
    print("Clés :", clés)
    print("Valeurs :", valeurs)

