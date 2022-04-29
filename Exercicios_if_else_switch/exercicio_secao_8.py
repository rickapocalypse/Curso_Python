num = int(input('Informe 3 números '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10

if u > d :
    if d > c :
        print (f'{c} {d} {u}')
    elif c > d :
        print (f'{d} {c} {u}')
    else:
        print (f'{d} {d} {u}')
elif d > c :
    if c > u :
        print(f'{u} {c} {d}')
    elif u > c :
        print(f'{c} {u} {d}')
    else:
        print(f'{c} {c} {d}')
elif c > u :
    if u > d :
        print(f'{d} {u} {c}')
    elif d > u :
        print(f'{u} {d} {c}')
    else:
        print(f'{u} {u} {c}')
else :
    print (f' {u} {u} {u}')
