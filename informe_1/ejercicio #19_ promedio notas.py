# Solicitar el nombre de una asignatura y cuatro notas del proceso.
# Mostrar en el terminal el nombre de la asignatura y el promedio de las 4 notas.

asignatura = str(input("Ingrese el nombre de la asignatura: "))
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
n4 = float(input("Ingrese la cuarta nota: "))

prom = (n1 + n2 + n3 + n4) / 4

print("El nombre de la materia es:", asignatura, "\nY el promedio de la nota es:", prom)
