# Manejo de Excepciones.
# TypeError

try:
   number = 5
   text = 'example'
   print(number + text)
except TypeError:
   print('Error, no puede sumar un número con un texto.') # Al intentar sumar números con palabras genera excepción.