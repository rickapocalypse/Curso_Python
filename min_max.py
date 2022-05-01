nomes = ['ana', 'joao', 'maria', 'pedro', 'jose', 'henrique']

print(max(nomes))
print(max(nomes, key=lambda n: len(n)))


musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 1},
    {'titulo': 'Nothing else matters', 'tocou': 4},
    {'titulo': 'The Unforgiven', 'tocou': 5},
    {'titulo': 'Enter Sandman', 'tocou': 3}
]

print(max(musicas, key=lambda m: m['tocou'])['titulo'])