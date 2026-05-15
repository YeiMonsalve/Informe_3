# Manejo de Excepciones.
# ValueError.

try:
   number = int(input('Ingrese un número entero: '))
   print(f'Número ingresado: {number}')
except ValueError:
   print('Error, debe ingresar un número válido.') # Si intenta ingresar un texto y no un número, genera la excepción.