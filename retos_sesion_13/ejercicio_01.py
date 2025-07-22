# Imprimir los 20 primeros números de la sucesión de Lucas

print("Primeros 20 números de la sucesión de Lucas:")
l0 = 2
l1 = 1
print(l0, end = ', ')
print(l1, end = ', ')

for i in range(2,20):
    ln = l0 + l1
    l0, l1 = l1, ln
    if i == 19:
        print(ln)
    else:
        print(ln, end = ', ')