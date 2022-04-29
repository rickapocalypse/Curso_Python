from typing import Deque
import random
linha = 5
coluna = 10
provas = []

for l in range(linha):
    line = []
    for c in range(coluna):
        line.append(random.choice('abcd'))
    provas.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in provas]))

gabarito = ['a', 'b', 'c', 'd', 'a', 'a', 'b', 'c', 'd', 'a']

notas = {}


for l in range(linha):
    nota = []
    for c in range(coluna):
        if provas[l][c] == gabarito[c]:
            nota.append(1)
    notas[f'aluno {l + 1}'] = len(nota)
print(notas)

# Sistema de aprovação

for n in notas:
    if notas[n] >= 5:
        print(f'O {n} está aprovado com a nota de {notas[n]}. Parabéns')
    else:
        print(f'O {n} está reprovado com a nota de {notas[n]}.')
