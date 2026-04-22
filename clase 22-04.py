# try

"""
try:
    resultado = 10/0
except ZeroDivisionError:
    print("¡error! no debemos dividir entre cero.")

finally:
    print("boque finalizado")

"""

try:
    num1 =float(input("porfavor, ingresa un numero: "))
    num2 =float(input("porfavor, ingresa un numero: "))
  
    if num2 ==0:
        raise ZeroDivisionError
    
    else:
        resultado = num1/num2
    
        print(f"el resultado de es division es: {resultado}")
    
except ValueError:
   print("¡error! ingresa un numero nuevo")

except ZeroDivisionError:
   print("¡error! no se puede dividir en cero.")

print(f"fin del programa {resultado}")

"""
tarea:

estimado estudiante, usted a sido seleccionado para realizar la interfas de usuario de los cajeros del grupo santander
el programa debe solititar al usuario: numero de rut, el cual debe ser validado con su numero de verificaion. (el numero despues del guion)
posteriormente a eso, el ususario debe introducir su clave, que no deberia ser menor o mayor a 10 digitos
"""