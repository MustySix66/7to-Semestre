def repetir(n):
    def decorador (funcion):
        def wrapper():
            for _ in range(n):
                funcion()
        return wrapper
    return decorador

@repetir(3)
def hola():
    print("Hola mundo!")

hola()