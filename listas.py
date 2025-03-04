nombres = ['Juan', 'Ana', 'Luis', 'Pedro', 'María', 'Santiago']
# 0, 1, 2, 3, 4, 5
#0, 1, 2, 3, 4
# print(nombres[0])
"""print(nombres[0])"""
print(nombres)
"""nombres.append('Carlos')
print(nombres)
#nombres.remove('Ana')
del nombres[1]
print(nombres)
"""
"""print("Ana" in nombres)
print("Santiago" not in nombres)
"""
#f-strings 

for i, nombre in enumerate(nombres):
    #print("Se inscribio", i, "en la lista:", i, nombre)
    print(f"Se inscribio {nombre} en la lista con el indice: {i}")

print("Bienvenidos a la fiesta...", nombres[:3]) #Al quitar un valor se toma el valor anterior
print("Lo sentimos vuelve mas tarde...", nombres[3:]) #Al quitar un valor se toma el valor siguiente