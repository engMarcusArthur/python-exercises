n = int(input('Quantos termos deseja visualizar? '))
n1 = 1
n0 = 0
cont = 0
while cont < n:
    print(n0, end = ' ')
    num = n0 + n1
    n0 = n1
    n1 = num
    cont += 1
