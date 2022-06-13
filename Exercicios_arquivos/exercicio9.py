import os
os.chdir('Exercicios_arquivos')

with open('exemplo.txt', 'r') as arquivo:
    texto = arquivo.read()
with open('exemploUP.txt', 'r') as arquivo:
    textoUP = arquivo.read()

with open('exemplo_junto.txt', 'w') as arquivo:
    arquivo.write(texto)
    arquivo.write(textoUP)
print(open('exemplo_junto.txt', 'r').read())