#ejercicio que indica el tipo de musica y el año de nacimiento 

genero = str (input ("ingrese el genero de musica "))

if (genero=="electronica" or genero=="pop"):
   año = int (input ("ingrese su año de nacimiento :"))
   if (año >2000 and genero=="pop"):
     print ("tengo la camisa negra ")
   else: 
    print ("daft punk por siempre ")
else :  
 print ("los unicos generos buenos son electronica y pop")
print ("fin del algoritmo")
