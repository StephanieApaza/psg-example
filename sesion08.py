print ("Tupla de enteros")
enteros = (1,2,3,4,5,6)
print (enteros)
print (type(enteros))

print ("Tupla de cadenas")
cadenas = ("hola", "mundo", "desde", "python")
print (cadenas)
print (type(cadenas))

print ("Tupla Mixta") 
mixta = (1, "hola", True, 2.5)
print (mixta)
print (type(mixta))

print ("Tupla vacia")
vacia = ()
print (vacia)
print (type(vacia))

print ("Tupla de un solo elemento")
uno = (1,)
print (uno)
print (type(uno))

print ("Tupla utilizando la función tuple()")
constructor = tuple("hola")
print (constructor)
print (type(constructor))

print ("Indexado positivo de una tupla")
tupla = (1,2.0, "hola", True)
print (tupla[0], type(tupla[0]))
print (tupla[1], type(tupla[1]))
print (tupla[2], type(tupla[2]))
print (tupla[3], type(tupla[3]))

print ("Slicing de una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:5]
print (sub_tupla)
print (type(sub_tupla))

print ("Slicing de una tupla con saltos")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[0:10:2]
print (sub_tupla)
print (type(sub_tupla))

print ("Slicing de una tupla con saltos negativos")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[7:2:-2]
print (sub_tupla)
print (type(sub_tupla))

print ("Slicing para revertir una tupla")
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print (tupla)
sub_tupla = tupla[-1::-1]
print (sub_tupla)
print (type(sub_tupla))

print ("Concatenación de tuplas")
tupla1 = (1,2,3)
tupla2 = (4,5,6)
concatenar = tupla1 + tupla2
print (tupla1, tupla2)
print (concatenar)
print (type(concatenar))

print ("Repetición de tuplas")
tupla = (1,2,3)
repetir = tupla * 3
print (tupla)
print (repetir)
print (type(repetir))

print ("Asignación múltiple")
persona = ("Jhon", "Doe", 22, 1.75)
nombre, apellido, edad, estatura = persona
print (persona)
print (nombre)
print (apellido)
print (edad)
print (estatura)

print ("Asignación múltiple")
persona = ("Jhon", "Doe", "12374238", 22, 1.75)
nombre, apellido,ci, edad, estatura = persona
print (persona)
print (nombre)
print (apellido)
print (edad)
print (estatura)

print ("Método index(valor)")
tupla = (1,2.0, "hola", True)
print (tupla.index(2.0))
print (tupla.index("hola"))

print("Método count(valor)")
tupla = (1,2.0,"hola",False,"hola","HOLA")
print(tupla.count(1))
print(tupla.count("hola"))
print(tupla.count(10))

print ("Función len()")
tupla = (1,2.0, "hola", True)
longitud = len(tupla)
print (tupla)
print (longitud)

print ("Función max()")
tupla = (1,2,10,5,8,0)
maximo = max(tupla)
print (tupla)
print (maximo)

print ("Función min()")
tupla = ("a","z","c","b","f","d")
minimo = min(tupla)
print (tupla)
print (minimo)

print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla)
print (tupla, type(tupla))
print (tupla[3], type(tupla[3]))
print (tupla[3][0], type(tupla[3][0]))
print (tupla[3][1], type(tupla[3][1]))

matrix = ((0,1,2),(3,4,5),(6,7,8))
print(matrix[0][2])
print(matrix[1][1])
print(matrix[2][0])

print(f"{matrix[0][2]},{matrix[1][1]},{matrix[2][0]}")

# Acceder a los valores necesarios para formar la frase:
# "Estoy aprendiendo a programar"

cadenas = (("a","es","el","programar"),("estoy","apre","ar"),("ndiendo","a"))
cadena_1 = cadenas[1][0]
cadena_2 = cadenas[1][1]
cadena_3 = cadenas[2][0]
cadena_4 = cadenas[0][0]
cadena_5 = cadenas[0][3]
cadena_0 = cadena_1.title()
print(cadena_0 + " "+ cadena_2 + cadena_3 + " "+ cadena_4 +" "+ cadena_5)

cadenas = (("a", "es", "el", "programar"),
            ("estoy", "apre", "ar"),
            ("ndiendo", "a"))
print(f"{cadenas[1][0].capitalize()} \
{cadenas[1][1]+cadenas[2][0]} \
{cadenas[0][0]} {cadenas[0][3]}")


