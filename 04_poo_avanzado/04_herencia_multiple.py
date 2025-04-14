
# MRO Method Resolution Order
# class Volador:
#     def volar(self) -> str:
#         return "Estoy volando"

# class Nadador:
#     def nadar(self) -> str:
#         return "Estoy nadando"
    
# class Pato(Volador, Nadador):
#     pass

# pato: Pato = Pato()
# # print(pato.volar())
# # print(pato.nadar())
# print(Pato.__mro__)

class A:
    def __init__(self) -> None:
        print("Init A")

class B(A):
    def __init__(self) -> None:
        print("Init B")
        super().__init__()

class C(A):
    def __init__(self) -> None:
        print("Init C")
        super().__init__()

class D(B, C):
    def __init__(self) -> None:
        print("Init D")
        super().__init__()

d = D()