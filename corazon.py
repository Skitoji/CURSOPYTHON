import math
from turtle import *
import time

start_time = time.time()

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 11.8 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")
color("red")
penup()

i = 0
while time.time() - start_time < 20 or i < 100:
    x = hearta(i / 10) * 20
    y = heartb(i / 10) * 20
    goto(x, y)
    pendown()
    i+=1

done()