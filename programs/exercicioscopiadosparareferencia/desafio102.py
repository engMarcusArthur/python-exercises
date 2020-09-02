def linha():
    '''
    -> função para escrever uma linha na tela
    '''
    print('-' * 30)


def validacao(resp):
    '''
    -> função para verificar se a resposta do usuário é válida ou não
    :param resp: string digitada pelo usuário; previamente tratada, onde será considerada apenas a posição 0
    :return: auxiliará na saída do looping ou não, sendo que se o valor estiver em 'Ss' retornará True, e se estiver em 'Nn' retornará False
    '''
    if resp in 'Ss':
        return True
    elif resp in 'Nn':
        return False
    else:
        print('Por favor, responda com SIM ou NÃO')


def fatorial(n, show=False):
    '''
    -> função que calcula o fatorial de um numero
    :param f: numero que será fatorado
    :param show: valor bool dado pelo usuário, que permitirá para o programa mostra o calculo lógico ou apenas o resultado
    :return:
    '''
    f = 1
    for i in range(n, 0, -1):
        if show:
           print(i, end='')
           if i > 1:
               print(' x ', end='')
           else:
               print(' = ', end='')
        f *= i
    return f


linha()
fat = int(input('Digite um número: '))
while True:
    com = validacao(input('Deseja exibir o calculo lógico? [S/N] ').strip()[0])
    if com is True or com is False:
        break
print(fatorial(fat, com))
linha()
