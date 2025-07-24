# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
print("Tablero de Ajedrez: ")
print()

for fila in range(8):
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            print('#', end = ' ')
        else:
            print('*', end = ' ')
    print( )