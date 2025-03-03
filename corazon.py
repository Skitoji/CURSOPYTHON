import math
from turtle import *
import time

# Guarda el tiempo de inicio
start_time = time.time()

# Define la función hearta que calcula la coordenada x del corazón
def hearta(k):
    return 15 * math.sin(k) ** 3

# Define la función heartb que calcula la coordenada y del corazón
def heartb(k):
    return 11.8 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Configura la velocidad de la tortuga al máximo
speed(0)
# Establece el color de fondo de la ventana de dibujo a negro
bgcolor("black")
# Establece el color del lápiz a rojo
color("red")
# Levanta el lápiz para que la tortuga no dibuje mientras se mueve
penup()

# Inicializa la variable i a 0
i = 0
# Inicia un bucle while que se ejecuta durante 20 segundos o hasta que i sea menor que 100
while time.time() - start_time < 20 or i < 100:
    # Calcula la coordenada x utilizando la función hearta y escala el resultado
    x = hearta(i / 10) * 20
    # Calcula la coordenada y utilizando la función heartb y escala el resultado
    y = heartb(i / 10) * 20
    # Mueve la tortuga a la posición (x, y)
    goto(x, y)
    # Baja el lápiz para que la tortuga dibuje mientras se mueve
    pendown()
    # Incrementa el valor de i en 1
    i += 1

# Finaliza el dibujo y mantiene la ventana abierta hasta que el usuario la cierre
done()