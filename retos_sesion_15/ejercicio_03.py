# Crea un programa que simule el funcionamiento de un cajero automático

class FondosInsuficientes(Exception):
    pass

saldo_disponible = 2000

try:
    monto_retirar = float(input("Ingrese el monto que quiere retirar: "))
    if monto_retirar > saldo_disponible:
        raise FondosInsuficientes("Su saldo disponible actual es menor que el monto que desa retirar.")
    if monto_retirar > 1000:
        raise Exception("El monto excede el límite permitido por transacción.")
    # Para realizar el retiro
    saldo_disponible -= monto_retirar
    print(f"Retiro realizado. Su nuevo saldo es: {saldo_disponible}")
    
except FondosInsuficientes as e:
    print(" ❌ No hay fondos suficientes:", e)
except Exception as e:
    print("⚠️  Error:", e)


