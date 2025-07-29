# Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado

def calculo_operacion(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
        
resultado = calculo_operacion(25, 15, "*")
print(f"El resultado de la operación es: {resultado}")