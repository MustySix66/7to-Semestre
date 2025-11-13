def numeros_infinitos():
    n = 1
    while True:
        yield n
        n += 1

for numero in numeros_infinitos():
    if numero > 5:
        break
    print(numero)