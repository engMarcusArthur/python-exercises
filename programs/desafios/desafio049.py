n1 = int(input('Digite um numero inteiro qualquer: '))
print('TABUADA DE {}' .format(n1))

for i in range(0, 10 + 1):
    print('{} x {} = {}' .format(i, n1, n1 * i))
print('\nFIM')
