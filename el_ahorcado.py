import random

from palabras import palabras


def obtener_palabras_validas(palabras):
    #Se selecciona una palabra al azar de la lista de palabras validas
    palabra = random.choice(palabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra=random.choice(palabras)
    

def juego_ahorcado():
    print(":::::::::::::::::::::::::::::::::")
    print("::::::¡Bienvenido al juego!::::::")
    print(":::::::::::::::::::::::::::::::::")
    
    palabra = obtener_palabras_validas(palabras)