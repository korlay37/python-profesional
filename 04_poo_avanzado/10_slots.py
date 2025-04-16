

class Punto:
    __slots__ = ("x", "y")
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

p: Punto = Punto(2, 3)
print(p.x, p.y)
# p.z = 5
# print(p.x, p.y, p.z)