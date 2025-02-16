import re

# . cualquier caracter menos saltos de linea
patron: str = r"h.la"

# print(bool(re.search(patron, "hola")))
# print(bool(re.search(patron, "h2la")))
# print(bool(re.search(patron, "hXla")))
# print(bool(re.search(patron, "hla")))
# print(bool(re.search(patron, "hoola")))

# \d digitos (0-9)
# \D calquier NO digito
# patron = r"\d{2}"
# print(bool(re.search(patron, "123")))
# print(bool(re.search(patron, "12a")))
# print(bool(re.search(patron, "1a2")))

# \w caracter alfanumerico o _
# \W caracter no alfanumerico
# patron = r"\w+"
# print(bool(re.search(patron, "Python3")))
# print(bool(re.search(patron, "Python_")))
# print(bool(re.search(patron, "muchas palabras")))
# print(bool(re.search(patron, "!@#$")))

# \s Espacios en blanco
# # \S NO espacios en blanco
# patron = r"\s"
# print(bool(re.search(patron, "Hola Mundo")))
# print(bool(re.search(patron, "Hola")))

# ^ Busca el inicio de la linea
# $ Busca el final de la linea
# patron = r"^Hola.*Mundo$"
# print(bool(re.search(patron, "Hola a todos, Mundo")))
# print(bool(re.search(patron, "Hola Mundo")))
# print(bool(re.search(patron, "Mundo Hola")))

# * 0 o mas veces
# + 1 o mas veces
# ? 0 o 1 vez
# {n} Exactamente n veces
# {n,} Al menos n veces
# {n,m} Entre n y m veces
# patron = r"ha+"
# ha, haa, haaaaaa

# patron = r"(python|java)"
# print(bool(re.search(patron, "python")))
# print(bool(re.search(patron, "java")))
# print(bool(re.search(patron, "c++")))

patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# ^ Inicio de la cadena

# [a-zA-Z0-9_.+-] permite letras a-z en mayus y minus numeros _.+-
# + significa al menos un caracter de los permitidos

# @ que haya una @

# [a-zA-Z0-9-] permite letras a-z en mayus y minus numeros y -
# + significa al menos un caracter de los permitidos

# \. \ escapa el punto para que sea punto literal

# [a-zA-Z0-9-.] permite letras a-z en mayus y minus numeros .-
# + significa al menos un caracter de los permitidos

# $ coincida con fin de la cadena
# print(bool(re.search(patron, "usuario@dominio.com")))
# print(bool(re.search(patron, "usuario@dominio")))
# print(bool(re.search(patron, "usuariodominio.com")))
# print(bool(re.search(patron, "usuario@dominio.co.uk")))