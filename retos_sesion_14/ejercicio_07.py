# Tres en Raya

tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Función para mostrar el tablero del juego
def mostrar_tablero(tres_raya):
    print("   1   2   3")
    print("--------------")
    for i, fila in enumerate(tres_raya):
        print(f"{i + 1}| " + " | ".join(fila) + " |")
        print("--------------")

# Función para realizar una jugada
def realizar_jugada(jugador):
    while True:
        print(f"\nEs el turno del {jugador}.")
        fila = int(input("Elige la fila (1, 2, 3): ")) -1
        col = int(input("Elige la columna (1, 2, 3): ")) -1
        # Verificando si la posición es válida
        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador
            break
        else:
            print("La casilla está ocupada, intenta otra jugada.")

# Función para verificar si alguien ganó
def verificar_ganador(jugador):
    # Lista de combinaciones posibles para ganar
    combinaciones = [   
        # Filas
        [tablero[0][0], tablero[0][1], tablero[0][2]],
        [tablero[1][0], tablero[1][1], tablero[1][2]],
        [tablero[2][0], tablero[2][1], tablero[2][2]],
        # Columnas
        [tablero[0][0], tablero[1][0], tablero[2][0]],
        [tablero[0][1], tablero[1][1], tablero[2][1]],
        [tablero[0][2], tablero[1][2], tablero[2][2]],
        # Diagonales
        [tablero[0][0], tablero[1][1], tablero[2][2]],
        [tablero[0][2], tablero[1][1], tablero[2][0]]]
    # Verificando si alguna de las combinaciones tiene 3 símbolos iguales (X ó O)
    for linea in combinaciones:
        if linea.count(jugador) == 3:
            return True
    return False

# Función para verificar el empate
def verificar_empate():
    # Hay empate si todas las casillas estan llenas
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False 
    return True

# Función del juego
def jugar():
    jugador = 'X'
    while True:
        mostrar_tablero(tablero)
        realizar_jugada(jugador)

        # Si hay ganador
        if verificar_ganador(jugador):
            mostrar_tablero(tablero)
            print(f"¡El jugador {jugador} es el ganador!")
            break
        # Si hay empate
        if verificar_empate():
            mostrar_tablero(tablero)
            print("¡Es un empate!")
            break
        # Cambiando de turno entre jugador 'X' y 'O'
        jugador = 'O' if jugador == 'X' else 'X'

# Ejecutando el juego
jugar()