# Una persona desea invertir su capital en un banco y desea saber
# cuánto dinero ganará después de un mes si el banco le paga
# intereses de 2% mensual. Este programa lo calcula.

# Definir variables
capital = int(input("Ingrese el monto a invertir: "))
dias = int(input("Ingrese el número total de días del mes a considerar: "))

# Interés mensual
interes = 0.02

# Calcular ganancia
ganancia = (capital * dias) * interes

# Mostrar resultado
print("La ganancia por cobrar después del mes es de:", ganancia)
