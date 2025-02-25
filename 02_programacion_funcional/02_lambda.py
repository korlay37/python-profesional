
from typing import Callable
from functools import reduce
#  lambda argumentos: expresion

# suma: Callable = lambda x, y: x + y
# print(suma(3, 5))

# Sorted()
# numeros: list = [ 1, 2, 3, 4, 5]
# num_ordenados: list = sorted(numeros, key=lambda x: -x)
# print(num_ordenados)

# map()
# cuadrados: list =  list(map(lambda x: x ** 2, numeros))
# print(cuadrados)

# filter()
# pares: list = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)

# reduce()
# suma_total: int = reduce(lambda x, y: x + y, numeros)
# print(suma_total)

# frutas: list = ["manzana", "banana", "cereza", "kiwi"]
# ordenadas: list = sorted(frutas, key=lambda f: len(f))
# print(ordenadas)