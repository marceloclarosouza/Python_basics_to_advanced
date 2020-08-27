"""with open("texto.txt", "w") as data:##criar um arquivo
    ##digite a sequencia de instrucoes
    data.write("Escreva o conteuúdo de ...\n")
    data.write("Conitnue escrevendo...\n")"""
    
    
"""Exemplo usando loop"""

with (open ("fruta.txt", "w")) as data:
    while True:
        fruta = input("Digite o nome de uma fruta ou sair\n")
        if fruta != 'sair':
            data.write(fruta)
            data.write("\n")
        else:
            break
