import random
A = []
linhas = 5
colunas = 4

primeira_coluna = 1
segunda_coluna = 1
terceira_coluna = 1
quarta_coluna = 1

for l in range(linhas):
    dados = []
    # Eu sei que não é necessario, mas acho que me ajuda a manter a ordem
    for c in range(primeira_coluna):
        dados.append(random.randrange(1000, 3000))
        #matricula = int(input(f'Informe o nome de matricula do {l} aluno:'))
    for c in range(segunda_coluna):
        dados.append(random.randrange(0, 10))
    for c in range(terceira_coluna):
        dados.append(random.randrange(0, 10))
    for c in range(quarta_coluna):
        dados.append((dados[1] + dados[2])/2)

    A.append(dados)

print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                 for row in A]))

for l in range(linhas):
    if A[l][3] >= 5:
        print(
            f'O Aluno, com a matricula {A[l][0]}, tirou {A[l][1]} nas provas e {A[l][2]} nos trabalhos, ficando com a média {A[l][3]}. Está aprovado ')
    else:
        print(
            f'O Aluno, com a matricula {A[l][0]}, tirou {A[l][1]} nas provas e {A[l][2]} nos trabalhos, ficando com a média {A[l][3]}. Está reprovado ')
