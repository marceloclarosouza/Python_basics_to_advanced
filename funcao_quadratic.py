
def gerador_funcao_quadratica(a, b, c):
    """retorna f(x)= a*x**2 + b*x +c"""
    return lambda x: a * x ** 2 + b * x + c ## o lambda x sera o teste do print

teste = gerador_funcao_quadratica(2, 3, -5)##gera do "f(x)"

print(teste(0))
print(teste(1))
print(teste(2))

#ou
print(gerador_funcao_quadratica(2,3,-5)(2))
