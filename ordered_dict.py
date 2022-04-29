'''
Modulo Collections: Ordered Dict

from typing import OrderedDict


dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')


'''

from typing import OrderedDict


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

# True -> Já que a ordem dos elementos não importa para o dicionário
print(dict1 == dict2)

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Porque a ordem faz diferença nesse caso
