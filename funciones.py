def saludar(nombre):
    print("¡Hola!,", nombre)


#Celsius a Fahrenheit: C = (F-32)*5/9
def convertir_a_fahrenheit(c):
    return (c * 9/5) +  32      #F = (C * 9/5) + 32


#saludar("Rodrigo")
#saludar("Juan")
#saludar("Samuel")
while True:
    print(convertir_a_fahrenheit(float(input("Ingrese la temperatura en grados Celsius: "))))
    break
"""
celsius = input("Ingrese la temperatura en grados Celsius: ")
celsius = float(celsius)
farenheit = convertir_a_fahrenheit(celsius)
print(farenheit)
"""
