#5.	Se tiene un monto en soles, deberá de mostrarlo en dólares. 
#Conversor de cambio de divisas
Soles=float(input("Cuanto es el Valor Soles: S/ "))
Valor_Dolar=3.84
Dolar=Soles/Valor_Dolar
Dolar=round(Dolar,2)
Dolar=str(Dolar)
print("El tipo de Cambio a Dolar es $",Dolar)
