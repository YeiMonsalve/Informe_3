# Manejo de Excepciones.
# ZeroDivisionError.

try:
    resultado = 10 // 1
    print(f'resultado: {resultado}')
except ZeroDivisionError:
    print('Error: no se puede dividir entre 0') # Si se intenta dividir por 0, el código tira la excepción y no el resultado.