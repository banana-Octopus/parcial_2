# respuesta trabajo prueba, como lo dijo el profe, pero llegue tarde asik no se si esta bien xd
from random import randint

num1=int (input("ingrese el limiete inferior"))
num2=int (input("ingrese el limite superior"))

while num1>=num2:
    print("error, el limite inferior debe ser menor al superior")
    print("error, el limite inferior debe ser menor al superior")
    num1=int (input("ingrese el limite inferior"))
    num2=int (input("ingrese el limite superior"))

#numero aleatorio
numero=randint(num1, num2)
#ajuste multiplo de 3

ajustado=(numero//3)*3

if ajustado<num1:
    ajustado=num1
#intento 1
intento1=int(input("intenta adivinar"))

if intento1==ajustado:
    print("felicitaciones, adivino en tu primer intento")
else:
    if intento1<ajustado:
        print("el numero es mayor")
    else:
        print("el numero es menor")
   #intento 2
intento2=int(input("intenta adivinar"))

if intento2==ajustado:
    print("felicitaciones, adivino en tu segundo intento")
else:
    if intento2<ajustado:
        print("el numero es mayor")
    else:
        print("el numero es menor")
    #pista
    print("te dare una pista: ")

dist1=abs(ajustado-intento1)
dist2=abs(ajustado-intento2)

if dist1<dist2:
    print(f"el numero que buscas es mas cercano de {intento1} que de {intento2}")
elif dist2<dist1:
    print(f"el numero es mas cerca {intento2} que de {intento1}")
else:
    print("ambos intentos estan a la misma distancia")
    #tercer intento

intento3=int(input("intenta la ultima vez: "))

if intento3==ajustado:
    print("lo lograste, adivinaste en el ultimo intento")
else:
    print("fracasaste, cuek")
    print("el numero era", {ajustado})

