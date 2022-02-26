#Ingresar un numero de 4 digitos; Crea un algoritmo para sumar us digitos.
Numero=int(input("Ingresa el Valor: "))
D1=Numero//1000
r1=Numero%1000
D2=r1//100
r2=r1%100
D3=r2//10
D4=r2%10
Suma=D1+D2+D3+D4
print("El resultado es:",Suma)
print("orden: ",D1,D2,D3,D4)
print("reves",D4,D3,D2,D1)

