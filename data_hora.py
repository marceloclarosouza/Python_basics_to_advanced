import datetime

atual = datetime.datetime.now()#retorno a data e hora atual
print(atual)
atualizado = atual.replace(hour = 10, minute = 10, second = 5)##alterar data e hora com replace()
print(atualizado)
evento = datetime.datetime(2020,12,22,18,30,0)#cruiar uma data e hora
print(evento)

##calcular quanti dias faltam p um evento
atual = datetime.datetime.now()
evento = datetime.datetime(2020, 12, 22, 18, 30, 0)
intervalo = evento -atual
print(intervalo)
print(intervalo.days)#dias que faltam
print(intervalo.seconds //60//60)#horas que faltam

#determinar prazo de pagamento de boleto
compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days = 3)##intervalo de tempo 
vencimento = compra + regra_boleto
print(vencimento)

#agendar a manutecao de backup p as 0h usando combine()
backup = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days = 1)), datetime.time())#datetime.time() indica que será as 0h
print(backup)

#encontrar od ia da semana que um evento ocorreu ou vai ocorrer
backup = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days = 1)), datetime.time())
print(backup.weekday())

#formatar data e hora usando strftime   F

hoje = datetime.datetime.now()
hoje_formatado = hoje.strftime("%d-%m-%Y %H:%M:%S")#%B retorna o nome do mes, %b retorna a sigla do mes; %Y 2020, %y 20
print(hoje_formatado)


#formatar data e hora usando strptime   P

data = input("d/m/ano\n")
data_corrigida = datetime.datetime.strptime(data, '%d/%m/%Y')
print(data_corrigida)

#somente hora

almoco = datetime.time(12,30,0)
print(almoco)

"""
#configurar data e hora para portugues
#pip install textblob

import datetime
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to = 'pt-br')} de {data.year}"

data = datetime.datetime.now()
print(data)"""


#verificar tempo de execução de um teste
import timeit, functools

def test(n):
	soma = 0
	for num in range(n*200):
		soma = soma + num**num+4
	return soma

print(timeit.timeit(functools.partial(test, 5), number = 1000))
