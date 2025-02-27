print("Escribe tu Nombre:") 
nombre = input()
print("Escribe tu edad:")
edad = int(input())

#elif = else if
#Operadores logicos
#and = y or = o
#and: Todas las condiciones deben ser verdaderas
#or: Al menos una condicion debe ser verdadera

if nombre == "Samuel" and edad >= 18 or nombre == "David" and edad >= 18:
    print("Bienvenido, eres mayor de edad")
elif nombre == "Samuel" and edad < 18 or nombre == "David" and edad < 18:
    print("Bienvenido, eres menor de edad")
else:
    print("Saludos", nombre)