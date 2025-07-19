print("Inicio de la calculadora")

datos = input("Escribe los números y una operación aritmética que deseas realizar, ejemplo (10, 5, +): ")
# Dividiendo los números y la operación ingresada
partes_datos = datos.split(",")
# Verificando que sean dos números y la operación
if len(partes_datos) == 3:
    num_1 = partes_datos[0].strip()
    num_2 = partes_datos[1].strip()
    operacion = partes_datos[2].strip()
    # Validando que no existen vacios
    if num_1 == "" or num_2 == "" or operacion == "":
        print("Error: No se permiten valores vaçios, intenta ingresar los datos de nuevo.")
    else:
        # Convirtiendo strings a float
        num_1 = float(num_1)
        num_2 = float(num_2)
        resultado = None
        # Determinando la operación a realizar
        if operacion == '+':
            resultado = num_1 + num_2
        elif operacion == '-':
            resultado = num_1 - num_2
        elif operacion == '*':
            resultado = num_1 * num_2
        elif operacion == '/':
            if num_2 != 0:
                resultado = num_1 / num_2
            else:
                print("Error: No se puede dividir entre 0, cambia el segundo número.")
        else:
            print("Error: Operación no válida, usa uno de estos operadores (+, -, *, /).")

        if resultado is not None:
            print(f"Operacion: {num_1}, {num_2}, {operacion}")
            print("-------------------------")
            print(f"Resultado: {resultado}")
else:
    print("Error: Formato incorrecto, Usa: num1, num2, operación")

print("Fin")