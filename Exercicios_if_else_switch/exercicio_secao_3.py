num1 = float(input('Informe a primeira nota do aluno'))
num2 = float(input('Informe a segunda nota do aluno'))

import math

if num1 < 0 : 
    print(f"A nota informada não é valida. Por favor, informe uma nota de 0 a 10")
elif num2 < 0 :
    print(f"A nota informada não é valida. Por favor, informe uma nota de 0 a 10")
elif num1 > 10 :
    print(f"A nota informada não é valida. Por favor, informe uma nota de 0 a 10")
elif num2 > 10 :
    print(f"A nota informada não é valida. Por favor, informe uma nota de 0 a 10")
else:
    print(f'A nota é {(num1+num2)/2}')




