# Escriba un programa que calcule la cantidad de arena
# necesaria para revocar una pared cualquiera,
# según sus medidas (largo y ancho) expresados en metros.

# Definir variables
metros = 0.5
largo = float(input("Ingrese el largo de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))

# Calcular cantidad de arena
arena = (largo * ancho) * metros

# Mostrar resultado
print("Cantidad de arena necesaria es:", arena)
