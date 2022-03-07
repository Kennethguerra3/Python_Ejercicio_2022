# Un alumno desea saber cuál será su calificación final en cierta materia. Dicha calificación se compone de lo
# siguiente: (7 pts.) 60% corresponde al examen escrito. 20% corresponde a las lecciones 15% corresponde a las
# tareas. 5% corresponde a las prácticas en el laboratorio El dato del examen escrito es un valor entre 0 y 100 y los
# otros datos son valores entre 0 y 10. La calificación final debe ser un valor entre 0 y 20.
print("=======================================")
print("   CALCULANDO LA CALIFICACION FINAL    ")
print("=======================================")
n_escrtio = float(input("Examen escrito de 0-100: "))
n_lecciones = float(input("lecciones 0-10: "))
n_tareas = float(input("Tareas 0-10: "))
n_practicas = float(input("Laboratorio 0-10: "))

# Calculo de la Nota:
final = ((n_escrtio / 100) * 60) + ((n_lecciones / 10) * 20) + ((n_tareas / 10) * 15) + ((n_practicas / 10) * 5)

# Ponderado por base sobre 20:
nota = (final * 20) / 100
print("Calificacion Final |sobre 20|:", round(nota, 1))
