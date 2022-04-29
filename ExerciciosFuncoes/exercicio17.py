import itertools


def SomaDosNumeros(num1, num2):
    for n1, n2 in zip(str(num1), str(num2)):
        print(int(n1) + int(n2))
        


SomaDosNumeros(52000,10545)