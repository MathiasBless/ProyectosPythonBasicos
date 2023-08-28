#Juego de adivinar numero

import random  #sentencia import permite importar archivos que contienen funciones y elementos utiles


def adivina_el_numero(x):  
    
    print("::::::::::::::::::::::")
    print(" ¡Bienvenid@ al juego! ")
    print("::::::::::::::::::::::")
    print("Tu meta es adivinar el numero generado por la computadora!")
    
    numero_aleatorio = random.randint(1,x) #numero aleatorio entre 1 y x.
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        try:
            #El usuario ingresa un numero 
            prediccion = int(input(f"Adivina el numero entre 1 y {x}: ")) #f-string
            
            if prediccion < numero_aleatorio:
                print("Intenta otra vez,el numero que ingresaste es menor que el numero aleatorio")
                print("============================================================================")
            elif prediccion > numero_aleatorio:
                print("Intenta otra vez,el numero que ingresaste es mayor que el numero aleatorio")
                print("============================================================================")
        except ValueError:
            print("")
            print(".........::::::::::::::::Por favor ingrese un número de tipo entero, gracias::::::::::::::::.................")
            print("")
    print(f"Felicitaciones! ;) adivinaste el numero {numero_aleatorio} correctamente")
    
adivina_el_numero(10)    