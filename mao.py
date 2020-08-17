import math

def area(r):
    """Calcula e retorna a area de um circulo de raio 'r'"""
    return math.pi * (r**2)

raio = [2,4,5,6,7,8,1,1.6]

area = map(area, raio)##Nesse caso o map substitui o For, e passa toda a lista pela função
print(list(area))