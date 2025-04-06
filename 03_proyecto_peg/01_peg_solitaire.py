# Crear modo aleatorio y log

# 1 agrega pregunta de juego random antes de while del juego 
# 2 pasa juego random a obtener_seleccion y modifica esta para elegir aleatoriamente
# 3 agrega decorador de logs para guardar en un archivo de texto el resultado
#   y se aplica a finalizar_juego devolviendo info de juego

import os
from itertools import product
from pprint import pp
from typing import Callable
from random import randint

FILAS: list  = ["A", "B", "C", "D", "E", "F", "G"]
COLUMNAS: list = ["1", "2", "3", "4", "5", "6", "7"]
DIRECCIONES: dict = {
    "derecha": (0, 2, 0, 1),
    "izquierda": (0, -2, 0, -1),
    "abajo": (2, 0, 1, 0),
    "arriba": (-2, 0, -1, 0)
}

def log_juego(func: Callable) -> Callable:
    """Decorador para registrar logs del juego"""
    def wrapper(self, *args, **kwargs):
        resultado:str = func(self, *args, **kwargs)
        with open("solitario_log.txt", "a") as log:
            log.write(f"{resultado}\n")
        return resultado
    return wrapper

class Solitario:
    """Clase que representa el tablero y las acciones del juego"""
    
    def __init__(self) -> None:
        """Inicializar el tablero con la configuracion inicial"""
        self.tablero: list = self._crear_tablero()
        self.contador: Callable = self._crear_contador()
    
    def _crear_tablero(self) ->  list:
        """Define la estructura inicial del tablero"""

        def es_esquina(row: int, column: int) -> bool:
            """Verifica si la posicion es una esquina no jugable"""
            return (row < 2 and column < 2) or (row < 2 and column > 4) or (row > 4 and column < 2) or (row > 4 and column > 4)
        
        return [
            [
                " " if es_esquina(row, column)
                else "1" if (row, column) != (3,3)
                else "0"
                for column in range(7)
            ]
            for row in range(7)
        ]
    
    def mostrar_tablero(self) -> None:
        """Muestra el tablero en la consola"""

        print(f"  {' '.join(COLUMNAS)}")
        for i, fila in enumerate(self.tablero):
            print(f"{FILAS[i]} {' '.join(fila)}")

    def get_movimientos_validos(self) -> list:
        """Encuentra las fichas que pueden moverse y en que direccion"""
        filas = len(self.tablero) 
        columnas = len(self.tablero[0])
        def es_movimiento_valido(row: int, column: int, direccion: str) -> bool:
            """Verifica si una ficha se puede mover en una direccion dada"""
            mov_row, mov_col, elim_row, elim_col = DIRECCIONES[direccion]
            # Nueva posicion del salto
            nuevo_row: int = row + mov_row
            nueva_col: int = column + mov_col
            # Posicion intermedia a eliminar
            elim_row_f: int = row + elim_row
            elim_col_f: int = column + elim_col

            return(
                0 <= nuevo_row < filas and 0 <= nueva_col < columnas and
                self.tablero[row][column] == "1" and
                self.tablero[elim_row_f][elim_col_f] == "1" and
                self.tablero[nuevo_row][nueva_col] == "0"
            )
        
        todas_posiciones = product(range(filas), range(columnas), DIRECCIONES.keys())
        # pp(list(todas_posiciones))
        return list(filter(lambda x: es_movimiento_valido(x[0], x[1], x[2]), todas_posiciones))

    def mostrar_movimientos(self, movimientos: list) -> None:
        """Muestra los movimientos en formato legible para el usuario"""
        movimientos_convertios: list = list(map(lambda m: (FILAS[m[0]], COLUMNAS[m[1]], m[2]), movimientos))
        for i, movimiento in enumerate(movimientos_convertios):
            print(f"{i+1} {movimiento}")

    def aplicar_movimiento(self, movimiento: tuple) -> list | None:
        """Aplica un movimiento en el tablero y devuelve una nueva version de este"""
        if movimiento not in self.get_movimientos_validos():
            print(f"Movimiento invalido: {movimiento}")
            return None
        row: int
        column: int
        direccion: str
        row, column, direccion = movimiento

        mov_row, mov_col, elim_row, elim_col = DIRECCIONES[direccion]
        # Nueva posicion despues del salto
        nuevo_row: int = row + mov_row
        nueva_col: int = column + mov_col
        # Ficha intermedia a eliminar
        eliminar_row: int = row + elim_row
        eliminar_col: int = column + elim_col
        # Crear copia inmutable del tablero
        nuevo_tablero = [fila[:] for fila in self.tablero]
        nuevo_tablero[row][column] = "0"
        nuevo_tablero[eliminar_row][eliminar_col] = "0"
        nuevo_tablero[nuevo_row][nueva_col] = "1"

        return nuevo_tablero
    
    def obtener_seleccion(self, movimientos: list, random: bool) -> tuple:
        """Obtiene la seleccion del usuario en formato de fila y columna"""
        cantidad: int = len(movimientos)
        while True:
            seleccion: str = str(randint(1, cantidad)) if random else input(f"Seleccione un movimiento (1 - {cantidad}): ").strip()
            if seleccion.isdigit() and 1<= int(seleccion) <= cantidad:
                return movimientos[int(seleccion) - 1]
            print("Seleccion invalida, intente de nuevo")
    
    def contar_peg(self) -> int:
        """Cuenta la cantidad de fichas restantes en el tablero"""
        return sum(fila.count("1") for fila in self.tablero)
    
    def verificar_victoria(self) -> bool:
        """Verifica si ha ganado el juego"""
        fichas_restantes: int = self.contar_peg()
        if fichas_restantes == 1 and self.tablero[3][3] == "1":
            return True
        return False
    
    def _crear_contador(self) -> Callable:
        """Closure - contador"""
        movimientos: int = 0
        def incrementar() -> int:
            nonlocal movimientos
            movimientos += 1
            return movimientos
        return incrementar
    
    @log_juego
    def finalizar_juego(self, victoria: bool) -> str:
        """Finaliza el juego y retorna el resultado"""
        num_movimientos: int = self.contador() - 1
        restantes: int = self.contar_peg()
        mensaje: str = f"{'Victoria'if victoria else 'Derrota'}  | Movimientos: {num_movimientos} | Fichas Restantes: {restantes}"
        print(mensaje)
        return mensaje


def main():
    os.system("cls" if os.name == "nt" else "clear")
    solitario: Solitario = Solitario()
    solitario.mostrar_tablero()
    jugando: bool = True
    while True:
        respuesta: str =  input("Quieres jugar en modo random? (s/n): ").strip().lower()
        if respuesta in ("s", "n"):
            juego_random: bool = respuesta == "s"
            break
        else:
            print("Entrada invalida, ingresa 's' para si o 'n' para no")

    while jugando:
        movimientos: list = solitario.get_movimientos_validos()
        if not movimientos:
            victoria: bool = solitario.verificar_victoria()
            print("Fin del juego no hay mas movimientos!")
            jugando = False
        else:
            print("Movimientos validos:")
            solitario.mostrar_movimientos(movimientos)
            movimiento: tuple = solitario.obtener_seleccion(movimientos, juego_random)
            solitario.contador()
            nuevo_tablero: list|None = solitario.aplicar_movimiento(movimiento)
            if nuevo_tablero:
                os.system("cls" if os.name == "nt" else "clear")
                solitario.tablero = nuevo_tablero
                solitario.mostrar_tablero()
    solitario.finalizar_juego(victoria)

if __name__ == "__main__":
    main()
