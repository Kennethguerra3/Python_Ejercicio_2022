#1.	Desarrolle el programa que determine el porcentaje de varones y de mujeres que hay en un salón de clases.
Varones=float(input("Cantidad de Varones: "))
Mujeres=float(input("Cantidad de Mujeres: "))
Total=Varones+Mujeres
Porcen_Mujer=Varones/Total
porce_Hombre=Mujeres/Total
print("Porcentaje Varones: ",porce_Hombre)
print("Porcentaje Mujeres: ", Porcen_Mujer)