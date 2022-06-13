import os 
os.chdir('Exercicios_arquivos')
input_user = '1'

def format_number(number):
    num = '(' + number[0:2] + ')' + number[2:6] + '-' + number[6:]
    return num
        
# with open ('lista_telefonica.txt', 'w') as arquivo:
#     while input_user != '0':
#         input_user = str(input(f'Digite o nome: '))
#         arquivo.write(input_user + '\n')
#         input_user = str(input(f'Digite o número: '))
#         arquivo.write(input_user + '\n')
#         input_user = str(input(f'Deseja encerar ? Digite "1" para continuar e "0" para encerar: '))

with open('lista_telefonica.txt', 'r') as arquivo:
    lines = arquivo.read()


lines = lines.split()
list_names_fones = {}

for n in range(len(lines)):
    if n % 2 == 0:
        list_names_fones[lines[n]] = format_number(lines[n+1])

print(list_names_fones)