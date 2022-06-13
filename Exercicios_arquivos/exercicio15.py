import os
from datetime import date
os.chdir('Exercicios_arquivos')

year = int(str(date.today()).split()[0][0:4])
month = int(str(date.today()).split()[0][5:7])
day = int(str(date.today()).split()[0][8:10])


with open('nome_data.txt', 'r') as arquivo:
    lines = arquivo.read()

lines = lines.split('\n')

for user in range(len(lines)):
    born = int(lines[user].split()[-1])
    month_born = int(lines[user].split()[-2])
    day_born = int(lines[user].split()[-3])
    if year - born > 18:
        print(f'{lines[user].split()[0]} é maior de idade')
    elif year - born == 18:
        print(f'{lines[user].split()[0]} está entrando na maior idade')
    else:
        print(f'{lines[user].split()[0]} é menor de idade')