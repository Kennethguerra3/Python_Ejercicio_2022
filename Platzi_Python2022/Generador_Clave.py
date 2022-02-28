from random import SystemRandom

longitud = 30
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

cryptogen = SystemRandom()
p = ""

while longitud > 0:
    p = p + cryptogen.choice(valores)
    longitud = longitud - 1

print(p)























































