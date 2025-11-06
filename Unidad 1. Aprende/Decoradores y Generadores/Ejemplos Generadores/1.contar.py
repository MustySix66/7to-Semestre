def contar():
    yield 1
    yield 2
    yield 3

for numero in contar():
    print(numero)