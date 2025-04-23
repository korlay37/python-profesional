import pytest
from modulo_pytest.pares import es_par

@pytest.mark.parametrize(
    "n, resultado", 
    [
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
    ]
)
def test_es_par(n: int, resultado: bool):
    assert es_par(n) == resultado