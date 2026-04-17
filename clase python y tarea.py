""""
estimado usted sera seleccionado para hacer un login en banco santander
estimado un maximo de ingreso de 5 veces
de no logrado debe mostrar el siguiente mensaje en pantalla al usuario
po favor comuniquese a nuestro call center

de introducir correctamente sus credenciales, debe mostrar un mensaje de bienvenida con el nombre del usuario

"""

intento = 5

usuario=input("bienvenido al Banco Santander, por favor ingrese su usuario ")


if usuario == ("Amanda"):
  
  while intento > 0:
   pasword=input("ingrese su contraseña ")

   if pasword == "federico el pepino":
    print("bienvenida Amanda")

    break
  
   else:
    intento = intento-1
    print(f"intento fallido, te falta,{intento}")

    if intento == 0:
      print("por favor comuniquese a nuestro call center")
  
else:
 print ("usuario no reconocido")