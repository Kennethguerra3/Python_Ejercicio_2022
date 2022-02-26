#1.	Escribe un programa que lea una cantidad depositada en un banco 
# y que calcule la cantidad final después de aplicarle un 20% de interés.
c_deposito=float(input("Ingresa la Cantidad a depositar: "))
final=(c_deposito*0.2)
suma=round(c_deposito+final)
print("El Interes Ganado es:",final,"Total Estado de cuenta",suma)

