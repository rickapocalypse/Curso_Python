'''
Escrevendo em arquivos

1 - Abrir um arquivo
2 - Escrever algo no arquivo
3 - Fechar o arquivo

Abrir o arquivo no formato de escrita

'''

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é fácil. \n')
    arquivo.write('Acesse o site https://www.python.org.br')