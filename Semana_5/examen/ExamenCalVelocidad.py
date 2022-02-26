#e.	Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia
# entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar
# en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
print("Calculo de velocidad de vehiculos:")

d=float(input("Ingrese la distancia v1 : "))
v1=float(input("Introduce la velocidad (km/h) V1: "))
d2=float(input("Ingrese la distancia de V2:"))
v2=float(input("Introduce la velocidad (km/h) V2:  "))

tiempov01=round(d/v1)
tiempov02=round(d2/v2)
print("La Diferencia de tiempo entre ambos vehiculos es: ","V1=",format(tiempov01),"y", "V2=",format(tiempov02))