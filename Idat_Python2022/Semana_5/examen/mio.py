edad=int(input("Ingrese tu edad: "))
sueldo=float(input("Ingresa tu sueldo: "))
if edad<15:
    edad01=sueldo+100
    print("recibes un bono de 100","total a recibir es ",edad01)
elif edad>=20:
    edad02=sueldo+300
    print("Recibes un bono de 300","total a recibir es ",edad02)
elif edad>=40:
    edad03=sueldo+600
    print("Recibes un bono de 600","tota a recibir es ",edad03)
else:
    print("no cumples causa para ningun Bono")


