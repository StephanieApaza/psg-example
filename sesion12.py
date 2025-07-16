


# reto de clase
sexo = input("Sexo del paciente (hombre/mujer): ").strip().lower()
edad = int(input("Edad del paciente (en años): "))
hemoglobina = float(input("Nivel de hemoglobina (g/dl): "))

umbrales_anemia = {'hombre': 13.5, 'mujer':12, 'niño':11}

analizando_h = sexo == 'hombre' and edad >= 13 and hemoglobina < 13.5
analizando_m = sexo == 'mujer' and edad >= 13 and hemoglobina < 12
analizando_n = edad < 13 and hemoglobina < 11

resultado = analizando_h or analizando_m or analizando_n
print(resultado)