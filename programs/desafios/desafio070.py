total = valorcaro = valorbarato= 0
nomebarato = ''

while True:
    line = '#' * 100
    print(line)
    nome = input('Produto: ').strip().title()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        valorcaro += 1
    if preco < valorbarato:
        nomebarato = nome
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = input('Continuar compra? [S/N] ').strip().upper()
        continuar = continuar[0]
    if continuar != 'S':
        print(line)
        print(f'Foi gasto R$ {total:.2f} na compra, sendo que {valorcaro} produtos custaram mais de R$ 1000.00 e o produto mais barato foi {nomebarato}')
