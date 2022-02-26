monto = float(input("Ingresar monto presupuestal: "))
area = input("Ingresar Area: ")

if area == "urgencias":
    presupuesto = monto * 0.37
elif area == "pediatria":
    presupuesto = monto * 0.42
elif area == "traumatologia":
    presupuesto = monto * 0.21
else:
    presupuesto = 0
print("Area no existe.")

print("Presupuesto:",presupuesto)
