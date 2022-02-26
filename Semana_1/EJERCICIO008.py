#Ingresar la edad de 5 alumnos y mostrar la mayor y menor edad.
ALUMNO1=float(input("Ingresar su edad 1:"))
ALUMNO2=float(input("Ingresar su edad 2:"))
ALUMNO3=float(input("Ingresar su edad 3:"))
ALUMNO4=float(input("Ingresar su edad 4:"))
ALUMNO5=float(input("Ingresar su edad 5:"))

ALUMNOS=[ALUMNO1, ALUMNO2, ALUMNO3, ALUMNO4, ALUMNO5]
max_value=max(ALUMNOS)
min_value=min(ALUMNOS)

print("Alumno Mayor edad es:", max_value)
print("Alumno Menor edad es:", min_value)

