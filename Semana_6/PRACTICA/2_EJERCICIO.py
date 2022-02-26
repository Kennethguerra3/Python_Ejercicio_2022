"""Analizar los siguientes ejercicios de condiciones, representarlos mediante algoritmos en Python."""
#2.-Determine el tiempo de servicio de acuerdo con el año de ingreso. Si el trabajador tiene
#menos de 4 años el tendrá un aumento del 15% de su sueldo básico, en caso contrario
#tendrá un aumento del 12% por cada año. Muestre el Monto a Cobrar.
Sueldo=int(input("Ingresa el Sueldo Base: "))
T_Inicial=int(input("Año de ingreso: "))
T_Final=int(input("Ingrese año Final: "))
Tiempo_S=T_Final-T_Inicial
if Tiempo_S <=3:
    aumenta=0.15
    ope=(Sueldo*aumenta)+Sueldo
else:
    aumenta=0.12
    Incre=Tiempo_S*aumenta
    ope=(Incre*Sueldo)+Sueldo
print("Sueldo es: ",Sueldo,"Incremento es de: ",aumenta)
print("Años de servicio",Tiempo_S)
print("Monto a Cobrar es de : ",ope)




 