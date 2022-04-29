import random

a = []

for l in range(4):
    line = []
    for c in range(4):
        line.append(random.randrange(0, 20))
    a.append(line)


print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in a]))


maior = a[0][0]
indice_linha = 0
indice_coluna = 0
for l in range(4):
    for c in range(4):
        if a[l][c] > maior:
            maior = a[l][c]
            indice_linha = l
            indice_coluna = c

print(
    f'O maior elemento dá matriz é o {maior}, estã na linha {indice_linha} e na coluna {indice_coluna}')
