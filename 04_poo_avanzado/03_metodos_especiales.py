
# __init__, __str__, __repr__, __len__
# Comparacion: __eq__, __lt__, __gt__  (==, <, >)
# __hash__
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"{self.nombre} tiene {self.edad}"
    
    def __repr__(self) -> str:
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Persona):
            return NotImplemented
        return self.nombre == other.nombre and self.edad == other.edad
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Persona):
            return NotImplemented
        return self.edad < other.edad
    
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Persona):
            return NotImplemented
        return self.edad > other.edad
    
    def __hash__(self) -> int:
        return hash((self.nombre, self.edad))
    
    def __len__(self) -> int:
        return len(self.nombre)

    
# persona1 = Persona("Juan", 28)
# print(len(persona1))
# persona2 = Persona("Juan", 28)
# personas = {persona1}
# print(persona2 in personas)
# print(persona1 > persona2)


# __getitem__
# __setitem__
# __call__, __bool__, __new__
class Grupo():
    def __init__(self, miembros: list) -> None:
        self.miembros: list = miembros

    def __getitem__(self, index: int) -> str:
        return self.miembros[index]
    
    def __setitem__(self, index: int, valor: str) -> None:
        self.miembros[index] = valor

    def __call__(self) -> str:
        return "Hola desde el grupo!"
    
    def __bool__(self) -> bool:
        return len(self.miembros) > 10
    
g = Grupo(["Ana", "Luis", "Eduardo"])
g[1] = "Pepe"
print(g[1])
print(bool(g))