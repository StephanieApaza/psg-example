# Lista con 10 nombre
nombres = ["Paola","Matias","Mario","Judith","Lucia","Juan","Luciana","Carmen","Israel","Sonia"]

# Obtener una sublista de 5 a 9 con saltos de 2 en 2
sub_nombres = nombres[5:10:2]
print("Sub_lista de índices 5 al 9, con paso 2: ",sub_nombres)

# Buscar si existe el nombre "José" en la lista original
busqueda = "José" in nombres
print("¿Existe José en nombres?: ", busqueda)

# Ordenar la sub lista alfabeticamente a - z
sub_lista = list(sub_nombres)
sub_lista.sort()
print("Sub_lista ordenada A - Z: ", sub_lista)

# Ordenar la lista original alfabéticamente descendente z - a
nombres.sort(reverse = True)
print("Lista ordenada Z -A: ", nombres)