"""
Any e All  

all() -> Retorna True se todos os elementos de uma lista são True.
any() -> Retorna True se qualquer elemento de uma lista é True.

print(all([1,2,3,4,5]))
print(all([0,2,3,4,5]))


nomes = ['Joao', 'Jaria', 'Jose', 'Joana']

print(all([nome[0] == 'J' for nome in nomes]))

print(all(letra for letra in 'eio' if letra in 'aeiou')) 

print(all([num for num in [2,4,6,8,10] if num % 2 == 0]))

"""

