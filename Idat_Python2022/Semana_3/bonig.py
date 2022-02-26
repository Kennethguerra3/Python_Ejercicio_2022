#Calcular el salario de un trabajo en funcion a las horas trabajadas y al
#costo por hora; ademas de otorgarle una bonificacion del 10% del salario
#si el salario es menor a 1000 soles. Obtener el Salario Final.

cant_horas = int(input("Cantidad de Horas: "))
costo_horas = float(input("Costo por Horas: "))
salario = cant_horas * costo_horas

if salario < 1000:
    bonif = salario * 0.1
else:
    bonif = 0

salarioF = salario + bonif

print("Salario Base:",salario)
print("Bonificacion:",bonif)
print("Salario Final:",salarioF)
