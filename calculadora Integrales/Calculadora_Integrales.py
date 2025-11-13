# Importamos la libreria SymPy
import sympy as sp

# Definimos el simbolo
x = sp.symbols('x')

# Definimos la expresión a integrar
expresion = x**2

# Hacemos la integración con respecto a "x"
integral = sp.integrate(expresion, (x, 0, 2))

# Imprimimos el resultado
print(f"La función a integrar es: {expresion}")
print(f"El resultado de la integral es: {integral}")