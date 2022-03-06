# Una compañía dedicada al alquiler de automóviles cobra un monto fijo de S/.300 para los primeros 100 km de
# recorrido. Para más de 100 km y hasta 500 km, cobra un monto adicional de S/.15 por cada kilómetro en exceso sobre
# 100. Para más de 500 km cobra un monto adicional de S/.10 por cada kilómetro en exceso sobre 500. Los precios ya
# incluyen el 18% del impuesto general a las ventas, IGV. Diseñe un algoritmo que determine el monto a pagar por el
# alquiler de un vehículo y el monto incluido del impuesto. (7 pts.)
print("=======================================")
print("ALQUILER DE AUTOMÓVILES MODERNOS ")
print("=======================================")
print("                                       ")
print(" Se Calculara el Monto de alquiler incluido IGV ")
Kilometro=int(input("Ingrese el Km recorrido: "))

if Kilometro <= 100:
    alquiler=300
    IGV = (alquiler * 1.18)-alquiler
    Monto_Total=alquiler+IGV
    print("Total Alquiler", alquiler,"Total impuesto", IGV,"Total pagar",Monto_Total)

elif Kilometro >= 101 and 500:
    alquiler1=300
    extra_K1=Kilometro-100
    adicional2=(extra_K1*15)
    Monto_Neto=(alquiler1+adicional2)
    IGV=((Monto_Neto*1.18)-Monto_Neto)
    Monto_Total=Monto_Neto+IGV
    print("Total Alquiler", Monto_Neto, "Total Impuesto:", IGV, "Total pagar", Monto_Total)
    #print(extra_K1)
else:
    Kilometro >= 501
    alquiler1 = 300
    extra_k1 = 100
    extra_k3 = (Kilometro - 500)
    extra_K2 = ((Kilometro - 100) - extra_k3)
    adicional3 = (extra_k3 * 10)
    adicional2 = (extra_K2 * 15)
    Monto_Neto = (adicional2 + adicional3 + alquiler1)
    IGV = ((Monto_Neto * 1.18) - Monto_Neto)
    Monto_Total = Monto_Neto + IGV
    print("Total Alquiler", Monto_Neto, "Total Impuesto:", IGV, "Total pagar", Monto_Total)
    # print(extra_k1 extra_K2, extra_k3)



