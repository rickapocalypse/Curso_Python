import itertools
x = 52
y = 25

with open('arq.txt', 'w') as arquivo:

    for i, j in zip(str(x), str(y)):
        arquivo.write(f'{x} e {y}')