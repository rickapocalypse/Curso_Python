import os

os.chdir('Exercicios_arquivos')

name_archive = str(input(f'Digite o nome do arquivo: ')) + '.txt'
find_word = str(input(f'Digite a palavra: ')).lower()

with open(name_archive, 'r') as arquivo:
    words = arquivo.read().lower()

num_words = words.count(find_word)
print(num_words)
