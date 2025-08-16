# Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado

def calculo_operacion(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "No se puede dividir entre cero."
        return num1 / num2
    else:
        return "La operación no es válida."
        
resultado = calculo_operacion(25, 0, "/")
print(f"El resultado de la operación es: {resultado}")