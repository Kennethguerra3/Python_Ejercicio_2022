c = 1
c_m = 0
c_f = 0
mayor = 0
menor = 0

while c <= 5:
    Nombre = input("nombre: ")
    Apellido =input("Apellido: ")
    Sexo = input("Sexo: ")
    Edad = int(input("Ingresa Edad: "))
    if  Sexo == "M":
        c_m=c_m + 1 
    else:
        c_f=c_f + 1
    if Edad >=18:   
        mayor=mayor + 1
    else:
        menor=menor+1
    c=c+1
        
print("Cantidad de varones:", c_m)
print("Cantidad de mujeres: ",c_f)
print("cantidad de mayores de edad: ", mayor)
print("cantidad de menores de edad: ", menor)