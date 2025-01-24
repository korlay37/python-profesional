# all / any
# valores: list[bool] = [True, True, False]
# print(all(valores))
# print(any(valores))

# edad: int = 33
# es_adulto: bool = edad >= 18
# tiene_licencia: bool = True
# puede_manejar: bool = all([es_adulto, tiene_licencia])
# casi_puede_manejar: bool = any([es_adulto, tiene_licencia])

# callable
# def funcion() -> None:
#     pass
# print(callable(funcion))
# print(callable(43))

# filter(funcion, iterable)
# def esPar(num) -> bool:
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# numeros: list[int] = [1, 2, 3, 4, 5, 6]
# pares: list[int] = list(filter(esPar, numeros))
# print(pares)
# for num in filter(esPar, numeros):
#     print(num)

# map(funcion, iterable)
# def alCuadrado(num) -> int:
#     return num ** 2
# numeros: list[int] = [1, 2, 3, 4, 5, 6]
# cuadrados: list[int] = list(map(alCuadrado, numeros))
# print(cuadrados)

# sorted(iterable, key=None, reverse=False)
# letras: list[str] = ["c", "a", "b", "c", "B"]
# print(sorted(letras, key=str.lower))

# zip
# nombres: list[str] = ["Ana", "Luis", "Juan"]
# edades: list[int] = [25, 30, 22]
# combinados: list = list(zip(nombres, edades))
# print(combinados)
