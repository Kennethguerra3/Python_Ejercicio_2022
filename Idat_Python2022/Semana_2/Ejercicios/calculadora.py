
def operations():
    value1 = int(input("Inserta el primer valor: "))
    value2 = int(input("Inserta el segundo valor: "))
    result = str(value1 + value2)
    print("El resultado es:" + " " + result)

def operations2():
    value1 = int(input("Inserta el primer valor: "))
    value2 = int(input("Inserta el segundo valor: "))
    result = str(value1 - value2)
    print("El resultado es:" + " " + result)

def operations3():
    value1 = int(input("Inserta el primer valor: "))
    value2 = int(input("Inserta el segundo valor: "))
    result = str(value1 * value2)
    print("El resultado es:" + " " + result)

def operations4():
    value1 = float(input("Inserta el primer valor: "))
    value2 = float(input("Inserta el segundo valor: "))
    result = value1 / value2
    result = str(round(result,4))
    print("El resultado es:" + " " + result)

menu = """
Hola, bienvenido a la calculadora creada por Kenneth, porfavor escoge la operacion que voy a realizar: \n
1 - Suma
2 - Resta
3 - Multiplicacion
4 - Division

Elige una opcion: """

option = int(input(menu))

if option == 1:
    operations ()

elif option == 2:
    operations2()

elif option == 3:
    operations3()

elif option == 4:
    operations4()

else:
    print("No se hacer esta operacion aun, pero pronto!!!")