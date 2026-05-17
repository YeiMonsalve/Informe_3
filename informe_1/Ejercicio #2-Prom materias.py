# Este ejercicio realiza el promedio de 4 materias
# Imprime el promedio en pantalla
# y muestra un mensaje diferente si el promedio es mayor o igual a 4.5

# Definir variables
matematicas = float(input("Ingrese la nota de matemáticas: "))
castellano = float(input("Ingrese la nota de castellano: "))
ingles = float(input("Ingrese la nota de inglés: "))
sociales = float(input("Ingrese la nota de sociales: "))

# Calcular promedio
promedio = (matematicas + castellano + ingles + sociales) / 4

# Imprimir promedio
print("El promedio es:", promedio)

# Condición
if promedio >= 4.5:
    print("Puedes acceder a la beca")
