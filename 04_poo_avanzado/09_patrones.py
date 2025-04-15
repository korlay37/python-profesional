
from typing import Optional, Type
from abc import ABC, abstractmethod
# Singleton
# class Singleton:
#     _instance: Optional["Singleton"] = None

#     def __new__(cls: Type["Singleton"]) -> "Singleton":
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
    
# a = Singleton()
# b = Singleton()
# print(a is b)

# Factory
# class Animal(ABC):
#     @abstractmethod
#     def hablar(self):
#         pass

# class Perro(Animal):
#     def hablar(self):
#         return "woof"

# class Gato(Animal):
#     def hablar(self):
#         return "miau"

# class AnimalFactory:
#     @staticmethod
#     def crear_animal(tipo: str) -> Animal:
#         if tipo == "perro":
#             return Perro()
#         elif tipo == "gato":
#             return Gato()
#         else:
#             raise ValueError("Animal desconocido")

# animal = AnimalFactory.crear_animal("gato")
# print(animal.hablar())

# Strategy
# class Estrategia(ABC):
#     @abstractmethod
#     def ejecutar(self, a, b):
#         pass

# class Suma(Estrategia):
#     def ejecutar(self, a, b):
#         return a + b

# class Resta(Estrategia):
#     def ejecutar(self, a, b):
#         return a - b
    
# class Contexto:
#     def __init__(self, estrategia: Estrategia):
#         self.estrategia = estrategia

#     def establecer_estrategia(self, estrategia: Estrategia):
#         self.estrategia = estrategia

#     def ejecutar_operacion(self, a, b):
#         return self.estrategia.ejecutar(a, b)
    
# contexto = Contexto(Suma())
# print(contexto.ejecutar_operacion(5, 3))
# contexto.establecer_estrategia(Resta())
# print(contexto.ejecutar_operacion(5, 3))

# Decorator
class Vehiculo:
    def mover(self):
        return " El vehiculo se esta moviendo"

class VehiculoDecorator:
    def __init__(self, vehiculo: Vehiculo):
        self._vehiculo = vehiculo

    def mover(self):
        return self._vehiculo.mover()
    
class VehiculoConAireAcondicionado(VehiculoDecorator):
    def mover(self):
        return f"{self._vehiculo.mover()} con aire acondicionado"
    
vehiculo = Vehiculo()
vehiculo_con_aire = VehiculoConAireAcondicionado(vehiculo)
print(vehiculo_con_aire.mover())
