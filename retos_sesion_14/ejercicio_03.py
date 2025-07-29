# Crear una función recursiva para obtener el N-esimo número de la serie de Lucas

def serie_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return serie_lucas(n - 1) + serie_lucas(n - 2)

# Uso de la función    
for i in range(11):
    print(f"L({i}) = {serie_lucas(i)}")