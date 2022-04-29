import random
linha = 10
coluna = 3

alunos = linha
notas = coluna

notas_da_turma = []

for l in range(linha):
    nota = []
    for c in range(coluna):
        nota.append(random.randrange(0, 10))
    notas_da_turma.append(nota)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in notas_da_turma]))

for l in range(linha):
    if notas_da_turma[l][0] < notas_da_turma[l][1] and notas_da_turma[l][0] < notas_da_turma[l][2]:
        print(
            f'O aluno {l + 1} teve sua pior nota na primeira prova, indo com {notas_da_turma[l][0]}')
