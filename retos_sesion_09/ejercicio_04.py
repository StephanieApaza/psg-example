# Productos de una dulceria

#Lista de productos
productos = ['Oreo','Chizitos','Bon Bon Bum','Waffer','Tauri','Mecano','Gomitas']

#Lista de precios
precios = [3, 2.5, 1, 3.5, 1.5, 4, 2]

print("Lista de productos de la dulcería: ", productos)
print("Lista de precios de la dulcería: ", precios)

# Agrega 2 productos nuevos al final de las listas
productos.append('Palomitas')
precios.append(5)

productos.append('Bananitas')
precios.append(4.5)

print("Lista de productos actualizados: ", productos)
print("Lista de precios actualizados: ", precios)

# Elimina el producto con el nombre "Bon Bon Bum" de las listas
indice_b = productos.index('Bon Bon Bum')
productos.pop(indice_b)
precios.pop(indice_b)
print("Lsta de productos sin Bon Bon Bum: ", productos)
print("Lista de precios sin Bon Bon Bum: ", precios)

# ¿Cuanto cuesta el producto Oreo y Chizitos?
oreo = productos.index('Oreo')
precio_oreo = precios[oreo]
print("El precio de Oreo es:", precio_oreo,"Bs")

chizito = productos.index('Chizitos')
precio_chizito = precios[chizito]
print("El precio de Chizitos es: ", precio_chizito,"Bs")

# ¿Cuál es el producto más caro y el más barato?
# Producto más caro
indice_max = precios.index(max(precios))
product_max = productos[indice_max]
precio_max = precios[indice_max]
print("El producto más caro es: ", product_max, "con Bs", precio_max)

#Producto más barato
indice_min = precios.index(min(precios))
product_min = productos[indice_min]
precio_min = precios[indice_min]
print("El producto más barato es: ", product_min, "con Bs", precio_min)

# Cuantos productos tiene en total
num_product = len(productos)
print("La tienda tiene en total: ",num_product ,"productos" )

# Cuanto cuestan todos los productos
sum_product = sum(precios)
print("La suma de precios de todos los productos es: ", sum_product , "Bs")

# Ordena los productos y precios del más barato al más caro
precios_ordenados = sorted(precios)

productos_ordenados = [productos[precios.index(precio)] for precio in precios_ordenados]

print("Los productos ordenados del más barato al más caro son: ")
print(productos_ordenados)
print(precios_ordenados)

# Elimina todos los productos de las listas
productos.clear()
precios.clear()
print("Lista de productos vacía: ", productos)
print("Lista de precios vacía: ", precios)


