# FOR
print ("Inicio")
for i in range(5): # rango (0,5,1)
    print(i)
print ("Fin")

# Ejemplo 1, sumar los números del 1 al 10 de 2 en 2
print ("Ejemplo 1")
suma = 0
for i in range(1, 11, 2): # 1, 3, 5, 7, 9
    suma += i #suma += i
print(suma)

# Ejemplo 2, crear un árbol de navidad de 6 niveles

print ("Ejemplo 2")
for i in range(0, 6):
    print(" "*(5-i) + "*"*i*2+"*")

# Ejemplo 3, crear una serie de números cuadrados del 1 al 10

print ("Ejemplo 3")
for i in range(1, 11):
    print(i**2, end=" ")

# Ejemplo 4, crear una lista de números pares del 1 al 10

print ("Ejemplo 4")
pares = []
for i in range(0, 11, 2):
    pares.append(i)
print(pares)

# Imprimir los 10 primeros de la serie números cúbicos
for i in range(1,11):
    print(i ** 3, end=" ")

# For con estructuras
for fruta in ['🍎','🍌','🍇','🍉']:
    print(fruta)

print ("Ejemplo 5")
fiesta = ['🎄','🎆','🎁','🎊','✨','🧨']
for objeto in fiesta:
    print(objeto)

print ("Ejemplo 6")
frutas =  ('🍅','🍇','🍈','🍉','🍊')
for fruta in frutas:
    print(fruta, end=", ")

print ("Ejemplo 7")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
for clave in frutas:
    print(clave, frutas[clave])

# Ejemplo 8, imprimir los elementos del ciclo de vida de un pollo con flechas
print ("Ejemplo 8")
ciclo_vida = '🥚🐣🐥🐤🐔🍗'
for etapa in ciclo_vida:
    print(etapa, end="->")

print ("Ejemplo 9")
animales = ['🐶','🐱','🐰','🐭']
for animal in animales:
    print(animal)

# Ejemplo 10, Listar los elementos de la siguiente serie ['🐶','🐱','🐰','🐭']

print ("Ejemplo 10")
animales = ['🐶','🐱','🐰','🐭']
for i in range(len(animales)):
    print(animales[i])

animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal, animales[i])

print ("Ejemplo 11")
frutas = {'🍅':'Tomate','🍇':'Uva','🍈':'Melón','🍉':'Sandía','🍊':'Naranja'}
print (list(enumerate(frutas)))
for i, fruta in enumerate(frutas):
    print(i, fruta, frutas[fruta])

# Ejercicio 2
deportes = '⚽🏀🏐🎱'

for i, deporte in enumerate(deportes):
    print(deporte * (i + 1))

# WHILE
# Ejemplo 12, imprimir los números mientras sean menores o igual a 5 empezando desde 0

print ("Ejemplo 12")
i = 0
while i <= 5:
    print(i)
    i += 1
print("Fin")

print ("Ejemplo 13")
suma = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print(suma)

# Ejercicio
numero_1 = int(input("Ingresa un número: "))
while numero_1 >= 0:
    print(numero_1)
    numero_1 -= 1
print("Fin")

# Ejemplo 14, De la siguiente lista de frutas imprimir los elementos hasta que se encuentre un gusano 🐛 con for

frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta)
print ("Fin")


frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
print ("Ejemplo 14")
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i)
print ("Fin")


print ("Ejemplo 15")
contador = 0
while True:
    print(contador)
    contador += 1

# Ejemplo 16, Crear un ciclo infinito que pida una cadena de texto la ponga en mayúsculas y la 
# imprima hasta que se ingrese la palabra salir
print ("Ejemplo 16")
while True:
    texto = input("Ingrese un texto: ")
    if texto == 'salir':
        break
    print(texto.upper())
print ("Fin")

# Ejercicio 4, Crear un ciclo infinito que reciba un número por teclado y verifique si es par o impar hasta que se ingrese el número 0
print ("Ejercicio 4")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print ("Par" if numero % 2 == 0 else "Impar")

# ESTRUCTURA DE UNA LISTA POR COMPRENSIÓN
# Ejemplo 17, Crear una lista de los números pares del 2 al 10
print ("Ejemplo 17")
pares = [i for i in range(2, 11, 2)]
print(pares)

# Ejemplo 18, Crear una lista de los números pares del 2 al 10 con condicional
print ("Ejemplo 18")
pares = [i for i in range(2, 11) if i % 2 == 0]
print(pares)

# Ejemplo 19, Crear un diccionario números 2 al 10 donde si es par vale "Par" y si es impar valga "Impar"

print ("Ejemplo 19")
pares = {i: "Par" if i % 2 == 0 else "Impar" for i in range(2, 11)}
print(pares)

# Crear una tupla de los números impares del 1 al 10 usando una tupla por comprensión
print ("Ejercicio 5")
impares = tuple(i for i in range(1, 11) if i % 2 != 0)
print(impares)

# Ejemplo 20, Imprimir las tablas de multiplicar del 1 y 2
print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

#Ejemplo 21, Introducir un número por teclado y crear una tabla de multiplicar de ese número del 1 al 10, 
# si se ingresa 0 termina el programa
print ("Ejemplo 21")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    print(f"Tabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
print ("Fin")

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()

# Ejemplo 22, Introducir un número por teclado y crear una matriz nxn con la letra X
print ("Ejemplo 22")
n = int(input("Ingrese un número: "))
matriz = [['X' for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)

# Ejercicio
# Crear una matriz ingresando un número por teclado para el tamaño de la matriz y en cada posición colocar una tupla con (i, j)

print ("Ejercicio 6")
n = int(input("Ingrese un número: "))
matriz = [[(j, i) for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)

# Crear una matriz ingresando un número por teclado para el tamaño de la matriz y en cada posición colocar una tupla con (i, j)
print ("Ejercicio 6")
n = int(input("Ingrese un número: "))
matriz = [[(j, i) for i in range(n)] for j in range(n)]
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()
print (matriz)
