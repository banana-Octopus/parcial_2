#evaluacion formativa sara quitral parte dos

#sistema de arriendo de equipos

nombre=input("ingrese su nombre ")

while True:
    tel=input("ingrese su numero de telefono, despues del +56 ")

    if tel.isdigit()and len(tel)==9:
        break
    else:
        print("digite solo numeros")


chamba=int(input("ingrese sus horas de trabajo "))

excabadora=1
grua=2
mescladora=3

print("tipos de equipo de lam empresa")
print("opciones: " \
  "1.excabadora/" \
  "2.grua" \
  "3.mescladora")

equ=int(input("ingrese el tipo de equipo con el numero de opcion "))


cantequipo=int(input("ingrese la cantidad de horas usadas por el equipo "))

#horas usadas por equipo

while True:
 if equ == excabadora:
  print(f"el precio por hora del equipo es: 200.000")
  print (f"la cantidad de horas usadas por la excabadora es: {cantequipo}")
  pretotal=200000*cantequipo
  print ( f"el precio a pagar por la maquina es:{pretotal}")
  break
 
 elif equ==grua:
  print(f"el precio por hora del equipo es: 250.000")
  print (f"la cantidad de horas usadas por la grua es: {cantequipo}")
  pretotal=250000*cantequipo
  print (f"el precio a pagar por la maquina es:{pretotal}")
  break
 
 elif equ==mescladora:
  print(f"el precio popr hora del equipo es: 150.000")
  print (f"la cantidad de horas usadas por la mescladora es: {cantequipo}")
  pretotal=150000*cantequipo
  print (f"el precio a pagar por la maquina es:{pretotal}")
  break
 
 else:
  print("ingrese una opcion valida")


 
 