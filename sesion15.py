print ("Inicio Ejemplo 1")
#x = 1 / 0
#print (x)
print ("Fin Ejemplo 1")

print ("Inicio Ejemplo 1")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")


while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        print("Resultado:", num1 / num2)
    except Exception as e:
        print("💀 Error:", e)
    

print ("Inicio Ejemplo 2")
divisor = 0
try:
    x = 1 / divisor
    print (x)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 2")


calificaciones = [20,40,80,"A"]
suma = 0
try:
    for i in range(len(calificaciones)+1):
        suma += calificaciones[i] 
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except ZeroDivisionError as e:
    print("0️⃣ Error:", e, type(e))
except TypeError as e:
    print("🎭 Error:", e, type(e))
except Exception as e:
    print("💀 Error:", e, type(e))


print ("Inicio Ejemplo 4")
calificaciones = [20,40,80]
suma = 0
try:
    for i in range(len(calificaciones)):
        suma += calificaciones[i]
    promedio = suma / len(calificaciones)
    print("Promedio:", promedio)
except Exception as e:
    print("💀 Error:", e, type(e))
else:
    print ("🎉 Sin errores")
print ("Fin Ejemplo 4")


def division(num1, num2):
    return num1 / num2

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num1 = float(num1)
        num2 = float(num2)
        resultado = division(num1, num2)
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("Resultado: ",resultado)


print ("Inicio Ejemplo 5")
try:
    print("🔗 Ping...")
except Exception as e:
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")


print ("Inicio Ejemplo 6")
try:
    print("🔗 Ping...")
    raise Exception("Error de conexión") #Excepción genérica
except Exception as e: # Captura cualquier excepción
    print("💀 Error:", e)
else:
    print("🎉 Ping Exitoso")
finally:
    print("🔌 Cerrando conexión")


numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)

    except KeyboardInterrupt as error:
        print('🚫 Para salir escriba "salir" para detener la ejecución del programa.')
    except Exception as error:
        print("💀 Error:", error)
    else:
        print("Número agregado")
    finally:
        print("Suma:", sum(numeros))
        print(numeros)


print("Inicio Ejemplo 7")
def funcion():
    pass
funcion()
print("Fin Ejemplo 7")


#class MiError(Exception):
    #pass
#raise MiError("Mensaje de error")


print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass

frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e, type(e))
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")


class PalabraInvalida(Exception):
    pass

palabras = []
while True:
    palabra = input("Escribe una palabra: ")
    if palabra == 'salir':
        break
    try:
        if not palabra.isalpha():
            raise PalabraInvalida("Solo se permite carácteres alfabéticos.")
        palabras.append(palabra)
    except PalabraInvalida as e:
        print(f"error: {e}")
    except Exception as e:
        print("Error:", e)
    else:
        print("Palabra agregada")
    
print("Lista de palabras: ", palabras)

