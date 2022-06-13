import os

vogais = ['a', 'e', 'i', 'o', 'u']

os.chdir('Exercicios_arquivos') # muda o diretorio de trabalho para a pasta Exercicios_arquivos

arquivo = open('exemplo.txt', 'r')

texto = arquivo.read()
vCount = 0
cCount = 0

for letra in texto:
    if letra in vogais:
        vCount += 1
    else:
        cCount += 1

print(f'No arquivo lido, temos {vCount} vogais e {cCount} consoantes')