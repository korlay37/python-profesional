
# class MiMeta(type):
#     def __new__(cls, name, bases, dct) -> object:
#         name = "CLASE_" + name
#         return super().__new__(cls, name, bases, dct)
    
# class MiClase(metaclass=MiMeta):
#     atributo = 1

# type(name, bases, dict)
# MiClase = MiMeta("MiClase", (object,), {"atributo": 1})
# class MiMeta(type):
#     def __new__(cls, name, bases, dct) -> object:
#         dct["mi_atributo"] = "Este es un atributo comun"
#         return super().__new__(cls, name, bases, dct)
    
# class MiClase(metaclass=MiMeta):
#     pass

# class ValidarAtributos(type):
#     def __new__(cls, name, bases, dct) -> object:
#         if "nombre" not in dct:
#             raise TypeError("La clase debe tener atributo nombre")
#         return super().__new__(cls, name, bases, dct)
    
# class ClaseConNombre(metaclass=ValidarAtributos):
#     pass
    # nombre = "Clase valida"

# class SingletonMeta(type):
#     _instances: dict = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
    
# class Singleton(metaclass=SingletonMeta):
#     pass

# a = Singleton()
# b = Singleton()

# print(a is b)

class MiMeta(type):
    def __new__(cls, name, bases, dct):
        if not name.startswith("Clase"):
            raise ValueError("Las clases deben iniciar con 'Clase'")
        return super().__new__(cls, name, bases, dct)
    
class ClaseValida(metaclass=MiMeta):
    pass

class MalaValida(metaclass=MiMeta):
    pass