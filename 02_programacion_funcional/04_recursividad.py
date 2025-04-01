


# Caso base: condicion para detener recursion
# Caso recursivo: llamada a la misma funcion...

# def factorial(n: int) -> int:
#     if n == 0:
#         return 1  # caso base
#     return n * factorial(n - 1) # caso recursivo

# print(factorial(3))

# Fibonacci: 0,1,1,2,3,5,8,13,21
# def fibonacci(n: int, a: int = 0, b: int = 1) -> None:
#     if n <=0:
#         return # caso base
#     print(a, end=" ")
#     fibonacci(n - 1, b, a + b )
# fibonacci(100)

# def suma_lista(numeros: list) -> int:
#     if not numeros:
#         return 0
#     return numeros[0] + suma_lista(numeros[1:])
# print(suma_lista([1,2,3,4]))

# from functools import reduce

# numeros: list[int] = [1,2,3,4]
# suma_total: int = reduce(lambda x,y: x+y, numeros)
# print(suma_total)

from typing import Any

def buscar_valor(diccionario: dict, clave: str) -> Any:
    if clave in diccionario:
        return diccionario[clave]
    for valor in diccionario.values():
        if isinstance(valor, dict):
            resultado = buscar_valor(valor, clave)
            if resultado is not None:
                return resultado
    return None


datos = {"usuario": {"nombre": "Eduardo","datos": {"edad": 33}}}
print(buscar_valor(datos, "edad2"))