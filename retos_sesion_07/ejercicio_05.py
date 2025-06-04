# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palíndromo sin importar los espacios, mayúsculas o minúsculas

print("Este programa evaluará si la palabra o frase que ingreses es un palíndromo o no")

# Definiendo la variable que recibirá la palabra o frase
word = input("Escribe una palabra o frase: ")

# Reemplazando los espacios de la variable word
word_b = word.replace(" ","")

# Convirtiendo la variable word_b a minúsculas
word_c = word_b.lower()

# Evaluando la palabra o frase ingresada invertida
evaluar = word_c[::-1]

# Comparar la palabra ingresada con la invertida 
es_palindromo = word_c == evaluar

print("¿La palabra o frase ingresada es palíndromo?: ",es_palindromo)
print(word_c," -->" ,evaluar)