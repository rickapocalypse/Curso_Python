import os 
os.chdir('Exercicios_arquivos')

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

with open('exemplo_junto.txt', 'r') as arquivo:
    lines = arquivo.read()

lines = toBinary(lines)
lines = ' '.join(str(i) for i in lines)

with open('binary.txt', 'w') as arquivo:
    arquivo.write(lines)

