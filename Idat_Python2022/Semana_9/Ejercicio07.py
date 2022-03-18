cuenta = 0
for x in range(1,11):
	if x % 2 == 0:
		cuenta = cuenta + 1
		print("Nro. multiplo de 2: ",x)
print("Desde 1 hasta 10 hay ",cuenta," multiplos de 2")