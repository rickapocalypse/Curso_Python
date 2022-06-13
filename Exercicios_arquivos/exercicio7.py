import os
os.chdir('Exercicios_arquivos')
vogais = ['a', 'e', 'i', 'o', 'u']


with open('exemplo.txt', 'r') as arquivo:
    texto = arquivo.read()

def switch_vogal(letra):
    if letra in vogais:
        return '*'
    else:
        return letra


    

with open('novo.txt', 'w') as arquivo:
    for letra in texto:
        arquivo.write(switch_vogal(letra))


arquivo = open('novo.txt', 'r')
print(arquivo.read())