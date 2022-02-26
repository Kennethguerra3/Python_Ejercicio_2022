#8.	Una institución social recibe anualmente una donación que reparte de la siguiente forma: 
# 25% para el centro de salud, 35% en el comedor infantil, 25% para la escuela infantil y 
# el resto para el asilo de ancianos.  Desarrolle el programa que muestre los montos asignados.
Donacion=float(input("Ingrese el monto de la donacion: "))
salud=Donacion*0.25
comedor=Donacion*0.35
infantil=Donacion*0.25
ancianos=Donacion*0.15
print("El presupuesto donado para Salud es: ",salud)
print("El presupuesto donado para comedor es: ",comedor)
print("El presupuesto donado para ifantil es: ",infantil)
print("El presupuesto donado para ancianos es: ",ancianos)
