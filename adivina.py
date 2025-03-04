import random

def tirar_dados():
    return random.randint(2, 12)

def pedir_respuesta():
    print("Ingresa tu prediccion")
    print("1. Par")
    print("2. Impar")
    print("3. Salir")

    return input("Tu respuesta: ")
    pass

def imprimir_resultado(numero, prediccion):
    #not, % (modulo)
    #Saber si el numero es par o impar
    #Dividirlo entre 2 y si el remanente es 0 es par, si no es impar
    #resultado 5/2: Resultado 2 con remanente 1
    #resultado 4/2: Resultado 2 con remanente 0
    es_par = numero % 2 == 0
    #es_par, prediccion = 1: Gane
    #No es par, prediccion = 2: Gane
    #Perdi
    if es_par and prediccion == 1:
        print(f"El numero fue {numero}, es par. ¡Ganaste!")
    elif not es_par and prediccion == 2:
        print(f"El numero fue {numero}, es impar. ¡Ganaste!")
    else:    
        print(f"El numero fue {numero}. ¡Perdiste!")    
    pass

while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    if prediccion == "3":
        break
    imprimir_resultado(numero, prediccion)

print("¡Gracias por jugar!")

#print("Tirando los dados...", tirar_dados())