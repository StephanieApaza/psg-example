# Conversión a días, horas, minutos y segundos

# Cantidad de segundos totales
segundos = 288325

# Calculo de segundos a días
dias = segundos // 86400
tiempo_restante = segundos % 86400

# Calculo de segundos restantes a horas
horas = tiempo_restante // 3600
tiempo_restante = tiempo_restante % 3600

# Calculo de segundos restantes a minutos
minutos = tiempo_restante // 60

# Calculo de segundos restantes finales
segundos_rest = tiempo_restante % 60

# Resultado
print("Dias: ", dias)
print("Horas: ", horas)
print("Minutos: ", minutos)
print("Segundos: ", segundos_rest)