# Conversión de 1000000 segundos a semanas, días, horas, minutos y segundos

# Cantidad de segundos totales
t_segundos = 1000000

# Cantidad de segundos por cada unidad de tiempo
s_minuto = 60
s_hora = 60 * 60
s_dia = 24 * 60 * 60
s_semana = 7 * 24 * 60 * 60

# Calculo de cuantas semanas hay en 1000000 segundos
semanas = t_segundos // s_semana
resto = t_segundos % s_semana

# Calculo de cuantos días hay en el resto de segundos
dias = resto // s_dia
resto = resto % s_dia

# Calculo de cuantas horas hay en el resto de segundos
horas = resto // s_hora
resto = resto % s_hora

# Calculo de cuantos minutos hay en el resto de segundos
minutos = resto // s_minuto
segundos = resto % s_minuto

# Resultado
print("1000000 segundos equivalen a:")
print(semanas, "semanas")
print(dias, "días")
print(horas, "horas")
print(minutos, "minutos")
print(segundos, "segundos")