# Programa que categoriza postulantes según sexo y edad
# Femenino: FA si < 23 años, FB en caso contrario
# Masculino: MA si < 25 años, MB en caso contrario

# Entradas
sexo = input("Ingrese el sexo del postulante (Femenino/Masculino): ")
edad = int(input("Ingrese la edad del postulante: "))

# Proceso
if sexo == "Femenino":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
else:
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"

# Salida
print("La categoría asignada es:", categoria)
