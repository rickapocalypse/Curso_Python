'''
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer, no nosso código. Prevenindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // execução problemática
except:
    // tratamento do erro

Toda entrada do usuario deve ser tradada.

Else -> é executado se não ocorrer nenhum erro.
'''


try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Você não digitou um número!")
else:
    print(f"Você digitou o número {num}.")


def divide(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Existe um problema no: {err}"
print(divide(2, 0))