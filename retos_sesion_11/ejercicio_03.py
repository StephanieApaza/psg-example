# Tupla de especies de animales
tupla_animales = (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))

# Diccionario a partir de la tupla de especies de animales
especies_animales  = dict(tupla_animales)

# Del diccionario obtén y elimina el valor de la clave 'aves'
especie_aves = especies_animales.pop('aves')
print("Los animales que pertenecen a la especie aves son:", especie_aves)
print("Diccionario de especies de animales:",especies_animales)

# Modifica el valor de la clave 'felino'
especies_animales['felino'] = '🐈'
print("Diccionario modificado: ", especies_animales)

# Cambia la clave canino por caninos y su valor 
especies_animales['caninos'] = especies_animales['canino']
del especies_animales['canino']

especies_animales['caninos'] = ['🐶','🐕']
print("Diccionario modifcado por la especie caninos: ", especies_animales)



