'''
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
'''

from collections import deque


deq = deque('Henrique')

print(deq)

# Adicionando elementos no deque

sobre = 'Santos'

for n in sobre:
    deq.append(n)

print(deq)

# Adicionando a esquerda

substantivo = 'Doutor'
sub = substantivo[::-1]

for n in sub:
    deq.appendleft(n)
print(deq)


# Removendo elementos
