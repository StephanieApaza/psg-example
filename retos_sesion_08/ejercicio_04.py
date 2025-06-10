# Crear una tupla con las notas del estudiante
notas = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

# Calcula el promedio
suma_notas = sum(notas)
cantidad_notas = len(notas)

promedio = suma_notas/cantidad_notas

# Para aprobar el promedio debe ser >= 51
print("El promedio de las notas es: ",int(promedio))

aprobado = promedio >= 51
print("¿El estudiante aprobó?: ", aprobado)
