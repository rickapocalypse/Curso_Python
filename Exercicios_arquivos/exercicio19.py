import os
os.chdir('Exercicios_arquivos')

with open('aluno_nota.txt', 'r') as arquivo:
    lines = arquivo.read()

aluno_maior = ''
nota_maior = 0

for alunos_notas in lines.split('\n'):
    alunos_notas = alunos_notas.split(' ')
    print(f'O aluno {alunos_notas[1]} tem nota {alunos_notas[-1]}')
    if float(alunos_notas[-1]) > nota_maior:
        nota_maior = float(alunos_notas[-1])
        aluno_maior = alunos_notas[1]
print(f'O aluno {aluno_maior} tem a maior nota {nota_maior}')