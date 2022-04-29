dados = {}
nome = ''
while nome != 'sair':
    nome = input('Qual o nome do aluno ? Digite sair para terminar ')
    if nome == 'sair':
        break
    altura = float(input('Qual a altura desse aluno ? '))
    dados[nome] = altura

print(dados)

menor = min(dados.values())
maior = max(dados.values())

for n in dados:
    if dados.get(n) == menor:
        print(f'O {n} é o menor com {dados.get(n)} metros')

for n in dados:
    if dados.get(n) == maior:
        print(f'O {n} é o maior com {dados.get(n)} metros')
