""""
estimado usted sera seleccionado para hacer un login en banco santander
estimado un maximo de ingreso de 5 veces
de no logrado debe mostrar el siguiente mensaje en pantalla al usuario
po favor comuniquese a nuestro call center

de introducir correctamente sus credenciales, debe mostrar un mensaje de bienvenida con el nombre del usuario

"""

intento = 3

while intento >0:
 pasword=input("ingrese su clave")
 if pasword =="1234":
  print("bienvenido")
  break
 else:
  intento = intento-1
  print(f"intento fallido, te falta,{intento}")
  if intento ==0:
   print("acceso denegado")
   
