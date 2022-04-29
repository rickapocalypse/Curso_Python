import random

a = []
b = []
C = []
for l in range(4):
    lineA = []
    lineB = []
    for c in range(4):
        lineA.append(random.randrange(0, 25))
        lineB.append(random.randrange(0, 25))

    a.append(lineA)
    b.append(lineB)


print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in a]))
print('-'*18)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in b]))

# Criando uma matriz nula para ser substituída pelos maiores valores das matrizes a e b


for l in range(4):
    line = []
    for c in range(4):
        line.append(0)

    C.append(line)


# Encontrando os números nas matrizes


for l in range(4):
    for c in range(4):
        if a[l][c] >= b[l][c]:

            C[l][c] = a[l][c]
        else:
            C[l][c] = b[l][c]

print('-'*18)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in C]))
