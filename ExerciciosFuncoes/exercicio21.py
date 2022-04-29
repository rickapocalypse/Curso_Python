def numPrimo(*arg):
    for n in arg:
        pontos_de_divisao = 0
        for i in range(1,n):
            if n % i == 0:
                pontos_de_divisao += 1
        if pontos_de_divisao <= 1:
            print(n)            
  
numPrimo(1,2,3,4,5,6,7,8,9,10)