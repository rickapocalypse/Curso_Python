"""
Dictionary Comprehension

{chave:valor for valor in iterável}
"""

num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

quadrado = {chave : valor ** 2 for chave,valor in num.items()}

print(quadrado)

num = [1,2,3,4,5]
alf = ['a','b','c','d','e']
quadrado = {valor : valor for valor in num}
print(quadrado)

dicionario = {alf[i] : num[i] for i in range(len(alf))}
print(dicionario)

res = {n : ('par' if n % 2 ==0 else 'impar') for n in num}
print(res)