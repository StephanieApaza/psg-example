# Utiliza un diccionario para almacenar información de un animal marino de un acuario, 
# registra información como especie, habitat, dieta, estado de salud, edad y en un set los nombre de los responsables de su cuidado

tortuga = {
    'especie': 'Tortuga verde',
    'habitat': 'Aguas tropicales del océano Pacífico',
    'dieta': 'Pastos marinos',
    'estado de salud': 'Óptimo',
    'edad': 35,
    'responsables de cuidado': {'Maria','Leandro','Graciela'}
}

print("Información de: Tortuga")
print("Especie: ", tortuga['especie'])
print("Habitat: ", tortuga['habitat'])
print("Dieta: ", tortuga['dieta'])
print("Estado de salud: ", tortuga['estado de salud'])
print("Edad: ", tortuga['edad'], "años")
print("Responsables de su cuidado: ", tortuga['responsables de cuidado'])