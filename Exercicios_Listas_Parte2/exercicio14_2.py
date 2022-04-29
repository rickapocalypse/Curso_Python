import random
from typing import Counter

x = 5

sorteados = random.sample(range(1, 100), x**2)

A = [sorteados[i::x] for i in range(x)]

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))
