n = int(input('Digite um numero de 0 a 9999: '))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}''' .format(n // 1 % 10, n // 10 % 10, n // 100 % 10, n // 1000 % 10))
