from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
for i in range(1, 5):
    jogo[f'Jogador {i}'] = randint(1, 6)
rank = dict(sorted(jogo.items(), key = itemgetter(1), reverse = True))
print('Valores Sorteados:')
sleep(1)
for k, v in jogo.items():
    print(f"{k} tirou {v}")
    sleep(1)
print('\nRanking dos Jogadores: ')
sleep(1)
cont = 1
for k, v in rank.items():
    print(f"{cont}. {k} com {v}")
    sleep(1)
    cont += 1
