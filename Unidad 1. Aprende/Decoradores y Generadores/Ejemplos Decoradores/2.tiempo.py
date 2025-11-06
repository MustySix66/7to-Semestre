import time 

def medir_tiempo(funcion):
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"tiempo: {fin - inicio:.4f} segundos")
    return wrapper
    
@medir_tiempo
def contar():
    suma = 0
    for i in range(1000000):
        suma += i
    print("Suma lista")

contar()