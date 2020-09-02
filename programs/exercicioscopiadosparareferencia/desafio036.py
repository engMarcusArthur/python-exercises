house = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
parc = int(input('Parcelas anuais: '))
mens = house / parc / 12

if mens <= sal * 0.3:
    print('Valor da mensalidade: R$ {:.2f}' .format(mens))
else:
    print('''EMPRÉSTISMO NEGADO!
O valor da mensalidade seria R$ {:.2f}, excedendo, assim, 30% do salário de R$ {:.2f}''' .format(mens, sal))
