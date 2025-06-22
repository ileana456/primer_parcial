import tkinter as tk
from tkinter import messagebox

def mostrar_direccion():
    """Muestra un mensaje de alerta con la dirección."""
    messagebox.showinfo("Mensaje", "¡JICARO, NUEVA SEGOVIA!")

def mostrar_edad():
    """Muestra un mensaje de alerta con la edad."""
    messagebox.showinfo("Mensaje", "¡21 AÑOS!")

root = tk.Tk()
root.title("Examen I Parcial - ILEANA ALFARO")

# Etiqueta de título con el nombre del usuario
etiqueta_usuario = tk.Label(root, text="MI NOMBRE ES ILEANA ALFARO", font=("Arial", 18, "bold"))
etiqueta_usuario.pack(pady=100)

# Botón para mostrar dirección
boton_direccion = tk.Button(root, text="VIVO EN:", command=mostrar_direccion, width=15, font=("Arial", 14))
boton_direccion.pack(side="left", padx=70)

# Botón para mostrar edad
boton_edad = tk.Button(root, text="EDAD", command=mostrar_edad, width=15, font=("Arial", 14))
boton_edad.pack(side="right", padx=70)

# Configurar tamaño de la ventana
root.geometry("800x600")

# Establecer un color de fondo
root.configure(bg="pink")

# Ejecutar el bucle principal de la aplicación
root.mainloop()