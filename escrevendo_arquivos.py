"""with open("texto.txt", "w") as data:##criar um arquivo
    ##digite a sequencia de instrucoes
    data.write("Escreva o conteuúdo de ...\n")
    data.write("Conitnue escrevendo...\n")"""
    
    
"""Exemplo usando loop"""
"""
with (open ("fruta.txt", "w")) as data:
    while True:
        fruta = input("Digite o nome de uma fruta ou sair\n")
        if fruta != 'sair':
            data.write(fruta + "\n")
        else:
            break
"""


"""with (open("fruta.txt", "x")) as data:""" #cria um arquivo p escrita. caso exista um arquivo com o mesmo nome, o arquivo n~;ao será sobreposto como ocorre com o "w"

"""
##abrir arquivos p leitura e adicionar conteúdo ao final dos dados existentes
with (open("fruta.txt", "a")) as data:
    while True:
        fruta = input("Digite o nome de uma fruta ou sair\n")
        if fruta != 'sair':
            data.write(fruta + "\n")
        else:
            break"""
 