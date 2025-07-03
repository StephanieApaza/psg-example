# El dueño de una tienda de ropa deportiva ha comprado ropa formal y quiere abrir una nueva tienda que combine ambos estilos

# Declaración de listas
lista_1 = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
lista_2 = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

# Convirtiendo a conjuntos ambas listas
ropa_deportiva = set(lista_1)
ropa_formal = set(lista_2)

# Creando un conjunto con las prendas de ambos tipos
total_items = ropa_deportiva.union(ropa_formal)
print("El conjunto total de ropas de la tienda son: ", total_items)