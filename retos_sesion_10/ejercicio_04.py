# Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. 
# Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común

postres_Jane = ['Lemon Pie', 'Brownie', 'Tarta de Manzana','Helado de Chocolate', 'Flan']
postres_Jhon = ['Carrot Cake', 'Croissant de Chocolate', 'Lemon Pie', 'Tarta de Manzana', 'Pudding']

set_postres_Jane = set(postres_Jane)
set_postres_Jhon = set(postres_Jhon)

# Cantidad total de postres que pidieron
postres = set_postres_Jane.union(set_postres_Jhon)
total_postres = len(postres)

# Postres en común que comparten Jane y Jhon
postres_comun = set_postres_Jane.intersection(set_postres_Jhon)
print("Los postres en común que pidieron Jane y Jhon son: ", postres_comun)

# Cantidad de postres que tienen en común
cant_postres = len(postres_comun)

# Determinando si la cantidad de postres que tienen en común es mayor al 50%
medida = total_postres * 0.5
compatibles = cant_postres > medida
no_compatibles = cant_postres <= medida

print("La cantidad de postres que tienen en común es mayor al 50%, ¿Por tanto son compatibles?", compatibles)
print("La cantidad de postres que tienen en común es menor o igual al 50%, ¿Quieren replantear su relación?", no_compatibles)


