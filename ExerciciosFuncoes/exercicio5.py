import math
r = int(input('Quanto o tamanho do raio da esfera em metros ? '))

def volume_esfera(r):
    v = (4/3) * (math.pi) * (r**3)
    print(v)

volume_esfera(r)