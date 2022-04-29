def nTriangulo(num):

    for n in range(1 , 2*num ):

        if n <= num:
            print(n * '*')
        else:
            print((2*num - n) * '*')
nTriangulo(10)