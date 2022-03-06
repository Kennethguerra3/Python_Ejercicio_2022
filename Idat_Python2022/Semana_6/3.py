# cakjsdfkjlsbsdñp
cant = int(input("Ingresar cantidad de Llantas: "))

if cant < 5:
    precio_uni = 30
elif 5 <= cant <= 10:
    precio_uni = 25
else:
    precio_uni = 20

total = cant * precio_uni

print("Precio por Unidad:", precio_uni)
print("Total a pagar:", total)
