from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2
    
    def perimetro(self) -> float:
        return 4 * self.lado
    
class Circulo(Forma):
    def __init__(self, radio: float) -> None:
        self.radio = radio

    def area(self) -> float:
        return 3.1416 * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * 3.1416 * self.radio

c = Cuadrado(2.2)