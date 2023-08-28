import random


def jugar():
    while True:
        usuario = input(f"Ingrese una opcion, 'pi' para piedra, 'pa' para papel y 'ti' para tijera. Si deseas salir solo escribe salir \n").lower() #El usuario elije su opcion
        
        adios_usuario = "::::::¡Gracias por jugar!::::::::"
        
        if usuario == 'salir':
            return adios_usuario #Mensaje de gracias por jugar.
        
        if usuario not in ['pi', 'pa', 'ti']:
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("::¡Opcion invalida! por favor escriba: 'pi' , 'pa' , 'ti' o 'salir'::")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            continue #Vuelve al inicio del bucle si la opcion ingresada es invalida
        
        computadora = random.choice(['pi', 'pa', 'ti']) #La computadora eligira su opcion (un string) de la lista,al azar.
        
        if usuario == computadora:
            print(f'¡Empate! porque el computador tambien eligio {computadora}')
        
        elif gano_el_jugador(usuario, computadora):
            print(f'¡Ganaste! porque el computador eligio {computadora}')
        else:
            print(f'¡Perdiste! porque el computador eligio {computadora}')


def gano_el_jugador(jugador,oponente):
    #Esta funcion retornara True si es que gana el jugador.
    # Piedra gana a tijera (pi > ti)
    # Tijera gana a papel (ti > pa)
    # Papel le gana a la piedra (pa > pi)
    
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    
    
print(jugar())