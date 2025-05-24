print("Tipos de datos booleanos")
print (True)
print (False)

# Operaciones aritméticas con booleanos
print (True + True)
print (True * True)
print (True * False)
print (False + False)
print (False * False)

print ("Números y booleanos")
print (10 + True)
print (10 + False)
print (10 * True)
print (10 * False)

print ("Declarar variables booleanas")
var_booleana = True
print (var_booleana)
print (type(var_booleana))
var_booleana = False
print (var_booleana)
print (type(var_booleana))

print ("Declarar mediante función bool()")
var_booleana = bool(1)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(0)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(-15)
print (var_booleana)
print (type(var_booleana))

print ("Operadores de comparación")
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
a = 10
b = 10
print (a is b)
print (a is not b)

print ("Asignación de variables")
x = 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10)
print(type(mayor_que_cero))

print ("Operadores lógicos")
print (True and True)
print (True and False)
print (False or True)
print (False or False)
print (not True)
print (not False)

print("Operadores lógicos y prioridad")
print(False and False or True)
print(False and (False or True))
print(not True and False or True)
print(not (True and False or False))
print(not True and (False or False))
print(not True and False or False)

print("Operador AND")
print(True and True)
print(False and True)
print(True and False)
print(False and False)

print ("Operador OR")
print (True or True)
print (True or False)
print (False or True)
print (False or False)

print ("Operador OR")
print (10 != 0 or 10 != 0)
print (10 != 0 or 3 + 5 > 10)
print (3 + 5 > 10 or 0 != 0)
print (3 + 5 > 10 or 3 + 5 > 10)

print ("Ejemplo de uso Sensor y Batería")
sensor = True
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)

# Determinar si el número 20 está en el rango de 0 a 100
a = 20
print(a >= 0 and a <= 100)

# Un estudiante obtuvo las siguientes notas en sus examenes: 15, 20, 16 determinar si el estudiante aprobó con una nota superior a 50
examen_1 = 15
examen_2 = 20
examen_3 = 16
nota_aprobacion = 50
suma_notas = examen_1 + examen_2 + examen_3
print(suma_notas > nota_aprobacion)

# Reto 3
numero = 15
divisible_tres = numero % 3 == 0
divisible_cinco = numero % 5 == 0
divisible_dos = numero % 2 != 0
resultado = (divisible_tres and divisible_cinco) and divisible_dos
print(resultado)

print("Cortocircuito con operador and")
x = 3 + 5 
y = 0
print(x < 2 and (x / y) > 2)
print(x > 0 and (x / y) > 0)

print("Cortocircuito con operador or")
x = 1
y = 0
print (x > 0 or (x/y) > 0)
print (x > 2 or (x/y) > 2)