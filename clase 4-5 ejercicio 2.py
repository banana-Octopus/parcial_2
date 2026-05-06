#clase 4/5 ejercicio 2

"""
desarrolle un programa en python, que permite ingresar dos numeros enteros, que indique un rango de numero, el primero debe ser menor al segundo, luego el programa debe generar un numero aleatorio 
entre el rango de los numeros, para hacer esto, sigue las siguientes instrucciones 

1)'import'--->'from random','randint' 

2)numero = randint
(n1,n2)
la linea uno le permite cargar la funcion randint(), luego la linea 2 use la funcion que permite usar la funcion randint que permite generar un numero que se guardan en la variable numero uno

ej: randit=(1,10)
un generador de numero aleatorio debe ajustar el numero para que el valor final sea adivinado por el usuario luego de 3 intentos

si el numero ajustado llega a quedar fuera del rango, entonces el numero final debe dividirse por el limite inferior"""

#elegir numeros
from random import randint

n1= int(input("ingrese un numero "))
n2= int(input("ingrese un numero mayor al anterior "))

#elegir numero aleatorio
if n2>n1:
 numero=randint (n1,n2)
elif n2<n1:
 print("el segundo numero no es mayor al primero")

 #adivinar numero

def adivinar_numero():
    intento=0
    while True:
        numero_adivinado=int(input("adivine el numero elegido "))

        if numero_adivinado<numero:
         intento=intento+1
         print(f"sigue intentando, el numero es mayor a ese, intento {intento}")

        elif numero_adivinado>numero:
         intento=intento+1
         print(f"sigue intentando, el numero es menor a ese, intento {intento}")
         
        else:
          numero_adivinado=numero
          print(f"adivinaste el numero, el numero es {numero}")
          
        if intento==3:
          print(f"perdiste, el numero era {numero}")
          break
adivinar_numero()
#profe no entiendo lo ultimo que pidio