# Un alumno desea saber cuál será su calificación final en cierta materia. Dicha calificación se compone de lo
# siguiente: (7 pts.) 60% corresponde al examen escrito. 20% corresponde a las lecciones 15% corresponde a las
# tareas. 5% corresponde a las prácticas en el laboratorio El dato del examen escrito es un valor entre 0 y 100 y los
# otros datos son valores entre 0 y 10. La calificación final debe ser un valor entre 0 y 20.

""" Modo de desarrollo """
print("=======================================")
print("   CALCULANDO LA CALIFICACION FINAL    ")
print("=======================================")
n_escrtio = float(input("Examen escrito de 0-100: "))
n_lecciones = float(input("lecciones 0-10: "))
n_tareas = float(input("Tareas 0-10: "))
n_practicas = float(input("Laboratorio 0-10: "))

# Calculo de puntaje:
p_escrito = (0.60 * (n_escrtio / 100))
p_lecciones = (0.20 * (n_lecciones / 10))
p_tareas = (0.15 * (n_tareas / 10))
p_practicas = (0.05 * (n_practicas / 10))
# Suma de puntaje:
Puntaje_Final = (p_escrito + p_lecciones + p_tareas + p_practicas)
C_Final = (Puntaje_Final * 20)
print("Puntos obtenido ", round(p_escrito, 3), round(p_lecciones, 3), round(p_tareas, 3), round(p_practicas, 3))
print("Calificacion Final ", C_Final)
