import os

os.chdir('Exercicios_arquivos')

with open('cidades.txt', 'r') as arquivo:
    cidades = arquivo.readlines()

# o strip()

cidades_lista = {}
num_hab = 0

for n in range(len(cidades)):
    habitantes = int(cidades[n].split()[-1])
    cidades[n] = cidades[n].removesuffix('\n')
    if habitantes > num_hab:
        num_hab = habitantes
        cidade_mais_hab = cidades[n]


del(cidade_mais_hab.split()[-1])

# habitantes = cidade_mais_hab.split(' ').pop()
print(cidade_mais_hab)





