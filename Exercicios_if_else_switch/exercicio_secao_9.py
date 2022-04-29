h = float(input('Informe a altura'))
kg = float(input('Informe o peso'))

if h < 1.2 :
    if kg < 60 :
        print('A')
    elif 60 <= kg <= 90 :
        print('D')
    else:
        print('G')
elif 1.2 <= h <= 1.7 :
    if kg < 60 :
        print('B')
    elif 60 <= kg <= 90 :
        print('E')
    else:
        print('H')
elif h > 1.7:
    if kg < 60 :
        print('C')
    elif 60 <= kg <= 90 :
        print('F')
else:
    print('I')