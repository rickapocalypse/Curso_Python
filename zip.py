'''
Zip

zip() -> cria um iterável(Zip Object) com os elementos de cada iterável passado como argumento.

'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zip1 = zip(list1, list2)  

print(zip1)

# Podes gerar uma lista, tuplas, ou dicionários a partir de um zip

print(list(zip1))
print(tuple(zip1))
print(dict(zip1))
print(set(zip1))

# O zip() utiliza o menor tamanho dos iterários passados como argumento.

prova1 = [80, 91,78,100,99]
prova2 = [80, 89, 50, 40,80]

alunos = ['maria', 'joao', 'pedro', 'joana', 'jose']
print(len(prova1)==len(alunos))
dados = list(zip(alunos, prova1, prova2))
for n in dados:
    media = (n[1] + n[2]) / 2
    print(f'{n[0]} tem media {media}')

#As maiores notas de cada aluno

maior = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(maior)

#Maior nota em certa prova

maior_nota1 = ['',0]
maior_nota2 = ['',0]

for n in dados:
    if n[1] > maior_nota1[1]:
        maior_nota1[1] = n[1]
        maior_nota1[0] = n[0]
    if n[2] > maior_nota2[1]:
        maior_nota2[1] = n[2]
        maior_nota2[0] = n[0]

print(maior_nota1)
print(maior_nota2)