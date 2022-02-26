"""Analizar los siguientes ejercicios de condiciones, representarlos mediante algoritmos en Python. """
#1.-Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
Numero01=int(input("Ingresa El N° 01="))
Numero02=int(input("Ingresa El N° 02="))
if Numero01==Numero02 :
    resultado=Numero01*Numero02
elif Numero01 >Numero02:
    resultado=Numero01-Numero02
else:
    resultado=Numero01+Numero02
print("Resultado de comprativo: ", resultado)
    