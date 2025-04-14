
# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)

# class Descriptor:
#     def __get__(self, instance, owner):
#         print("Accediendo al atributo")

#     def __set__(self, instance, value):
#         print(f"Asignando: {value}")

#     def __delete__(self, instance):
#         print("Eliminando atributo")

# class MiClase:
#     x = Descriptor()

# obj = MiClase()
# print(obj.x)
# obj.x = 10
# del obj.x

# class Nombre:
#     def __get__(self, instance: object, owner: type) -> str:
#         print("Accediendo")
#         return instance.__dict__["_nombre"]

#     def __set__(self, instance: object, value: str):
#         if not value.isalpha():
#             raise ValueError("El nombre debe contener letras")
#         instance.__dict__["_nombre"] = value

# class Persona:
#     nombre: Nombre = Nombre()

#     def __init__(self, nombre: str) -> None:
#         self.nombre = nombre

# p: Persona = Persona("111")
# print(p.nombre)

from datetime import datetime

class LazyFecha:
    def __get__(self, instance: object, owner: type) -> datetime:
        if "_fecha" not in instance.__dict__:
            print("Cargando fecha...")
            instance.__dict__["_fecha"] = datetime.now()
        return instance.__dict__["_fecha"]
    
class Documento:
    fecha_creacion: LazyFecha = LazyFecha() 

doc = Documento()
print(doc.fecha_creacion)
print(doc.fecha_creacion)