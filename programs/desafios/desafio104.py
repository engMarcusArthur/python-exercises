def linha():
    '''
    -> Função que imprime uma linha
    '''
    print('~~' * 15)


def leiaInt(msg):
    '''
    -> função que le uma entrada do usuario até que ela seja um valor inteiro
    :param num: frase do input
    :return: global n
    '''
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mDado não informado\033[m')
            n = 0
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um valor inteiro valido\033[m')
            continue
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um valor real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mDado não informado\033[m')
            n = 0
        else:
            return n


linha()
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaReal('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {inteiro} e o real {real}')
linha()
