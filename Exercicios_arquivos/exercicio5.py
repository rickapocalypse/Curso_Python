import os 
os.chdir('Exercicios_arquivos') # muda o diretorio de trabalho para a pasta Exercicios_arquivos

entrada = input(f'Digite a letra: ')

with open('exemplo.txt', 'r') as arquivo:
    arquivo = arquivo.read()
    count = 0
    for letra in arquivo:
        if letra == entrada:
            count += 1

print(count)