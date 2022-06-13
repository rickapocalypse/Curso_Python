import os 
from datetime import date
os.chdir('Exercicios_arquivos')


with open('nome_data.txt', 'r') as arquivo:
    lines = arquivo.read()

year = int(str(date.today()).split()[0][0:4])

lines = lines.split('\n')

for n in range(len(lines)):
    if int(lines[n].split()[-2]) <= int(str(date.today()).split()[0][5:7]) and int(lines[n].split()[-2]) <= int(str(date.today()).split()[0][8:10]):
        print(f'{lines[n].split()[0]} tem {year - int(lines[n].split()[-1])} anos')
    else:
        print(f'{lines[n].split()[0]} tem {year - int(lines[n].split()[-1]) - 1} anos')