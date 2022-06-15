import os
os.chdir('Exercicios_arquivos')

with open('matrix.txt', 'r') as arquivo:
    lines = arquivo.read()


lines = lines.split('\n')
print(lines)
matriz = []
for line in range(int(lines[0][0])):
    matriz.append([])
    for column in range(int(lines[0][2])):
        matriz[line].append(1)
matriz[int(lines[1][0])][int(lines[1][2])] = 0
matriz[int(lines[2][0])][int(lines[2][2])] = 0

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                 for row in matriz]))