# Calculadora interactiva que solicita dos números por teclado y realice las operaciones de suma, resta, multiplicación y división.

print("Calculadora interactiva:")

while True:
    try:
        num1 = input("Escribe un número (o 'salir' para terminar): ").strip()
        if num1.lower() == "salir":
            break
        num2 = input("Escribe otro número (o 'salir' para terminar): ").strip()
        if num2.lower() == "salir":
            break

        num1 = float(num1)
        num2 = float(num2) 
        print("La suma es: ", num1 + num2)
        print("La resta es: ", num1 - num2)
        print("La multiplicación es: ", num1 * num2)
        print("La división es: ", num1 / num2)

    except ValueError:
        print("Error, no ingresaste un número válido.")
    except ZeroDivisionError as e:
        print("Error", e)
    except Exception as e:
        print("Error inesperado.", e)