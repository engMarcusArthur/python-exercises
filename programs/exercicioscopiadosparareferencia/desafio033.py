n1 = int(input('Digite um numero: '))
n2 = int(input('Outro numero: '))
n3 = int(input('Outro numero: '))

if n1 > n2 > n3:
    print('{} é o maior e {}, o menor' .format(n1, n3))
if n1 > n3 > n2:
    print('{} é o maior e {}, o menor' .format(n1, n2))
if n2 > n1 > n3:
    print('{} é o maior e {}, o menor' .format(n2, n3))
if n2 > n3 > n1:
    print('{} é o maior e {}, o menor' .format(n2, n1))
if n3 > n2 > n1:
    print('{} é o maior e {}, o menor' .format(n3, n1))
else:
    print('{} é o maior e {}, o menor' .format(n3, n2))
