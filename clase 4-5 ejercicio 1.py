#clase 4/5 ejercicio 1

"""
desarrolle un program en python, que permita calcular el valor final de un bicicletero/moto (estacionamiento) y del candado para el centro civico que ofrece descuento para el guardado de su moto mensual, 
segun los dias de uso. 
valor inicial: motocicleta desde 15000 peso mensuales, candados desde 9000 pesos mensuales
realiza una tabla con los dias de uso, estudiante y descuento por la motocicleta
cantidad de dias >=20, estudiantes =si, descuento de 25%

cantidad de dias >=20, estudiantes =no, descuento del 15%

10<=<20, estudiante =si, desc 15%

10<=<20 estudante= no, desc 8%

ademas el candado tiene una regla adicional
los estudiantes tienen un desc de 12% adicional por usar tarjeta de  credito
si ademas la cantidad de dias es menor a15 o obtendra solo un 5%(estudiantes)
si la cantidad de dias es menor a 10, el descuento es de 0"""

from tabulate import tabulate

valores = [moto 15000 mensual, candados 9000 mensual]

tabla_moto = [[dias=20 o menos, estudiante, descuento de 25%],[dias=20 o menos, NO estudiante, descuento de 15%],[dias=entre 10 y 20, estudiante, descuento de 15%],
       [dias=entre 10 y 20, NO estudiante, descuento de 8%]]
print(tabulate(valores,\
               tabla_moto, headers=['dias', 'estudiante', 'descuento']))

#patente= input ("bienvenido, por favor ingrese la patente de su moto")
#dias= int (input ("por favor ingrese el numero de dias de uso del estacionamiento"))








