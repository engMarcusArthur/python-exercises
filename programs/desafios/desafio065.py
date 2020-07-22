qtd = 0 ### quantidade de numeros
big = 0
little = 0
s = 0
com = 'S'
while com == 'S':
    n = int(input('Digite um número inteiro: '))
    qtd += 1
    s += n
    if n > big:
        big = n
    elif n < little:
        little = n
    com = input('Deseja informar mais valores? (S/N)\n').strip().upper()
    while com != 'S' and com != 'N':
        com = input('Informe novamente: ').strip().upper()
    if com == 'N':
        print('O maior número foi {}, e o menor, {}.  a média entre os valores é {:.1f}' .format(big, little, s/qtd))
