#2.	Desarrolle el programa que determine si un numero de 3 cifras en capicúa o no
numero = int (input ('Ingresa el valor de numero: '))
if numero%10==(numero%1000-numero%100)//100:
    print ('es capicua.')
else:
    print ('No es capicua.')
