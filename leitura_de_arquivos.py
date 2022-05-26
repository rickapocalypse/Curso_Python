'''
Leitura de Arquivos

Para o conteúdo de um arquivo Python, utilizamos a função open()

open() -> A função open() recebe como parâmetro o nome do arquivo que desejamos ler.
retornando um io.TextIOWrapper
'''

arquivo = open('texto.txt')

print(arquivo.read())