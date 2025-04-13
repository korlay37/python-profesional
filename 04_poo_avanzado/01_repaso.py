

class Persona:
    def __init__(self, nombre: str, edad: int)-> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre} y tengo {self.edad}"



# HERENCIA
class Estudiante(Persona): 
    def __init__(self, nombre: str, edad: int, carrera: str) -> None:
        super().__init__(nombre, edad)
        self.carrera: str = carrera

    def saludar(self) -> str:
        return f"Soy {self.nombre}, estudio {self.carrera} y tengo {self.edad}"
    
persona1: Persona = Persona("Ana", 30)
print( persona1.saludar())
estudiante1: Estudiante= Estudiante("Luis", 22, "Ingenieria")
print(estudiante1.saludar())