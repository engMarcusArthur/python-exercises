n = int(input('Digite um número: '))
s = 0
if n != 1 and n > 0:
    for c in range(1, n + 1):
        if n % c == 0:
            s += 1
    if s == 2:
        print('{} é um número primo, pois é divisível apenas por 1 e por ele mesmo' .format(n, s))
    else:
        print('{} não é um número primo, pois foi divisível por {} números diferentes' .format(n, s))
elif n <= 0:
    if n == 0:
        print('0 não é um número primo')
    else:
        print('{} não é um número primo, pois é negativo' .format(n))
else:
    print('1 não é número primo')
