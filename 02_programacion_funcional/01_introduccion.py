
# Programacion Imperativa/ Procedural
# numeros: list = [1,2,3,4]
# dobles: list = []

# for n in numeros: 
#     dobles.append(n * 2)

# print(dobles)

#  POO
# class Calculadora:
#     def __init__(self):
#         self.total = 0
    
#     def suma(self, n: int) -> None:
#         self.total += n

# calc: Calculadora = Calculadora()
# calc.suma(5)
# print(calc.total)

# Programacion Funcional
numeros: list = [1,2,3,4,5]
dobles = list(map(lambda x: x * 2, numeros))

print(dobles)