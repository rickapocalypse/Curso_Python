'''
Modulo Collection - named tuple

recapitulando tuplas

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a 
mesma e também parâmetros

'''
from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
paty = cachorro(idade=3, raca='yorkshire', nome='Paty')

print(ray)

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(paty)
