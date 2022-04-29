
fimDoLoop = 20
casas = 100

vs = 2.63

def eq1(ra, rb, rc):
    return ((1/(1+(42.7818/ra)) - (1/(1+(rc/rb))))) * vs

def eq2(ra, rb, rc):
    return ((1/(1+(17.8188/ra)) - (1/(1+(rc/rb))))) * vs - 0.5

def eq3(ra, rb, rc):
    return ((1/(1+(8.2321/ra)) - (1/(1+(rc/rb))))) * vs - 1
print('========= começando =========')
with open('dados.txt', 'w') as arquivo:
    for na in range(1, fimDoLoop * casas):
        na /=  casas
        print(f'\r {round((na)*100, 2)}%' , end = '')
        for nb in range(1, fimDoLoop * casas):
            nb /= casas
            for nc in range(1,fimDoLoop * casas):
                nc /= casas
                if round(eq1(na,nb,nc), 3) == 0.00 and round(eq2(na,nb,nc), 3) == 0.00 and round(eq2(na,nb,nc), 3) == 0.00:
                    arquivo.write(f'{na} / {nb} / {nc} .\n')

print('========= Terminou o Processo =========')