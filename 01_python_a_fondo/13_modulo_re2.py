import re

# re.findall() todas las coincidencias en un texto -> List
# texto: str = "Correos: eduardo@gmail.com, user@examlpe.org"
# patron: str = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

# correos: list = re.findall(patron, texto)
# print(correos)

# re.sub() Cambiar todas las coincidencias
# texto: str = "Javascript es increible, me encanta Javascript"
# nuevo_texto: str = re.sub(r"Javascript", "Python", texto)

# print(nuevo_texto)

# re.split() dividir texto usando expresion regular
# texto: str = "manzana,banana;naranja|pera"
# frutas: list = re.split(r"[,;|]", texto)

# print(frutas)

# re.match() Coincidencia al inicio del texto
# texto: str = "Python es genial"
# patron: str = r"Python"

# resultado = re.match(patron, texto)
# if resultado:
#     print("Hubo una coincidencia!")