"""
usuario correcto: Duoc

contraseña:123444pollo
"""
correct_password=("123444pollo")
max_intentos=3
intento=0

usuario = input("Ingrese el usuario ")

  
if usuario == ("Duoc"):
  print("Usuario correcto")

  password = input("ingrese la contraseña: ")

  if password == correct_password:
        print("Ingreso correctamente, ¡bienvenido!")
   

  else:
   while True:
    print ("Contraseña incorrecta")
    
    password = input("Contraseña: ")
    intento += 1

    if intento >= max_intentos:
        print ("usuario bloqueado")
        break

    
    else:
      
     print ( f"intentos restantes: . {max_intentos - intento}. ")
     if password == correct_password:
            print("Ingreso correctamente, ¡bienvenido!")
 

else:
    print("Usuario incorrecto, acceso denegado")
