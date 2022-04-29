import random
x = 3

A = []

for l in range(x):
    line = []
    for c in range(x):
        line.append(random.randrange(0, 10))
    A.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))

soma_coluna = []

for c in range(x):
    soma = []
    for l in range(x):
        soma.append(A[l][c])

    soma_coluna.append(sum(soma))
print(soma_coluna)
