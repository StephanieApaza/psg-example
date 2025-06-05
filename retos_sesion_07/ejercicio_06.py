# Funciones no vistas en la sesion

# 1. Función rstrip
print("Esta función elimina espacios en blanco del final de una cadena")
frase = "El clima en la ciudad de El Alto descenderá más en invierno.      "
frase_l = frase.rstrip()
print(frase_l)

# 2. Función partition
print("Esta función divide una cadena en tres partes, la parte antes del separador, después y el separador en sí")
texto = "Ejercicio-Siete"
texto_l = texto.partition("-")
print(texto_l)

# 3. Función isprintable
print("Esta función true si todos los caracteres de una cadena se pueden imprimir")
palabras = "Viaje al centro de la tierra"
print(palabras.isprintable())

# 4. Funcion casefold
print("Esta funcion convierte todo en minúsculas, incluso letras acentuadas")
texto_2 = "LinGUística"
print(texto_2.casefold())

# 5. Funcion endswith
print("Esta funcion verifica si una cadena termina con un sufijo específico y devuelve True o False")
nombre = "Descubre Bolivia.xls"
print(nombre.endswith("xls"))