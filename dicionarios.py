"""
Dicionários

 Obs : Em algumas linguagens, pode ser conhecido como mapas

 Dicionários são coleções do tipo chave/valor.

 Dicionários são representados por {chave:valor}


# Forma 1 para criação de dicionários

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma 2

paises = dict(br='brasil', eua='Estados Unidos', py='Paraguay')



paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Acessando via chave, dá mesma forma que lista/tupla
print(paises['br'])
print(paises.get('br'))

pais = paises.get('py')
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')

# Esse comando diz, procura ru para mim, se não achar, coloque 'não encontrado' no lugar
pais = paises.get('ru', 'Não encontrado')


# Ele busca se determinada chave está em um dicionário, retornando True ou False
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)



# Dicionários com outras variaveis

loc = {
    (123.4444, 10.1010): 'Escritorio em Tókio',
    (123.4445, 11.1101): 'Escritorio em São Paulo',
    (123.4456, 12.1102): 'Escritorio em NY'
}
print(loc)

"""

# Adicionando elementos em um dicionário

"""

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# adicionando
receita['abr'] = 350

novo_dado = {'mai': 500}

receita.update(novo_dado)
print(receita)
# Atualizando dados
receita['mai'] = 550
print(receita)



# Removendo dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
# Forma 1
receita.pop('mar')

print(receita)

del receita['fev']

print(receita)




# Carrinho de compras

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150]

carrinho.append(produto1)
carrinho.append(produto2)
# utilizando Tupla para

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150]

carrinho = (produto1, produto2)

# utilizando dicionário

carrinho = []

produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'Quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)


# métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)

# limpar dicionário
d.clear()
print(d)


# Copiando um dicionário para outro

novo = d.copy()

print(novo)

novo['d'] = 4

print(novo)


# ou

novo = d

print(novo)

novo['d'] = 4

print(novo)


# fromkeys cria varias chaves para um determinado valor

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)


"""

# métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)

# fromkeys cria varias chaves para um determinado valor

usuario = {}.fromkeys('abcdefjh', 1)
print(usuario)
