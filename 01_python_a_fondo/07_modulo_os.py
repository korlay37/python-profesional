import os

# Obtener el sistema operativo
# print(os.name)

# Ruta actual
# print(os.getcwd())

# Cambiar directorio actual
# os.chdir("ruta/a/directorio")

# Crear directorio
# os.mkdir("nuevo")

# Borrar un directorio
# os.rmdir("nuevo")

# Listar contenido
# print(os.listdir("."))

# Comprobar existencia
# archivo: str = "archivo.txt"
# if os.path.exists(archivo):
#     print("Si existe")
# else:
#     print("No existe")

# Checar si es archivo
# print(os.path.isfile("error.log"))

# Obtener tamanio/size
# print(os.path.getsize("error.log"))

# Checar variables de entorno
# usuario: str = os.getenv("USERNAME", "Desconocido")
# print(f"{ usuario = }")

# Unir Rutas
# directorio: str = "/home/user"
# archivo: str = "archivo.txt"
# ruta: str = os.path.join(directorio, archivo)
# print(ruta)

# Dividir la ruta en directorio y archivo
# ruta_c: str = "C:\\Users\\ercor\\Desktop\\python-profesional\\01_python_a_fondo\\07_modulo_os.py"
# ruta, archivo = os.path.split(ruta_c)
# print(f"{ruta = }")
# print(f"{archivo = }")