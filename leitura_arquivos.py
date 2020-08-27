data = open("texto.txt", "r")##abrir arquivo modo leitura
data = open("texto.txt", "w")##abrir arquivo nodo escrita

data.read()##ler o arquivo
data.seek(x)##move o cursor para o para a posiçao X, seek(0) inicio
data.readline(x)##imprime a linha a linha
data.readlines()##imprime todas as linhas seprando-as por \n
data.split(' ')##cria uma lista de strings separdas por espaco

data.close() #fecha a coneção com o arquivo aberto open()


with(open('texto.txt')) as arquivo:##o bloco with abre e fecha o arquivo automaticamente após a execução
    print(arquivo.readlines())

