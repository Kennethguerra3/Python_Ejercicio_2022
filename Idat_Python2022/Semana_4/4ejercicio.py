#4.	Hacer un programa que ingresado el costo de los medicamentos calcule el 
# descuento y el precio final. (Descuento es el 10% del costo).

Costo=float(input("Ingresa el Valor del Medicamento: "))
dsto=0.10
resulta=round(dsto * Costo, 2)
final= Costo - resulta
print("El descuento es de: ", resulta)
print("Importe a pagar es: ",final)