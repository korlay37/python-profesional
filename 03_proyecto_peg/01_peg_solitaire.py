# Si quieres intentarlo sin ver el video:
# 1 Crea una funcion mostrar_movimientos que reciba la lista de movimientos, 
#   creara una lista a base de los movimientos con map, para "traducir" las coordenadas 
#   a los nombres de fila y columnas que ve el usuario
# 2 Crea una función/método que reciba el tablero y un 
#   movimiento válido (posición inicial y dirección).
# 3 Verifica que solo se aplique si el movimiento es válido.
# 4 Usa la información de DIRECCIONES para calcular la nueva posición y 
#   la posición de la ficha eliminada.
# 5 Retorna una nueva versión del tablero, sin modificar el original.

from itertools import product
from pprint import pp

FILAS: list  = ["A", "B", "C", "D", "E", "F", "G"]
COLUMNAS: list = ["1", "2", "3", "4", "5", "6", "7"]
DIRECCIONES: dict = {
    "derecha": (0, 2, 0, 1),
    "izquierda": (0, -2, 0, -1),
    "abajo": (2, 0, 1, 0),
    "arriba": (-2, 0, -1, 0)
}

class Solitario:
    """Clase que representa el tablero y las acciones del juego"""
    
    def __init__(self) -> None:
        """Inicializar el tablero con la configuracion inicial"""
        self.tablero: list = self._crear_tablero()
    
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

solitario: Solitario = Solitario()
solitario.mostrar_tablero()
movimientos:list = solitario.get_movimientos_validos()
solitario.mostrar_movimientos(movimientos)
nuevo_tablero: list|None = solitario.aplicar_movimiento((3,1,"derecha"))
if nuevo_tablero:
    solitario.tablero = nuevo_tablero
    solitario.mostrar_tablero()