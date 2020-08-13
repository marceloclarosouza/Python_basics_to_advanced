"""
Calcule o fatorial quadruplo de n, (2n)!/n!
"""

def fatorial_q(numero):
    numerador = 1
    denominador = 1
    for n in range(numero, 1, -1):
        numerador = numerador*(2*n)
    for d in range(numero, 1, -1):
        denominador = denominador*n       
    return numerador/denominador

print(fatorial_q(5))
