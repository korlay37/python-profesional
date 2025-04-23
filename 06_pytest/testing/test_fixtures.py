import pytest

@pytest.fixture
def lista_vacia() -> list:
    return []

def test_agregar_a_lista(lista_vacia: list) -> None:
    lista_vacia.append(22)
    assert lista_vacia == [22]

# scope= 
# "function" (default) = Se va a crear para cada prueba
# "module" = Una vez por archivo
# "session" = Una vez para todas las pruebas
# "class" = Una vez por clase de pruebas

@pytest.fixture(scope="module")
def db_falsa() -> dict:
    print("Creando base de datos simulada")
    return {"usuario": "admin", "clave": "1234"}

def test_usuario_es_admin(db_falsa: dict) -> None:
    assert db_falsa["usuario"] == "admin"