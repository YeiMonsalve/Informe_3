# Manejo de Excepciones.
# IndexError.

try:
   numbers = [1, 2, 3, 4, 5]
   print(numbers[7])
except IndexError:
   print('Error, el indice indicado no existe.') # Sale el IndexError al acceder a un indice que no existe, en este caso, va de 0 a 4, al poner 7, genera excepción.