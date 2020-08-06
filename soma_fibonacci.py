"""
faça um programa que some os termos pares da sequencia de Fibonacci, cujos valores não ultrapassem 4 milhões
"""


num = 0
f1 = 1
f2 = 1
temp = 0

while num < 4000000:
    num = f1 + f2
    print(num)
    temp = f2
    f2 = num
    f1 = temp    
