"""
#Random = Genera numeros aleatorios
import random

#randint(min, max) = Genera un numero aleatorio entre min y max

resultado = random.randint(1, 100)
print(resultado)
"""
def saludar_y_sumar(nombre, num1=0, num2=0): # =0 es un valor por defecto
    print(f"Hola, {nombre}! El resultado de la suma es: {num1 + num2}")

saludar_y_sumar("Samuel", 6, 6)
saludar_y_sumar("Juan", 10, 10)
saludar_y_sumar("Rodrigo", 20, 20)
