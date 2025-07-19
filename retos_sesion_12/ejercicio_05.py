print("Inicio de la app para gestionar contactos")

contactos = {}

nombre = input("Escribe el nombre de contacto: ").strip().title()
numero_telefono = input("Escribe +(código del país) seguido del número de teléfono: ").strip()

es_valido = nombre and numero_telefono.startswith('+') and numero_telefono[1:].isdigit() and len(numero_telefono[1:]) == 11

print("Nombre: ", nombre)
print("Teléfono: ", numero_telefono)
print("-----------------------")

if es_valido:
    contactos[nombre] = numero_telefono
    print("Contacto guardado")
else:
    print("Datos incorrectos")

print("Fin")