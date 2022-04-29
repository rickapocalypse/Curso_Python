l1 = float(input('informe o primeiro lado do triângulo'))
l2 = float(input('informe o segundo lado do triângulo'))
l3 = float(input('informe o terceiro lado do triângulo'))

if l1 == l2 :
    if l1 != l3 :
        print('É um triângulo isosceles')
    else:
        print('É um triângulo equilátero') 
elif l1 == l3 :
    if l1 != l2 :
        print('É um triângulo isosceles')
    else:
        print('É um triângulo equilátero') 
elif l2 == l3 :
    if l2 != l1 :
        print('É um triângulo isosceles')
    else:
        print('É um triângulo equilátero')
else:
    print('O triângulo é escaleno')
