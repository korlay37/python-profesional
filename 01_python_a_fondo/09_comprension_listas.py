# numeros: list[int] = [1,2,3,4,5]
# cuadrados: list[int] = []

# for numero in numeros:
#     cuadrados.append(numero ** 2) 

# cuadrados: list[int] = [n**2 for n in numeros]
# print(cuadrados)

# ESTRUCTURA BASICA
# lista = [ expresion for elemento in iterable]
# expresion (que hacer con cada elemento)
# elemento (cada item del iterable)
# iterable (Fuente de los datos, lista, rango etc.)

# FILTRAR ELEMENTOS
# numeros: list[int] = [1,2,3,4,5,6,7,8,9,10]
# pares: list[int] = [n for n in numeros if n % 2 == 0]
# print(pares)

# # TRANSFORMAR DATOS
# palabras: list[str] = ["python", "curso", "udemy"]
# mayusculas: list[str] = [palabra.upper() for palabra in palabras]
# print(mayusculas)

# # CONDICIONALES
# paridad: list[str] = ["par" if n % 2 == 0 else "impar" for n in numeros]
# print(paridad)

# # RANGOS
# potencias: list[int] =[2**n for n in range(10)]
# print(potencias)

# colores: list[str] = ["verde", "rojo", "naranja"]
# objetos: list[str] = ["carro", "camisa", "lapiz"]

# combinacion: list[str] = [f"{objeto} {color}" for color in colores for objeto in objetos]
# print(combinacion)

# matriz: list[list[int]] = [[ i * j for j in range(1,4)] for i in range(1,4)]
# print(matriz)