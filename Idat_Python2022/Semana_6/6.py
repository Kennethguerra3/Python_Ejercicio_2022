edad = int(input("Edad: "))

if edad <= 3:
   print("Bebe")
elif edad <= 10:
   print("Niño")
elif edad <= 15:
   print("Puber")
elif edad <= 18:
   print("Adolescente")
elif edad <= 30:
   print("Joven")
elif edad <= 65:
   print("Adulto")
else:
   print("Adulto mayor")
