# para ler o arquivo de outro diretorio basta usar o caminho absoluto
import os
os.chdir('Exercicios_arquivos') # muda o diretorio de trabalho para a pasta Exercicios_arquivos

arquivo = open('exemplo.txt', 'r') 
linhas = 0
for linha in arquivo:
    linhas += 1
print(linhas)