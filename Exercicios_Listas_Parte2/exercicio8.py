import random
x = int(input(f'Informe o tamanho da raiz quadrado que deseja, vou calcular a diagonal principal'))
A = []

for l in range(x):
    line = []
    for c in range(x):
        line.append(random.randrange(0, 9))
    A.append(line)

c = 0

for l in range(x - 1):
    c += A[l][l + 1]

print('A matriz então')
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))
print(f'A diagonal principal é {c}')
