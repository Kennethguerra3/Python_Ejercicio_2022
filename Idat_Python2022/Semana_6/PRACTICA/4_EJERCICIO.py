"""Analizar los siguientes ejercicios de condiciones, representarlos mediante algoritmos en Python. """
#4.-Determinar la cantidad de dinero que recibirá un trabajador por concepto de las 
# horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, 
# el resto se consideran horas extras y que estas se pagan al doble de una hora normal cuando no exceden de 8; 
# si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se pagan las horas normales y
# el resto al triple.
Pago_Hora=int(input("Pago por Hora es : "))
horas_lab=int(input("Ingrese las horas laboradas: "))
hor_extra=horas_lab-40
Triple=hor_extra-8
doble_horas=hor_extra-Triple

if horas_lab <=40:
    pago=Pago_Hora*horas_lab
elif horas_lab >40:
   pago=(Triple*(Pago_Hora*3))+(doble_horas*(Pago_Hora*2))+((horas_lab-hor_extra)*Pago_Hora)
else:
   print("Ingresa datos")
    
print("Total Horas Extras ", hor_extra,"doble horas es", doble_horas," horas para triple ",Triple)
print("Pago Total es de ", pago)