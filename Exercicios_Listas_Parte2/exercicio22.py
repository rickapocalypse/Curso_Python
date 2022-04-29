import random
x = 3
a = []
b = []

for l in range(x):
    linea = []
    lineb = []
    for c in range(x):
        linea.append(random.randrange(1, 10))
        lineb.append(random.randrange(1, 10))
    a.append(linea)
    b.append(lineb)

print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                 for row in a]))
print('-'*20)
print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                 for row in b]))
print('-'*20)
linhas_a = len(a)
colunas_a = len(a[0])
linhas_b = len(b)
colunas_b = len(b[0])


if colunas_a == linhas_b:

    C = []

    for l in range(linhas_a):
        C.append([])
        for c in range(colunas_b):
            C[l].append(0)
            for k in range(colunas_a):
                C[l][c] += a[l][k] * b[k][c]

    print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                     for row in C]))


else:
    print('não dá para fazer o produto')
