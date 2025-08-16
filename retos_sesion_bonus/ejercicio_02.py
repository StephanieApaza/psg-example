# Juego de adivinanzas en el que el jugador tiene que adivinar un número entre 1 y 100

def obtener_aleatorio(numeros):
    return numeros.pop() # Para sacar un número aleatorio de la lista de números

def adivina(secreto):
        intentos = 0
        print ("¿Que número estoy pensando? (1-100)")
        while True:
            try:
                intento = int(input(f"Intento N° {intentos + 1}: "))
                # Condicional para que solo se pueda ingresar un número entre 1 y 100
                if intento < 0 or intento > 100:
                    print("Ingresa un número entre 1 y 100.")
                else:
                    if intento == secreto:
                        print ("¡Felicidades! Has adivinado el número!")
                        break
                    elif intento < secreto:
                        print ("El número es mayor.")
                    else:
                        print ("El número es menor.")
            except ValueError:
                print ("Por favor, ingresa un número válido.")
            finally:
                intentos += 1
        # Correción de {intentos * 10}        
        print (f"Has adivinado el número en {intentos} intentos.\n")

def jugar():
    print("¡Bienvenido al juego de adivinanzas del Python Study Group 2025!")
    print("=" * 63)
    nombre_jugador = input("¿Cuál es tu nombre?: ").strip()
    print(f"¡Bienvenido, {nombre_jugador}!")
    print("=" * 63)
    print()

    # Creando una lista dentro de la función jugar para que en cada intento se adivine diferentes números
    numeros = list(range(1, 101))

    while True:
        opcion = input("¿Quieres jugar? escribe 's' para jugar y 'n' para terminar el juego (s/n): ")
        # Si la letra ingresada es diferente a 's' minúscula el juego termina
        if opcion.lower() != 's':
            print("¡Gracias por participar!")
            print(f"🐍 Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")
            break

        secreto = obtener_aleatorio(numeros)
        adivina(secreto)

jugar()


