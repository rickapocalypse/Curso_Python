import os 
os.chdir('Exercicios_arquivos')

with open('aluno_nota.txt', 'r') as arquivo:
    lines = arquivo.read()

def complete_name(name):
    if len(name) < 40:
        for space in range(40 - len(name)):
            name += '_'
    return name

lines = lines.split('\n')

grade = []
students = []
print(f'Essa materia tem {len(lines)} alunos')
print(lines)

for student in lines:
    students.append(complete_name(student.split(' ')[1]))
    grade.append(float(student.split(' ')[-1]))

print(students)
print(grade)

print(f'O aluno {students[grade.index(max(grade))]} tem a maior nota {max(grade)}')