#5.	Un vendedor recibe mensualmente un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
# que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo=float(input("Ingresa el sueldo Base: "))
Venta01=float(input("Ingresa el Venta 01 "))
venta02=float(input("Ingresa el venta 02 "))
venta03=float(input("Ingresa el venta 03 "))
ventas=venta02+Venta01+venta03
comi=ventas*0.1
total=sueldo+comi
print("Comision a recibir por venta de ",ventas,"es:",comi)
print("Total Sueldo a percibir es: ",total)