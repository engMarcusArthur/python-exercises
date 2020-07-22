n1 = 0
n2 = 0
op = 1
while op != 5:
    op = int(input('''\nSelecione uma das opções:
1. Somar
2. Multiplicar
3. Maior
4. Novos números
5. Sair\n'''))

    if op == 1:
        print(n1 + n2)
    elif op == 2:
        print(n1 * n2)
    elif op == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif op == 4:
        n1 = float(input('\nDigite um valor: '))
        n2 = float(input('Digite um valor: '))
    elif op == 5:
        print('\nFIM')
    else:
        print('\nValor inválido')
