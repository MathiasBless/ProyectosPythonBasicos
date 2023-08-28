import random


def adivina_el_numero_pc(x):
    
    print("::::::::::::::::::::::::::::::")
    print("    BIENVENIDO AL JUEGO    ")
    print("::::::::::::::::::::::::::::::")
    print(f"Piensa en un numero entre 1 y {x} para que el pc intente adivinarlo...")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        try:
            #Generar prediccion
            if limite_inferior != limite_superior:
                prediccion = random.randint(limite_inferior,limite_superior)
            else:
                prediccion = limite_inferior #tambien puede ser el limite superior
                
            #Obtener respuesta del usuario
            respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A), si es muy baja, ingresa (B). Y si es correcta ingresa (C): ").lower()
            
            if respuesta == "a":
                limite_superior = prediccion - 1
            elif respuesta == "b":
                limite_inferior = prediccion + 1
            #Intervalo inicial: [1,10]
            #Prediccion de computadora: 6
            #Respuesta: a (numero demasiado alto)
            #Entonces actualizamos el intervalo cambiando el limite superior [1,5]
                
        except ValueError:
            print("")
            print(".........::::::::::::::::Por favor ingrese un string, gracias::::::::::::::::.................")
            print("")             
    print(f"¡Asi se hace! ¡la computadora adivino el número correctamente!: {prediccion}") 
        
adivina_el_numero_pc(30)    

