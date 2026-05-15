# Manejo de Excepciones.
# AttributeError.

try:
   string1 = "hola"
   string1.append(" mundo") # .append() falla porque los textos no tienen este método, a diferencia de las listas. 
except AttributeError:
   print('Error, atributo o método inexistente.') # Se genera si se intenta abrir un archivo que no existe.