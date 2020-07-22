def linha():
    print('=-' * 30)


def next():
    while True:
        global resp
        resp = input('Deseja continuar? [S/N] ').strip()[0]
        if resp in 'SsNn':
            break
        print('Resposta inválida. Tente Novamente')


def maior(valores):
    linha()
    print('''Analisando dados...
 - Os valores informados foram: ''', end='')
    for i in valores:
        print(f'{str(i): ^3}', end='')
    print(f'''\n - O total de valores informados foi {len(valores)}
 - O maior valor informado foi {max(valores)}''')


lista = list()

while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
    resp = ''
    next()
    if resp in 'Nn':
        break

maior(lista)
