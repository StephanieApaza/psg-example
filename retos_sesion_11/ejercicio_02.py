# Crea un diccionario de alimentos y que animales domésticos lo consumen

alimentos = {
    'croquetas':['perro', 'gato'],
    'frutas':['hámster','perico']
}

# Añade al diccionario 4 alimentos más
alimentos.update(pescado = ['gato'], zanahoria = ['conejo'], semillas = ['canario'], verduras = ['tortuga','loro'])
print("El diccionario actualizado es: ", alimentos)

# Existe en el diccionario de alimentos la comida 'trigo'?
print("¿Existe en el diccionario la comida trigo?: ", 'trigo' in alimentos)

# Elimina la comida 'zanahoria' del diccionario de alimentos
print(f"Eliminando a quienes consumen zanahoria: {alimentos.pop('zanahoria')}")

print("El diccionario actualizado sin el alimento zanahoria es :", alimentos)