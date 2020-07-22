print('PROGRESSÃO ARITMÉTICA')
a1 = float(input('Digite o primeiro termo da progressão: '))
r = float(input('Digite a razão da progressão: '))
print('\nEXIBINDO OS 10 PRIMEIROS TERMOS DA PA')
cont = 0

while cont < 10:
    res = a1 + r * cont
    print(res, end = '  ')
    cont += 1
n = int(input('\nDeseja visualizar mais quantos termos? '))
n += 10
if n != 0:
    while cont < n:
        res = a1 + r * cont
        print(res, end = '  ')
        cont += 1
else:
    print('FIM')
    