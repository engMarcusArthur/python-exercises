prize = float(input('Preço do produto: R$ '))
cond = int(input('''Condição de pagamento:
1. À vista no dinheiro ou cheque
2. À vista no cartão
3. 2x no cartão
4. 3x ou mais no cartão\n'''))

if cond >= 1 and cond <= 4:
    if cond == 1:
        print('Você pagará à vista com dinheiro ou cheque, portanto tem direito à um desconto de 10%! O novo valor é R$ {:.2f}' .format(prize * 0.9))
    elif cond == 2:
        print('Você pagará à vista no cartão, portanto tem direito à um desconto de 5%! O novo valor é R$ {:.2f}' .format(prize * 0.95))
    elif cond == 3:
        print('Você pagará em até 2x no cartão, portanto o preço continuará R$ {:.2f}' .format(prize))
    else:
        print('Você parcelou a sua compra em mais de 2x, portanto, arcará com um juros de 20%. O novo valor integral será R$ {:.2f}' .format(prize * 1.2))
else:
    print('Comando inválido')
