import random
A = []

linhas = 3
colunas = 6

for l in range(linhas):
    line = []
    for c in range(colunas):
        line.append(random.randrange(0, 10))
    A.append(line)

print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                 for row in A]))
soma = 0

for l in range(linhas):
    for c in range(colunas):
        if c % 2 != 0:
            soma += A[l][c]
print(soma)

media = 0

for l in range(linhas):
    for c in range(colunas):
        if c == 2:
            media += A[l][c]
        elif c == 4:
            media += A[l][c]

media = media / 2
print(media)

sub = []
for l in range(linhas):
    sub.append(A[l][1] + A[l][2])
print(sub)

for l in range(linhas):
    A[l][5] = sub[l]

print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                 for row in A]))
