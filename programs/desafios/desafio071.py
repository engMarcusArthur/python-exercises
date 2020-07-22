c50 = c20 = c10 = 0
while True:
    saque = int(input('Valor do saque: R$ '))
    while saque != 0:
        print('\nEntregando cédulas:')
        c50 = saque // 50
        if c50 > 0:
            print(f'{c50} de R$ 50,00')
        saque -= c50 * 50
        c20 = saque // 20
        if c20 > 0:
            print(f'{c20} de R$ 20,00')
        saque -= c20 * 20
        c10 = saque // 10
        if c10 > 0:
            print(f'{c10} de R$ 10,00')
        saque -= c20 * 10
        if saque > 0:
            print(f'{saque} de R$ 1,00')
        break
    comand = ''
    while comand != 'S' and comand != 'N':
        comand = input('\nDeseja realizar mais alguma operação? [S/N] ').strip().upper()
        comand = comand[0]
    if comand == 'N':
        break
