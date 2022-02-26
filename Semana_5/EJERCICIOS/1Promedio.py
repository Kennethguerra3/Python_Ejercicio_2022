"""1.	El promedio final de un curso se obtiene en base al promedio
simple de tres prácticas calificadas. Para ayudar a los alumnos, el profesor 
del curso ha prometido incrementar en dos puntos la nota de la tercera  práctica calificada,
si es que esta no es menor que 10. Desarrolle el programa que determine el promedio final de un
alumno conociendo sus tres notas. 
from typing import final"""

practica01=int(input("Ingrese Nota Practica N°1: "))
practica02=int(input("Ingrese Nota Practica N°2: "))
practica03=int(input("Ingrese Nota Practica N°3: "))

if practica03 >10:
   puntos= practica03+2
else:
    puntos= practica03
    
suma=(practica01+practica02+puntos)
promedio=suma/3

print("Promedio Final", promedio)
