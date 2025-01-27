import logging

# Consola
console_handler: logging.StreamHandler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

# Archivo
file_handler: logging.FileHandler = logging.FileHandler("error.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter("%(name)s - %(asctime)s - %(levelname)s - %(message)s"))

# Logger principal
logger: logging.Logger = logging.getLogger(__name__)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def procesar_datos(dato: int)-> None:
    if dato < 0:
        logger.warning(f"Dato negativo: {dato}")
    elif dato == 0:
        logger.error("Fato igual a cero, invalido!")
    else:
        logger.info(f"Dato procesado: {dato}")

procesar_datos(10)
procesar_datos(-5)
procesar_datos(0)