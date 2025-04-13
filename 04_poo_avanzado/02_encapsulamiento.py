

# class Producto:
#     def __init__(self, precio: float) -> None:
#         self.precio: float = precio

# producto: Producto = Producto(-50.0)
# print(producto.precio)
# producto.precio = 10
# print(producto.precio)

class Producto:
    def __init__(self, precio: float) -> None:
        self._precio: float = 0.0
        self.precio = precio
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @precio.deleter
    def precio(self) -> None:
        self._precio = 0.0

p: Producto = Producto(30.2)
print(p.precio)
del p.precio
print(p.precio)