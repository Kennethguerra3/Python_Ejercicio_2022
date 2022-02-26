"""Analizar los siguientes ejercicios de condiciones, representarlos mediante algoritmos en Python. """
#5.-En una tienda de descuento se efectúa una promoción en la cual se hace un descuento sobre el valor 
# de la compra total según el color de la bolita que el cliente saque al pagar en caja. Si la bolita es 
# de color blanco no se le hará descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un 25%, 
# si es azul un 50% y si es roja un 100%. Determinar la cantidad final que el cliente deberá pagar por su compra se sabe 
# que solo hay bolitas de los colores mencionados.a

# pantalla
print("""
    1) Blanco       3) Verde
    2) Amarillo       4) Azul
    5) Rojo
    """)
# Input para que seleccione la opcion.
Lista=input("-Selecciona algo :")

# Según lo que ingresó, código diferente
if Lista=="1":
    print("Blanco")
    print("Lo Lamento no hay ningun descuento para esta opcion. :C")
elif Lista=="2":
   print("Amarillo, Tienes descuento del 25%")
   des=0.25
   #la cantidad final que el cliente deberá pagar por su compra.
   V_compra=int(input("Ingrese el Valor: "))
   Pago=V_compra-(V_compra*des)
   print("Total a Pagar es ",Pago)
elif Lista=="3":
    print("Verde, Tienes descuento de 10%")
    des=0.10
    #la cantidad final que el cliente deberá pagar por su compra.
    V_compra=int(input("Ingrese el Valor: "))
    Pago=V_compra-(V_compra*des)
    print("Total a Pagar es ",Pago)
elif Lista=="4":
    print("Azul, Tienes descuento del 50%")
    des=0.5
    #la cantidad final que el cliente deberá pagar por su compra.
    V_compra=int(input("Ingrese el Valor: "))
    Pago=V_compra-(V_compra*des)
    print("Execelente hoy te llevas todo GRATIS.!! ",Pago)
elif Lista=="5":
    print("Rojo, Tienes descuento de 100%")
    des=1
    #la cantidad final que el cliente deberá pagar por su compra.
    V_compra=int(input("Ingrese el Valor: "))
    Pago=V_compra-(V_compra*des)
    print("Total a Pagar es ",Pago)
else:
    print("Ingrese el Valor Correcto.")
    






