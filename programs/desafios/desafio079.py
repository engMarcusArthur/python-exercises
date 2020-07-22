num = list()
while True:
    while True:
        v = int(input('Digite um valor: '))
        if v in num:
            print('O valor já foi digitado. Por favor, tente novamente')
        else:
            num.append(v)
            print('Valor adicionado com suceeso')
            break
    com = ' '
    while com[0] != 'S' and com[0] != 'N':
        com = input('Deseja continuar? [S/N] ').strip().upper()
    if com[0] == 'N':
        print(f'Os valores digitados foram {sorted(num)}')
        break
