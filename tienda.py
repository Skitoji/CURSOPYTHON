print("*************************")
print("**  Bienvenido a la tienda  **")
print("**     de Mascotas     **")
print("*************************")

num_perros = 10
num_gatos = 5
num_pajaros = 3

animales_totales = num_perros + num_gatos + num_pajaros

print("Cual es tu nombre?")
nombre = input ()
print("Por favor ingresa tu apellido")
apellido = input()

# concatenar
nombre_completo = nombre + " " + apellido # "Juan" + " " + "Perez" = "Juan Perez" #El espacio se agrega con " "

print("Gracias por visitarnos", nombre_completo)

while True: #ciclo infinito
    print("")
    print("*************************")
    print("Selecciona la opcion que deseas:")
    print("1. Conocer cuantos animales hay")
    print("2. Comprar un animal")
    print("3. Salir")

    Respuesta = int(input())

    if Respuesta == 1:
        print("Actualmente contamos con:")
        print("Perros:", num_perros, "Gatos:", num_gatos, "Pajaros:", num_pajaros)
        print("En total tenemos", animales_totales, "mascotas") 
    elif Respuesta == 2:
        print("Que tipo de animal deseas comprar?")
        animal = input()
        print("Has comprado un", animal)
    elif Respuesta == 3:
        print("Gracias por tu visita")
        break