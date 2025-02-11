from typing import Generator

# def generador_simple() -> Generator:
#     print("Iniciando")
#     yield 1
#     print("Retomando")
#     yield 2
#     print("Finalizando")

# for valor in generador_simple():
#     print(f"{valor = }")

# def generador_pares(limite: int) -> Generator:
#     for numero in range(0, limite, 2):
#         yield numero

# pares: Generator = generador_pares(10)
# for par in pares:
#     print(par)

# def lista_pares(limite: int) -> list[int]:
#     return [numero for numero in range(0, limite, 2)]

# print(lista_pares(10))

# # Lista
# lista_pares: list = [x for x in range(10) if x % 2 == 0]
# # Generador
# generador_pares: Generator = (x for x in range(10) if x % 2 == 0)

# suma_cuadrados: int = sum(x ** 2 for x in range(1_000_000))
# print(suma_cuadrados)

# Avanzado: Generador infinito
def generador_infinito() -> Generator:
    numero = 0
    while True: 
        yield numero
        numero += 1

contador: Generator = generador_infinito()
for _ in range(5):
    print(next(contador))
    