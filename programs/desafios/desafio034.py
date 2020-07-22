sal = float(input('Digite o seu salário: R$ '))

print('NOVO SALÁRIO')
if sal > 1250:
    print('R$ {:.2f}' .format(sal * 1.1))
else:
    print('R$ {:.2f}' .format(sal * 1.15))