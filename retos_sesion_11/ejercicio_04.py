# Gestión de hábitats en peligro

habitats_peligro = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, 
                    "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}
}

# Actualizando el diccionario
habitats_peligro.update({
    "selva":{"especies":{"jaguar","gato andino"}},
    "altiplano":{"especies":{"condor andino","chinchilla"}}
})

# Verificando el habitat amazonas
print("¿Existe en el diccionario el habitat de amazonas?: ", "amazonas" in habitats_peligro )

# Agregando al habitat amazonas la especie anaconda con el método add
habitats_peligro["amazonas"]["especies"].add("anaconda")
print("El diccionario actualizado de hábitats en peligro es: ", habitats_peligro) 
