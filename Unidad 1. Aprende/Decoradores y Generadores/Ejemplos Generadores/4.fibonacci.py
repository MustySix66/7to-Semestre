def numeros_fibonacci():
    antes = 0
    actual = 1
    while True:
        yield actual
        aux=antes+actual
        antes=actual
        actual=aux

for numero in numeros_fibonacci():
    if numero > 100:
        break
    print(numero)