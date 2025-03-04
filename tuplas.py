#Tuplas muy similares a las listas
#No pueden modificarse
#Se definen con parentesis

lista = [1, 2, 3, 4, 5] #Constantemente agregando informacion
tupla = (1, 2, 3, 4, 5) #Definir datos con longitud fija

#ejemplo de tupla
"""
lista[0] = 10
tupla[0] = 10
print(lista)
print(tupla)
"""

videojuegos = []
#Nombre, Genero, Año de lanzamiento, Precio
#final_fantasy_7 = ("final_fantasy_7", "RPG", 1997, 60)
videojuegos.append( ("Final Fantasy 7", "RPG", 1997, 60) )
videojuegos.append( ("The Legend of Zelda: Ocarina of Time", "Aventura", 1998, 60) )
videojuegos.append( ("Super Mario 64", "Plataforma", 1996, 60) )
videojuegos.append( ("Metal Gear Solid", "Accion", 1998, 60) )
videojuegos.append( ("Resident Evil 2", "Survival Horror", 1998, 60) )
videojuegos.append( ("Half-Life", "FPS", 1998, 60) )
videojuegos.append( ("Gran Turismo", "Carreras", 1998, 60) )
print(videojuegos)