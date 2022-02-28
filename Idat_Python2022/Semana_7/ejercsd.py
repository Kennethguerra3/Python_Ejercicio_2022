#Practicxa de ejercicio
Edad=int(input("Ingrese la edad: "))
if 40 >= Edad:
    Bono = 300
    print("Excelente tienes un bono de S/ 300.")
elif 50 >= Edad:
    Bono = 400
    print("Excelente tienes un bono de S/ 400.")
elif 80 >= Edad:
    Bono = 600
    print("Excelente tienes un bono de S/ 600.")
elif 90 >= Edad:
    Bono = 700
    print("Excelente tienes un bono de S/ 700.")
else:
    print("Lamento No hay bono para este rango de edad.!")

