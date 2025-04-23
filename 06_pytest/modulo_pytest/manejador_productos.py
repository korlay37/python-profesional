class ManejadorProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre: str, precio: float):
        if nombre in self.productos:
            raise ValueError("Ya existre el producto")
        self.productos[nombre] = precio
        return True
    
    def obtener_producto(self, nombre: str):
        return self.productos.get(nombre)