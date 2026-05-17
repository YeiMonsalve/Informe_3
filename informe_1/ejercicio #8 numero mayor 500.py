# Construir un programa que permita ingresar
# un número. Si el número es mayor de 500,
# se debe calcular y mostrar en pantalla el 18% de este.

# Entrada
num = float(input("Ingrese un número: "))

# Proceso
if num > 500:
    porcentaje = num * 0.18
    print("El 18% es:", porcentaje)
