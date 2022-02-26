#Ingresar un numero de 3 digitos; Crea un algoritmo para sumar us digitos.
Numero=int(input("Ingrese el Valor: "))
D1=Numero//100
r1=Numero%100
D2=r1/10
D3=r1%10
suma=D1+D2+D3
print("El resultado es:",suma)
