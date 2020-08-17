""" filtrar valores usando filter e lambda"""

import statistics

valores = 1,2,3,4,5,6

media = statistics.mean(valores)
maior_q_media = filter(lambda x: x > media, valores)
print(list(maior_q_media))