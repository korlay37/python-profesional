import pytest
from modulo_pytest.sumar import sumar

# @pytest.mark.skip(reason="Funcionalidad no implementada")
@pytest.mark.xfail(reason="Bug conocido en progreso")
def test_sumar() -> None:
    resultado: int = sumar(2, 5)
    assert resultado == 10