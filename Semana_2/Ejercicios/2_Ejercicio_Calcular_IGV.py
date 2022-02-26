#2.	Programa que pida el precio de un artículo y calcule su valor aplicándole un 18% de IGV. 
Precio=float(input("Ingresa Precio Neto de Articulo:"))
IGV=Precio*0.18
Total_Valor=Precio+IGV
print("El IGV Calculado es:",IGV)
print("El Valor del Articulo Incluido IGV:",Total_Valor)