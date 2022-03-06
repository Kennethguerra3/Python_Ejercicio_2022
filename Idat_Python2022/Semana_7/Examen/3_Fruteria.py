# Una frutería ofrece las manzanas con descuento según la siguiente tabla:
"""   Numero de kilos comprados	| % Descuento
            0 – 2	            |       0%
            2.01 – 5	        |       10%
            5.01 – 10	        |       15 %
            10.01 en adelante	|       20%   """
print("=======================================")
print("PESAJE | DESCUENTO | PAGO TOTAL")
print("=======================================")
print("        |FRUTITA.COM|                  ")

cantidad = float(input("Ingrese kilos a comprar : "))
precio = float(input("Ingrese Precio por kilo: "))

# Calculo para la condiciones de descuento del if y elif:

# Ingresar la variables para el input:
if cantidad <= 2:
    total_neto = precio * cantidad
    print("Total a pagar", total_neto)
elif cantidad >= 2.01 and 5:
    total_neto = precio * cantidad
    descuento = total_neto * 0.10
    Total_Pagar = total_neto - descuento
    print("Total Pagar Manzana", Total_Pagar)

elif cantidad == 5.01 and 10:
    total_neto = precio * cantidad
    descuento = total_neto * 0.15
    Total_Pagar = total_neto - descuento
    print("Total Pagar Manzana", Total_Pagar)

elif cantidad >= 10.01:
    total_neto = cantidad * precio
    descuento = total_neto * 0.20
    Total_Pagar = total_neto - descuento
    print("Total Pagar Manzana", Total_Pagar)
else:
    print("No hay descuento para este pesaje!")
