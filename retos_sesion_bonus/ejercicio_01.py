# Programa que cuenta la cantidad de frutas que aparecen en una lista y las guarda en un diccionario

frutas = ['🍅','🍇','🍈','🍉','🍊','🍌','🍍','🍌','🍊','🍉','🍈','🍇','🍅','🍅','🍇']

# Función para contar las frutas
def contar_frutas(lista_frutas):
    contador = {}
    for fruta in frutas: # Corrección del nombre lista_frutas por frutas
        if fruta in contador:
            contador[fruta] += 1
        else:
            contador[fruta] = 1 # Corrección de 0 por 1 para la primera vez que se cuenta una fruta
    return contador

# Función para imprimir el conteo de frutas
def imprimir_conteo(conteo):
    for fruta, cantidad in conteo.items(): # Agregar .items() debido a que se esta realizando el conteo en un diccionario
        print(f"Hay {cantidad} {fruta}(s).")

# Llamando a las funciones
conteo_frutas = contar_frutas(frutas)
imprimir_conteo(conteo_frutas)