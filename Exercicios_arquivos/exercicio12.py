import os 
os.chdir('Exercicios_arquivos')

with open('exemplo_junto.txt', 'r') as arquivo:
    words = arquivo.readlines()  

print(f'O texto tem {len(words)} linhas')
words = ''.join(words).lower()
print(f'O texto tem {len(words.split())} palavras')
print(f'O texto tem {len(words)} letras')
dict = {}

for word in words.split():
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)

for word in dict:
    print(f'A palavra {word} aparece {dict[word]} vezes')
