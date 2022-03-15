c=1 
menor = 9999
while True:
	numero =int(input())
	#condicion para obtener el menor
	if numero < menor and numero != 0:
		menor = numero 
 	#condicion para detener el bucle
	if numero ==0:
		break
	c=c+1
print("Menor:",menor)