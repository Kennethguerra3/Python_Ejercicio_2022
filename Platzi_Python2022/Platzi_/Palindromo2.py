def palindromo(Palabra):
    palabra = palabra.replace(' ',' ')
    palabra = palabra.lower()
    palabra_Invertida=palabra[::-1]
    if palabra == palabra_Invertida:
        return True
    else:
        return False
    
    
def run():
    palabra=input('Escribe una palabra:')
    es_palindromo= palindromo(palabra)
    if es_palindromo == True:
        print("Es Palindromo")
    else:
        print("No es Palindromo")
        
                
if __name__ == "__main__":
     run()

















