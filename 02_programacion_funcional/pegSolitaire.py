
from pprint import pp
def crear_tablero() -> list:
    return [
        [
            " " if (r < 2 and c < 2) or (r < 2 and c > 4) or (r > 4 and c < 2) or (r > 4 and c > 4)
            else "1" if (r, c) != (3, 3)  # Centro vacío
            else "0"
            for c in range(7)
        ]
        for r in range(7)
    ]
class PegSolitaire:
    def __init__(self) -> None:
        self.tablero = crear_tablero()
        pp(self.tablero)

    # def mover(self, origen: tuple[int, int], destino: tuple[int, int]) -> None:
    #     self.tablero = mover(self.tablero, origen, destino)
    def mostrar(self) -> None:
        for fila in self.tablero:
            print(" ".join(str(c) for c in fila))

def encontrar_movimientos(tablero: list) -> list:
    movimientos = []
    filas, columnas = len(tablero), len(tablero[0])
    direcciones = {
        "derecha": (0, 2, 0, 1),
        "izquierda": (0, -2, 0, -1),
        "abajo": (2, 0, 1, 0),
        "arriba": (-2, 0, -1, 0)
    }

    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == "1":  # Hay una ficha en esta posición
                for direccion, (df, dc, mf, mc) in direcciones.items():
                    nf, nc = fila + df, columna + dc
                    mf, mc = fila + mf, columna + mc
                    if 0 <= nf < filas and 0 <= nc < columnas and tablero[mf][mc] == "1" and tablero[nf][nc] == "0":
                        movimientos.append(((fila, columna), direccion))

    return movimientos

juego = PegSolitaire()
pp(encontrar_movimientos(juego.tablero))
# juego.mostrar()
# juego.mover((3, 1), (3, 3))
