# Tienes una app para gestionar tareas de 4 usuarios, para acceder los usuarios deben iniciar sesión con un nombre de usuario 
# y una contraseña introducidos por teclado

usuarios_app = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'user123',
    'user3': 'user123'
}

print("Inicio de sesión para acceder a la app")

usuario = input("Nombre del usuario: ").strip()
contraseña = input("Contraseña: ").strip()

if usuario in usuarios_app and usuarios_app[usuario] == contraseña:
    print("Acceso aprobado")
else:
    print("Acceso denegado")

print("Fin")