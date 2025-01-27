import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# logging.debug("Esto es mensaje de depuracion")
# logging.info("Esto es mensaje de informacion")
# logging.warning("Esto es mensaje de warning")
# logging.error("Esto es mensaje de error")
# logging.critical("Esto es mensaje de critical")

def division(a: float, b: float)-> None:
    try:
        resultado: float = a / b
        logging.info(f"Division realizada con exito resultado: {resultado}")
        print(f"{resultado =}")
    except ZeroDivisionError:
        logging.error("Error: Division entre cero")
        print("Log de error guardado")

division(5, 2.2)
division(10, 0)