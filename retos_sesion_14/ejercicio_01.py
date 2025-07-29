# Crea una funcion que reciba una lista de calificaciones y devuelva el promedio de las mismas.
# Las calificaciones son: 50, 75, 80, 91, 70

def calcular_promedio (calificaciones):
    promedio = sum(calificaciones)/len(calificaciones)
    return promedio
    
notas = [50, 75, 80, 91, 70]

promedio_notas = calcular_promedio(notas)
print(f"El promedio de las calificaciones es: {promedio_notas}")