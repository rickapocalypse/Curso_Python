def soma(num1,num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def produto(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def operacao(num1, num2, fun):
    if fun == '-':
        fun = subtracao
    elif fun == '+':
        fun = soma 
    elif fun == '*':
        fun = produto
    elif fun == '/':
        fun = div
    return fun(num1, num2)



print(operacao(1,2, '*'))