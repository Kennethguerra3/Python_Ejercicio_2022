def palindromo(palabra):
    palabra = palabra.replace(' ',' ')
    palabra = palabra.lower()
    palabra_inverter = palabra[::-1]
    if palabra == palabra_inverter:
        return True
    else:
        return False

def pali_run():
    palabra = input("Ingresa Una Palabra:  ")
    es_pali= palindromo(palabra)
    if es_pali == True:
        print('Es palindrome')
    else:
        print('No es palindromo')
if __name__=='__main__':
    pali_run()