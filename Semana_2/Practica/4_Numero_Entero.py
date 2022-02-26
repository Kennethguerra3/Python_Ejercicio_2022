#4.	Desarrolle el programa que lea un número 
#entero y determine la suma de sus cifras. Asumir que el número es positivo y de 4 cifras.
Numero=int(input("Ingresa Valor Entero 4 crifras: "))
N4= Numero%10
N3=int((Numero%100)/10)
N2=int((Numero%1000)/100)
N1=int((Numero-(Numero%1000))/1000)
Suma=N1+N2+N3+N4
print(N4)
print(N3)
print(N2)
print(N1)
print("la Suma es : ",Suma)



