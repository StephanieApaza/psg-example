# Crear un script que pida un número entero y verifique si es múltiplo de 5 usando operador ternario

print("Inicio si es múltiplo de 5")
numero = int(input("Escribe un número entero: "))
multiplo_cinco = "Es múltiplo de 5" if not(numero % 5) else "No es múltiplo de 5"
print(multiplo_cinco)
print("Fin")