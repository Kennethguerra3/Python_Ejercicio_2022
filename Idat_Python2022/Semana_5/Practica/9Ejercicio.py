monto = float(input("Ingresar monto total: "))

if monto >= 500:
invertir = 0.55 * monto
prestamo = 0.30 * monto
credito = 0.15 * monto
else:
invertir = 0.70 * monto
prestamo = 0
credito = 0.30 * monto



interes = credito * 0.20



monto_Pagar = monto + interes



print("Monto total a pagar:",monto_Pagar)
print("Detalle de Pago")
print("***************")
print("Inversion:",invertir)
print("Prestamo al banco:",prestamo)
print("Credito a la fabrica:",credito)
print("Interes por Credito:",interes)