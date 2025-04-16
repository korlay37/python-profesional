from dataclasses import dataclass

# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, 
# frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)

@dataclass
class Persona:
    nombre: str
    edad: int

@dataclass(frozen=True)
class Personas:
    personas: list[Persona]

persona1: Persona = Persona("Eduardo", 33)
persona2: Persona = Persona("Juan", 28)
personas: Personas = Personas([persona1, persona2])

personas.personas[0] = Persona("Luis", 50)
print(personas.personas)
