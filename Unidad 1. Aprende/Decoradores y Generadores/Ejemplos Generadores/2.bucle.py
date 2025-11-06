def cuadrados(n):
    for i in range(n):
        yield i ** 2

for valor in cuadrados(9):
    print(valor)