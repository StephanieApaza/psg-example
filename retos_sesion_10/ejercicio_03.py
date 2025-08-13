# Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online

tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

set_tienda_fisica = set(tienda_fisica)
set_tienda_online = set(tienda_online)

# Quiénes compraron en ambos canales
ambas_tiendas = set_tienda_fisica.intersection(set_tienda_online)
print("Las personas que compraron en ambas tiendas son: ", ambas_tiendas)

# Quiénes compraron solo en la tienda física
only_fisica = set_tienda_fisica.difference(set_tienda_online)
print("Las personas que compraron solo en la tienda fisica son: ", only_fisica)

# Quiénes compraron solo online
only_online = set_tienda_online.difference(set_tienda_fisica)
print("Las personas que compraron solo en la tienda online son: ", only_online)