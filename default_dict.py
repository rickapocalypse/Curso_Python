"""
Modulo Collection - Default dict

# Recap Dicionário 

dicionario = {'curso':'Programação em Python'}

print(dicionario)

print(dicionario('curso'))


Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentarmos acessar uma chave que não existe, essa chave então 
será criada e o valor default será atribuída.

OBS: Lambdas são funções sem nome, que podem ou não receber parámetros 
de entrada e retornar valores
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python'
