# Comparar los número 44 y 98, 111 y 333 para comprobar si ambos son pares o impares

# Primer grupo
num_1 = 44
num_2 = 98
result_1 = num_1 % 2 == 0
result_2 = num_2 % 2 == 0
result_3 = num_1 % 2 != 0
result_4 = num_2 % 2 != 0
par = result_1 and result_2
impar = result_3 and result_4
misma_paridad = par or impar
print("¿44 y 98 tienen la misma paridad?: ", misma_paridad)
print("44 es par: ", result_1)
print("44 es impar: ", result_3)
print("98 es par: ", result_2)
print("98 es impar: ", result_4)

# Segundo grupo
num_3 = 111
num_4 = 333
result_5 = num_3 % 2 == 0
result_6 = num_4 % 2 == 0
result_7 = num_3 % 2 != 0
result_8 = num_4 % 2 != 0
misma_paridad_1 = (result_5 and result_6) or (result_7 and result_8)
print("¿111 y 333 tienen la misma paridad?: ", misma_paridad_1)
print("111 es par: ", result_5)
print("111 es impar: ", result_7)
print("333 es par: ", result_6)
print("333 es impar: ", result_8)
