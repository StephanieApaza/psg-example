# ¿El cubo de 300 se encuentra en el siguiente rango? [N > 0 & N < 27_000_000]

num_1 = 300
cubo = num_1 ** 3
rango = (cubo > 0) & (cubo < 27000000)
print("¿El cubo de 300 se encuentra en el rango?: ", rango)