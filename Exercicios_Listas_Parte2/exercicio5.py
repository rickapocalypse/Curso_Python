import random
a = []

for l in range(5):
    line = []
    for c in range(5):
        line.append(random.randrange(0, 25))
    a.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in a]))

x = int(input('Agora que viu a matriz, informe um numero, se ele estiver na matriz, vou te retornar a sua posição'))

indice_linha = 0
indice_coluna = 0

for l in range(5):
    for c in range(5):
        if a[l][c] == x:
            print(
                f'Encontrei o valor {a[l][c]} e está na linha {l} e coluna {c}')
