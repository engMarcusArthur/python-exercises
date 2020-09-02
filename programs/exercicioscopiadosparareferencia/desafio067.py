print('Tabuada')
while True:
    n = int(input('De qual número deseja ver a tabuada? Digite negativo para encerrar: '))
    i = 0
    linha = '=' * 12
    print(linha)
    for i in range (0, 10 + 1):
        print(f'{i} x {n} = {i * n}')
    print(linha)
    if n < 0:
        print('Encerrando o programa')
        break
print('programa encerrado')
