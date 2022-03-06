# Un alumno desea saber cuál será su calificación final en cierta materia. Dicha calificación se compone de lo siguiente: 
# (7 pts.) 
# 60% corresponde al examen escrito. 
# 20% corresponde a las lecciones 
# 15% corresponde a las tareas. 
# 5% corresponde a las prácticas en el laboratorio 
# El dato del examen escrito es un valor entre 0 y 100 y los otros datos son valores entre 0 y 10.
# La calificación final debe ser un valor entre 0 y 20. 

ex_exrito=int(input("Ingrese nota examen escrito: "))
nota=int(input("ingrese nota de lecciones"))
tarea=int(input("ingrese nota de tarea: "))
laboratorio=int(input("Ingrese nota de laboratorio: "))
if ex_exrito >= 0 and 20:
    