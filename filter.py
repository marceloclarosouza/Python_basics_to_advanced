""" filtrar valores usando filter e lambda"""

import statistics

valores = [1,2,3,4,5,6]

media = statistics.mean(valores)
maior_q_media = filter(lambda x: x > media, valores)## filter(funcao, iteravel)
print(list(maior_q_media))

""" elimimando valores ausentes"""
lista = ["um","", "dois", "tres", "quatro", "seis", "", ""]
res = filter(None, lista)
print(list(res))

"""Filtrar valore sinativos de dicionarios dentro de uma lista"""

dados = [{"username" : "calos", "tweets": ["oi", "tudo bem"]},
         {"username" : "alberto", "tweets": ["oi"]},
         {"username" : "sonia", "tweets": ["tudo bem"]},
         {"username" : "luffy", "tweets": []},
         {"username" : "fauno", "tweets": []}]

inativos = list(filter(lambda usuario: len(usuario["tweets"])==0,dados))
print(inativos)