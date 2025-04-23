import pytest
from modulo_pytest.operaciones import multiplicar, dividir

def test_multiplicar_positivos() -> None:
    assert multiplicar(2, 3) == 6

def test_multiplicar_por_cero() -> None:
    assert multiplicar(5, 0) == 0

def test_multiplicar() -> None:
    assert multiplicar(4, 3) == 12
    assert multiplicar(2, 4) == 8
    assert multiplicar(7, 2) == 14

def test_dividir() -> None:
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(5, 0)