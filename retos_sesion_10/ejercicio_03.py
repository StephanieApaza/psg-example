# Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online

tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

# Quiénes compraron en ambos canales
ambas_tiendas = set(tienda_fisica).intersection(tienda_online)
print("Las personas que compraron en ambas tiendas son: ", ambas_tiendas)

# Quiénes compraron solo en la tienda física
only_fisica = set(tienda_fisica).difference(tienda_online)
print("Las personas que compraron solo en la tienda fisica son: ", only_fisica)

# Quiénes compraron solo online
only_online = set(tienda_online).difference(tienda_fisica)
print("Las personas que compraron solo en la tienda online son: ", only_online)