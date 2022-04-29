'''
Modulo Collections - Counter

Collections -> high-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
com um dicionario, contendo como chave o elemento da lista passada como parâmetro e como o 
valor a quantidade de ocorrência desse elemento.


# Utilizando o Counter

from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 5, 5, 53, 3, 3, 34, 45, 45, 66, 66, 43, 34]

res = Counter(lista)
print(res)

# O Counter conta cada elemento da lista, criando uma chave com o elemento e numero de ocorrência como valor


# Para strings
from collections import Counter

print(Counter('Henrique'))


'''

from collections import Counter

texto = """
Máquina térmica, em termodinâmica, é aquela integrada num sistema que realiza 
a conversão de calor em trabalho mecânico.
Isto se dá quando uma fonte de calor leva uma substância de trabalho de um estado 
de baixa temperatura para um estado de temperatura mais alta.
"""

palavras = texto.split()
print(palavras)


res = Counter(palavras)
print(res)

# Encontrando as palavras que mais ocorrem no texto
print(res.most_common(5))
