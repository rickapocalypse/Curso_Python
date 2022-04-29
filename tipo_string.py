"""
Tipo string

É uma variável do tipo referência, ou seja, contém um endereço do objeto(instanvia) 

Em python, um dado é considerado do tipo string sempre que:

Estiver entre àspas simples, duplas, simples tripas e duplas triplas.

\n            -> pula uma linha

"""
# Como o Python entende a minha String
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13]
# ['r', 'i', 'c', 'k', ' ', 'a', 'p', 'o', 'c', 'a', 'l', 'p', 's', 'e']
nome = 'rick apocalypse'
print(nome.title())

print(nome[0:4].title())

#.split() faz um vetor linha de palavras, se transformar em vetor linha de frases
#['rick', 'apocalypse']

#[ : : -1] -> comece no primeiro elemento, v[a at[e o ultimo elemento e inverta]]
#.raplace ('' , '') trocas todas as letras do primeiro '' por a letra do segundo ''