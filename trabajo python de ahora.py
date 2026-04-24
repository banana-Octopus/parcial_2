#clase 24/4
"""
acaban de tener su primer empleo en el retail de falabella y les solicitan crear un programa en python, que entrege descuentos a los clientes,
 y para eso empezamos solicitando a los usuarios su numero de rut, el cual debe validar los 8 digitos del mismo
 en un casilla posterior validaar el numero de verificacion
 posteriormente debe solicitar el nombre del cliente, el monto de la compra, para saber si obtiene descuento, si/no, 
 toda compra menor a 10 lucas no obtiene descuento, toda compra mayor a 10 lucas, hasta 50 lucas obtiene un 10 % de descuento
 y toda compra mayor a 50 lucas obtiene un 20% de descuento
 que deberia calcular mi programa: monto de descuento, total a pagar, y deberia mostrar en pantalla tipo voleta, el rut, el nombre del usuario, el monto de la compra y el descuento final

 """


rut = int(input("ingrese su rut, sin puntos y sin verificador "))
if rut
ver = input("ingrese el digito verificador ")
#ver=[0,1,2,3,4,5,6,7,8,9]
#k=0

nombre = input("ingrese su nombre, por favor ")

compra =int(input("ingrese el precio de su compra "))



try:

    if compra >=10000 <= 500000:
     preciofin = compra-((10/100)*compra)
     desc = 10
     print("tiene un descuento de 10%, en esta compra")
      

    elif compra>=50000:
      preciofin = compra-((20/100)*compra)
      desc = 20
      print ("tienes un descuento del 20%, en esta compra")
        
    else:
       compra <10000
       preciofin = compra
       desc = 0
except compra==0:
   print("compra invalida")    


print(rut+"-"+ver, nombre)
print ({compra},"descuento: " , desc,"%")
print("el valor total es: ", {preciofin})
    



