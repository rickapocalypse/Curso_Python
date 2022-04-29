import random
x = 4
A = []

for l in range(x):
    line = []
    for c in range(x):
        line.append(random.randrange(1, 20))
    A.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))

for n in range(1, x):
    for l in range(x - n):
        A[l][l + n] = 0

print('-' * 18)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))
print(A)
