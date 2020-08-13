"""
Escreva uma função que gera um triângulo lateral de altura 2*n-1 e na largura.
"""

def triangulo_lateral(largura):
    n = 2*largura-1
    for n in range(1,largura +1):
        print('*'*n)
        if n == 4:
           for n in range(largura -1, 0, -1):
                print('*'*n)
       
triangulo_lateral(4)