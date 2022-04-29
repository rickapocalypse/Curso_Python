import random

x = 10
A = []

for l in range(x):
    line = []
    for c in range(x):
        line.append(random.randrange(0, 10))
    A.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))

d = 0

for n in range(1, x):

    for l in range(x - n):

        d += A[l + n][l]


print(d)
