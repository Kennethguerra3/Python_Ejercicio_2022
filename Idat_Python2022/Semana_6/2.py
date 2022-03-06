# Calcular la bonificacion en funcion al sueldo basico y a los años
# trabajados:asasasasadadadadq
# Si sueldo >= 3000 y años >= 10 : 5%
# Si sueldo >= 2000 y años >= 8 : 8%
# caso contrario : 10%

s_basico = float(input("Ingresar sueldo basico: "))
year = int(input("Ingresar años trabajados: "))
if s_basico >= 3000 and year >= 10:
    bonif = s_basico * 0.05
elif s_basico >= 2000 and year >= 8:
    bonif = s_basico * 0.08
else:
    bonif = s_basico * 0.10

s_final = s_basico + bonif

print("Bonificacion:", bonif)
print("Sueldo Final:", s_final)
