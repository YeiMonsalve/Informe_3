#ejercicio que muestra un ingreso con usuario y contraseña 

usuario_correcto=("admin")
contraseña_correcto =("123")

opcion =0
while opcion !=2: 
  print (" Login ")
  print ("1. ingrese las credenciales ")
  print ("2. salir ")

  opcion = int (input ("seleccione una opcion "))
   if opcion ==1: 
     usuario= str(input("ingrese el usuario: "))
     contraseña= str(input("ingrese la contraseña:"))
     if usuario == usuario_correcto and contraseña==contraseña_correcto:
       print ("inicio de sesion valido")
     else : 
       print ("inicio de sesion invalido ")
