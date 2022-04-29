def consumo(km, l):
    consunno = km / l

    if consunno < 8:
        print('Venda o carro')
    elif consunno > 8 and consunno < 14:
        print('Económico')
    else:
        print('Super Económico')


consumo(10,1)