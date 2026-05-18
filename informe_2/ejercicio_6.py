#ejercicio de votos para un partido 
#determinar si adquieren la curul o si se queman 

votosvalidos= int (input("ingrese los votos validos: "))
votospartido=int (input("ingrese los votos de su partido"))
umbral= votosvalidos*0.03
if (votospartido>umbral):
  print("tu partido tendra curules ")

else : 
  print ("se quemaron")
