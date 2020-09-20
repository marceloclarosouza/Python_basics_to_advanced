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

#formatar data e hora usando strftime

hoje = datetime.datetime.now()
hoje_formatado = hoje.strftime("%d-%m-%Y %H:%M:%S")
print(hoje_formatado)