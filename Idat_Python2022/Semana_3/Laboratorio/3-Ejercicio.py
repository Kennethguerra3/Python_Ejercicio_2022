#3.	Una farmacia aplica al precio de los remedios el 10% de descuento. Hacer un programa que ingresado el costo 
# de los medicamentos calcule el descuento y el precio final.
costo=float(input("Ingresa el costo: "))
Des=costo*0.1
final=costo-Des
print("El Descunto a Aplicar es: ",Des,"Pago includio descuento ",final)