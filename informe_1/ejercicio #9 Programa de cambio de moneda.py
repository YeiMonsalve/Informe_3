# Programa de cambio de moneda
# Convierte soles a dólares o euros según selección del usuario.
# Tipo de cambio: $ = S/. 2.35 y € = S/. 3.58

# Entradas
nombre = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese el monto a cambiar en soles: "))

print("Seleccione moneda de cambio")
print("[1] Dólares")
print("[2] Euros")
moneda = int(input("Ingrese opción: "))

# Proceso
if moneda == 1:
    cambio = monto / 2.35
    simbolo = '$'
else:
    cambio = monto / 3.58
    simbolo = '€'

# Salida
print("Se cambió en", simbolo, cambio)
