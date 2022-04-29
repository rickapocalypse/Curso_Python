"""
Entendendo o *args

- o *args é um parâmetro, como outro qualquer. Isso significa que vc poderá chamar de qualquer coisal, desde que começe com asterísco

Exemplo

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados em 
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis

"""


"""
def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total
"""
#ou
"""
def soma(*args):
    print(sum(args))

soma(1,2,4,5,6)
"""

"""
def verfica(*args):
    if 'Henrique' in args and 'Apocalypse' in args:
        return f'bem-vindo {args[0]}'
    return f'Eu não sei quem é vc {args[0]} {args[1]}'

print(verfica('Henrique', 'Apocalypse'))
print(verfica('Leonardo', 'Eiji NOG'))

"""

def soma(*args):
    print(sum(args))

numeros = [1,2,3,4,5,6,7,8]

soma(*numeros)

# Desempacotador