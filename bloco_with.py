'''
o Bloco with

passo a passo para se trabalhar com arquivos

1 - Abrir o arquivo
2 - Fazer alguma coisa
3 - Fechar o arquivo

O block with é utilizado para abrir e fechar o arquivo automaticamente
'''

with open('texto.txt') as arquivo:
    print(arquivo.read())