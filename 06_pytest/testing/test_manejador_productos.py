import pytest
from modulo_pytest.manejador_productos import ManejadorProductos

@pytest.fixture
def manejador_productos():
    """Crear una nueva instancia del manejador"""
    return ManejadorProductos()

def test_agregar_producto(manejador_productos):
    assert manejador_productos.agregar_producto("galletas", 22.2) == True
    assert manejador_productos.obtener_producto("galletas") == 22.2

def test_agregar_duplicado(manejador_productos):
    manejador_productos.agregar_producto("galletas", 30.5)
    with pytest.raises(ValueError):
        manejador_productos.agregar_producto("galletas", 11.3)