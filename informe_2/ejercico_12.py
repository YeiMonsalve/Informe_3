#jercicio while propuesto en clase : Solicitar un número entero hasta que esta que este 
numero = int(input("Ingrese un número entero: "))

while numero % 11 != 0:
    print("El número no es múltiplo de 11.")
    numero = int(input("Ingrese otro número: "))

print("El número es múltiplo de 11.")
   
