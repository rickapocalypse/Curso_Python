"""
Conjuntos é uma referencia a Teoria dos Conjuntos da matemática 

- São chamados de sets em Python
- Sets (conjuntos) não possuem valores duplicados
- Sets não possuem valores ordenados
- Sets não são acessados por índice 


Conjuntos são bons para armazenar elementos, mas sem ordenar eles, sem se preocupar com chave , valores e itens duplicados


Os Sets são referenciados em Python por {}

Diferença de Sets para dicionários 
    - Um dicionário tem chave:valor
    - Um conjunto tem apenas valor


# Definindo um conjunto:

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})

print(s)

# Convertendo para Set

p = set('henrique')

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

# Importante lembra que além de não termos valores duplicados, não temos ordem


# Listas aceitam valores duplicados
lista = [99, 2, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista}')

# Tuplas aceitam valores duplicados
tupla = (99, 2, 34, 23, 12, 1, 44, 5)
print(f'Tupla: {tupla}')

# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario}')

#Conjuntos não aceitam valores duplicados
s = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {s}')



# Usos interessantes com sets

# Imagine que fizemos umn formulário de cadastro de visitantes em uma feira
# Os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, já que uma lista podemos
# adicionar novos e ter repetição

cidade = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
          'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

# Quantas pessoas vieram ?
print(len(cidade))

# De quais cidades vieram ?
print(set(cidade))

# Quantas cidades únicas foram ?
print(len(set(cidade)))




# Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
print(s)

# Remover elementos em um conjunto

s.remove(3)
print(s)

# copiando um conjunto

novo = s.copy()


# Removendo todos os itens de um conjunto

s.clear()

"""


# Métodos Matemáticos de Conjuntos

estudantes_python = {'Marcos', 'Patricia',
                     'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Estudantes unicos do curso

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# ou

unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Estudantes que estudando nos dois cursos

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# ou

ambos2 = estudantes_java & estudantes_python
print(ambos2)


# Estudantes que só fazem um dos cursos

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# soma*, max*, min*, len* é igual a listas, tuplas e dicionários
