print("Inicio de aplicación de descuentos en la tienda")

edad = int(input("Anota la edad del cliente (en años): "))
compra = float(input("Anota el monto de la compra (solo el importe): "))

if edad > 60 and compra > 1000:
    print("Se le aplica un descuento del 20%")
    tasa_descuento = 0.20
elif (edad >= 18 and edad <= 60) and compra > 500:
    print("Se le aplica un descuento del 10%")
    tasa_descuento = 0.10
else:
    print("Se le aplica un descuento del 2%")
    tasa_descuento = 0.02

descuento = compra * tasa_descuento
total_pagar = compra - descuento
print("El descuento es de: ", descuento, "Bs")
print("Y el total a pagar es de: ", total_pagar, "Bs")

print("Fin")
