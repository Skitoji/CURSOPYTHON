print("------------------------------------------")
print("------ HOLA, BIENVENIDO A LA TIENDA ------")
print("--------------- DE MANZANAS --------------")
print("------------------------------------------")

# Solicitar el nombre del usuario
print("Ingrese su nombre:")
nombre = input()

# Solicitar el apellido del usuario
print("Ingrese su apellido:")
apellido = input()

# Concatenar el nombre y apellido para formar el nombre completo
nombre_completo = nombre + " " + apellido

# Agradecer al usuario por su visita
print("Gracias por visitarnos", nombre_completo)

# Definir las variables de inventario y precio
manzanas_rojas = 10
manzanas_verdes = 5
manzanas_amarillas = 3
precio_por_manzana = 5

# Mostrar el inventario actual de manzanas y el precio por manzana
print("Actualmente contamos con:", manzanas_rojas, "manzanas rojas,", manzanas_verdes, "manzanas verdes y", manzanas_amarillas, "manzanas amarillas", "", "por un precio de:", precio_por_manzana, "pesos")

# Calcular el total de manzanas
manzanas_totales = manzanas_rojas + manzanas_verdes + manzanas_amarillas 

# Solicitar la cantidad de manzanas que el usuario desea comprar
print("Cuantas manzanas desea comprar?")
cantidad = int(input())

# Solicitar el tipo de manzana que el usuario desea comprar
while True:
    print("-------------------------------------------------")
    print("Que tipo de manzana desea comprar?")
    print("1. Roja")
    print("2. Verde")
    print("3. Amarilla")
    print("4. Salir")
    tipo = int(input())
    break

# Inicializar el precio total de la compra
precio_total = 0

# Verificar el tipo de manzana y la cantidad disponible
if tipo == 1:
    if cantidad <= manzanas_rojas:
        manzanas_rojas -= cantidad
        precio_total = cantidad * precio_por_manzana
        print("Has comprado", cantidad, "manzanas rojas.")
    else:
        print("Lo siento, no tenemos suficientes manzanas rojas.")
elif tipo == 2:
    if cantidad <= manzanas_verdes:
        manzanas_verdes -= cantidad
        precio_total = cantidad * precio_por_manzana
        print("Has comprado", cantidad, "manzanas verdes.")
    else:
        print("Lo siento, no tenemos suficientes manzanas verdes.")
elif tipo == 3:
    if cantidad <= manzanas_amarillas:
        manzanas_amarillas -= cantidad
        precio_total = cantidad * precio_por_manzana
        print("Has comprado", cantidad, "manzanas amarillas.")
    else:
        print("Lo siento, no tenemos suficientes manzanas amarillas.")
elif tipo == 4:
    print("Gracias por tu visita")
else:
    print("Tipo de manzana no válido.")

# Agradecer al usuario por su compra y mostrar el inventario actualizado y el precio total
if precio_total > 0:
    print("Gracias por su compra,", nombre_completo)
    print("Actualmente contamos con:", manzanas_rojas, "manzanas rojas,", manzanas_verdes, "manzanas verdes y", manzanas_amarillas, "manzanas amarillas")
    print("El precio total de su compra es:", precio_total, "pesos")
else:
    print("No se ha realizado ninguna compra.")