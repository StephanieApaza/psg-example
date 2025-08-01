# Tres en Raya

# Variables globales
tablero = [[" " for _ in range(3)] for _ in range(3)]
turno_actual = 'X'
juego_terminado = False

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print(fila)

# Función para verificar el jugador ganador
def verificar_ganador():
    
    for i in range(3):
        # En filas y columnas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    # En diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False

# Función para verificar el empate
def verificar_empate():
    for fila in tablero:
        if " " in fila:
            return False
    return True

# Función del juego    
def tres_en_raya(jugador, fila, columna):
    # variables globales
    global tablero, turno_actual, juego_terminado

    if juego_terminado:
        print("El juego ha terminado. Reinicia para comenzar de nuevo.")
        return
    if jugador != turno_actual:
        print(f"No es el turno de {jugador}. Le toca a '{turno_actual}'.")
        return
    # Verificando si la casilla esta vacía
    if tablero[fila][columna] != " ":
        print("Casilla ocupada. Realiza otra jugada.")
        return
    
    # Colocar la jugada
    tablero[fila][columna] = jugador
    mostrar_tablero()
    # Verificando el ganador
    if verificar_ganador():
        print(f"¡El jugador {jugador} ha ganado!")
        juego_terminado = True
        return
    # Verificando si hubo empate
    if verificar_empate():
        print("Empate.")
        juego_terminado = True
        return
    # Para cambiar de turno
    turno_actual = 'O' if jugador == 'X' else 'X'
    print(f"Juega {turno_actual}.")


tres_en_raya('X', 0, 0)
tres_en_raya('O', 1, 0)
tres_en_raya('X', 1, 1)
tres_en_raya('O', 2, 2)
tres_en_raya('X', 0, 2)
tres_en_raya('O', 2, 0)
tres_en_raya('X', 0, 1)
