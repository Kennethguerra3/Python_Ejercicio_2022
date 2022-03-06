# Una frutería ofrece las manzanas con descuento según la siguiente tabla:
"""   Numero de kilos comprados	|     % Descuento
            0 – 2	            |       0%
            2.01 – 5	        |       10%
            5.01 – 10	        |       15 %
            10.01 en adelante	|       20%   """
print("=======================================")
print("PESAJE | DESCUENTO | PAGO TOTAL")
print("=======================================")
print("        |FRUTITA.COM|                  ")

# Ingresar la variables para el input:
cant = float(input("Ingrese kilos a comprar : "))
precio = float(input("Ingrese Precio por kilo: "))

# Primera tanda de descuento:
if cant <2:
    neto = cant * precio
    des = neto * 0
    total_pa = neto - des
    print("Monto Neto:", neto, "Descuento: ", des, "Total Pagar Manzana:", total_pa)
elif 2.01 <= cant <= 5:
    neto = cant * precio
    des = neto * 0.10
    total_pa = neto - des
    print("Monto Neto:", neto, "Descuento: ", des, "Total Pagar Manzana:", total_pa)

# Segunda tanta de descuento:
elif 5.01 <= cant <= 10:
    neto = cant * precio
    des = neto * 0.15
    total_pa = neto - des
    print("Monto Neto:", neto, "Descuento: ", des, "Total Pagar Manzana:", total_pa)
elif cant >=10.01:
    neto = cant * precio
    des = neto * 0.20
    total_pa = neto - des
    print("Monto Neto:", neto, "Descuento: ", des, "Total Pagar Manzana:", total_pa)
else:
    print("No hay descuento para este peso.")
