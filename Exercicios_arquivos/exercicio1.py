import os

with open('exercicio1.txt', 'w') as arquivo:
    c = 'oi'
    while c != "0":
        c = input(f'digite o carácter, ou 0 para sair: ')
        arquivo.write(c)

print(open('exercicio1.txt').read())

os.remove('exercicio1.txt')