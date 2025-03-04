from datetime import datetime

# Imprime el mensaje de bienvenida
print("*************************")
print("**  Bienvenido a la tienda  **")
print("**     de Mascotas     **")
print("*************************")

# Define las variables de inventario
inventario = {
    "Perro": 10, 
    "Gato": 5, 
    "Pajaro": 3,
    "Iguana": 2,
    }

# Calcula el total de animales
animales_totales = 0
for val in inventario.values():
    animales_totales += val

# Solicita el nombre y apellido del usuario
print("Cual es tu nombre?")
nombre = input()
print("Por favor ingresa tu apellido")
apellido = input()

# Concatena el nombre y apellido para formar el nombre completo
nombre_completo = nombre + " " + apellido # "Juan" + " " + "Perez" = "Juan Perez" #El espacio se agrega con " "

# Agradece al usuario por su visita
print("Gracias por visitarnos", nombre_completo)

compras = []  # Inicializa la lista de compras

# Define la función para mostrar el menú
def mostrar_menu():
    print("")
    print("*************************")
    print("Selecciona la opcion que deseas:")
    print("1. Conocer cuantos animales hay")
    print("2. Comprar un animal")
    print("3. Mostrar Compras")
    print("4. Salir")
    print("5. Agregar nuevo inventario (Solo empleados)")

# Define la función para mostrar el inventario
def mostrar_inventario():
    print("***Inventario de la tienda***")
    for llave, valor in inventario.items():
        print(f"  {llave}: {valor}")
    print("En total tenemos", animales_totales, "mascotas") 

# Define la función para comprar un animal
def comprar_animal():
    carrito = []  # Inicializa el carrito de compras

    while True:
        print("Que tipo de animal deseas comprar? Solo puedes elegir 1 de cada especie")
        print("Escribe F para terminar la compra, o V para ver tu carrito")
        animal = input()

        if animal == "F": break  # Termina la compra si el usuario escribe "F"

        if animal == "V":
            print(f"Tu carrito tiene {carrito}")  # Muestra el contenido del carrito
            continue

        if animal not in inventario:
            print(f"Lo sentimos no contamos con el animal {animal}")  # Informa al usuario si la especie no existe
        elif inventario[animal] == 0:
            print(f"Lo sentimos no contamos con {animal} en existencia")  # Informa al usuario si no hay animales disponibles
        elif animal not in carrito:
            carrito.append(animal)  # Agrega el animal al carrito si no está ya en él
        else:
            print("Ese animal ya esta en tu carrito")  # Informa al usuario si el animal ya está en el carrito

    # Muestra el contenido final del carrito
    print("El contenido de tu carrito es:")
    for animal in carrito:
        print("   ", animal)
        inventario[animal] -= 1 

    # Agrega los animales comprados al carrito de compras
    fecha = datetime.now()
    compras.append((nombre_completo, carrito, fecha))
    # Compras tiene longitud 1 porque solo tengo 1 compra
    # Tupla: Nombre, Carrito, Fecha

# Define la función para mostrar las compras realizadas
def mostrar_compras():
    print("")
    print("****Compras realizadas****")
    for compra in compras:  # Compra = tupla que tiene nombre, carrito y fecha
        print(f"   {compra[0]} compro {compra[1]} el {compra[2]}")

# Define la función para agregar nuevo inventario
def agregar_inventario():
    password = input("Ingrese la contraseña de empleado: ")
    if password == "empleado123":  # Verifica la contraseña
        nuevo_animal = input("Ingrese el nombre del nuevo animal: ")
        cantidad = int(input("Ingrese la cantidad de animales: "))
        if nuevo_animal in inventario:
            inventario[nuevo_animal] += cantidad  # Si el animal ya existe, suma la cantidad
        else:
            inventario[nuevo_animal] = cantidad  # Si el animal no existe, lo agrega al inventario
        print(f"Se han agregado {cantidad} {nuevo_animal}(s) al inventario.")
    else:
        print("Contraseña incorrecta. Acceso denegado.")

# Inicia un ciclo infinito para mostrar el menú y procesar las opciones del usuario
while True:
    mostrar_menu()
    Respuesta = int(input())

    if Respuesta == 1:
        mostrar_inventario()  # Muestra el inventario si el usuario selecciona la opción 1

    elif Respuesta == 2:
        comprar_animal()  # Permite al usuario comprar un animal si selecciona la opción 2

    elif Respuesta == 3:
        mostrar_compras()  # Muestra las compras realizadas si selecciona la opción 3

    elif Respuesta == 4:
        print("Gracias por tu visita")  # Agradece al usuario y termina el programa si selecciona la opción 4
        break

    elif Respuesta == 5:
        agregar_inventario()  # Permite agregar nuevo inventario si selecciona la opción 5