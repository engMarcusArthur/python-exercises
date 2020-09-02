print('PROGRESSÃO ARITMÉTICA')
a1 = float(input('Digite o primeiro termo da progressão: '))
r = float(input('Digite a razão da progressão: '))
print('EXIBINDO OS 10 PRIMEIROS TERMOS DA PA')

for n in range(1, 10 + 1):
    print(a1 + (n - 1) * r, end = ' - ')
print('FIM')
