#	Un alumno desea saber cuál será su calificación final en la materia de Lógica Computacional. Dicha calificación 
#se compone de tres exámenes parciales cuya ponderación es de 30%, 30% y 40%.
Nota1=int(input("Ingresa la Notas N°1 a calcular: "))
Nota2=int(input("Ingresa la Notas N°2 calcular: "))
Nota3=int(input("Ingresa la Notas N°3 calcular: "))
R1=Nota1*0.3
R2=Nota2*0.3
R3=Nota3*0.4
suma=R1+R2+R3
print("El Resultadod de la calificacion es:",suma)