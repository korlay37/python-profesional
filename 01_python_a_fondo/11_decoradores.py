# from typing import Callable
# import time

# def mi_decorador(func: Callable) -> Callable:
#     def wrapper() -> None:
#         print("Antes de la funcion")
#         func()
#         print("Despues de la funcion")
#     return wrapper

# def saludar() -> None:
#     print("Hola mundo!")

# @mi_decorador
# def sumar() -> None:
#     print(f"{2 + 2}")

# sumar()

# def medir_tiempo(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs) -> None:
#         inicio: float = time.time()
#         func(*args, **kwargs)
#         fin: float = time.time()
#         print(f"Tiempo de ejecucion: {fin - inicio:.4f} segundos")
#     return wrapper

# @medir_tiempo
# def tarea() -> None:
#     time.sleep(2)
#     print("Tarea completada!")

# tarea()

# def repetir(n: int) -> Callable[[Callable], Callable]:
#     def decorador(func: Callable) -> Callable:
#         def wrapper() -> None:
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorador

# @repetir(3)
# def mensaje() -> None:
#     print("Ejecutando funcion")

# mensaje()

from functools import wraps

def mi_decorador(func):
    @wraps(func)
    def wrapper():
        """Doc de wrapper"""
        print("Ejecutando funcion decorada")
        func()
    return wrapper

@mi_decorador
def mi_funcion():
    """Doc de funcion"""
    print("Hola mundo!")

print(mi_funcion.__name__)
print(mi_funcion.__doc__)