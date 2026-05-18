#diseñe  un programa que pida numeros enteros al usuario
#hasta que ingrese el 0, para cada entradad publique si es par o impar 

numero= int (input ("ingrese el numero entero : (para finalizar ingrese el 0)"))
while numero!=0: 
  if numero %2==0: 
    print (f"el numero{numero} es par ")
  else: 
    print (f"el numero {numero} es impar ")
   numero = int (input (ingrese otro numero: ))
print ("programa finalizado ")
