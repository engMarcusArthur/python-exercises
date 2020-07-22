s = 0
qtd = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        qtd += 1
    else:
        print('Foram digitados {} números, sendo a soma entre eles {}' .format(qtd, s))
