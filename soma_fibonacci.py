"""
faça um programa que some os termos pares da sequencia de Fibonacci, cujos valores não ultrapassem 4 milhões
"""


num = 0
f1 = 1
f2 = 1
temp = 0
soma = 0

while f2 < 4000000:
    num = f1 + f2
    print(f2)
    if f2 % 2 == 0:
        soma += f2
    temp = f2
    f2 = num
    f1 = temp
print(f'soma = {soma}')
