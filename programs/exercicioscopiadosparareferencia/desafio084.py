lista = list()
dados = list()
pmen = pmai = 0
while True:
    dados.append(input('Nome: ').strip().title())
    dados.append(float(input('Peso: (Kg) ')))
    if dados[-1] > pmai:
        pmai = dados[-1]
    if dados[-1] < pmen or pmen == 0:
        pmen = dados[-1]
    lista.append(dados[:])
    dados.clear()
    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp[0] == 'S' or resp[0] == 'N':
            break
    if resp[0] == 'N':
        print(f'{len(lista)} pessoas foram cadastras. A(s) pessoa(s) mais pesada(s) tinha(m) {pmai:.3f} Kg, sendo ele(s): ', end='')
        for i in lista:
            if i[1] == pmai:
                print(f'{i[0]}', end='...')
        print(f'e a(s) mais leve(s), que pesava(m) {pmen:.3f} Kg, era(m): ', end='')
        for i in lista:
            if i[1] == pmen:
                print(f'{i[0]}', end='...')
        break
print()
