# Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene

def cantidad_vocales(cadena):
    vocales = sum([1 for letra in cadena if letra in "aeiou"])
    return vocales

cadena_usuario = input("Escribe una palabra o frase para contar sus vocales: ").strip().lower()
resultado = cantidad_vocales(cadena_usuario)
print(f"Existen {resultado} vocales.")
