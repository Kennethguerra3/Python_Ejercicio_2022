# Una frutería ofrece las manzanas con descuento según la siguiente tabla:
"""   Numero de kilos comprados	| % Descuento
            0 – 2	            |       0%
            2.01 – 5	        |       10%
            5.01 – 10	        |       15 %
            10.01 en adelante	|       20%   """
print("=======================================")
print("PESAJE | DESCUENTO | PAGO TOAL")
print("=======================================")
print("                                       ")
# Ingresar la variables para el input:
cantidad=float(input("Ingrese kilos a comprar : "))
precio=float(input("Ingrese precio por kilo: "))

#Calculo para la condiciones de descuento del if y elif:
if cantidad <=2:
    total_neto=precio*cantidad
    print("Total a pagar", total_neto)
elif
    cantidad >= 2.01 and 5:
    total_neto=precio*cantidad
    descueto=total_neto * 0.10
    Total_Pagar=total_neto-descueto
    print("Total Pagar Manzana", Total_Pagar)
elif cantidad ==5.01 and 10:
    total_neto=precio*cantidad
    descueto=total_neto * 0.15
    Total_Pagar=total_neto-descueto
    print("Total Pagar Manzana", Total_Pagar)

else:
    cantidad >= 10.01:
    total_neto =cantidad*precio
    descueto = total_neto * 0.20
    Total_Pagar = total_neto - descueto
    print("Total Pagar Manzana", Total_Pagar)