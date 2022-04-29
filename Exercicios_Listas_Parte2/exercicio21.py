import random
x = 2
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


r = ''

while r != 'sair':

    print('Aqui estão as matrizes')
    print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                     for row in a]))
    print('-' * 14)
    print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                     for row in b]))

    var = int(input(f'Escolha uma função. (1) Somar as matrizes. (2) Subtrair a primeira pela segunda. (3) Adicionar uma constante a matriz. Ou digite sair para parar a execução:'))

    if var == 1:
        matriz_soma = []
        for l in range(x):
            line = []
            for c in range(x):
                line.append(a[l][c] + b[l][c])
            matriz_soma.append(line)
        print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                         for row in matriz_soma]))

    elif var == 2:
        matriz_sub = []
        for l in range(x):
            line = []
            for c in range(x):
                line.append(b[l][c] - a[l][c])
            matriz_sub.append(line)
        print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                         for row in matriz_sub]))

    elif var == 3:
        cst = int(
            input(f' Informe a constante que deseja multiplicar as matrizes: '))
        matriz_cst1 = []
        matriz_cst2 = []
        for l in range(x):
            linea = []
            lineb = []
            for c in range(x):
                linea.append(a[l][c] * cst)
                lineb.append(b[l][c] * cst)
            matriz_cst1.append(linea)
            matriz_cst2.append(lineb)

        print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                         for row in matriz_cst1]))
        print('-'*14)
        print('\n'.join([''.join(['{:5}'.format(item) for item in row])
                         for row in matriz_cst2]))
