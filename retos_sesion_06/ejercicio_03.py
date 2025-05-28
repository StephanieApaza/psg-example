# Imprime una tabla de verdad para la siguiente sentencia: Un sistema de seguridad controla el acceso a una habitación, la puert<
# sólo se abre si se introduce una tarjeta válida o la huella dactilar, pero no ambas al mismo tiempo. 
# Si se introduce la tarjeta y la huella dactilar, la puerta no se abre.

print("Sistema de Seguridad: Acceso a la habitación")

# Caso 1
tarjeta = True
huella = True
abrir = (tarjeta or huella) and not (tarjeta and huella)
print(" ",tarjeta, " | ",huella," | ", abrir)

# caso 2
tarjeta = False
huella = True
abrir = (tarjeta or huella) and not (tarjeta and huella)
print(" ",tarjeta, " | ",huella," | ", abrir)

# caso 3
tarjeta = True
huella = False
abrir = (tarjeta or huella) and not (tarjeta and huella)
print(" ",tarjeta, " | ",huella," | ", abrir)

# caso 4
tarjeta = False
huella = False
abrir = (tarjeta or huella) and not (tarjeta and huella)
print(" ",tarjeta, " | ", huella, " | ", abrir)
