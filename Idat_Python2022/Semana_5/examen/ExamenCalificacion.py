#b.	Un alumno desea saber cuál será su calificación final en la materia de Lógica Computacional.
# Dicha calificación se compone de tres exámenes parciales cuya ponderación es de 30%, 30% y 40%. 

print("¡Calculo de calificacion Final de un alumno!")
examen01=float(input("Ingrese nota de examen N° 1 = "))
examen02=float(input("Ingrese nota de examen N° 2 = "))
examen03=float(input("Ingrese nota de examen N° 3 = "))
Peso01=examen01 * 0.3
Peso02=examen02 * 0.3
Peso03=examen03 * 0.4
calificacion=Peso01+Peso02+Peso03
print("Tu Nota de Calificacion es = ", calificacion)
