def mi_decorador(funcion):
    def nueva_funcion():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return nueva_funcion

@mi_decorador
def saludar():
    print("Hola!")

saludar()