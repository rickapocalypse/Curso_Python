'''
Reduce


Reduce é uma função que recebe uma lista e uma função e retorna um único valor.
Imagine que voce tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

E vc tem uma função que recebe dois parâmetros:

def funcao(a, b):
    return a * b

reduce(funcao, dados)

A funcao reduce() funciona da seguinte forma:
passo 1: res1 = funcao(a1, a2) Aplicada a função nos dois primeiros elementos de coleção e guarda o resultado
passo 2: res2 = funcao(res1, a3) Aplicada a função nos dois primeiros elementos de coleção e guarda o resultado

Isto é, aplica a função aos dois primeiros elementos de coleção e guarda o resultado.

reduce é bom para fazer somatorios e produtorios.
'''

from functools import reduce
dados = [2,3,4,5,7,11,13,17,19,23,29]

multi = lambda x,y: x*y

print(reduce(multi, dados))