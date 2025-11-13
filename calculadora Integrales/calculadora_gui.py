import tkinter as tk

# Crear una venta base o root
ventana = tk.Tk()
ventana.title("Calculadora de Integrales")
ventana.geometry("400x300") #Definimos el tamaño de la ventana

etiqueta_Funcion = tk.Label(ventana, text="Función f(x):")
etiqueta_Funcion.pack()

ventana.mainloop()
