#ciclo (iteracion o bloque de codigo que se repite varias veces)
# for, while
# for: se usa cuando sabemos cuantas veces se va a repetir el bloque de codigo
#while: se usa cuando no sabemos cuantas veces se va a repetir el bloque de codigo
"""
i = 0
while i < 10:
    if i < 5:
        print(i, "es menor que 5")
    else: 
        print(i, "es mayor o igual que 5")

    i += 1  # i = i + 1
print("fin del ciclo while")
"""

#for x in range(1, 10): #range(1,10) genera una lista de numeros del 1 al 9
#    print(x)

while True:
    print("Escribe la opcion que deseas")
    print("1) Saludar")
    print("2) Salir")

    respinput = input()

    if respinput == "1":
        print("Hola, como estas?")
    elif respinput == "2":
        break

print("Fin del programa")
