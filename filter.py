""" filtrar valores usando filter e lambda"""

import statistics

valores = [1,2,3,4,5,6]

media = statistics.mean(valores)
maior_q_media = filter(lambda x: x > media, valores)## filter(funcao, iteravel)
print(list(maior_q_media))

""" eli,imando valores ausentes"""
lista = ["um","", "dois", "tres", "quatro", "seis", "", ""]
res = filter(None, lista)
print(list(res))