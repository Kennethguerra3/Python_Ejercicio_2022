#3.	Un estudiante recibe una propina mensual S/. 20.
# El estudiante rinde mensualmente dos exámenes. 
# Su papá ha decidido incentivarlo dándole una propina adicional de S/. 5 
# por cada examen aprobado. Desarrolle el programa que determine el monto total de la propina.

ex01=int(input("Ingrese Nota aprobatoria N°1: " ))
ex02=int(input("Ingrese Nota aprobatoria N°2: " ))
if ex01 >10:
    propina=5
else:
    propina=0
mensula=20
PropinaR01=propina
if ex02 >10:
    propina02=5
else:
    propina02=0
PropinaR02=propina02
suma=PropinaR01+PropinaR02
MontoTota=suma+mensula
print("Total Propina es =", suma,"Total Monto de propina",MontoTota)
