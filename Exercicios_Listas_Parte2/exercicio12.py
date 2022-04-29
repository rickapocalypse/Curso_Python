import random
x = 4
A = []
T = []
for l in range(x):
    linea = []
    linet = []
    for c in range(x):
        linea.append(random.randrange(0, 9))
        linet.append(0)
    A.append(linea)
    T.append(linet)


print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))


for l in range(x):
    for c in range(x):
        T[l][c] = A[c][l]

print('=' * 12)
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in T]))
