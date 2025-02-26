from typing import Callable

# def generar_multiplicador(factor: int) -> Callable:
#     def multiplicador(numero: int) -> int:
#         return numero * factor
#     return multiplicador

# multiplicar_por_3: Callable = generar_multiplicador(3)
# print(multiplicar_por_3(5))
# print(multiplicar_por_3(6))

# def contador()-> Callable:
#     cuenta: int = 0
#     def incrementar() -> int:
#         nonlocal cuenta
#         cuenta += 1
#         return cuenta
#     return incrementar

# mi_contador: Callable = contador()
# print(mi_contador())
# print(mi_contador())
# print(mi_contador())

# def crear_filtro(minimo: int) -> Callable:
#     def filtrar(numeros: list) -> list:
#         return [n for n in numeros if n >= minimo]
#     return filtrar

# filtro_mayores_2: Callable = crear_filtro(2)
# print(filtro_mayores_2([1, 3, 2, 6, 0, -2]))