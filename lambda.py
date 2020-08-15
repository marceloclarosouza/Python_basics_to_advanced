"""
funções lambdas são funções sem nome
"""
nome = ['aline simsic', 'pud d. luffy', 'marcelo souza', 'panceta gorda', 'jimbei']

nome.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())##ordenar os nomes pelo último sobrenome
print(nome)
