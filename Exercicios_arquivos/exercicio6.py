import os
os.chdir('Exercicios_arquivos')

letra_quantidade = {}
print(letra_quantidade)
with open('exemplo.txt', 'r') as arquivo:
    texto = arquivo.read()
    texto = texto.lower()
    for letra in texto:
        if letra in letra_quantidade:
            letra_quantidade[letra] += 1
        else:
            letra_quantidade[letra] = 1
print(letra_quantidade)
