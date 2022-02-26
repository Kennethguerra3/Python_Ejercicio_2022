#5.	Un supermercado ha puesto en oferta la venta al por 
# mayor de cierto producto, ofreciendo un descuento del 15% por
# la compra de más de 3 docenas y 10% en caso contrario. Además, 
# por la compra de más de 3 docenas se obsequia una unidad del producto
# por cada docena en exceso sobre 3. Diseñe un algoritmo que determine el 
# monto de la compra, el monto del descuento, el monto a pagar y el número de unidades
# de obsequio por la compra de cierta cantidad de docenas del producto.
producto=str(input("Ingresa el producto: "))
Cantidad=float(input("Ingresa La candidad: "))
precio=float(input("Ingrese Precio: "))
if Cantidad>=36:
    descuento=0.15
else:
    descuento=0.10  
Neto=Cantidad*precio
descuentoresultado=Neto*descuento
totalPagar=Neto-descuentoresultado
print("Se Aplicac un Descuento de ",descuento)
print("Total Descuento es : ",descuentoresultado,"Total a pagar seria: ", totalPagar )

if Cantidad>=36:
    bono=1
else:
    bono:0
totalCantidad=Cantidad+bono
print("Unidades compradas",Cantidad)
print("Total unidades de obsequi es = ", bono)