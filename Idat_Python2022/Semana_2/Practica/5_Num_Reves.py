#Dado un número natural de cuatro cifras, 
# desarrolle el programa que permite obtener el número al revés. Ejemplo 1234  =>4321.
Numero=int(input("Ingresa Valor Entero 4 crifras: "))
N4= Numero%10
N3=int((Numero%100)/10)
N2=int((Numero%1000)/100)
N1=int((Numero-(Numero%1000))/1000)
print("El Numero Al reves es : ",N4,N3,N2,N1)