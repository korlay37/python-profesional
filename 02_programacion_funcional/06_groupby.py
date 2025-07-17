from itertools import groupby
from collections import Counter

datos: list = ["a", "a", "b", "b", "c", "a", "a"]
datos_ordenados: list = ["a", "a", "a", "a", "b", "b", "c"]
# agrupados: dict = {clave: list(grupo) for clave, grupo in groupby(datos_ordenados)}

# for clave, grupo in groupby(sorted(datos)):
#     print(clave)
#     print(list(grupo))

counter = Counter(datos)
# print(counter)
# print(counter.most_common(2))
# print(counter["c"])

for element, count in counter.items():
    print(element, count)