"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outra linguagens,
com a diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.


Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    ou seja, nestas linguagens se vc criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.
Em Python :
    -Dinâmico: Não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos
    -Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;
 As listas em Python são representadas por colchete: []


# Podemos facilmente checar se determinado valor está contido na lista

if 8 in lista4:
    print('Encontrei o numero 8')
else:
    print('Não encontrei o número 8')

# Ordenando uma lista
lista1.sort()

print(lista1)

# Ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))


'''
Para adicionar elementos em lista, utilizamos a função append
'''

print(lista1)
lista1.append(42)
print(lista1)


# Para adicionar mais elementos, podemos utilizar uma lista

lista1.extend([8, 3, 1])
print(lista1)

# Para adicionar uma lista dentro de outra lista

lista1.append([8, 3, 1])
print(lista1)

# Para adicionar o elemento na parte desejada do vetor basta .insert(2, 'novo valor')
# Adiciona o 'novo valor' na posição 2

lista1.insert(0, 'corona')
print(lista1)

# Juntar lista
# lista6 = Lista 1 + lista 2 ;
# lista1.extend(lista2)


# Inverter uma lista
# lista1.reverse() ;
# print(lista1[::-1]).


# contagem de elementos de listas len('lista desejada aqui')

# removendo elemento de uma lista  lista.pop() o ultimo dado
# podemos remover um elemento pelo indice no proprio .pop()

# para remover todos os elementos utilizamos o .clear()


# convertendo string para lista
#curso = 'programação em python: Essencial'
#curso = curso.split()

# montando uma string
#lista['sim', 'não', 'e', 'talvez']
#curso = ' '.join(lista)
# pega a lista, coloca espaço entre cada elemento e me devolva uma string


# Iterando sobre listas
'''
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print (elemento)
'''



carrinho = []
produto = ''

while produto != 'sair':
    produto = input(
        'Adicione um produto na lista ou digite "sair" para sair: ')
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)



# Fazendo acesso aos elementos da lista, de forma indexada

cores = ['verde', 'amarelo', 'azul']
print(cores[0]) #verde

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice =+ 1

#criando um indice
for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar o indice de um elemento na lista
numero = [5, 6, 7, 8, 9]

print(numero.index(6))

print(numero.index(5, 1))   #buscar a partir do indice 1
print(numero.index(5,1,9))  #buscar o valor 5, entre os indices 1 e 9

#trabalhando com slice de lista com parâmetro 'inicio'
lista = [1, 2, 3, 4]
print(lista[1:])  #iniciando do índice 1



print(sum(lista))   #soma
print(max(lista))   #max valor
print(min(lista))   #min valor
print(len(lista))   #tamanho


"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['H', 'e', 'n', 'r', 'i', 'q', 'u', 'e']

lista3 = []

lista4 = list(range(11))

lista5 = list('Henrique')

# desempacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
