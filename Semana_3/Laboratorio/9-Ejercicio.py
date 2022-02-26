#9.	Juan, Raquel y Daniel aportan cantidades de dinero para formar un capital. 
# Juan y Raquel aportan en dólares y Daniel, en soles. Desarrolle el programa que
# determine el capital total en dólares y que porcentaje de dicho capital aporta cada uno. Dólar = S/. 3.00 nuevos soles.
j=float(input("Aporte de Juan sera $: "))
r=float(input("Aporte de Raquel sera $: "))
d=float(input("Aporte de Danielsera S/: "))

dolar=3
Daniel=d/dolar
suma=round(j+r+Daniel,3)

j_p=round(j/suma,4)
r_p=round(r/suma,4)
Daniel_p=round(Daniel/suma,4)
print("El Capital Total en Dolar es:",suma)
print("El porcentaje por cada aportante es","Juan:",j_p,"Ranquel:",r_p,"Daniel:",Daniel_p)
