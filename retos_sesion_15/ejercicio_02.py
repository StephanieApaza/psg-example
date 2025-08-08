# Crea un programa que permita construir una canasta de frutas solicitando ingresar frutas por teclado

class FrutaNoPermitida(Exception):
    pass

frutas_permitidas = ['🍅', '🍇', '🍈', '🍉', '🍊','🍌', '🍍', '🍑']
canasta_frutas = []

while True:
    try:
        fruta = input("Ingresa el emoji de una fruta (o escribe 'salir' para terminar): ")
        if fruta == 'salir':
            break
        if fruta not in frutas_permitidas:
            raise FrutaNoPermitida("La fruta ingresada no es válida.")
        canasta_frutas.append(fruta)
    except FrutaNoPermitida as e:
        print("❌ !Error¡", e)

print("🧺 Canasta final de frutas: ", canasta_frutas)


