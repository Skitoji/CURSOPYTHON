import tkinter as tk
from tkinter import messagebox

def mostrar_inventario():
    inventario = f"Actualmente contamos con:\n{manzanas_rojas} manzanas rojas,\n{manzanas_verdes} manzanas verdes,\n{manzanas_amarillas} manzanas amarillas\npor un precio de: {precio_por_manzana} pesos cada una."
    messagebox.showinfo("Inventario", inventario)

def comprar_manzanas():
    global manzanas_rojas, manzanas_verdes, manzanas_amarillas
    cantidad = int(entry_cantidad.get())
    tipo = tipo_var.get()
    precio_total = 0

    if tipo == 1:
        if cantidad <= manzanas_rojas:
            manzanas_rojas -= cantidad
            precio_total = cantidad * precio_por_manzana
            messagebox.showinfo("Compra", f"Has comprado {cantidad} manzanas rojas.")
        else:
            messagebox.showerror("Error", "Lo siento, no tenemos suficientes manzanas rojas.")
    elif tipo == 2:
        if cantidad <= manzanas_verdes:
            manzanas_verdes -= cantidad
            precio_total = cantidad * precio_por_manzana
            messagebox.showinfo("Compra", f"Has comprado {cantidad} manzanas verdes.")
        else:
            messagebox.showerror("Error", "Lo siento, no tenemos suficientes manzanas verdes.")
    elif tipo == 3:
        if cantidad <= manzanas_amarillas:
            manzanas_amarillas -= cantidad
            precio_total = cantidad * precio_por_manzana
            messagebox.showinfo("Compra", f"Has comprado {cantidad} manzanas amarillas.")
        else:
            messagebox.showerror("Error", "Lo siento, no tenemos suficientes manzanas amarillas.")
    else:
        messagebox.showerror("Error", "Tipo de manzana no válido.")

    actualizar_inventario()
    label_precio_total.config(text=f"El precio total de su compra es: {precio_total} pesos")

def actualizar_inventario():
    label_inventario.config(text=f"Inventario actualizado:\n{manzanas_rojas} manzanas rojas,\n{manzanas_verdes} manzanas verdes,\n{manzanas_amarillas} manzanas amarillas")

# Definir las variables de inventario y precio
manzanas_rojas = 10
manzanas_verdes = 5
manzanas_amarillas = 3
precio_por_manzana = 5

# Crear la ventana principal
root = tk.Tk()
root.title("Tienda de Manzanas")

# Crear widgets
label_bienvenida = tk.Label(root, text="------ HOLA, BIENVENIDO A LA TIENDA ------\n--------------- DE MANZANAS --------------")
label_bienvenida.pack()

label_nombre = tk.Label(root, text="Ingrese su nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Ingrese su apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

button_inventario = tk.Button(root, text="Mostrar Inventario", command=mostrar_inventario)
button_inventario.pack()

label_cantidad = tk.Label(root, text="Cuantas manzanas desea comprar?")
label_cantidad.pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

label_tipo = tk.Label(root, text="Que tipo de manzana desea comprar?")
label_tipo.pack()

tipo_var = tk.IntVar()
radio_roja = tk.Radiobutton(root, text="Roja", variable=tipo_var, value=1)
radio_roja.pack()
radio_verde = tk.Radiobutton(root, text="Verde", variable=tipo_var, value=2)
radio_verde.pack()
radio_amarilla = tk.Radiobutton(root, text="Amarilla", variable=tipo_var, value=3)
radio_amarilla.pack()

button_comprar = tk.Button(root, text="Comprar", command=comprar_manzanas)
button_comprar.pack()

label_precio_total = tk.Label(root, text="El precio total de su compra es: 0 pesos")
label_precio_total.pack()

label_inventario = tk.Label(root, text="")
label_inventario.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()