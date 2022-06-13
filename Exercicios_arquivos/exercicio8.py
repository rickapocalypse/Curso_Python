import os 
os.chdir('Exercicios_arquivos')



with open('exemplo.txt', 'r') as arquivo:
    arquivo = arquivo.read()

texto = arquivo.upper()

name_file = input('Digite o nome do arquivo: ')

with open(f'{name_file}.txt', 'w') as arquivo:
    arquivo.write(texto)

print(open(f'{name_file}.txt', 'r').read())
option = input('Deseja remover o arquivo? (y/n) ')
if option == 'y':
    os.remove(f'{name_file}.txt')
else:
    print('Arquivo não removido')