import random
from typing import Counter
A = []

for l in range(5):
    line = []
    for c in range(5):
        line.append(random.randrange(1, 99))
    A.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))

list = []

for l in range(5):
    for c in range(5):
        list.append(A[l][c])


res = Counter(list)
print(res)

repitidos = []

for n in res:
    if res[n] > 1:
        repitidos.append(n)

print(repitidos)

for l in range(5):
    for c in range(5):
        for n in repitidos:
            if n == A[l][c]:
                A[l][c] = 0

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))
