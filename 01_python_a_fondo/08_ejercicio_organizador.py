"""
Organizador de archivos
Crearemos una funcion que reciba el directorio(str)
Itera en los diferentes archivos
Crea un directorio por cada tipo de archivo diferente encontrado
Mueve los archivos de dichas extensiones a sus directorios correspondientes
Utiliza logging para crear un archivo logs.log donde vaya guardando los logs del proceso

Tips:
Usa os.chdir para establecer el directorio donde se ejecutara la organizacion
Usa os.listdir para listar los archivos y carpetas dentro del directorio
Usa el metodo .split de una string para obtener las extensiones
Usa os.path.exists para verificar si ya existe el directorio de extension
Usa os.mkdir para crear directorios
Usa os.rename para mover archivos a sus directorios

"""
import os
import logging

# Configurar logging
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def organizar_archivos(directorio: str) -> None:
    try:
        # Cambio de directorio
        os.chdir(directorio)
        logging.info(f"Directorio cambiado a: {directorio}")

        archivos: list[str] = os.listdir()
        logging.info(f"Archivos en el directorio: {archivos}")

        for archivo in archivos:
            if os.path.isfile(archivo):
                extension: str = archivo.split(".")[-1]

                if not os.path.exists(extension):
                    os.mkdir(extension)
                    logging.info(f"Directorio creado: {extension}")
                
                destino: str = os.path.join(extension, archivo)
                os.rename(archivo, destino)
                logging.info(f"Archivo {archivo} movido a directorio {extension}")
        
        logging.info("Archivos organizados correctamente")

    except Exception as e:
        logging.error("Ocurrio un error!")


directorio: str = "C://Users//ercor//Desktop//python-profesional//01_python_a_fondo//prueba"
organizar_archivos(directorio)