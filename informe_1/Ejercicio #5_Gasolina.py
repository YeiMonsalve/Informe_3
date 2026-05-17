# Programa que calcula consumo de gasolina y velocidad media
# según kilómetros recorridos, tiempo del viaje y precio de gasolina.

# Entradas
kmRecorrido = float(input("Ingrese el total de km recorridos: "))
precio = float(input("Ingrese el precio de la gasolina (por litro): "))
dinero = float(input("Ingrese el dinero gastado en el viaje: "))
horas = float(input("Ingrese el tiempo del viaje en horas: "))
minutos = float(input("Ingrese el tiempo adicional en minutos: "))

# Cálculos de consumo
consumoGasTotal = dinero / precio  # Total en litros
consumoLitros100Km = (consumoGasTotal / kmRecorrido) * 100  # Litros por 100 km
consumoEuros100Km = consumoLitros100Km * precio  # Euros por 100 km
consumoEurosKm = consumoEuros100Km / 100  # Euros por km

# Cálculos de velocidad
velocidadKm = kmRecorrido / (horas + (minutos / 60))
velocidadMs = (kmRecorrido * 1000) / ((horas * 3600) + (minutos * 60))

# Salidas
print("El consumo de gasolina en litros por 100 km es:", consumoLitros100Km)
print("El consumo de gasolina en euros por 100 km es:", consumoEuros100Km)
print("El consumo de gasolina en euros por km es:", consumoEurosKm)
print("La velocidad media en km/h es:", velocidadKm)
print("La velocidad media en m/s es:", velocidadMs)
