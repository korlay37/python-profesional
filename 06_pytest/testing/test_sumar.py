from modulo_pytest.sumar import sumar

def test_sumar() -> None:
    resultado: int = sumar(2, 5)
    assert resultado == 7