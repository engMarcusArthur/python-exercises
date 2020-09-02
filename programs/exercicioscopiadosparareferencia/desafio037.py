n = int(input('Digite um numero inteiro: '))
b = int(input('''Selecione a base para conversão:
1. Binário
2. Octal
3. Hexadecimal\n'''))

if b == 1:
    print('''DECIMAL PARA BINÁRIO
    {} = {}''' .format(n, bin(n)[2:]))
elif b == 2:
    print('''DECIMAL PARA OCTAL
    {} = {}''' .format(n, oct(n)[2:]))
elif b == 3:
    print('''DECIMAL PARA HEXADECIMAL
    {} = {}''' .format(n, hex(n)[2:]))
else:
    print('Valor inválido.')
