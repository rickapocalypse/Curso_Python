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

cidade_mais_hab=cidade_mais_hab.split()[0:-1]
cidade_mais_hab_string = ' '.join(cidade_mais_hab)
print(f'{cidade_mais_hab_string}, tem um total de {num_hab} habitantes')




