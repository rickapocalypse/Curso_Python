"""
Generators


# list comprehension

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Julia']

res = [nome[0] == "C" for nome in nomes]
print(res)

# generator

res = (nome[0] == "C" for nome in nomes)
print(res)

generator são muito mais rápidos que list comprehension.

"""
