# Crear una función que reciba una lista de números y devuelva una lista con los números pares y otra lista con los números impares

def lista_numeros(numeros):
    numeros_pares = [num for num in numeros if num % 2 == 0]
    numeros_impares = [num for num in numeros if num % 2 != 0]
    return numeros_pares, numeros_impares


lista = [24,67,25,74,1,8,4,28,31,93]
numeros_pares, numeros_impares = lista_numeros(lista)
print("Números pares: ", numeros_pares)
print("Números impares: ", numeros_impares)

