extenso = 'zero', 'um', 'dois', 'três', 'quatro', \
          'cinco', 'seis', 'sete', 'oito', 'nove', \
          'dez', 'onze', 'doze', 'treze', 'quatorze', \
          'quinze', 'dezesseis', 'dezessete', 'dezoito', \
          'dezenove', 'vinte'
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {extenso[n].upper()}')
    while True:
        com = input('Deseja continuar?[S/N] ').strip().upper()
        if com[0] == 'S' or com[0] == 'N':
            break
        print('Tente novamente. ', end='')
    if com[0] == 'N':
        break
