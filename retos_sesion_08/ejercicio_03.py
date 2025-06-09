# Ingresa una pregunta por teclado y almacena el valor en una tupla

frase_input = input("Ingresa una pregunta: ")
frase = (frase_input,)

# Concatenando la tupla
pregunta = ('¿',) + frase + ('?',)

# Imprimiendo el resultado
print("Tupla concatenada: ",pregunta)

# Repitiendo la tupla concatenada 2 veces
resultado = pregunta * 2
print("Tupla repetida: ",resultado)