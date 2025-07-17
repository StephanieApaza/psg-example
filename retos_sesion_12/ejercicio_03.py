# Jhon colecciona autos a escala 1:64, tiene los siguientes autos
autos_Jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}

# Jess tambien colecciona autos a escala 1:64, tiene los siguientes autos
autos_Jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

# ¿Que autos tienen en común ambos coleccionistas?, ¿Cuáles son los autos en común?

print("Inicio de autos coleccionados en común:")
if autos_Jhon.isdisjoint(autos_Jess):
    print("Jhon y Jess no tienen autos en común coleccionados.")
else:
    autos_c = autos_Jhon.intersection(autos_Jess)
    print("Jhon y Jess tienen coleccionados: ")
    print(autos_c)
print("Fin")