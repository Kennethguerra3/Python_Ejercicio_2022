#7.	Escribir un programa que calcule el salario de un trabajador de la manera siguiente. 
# El trabajador cobra un precio fijo por hora y se le descuento el 10% en concepto de 
# impuesto sobre la renta. El programa debe pedir el nombre del trabajador, las horas 
# trabajadas y el precio que cobra por hora. Como salida debe imprimir el sueldo bruto, 
# el descuento de renta y el salario a pagar. 

from ast import Str


print("Calculo del Salario de un Trabajdor")
N_trabajador=str(input("Nombre del Trabajador: "))
Hora=float(input("Indica las Horas Trabajadas= "))
Precio_Hora=float(input("Indica Precio por Hora= "))
Sueldo_B=Precio_Hora*Hora
Dsto=Sueldo_B*0.10
Pago=Sueldo_B-Dsto
print("El Calculo del Trabajador ",N_trabajador)
print("Sueldo Bruto Calculado es= ",Sueldo_B)
print("Descuento de Renta es =", Dsto)
print("Total Salario a pagar es=",Pago)
