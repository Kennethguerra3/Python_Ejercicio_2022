# Crear una tabla de multiplcar
print("============================")
print("*   CREA TU CALENDARIO     *")
print("============================")
c = 1
numero = int(input("Numero: "))
while c <= 12:
    x = numero * c
    print(numero, " X ", c, " = ", x)
    c = c + 1
