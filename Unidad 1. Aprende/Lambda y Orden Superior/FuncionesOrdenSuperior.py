# Función de orden superior
def aplicarFuncion(funcion, valor):
    return funcion(valor)

# Funciones dentro de la función superior
def cuadrado(x):
    return x*x

print(aplicarFuncion(cuadrado, 5))


#funcion de orden superior que permite cualquier numero de argumentos
def FuncionEscalable(funcione, *args):
    return funcione(*args)

def suma(x, y):
    return x+y

def multi(x, y):
    return x*y

print(FuncionEscalable(suma, 5, 10))
print(FuncionEscalable(multi, 5, 10))