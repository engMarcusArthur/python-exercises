num = list()
while True:
    num.append(int(int(input('Digite um número: '))))
    while True:
        com = input('Deseja continuar? [S/N] ').strip().upper()
        if com[0] == 'S' or com[0] == 'N':
            break
    if com[0] == 'N':
        print(f'A quantidade de numeros digitados foi {len(num)}, sendo que o número 5 ', end='')
        if 5 in num:
            print('foi digitado')
        else:
            print('não foi digitado')
        print(f'''A lista em ordem descrescente é {sorted(num, reverse=True)}''')
        break
