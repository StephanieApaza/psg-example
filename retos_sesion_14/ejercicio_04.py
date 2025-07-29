# Crear una función anónima para obtener el valor absoluto de un número

valor_absoluto = lambda numero: numero if numero >=0 else -numero
resultado = valor_absoluto(-10)
print(resultado)
resultado = valor_absoluto(85)
print(resultado)