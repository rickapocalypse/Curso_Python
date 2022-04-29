import random
a = []
linha_a = 3
coluna_a = 3


for l in range(linha_a):
    a.append([])
    for c in range(coluna_a):
        a[l].append(random.randrange(1, 10))

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in a]))

linha_a = len(a)
coluna_a = len(a[0])


if len(a[0]) == len(a):
    b = []
    for l in range(linha_a):
        b.append([])
        for c in range(coluna_a):
            b[l].append(0)
            for k in range(coluna_a):
                b[l][c] += a[l][k] * a[k][c]

    print('sua matriz quadrado então é')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in b]))

else:
    print('Essa matriz não pode ter um produto por ela mesma, pois a coluna de "a" se difere da linha de "a"')
