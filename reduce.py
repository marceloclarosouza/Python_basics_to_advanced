""" o reduce faz operaç~;oes seriadas e exige uma função com duas entradas (x, y)"""


from functools import reduce
numeros = [2,3,4,5,6]

multi = lambda x, y: x*y
res = reduce(multi, numeros)
print(res)

