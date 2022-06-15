import os 
os.chdir('Exercicios_arquivos')

with open('aluno_nota.txt', 'r') as arquivo:
    lines = arquivo.read()

def complete_name(name):
    if len(name) < 40:
        for space in range(40 - len(name)):
            name += '_'
    return name

organizer_grade = []
organizer_student = lines.split('\n')
for item in lines.split('\n'):
    item = item.split(' ')
    organizer_grade.append(item[-1])

organizer_grade.sort()

for item in lines.split('\n'):
    item = item.split(' ')
    organizer_student[organizer_grade.index(item[-1])] = item

