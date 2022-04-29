"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas as nossas list Comprehension

"""

numeros = [n for n in range(1,7)]

par = [n for n in numeros if n % 2 == 0]
impar = [n for n in numeros if n % 2 != 0]

print(par, impar)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)


# Para matriz

m = [[1,2,3], [4,5,6], [7,8,9]]
[[print(valor) for valor in coluna ] for coluna in m]

# Gerando uma matriz simplificadamente

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]
print(tabuleiro)