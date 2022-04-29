"""
List comprehension

-
Utilizando List comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável

# Sintaxe de List Comprehension

[ Dado for dado um iterável]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros ]

print(res)

res = [n / 2 for n in numeros]

print(res)

def funcao(valor):
    return valor ** valor

res = [funcao(n) for n in numeros]

print(res)

"""
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

print([numero * 3 for numero in range(1,10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])