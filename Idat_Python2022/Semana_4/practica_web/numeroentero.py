#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números 
# debe devolver un aviso de error y si el divisor es cero también.

n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")