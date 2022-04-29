'''
Filter

filter() -> Serve para filtrar dados de uma determinada coleção 

valores = 1, 2, 3, 4, 5, 6   # Uma tupla

media = sum(valores)/ len(valores)

print(media)

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, 0.1]

# calculando a média pela biblioteca

media = statistics.mean(dados)

# Assim como map, a função filter recebe dois parametros, sendo uma função e um iterável
# O filter retorna um iterável com os valores que passaram no teste, com retorno de verdadeiro
res = filter(lambda x: x > media, dados)
print(list(res))

# Filtro para eliminar dados em branco

paises = ['', 'Argentina', '', 'Brasil', '', '', 'Chile', 'Colombia', 'Equador','','','Venezuela']

print(paises)
# A função none no filter serve para filtrar os dados em branco
res = filter(None, paises)
print(list(res))

# map() -> recebe dois parámetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
# Filter() -> Recebe doi parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

usuario = [
    {'usernamoe': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'usernamoe': 'carla', 'tweets': ['Eu amo meu gato']},
    {'usernamoe': 'jeff', 'tweets': []},
    {'usernamoe': 'bob123', 'tweets': []},
    {'usernamoe': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'usernamoe': 'gal', 'tweets': []}

]

# Filtrar os usuários que estão inativos no tt

print(usuario)

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuario))

print(inativos)


'''

# Exemplo mais complexo

nomes = ['Vanessa', 'Ana', 'Maria']

print(list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) > 5, nomes))))
