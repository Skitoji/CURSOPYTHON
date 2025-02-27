print("Bienvenido al conversor de millas a Kilometros")

print("Cuantas millas quieres convertir?")
millas = input() #string

print("Tipo de dato:", type(millas))
# Convertir a float
millas = float(millas)
print("Tipo de dato:", type(millas))

# 1 milla = 1.60934 km
km = float(millas) * 1.60934

print("Millas ingresadas:", millas)
print("Kilometros:", km)
print("Gracias por usar el conversor de millas a kilometros")