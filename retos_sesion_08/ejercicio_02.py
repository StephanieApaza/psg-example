# Crea una tupla e imprime los resultados

abecedario = ('a','b','c','d','e','f','g','h','i','j')

# Imprime el primer elemento
elemento_1 = abecedario[0]
print("primer elemento: ", elemento_1)

# Imprime el último elemento
elemento_2 = abecedario[-1]
print("Último elemento: ", elemento_2)

# Imprime un slice del índice 3 al 5
elemento_3 = abecedario[3:6]
print("Slice del índice 3 al 5:" ,elemento_3)

# Imprime un slice del 5 al 9 con pasos de 3
elemento_4 = abecedario[5:10:3]
print("Slice del índice 5 al 9 con pasos de 3: ",elemento_4)

# Imprime un slice del 9 al 0 con pasos de -2
elemento_5 = abecedario[9:0:-2]
print("Slice del índice 9 al 0 con pasos de -2: ",elemento_5)