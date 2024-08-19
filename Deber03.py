import random

# Variables globales para el rango y los intentos máximos
rango_minimo = 1
rango_maximo = 100
intentos_maximos = 5

# Función para configurar el juego
def configurar_juego():
    global rango_minimo, rango_maximo, intentos_maximos
    
    rango_minimo = int(input("rango mínimo para el número secreto: "))
    rango_maximo = int(input("rango máximo para el número secreto: "))
    intentos_maximos = int(input("número máximo de intentos: "))
    
    if rango_minimo >= rango_maximo:
        print("Error: El rango mínimo debe ser menor que el rango máximo.")
        return configurar_juego()
    
    if intentos_maximos <= 0:
        print("Error: El número máximo de intentos debe ser mayor que cero.")
        return configurar_juego()

# Función principal del juego
def adivinar_numero():
    configurar_juego()
    
    numero_secreto = random.randint(rango_minimo, rango_maximo)
    intentos_restantes = intentos_maximos
    
    print(f"Adivina el número entre {rango_minimo} y {rango_maximo}.")
    
    while intentos_restantes > 0:
        intento = int(input(f"Te quedan {intentos_restantes} intentos. Ingresa tu intento: "))
        
        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print("¡Felicidades! acertastes el número secreto.")
            break
        
        intentos_restantes -= 1
    
    if intentos_restantes == 0:
        print(f"Lo siento, sigue intentando. El número secreto era {numero_secreto}.")

# Llamada a la función principal del juego
adivinar_numero()