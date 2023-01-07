import string
p = 0
maior = 0
menor = 1_000_000_000


num = input('Informe numeros para serem somados, no final, apenas digite (final) ')
currect = string.ascii_letters
status = False

for caracteres in num:
    if caracteres not in currect:
        status = True
if status == False:
    print('O programa encerrou')

if status:
    while p < 10 :

        d = num

        if d == 'final':
            print(f'O programa encerrou, maior numero é {maior} e o menor é {menor}')
            break
        elif d in currect:
            print(f'Insira, uma variavel valida mas, programa encerrou, maior numero é {maior} e o menor é {menor} ')
            break
        else:
            x = int(d)
            if x >= maior:
                maior = x
            if x <= menor:
                menor = x

        c = input('Informe numeros para serem somados, no final, apenas digite (final) ')

        if c == 'final':
            print(f'O programa encerrou, maior numero é {maior} e o menor é {menor}')
            break
        elif c in currect:
            print(f'Insira, uma variavel valida mas, programa encerrou, maior numero é {maior} e o menor é {menor} ')
            break
        else:
            x = int(c)
            if x >= maior:
                maior = x
            if x <= menor:
                menor = x

 






