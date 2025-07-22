# Imprimir los 20 primeros números que sean múltiplos de 2 y 5

print("Primeros 20 números múltiplos de 2 y 5:")

multiplos = []
i = 1

while len(multiplos) < 20:
    if i % 2 == 0 and i % 5 == 0:
        multiplos.append(i)
    i += 1

print(multiplos)