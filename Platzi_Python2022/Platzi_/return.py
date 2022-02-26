import random

is_game = True

def conversacion(mensaje):
  if mensaje == 'piedra':
    return 1
  elif mensaje == 'papel':
    return 2
  elif mensaje == 'tijera':
    return 3
  else:
    return 0

def quien_gano(oponente, ususario):
  if oponente == 1 and usuario == 2:
    return 'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 2 and usuario == 1:
    return 'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == 1 and usuario == 3:
    return 'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == 3 and usuario == 1:
    return 'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 2 and usuario == 3:
    return 'YASSSSS GANASTEEEEE 🎉🎉'
  elif oponente == 3 and usuario == 1:
    return 'NOOOO PANAAAA PERDISTEEEE'
  elif oponente == usuario:
    return 'lol fue un empate equisde'
  elif oponente == 0 or usuario == 0:
    return 'Error watafak ???????'
  else:
    return 'Error???????'

def seguir_jugando(respuesta):
  if respuesta == 'si':
    return True
  else:
    return False

