def linha():
    '''
    -> Função que escreve uma linha
    '''
    print('-' * 30)


def verificaG(gol):
    '''
    ->  função que verifica se a entrada do usuário pode ser um inteiro ou não para o numero de gols
    :param gol: string com o numero de gols, informada pelo usuario
    :return: retorna gol após validado. caso ele seja um numero, retorna-o como int, senão, retorna 0
    '''
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    return gol


def ficha(nome='desconhecido', gols=0):
    '''
    -> função que exibe, dentro de um print, o nome do jogador e seu numero de gols no campeonato
    :param nome: nome do jogador - opcional
    :param gols: gols marcados - opcional
    :return: literal, informando o nome do jogador e o numero de gols
    '''
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


#Main
linha()
n = input('Nome do Jogador: ').strip().title()
g = verificaG(input('Número de Gols: '))
if n == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
linha()
