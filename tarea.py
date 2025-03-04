# Solicitar al usuario un número entre 1 y 100
numero = int(input("Por favor, ingrese un número entre 1 y 100: "))

# Verificar las condiciones y mostrar los mensajes correspondientes
if numero < 1:
    print("Favor de ingresar un número mayor a 0")
elif numero > 100:
    print("Favor de ingresar un número menor o igual a 100")
else:
    print(f"¡Muy bien! El {numero} es una gran opción.")