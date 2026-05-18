# programa que imprime las primeras N potencias de 2 requeridas por el usuario 
# y calcula su promedio 
N= int (input ("ingrese la cantidad de potencias que desea: "))
i=0
suma=0
while i<N: 
  potencia=2**i
  print ("2 ^",i, "=" , potencia)
   suma +=potencia 
   i+= suma /N 
print ("el promedio de las potencias es de: ",promedio)
