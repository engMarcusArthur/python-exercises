from random import randint
from time import sleep
jogos = list()
bet = int(input('Quantos jogos deseja visualizar? '))
for nbet in range(0, bet):
    jogos.append([nbet])
    jogos[nbet].pop()
    for dez in range(0, 6):
        while True:
            v = randint(1, 60)
            if v not in jogos[nbet]:
                jogos[nbet].append(v)
                break
        jogos[nbet].sort()
sleep(0.5)
print('Os números sorteados foram:', end='')
for pos, nums in enumerate(jogos):
    sleep(1)
    print(f'\nJogo {pos + 1}:', end=' ')
    for n in nums:
        sleep(1)
        print(n, end=' ')
