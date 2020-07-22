jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ').strip().title()
    while True:
        tot = int(input(f"Número de partidas jogadas por {jogador['nome']}: "))
        if tot < 0:
            print(f'O valor {tot} é inválido. Por favor, tente novamente, com valores iguais ou maiores à 0')
        else: break
    if tot == 0:
        jogador['gols'] = jogador['total'] = 0
    else:
        for c in range(0, tot):
            while True:
                partidas.append(int(input(f'Gols na partida {c + 1}: ')))
                if partidas[-1] < 0:
                    partidas.pop()
                    print(f'Por favor, digite apenas números inteiros não negativos')
                else:
                    break
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    while True:
        resp = input('Deseja continuar cadastrando? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Resposta inválida. Tente novamente')
    if resp == 'N':
        break
print('=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print(f'\n{"-" * 40}')
for k, v in enumerate(time):
    print(f'{k:>3}. ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    while True:
        perg = input('Deseja visualizar detalhes de algum jogador? [S/N] ').strip().upper()[0]
        if perg in 'SN':
            break
        print('ERRO!. Porfavor, responda apenas com sim ou não')
    if perg == 'N':
        break
    while True:
        busca = int(input('Digite o código do jogador: '))
        if busca < len(time):
            break
        print(f'Código inválido! Tente novamente, com um valor entre 0 e {len(time) - 1}')
    print(f"Detalhamento do número de gols do jogador {time[busca]['nome']}")
    for i, g in enumerate(time[busca]['gols']):
        print(f' - {i + 1}ª partida: {g} gols.')
    print('=' * 40)
print('>>>FIM<<<')
