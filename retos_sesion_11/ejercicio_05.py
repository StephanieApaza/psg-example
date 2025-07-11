# Eres NOE y tienes que guardar dos animales de cada especie en un arca
arca_noe = {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}

# Añadiendo al arca 3 especies más
arca_noe.update({'🦜': 2, '🐢': 2, '🐻': 2})
print("Arca de Noé después de haber añadido tres especies:", arca_noe)

# Tomando lista de los animales en el arca iterando el diccionario
print("Tomando lista de cuantos animales hay por especie en el Arca:")
lista_animales = iter(arca_noe.items())
perro = next(lista_animales)
print(perro)
gato = next(lista_animales)
print(gato)
tigre = next(lista_animales)
print(tigre)
mono = next(lista_animales)
print(mono)
unicornio = next(lista_animales)
print(unicornio)
jirafa = next(lista_animales)
print(jirafa)
loro = next(lista_animales)
print(loro)
tortuga = next(lista_animales)
print(tortuga)
oso = next(lista_animales)
print(oso)

# Verificando si existe la especie dragon
print("¿Existe en el arca la especie 'dragon'?: ", '🐲' in arca_noe)

# Eliminando la especie unicornio del arca
del arca_noe['🦄']
print("Arca de Noé después de haber verificado que no existen unicornios: ", arca_noe)

# Modificando el valor de la especie jirafa por 2
arca_noe['🦒'] = 2
print("Arca de Noé después de haber aumentado un ejemplar en la especie jirafa: ", arca_noe)

# Después del diluvio
arca_noe.clear()
print("El arca de Noé despúes del diluvio: ", arca_noe)