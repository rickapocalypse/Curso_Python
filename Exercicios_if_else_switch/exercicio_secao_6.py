ano = int(input('informe o ano '))

c = ano // 1 % 10
d = ano // 10 % 10

if ano % 4 == 0 :
    if ano % 100 != 0 :
        print(f'O ano {ano} é bissexto')
    elif c == 0 :
        if d ==0 :
            print(f'o ano {ano} é bissexto')
        else:
            print(f'o ano {ano} não é bissexto')
    else:
        print(f'o ano {ano} não é bissexto')
else:
    print(f'o ano {ano} não é bissexto')

