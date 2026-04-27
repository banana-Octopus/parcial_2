#clase fecha 27-04

print("---------bienvenid al banco fallabella--------")
#validar rut


while True:
    rut=input("ingresa tu rut sin punto ni guuion")

    if rut.isdigit()and len(rut)==8:
        break
    else:
        print("digite solo numeros")

#valida codigo de verificacion

while True:
    dv=input("ingresa tu digito verificador").upper()
    if len(dv)==1 and (dv.isdigit()or dv=="k"):
        break

    else:
        print("ingrese el codigo valido")    
    
    #nombre


    nombre = input("ingrese su nombre")

    #valida compra

    while True:
        montos = input("ingrese el monto de la compra")

        if montos.isdigit():
            monto= int(montos)

            if monto >=0:
                break
            else:
                print("error, el monto es negativo")

        else:
            print("error ingresa solo numero")

#calculos renales

if monto <10000:
    descuento= 0
    porcentaje=0

elif monto <=50000:
    descuento=monto*0.10
    porcentaje= 10

else:
    descuento = monto *0.20
    porcentaje=20
total= monto - descuento

#voleta
#\ salto de linea
print("\n-----------------------------boleta------------------------------------------")
print(f"rut: {rut}-{dv}")
print(f"nombre: {nombre}")
