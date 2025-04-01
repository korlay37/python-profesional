from typing import Iterator
from itertools import count, cycle, repeat, product, permutations, combinations, filterfalse, groupby

# contador: Iterator = count(start=10, step=2)
# for _ in range(5):
#     print(next(contador))

# colores: list = ["rojo", "verde", "azul"]
# ciclo_colores: Iterator = cycle(colores)

# for _ in range(10):
#     print(next(ciclo_colores))

# repetidos: Iterator =  repeat("Python", 3)
# print(list(repetidos))

# opciones = product([1,2], ["A","B"])
# print(list(opciones))

# valores: Iterator = permutations([1,2,3])
# print(list(valores))

# valores = combinations([1,2,3], 2)
# print(list(valores))

# numeros: list = [1,2,3,4,5,6]
# impares = filterfalse(lambda x: x % 2 == 0, numeros)
# print(list(impares))

# datos: list = ["a", "a", "b", "b", "c", "a", "a"]
# agrupados: dict = {clave: list(grupo) for clave, grupo in groupby(datos)}
# print(agrupados)