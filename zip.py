"""gerar um lista com a maior nota de cada aluno usando zip"""

prova1 = (8, 7, 3)
prova2 = (3, 5, 7)
aluno = ("Maria", "Pedro", "Jose")

maior_nota = {dado[0]: max(dado[1], dado[2]) for dado in zip(aluno, prova1, prova2)}
print(maior_nota)

