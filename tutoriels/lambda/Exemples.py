#Exemple 1:

nombres = [1, 2, 3, 4, 5]
nombre_pairs = map(lambda x: x**2, nombres)
resultat1 = list(nombre_pairs)
print(resultat1)


#Exemple 2:

etudiants = [('Philippe', 27), ('Roger', 15), ('Anna', 33)]
tri_etudiants = sorted(etudiants, key=lambda x: x[1])
print(tri_etudiants)

#Exemple 3:

nombre = [1, 2, 3, 4, 5]
nombre_pairs = filter(lambda x: x % 2 == 0, nombre)
resultat2 = list(nombre_pairs)
print(resultat2)

#Exemple 4:

nombres = [1, 2, 3, 4, 5]
nombres_carre = [x**2 for x in nombres]
print(nombres_carre)