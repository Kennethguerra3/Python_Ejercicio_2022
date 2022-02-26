#a.	Escribir un programa que calcule el salario de un trabajador de la manera siguiente. 
# El trabajador cobra un precio fijo por hora y se le descuento el 15% en concepto de impuesto sobre la renta. 
# El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio que cobra por hora. 
# Como salida debe imprimir el sueldo bruto, el descuento de renta y el salario a pagar. 
print("Programa que calcla el salario de un trabajdor")

N_Trabajador=str(input("Ingresa el Nombre del trabajador= "))
Horas_Trabajada=int(input("Ingresa las horas trabajadas = "))
precio_Fijo=float(input("Ingrese el Precio por hora= "))
impuesto=0.15
resultado=Horas_Trabajada*precio_Fijo
renta=resultado*impuesto
f_pagar=resultado-renta

print(N_Trabajador, "El sueldo bruto calculado es = ",resultado,"La renta descontada es ", renta,"Salario a pagar ", f_pagar)
