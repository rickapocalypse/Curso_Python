import random
A = []

# Criando a Matriz

for l in range(4):
    line = []
    for c in range(4):
        line.append(random.randrange(1, 20))
    A.append(line)

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in A]))

qtd_maior_dez = 0
# Acessando os elementos da matriz
for l in range(4):
    for c in range(4):
        if A[l][c] > 10:
            qtd_maior_dez += 1
print(f'Apareceu {qtd_maior_dez} números maiores que 10')
