# Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo. 
# La ejecución termina si la frase ingresada contiene la palabra salir

print("Vericación si la frase es palíndromo:")

while True:
    frase = input("Escribe una frase: ")
    if frase.lower() == "salir":
        break
    frase_limpia = frase.replace(" ", "").lower()
    if frase_limpia == frase_limpia[::-1]:
        print(f"{frase} es un palíndromo.")
    else:
        print(f"{frase} no es un palíndromo, ingrese otra frase.")
        
print("Fin")