#2.	Desarrolle el programa que, dada la capacidad de un disco duro en gigabytes, 
# lo convierta a megabytes, kilobytes y bytes. 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB.
gigabytes=float(input("Ingrese El Varlo Disco Duro en gigabytes: "))
megabytes=1024*gigabytes
kilobytes=megabytes*1024
bytes=kilobytes*1024
print("megabytes es: ",megabytes)
print("kilobytes es:",kilobytes)
print("bytes es:",bytes)




