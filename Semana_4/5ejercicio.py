#5.	Un vendedor recibe mensualmente un sueldo base más un 10% 
# extra por comisión de sus ventas. El vendedor desea saber cuánto 
# dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y
# el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo=float(input("Ingresa el Sueldo: "))
venta01=float(input("Ingrese venta N° 01: "))
venta02=float(input("Ingrese venta N° 02: "))
venta03=float(input("Ingrese venta N° 03: "))
incremento=0.10
sumaventa=venta01+venta02+venta03
opincremento=sumaventa*incremento
final=sueldo+opincremento
print("el Incremento de 10% es igual= ", opincremento)
print("Total sueldo a recibir + incremento es = ", final)
