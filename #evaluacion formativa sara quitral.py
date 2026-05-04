#evaluacion formativa sara quitral

# ejercicio 1, sistema de descuentos

nombre =input("bienvenio a la tiena boushe, por favor introdusca su nombre ")

while True:
 compra = input("por favor ingrese el monto de la compra ")
 if compra.isdigit():
    monto =int(compra)
    if monto >=0:
     break
    else:
     monto <=0
     print("porfavor ingrese un monto valido")
 else:
        print("digite solo numeros")

# descuentos



if monto <10000:
    desc =0
    montototal=monto

elif monto >=10000 <=50000:
    desc = monto*0.10
    porc=10
    montototal=monto-desc

else:
   monto >50000
   desc = monto*0.20
   porc=20
   montototal=monto-monto-desc


   
#boleta

print("------boleta--------")
print(f"señor/a {nombre}")
print(f"valor de la compra: {compra}, descuento:{porc}% , monto del descuento: {desc}")
print(f"total a pagar: {montototal}")
    
