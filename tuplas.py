"""
Tuplas (tuple)

Tuplas são bastantes parecidas com listas. 
Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por parenteses ()
2 - As tuplas são imutaveis, isso significa que ao se criar uma tupla, ela não muda. Toda operação em uma tupla gera outra tuplar. 


#Cuidados: AS Tuplas são representadas por parenteses mas:

tupla1 = (1, 2, 3, 4, 5, 6)

tupla2 = 1, ,2 ,3 ,4 ,5 ,6

tupla3 = (4,)

tupla4 = 4,

São tuplas

"""

"""
Criando uma tupla em um range
tupla = tuple(range(11))   #Criando uma tupla de 0 a 10
"""

"""
Desempacotamento

tuple ('geek university', 'Programação em Python: Essencial')
escola, curso = tupla
"""


# Métodos para adição e remoção de elementos nas tuplas não existem (São imutaveis)
"""
sum(tupla)
max(tupla)
min(tupla)
len(tupla)


tupla = (0, 5, 6, 88, 17, 2, 1)

for indice, n in enumerate(tupla):
    print(indice, n)


# Contando elementos de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'f')
print(tupla.count('c'))
tupla = ("a", "b", "e", "f", "g", "h", "h", "p", 'p', 'p', 'p')
print(tupla.count('p'))


"""

# Usamos tupla quando não precisamos modificar os dados que nela estão

"""
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez')

# Acesso de elementos na tupla é semelhante a lista

print(meses[5 - 1])
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez')

# verificando em qual índice um elemento está na tupla

# Qual o índice que a string 'mai' está, contando a partir do indice 7
print(meses.index('mai', 4) + 1)
# tupla[inicio:fim:passo]
print(meses[0:6])

"""

# Tuplas são mais rapidas do que listas. E mais segurança para o código

# Copiando uma tupla para outra não temos problema de Shallow Copy
