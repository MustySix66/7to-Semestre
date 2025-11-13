import tkinter as tk
import sympy as sp

def calcular_integral():
    # 1. Obtenemos el texto y limpiamos espacios en blanco
    funcion_str = entrada_funcion.get()
    limite_inf_str = entrada_desde.get().strip() # .strip() elimina espacios
    limite_sup_str = entrada_hasta.get().strip() # .strip() elimina espacios

    try:
        x = sp.symbols('x')
        expresion = sp.sympify(funcion_str)

        if not limite_inf_str and not limite_sup_str:
            # Caso 1: Integral Indefinida
            resultado = sp.integrate(expresion, x)
            # Descomponemos el resultado en numerador y denominador
            num, den = resultado.as_numer_denom()
            # Si el denominador es 1 (ej. -cos(x)), no mostramos "/1"
            if den == 1:
                resultado_str = f"{num}"
            # Si el denominador no es 1 (ej. x**3/3)
            else:
                resultado_str = f"({num})/{den}"

            resultado_final = f"{resultado_str} + C"
        else:
            # Caso 2: Integral Definida
            resultado = sp.integrate(expresion, (x, float(limite_inf_str), float(limite_sup_str)))
            resultado_final = str(resultado) 
        
        etiqueta_resultado.config(text=f"Resultado: {resultado_final}")

    except Exception as e:
        etiqueta_resultado.config(text=f"Error: {e}")

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Integrales")
ventana.geometry("400x300") # Tamaño inicial

# --- Sección de la Función ---
etiqueta_funcion = tk.Label(ventana, text="Función f(x):")
etiqueta_funcion.pack() # Coloca la etiqueta

# Campo de entrada para la función
entrada_funcion = tk.Entry(ventana, width=30)
entrada_funcion.pack() # Coloca el campo de entrada

# --- Sección Límite Inferior (Desde) ---
etiqueta_desde = tk.Label(ventana, text="Desde (límite inferior):")
etiqueta_desde.pack()

entrada_desde = tk.Entry(ventana, width=10)
entrada_desde.pack()

# --- Sección Límite Superior (Hasta) ---
etiqueta_hasta = tk.Label(ventana, text="Hasta (límite superior):")
etiqueta_hasta.pack()

entrada_hasta = tk.Entry(ventana, width=10)
entrada_hasta.pack()

# --- Botón de Cálculo ---
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_integral)
boton_calcular.pack()

# --- Etiqueta para el Resultado ---
etiqueta_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 12))
etiqueta_resultado.pack()


# 4. Iniciar el bucle de la aplicación
ventana.mainloop()