"""
Sorted

Sorted != sort()

sort() funciona apenas em listas.
sorted() funciona em qualquer iterável, retornando uma lista ordenada.


list = [1, 2, 3, 4, 5,0]
list.sort()
print(list)
#Ordenação de listas

numeros = [6,1,2,3,4,5]

print(sorted(numeros))
print(sorted(numeros, reverse=True))

print(usuario)
# ordenando por username
print(sorted(usuario, key=lambda u: u['username']))

# ordenando por tweets
print(sorted(usuario, key=lambda u: len(u['tweets']))) 
"""

usuario = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}

]

