c = 1
A = []
while c < 7:
    valor = int(input(f'Informe um numero inteiro em um total de 6. {c}/6 '))
    A.append(valor)
    c += 1

print(A)

soma = A[0] + A[1] + A[5]

print(soma)


A[3] = 100

print(A)

for n in A:
    print(n)
