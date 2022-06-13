import os 
vogais = ['a', 'e', 'i', 'o', 'u']
os.chdir('Exercicios_arquivos') # muda o diretorio de trabalho para a pasta Exercicios_arquivos

arquivo = open('exemplo.txt', 'r')

texto = arquivo.read()

count = 0

for letra in texto:
    if letra in vogais:
        count += 1  

print(count)