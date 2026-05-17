# Algoritmo bonificación
# Elaborar un programa que permita ingresar el
# nombre del trabajador, su sueldo básico y el
# número de hijos. Se deberá mostrar su
# bonificación y el sueldo final, teniendo en cuenta
# que la empresa da una bonificación del 7% del sueldo
# básico solo si el trabajador tiene hijos.

# Entradas
nombre = input("Ingrese el nombre del trabajador: ")
basico = float(input("Ingrese el sueldo básico: "))
hijos = int(input("Ingrese el número de hijos: "))

# Inicializar bonificación
bonificacion = 0

# Condición
if hijos > 0:
    bonificacion = basico * 0.07

# Calcular sueldo final
final = basico + bonificacion

# Salidas
print("La bonificación es:", bonificacion)
print("El sueldo final es:", final)
