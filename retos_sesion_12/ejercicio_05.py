print("Inicio de la app para gestionar contactos")

contactos = {}

nombre = input("Escribe el nombre de contacto: ").strip().title()
numero_telefono = input("Escribe +(código del país) seguido del número de teléfono: ").strip()

if nombre and numero_telefono.startswith('+') and numero_telefono[1:].isdigit() and len(numero_telefono) == 12:
    contactos[nombre] = numero_telefono
    print("Contacto guardado")
    print("Lista de contactos: ",contactos)
else:
    print("Datos incorrectos")

print("Fin")