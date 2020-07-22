num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    if num[-1] % 2 == 0:
        par.append(num[-1])
    else:
        impar.append(num[-1])
    while True:
        com = input('Deseja continuar? [S/N] ').strip().upper()
        if com[0] == 'S' or com[0] == 'N':
            break
    if com[0] == 'N':
        print(f'Foram digitados {num}, sendo que os valores pares são {par} e os ímpares, {impar}')
        break
