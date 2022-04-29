'''
Map

Com map fazemos mapeamento de valores para função
'''
import math

def area(r):
    return  math.pi * r **2

print(area(2))

raios = [2,5,7,0.3,10,44]

# Map é uma função que recebe dois parametros: o primeiro é uma função, o segundo é iterável  

areas = map(area, raios)

print(list(areas))

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Lós Angeles', 26), ('Tokio', 27),
('Nova York', 28), ('Londres', 22)]

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32 )

print(list(map(c_para_f, cidades)))



