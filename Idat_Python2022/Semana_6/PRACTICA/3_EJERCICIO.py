"""Analizar los siguientes ejercicios de condiciones, representarlos mediante algoritmos en Python. """
#3.-Se tiene que evaluar cuatro notas de un alumno, como resultado se visualiza el 
# promedio del alumno junto con su condición de APROBADO o DESAPROBADO, 
# sieste aprobado y con 18 o más, saldrá el siguiente mensaje “Certificado en MSOFFICE”.
Nota01=int(input("Ingresa Nota N°01 : "))
Nota02=int(input("Ingresa Nota N°02 : "))
Nota03=int(input("Ingresa Nota N°03 : "))
Nota04=int(input("Ingresa Nota N°04 : "))
Promedio=(Nota01+Nota02+Nota03+Nota04)/4
if Promedio >=18:
    print("“Certificado en MSOFFICE”")
elif Promedio>=11:
    print("APROBADO")
else:
    print("DESAPROBADO")