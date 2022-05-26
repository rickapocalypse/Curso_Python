'''
Seek e cursors

seek() -> Move o cursor para a posição especificada

'''

arquivo = open('texto.txt')
print(arquivo.read())

#movimentando o cursor pelo arquivo com função seek()

arquivo.seek(0)

#readline() -> Lê uma linha do arquivo

'''
Para trabalhar com arquivos:

1 - Abrir o arquivo
2 - Fazer alguma coisa
3 - Fechar o arquivo
'''
# 1 - abrir o arquivo
arquivo = open('texto.txt')
# 2 - fazer alguma coisa
print(arquivo.readline())
print(arquivo.readline())
# 3 - fechar o arquivo
arquivo.close()

# Verificar se o arquivo está aberto

print(arquivo.closed) #True é por que está fechado