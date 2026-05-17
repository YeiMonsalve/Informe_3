# La entrada a un circo vale p soles por persona.
# Si la edad de la persona es menor de 10 años,
# se aplica un descuento del 25% en el valor del boleto.

# Entradas
p = float(input("Ingrese el precio de la entrada: "))
edad = int(input("Ingrese la edad del cliente: "))

# Proceso
if edad < 10:
    p = p - (p * 0.25)

# Salida
print("El monto final a pagar es:", p)
